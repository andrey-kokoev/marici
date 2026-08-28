#!/usr/bin/env python3
"""Construct occurrence transport directly on the repaired low quotients."""
from __future__ import annotations
import contextlib, importlib, io, json, os, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"
sys.path[:0]=[str(BEN),str(BEN/"checkers")]
P=int(sys.argv[1]) if len(sys.argv)>1 else int(os.environ.get("MARICI_FIELD_PRIME","32009"))
os.environ["MARICI_FIELD_PRIME"]=str(P)
with contextlib.redirect_stdout(io.StringIO()):
    base=importlib.import_module("physical_four_mark_residue_twisted_derham")
    charts=importlib.import_module("g12_g31_residue_chart_transition")
    l5s=importlib.import_module("check_rank26_anti_invariant_infinity_map")
    l5t=importlib.import_module("check_rank5_g12_g31_naturality")

def reduce(row,piv):
    row=dict(row)
    while True:
        active=[c for c in row if c in piv]
        if not active:return row
        c=max(active); a=row[c]
        for j,v in piv[c].items():base.add_value(row,j,-a*v)

def internal_low(pres):
    count=len(pres["low_labels"]); piv={}
    for p in sorted(x for x in pres["pivots"] if x<count):
        row=pres["pivots"][p]; tail={c:v for c,v in row.items() if c!=p}
        other={q:r for q,r in pres["pivots"].items() if q!=p}
        rel={p:1,**reduce(tail,other)}
        assert all(c<count for c in rel)
        base.add_pivot(rel,piv)
    free=[c for c in range(count) if c not in piv]
    return piv,free,{c:i for i,c in enumerate(free)}

def qrow(pres,piv,pos,exp,sign=1):
    label=(0,1,1,1,1,1,exp)
    row=reduce({pres["columns"][label]:sign%P},piv)
    assert all(c in pos for c in row)
    return {pos[c]:v for c,v in row.items()}

def rank(rows):
    piv={}
    for r in rows:
        row={i:v for i,v in enumerate(r) if v}
        base.add_pivot(row,piv)
    return len(piv)

def dense(row,n=26):return [row.get(i,0) for i in range(n)]
def matmul(a,b):return [[sum(x*y for x,y in zip(r,c))%P for c in zip(*b)] for r in a]
def inverse(a):
    n=len(a); w=[[x%P for x in r]+[int(i==j) for j in range(n)] for i,r in enumerate(a)]
    for c in range(n):
        k=next(i for i in range(c,n) if w[i][c]);w[c],w[k]=w[k],w[c]
        iv=pow(w[c][c],P-2,P);w[c]=[x*iv%P for x in w[c]]
        for i in range(n):
            if i!=c and w[i][c]:
                q=w[i][c];w[i]=[(x-q*y)%P for x,y in zip(w[i],w[c])]
    return [r[n:] for r in w]

half=(-pow(2,P-2,P))%P
charts.GAMMA=half;charts.AMBIENT=14;charts.CUTOFF=7;charts.K_DEPTH=3
s=charts.presentation(base.fiber_data,charts.SOURCE_POINT,charts.SOURCE_NAMES)
t=charts.presentation(charts.g31_fiber_data,charts.TARGET_POINT,charts.TARGET_NAMES)
sp,sf,spos=internal_low(s);tp,tf,tpos=internal_low(t)

relation_failures=[]
for pivot,row in sp.items():
    mapped={}
    for c,v in row.items():
        exp=s["ordered_columns"][c][-1]
        raw=qrow(t,tp,tpos,(exp[1],exp[0]),-v)
        for j,w in raw.items():base.add_value(mapped,j,w)
    if mapped:relation_failures.append(pivot)

T=[[0]*26 for _ in range(26)]
for j,c in enumerate(sf):
    exp=s["ordered_columns"][c][-1]
    for i,v in qrow(t,tp,tpos,(exp[1],exp[0]),-1).items():T[i][j]=v
Ti=inverse(T)

def l5rows(pres,free,table):
    rows=[[0]*26 for _ in range(5)]
    for j,c in enumerate(free):
        exp=pres["ordered_columns"][c][-1]
        for i,v in enumerate(table[exp]):rows[i][j]=v%P
    return rows

Ls=l5rows(s,sf,l5s.coordinates); Lt=l5rows(t,tf,l5t.target_coordinates)
transported=matmul(Ls,Ti)
checks={
 "source_internal_relation_count_10":len(sp)==10,
 "target_internal_relation_count_10":len(tp)==10,
 "source_relations_map_to_zero":not relation_failures,
 "transition_rank_26":rank(T)==26,
 "repaired_transition_preserves_L5":rank(Lt+transported)==5,
 "residual_A7_gate_remains_unavailable":True,
}
packet={
 "schema":"marici.repaired-low-occurrence-transition.v1","prime":P,
 "source_rank":len(sf),"target_rank":len(tf),
 "source_relation_failure_count":len(relation_failures),
 "checks":checks,"passed":all(checks.values()),
 "conclusion":"The occurrence transition exists canonically on the repaired low quotient and preserves L5. An action on A7/L5 still requires A7 to be independently reconstructed in this repaired quotient convention; legacy A7 coordinates cannot supply it."
}
out=ROOT/"research"/"benincasa"/"results"/f"repaired-low-occurrence-transition-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]:raise SystemExit(1)
