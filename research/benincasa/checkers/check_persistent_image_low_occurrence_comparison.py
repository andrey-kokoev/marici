#!/usr/bin/env python3
"""Compare the persistent K-depth image with the rank-26 low sector and ten Boolean occurrence classes."""
from __future__ import annotations
import contextlib, importlib, io, json, os, sys
from collections import deque
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(BEN/"checkers"),str(NCHK)]
P=int(sys.argv[1]); CHART=sys.argv[2] if len(sys.argv)>2 else "G12"
SOURCE_DEPTH=int(sys.argv[3]) if len(sys.argv)>3 else 3
TARGET_DEPTH=int(sys.argv[4]) if len(sys.argv)>4 else 6
os.environ.update({"MARICI_FIELD_PRIME":str(P),"MARICI_RESIDUE_CHART":CHART,
 "MARICI_K_DEPTH":str(SOURCE_DEPTH),"MARICI_MAX_JET_ORDER":"0","MARICI_TWIST":"physical"})
with contextlib.redirect_stdout(io.StringIO()):
    jet=importlib.import_module("check_rank26_physical_source_covariant_jet_census")
base=jet.base
k,q=jet.source_polynomials()
kd=[{e:jet.pder(poly,a) for e,poly in k.items()} for a in range(3)]
qd=[{n:{e:jet.pder(poly,a) for e,poly in qp.items()} for n,qp in q.items()} for a in range(3)]
numerator={e:dict(poly) for e,poly in q[jet.NUMERATOR_NAMES[0]].items()}
for e,poly in q[jet.NUMERATOR_NAMES[1]].items(): jet.padd(numerator.setdefault(e,{}),poly)
root_prefix=(0,1,1,1,1,1)
adapters=(
 (0,1,2,1,2,1,(0,0)),(0,1,1,2,2,1,(0,0)),
 (0,1,2,2,1,1,(0,0)),(0,2,2,1,1,1,(0,0)),
 (0,2,1,1,1,2,(0,0)),(0,2,1,2,1,1,(0,0)),
 (0,1,1,2,1,2,(0,0)),(0,2,1,1,2,1,(0,0)),
 (0,1,2,1,1,2,(0,0)),(0,1,1,1,2,2,(0,0)),
)

def presentation(depth):
    jet.K_DEPTH=depth
    jet.charts.GAMMA=jet.GAMMA; jet.charts.AMBIENT=14
    jet.charts.CUTOFF=7; jet.charts.K_DEPTH=depth
    return jet.charts.presentation(jet.FIBER,jet.POINT,jet.NAMES)

def reachable(pres,depth):
    jet.K_DEPTH=depth
    roots=sorted({pres["columns"][(*root_prefix,e)] for e,poly in numerator.items() if poly})
    found=set(roots); queue=deque(roots)
    while queue:
        c=queue.popleft(); label=pres["ordered_columns"][c]; targets=set()
        for axis in range(3): targets.update(jet.connection_poly(label,axis,pres,kd[axis],qd[axis]))
        for t in sorted(targets):
            if t not in found: found.add(t); queue.append(t)
    return found

def add_reduced(label,pres,span):
    c=pres["columns"][label]
    red=jet.prior.reduce_complete({c:1},pres["pivots"])
    return base.add_pivot(dict(red),span)

def reduced_vector(label,pres):
    c=pres["columns"][label]
    return jet.prior.reduce_complete({c:1},pres["pivots"])

def insert_with_provenance(vector,coefficients,basis):
    vector=dict(vector); coefficients=dict(coefficients)
    while vector:
        pivot=min(vector)
        if pivot not in basis:
            inv=pow(vector[pivot],P-2,P)
            vector={c:(v*inv)%P for c,v in vector.items() if (v*inv)%P}
            coefficients={c:(v*inv)%P for c,v in coefficients.items() if (v*inv)%P}
            basis[pivot]=(vector,coefficients)
            return True,None
        row,provenance=basis[pivot]
        factor=vector[pivot]
        for c,v in row.items():
            value=(vector.get(c,0)-factor*v)%P
            if value: vector[c]=value
            else: vector.pop(c,None)
        for c,v in provenance.items():
            value=(coefficients.get(c,0)-factor*v)%P
            if value: coefficients[c]=value
            else: coefficients.pop(c,None)
    return False,coefficients

def linear_combination(generators,coefficients):
    result={}
    for i,a in coefficients.items():
        for c,v in generators[i].items():
            value=(result.get(c,0)+a*v)%P
            if value: result[c]=value
            else: result.pop(c,None)
    return result

