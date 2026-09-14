#!/usr/bin/env python3
"""VC2b2 fast test: does the odd target lie in image(d0)+overlap columns?"""
import gzip,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
pres=json.loads((ROOT/'research/benincasa/results/G12_char0_H1_presentation.json').read_text());ov=json.loads((ROOT/'research/benincasa/results/G12_coefficient_overlap_representatives.json').read_text());data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text())
lines=gzip.decompress((ROOT/pres['matrix_artifact']).read_bytes()).decode().splitlines();nr,nc,nnz=map(int,lines[1].split());rawcols=[{} for _ in range(nc)]
for line in lines[2:]:
 r,c0,x=line.split();num,den=x.split('/');rawcols[int(c0)-1][int(r)-1]=(int(num),int(den))
a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c};qs=[b+c+1,a+c+1,b+c+2,a+c+2];N23=s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L);N31=s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L);target=s.expand(N23*qs[3]**3-N31*qs[2]**3);rows=[(i,j,d-i-j) for d in range(19) for i in range(d+1) for j in range(d-i+1)];ridx={e:i for i,e in enumerate(rows)}
def polyvec(poly,p):return {ridx[e]:(int(x.p)%p)*pow(int(x.q),-1,p)%p for e,x in s.Poly(poly,a,b,c,domain=s.QQ).terms() if x}
def add(v,basis,p,insert):
 while v:
  z=max(v)
  if z not in basis:
   if not insert:return False,v
   inv=pow(v[z],-1,p);basis[z]={e:x*inv%p for e,x in v.items()};return True,{}
  t=v[z]
  for e,x in basis[z].items():
   y=(v.get(e,0)-t*x)%p
   if y:v[e]=y
   else:v.pop(e,None)
 return True,{}
results=[]
for p in (32003,32009):
 t=time.perf_counter();basis={}
 for col in rawcols:add({r:num%p*pow(den,-1,p)%p for r,(num,den) in col.items()},basis,p,True)
 rank0=len(basis);overlap_classes=[]
 for col in ov['columns']:
  poly=s.sympify(col['formula'],locals=L);v=polyvec(poly,p);_,res=add(dict(v),basis,p,False);nonzero=bool(res);add(v,basis,p,True);overlap_classes.append(nonzero)
 rank1=len(basis);inside,res=add(polyvec(target,p),basis,p,False)
 results.append({'prime':p,'rank_d0':rank0,'nonzero_overlap_classes':sum(overlap_classes),'rank_after_overlaps':rank1,'overlap_rank_in_H1':rank1-rank0,'target_in_augmented_image':inside,'target_residual_support':len(res),'elapsed_seconds':round(time.perf_counter()-t,3)})
resolution='++' if all(x['target_in_augmented_image'] for x in results) else '-+'
checks={'matrix_shape':(nr,nc,nnz)==(1330,1144,245286),'six_overlaps':len(ov['columns'])==6,'two_prime_profile_stable':len({(x['rank_d0'],x['overlap_rank_in_H1'],x['target_in_augmented_image'],x['target_residual_support']) for x in results})==1,'fast':all(x['elapsed_seconds']<30 for x in results)};assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-overlap-span-in-H1.v1','prospective_action':'VC2b2_compare_overlap_to_H1','test':'target membership in image(d0)+span(six logarithmic overlap columns)','results':results,'resolution':resolution,'conclusion':'overlap comparison lowers the target residual' if resolution=='++' else 'the canonical logarithmic overlap classes do not span the odd target in H1','next':'reconstruct exact comparison and audit K0/boundary coherence' if resolution=='++' else 'resolve VC2b2=-+ and replan; enlarging overlap coefficients requires a new priced action','checks':checks,'passed':True};d=ROOT/'research/benincasa/results/G12_overlap_span_in_H1.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':resolution,'results':results,'next':out['next']}))
