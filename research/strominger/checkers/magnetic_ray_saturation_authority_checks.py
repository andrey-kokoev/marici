"""Authority gates for primitive image-ray saturation."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[3]
contract=json.loads((root/"research/strominger/contracts/magnetic-ray-saturation-authority.v1.json").read_text())
physical=(root/"research/strominger/completed-physical-source-category.md").read_text()
checks={
 "integral_units_only":contract["engine_basis_units"]==["1","-1"],
 "physical_exclusion_sourced":"independent Laurent monomials or arbitrary Laurent sequences" in physical,
 "hostile_changes_cokernel":contract["hostile_fixture"]["original_cokernel"]=="Z/7" and contract["hostile_fixture"]["saturated_image_cokernel"]=="0",
 "authority_rejected":contract["verdict"]=="not_authorized",
 "promotion_forbidden":"physical residue" in contract["forbidden_promotion"]
}
result={"schema":"marici.checker_results.v1","checker":"magnetic_ray_saturation_authority_checks.py",
 "passed":all(checks.values()),"checks":checks,
 "verdict":"Primitive-ray saturation is a changed constructor, not an authority-preserving normalization of the integral magnetic source."}
(root/"research/strominger/results/magnetic_ray_saturation_authority.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["passed"] else 1)
