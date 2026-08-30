#!/usr/bin/env python3
"""WP65: exact full-weak-basis descent test for the illustrative spurion relation."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp65_spurion_relation_descent.json"

def dag(x): return x.conjugate().T

def main():
    chi_sum=1+sp.I; y22=sp.Integer(3)
    yu=sp.Matrix([[2,chi_sum*y22],[1,y22]])
    q=sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5)],[-sp.Rational(4,5),sp.Rational(3,5)]])
    yup=sp.simplify(q*yu)
    residual_before=sp.simplify(yu[0,1]-chi_sum*yu[1,1])
    residual_after=sp.simplify(yup[0,1]-chi_sum*yup[1,1])
    hu,yh=yu*dag(yu),yup*dag(yup)
    invariant_residuals={
      "trace":sp.simplify(sp.trace(hu)-sp.trace(yh)),
      "det":sp.simplify(hu.det()-yh.det()),
      "trace_square":sp.simplify(sp.trace(hu**2)-sp.trace(yh**2)),
    }
    authority=json.loads((ROOT/"research/flavor/results/wp60_source_authority_inventory.json").read_text())
    gates={
      "source_component_relation_holds_before_rotation":residual_before==0,
      "same_scalar_spurion_relation_fails_after_q_rotation":residual_after!=0,
      "physical_gram_invariants_are_preserved":all(v==0 for v in invariant_residuals.values()),
      "failure_occurs_on_one_full_weak_basis_orbit":sp.simplify(yh-q*hu*dag(q))==sp.zeros(2),
      "spurion_picture_is_illustrative_deferred":authority["markers"]["z8_modal"]["unique"] and authority["markers"]["uv_deferred"]["unique"],
    }
    assert all(gates.values()),gates
    result={
      "schema":"marici.flavor.spurion-relation-descent.v1",
      "arithmetic":"exact Gaussian-rational matrix algebra",
      "relation":"Y_12=(chi_1+chi_2)Y_22",
      "exact_residuals":{"before":str(residual_before),"after_common_left_rotation":str(residual_after),"physical_invariants":{k:str(v) for k,v in invariant_residuals.items()}},
      "descent":"fails if chi_1+chi_2 is treated as the source's scalar component datum",
      "contextual_partition":"the relation selects component presentations inside a chosen generation frame, not full weak-basis orbits",
      "classification":{"presentation_rigidifier":True,"physical_selector":False,"instrument":"none declared"},
      "repair_requirement":"declare a complete flavor representation for the spurions and a covariant tensor contraction producing the Yukawa pair, then quotient the joint flavon-Yukawa vacuum orbit",
      "smallest_exact_falsifier":"one rational common-left rotation preserves Gram invariants while making the component relation residual nonzero",
      "conclusion":"The illustrative Z8 spurion equation is basis-component data and does not descend to physical16 without additional tensorial source structure.",
      "gates":gates,
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()
