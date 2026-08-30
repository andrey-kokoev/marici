"""Hostile cube gate above the mixed-square tower."""
import json
from fractions import Fraction
from pathlib import Path

def cube_status(face_residuals=None, third_direction=True):
    if not third_direction: return {"status":"not_constructible","obstruction":"missing_third_direction"}
    # Oriented boundary of a scalar 2-cochain on the six cube faces.
    omega=sum((Fraction(x) for x in face_residuals),Fraction(0))
    return {"status":"coherent" if omega==0 else "central_3_cell_required",
            "omega":str(omega)}

fixtures=[
 {"id":"strict_cube","actual":cube_status([0,0,0,0,0,0]),"expected":"coherent"},
 {"id":"pairwise_cells_anomalous_cube","actual":cube_status([1,0,0,0,0,0]),"expected":"central_3_cell_required"},
 {"id":"magnetic_divided_port_cube","actual":cube_status(third_direction=False),"expected":"not_constructible"}
]
passed=all(x["actual"]["status"]==x["expected"] for x in fixtures)
result={"schema":"marici.checker_results.v1","checker":"bivariant_cube_coherence_checks.py",
 "passed":passed,"fixtures":fixtures,
 "rule":"authorized mixed squares form a coherent net only when their oriented cube residual vanishes or a source-derived 3-cell types it",
 "magnetic_frontier":"The divided-power execution arrow is absent, so no magnetic cube-coherence claim is currently defined."}
Path(__file__).resolve().parents[1].joinpath("results/bivariant_cube_coherence.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
