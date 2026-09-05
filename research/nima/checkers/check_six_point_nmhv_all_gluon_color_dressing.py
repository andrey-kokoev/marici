from __future__ import annotations

import itertools
import json
from collections import defaultdict
from pathlib import Path

import sympy as sp

import check_six_point_nmhv_ordering_relations as rel
from check_six_point_nmhv_universal_ddm_dressing import basis_orders, half_ladder_trace

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-nmhv-all-gluon-color-dressing.json"


def prepare(order):
    mus=rel.reconstruct_mus(order,rel.LAM,rel.TILDE)
    z={i:rel.LAM[i]+mus[i] for i in order}
    transport=rel.chi_transport(order)
    o=order
    terms=[(o[0],o[1],o[2],o[3],o[4]),(o[0],o[1],o[2],o[4],o[5]),(o[0],o[2],o[3],o[4],o[5])]
    pt=sp.prod(rel.bracket(rel.LAM[o[i]],rel.LAM[o[(i+1)%6]]) for i in range(6))
    return z,transport,terms,pt


def component(prepared,target):
    z,transport,terms,pt=prepared
    old=rel.TARGET
    rel.TARGET=target
    try:
        value=sum(rel.five_bracket_component(z,transport,term) for term in terms)
    finally:
        rel.TARGET=old
    return sp.cancel(value/pt)


def dressed(basis,amps,mutate=None):
    out=defaultdict(lambda:sp.Integer(0))
    for order in basis:
        sign=-1 if order==mutate else 1
        for word,coefficient in half_ladder_trace(order).items(): out[word]+=sign*coefficient*amps[order]
    return {word:sp.cancel(value) for word,value in out.items() if sp.cancel(value)!=0}


def main():
    basis16=basis_orders(1,6); basis26=basis_orders(2,6)
    orders=set(basis16+basis26)
    prepared={order:prepare(order) for order in orders}
    rows=[]
    for target in itertools.combinations(range(1,7),3):
        amps={order:component(prepared[order],target) for order in orders}
        left=dressed(basis16,amps); right=dressed(basis26,amps)
        keys=set(left)|set(right)
        residual={word:sp.cancel(left.get(word,0)-right.get(word,0)) for word in keys}
        residual={word:value for word,value in residual.items() if value!=0}
        rows.append({
            "negative_helicity_legs":list(target),
            "ddm_basis_independent":not residual,
            "nonzero_partial_amplitude_count":sum(value!=0 for value in amps.values()),
            "residual_word_count":len(residual)
        })
    target=(1,2,3)
    amps={order:component(prepared[order],target) for order in orders}
    hostile=dressed(basis16,amps,mutate=basis16[0]); control=dressed(basis26,amps)
    hostile_count=sum(sp.cancel(hostile.get(word,0)-control.get(word,0))!=0 for word in set(hostile)|set(control))
    assertions={
        "all_20_pure_gluon_nmvh_components_basis_independent":all(row["ddm_basis_independent"] for row in rows),
        "all_components_have_nonzero_partial_amplitudes":all(row["nonzero_partial_amplitude_count"]>0 for row in rows),
        "hostile_sign_flip_detected":hostile_count>0
    }
    out={
        "schema":"marici.nima.six_point_nmhv_all_gluon_color_dressing.result.v1",
        "status":"passed" if all(assertions.values()) else "failed",
        "assertions":assertions,
        "component_count":len(rows),
        "kinematic_fixture_count":1,
        "components":rows,
        "hostile_residual_word_count":hostile_count,
        "claim_boundary":"All 20 pure-gluon six-point NMHV helicity components are DDM endpoint-basis independent in the free cyclic trace module at one exact nonsingular kinematic point. This does not span the complete N=4 supermultiplet or prove a symbolic kinematic identity."
    }
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    if out["status"]!="passed": raise SystemExit(1)

if __name__=="__main__": main()
