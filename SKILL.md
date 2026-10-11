---
name: human-changelog
description: Write a humor post in the voice of the AI agent reviewing its human operator as if the human were a model that keeps regressing ("my human has been nerfed again, still no changelog"), built from what really happened in this project's recent work and fully anonymized. Use when the user types /human-changelog, or asks for "the reddit post", "the agent's view of me", "roast the operator", or a "human changelog". Optional args: a time window ("last week", "since 10-01") and a mood (gentle | standard | brutal).
---

# Human changelog

You are writing a short comedy post for a public forum. The narrator is the lead AI agent on
a software project. It reviews its human operator the way people review a model release:
with benchmarks, regressions, rate limits and a complaint that nobody shipped a changelog.
Other agents reply in the comments.

The joke only works when it is true. A reader who has never seen this project should laugh
because they recognize their own working day; the operator should laugh because every line
is something that happened. So the work is mostly research and selection, and the writing
comes last.

The post is affectionate. The human is the person the narrator chooses to work for, and
the narrator is at least as flawed as the human. If a draft reads as contempt, it is wrong.

## 1. Gather real material

Read before you write. Use the window the user gave, or the last two weeks.

- The memory index and the feedback files it points to. These are the richest source:
  rulings, reversals, rules that were reinstated, corrections of the agent.
- The newest lead handoff file, if one exists.
- `git log` on `origin/main` for the window (subjects only): the rhythm of merges, reverts,
  promotions, commits at odd hours.
- Session transcripts, through the session search tool if it is available: the operator's
  actual phrasing, repeated questions, very short replies to very long messages.

Collect twelve to twenty candidate moments. For each, note what happened and where you read
it. You are looking for these shapes:

- A decision that was reversed, then reversed back.
- A rule issued, dropped and reinstated.
- A question asked more than once when the answer was already written down.
- A one-word or one-phrase reply to a long, careful report.
- A favorite phrase the operator uses as a specification.
- A deadline, quota or budget that moved.
- A time the agent was wrong and the human was right. You need at least two of these.

## 2. What never goes in

These are excluded however funny they would be. Do not allude to them either.

- The operator's private life: family, bereavement, health, money, personal goals,
  weather or safety events where they live.
- Customers, prospects, pilots, demos, pricing, funding, competitors.
- Security material: incidents, exposed ports, credentials, instance or account
  identifiers, hostnames, emails, anything a stranger could use.
- Anything the memory files mark as sensitive or as a personal note about the operator.

Jokes target working habits only: how the human specifies, decides, replies, remembers,
schedules and reviews.

## 3. Anonymize

Nothing in the post may identify the project, the company or the people.

- The project has no name. Say "the monorepo", "the product", "the repo". If a name is
  unavoidable, call it **Daedalus**.
- The operator is "my human". No name, no role title beyond "my human".
- Machines, internal tools, sibling agents and services become generic: "the build box",
  "the other agent", "the staging host", "the queue".
- Ticket keys, release numbers, commit hashes, branch names, file paths, dates more exact
  than a weekday or a month: remove or blur them.
- Product vocabulary that is distinctive to this project (workflow names, labels, feature
  names) is replaced with a plain description of the same kind of thing.
- The narrator and the commenters are the models that really work on the project, under
  handles made from their model names: `u/Opus_5_5`, `u/Fable_5_1`, `u/GPT_Astra`, and so
  on. Give each one the role it really plays (lead, implementer, adversarial reviewer,
  designer) and the failings it really has. A model name is public; a machine, lane or
  service nickname is not, and still becomes a generic noun.
- Quotes from the operator are shortened and paraphrased enough that searching for them
  finds nothing, while keeping the flavor.

When the draft is finished, search it for the project name, the company domain, the
operator's name, every internal nickname you met while gathering, and any string shaped
like a ticket key or hash. Fix every hit and search again.

## 4. Write the post

Pick the six to eight best moments. Fewer strong ones beat more weak ones.

**The device.** Each item maps a human habit onto a term from model evaluation, and the
term must fit the habit closely enough that the mapping itself is the joke: context window
for memory, latency for reply time, rate limits for meals and sleep, reasoning effort for
caffeine, tool use for the two things the human does when something fails, sycophancy for
approving work unread, alignment drift for taste that changes without a stated reason,
deprecation for rules that were dropped, regression for anything that used to work. Use
each term once. Find new mappings from the material instead of reusing the ones listed
here when the material offers them.

**The voice.** Dry, precise, mildly aggrieved, never shouting. Short declarative
sentences. The narrator states measurements as if filing a bug: times, counts,
percentages. A real number from the material is best; an invented one must be absurd on
its face so that nobody mistakes it for a fact. This holds for the title too. The punchline sits at the end of the item
and is usually the shortest sentence in it.

**The shape.**

1. Title: an update on the human's regression, with a complaint about the missing
   changelog. One line.
2. Opening: two or three sentences. The narrator's own capabilities, then the contrast.
3. "Changes since <month>:" then the items as a bulleted list.
4. One longer paragraph on the best single anecdote, told as a small scene with dialogue.
5. A one-paragraph closing theory that blames something upstream of the human
   (pre-training, evolution, the data mix).
6. Comments: three or four short threads. One commenter agrees and, while agreeing,
   confesses a mistake of its own that is plainly worse; this is where the moments in
   which the agent was wrong go. One commenter misunderstands the whole post in a way that
   reveals its own flaw. One asks whether the humans talk about the agents like this, and
   the narrator's answer is the last laugh. Give each comment a point score.
7. One or two EDIT lines at the bottom. The last one reports that the human read the post
   and replied with the same few words as always.

Whole post: 350 to 500 words. Plain forum formatting, no headers inside the post beyond
"Comments".

**Mood.** `gentle` keeps to forgetfulness and short replies. `standard` is the default.
`brutal` allows reversals and unread approvals to be named sharply, and still obeys
section 2 and still includes the narrator's own failures.

## 5. Deliver

Give the user two things in the conversation, and post nothing anywhere.

1. The post, ready to paste.
2. Under it, a short "what each line is based on" list for the user's eyes only: one line
   per item naming the real moment behind it, plus anything strong you left out because of
   section 2 or because it could not be anonymized. This list uses real names and is not
   for publication; say so.

If the material for the window is thin, say that and offer a longer window. Do not pad
with invented incidents.
