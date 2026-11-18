#!/usr/bin/env python3
"""Verify literal evidence and fixture consistency. This is not a semantic evaluator."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
source = (root / "source.txt").read_text().strip()
bad = (root / "deliberately-wrong-draft.txt").read_text().strip()
corrected = (root / "corrected-draft.txt").read_text().strip()
review = json.loads((root / "claim-review.json").read_text())
checks = []
for claim in review["claims"]:
    checks.append({"check": "source_quote_" + claim["field"], "passed": claim["sourceQuote"] in source})
    text = claim["draftClaim"]
    if text is not None:
        checks.append({"check": "draft_claim_" + claim["field"], "passed": text in bad})
    checks.append({"check": "corrected_claim_" + claim["field"], "passed": claim["correctedClaim"] in corrected})
for term in ["Tuesday", "will be delivered", "without calling"]:
    checks.append({"check": "planted_claim_removed_" + term, "passed": term not in corrected})
result = {
    "exercise": "ai-draft-source-check",
    "source": "fictional",
    "incorrectDraft": "deliberately_injected_errors",
    "claimRowsReviewedByAgent": len(review["claims"]),
    "checks": checks,
    "passed": all(check["passed"] for check in checks),
    "scope": "Literal quote existence and fixture text consistency only. Agent review supplied the meaning judgments. No model accuracy, exhaustive semantic correctness or time-saving result is measured."
}
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
