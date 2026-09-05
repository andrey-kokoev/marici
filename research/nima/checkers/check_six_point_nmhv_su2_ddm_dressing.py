from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

from check_six_point_nmhv_ordering_relations import amplitude

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/six-point-nmhv-su2-ddm-dressing.json"
LEGS = tuple(range(1, 7))
COLORS = (0, 1, 2)


def epsilon(a,b,c):
    if len({a,b,c}) < 3: return 0
    return 1 if (a,b,c) in ((0,1,2),(1,2,0),(2,0,1)) else -1


def half_ladder(order, external):
    a=[external[i] for i in order]
    total=0
    for b1,b2,b3 in itertools.product(COLORS,repeat=3):
        total += epsilon(a[0],a[1],b1)*epsilon(b1,a[2],b2)*epsilon(b2,a[3],b3)*epsilon(b3,a[4],a[5])
    return total


def basis_orders(left,right):
    middle=tuple(i for i in LEGS if i not in (left,right))
    return [(left,)+p+(right,) for p in itertools.permutations(middle)]


def main():
    amp_cache={}
    def A(order):
        order=tuple(order)
        if order not in amp_cache: amp_cache[order]=amplitude(order)
        return amp_cache[order]
    basis_16=basis_orders(1,6)
    basis_26=basis_orders(2,6)
    values=[]; hostile=[]
    mutated_order=basis_16[0]
    for assignment in itertools.product(COLORS,repeat=6):
        external={i:assignment[i-1] for i in LEGS}
        value_16=sum(half_ladder(o,external)*A(o) for o in basis_16)
        value_26=sum(half_ladder(o,external)*A(o) for o in basis_26)
        values.append(sp.cancel(value_16-value_26))
        hostile.append(sp.cancel((value_16-2*half_ladder(mutated_order,external)*A(mutated_order))-value_26))
    assertions={
        "all_729_su2_color_assignments_basis_independent":all(x==0 for x in values),
        "hostile_single_half_ladder_sign_flip_detected":any(x!=0 for x in hostile),
        "both_ddm_bases_have_24_terms":len(basis_16)==len(basis_26)==24
    }
    out={
        "schema":"marici.nima.six_point_nmhv_su2_ddm_dressing.result.v1",
        "status":"passed" if all(assertions.values()) else "failed",
        "component":"six-point NMHV three-negative-gluon component on legs 1,2,3",
        "gauge_algebra":"su(2), structure constants epsilon_abc",
        "assertions":assertions,
        "nonzero_basis_difference_count":sum(x!=0 for x in values),
        "nonzero_hostile_difference_count":sum(x!=0 for x in hostile),
        "partial_amplitude_ordering_count":len(amp_cache),
        "claim_boundary":"Exact finite SU(2) color dressing for all 3^6 external adjoint-color assignments at one rational kinematic point. This proves neither arbitrary-Lie-algebra dressing nor geometry-level Jacobi descent."
    }
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    if out["status"]!="passed": raise SystemExit(1)

if __name__=="__main__": main()
