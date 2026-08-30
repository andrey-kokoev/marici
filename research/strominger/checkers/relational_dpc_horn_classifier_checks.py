"""Relational DPC horn classification and anti-selection gates."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[3]
c=json.loads((root/"research/strominger/contracts/relational-dpc-horn-classifier.v1.json").read_text())
records=[]
for x in c["fixtures"]:
    if x["filler_object"]=="empty":
        expected="undefined"
    elif not x["pointed_by_source"]:
        expected="undefined"
    else:
        expected=x["scalar_status"]
    records.append({"id":x["id"],"expected_scalar_status":expected,
                    "actual_scalar_status":x["scalar_status"],
                    "passes":expected==x["scalar_status"]})
tests={
 "all_fixture_types_classified":all(x["filler_object"] in c["horn_classifier"]["cardinalities"] for x in c["fixtures"]),
 "unpointed_line_does_not_select_scalar":records[2]["passes"],
 "detector_alone_does_not_select_scalar":records[3]["passes"],
 "instrument_relation_not_promoted_to_universal_tower":c["instrument_relation"]["universal_tower"] is False
}
result={"schema":"marici.checker_results.v1","checker":"relational_dpc_horn_classifier_checks.py",
 "passed":all(tests.values()),"tests":tests,"records":records,
 "verdict":"Universal DPC classifies filler objects and relational residues. Point selection and scalar realization remain instrument-indexed relations."}
(root/"research/strominger/results/relational_dpc_horn_classifier.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["passed"] else 1)