source=presentation(SOURCE_DEPTH); target=presentation(TARGET_DEPTH)
source_reachable=reachable(source,SOURCE_DEPTH)
image={}
image_generators=[]; image_generator_labels=[]
for c in sorted(source_reachable):
    label=source["ordered_columns"][c]
    red=reduced_vector(label,target)
    before=len(image)
    base.add_pivot(dict(red),image)
    if len(image)>before:
        image_generators.append(red)
        image_generator_labels.append(label)

low_count=len(target["low_labels"])
internal={}
for pivot in sorted(x for x in target["pivots"] if x<low_count):
    row=target["pivots"][pivot]; tail={c:v for c,v in row.items() if c!=pivot}
    other={q:r for q,r in target["pivots"].items() if q!=pivot}
    rel={pivot:1,**jet.prior.reduce_complete(tail,other)}
    if any(c>=low_count for c in rel): raise RuntimeError("internal relation escaped low sector")
    base.add_pivot(rel,internal)
free_low=[c for c in range(low_count) if c not in internal]
low={}
low_generators=[]; low_generator_labels=[]
for c in free_low:
    label=target["ordered_columns"][c]
    red=reduced_vector(label,target)
    before=len(low)
    base.add_pivot(dict(red),low)
    if len(low)>before:
        low_generators.append(red)
        low_generator_labels.append(label)

union=dict(image)
for row in low.values(): base.add_pivot(dict(row),union)
intersection_dim=len(image)+len(low)-len(union)

# Canonical labelled complements and an exact intersection basis.
joint_basis={}
for i,vector in enumerate(image_generators):
    independent,_=insert_with_provenance(vector,{i:1},joint_basis)
    if not independent: raise RuntimeError("image generator list is dependent")
low_external=[]; intersection=[]
offset=len(image_generators)
for j,vector in enumerate(low_generators):
    independent,relation=insert_with_provenance(vector,{offset+j:1},joint_basis)
    if independent:
        low_external.append(j)
        continue
    image_coeff={i:(-a)%P for i,a in relation.items() if i<offset}
    common=linear_combination(image_generators,image_coeff)
    if not common: raise RuntimeError("zero vector in intersection basis")
    intersection.append({
      "image_coefficients":[
        {"source_label":repr(image_generator_labels[i]),"coefficient":a}
        for i,a in sorted(image_coeff.items()) if a
      ],
      "ambient_representative":[
        {"label":repr(target["ordered_columns"][c]),"coefficient":a}
        for c,a in sorted(common.items())
      ],
    })

low_first={}
for vector in low_generators: insert_with_provenance(vector,{},low_first)
image_external=[]
for i,vector in enumerate(image_generators):
    independent,_=insert_with_provenance(vector,{i:1},low_first)
    if independent: image_external.append(i)

adapter_rows=[]
for label in adapters:
    span=dict(low)
    before=len(span)
    add_reduced(label,target,span)
    added=len(span)>before
    union_with_image=dict(image)
    for row in span.values(): base.add_pivot(dict(row),union_with_image)
    adapter_rows.append({
      "label":repr(label),
      "adds_to_low":bool(added),
      "low_plus_adapter_rank":len(span),
      "image_plus_low_plus_adapter_rank":len(union_with_image),
      "lies_in_image_plus_low":len(union_with_image)==len(union),
      "completes_image_over_low":len(union)==len(image) and len(span)==len(image) and len(union_with_image)==len(image),
    })

packet={
 "schema":"marici.persistent-image-low-occurrence-comparison.v1",
 "prime":P,"chart":CHART,"source_depth":SOURCE_DEPTH,"target_depth":TARGET_DEPTH,
 "source_reachable_count":len(source_reachable),
 "persistent_image_rank":len(image),"low_rank":len(low),
 "image_plus_low_rank":len(union),"image_low_intersection_rank":intersection_dim,
 "low_is_contained_in_image":len(union)==len(image),
 "persistent_quotient_over_low_rank":len(image)-intersection_dim,
 "intersection_basis":intersection,
 "low_external_labels":[repr(low_generator_labels[j]) for j in low_external],
 "persistent_external_source_labels":[repr(image_generator_labels[i]) for i in image_external],
 "adapter_tests":adapter_rows,
 "checks":{
   "expected_image_rank_27":len(image)==27,
   "expected_low_rank_26":len(low)==26,
   "rank_formula":intersection_dim==len(image)+len(low)-len(union),
   "intersection_basis_rank_19":len(intersection)==intersection_dim==19,
   "low_external_rank_7":len(low_external)==len(low)-intersection_dim==7,
   "persistent_external_rank_8":len(image_external)==len(image)-intersection_dim==8,
 },
}
packet["passed"]=all(packet["checks"].values())
out=BEN/"results"/f"persistent-image-low-occurrence-comparison-{CHART.lower()}-p{P}-k{SOURCE_DEPTH}-to{TARGET_DEPTH}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]: raise SystemExit(1)
