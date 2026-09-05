from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

from check_six_point_nmhv_ordering_relations import sij, shuffles

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-bcj-quotient-rank.json"
DDM=[(1,)+p+(6,) for p in itertools.permutations((2,3,4,5))]
INDEX={order:i for i,order in enumerate(DDM)}


def rotate_to_one(order):
    k=order.index(1)
    return order[k:]+order[:k]


def kk_reduce(order):
    order=rotate_to_one(tuple(order))
    six=order.index(6)
    alpha=order[1:six]; beta=order[six+1:]
    coefficient=(-1)**len(beta)
    out={}
    for middle in shuffles(alpha,tuple(reversed(beta))):
        ddm=(1,)+middle+(6,)
        out[ddm]=out.get(ddm,0)+coefficient
    return out


def main():
    rows=[]
    for moved in range(1,6):
        others=tuple(i for i in range(1,6) if i!=moved)
        for p in itertools.permutations(others):
            row=[sp.Integer(0)]*24
            weight=sp.Integer(0)
            for k in range(1,5):
                weight+=sij(moved,p[k-1])
                order=p[:k]+(moved,)+p[k:]+(6,)
                for ddm,coefficient in kk_reduce(order).items(): row[INDEX[ddm]]+=weight*coefficient
            rows.append(row)
    matrix=sp.Matrix(rows)
    rank=matrix.rank()
    hostile=matrix.copy(); hostile[0,0]=-hostile[0,0]
    checks={
        "ddm_basis_dimension_24":matrix.cols==24,
        "fundamental_bcj_rank_18":rank==18,
        "bcj_quotient_dimension_6":matrix.cols-rank==6,
        "hostile_entry_sign_changes_row_space":hostile.rank()!=rank or hostile.rref()[1]!=matrix.rref()[1]
    }
    out={
        "schema":"marici.nima.six_point_bcj_quotient_rank.result.v1",
        "status":"passed" if all(checks.values()) else "failed",
        "checks":checks,
        "matrix_shape":[matrix.rows,matrix.cols],
        "rank":rank,
        "quotient_dimension":matrix.cols-rank,
        "expected_twisted_cohomology_rank":"(6-3)! = 6",
        "claim_boundary":"At one exact generic kinematic fixture, KK-reduced fundamental BCJ relations cut the 24-dimensional DDM module to dimension 6, matching the expected M0,6 twisted-cohomology rank. Rank agreement does not construct or identify the NMHV cocycle."
    }
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    if out["status"]!="passed": raise SystemExit(1)

if __name__=="__main__": main()
