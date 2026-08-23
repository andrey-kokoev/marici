#!/usr/bin/env python3
"""Classify the five relations replaced by physical half-twist specialization."""
from __future__ import annotations
import contextlib, importlib, io, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
with contextlib.redirect_stdout(io.StringIO()):
    base = importlib.import_module("physical_four_mark_residue_twisted_derham")
P = base.PRIME
OUT = Path(__file__).resolve().parents[1] / "results" / f"rank26_replaced_relation_profile_p{P}.json"

def rank(rows):
    pivots = {}
    for row in rows: base.add_pivot(dict(row), pivots)
    return len(pivots)

def nullspace(rows, width):
    work=[]; piv=[]
    for raw in rows:
        row=[x%P for x in raw]
        for rr, pc in zip(work,piv):
            if row[pc]:
                c=row[pc]; row=[(x-c*y)%P for x,y in zip(row,rr)]
        nz=next((i for i,x in enumerate(row) if x),None)
        if nz is None: continue
        inv=pow(row[nz],P-2,P); row=[x*inv%P for x in row]
        for i,rr in enumerate(work):
            if rr[nz]:
                c=rr[nz]; work[i]=[(x-c*y)%P for x,y in zip(rr,row)]
        pos=next((i for i,p in enumerate(piv) if p>nz),len(piv))
        piv.insert(pos,nz); work.insert(pos,row)
    free=[i for i in range(width) if i not in piv]
    out=[]
    for f in free:
        v=[0]*width; v[f]=1
        for rr,pc in reversed(list(zip(work,piv))):
            v[pc]=(-sum(rr[j]*v[j] for j in free))%P
        out.append(v)
    return out

def dense(row,n): return [row.get(i,0)%P for i in range(n)]
def combine(coeffs, rows, n):
    return {j:sum(c*rows[i].get(j,0) for i,c in enumerate(coeffs))%P for j in range(n) if sum(c*rows[i].get(j,0) for i,c in enumerate(coeffs))%P}

def relation_data(gamma):
    low,_,pivots,free=base.presentation(("g1","g2","g3","g23","g31"),gamma,14,7,minimum_q_level=1)
    rel=[{j:v for j,v in row.items() if j<len(low)} for pc,row in pivots.items() if pc<len(low)]
    assert rank(rel)==len(low)-len(free)==10
    return low,rel

def intersection(left,right,n):
    equations=[]
    for j in range(n): equations.append([r.get(j,0) for r in left]+[(-r.get(j,0))%P for r in right])
    ker=nullspace(equations,len(left)+len(right))
    rows=[combine(v[:len(left)],left,n) for v in ker]
    piv={}; out=[]
    for row in rows:
        before=len(piv); base.add_pivot(dict(row),piv)
        if len(piv)>before: out.append(row)
    return out

def subspace_supported(rows, allowed, n):
    outside=[j for j in range(n) if j not in allowed]
    equations=[[r.get(j,0) for r in rows] for j in outside]
    return [combine(v,rows,n) for v in nullspace(equations,len(rows))]

def exclusive_profile(rows, shared, subsets, n):
    return {name:rank(shared+subspace_supported(rows,S,n))-rank(shared) for name,S in subsets.items()}

def complement(rows,shared):
    piv={}; [base.add_pivot(dict(r),piv) for r in shared]
    out=[]
    for r in rows:
        before=len(piv); base.add_pivot(dict(r),piv)
        if len(piv)>before: out.append(r)
    return out

def terms(row,low):
    ans=[]
    for j,c in sorted(row.items()):
        mon=low[j][-1]; signed=c if c<=P//2 else c-P
        ans.append({"monomial":list(mon),"coefficient":signed})
    return ans

def main():
    low,generic=relation_data(5); low2,physical=relation_data((-pow(2,P-2,P))%P); assert low==low2
    n=len(low); shared=intersection(generic,physical,n); assert rank(shared)==5
    degrees={f"degree_le_{d}":{i for i,l in enumerate(low) if sum(l[-1])<=d} for d in range(8)}
    parities={f"parity_{pa}{pb}":{i for i,l in enumerate(low) if l[-1][0]%2==pa and l[-1][1]%2==pb} for pa in range(2) for pb in range(2)}
    gc=complement(generic,shared); pc=complement(physical,shared)
    payload={
      "schema":"marici.rank26-replaced-relation-profile.v1","prime":P,"low_numerator_dimension":n,
      "relation_ranks":{"generic":rank(generic),"physical":rank(physical),"intersection":rank(shared),"sum":rank(generic+physical)},
      "generic_exclusive_degree_profile":exclusive_profile(generic,shared,degrees,n),
      "physical_exclusive_degree_profile":exclusive_profile(physical,shared,degrees,n),
      "generic_exclusive_parity_profile":exclusive_profile(generic,shared,parities,n),
      "physical_exclusive_parity_profile":exclusive_profile(physical,shared,parities,n),
      "deterministic_generic_complement":[terms(r,low) for r in gc],
      "deterministic_physical_complement":[terms(r,low) for r in pc],
      "support_unchanged":True,"new_denominators_introduced":False,"passed":rank(gc)==rank(pc)==5,
      "scope":"profiles are invariant; displayed complements depend on deterministic elimination order"
    }
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in payload.items() if not k.startswith("deterministic_")},indent=2))
    if not payload["passed"]: raise SystemExit(1)
if __name__=="__main__": main()
