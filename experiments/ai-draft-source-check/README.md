# The source says Thursday. The draft says Tuesday.

A small source-check exercise for people using AI to draft office messages.
The email is fictional. The incorrect draft contains errors inserted on purpose.
Codex reviewed the claims and wrote the correction in this exercise.

## Try it

Read [the source](source.txt) and [the deliberately wrong draft](deliberately-wrong-draft.txt).
Before asking for a rewrite, check the day, time, action, condition and commitment.
Use [the revised copyable prompt](prompt.txt) and [review worksheet](review-worksheet.md).
The worksheet uses three findings: **Supported**, **Contradicted**, and
**Not established**. It separates complete claims without dropping their conditions.
Then compare the original packet review with [the worked claim table](claim-review.json)
and [the correction](corrected-draft.txt).

| Draft | Exact source | What changed |
| --- | --- | --- |
| Tuesday | Your signed packet will be ready Thursday after 2 pm. | The day |
| at 2 pm | Your signed packet will be ready Thursday after 2 pm. | An after-time becomes an exact time |
| will be delivered | No delivery has been arranged. | An unsupported delivery commitment |
| Anyone may collect it without calling. | If someone else is collecting it, call us before sending them. | The condition is reversed |
| No pickup location | Please collect it at the front desk. | An instruction is omitted |

## Did the reply answer both questions?

Fictional event brief: The workshop is online.

> **Sender:** Is the workshop online? Will there be a recording?  
> **Draft reply:** Yes, the workshop is online.

The draft answers the first question. The brief says nothing about a recording, so leave that answer open: “Yes, the workshop is online. I don't know yet whether there will be a recording.”

[Copy the question-by-question email review prompt on X](https://x.com/SangTheRhee/status/2117440476580090244).

## What changed after reader feedback

This revision applies two comments from one reader,
[krishkhinchi's three-state suggestion](https://github.com/microsoft/generative-ai-for-beginners/discussions/1460#discussioncomment-19756606)
and [the follow-up on split claims and full conditions](https://github.com/microsoft/generative-ai-for-beginners/discussions/1460#discussioncomment-19763433).
The revised prompt requires exact evidence for Supported or Contradicted, leaves
unestablished details unknown, and keeps conditions attached to each claim.
The worksheet works through the existing fictional invoice and courier examples.
No new model run or accuracy gain is claimed.

The original packet fixtures and `claim-review.json` are unchanged. Its historical
categories such as `changed` and `omitted_instruction` are preserved rather than
silently relabeled as three-state findings. Use the worksheet for the new review
format, and report omitted supported instructions separately.

## Reproduce the text checks

Python 3, no packages or API key needed. Download or clone this folder and run:

```sh
python3 verify.py
```

The saved run passed 17 literal checks across five claim rows. See [the output](verification-result.json).
These checks confirm that the quoted text exists and that the supplied fixtures are consistent.
The meaning judgments came from agent review. This exercise measures no model accuracy or time saving.
Rerunning this verifier still checks only those original packet fixtures. It does
not validate the revised prompt or the new worksheet examples semantically.

Try removing the day from the source. A source-only review should leave the day unknown instead of inventing one.

More small AI workflow experiments on [X @SangTheRhee](https://x.com/SangTheRhee).
