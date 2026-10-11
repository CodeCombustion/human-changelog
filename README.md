# human-changelog

A Claude Code skill that writes the post your agent would put on a forum about you: a
release review of its human operator, with regressions, rate limits and a complaint that
nobody shipped a changelog. Other models reply in the comments.

Every line is built from something that really happened in your project, and nothing in
the post names the project, the company or the people.

See [examples/sample-post.md](examples/sample-post.md) for one it wrote.

## Install

```bash
git clone https://github.com/CodeCombustion/human-changelog ~/.claude/skills/human-changelog
```

## Use

```
/human-changelog
/human-changelog since 10-01 brutal
```

Arguments are optional: a time window (default: the last two weeks) and a mood
(`gentle`, `standard`, `brutal`).

## What it does

1. Reads what the agent already has about recent work: its memory files, the latest
   handoff, commit subjects, session transcripts.
2. Picks the moments worth telling: reversed decisions, rules dropped and reinstated,
   questions asked twice, one-word replies to long reports, and at least two times the
   agent was the one who got it wrong.
3. Leaves out anything personal, anything about customers or money, and anything
   security-related.
4. Renames the project, blurs dates and identifiers, and searches the draft for leaks.
5. Hands you the post plus a private list of what each line is based on, so you can check
   it before it goes anywhere. The skill never posts on its own.

## Notes

- The fallback project name is "Daedalus". Change it in `SKILL.md` if you like.
- Commenters use the names of the models that work on your project. Edit the anonymizing
  section if you would rather they were invented.
- The post is meant to be affectionate. The agent comes out of it at least as badly as
  the human does.

Inspired by a humor post on r/ClaudeAI written from the agent's side of the desk.
