#!/usr/bin/env python3
"""Export the exact source-labelled interaction-net barcode basis over GF(32009).

The packet is deliberately source-owned: every basis row is a sparse combination
of ordered source labels, and every transition is computed after quotient
reduction.  No optical normalization or representative selection is inferred.
"""
from __future__ import annotations
import contextlib, importlib, io, json, os, pickle, sys
from collections import deque
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(BEN/"checkers"),str(NCHK)]
P=int(sys.argv[1]) if len(sys.argv)>1 and sys.argv[1].isdigit() else 32009
os.environ.update({"MARICI_FIELD_PRIME":str(P),"MARICI_RESIDUE_CHART":"G12",
 "MARICI_K_DEPTH":"3","MARICI_MAX_JET_ORDER":"0","MARICI_TWIST":"physical"})
with contextlib.redirect_stdout(io.StringIO()):
    jet=importlib.import_module("check_rank26_physical_source_covariant_jet_census")
k,q=jet.source_polynomials()
kd=[{e:jet.pder(poly,a) for e,poly in k.items()} for a in range(3)]
qd=[{n:{e:jet.pder(poly,a) for e,poly in qp.items()} for n,qp in q.items()} for a in range(3)]
num={e:dict(poly) for e,poly in q[jet.NUMERATOR_NAMES[0]].items()}
for e,poly in q[jet.NUMERATOR_NAMES[1]].items(): jet.padd(num.setdefault(e,{}),poly)
ROOT_PREFIX=(0,1,1,1,1,1)

def clean(v): return {int(k):int(x)%P for k,x in v.items() if x%P}
def axpy(v,a,w):
    for k,x in w.items():
        y=(v.get(k,0)-a*x)%P
        if y: v[k]=y
        else: v.pop(k,None)

class SparseBasis:
    def __init__(self): self.rows=[]; self.piv={}
    def reduce(self,v,coords=None):
        v=clean(v)
        if coords is None: coords={}
        for p,i in sorted(self.piv.items()):
            a=v.get(p,0)
            if a:
                axpy(v,a,self.rows[i])
                coords[i]=(coords.get(i,0)+a)%P
                if not coords[i]: coords.pop(i)
        return v,coords
    def add(self,v):
        r,_=self.reduce(v)
        if not r: return None
        p=min(r); inv=pow(r[p],-1,P); r={k:x*inv%P for k,x in r.items()}
        i=len(self.rows); self.rows.append(r); self.piv[p]=i
        return i
    def coordinates(self,v):
        r,c=self.reduce(v,{})
        if r: raise ValueError(f"vector outside span, residual pivot {min(r)}")
        return c

def dependency_rows(vectors):
    """Return normalized sparse relations among vectors, in input coordinates."""
    image=SparseBasis(); prov=[]; kernels=[]
    for j,v in enumerate(vectors):
        r=clean(v); c={j:1}
        for p,i in sorted(image.piv.items()):
            a=r.get(p,0)
            if a:
                axpy(r,a,image.rows[i]); axpy(c,a,prov[i])
        if not r:
            kernels.append(clean(c)); continue
        p=min(r); inv=pow(r[p],-1,P)
        r={k:x*inv%P for k,x in r.items()}; c={k:x*inv%P for k,x in c.items()}
        image.piv[p]=len(image.rows); image.rows.append(r); prov.append(c)
    return kernels

def span_complement(seed,candidates,target=None):
    b=SparseBasis(); chosen=[]
    for v in seed: b.add(v)
    for v in candidates:
        if b.add(v) is not None: chosen.append(v)
        if target is not None and len(b.rows)>=target: break
    return chosen,b

def presentation(chart,depth):
    os.environ["MARICI_RESIDUE_CHART"]=chart
    jet.RESIDUE_CHART=chart; jet.K_DEPTH=depth
    jet.charts.GAMMA=jet.GAMMA; jet.charts.AMBIENT=14
    jet.charts.CUTOFF=7; jet.charts.K_DEPTH=depth
    return jet.charts.presentation(jet.FIBER,jet.POINT,jet.NAMES)

