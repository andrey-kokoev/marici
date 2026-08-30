#!/usr/bin/env python3
"""WP63: exact threshold Schur-complement descent, kernel, and image audit."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp63_threshold_schur_selector_gate.json"

def dag(x): return x.conjugate().T
def schur(a,b,d): return sp.simplify(a-b*d.inv()*dag(b))

def main():
    a=sp.Matrix([[3,1],[1,5]]); b=sp.Matrix([[1],[2]]); d=sp.Matrix([[2]])
    eff=schur(a,b,d)
    u=sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5)],[-sp.Rational(4,5),sp.Rational(3,5)]])
    w=sp.Matrix([[-1]])
    covariance=sp.simplify(schur(u*a*dag(u),u*b*dag(w),w*d*dag(w))-u*eff*dag(u))
    # Distinct UV completions of the same EFT target.
    target=sp.Matrix([[2,1],[1,4]])
    d1,d2=sp.Matrix([[2]]),sp.Matrix([[5]])
    b1,b2=sp.Matrix([[1],[0]]),sp.Matrix([[0],[2]])
    a1=target+b1*d1.inv()*dag(b1); a2=target+b2*d2.inv()*dag(b2)
    e1,e2=schur(a1,b1,d1),schur(a2,b2,d2)
    # Every target has a block-diagonal completion, proving surjectivity.
    block_completion=schur(target,sp.zeros(2,1),sp.Matrix([[7]]))
    authority=json.loads((ROOT/"research/flavor/results/wp60_source_authority_inventory.json").read_text())
    gates={
      "threshold_map_is_light_basis_covariant":covariance==sp.zeros(2),
      "distinct_uv_completions_have_same_eft_image":e1==target and e2==target and (a1!=a2 or b1!=b2 or d1!=d2),
      "threshold_map_has_nontrivial_source_fibers":e1==e2,
      "threshold_map_is_surjective_on_eft_targets":block_completion==target,
      "noninjective_does_not_imply_proper_image":e1==e2 and block_completion==target,
      "threshold_law_absent_from_declared_source":authority["explicit_absences"]["threshold_matching_law"],
    }
    assert all(gates.values()),gates
    result={
      "schema":"marici.flavor.threshold-schur-selector-gate.v1",
      "arithmetic":"exact rational matrix algebra",
      "extended_domain":"light/heavy Hermitian block data (A,B,D) with invertible D",
      "operation":"H_eff=A-B D^{-1} B^dag",
      "descent":"covariant under independent light/heavy basis transformations",
      "contextual_partition":"many UV completions collapse to one EFT point",
      "proper_image":"no: every light target has the block-diagonal completion (target,0,D)",
      "classification":{"transport_or_reduction":"noninjective reduction","selector":False,"rigidifier":False,"source_authorized":False,"instrument":"requires a declared heavy sector and threshold experiment"},
      "smallest_exact_falsifier":"two distinct UV completions share one target while every target remains attainable",
      "minimal_added_structure":"a source restriction on admissible UV blocks whose Schur-complement image is proper, plus independently fixed threshold parameters",
      "conclusion":"Threshold information loss creates source fibers but does not select a proper low-energy family; noninjective is not non-surjective.",
      "gates":gates,
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()
