#!/usr/bin/env python3
"""Project source derivatives of the seven lost fiber jets to the eight persistent occurrence directions."""
from __future__ import annotations
import contextlib, importlib, io, itertools, json, os, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(BEN/"checkers"),str(NCHK)]
P=int(sys.argv[1]); CHART=sys.argv[2] if len(sys.argv)>2 else "G12"; DEPTH=6
os.environ.update({"MARICI_FIELD_PRIME":str(P),"MARICI_RESIDUE_CHART":CHART,
 "MARICI_K_DEPTH":str(DEPTH),"MARICI_MAX_JET_ORDER":"0","MARICI_TWIST":"physical"})
with contextlib.redirect_stdout(io.StringIO()):
    jet=importlib.import_module("check_rank26_physical_source_covariant_jet_census")
base=jet.base
jet.K_DEPTH=DEPTH
jet.charts.GAMMA=jet.GAMMA; jet.charts.AMBIENT=14; jet.charts.CUTOFF=7; jet.charts.K_DEPTH=DEPTH
pres=jet.charts.presentation(jet.FIBER,jet.POINT,jet.NAMES)
k,q=jet.source_polynomials()
kd=[{e:jet.pder(poly,a) for e,poly in k.items()} for a in range(3)]
qd=[{n:{e:jet.pder(poly,a) for e,poly in qp.items()} for n,qp in q.items()} for a in range(3)]

lost_labels=(
 (0,1,1,1,1,1,(0,4)),(0,1,1,1,1,1,(0,5)),
 (0,1,1,1,1,1,(0,6)),(0,1,1,1,1,1,(0,7)),
 (0,1,1,1,1,1,(1,4)),(0,1,1,1,1,1,(4,0)),
 (0,1,1,1,1,1,(4,1)),
)
occurrence_labels=(
 (0,1,1,1,2,2,(0,0)),(0,1,1,2,1,2,(0,0)),
 (0,1,1,2,2,1,(0,0)),(0,1,2,1,2,1,(0,0)),
 (0,1,2,2,1,1,(0,0)),(0,2,1,1,1,2,(0,0)),
 (0,2,1,2,1,1,(0,0)),(0,2,2,1,1,1,(0,0)),
)

def reduced_label(label):
    return jet.prior.reduce_complete({pres["columns"][label]:1},pres["pivots"])

def insert(vector,coords,basis):
    vector=dict(vector); coords=dict(coords)
    while vector:
        pivot=min(vector)
        if pivot not in basis:
            inv=pow(vector[pivot],P-2,P)
            vector={c:(v*inv)%P for c,v in vector.items() if (v*inv)%P}
            coords={c:(v*inv)%P for c,v in coords.items() if (v*inv)%P}
            basis[pivot]=(vector,coords)
            return True
        row,known=basis[pivot]; factor=vector[pivot]
        for c,v in row.items():
            x=(vector.get(c,0)-factor*v)%P
            if x: vector[c]=x
            else: vector.pop(c,None)
        for c,v in known.items():
            x=(coords.get(c,0)-factor*v)%P
            if x: coords[c]=x
            else: coords.pop(c,None)
    return False

def project(vector,basis):
    vector=dict(vector); coords={}
    while vector:
        pivot=min(vector)
        if pivot not in basis: return None,vector
        row,known=basis[pivot]; factor=vector[pivot]
        for c,v in row.items():
            x=(vector.get(c,0)-factor*v)%P
            if x: vector[c]=x
            else: vector.pop(c,None)
        for c,v in known.items():
            x=(coords.get(c,0)-factor*v)%P
            if x: coords[c]=x
            else: coords.pop(c,None)
    return {c:(-v)%P for c,v in coords.items()}, {}

# Build the quotient coordinate frame L + U.
low_count=len(pres["low_labels"]); internal={}
for pivot in sorted(x for x in pres["pivots"] if x<low_count):
    row=pres["pivots"][pivot]; tail={c:v for c,v in row.items() if c!=pivot}
    other={q:r for q,r in pres["pivots"].items() if q!=pivot}
    rel={pivot:1,**jet.prior.reduce_complete(tail,other)}
    if any(c>=low_count for c in rel): raise RuntimeError("internal relation escaped low")
    base.add_pivot(rel,internal)