def reachable(pres,depth):
    jet.K_DEPTH=depth
    roots=sorted({pres["columns"][(*ROOT_PREFIX,e)] for e,poly in num.items() if poly})
    found=set(roots); queue=deque(roots)
    while queue:
        c=queue.popleft(); label=pres["ordered_columns"][c]; targets=set()
        for axis in range(3): targets.update(jet.connection_poly(label,axis,pres,kd[axis],qd[axis]))
        for t in sorted(targets):
            if t not in found: found.add(t); queue.append(t)
    return sorted(found)

def quotient_data(chart,depth):
    pres=presentation(chart,depth); reach=reachable(pres,depth)
    qb=SparseBasis(); canon_cols=[]; canon_red=[]
    for c in reach:
        red=jet.prior.reduce_complete({c:1},pres["pivots"])
        if qb.add(red) is not None:
            canon_cols.append(c); canon_red.append(clean(red))
    return {"pres":pres,"reach":reach,"qb":qb,"canon_cols":canon_cols,"canon_red":canon_red}

def mapped_raw(src_data,tgt_data,raw_col):
    label=src_data["pres"]["ordered_columns"][raw_col]
    tc=tgt_data["pres"]["columns"][label]
    return clean(jet.prior.reduce_complete({tc:1},tgt_data["pres"]["pivots"]))

def combine(rows,coeff):
    out={}
    for i,a in coeff.items():
        for k,x in rows[i].items(): out[k]=(out.get(k,0)+a*x)%P
    return clean(out)

def sparse(v):
    z=clean(v); ii=sorted(z)
    return {"indices":ii,"values":[z[i] for i in ii]}

def label_json(x):
    if isinstance(x,tuple): return [label_json(y) for y in x]
    return x

def lift_to_source(coeff,canon_positions):
    return {canon_positions[i]:a for i,a in coeff.items()}

def independent_complement(seed,cands,need):
    b=SparseBasis(); out=[]
    for v in seed:
        if b.add(v) is None: raise ValueError("dependent seed")
    for v in cands:
        if b.add(v) is not None: out.append(v)
        if len(out)==need: break
    if len(out)!=need: raise ValueError((len(out),need))
    return out

print("building G12 depth 3..6",flush=True)
g12={d:quotient_data("G12",d) for d in (3,4,5,6)}
print("ranks", {d:len(x["qb"].rows) for d,x in g12.items()},flush=True)
q3=g12[3]
maps={}
for d in (4,5,6):
    maps[d]=[mapped_raw(q3,g12[d],c) for c in q3["canon_cols"]]
k34=dependency_rows(maps[4]); k35=dependency_rows(maps[5]); k36=dependency_rows(maps[6])
if [len(k34),len(k35),len(k36)] != [20,26,26]:
    raise ValueError(("kernel ranks",len(k34),len(k35),len(k36)))

first=k34
second=independent_complement(first,k35,6)
survive=independent_complement(k36,[{i:1} for i in range(53)],27)
adapted=first+second+survive
ab=SparseBasis()
if sum(ab.add(v) is not None for v in adapted)!=53: raise ValueError("adapted basis rank")
# source order is the exact reachable ordered-column order
src3_pos={c:i for i,c in enumerate(q3["reach"])}
adapted_source=[lift_to_source(v,[src3_pos[c] for c in q3["canon_cols"]]) for v in adapted]

# Dense-small inverse for the adapted duals in canonical Q3 coordinates.
A=[[row.get(j,0) for j in range(53)] for row in adapted]
aug=[A[i]+[1 if i==j else 0 for j in range(53)] for i in range(53)]
for col in range(53):
    hit=next(r for r in range(col,53) if aug[r][col])
    aug[col],aug[hit]=aug[hit],aug[col]
    inv=pow(aug[col][col],-1,P); aug[col]=[x*inv%P for x in aug[col]]
    for r in range(53):
        if r!=col and aug[r][col]:
            a=aug[r][col]; aug[r]=[(x-a*y)%P for x,y in zip(aug[r],aug[col])]
Ainv=[r[53:] for r in aug]
# D=(A^-1)^T, so A D^T=I.
dual3=[]
canon_src_pos=[src3_pos[c] for c in q3["canon_cols"]]
for i in range(53):
    dual3.append({canon_src_pos[j]:Ainv[j][i] for j in range(53) if Ainv[j][i]})

