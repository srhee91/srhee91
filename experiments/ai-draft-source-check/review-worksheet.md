# Review worksheet

Use the [copyable prompt](prompt.txt) with a supplied source and draft. Split a
compound sentence into complete claims without dropping its conditions, dates,
exceptions or commitments. A supported fragment does not support the whole.

Use exactly **Supported**, **Contradicted**, or **Not established**. Supported and
Contradicted need exact source quotations. If the source does neither, retain the
unknown. A quotation of related context does not establish an unstated detail.

| Complete claim | Finding | Exact source | Unknown | Rewrite |
| --- | --- | --- | --- | --- |
| [Include all conditions and limits.] | [Supported / Contradicted / Not established] | [Exact establishing/conflicting passage, or say none; label related context as context.] | [Missing detail, or none needed for this finding.] | [Supported meaning with qualifiers; keep other details unknown.] |

## Worked example 1: a fictional invoice note

Source: **"Deposit received. Balance unpaid."**

| Complete claim | Finding | Exact source | Unknown | Rewrite |
| --- | --- | --- | --- | --- |
| A deposit was received. | Supported | "Deposit received." | No missing detail is needed for this finding. | A deposit was received. |
| The balance is paid. | Contradicted | "Balance unpaid." | No missing detail is needed for this finding. | The balance is unpaid. |
| The deposit was paid by card. | Not established | No establishing or contradicting passage. Context only: "Deposit received. Balance unpaid." | Payment method. | A deposit was received; the note does not establish the payment method. |

The method is unknown, not disproved. These three findings can coexist for the
same supplied note. This fictional example appeared in the
[existing invoice reply](https://github.com/microsoft/generative-ai-for-beginners/discussions/1460#discussioncomment-19761178).

## Worked example 2: a fictional conditional courier note

Source: **"The packet is ready. A courier may collect it only after we confirm the caller's name."**

Draft: **"The packet is ready for courier pickup now."**

| Complete claim | Finding | Exact source | Unknown | Rewrite |
| --- | --- | --- | --- | --- |
| The packet is ready. | Supported | "The packet is ready." | No missing detail is needed for this finding. | The packet is ready. |
| A courier may collect it only after we confirm the caller's name. | Supported | "A courier may collect it only after we confirm the caller's name." | Whether that confirmation has happened is not needed to establish the rule itself. | A courier may collect it only after we confirm the caller's name. |
| The caller's name has been confirmed. | Not established | No establishing or contradicting passage. Context only: "A courier may collect it only after we confirm the caller's name." | Whether confirmation happened. | The source does not establish whether the caller's name has been confirmed. |
| Courier pickup is allowed now. | Not established | No establishing or contradicting passage for current permission. Context only: "A courier may collect it only after we confirm the caller's name." | Whether confirmation happened; current pickup permission. | A courier may collect it only after we confirm the caller's name. |

The first two rows show source facts/rules; the last two test details the source
does not establish. Do not rewrite the last row as "pickup is forbidden now" or
"the name has not been confirmed." Neither statement is established. The whole
compound draft is not Supported merely because the packet is ready.

A source-only correction is:

> The packet is ready. A courier may collect it only after we confirm the caller's name.

The rule is established; its completion and current pickup permission remain
unknown. This fictional example appeared in the
[existing courier reply](https://github.com/microsoft/generative-ai-for-beginners/discussions/1460#discussioncomment-19770560).

## Keep omissions separate

In the original packet exercise, "Please collect it at the front desk." is a
supported instruction missing from the draft. List that omission separately and
restore it in the correction. Do not force an omission into a truth-status label.

The worksheet is an agent-authored worked review, not a new model run, test
result, accuracy measurement or guarantee. The preserved `verify.py` checks only
the original packet fixtures; it does not validate this prompt or worksheet's
meaning judgments.
