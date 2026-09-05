from __future__ import annotations

import itertools
import json
from collections import defaultdict
from pathlib import Path

import sympy as sp

from check_six_point_nmhv_ordering_relations import amplitude

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-nmhv-universal-ddm-dressing.json"
LEGS=tuple(range(1,7))


def commutator(poly,letter):
    out=defaultdict(lambda:sp.Integer(0))
    for word,coefficient in poly.items():
        out[word+(letter,)]+=coefficient
        out[(letter,)+word]-=coefficient
    return dict(out)


def cyclic_word(word):
    rotations=[word[i:]+word[:i] for i in range(len(word))]
    return min(rotations)


def half_ladder_trace(order):
    poly={(order[0],):sp.Integer(1)}
    for letter in order[1:-1]: poly=commutator(poly,letter)
    out=defaultdict(lambda:sp.Integer(0))
    for word,coefficient in poly.items(): out[cyclic_word(word+(order[-1],))]+=coefficient
    return dict(out)


def basis_orders(left,right):
    middle=tuple(i for i in LEGS if i not in (left,right))
    return [(left,)+p+(right,) for p in itertools.permutations(middle)]


def dressed(basis,amps,mutate=None):
    out=defaultdict(lambda:sp.Integer(0))
    for order in basis:
        sign=-1 if order==mutate else 1
        for word,coefficient in half_ladder_trace(order).items():
            out[word]+=sign*coefficient*amps[order]
    return {word:sp.cancel(value) for word,value in out.items() if sp.cancel(value)!=0}


def main():
    basis16=basis_orders(1,6); basis26=basis_orders(2,6)
    all_orders=set(basis16+basis26)
    amps={order:amplitude(order) for order in all_orders}
    value16=dressed(basis16,amps); value26=dressed(basis26,amps)
    keys=set(value16)|set(value26)
    residual={word:sp.cancel(value16.get(word,0)-value26.get(word,0)) for word in keys}
    residual={word:value for word,value in residual.items() if value!=0}
    hostile=dressed(basis16,amps,mutate=basis16[0])
    hostile_residual={word:sp.cancel(hostile.get(word,0)-value26.get(word,0)) for word in set(hostile)|set(value26)}
    hostile_residual={word:value for word,value in hostile_residual.items() if value!=0}
    assertions={
        "free_trace_word_coefficients_basis_independent":not residual,
        "hostile_half_ladder_sign_flip_detected":bool(hostile_residual),
        "expected_cyclic_single_trace_support":len(keys)==120
    }
    out={
        "schema":"marici.nima.six_point_nmhv_universal_ddm_dressing.result.v1",
        "status":"passed" if all(assertions.values()) else "failed",
        "component":"six-point NMHV three-negative-gluon component on legs 1,2,3",
        "assertions":assertions,
        "cyclic_trace_word_count":len(keys),
        "basis_residual_word_count":len(residual),
        "hostile_residual_word_count":len(hostile_residual),
        "partial_amplitude_ordering_count":len(amps),
        "claim_boundary":"Equality in the free cyclic single-trace word module proves DDM endpoint-basis independence for tree-level adjoint color algebras admitting the commutator trace realization, at one exact kinematic component. It does not construct geometry-level Jacobi descent or cover exceptional non-trace presentations independently."
    }
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    if out["status"]!="passed": raise SystemExit(1)

if __name__=="__main__": main()
