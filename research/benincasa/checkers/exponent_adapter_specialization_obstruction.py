"""Verify the first-normal lifting obstruction at the adapter quarter points."""

import json
from pathlib import Path

root=Path(__file__).resolve().parents[3];res=root/'research/benincasa/results'
labels=[(i,j) for i in range(8) for j in range(8-i)]
def add(r,c,v,p):
 v=(r.get(c,0)+v)%p
 if v:r[c]=v
 else:r.pop(c,None)
def scale(r,s,p):return {c:v*s%p for c,v in r.items() if v*s%p}
def axpy(r,q,s,p):
 for c,v in s.items():add(r,c,-q*v,p)
def load(packet,num,den,count):
 p=packet['p'];g=num*pow(den,p-2,p)%p; a=[{} for _ in range(count)];b=[{} for _ in range(count)]
 for i,j,x in packet['a']:
  if i<count:add(a[i],j,x,p)
 for i,j,x in packet['b']:
  if i<count:add(a[i],j,g*x,p);add(b[i],j,x,p)
 return a,b
def dual_basis(a,b,p):
 piv={}
 for aa,bb in zip(a,b):
  aa=dict(aa);bb=dict(bb)
  while aa:
   j=max(aa);q0=aa[j];q1=bb.get(j,0)
   if j not in piv:
    for k in sorted(piv,reverse=True):
     q=bb.get(k,0)
     if q:axpy(bb,q,piv[k][0],p)
    q1=bb.get(j,0)
    z=pow(q0,p-2,p); z1=-q1*z*z%p
    olda,oldb=aa,bb;aa=scale(olda,z,p);bb=scale(oldb,z,p)
    for c,v in olda.items():add(bb,c,z1*v,p)
    piv[j]=(aa,bb);break
   pa,pb=piv[j];axpy(aa,q0,pa,p);axpy(bb,q0,pb,p);axpy(bb,q1,pa,p)
 return piv
def reduce_dual(a,b,piv,p):
 a=dict(a);b=dict(b)
 for j in sorted(piv,reverse=True):
  q0=a.get(j,0);q1=b.get(j,0)
  if q0 or q1:
   pa,pb=piv[j];axpy(a,q0,pa,p);axpy(b,q0,pb,p);axpy(b,q1,pa,p)
 for j in sorted(piv,reverse=True):
  q=b.get(j,0)
  if q:axpy(b,q,piv[j][0],p)
 return a,b
def row_basis(rows,p):
 piv={}
 for src in rows:
  r=dict(src)
  while r:
   j=max(r);q=r[j]
   if j not in piv:
    piv[j]=scale(r,pow(q,p-2,p),p);break
   axpy(r,q,piv[j],p)
 return piv
def reduce(r,piv,p):
 r=dict(r)
 for j in sorted(piv,reverse=True):
  q=r.get(j,0)
  if q:axpy(r,q,piv[j],p)
 return r
def kernel(rows,width,p):
 piv=row_basis(rows,p);free=[i for i in range(width) if i not in piv];out=[]
 for f in free:
  v={f:1}
  for j in sorted(piv):
   s=sum(x*v.get(c,0) for c,x in piv[j].items() if c!=j)%p
   if s:v[j]=-s%p
  out.append(v)
 return out
def combine(coeff,rows,p):
 out={}
 for i,x in coeff.items():
  for c,v in rows[i].items():add(out,c,x*v,p)
 return out
def analyze(p,pt,packet=None):
 if packet is None:packet=json.loads((res/f'exponent_adapter_full_pencil_{p}.json').read_text())
 a,b=load(packet,*pt,756)
 mb=dual_basis(a[:720],b[:720],p)
 source_rem=[reduce_dual(a[i],b[i],mb,p) for i in range(720)]
 source_normal_rank=len(row_basis([x[1] for x in source_rem if not x[0]],p))
 rem=[reduce_dual(a[i],b[i],mb,p) for i in range(720,756)]
 r0=[x[0] for x in rem];r1=[x[1] for x in rem];rb=row_basis(r0,p)
 coords=sorted(set().union(*(set(r) for r in r0)));eq=[{i:r[c] for i,r in enumerate(r0) if c in r} for c in coords]
 k=kernel(eq,36,p);obs=[reduce(combine(v,r1,p),rb,p) for v in k]
 total=len(row_basis(obs,p)); filt=[]
 for d in range(8):
  ids=[i for i,l in enumerate(labels) if sum(l)<=d]
  # relations supported in ids: recompute kernel of restricted r0 rows, then embed
  cs=sorted(set().union(*(set(r0[i]) for i in ids))) if ids else []
  ee=[{j:r0[i][c] for j,i in enumerate(ids) if c in r0[i]} for c in cs]
  kk=kernel(ee,len(ids),p);oo=[]
  for v in kk:oo.append(reduce(combine({ids[j]:x for j,x in v.items()},r1,p),rb,p))
  filt.append(len(row_basis(oo,p)))
 return len(mb),source_normal_rank,len(rb),len(k),total,filt
def main():
 output={"status":"pass","convention":"dual-number source quotient followed by the first-normal relation-lifting obstruction","analyses":[]}
 expected={(-5,4):(479,0,21,15,5,[0,0,0,0,0,2,5,5]),(-7,4):(479,0,19,17,7,[0,0,0,0,0,2,6,7])}
 for p in (32003,32009):
  for pt in ((-5,4),(-7,4)):
   result=analyze(p,pt)
   assert result==expected[pt],(p,pt,result)
   output["analyses"].append({"prime":p,"point":list(pt),"source_rank":result[0],"source_first_normal_residual_rank":result[1],"special_relative_rank":result[2],"relation_dimension":result[3],"obstruction_rank":result[4],"obstruction_rank_by_degree_0_through_7":result[5]})
 (res/'exponent_adapter_specialization_obstruction.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(output,indent=2))

if __name__=='__main__':main()
