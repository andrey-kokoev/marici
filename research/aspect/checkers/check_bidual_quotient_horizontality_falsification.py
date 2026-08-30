#!/usr/bin/env python3
"""Independently admit the four bidual nonhorizontality packets."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research"/"aspect"/"results"/"bidual_quotient_horizontality_falsification.json"

def rank(vectors,p):
    pivots={}
    for raw in vectors:
        row={int(k):int(v)%p for k,v in raw.items() if int(v)%p}
        while row:
            c=max(row); q=row[c]
            if c not in pivots:
                iq=pow(q,-1,p); pivots[c]={k:v*iq%p for k,v in row.items()}; break
            pivot=pivots[c]
            for k,v in pivot.items():
                x=(row.get(k,0)-q*v)%p
                if x: row[k]=x
                else: row.pop(k,None)
    return len(pivots)

def combine(a,b,x,y,p):
    keys=set(a)|set(b); return {k:(x*a.get(k,0)+y*b.get(k,0))%p for k in keys if (x*a.get(k,0)+y*b.get(k,0))%p}

reports=[]
missing_exports=[]
for p in (32009,32003):
    for direction in ("x","y"):
        suffix=("" if p==32009 else f"-p{p}")+f"-{direction}"
        path=ROOT/"research"/"benincasa"/"results"/f"rank26-bidual-quotient-horizontality{suffix}.json"
        packet=json.loads(path.read_text(encoding="utf-8"))
        if "bockstein_vectors" not in packet or "mixed_vectors" not in packet:
            missing_exports.append({"prime":p,"direction":direction,"missing":[name for name in ("bockstein_vectors","mixed_vectors") if name not in packet]})
            continue
        beta=packet["bockstein_vectors"]; mixed=packet["mixed_vectors"]
        rb=rank(beta,p); rm=rank(beta+mixed,p)
        # Joint invertible changes of the two lifted relation representatives.
        basis_tests=[]
        for matrix in (((1,1),(1,2)),((2,3),(5,7)),((1,0),(9,1))):
            det=(matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])%p
            if not det: continue
            bb=[combine(beta[0],beta[1],*row,p) for row in matrix]
            mm=[combine(mixed[0],mixed[1],*row,p) for row in matrix]
            basis_tests.append(rank(bb,p)==rb and rank(bb+mm,p)==rm)
        # gamma and kinematic dual-coordinate rescalings act by nonzero scalars.
        scale_tests=[]
        for ug,ux in ((2,3),(5,7),(p-1,11)):
            bb=[{k:ug*v%p for k,v in row.items()} for row in beta]
            mm=[{k:ug*ux*v%p for k,v in row.items()} for row in mixed]
            scale_tests.append(rank(bb,p)==rb and rank(bb+mm,p)==rm)
        reports.append({"prime":p,"direction":direction,"free_dimension":packet.get("free_dimension"),"base_relation_dimension":packet.get("base_relation_dimension"),"lifted_relation_dimension":packet.get("lifted_relation_dimension"),"obstructed_relation_dimension":packet.get("obstructed_relation_dimension"),"bockstein_rank":rb,"combined_rank":rm,"horizontal":rm==rb,"basis_variance_passed":all(basis_tests),"dual_rescaling_passed":all(scale_tests)})

checks={
    "four_vector_bearing_packets_present":len(reports)==4 and not missing_exports,
    "all_packets_use_rank_26_free_quotient":all(r.get("free_dimension")==26 for r in reports),
    "all_base_relation_dimensions_are_two":all(r.get("base_relation_dimension")==2 for r in reports),
    "all_base_relations_lift_after_quotient_projection":all(r.get("lifted_relation_dimension")==2 and r.get("obstructed_relation_dimension")==0 for r in reports),
    "all_bockstein_ranks_are_one":all(r["bockstein_rank"]==1 for r in reports),
    "all_combined_ranks_are_two":all(r["combined_rank"]==2 for r in reports),
    "horizontality_fails_in_all_replications":all(not r["horizontal"] for r in reports),
    "joint_relation_basis_variance_passes":all(r["basis_variance_passed"] for r in reports),
    "dual_coordinate_rescaling_variance_passes":all(r["dual_rescaling_passed"] for r in reports)
}
passed=all(checks.values())
payload={"schema":"marici.aspect.bidual-quotient-horizontality-falsification.v2","reports":reports,"missing_exports":missing_exports,"checks":checks,"passed":passed,"classification":"local_nonhorizontality_at_audited_point" if passed else "provisional_scalar_rank_claim_not_independently_auditable","admitted_scope":"source point (2,3,4), rank-26 free quotient, two parameter directions, primes 32009 and 32003, with exact inhomogeneous relation lifts, joint GL2 relation-basis hostiles, and nonzero dual-coordinate rescaling hostiles; no neighborhood or global Fitting claim" if passed else "none beyond the four reported scalar rank pairs","rejected_artifacts":["nilpotent-only ambient residual admitted as a relation","eliminated ambient coordinate admitted as a quotient obstruction"],"missing_constructors":["global Fitting-locus stratification"] if passed else ["four regenerated packets from the quotient-projected inhomogeneous lift solver"],"next_falsifier":"recompute joint x/y first saturation from the repaired quotient-projected packets, then replay across a source-derived Fitting stratification" if passed else "rerun all four reducer packets from the quotient-projected inhomogeneous lift solver"}
OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");print(json.dumps(payload,indent=2));raise SystemExit(0 if payload["passed"] else 1)
