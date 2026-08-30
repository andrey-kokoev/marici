#!/usr/bin/env python3
"""WP62: exact necessity and sufficiency of independent UV boundary data."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp62_uv_boundary_normalization_gate.json"

def main():
    a=sp.Matrix([[1,1,0],[0,1,1],[1,0,1]])
    ainv=a.inv(); b=sp.Matrix([[1, -1, 0]])
    transported=sp.simplify(b*ainv)
    x1=sp.Matrix([1,2,3]); x2=sp.Matrix([2,1,3])
    uv1,uv2=ainv*x1,ainv*x2
    n1,n2=(b*uv1)[0],(b*uv2)[0]
    frozen=n1
    residual1=sp.simplify((transported*x1)[0]-frozen)
    residual2=sp.simplify((transported*x2)[0]-frozen)
    source=json.loads((ROOT/"research/flavor/results/wp60_source_authority_inventory.json").read_text())
    gates={
      "transport_is_invertible_without_boundary":a.det()!=0,
      "boundary_pushes_forward_to_exact_ir_constraint":sp.simplify(transported*a-b)==sp.zeros(1,3),
      "one_independent_boundary_reduces_dimension_by_one":transported.rank()==1,
      "frozen_boundary_selects_one_hostile_point":residual1==0 and residual2!=0,
      "ir_fitted_normalization_is_circular":sp.simplify((transported*x2)[0]-n2)==0,
      "declared_source_lacks_frozen_normalization":source["explicit_absences"]["frozen_normalization"],
    }
    assert all(gates.values()),gates
    result={
      "schema":"marici.flavor.uv-boundary-normalization-gate.v1",
      "arithmetic":"exact rational linear transport",
      "model":"x_IR=A x_UV with invertible A; UV law B x_UV=b",
      "transported_constraint":"B A^{-1} x_IR=b",
      "ranks":{"ambient":3,"constraint":transported.rank(),"selected_dimension":2},
      "hostile_pair":{"x1":list(map(str,x1)),"x2":list(map(str,x2)),"frozen_b":str(frozen),"x1_residual":str(residual1),"x2_residual":str(residual2)},
      "classification":{"rg_transport_selector":False,"transport_plus_independent_boundary_selector":True,"source_authorized_in_declared_paper":False,"instrument":"requires independent UV/threshold measurement or a derived vacuum law"},
      "minimal_added_structure":"one source-derived quotient-level boundary equation with normalization fixed independently of the IR point",
      "smallest_exact_falsifier":"refitting b separately to x1 and x2 makes both pass, proving an unfrozen normalization predicts nothing",
      "conclusion":"A boundary law can turn invertible transport into proper selection, but only when its normalization is independently frozen; the declared source supplies no such law.",
      "gates":gates,
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()