free_low=[c for c in range(low_count) if c not in internal]
frame={}
for c in free_low:
    if not insert(reduced_label(pres["ordered_columns"][c]),{},frame):
        raise RuntimeError("dependent low frame")
for j,label in enumerate(occurrence_labels):
    if not insert(reduced_label(label),{j:1},frame):
        raise RuntimeError(f"dependent occurrence quotient label {label}")

cache={}
def connection(column,axis):
    key=(column,axis)
    if key not in cache:
        cache[key]=jet.connection_poly(pres["ordered_columns"][column],axis,pres,kd[axis],qd[axis])
    return cache[key]

def differentiate(raw,axis):
    out={}
    for column,coefficient in raw.items():
        jet.row_add(out,column,jet.pder(coefficient,axis))
        for target,factor in connection(column,axis).items():
            jet.row_add(out,target,jet.pmul(coefficient,factor))
    return out

def evaluate(raw):
    numeric={c:jet.peval(poly,jet.POINT) for c,poly in raw.items() if jet.peval(poly,jet.POINT)}
    return jet.prior.reduce_complete(numeric,pres["pivots"])

def rank(vectors):
    span={}
    for v in vectors: base.add_pivot(dict(v),span)
    return len(span)

orders=[]
for length in (1,2):
    words=list(itertools.product(range(3),repeat=length))
    word_packets=[]; combined=[{} for _ in lost_labels]; vectors_by_word={}
    for wi,word in enumerate(words):
        vectors=[]; escaped=[]
        for di,label in enumerate(lost_labels):
            raw={pres["columns"][label]:{(0,0,0):1}}
            for axis in word: raw=differentiate(raw,axis)
            coordinates,residual=project(evaluate(raw),frame)
            if coordinates is None:
                escaped.append({
                  "domain_label":repr(label),
                  "residual_labels":[repr(pres["ordered_columns"][c]) for c in sorted(residual)[:20]],
                })
                coordinates={}
            vectors.append(coordinates)
            for j,value in coordinates.items(): combined[di][(wi,j)]=value
        vectors_by_word[word]=vectors
        word_packets.append({
          "word":list(word),"rank":rank(vectors),"escape_count":len(escaped),
          "matrix_rows":[[v.get(j,0) for j in range(8)] for v in vectors],
          "escape_examples":escaped[:5],
        })
    commutators=[]
    if length==2:
        for a in range(3):
            for b in range(a+1,3):
                differences=[]
                for left,right in zip(vectors_by_word[(a,b)],vectors_by_word[(b,a)]):
                    differences.append({
                      j:(left.get(j,0)-right.get(j,0))%P
                      for j in set(left)|set(right)
                      if (left.get(j,0)-right.get(j,0))%P
                    })
                commutators.append({"axes":[a,b],"rank":rank(differences)})
    orders.append({
      "derivative_order":length,
      "word_maps":word_packets,
      "combined_rank":rank(combined),
      "codomain_span_rank":rank([
        vector for vectors in vectors_by_word.values() for vector in vectors
      ]),
      "ordered_word_commutators":commutators,
      "all_routes_land_in_low_plus_occurrence":all(w["escape_count"]==0 for w in word_packets),
    })

packet={
 "schema":"marici.persistence-exchange-source-derivative.v1",
 "prime":P,"chart":CHART,"depth":DEPTH,
 "domain_labels":[repr(x) for x in lost_labels],
 "codomain_labels":[repr(x) for x in occurrence_labels],
 "orders":orders,
 "checks":{
   "domain_rank_7":len(lost_labels)==7,
   "codomain_rank_8":len(occurrence_labels)==8,
 },
}
packet["passed"]=all(packet["checks"].values())
out=BEN/"results"/f"persistence-exchange-source-derivative-{CHART.lower()}-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]: raise SystemExit(1)
