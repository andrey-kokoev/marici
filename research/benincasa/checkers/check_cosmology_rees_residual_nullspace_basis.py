#!/usr/bin/env python3
"""Extract the corrected symbol-kernel quotient at weighted degree 26."""
import contextlib,io,json,runpy,sys
from pathlib import Path
P=101;ROOT=Path(__file__).resolve().parents[1]
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(ROOT/'checkers/check_cosmology_rees_logarithmic_Hilbert_rank.py'))
add,mul,pw,H,Q,comp,ins=g['add'],g['mul'],g['pw'],g['H'],g['Q'],g['comp'],g['ins'];D=int(sys.argv[1]) if len(sys.argv)>1 else 26;n0=D-12;n1=D-8
def der(a,z):return {((i-1,j) if z==0 else (i,j-1)):v*(i if z==0 else j)%P for (i,j),v in a.items() if (i if z==0 else j)}
def scale(a,c):return {k:v*c%P for k,v in a.items() if v*c%P}
def Bop(f,z):return add(mul(Q,der(f,z)),scale(mul(der(Q,z),f),-1))
def Lop(f,z,kp):
 if kp==0:return add(mul(pw(H,4),Bop(f,z)),scale(mul(mul(pw(H,3),Q),mul(der(H,z),f)),-1))
 return add(mul(pw(H,2),Bop(f,z)),scale(mul(mul(H,Q),mul(der(H,z),f)),-3))
labels=[];cols=[]
for kp,n in [(0,n0),(1,n1)]:
 for z in (0,1):
  for i in range(n+1):labels.append((kp,z,i,n-i));cols.append(Lop({(i,n-i):1},z,kp))
# RREF output-by-domain matrix and nullspace.
rows=[[c.get((i,D-i),0) for c in cols] for i in range(D+1)];pr=0;pivs=[]
for j in range(len(cols)):
 q=next((i for i in range(pr,len(rows)) if rows[i][j]),None)
 if q is None:continue
 rows[pr],rows[q]=rows[q],rows[pr];iv=pow(rows[pr][j],-1,P);rows[pr]=[x*iv%P for x in rows[pr]]
 for i in range(len(rows)):
  if i!=pr and rows[i][j]:
   v=rows[i][j];rows[i]=[(a-v*b)%P for a,b in zip(rows[i],rows[pr])]
 pivs.append(j);pr+=1
free=[j for j in range(len(cols)) if j not in pivs];null=[]
for f in free:
 v={f:1}
 for i,p in enumerate(pivs):
  if rows[i][f]:v[p]=(-rows[i][f])%P
 null.append(v)
# Known exact leading families in domain coordinates.
index={x:i for i,x in enumerate(labels)};known=[];d=D-14;pdeg=D-18
def vec(parts):
 r={}
 for kp,z,p,c in parts:
  for (i,j),v in p.items():r[index[(kp,z,i,j)]]=(r.get(index[(kp,z,i,j)],0)+c*v)%P
 return {k:v for k,v in r.items() if v}
for z in (0,1):
 for i in range(d+1):
  f={(i,d-i):1};known.append(vec([(0,z,mul(H,f),1),(1,z,mul(pw(H,3),f),-1)]))
for kp,hpow in [(0,1),(1,3)]:
 for i in range(pdeg+1):
  psi={(i,pdeg-i):1};known.append(vec([(kp,0,mul(pw(H,hpow),mul(Q,der(psi,1))),1),(kp,1,mul(pw(H,hpow),mul(Q,der(psi,0))),-1)]))
EB={};knownrank=sum(ins(EB,dict(v)) for v in known);residual=[]
for v in null:
 if ins(EB,dict(v)):residual.append(v)
out={'schema':'marici.benincasa.cosmology-rees-residual-nullspace-basis.v1','prime':P,'weighted_degree':D,'domain_dimension':len(cols),'symbol_rank':len(pivs),'nullity':len(null),'known_generator_rank':knownrank,'residual_quotient_dimension':len(residual),'residual_basis':[{'support_size':len(v),'leading_input':repr(labels[min(v)])} for v in residual]};(ROOT/f'results/cosmology_rees_residual_nullspace_basis_D{D}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
