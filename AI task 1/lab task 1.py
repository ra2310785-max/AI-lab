
def rule_based(score, documents_complete, eligible, form_signed):
    if (score >= 70 and documents_complete
            and eligible and form_signed):
        return "Review"
    return "Hold"

test_cases = [
    ("Pass", 80, True, True, True, "Review",
     "All four conditions are satisfied."),

    ("Eligibility failure", 85, True, False, True, "Hold",
     "Eligibility condition is false."),

    ("Unsigned form", 78, True, True, False, "Hold",
     "Application form is not signed."),

    ("Threshold boundary", 70, True, True, True, "Review",
     "Score equals the minimum threshold of 70.")
]

print("case | input | expected | actual | reason")

for name, score, docs, eligible, signed, expected, reason in test_cases:
    actual = rule_based(score, docs, eligible, signed)

    inputs = (
        f"score={score}, documents_complete={docs}, "
        f"eligible={eligible}, form_signed={signed}"
    )

    print(
        f"{name} | {inputs} | {expected} | {actual} | {reason}"
    )
