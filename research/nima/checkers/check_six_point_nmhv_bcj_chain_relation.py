from __future__ import annotations

import itertools
import json
from collections import defaultdict
from pathlib import Path

import sympy as sp

from check_six_point_nmhv_ordering_relations import LABELS, LAM, amplitude, bracket, sij

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/six-point-nmhv-bcj-chain-relation.json"


def parity_to_sorted(values):
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def simplex_chain(order):
    o = order
    terms = [(o[0],o[1],o[2],o[3],o[4]), (o[0],o[1],o[2],o[4],o[5]), (o[0],o[2],o[3],o[4],o[5])]
    out = defaultdict(lambda: sp.Integer(0))
    for term in terms:
        out[tuple(sorted(term))] += parity_to_sorted(term)
    return out


def parke_taylor(order):
    return sp.prod(bracket(LAM[order[i]], LAM[order[(i + 1) % 6]]) for i in range(6))


def main():
    rows=[]
    for p in itertools.permutations((2,3,4,5)):
        raw=defaultdict(lambda:sp.Integer(0))
        dressed=defaultdict(lambda:sp.Integer(0))
        form_residual=sp.Integer(0)
        weight=sp.Integer(0)
        for k in range(1,5):
            weight += sij(1,p[k-1])
            order=p[:k]+(1,)+p[k:]+(6,)
            form_residual += weight*amplitude(order)
            for cell,sign in simplex_chain(order).items():
                raw[cell] += weight*sign
                dressed[cell] += sp.cancel(weight*sign/parke_taylor(order))
        raw={''.join(map(str,k)):sp.cancel(v) for k,v in raw.items() if sp.cancel(v)!=0}
        dressed={''.join(map(str,k)):sp.cancel(v) for k,v in dressed.items() if sp.cancel(v)!=0}
        rows.append({
            "permutation":list(p),
            "canonical_form_component_residual_zero":sp.cancel(form_residual)==0,
            "raw_chain_zero":not raw,
            "parke_taylor_dressed_chain_zero":not dressed,
            "raw_nonzero_cell_coefficients":{k:str(v) for k,v in raw.items()},
            "dressed_nonzero_cell_coefficients":{k:str(v) for k,v in dressed.items()}
        })
    assertions={
        "all_24_bcj_component_forms_zero":all(r["canonical_form_component_residual_zero"] for r in rows),
        "any_raw_chain_relation":any(r["raw_chain_zero"] for r in rows),
        "any_parke_taylor_dressed_chain_relation":any(r["parke_taylor_dressed_chain_zero"] for r in rows)
    }
    out={
        "schema":"marici.nima.six_point_nmhv_bcj_chain_relation.result.v1",
        "status":"raw_chain_obstruction" if assertions["all_24_bcj_component_forms_zero"] and not assertions["any_raw_chain_relation"] and not assertions["any_parke_taylor_dressed_chain_relation"] else "candidate_relation_found",
        "assertions":assertions,
        "relations":rows,
        "claim_boundary":"Tests whether the standard three-simplex triangulation chains satisfy fundamental BCJ before canonical-form evaluation, with Mandelstam weights alone or Mandelstam/Parke-Taylor weights. A nonzero chain with zero form is a kernel obstruction, not a refutation of every possible enriched cross-order complex."
    }
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    if not assertions["all_24_bcj_component_forms_zero"]: raise SystemExit(1)

if __name__=="__main__": main()