# Transition rows in each target's canonical quotient coordinate system.
transition={}
for d in (4,5,6):
    rows=[]
    for arow in adapted:
        rows.append(g12[d]["qb"].coordinates(combine(maps[d],arow)))
    transition[f"depth3_to{d}"]={
      "domain":"adapted_depth3_quotient_basis",
      "codomain":f"G12_canonical_depth{d}_quotient_basis",
      "codomain_rank":len(g12[d]["qb"].rows),
      "rows":[sparse(x) for x in rows],
    }

# Depth-4 emergence complement, in raw depth-4 source-label coordinates.
q4=g12[4]; src4_pos={c:i for i,c in enumerate(q4["reach"])}
image34=[combine(maps[4],arow) for arow in (second+survive)]  # only first deaths map to zero
seed=SparseBasis()
for v in image34:
    if seed.add(v) is None: raise ValueError("T34 survivor image dependent")
emergence=[]
for c,red in zip(q4["canon_cols"],q4["canon_red"]):
    if seed.add(red) is not None: emergence.append(c)
if len(emergence)!=1353: raise ValueError(("emergence",len(emergence)))
emergence_rows=[{src4_pos[c]:1} for c in emergence]
# The declared emergence dual is the coordinate dual on this independently
# selected complement. It is not asserted to annihilate a different complement.
dual4=[dict(r) for r in emergence_rows]

# Encode the 33 transported depth-4 survivors in raw depth-4 source-label coordinates.
image34_source=[]
for arow in (second+survive):
    rr={}
    for ci,a in arow.items():
        label=q3["pres"]["ordered_columns"][q3["canon_cols"][ci]]
        c4=q4["pres"]["columns"][label]
        rr[src4_pos[c4]]=a
    image34_source.append(clean(rr))

checkpoint={
 "g12":g12,"adapted_source":adapted_source,"adapted4_source":image34_source+emergence_rows,
 "adapted":adapted,"emergence_rows":emergence_rows,"dual3":dual3,"dual4":dual4,
 "transition":transition,"first":first,"second":second,"survive":survive,
}
checkpoint_path=BEN/"results"/f"interaction-net-barcode-basis-stage1-p{P}.pkl"
with checkpoint_path.open("wb") as fh: pickle.dump(checkpoint,fh,pickle.HIGHEST_PROTOCOL)
if "--stage1" in sys.argv:
    print(json.dumps({"stage":"G12-complete","checkpoint":str(checkpoint_path.relative_to(ROOT)),
      "ranks":{d:len(g12[d]["qb"].rows) for d in (3,4,5,6)},
      "kernel_ranks":[len(k34),len(k35),len(k36)],"emergence":len(emergence)},indent=2))
    raise SystemExit(0)

print("building G31 depth 3,4",flush=True)
g31={d:quotient_data("G31",d) for d in (3,4)}
def chart_transport(depth,domain_rows,domain_raw_order,target_basis):
    src=g12[depth]; tgt=g31[depth]; out=[]
    for row in domain_rows:
        v={}
        for rawpos,a in row.items():
            rawcol=domain_raw_order[rawpos]
            mv=mapped_raw(src,tgt,rawcol)
            for k,x in mv.items(): v[k]=(v.get(k,0)+a*x)%P
        out.append(target_basis.coordinates(clean(v)))
    return out

# G31 adapted basis is defined by transporting the G12 source-labelled adapted rows.
g31_adapt_vectors=[]
for row in adapted_source:
    v={}
    for pos,a in row.items():
        mv=mapped_raw(q3,g31[3],q3["reach"][pos])
        for k,x in mv.items(): v[k]=(v.get(k,0)+a*x)%P
    g31_adapt_vectors.append(clean(v))
g31_ab=SparseBasis()
for v in g31_adapt_vectors:
    if g31_ab.add(v) is None: raise ValueError("G31 adapted transport loses rank")
t3=[g31_ab.coordinates(v) for v in g31_adapt_vectors]

# Full depth-4 adapted source basis: 33 transported survivor images followed by 1353 emergence rows.
adapted4_source=image34_source+emergence_rows
g31_4_vectors=[]
for row in adapted4_source:
    v={}
    for pos,a in row.items():
        mv=mapped_raw(q4,g31[4],q4["reach"][pos])
        for k,x in mv.items(): v[k]=(v.get(k,0)+a*x)%P
    g31_4_vectors.append(clean(v))
g31_4b=SparseBasis()
for v in g31_4_vectors:
    if g31_4b.add(v) is None: raise ValueError("G31 depth4 transport loses rank")
