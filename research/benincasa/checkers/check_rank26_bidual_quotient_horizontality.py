#!/usr/bin/env python3
"""Reduce the rank-26 presentation over the mixed gamma/kinematic bidual ring."""
from __future__ import annotations
import importlib,json,os,sys
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; P=int(os.environ.get("MARICI_FIELD_PRIME","32009")); AX=int(os.environ.get("MARICI_PARAMETER_AXIS","0"))
POINT=tuple(int(os.environ.get(n,d)) for n,d in (("MARICI_SOURCE_X","2"),("MARICI_SOURCE_Y","3"),("MARICI_SOURCE_Z","4")))
psuffix="" if POINT==(2,3,4) else "-at-"+"-".join(map(str,POINT))
suffix=("" if P==32009 else f"-p{P}")+f"-{'x' if AX==0 else 'y'}"+psuffix
OUT=ROOT/"research"/"benincasa"/"results"/f"rank26-bidual-quotient-horizontality{suffix}.json"
os.environ["MARICI_FIELD_PRIME"]=str(P); sys.path.insert(0,str(ROOT/"research"/"benincasa")); base=importlib.import_module("physical_four_mark_residue_twisted_derham")
Z=(0,0,0,0)
def A(a,b): return tuple((x+y)%P for x,y in zip(a,b))
def M(a,b):
 a0,ag,ax,agx=a; b0,bg,bx,bgx=b
 return (a0*b0%P,(a0*bg+ag*b0)%P,(a0*bx+ax*b0)%P,(a0*bgx+ag*bx+ax*bg+agx*b0)%P)
def I(a):
 a0,ag,ax,agx=a; q=pow(a0,-1,P)
 return (q,-ag*q*q%P,-ax*q*q%P,(-agx*q*q+2*ag*ax*q*q*q)%P)
def S(a,n): return tuple(n*x%P for x in a)
def put(r,c,v):
 v=A(r.get(c,Z),v)
 if v!=Z:r[c]=v
 else:r.pop(c,None)
def pivot(r,ps):
 while any(v[0] for v in r.values()):
  c=max(k for k,v in r.items() if v[0]); q=r[c]
  if c not in ps: ps[c]={k:M(v,I(q)) for k,v in r.items()}; return
  for k,v in ps[c].items():put(r,k,S(M(q,v),-1))
def red(r,ps):
 r=dict(r)
 while any(v[0] for v in r.values()):
  c=max(k for k,v in r.items() if v[0])
  if c not in ps:break
  q=r[c]
  for k,v in ps[c].items():put(r,k,S(M(q,v),-1))
 return r
def coeffs(p0,px):
 return {e:(p0.get(e,0),0,px.get(e,0),0) for e in set(p0)|set(px)}
def presentation():
 names=("g1","g2","g3","g23","g31"); k,aq=base.fiber_data(*POINT); kx,aqx=base.parameter_derivative_data(AX,POINT); qs=[aq[n] for n in names]; qxs=[aqx[n] for n in names]
 low=[(0,*ls,m) for ls in product(range(1,2),repeat=5) for m in base.monomials_at_most(7)]; lowset=set(low); ordered=list(low)
 for kp in range(3):
  for ls in product(range(1,3),repeat=5):ordered.extend(t for m in base.monomials_at_most(18) if (t:=(kp,*ls,m)) not in lowset)
 cols={x:i for i,x in enumerate(ordered)}; ps={}; gamma=-pow(2,-1,P)%P
 kd=[(base.derivative(k,a),base.derivative(kx,a)) for a in range(2)]; qd=[[(base.derivative(q,a),base.derivative(qx,a)) for a in range(2)] for q,qx in zip(qs,qxs)]
 for kp in range(2):
  for ls in product(range(1,3),repeat=5):
   if 2 in ls:continue
   for a in range(2):
    for ex in base.monomials_at_most(14):
     r={}
     if ex[a]:d=list(ex);d[a]-=1;put(r,cols[(kp,*ls,tuple(d))],(ex[a],0,0,0))
     for t in set(kd[a][0])|set(kd[a][1]):
      c,cx=kd[a][0].get(t,0),kd[a][1].get(t,0);g=(gamma-kp)%P;put(r,cols[(kp+1,*ls,base.shifted(ex,t))],(g*c%P,c%P,g*cx%P,cx%P))
     for qi,pole in enumerate(ls):
      raised=list(ls);raised[qi]+=1
      for t in set(qd[qi][a][0])|set(qd[qi][a][1]):put(r,cols[(kp,*raised,base.shifted(ex,t))],S((qd[qi][a][0].get(t,0),0,qd[qi][a][1].get(t,0),0),-pole))
     pivot(r,ps)
 for kp in range(2):
  for ls in product(range(1,3),repeat=5):
   for ex in base.monomials_at_most(10):
    r={cols[(kp,*ls,ex)]:(1,0,0,0)}
    for t,v in coeffs(k,kx).items():put(r,cols[(kp+1,*ls,base.shifted(ex,t))],S(v,-1))
    pivot(r,ps)
 for qi,(q,qx) in enumerate(zip(qs,qxs)):
  for kp in range(3):
   for ls in product(range(1,3),repeat=5):
    if ls[qi]==2:continue
    raised=list(ls);raised[qi]+=1
    for ex in base.monomials_at_most(13):
     r={cols[(kp,*ls,ex)]:(1,0,0,0)}
     for t,v in coeffs(q,qx).items():put(r,cols[(kp,*raised,base.shifted(ex,t))],S(v,-1))
     pivot(r,ps)
 free=[i for i in range(len(low)) if i not in ps]; return cols,ps,free
