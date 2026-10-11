"""List what the operator typed, across every Claude Code project, since a date.

    python operator_messages.py 2026-08-11 [--here <project-dir-fragment>] [--limit N] [--out FILE]

Reads the session transcripts under ~/.claude/projects, keeps only messages a person
typed (no tool results, no subagent turns, no injected reminders), and writes them
grouped by project with a few counts on top. The transcripts are large; this is the cheap
way to read them.
"""
import argparse
import collections
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone

MAX_CHARS = 400
WRAPPER = re.compile(r"<(system-reminder|command-name|command-message|command-args|local-command-stdout|"
                     r"task-notification|pasted_content)\b.*?(</\1>|$)", re.S)


def typed_text(entry):
    if entry.get("type") != "user" or entry.get("isSidechain") or entry.get("isMeta"):
        return None
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, list):
        if any(b.get("type") == "tool_result" for b in content if isinstance(b, dict)):
            return None
        content = " ".join(b.get("text", "") for b in content
                           if isinstance(b, dict) and b.get("type") == "text")
    if not isinstance(content, str):
        return None
    text = WRAPPER.sub("", content).strip()
    if not text or text.startswith(("[Request interrupted", "Caveat:", "Base directory for this skill")):
        return None
    return text


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("since")
    ap.add_argument("--here", help="only project folders whose name contains this")
    ap.add_argument("--limit", type=int, help="keep only the N projects with the most typed messages")
    ap.add_argument("--out", default="operator-messages.txt")
    args = ap.parse_args()
    since = datetime.fromisoformat(args.since).replace(tzinfo=timezone.utc)

    root = os.path.join(os.path.expanduser("~"), ".claude", "projects")
    by_project = collections.defaultdict(list)
    seen = set()  # a resumed or forked session repeats its earlier lines
    for path in glob.glob(os.path.join(root, "*", "*.jsonl")):
        if os.path.getmtime(path) < since.timestamp():
            continue
        if args.here and args.here.lower() not in path.lower():
            continue
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if '"type":"user"' not in line:
                    continue
                try:
                    entry = json.loads(line)
                except ValueError:
                    continue
                text = typed_text(entry)
                stamp = entry.get("timestamp")
                if not text or not stamp:
                    continue
                when = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
                if when < since or (stamp, text) in seen:
                    continue
                seen.add((stamp, text))
                project = os.path.basename((entry.get("cwd") or os.path.dirname(path)).rstrip("\\/"))
                by_project[project].append((when, text))

    found = len(by_project)
    if args.limit:
        by_project = dict(sorted(by_project.items(), key=lambda kv: -len(kv[1]))[:args.limit])
    every = [m for msgs in by_project.values() for m in msgs]
    if not every:
        sys.exit("no operator messages found since " + args.since)
    lengths = sorted(len(t) for _, t in every)
    short = collections.Counter(t.lower().strip(" .!") for _, t in every if len(t) <= 40)
    hours = collections.Counter(w.astimezone().strftime("%H") for w, _ in every)

    with open(args.out, "w", encoding="utf-8") as out:
        out.write(f"# {len(every)} typed messages in {len(by_project)} project folder(s) since {args.since}"
                  + (f" (top {args.limit} of {found} by message count)" if found > len(by_project) else "") + "\n")
        days = collections.Counter(w.astimezone().strftime("%Y-%m-%d") for w, _ in every)
        busiest_day, busiest_n = days.most_common(1)[0]
        out.write(f"# active on {len(days)} day(s); busiest {busiest_day} with {busiest_n} messages; "
                  f"{sum(1 for _, t in every if t.rstrip().endswith('?'))} end in a question mark\n")
        out.write(f"# median length {lengths[len(lengths) // 2]} chars; "
                  f"{sum(1 for n in lengths if n <= 20)} of them are 20 chars or fewer\n")
        out.write("# busiest local hours: " + ", ".join(f"{h}:00 x{n}" for h, n in hours.most_common(5)) + "\n")
        out.write("# most repeated short messages: " +
                  "; ".join(f"{t!r} x{n}" for t, n in short.most_common(15) if n > 1) + "\n")
        for project, msgs in sorted(by_project.items(), key=lambda kv: -len(kv[1])):
            out.write(f"\n## {project} ({len(msgs)})\n")
            for when, text in sorted(msgs):
                one_line = " ".join(text.split())
                out.write(f"{when:%m-%d %H:%M}Z {one_line[:MAX_CHARS]}\n")
    with open(args.out, encoding="utf-8") as fh:
        for _ in range(5):
            print(fh.readline().rstrip())
    print("projects: " + ", ".join(f"{p} ({len(m)})" for p, m in
                                   sorted(by_project.items(), key=lambda kv: -len(kv[1]))[:20]))
    print("written to " + args.out)


if __name__ == "__main__":
    main()
