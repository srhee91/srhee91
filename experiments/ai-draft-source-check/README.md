# The source says Thursday. The draft says Tuesday.

A small source-check exercise for people using AI to draft office messages.
The email is fictional. The incorrect draft contains errors inserted on purpose.
Codex reviewed the claims and wrote the correction in this exercise.

## Try it

Read [the source](source.txt) and [the deliberately wrong draft](deliberately-wrong-draft.txt).
Before asking for a rewrite, check the day, time, action, condition and commitment.
Use [the copyable prompt](prompt.txt), then compare your review with [the worked claim table](claim-review.json) and [the correction](corrected-draft.txt).

| Draft | Exact source | What changed |
| --- | --- | --- |
| Tuesday | Your signed packet will be ready Thursday after 2 pm. | The day |
| at 2 pm | Your signed packet will be ready Thursday after 2 pm. | An after-time becomes an exact time |
| will be delivered | No delivery has been arranged. | An unsupported delivery commitment |
| Anyone may collect it without calling. | If someone else is collecting it, call us before sending them. | The condition is reversed |
| No pickup location | Please collect it at the front desk. | An instruction is omitted |

## Reproduce the text checks

Python 3, no packages or API key needed. Download or clone this folder and run:

```sh
python3 verify.py
```

The saved run passed 17 literal checks across five claim rows. See [the output](verification-result.json).
These checks confirm that the quoted text exists and that the supplied fixtures are consistent.
The meaning judgments came from agent review. This exercise measures no model accuracy or time saving.

Try removing the day from the source. A source-only review should leave the day unknown instead of inventing one.

More small AI workflow experiments on [X @SangTheRhee](https://x.com/SangTheRhee).