cols,ps,free=presentation(); mons=[(i,j) for i in range(7) for j in range(7-i)]; normals=[red({cols[(0,1,1,1,1,1,e)]:(1,0,0,0)},ps) for e in mons]
# First compute ker(M0), then solve M0 r_X = -M_X r_0.  Kernel ambiguity
# changes r_X by a base relation and hence changes the mixed image only by
# the already retained Bockstein image.
basecols=[{c:n[c][0] for c in free if c in n and n[c][0]} for n in normals]
cp={}; base_rel=[]
for j,src in enumerate(basecols):
 col=dict(src);comb={j:1}
 while col:
  c=max(col);q=col[c]
  if c not in cp:
   iq=pow(q,-1,P);cp[c]=({k:v*iq%P for k,v in col.items()},{k:v*iq%P for k,v in comb.items()});break
  ec,er=cp[c]
  for k,v in ec.items():
   w=(col.get(k,0)-q*v)%P
   if w:col[k]=w
   else:col.pop(k,None)
  for k,v in er.items():
   w=(comb.get(k,0)-q*v)%P
   if w:comb[k]=w
   else:comb.pop(k,None)
 else:base_rel.append(comb)
def solve(rhs):
 col=dict(rhs);sol={}
 for c in sorted(cp,reverse=True):
  if c not in col:continue
  q=col[c]
  ec,er=cp[c]
  for k,v in ec.items():
   w=(col.get(k,0)-q*v)%P
   if w:col[k]=w
   else:col.pop(k,None)
  for k,v in er.items():
   w=(sol.get(k,0)+q*v)%P
   if w:sol[k]=w
   else:sol.pop(k,None)
 return sol,col
rel=[];lift_obstructions=[];obstruction_classes=[]
for r0 in base_rel:
 rhs={}
 for j,a in r0.items():
  for c,v in normals[j].items():
   if c not in free:continue
   w=(rhs.get(c,0)-a*v[2])%P
   if w:rhs[c]=w
   else:rhs.pop(c,None)
 rx,residual=solve(rhs)
 if residual:lift_obstructions.append(r0);obstruction_classes.append(residual);continue
 rr={j:(a,0,rx.get(j,0),0) for j,a in r0.items()}
 for j,a in rx.items():
  if j not in rr:rr[j]=(0,0,a,0)
 rel.append(rr)
beta=[];mixed=[];beta_full=[];mixed_full=[]
for rr in rel:
 n={}
 for j,c in rr.items():
  for k,v in normals[j].items():put(n,k,M(c,v))
 beta_full.append({k:v[1] for k,v in n.items() if v[1]});mixed_full.append({k:v[3] for k,v in n.items() if v[3]})
 beta.append({k:v[1] for k,v in n.items() if k in free and v[1]});mixed.append({k:v[3] for k,v in n.items() if k in free and v[3]})
def rank(vs):
 ps={}
 for r0 in vs:
  r=dict(r0);base.add_pivot(r,ps)
 return len(ps)
rb=rank(beta); rm=rank(beta+mixed); horizontal=rm==rb
checks={"base_relation_dimension_two":len(base_rel)==2,"lift_equation_classified_both_relations":len(rel)+len(lift_obstructions)==2,"both_relations_lift":len(rel)==2,"bockstein_rank_one":rb==1,"mixed_image_adds_one_direction":rm==2}
payload={"schema":"marici.rank26-bidual-quotient-horizontality.v1","prime":P,"direction":"x" if AX==0 else "y","free_dimension":len(free),"lifted_relation_dimension":len(rel),"bockstein_rank":rb,"bockstein_plus_mixed_rank":rm,"bockstein_vectors":[{str(k):v for k,v in sorted(r.items())} for r in beta],"mixed_vectors":[{str(k):v for k,v in sorted(r.items())} for r in mixed],"mixed_support_sizes":[len(v) for v in mixed],"horizontal":horizontal,"checks":checks,"passed":all(checks.values()),"conclusion":"The simultaneous bidual reduction lifts relation representatives before extracting gamma and mixed grades. The mixed image raises the rank-one Bockstein span to rank two, so the boundary line is not horizontal in the source-normalized quotient frame."}
payload["base_relation_dimension"]=len(base_rel);payload["obstructed_relation_dimension"]=len(lift_obstructions);payload["obstruction_classes"]=[{str(k):v for k,v in sorted(r.items())} for r in obstruction_classes];payload["conclusion"]="Both base relations lift after the inhomogeneous equation is solved in the 26-dimensional free quotient. The rank-one Bockstein image acquires one independent mixed direction, so the line is locally nonhorizontal."
payload["base_relation_vectors"]=[{str(k):v for k,v in sorted(r.items())} for r in base_rel]
payload["base_quotient_columns"]=[{str(k):v for k,v in sorted(r.items())} for r in basecols]
payload["bockstein_full_vectors"]=[{str(k):v for k,v in sorted(r.items())} for r in beta_full]
payload["mixed_full_vectors"]=[{str(k):v for k,v in sorted(r.items())} for r in mixed_full]
payload["bockstein_omitted_support_sizes"]=[sum(1 for k,v in r.items() if k not in free and v) for r in beta_full]
payload["mixed_omitted_support_sizes"]=[sum(1 for k,v in r.items() if k not in free and v) for r in mixed_full]
payload["lifted_base_relation_vectors"]=[{str(k):c[0] for k,c in sorted(r.items()) if c[0]} for r in rel]
payload["obstructed_base_relation_vectors"]=[{str(k):v for k,v in sorted(r.items())} for r in lift_obstructions]
OUT.write_text(json.dumps(payload,indent=2)+"\n");print(json.dumps(payload,indent=2));raise SystemExit(0 if payload["passed"] else 1)