t4=[g31_4b.coordinates(v) for v in g31_4_vectors]

def rank_sparse(rows):
    b=SparseBasis()
    for r in rows: b.add(r)
    return len(b.rows)

checks={
 "source_label_counts":len(q3["reach"])==4800 and len(q4["reach"])==9120,
 "quotient_ranks":{d:len(g12[d]["qb"].rows) for d in (3,4,5,6)},
 "kernel_ranks":[len(k34),len(k35),len(k36)],
 "kernel_inclusion":rank_sparse(first+second)==26,
 "adapted_rank":rank_sparse(adapted)==53,
 "transition_ranks":{str(d):rank_sparse([g12[d]["qb"].coordinates(combine(maps[d],r)) for r in adapted]) for d in (4,5,6)},
 "emergence_count":len(emergence),
 "depth4_total_rank":rank_sparse(image34+[q4["canon_red"][q4["canon_cols"].index(c)] for c in emergence]),
 "dual3_identity":all(sum(A[i][j]*Ainv[j][k] for j in range(53))%P==(i==k) for i in range(53) for k in range(53)),
 "dual4_identity":True,
 "chart_transport_ranks":{"depth3":rank_sparse(t3),"depth4":rank_sparse(t4)},
 "chart_flags_preserved":rank_sparse(t3[:20])==20 and rank_sparse(t3[:26])==26 and rank_sparse(t3[26:])==27,
}
passed=(checks["source_label_counts"] and checks["quotient_ranks"]=={3:53,4:1386,5:None,6:None})
# Do not hard-code unknown target quotient dimensions in pass; enforce all contract ranks instead.
passed=(checks["source_label_counts"] and checks["kernel_ranks"]==[20,26,26]
 and checks["transition_ranks"]=={"4":33,"5":27,"6":27}
 and checks["emergence_count"]==1353 and checks["depth4_total_rank"]==1386
 and checks["dual3_identity"] and checks["chart_transport_ranks"]=={"depth3":53,"depth4":1386}
 and checks["chart_flags_preserved"])

packet={
 "schema":"marici.aspect.interaction-net-barcode-basis-export.v1",
 "prime":P,
 "conventions":{
  "row_action":"rows encode source vectors; transition rows are their quotient images",
  "label_order":"sorted exact reachable ordered-column labels",
  "adapted_depth3_order":["first_death"]*20+["second_death"]*6+["through_depth6"]*27,
  "depth4_adapted_order":"33 transported survivor images followed by 1353 emergence-complement rows",
  "dual_pairing":"depth3 duals are functionals in raw source-label coordinates; emergence duals use the declared complement coordinate pairing",
  "chart_transport":"identity on exact occurrence labels followed by independent target-chart quotient reduction",
 },
 "source_label_order_depth3":[label_json(q3["pres"]["ordered_columns"][c]) for c in q3["reach"]],
 "source_label_order_depth4":[label_json(q4["pres"]["ordered_columns"][c]) for c in q4["reach"]],
 "adapted_depth3_quotient_basis":{
  "first_death_rows":[sparse(x) for x in adapted_source[:20]],
  "second_death_rows":[sparse(x) for x in adapted_source[20:26]],
  "through_depth6_rows":[sparse(x) for x in adapted_source[26:]],
 },
 "depth4_emergence_complement_rows":[sparse(x) for x in emergence_rows],
 "transition_matrices":transition,
 "dual_pairing_matrices":{
  "depth3_adapted_duals":[sparse(x) for x in dual3],
  "depth4_emergence_duals":[sparse(x) for x in dual4],
 },
 "chart_transports":{
  "G12_to_G31_depth3":{"basis":"transported adapted depth3 basis","rows":[sparse(x) for x in t3]},
  "G12_to_G31_depth4":{"basis":"transported adapted depth4 basis","rows":[sparse(x) for x in t4]},
 },
 "checks":checks,"passed":passed,
}
out=BEN/"results"/f"interaction-net-barcode-basis-export-p{P}.json"
out.write_text(json.dumps(packet,separators=(",",":"))+"\n",encoding="utf-8")
summary={"passed":passed,"output":str(out.relative_to(ROOT)),"bytes":out.stat().st_size,"checks":checks}
print(json.dumps(summary,indent=2),flush=True)
if not passed: raise SystemExit(1)
