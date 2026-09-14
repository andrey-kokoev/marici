#!/usr/bin/env python3
"""VC2e: find the minimum polynomial weight degree making overlaps hit the odd target."""
import gzip,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
pres=json.loads((ROOT/'research/benincasa/results/G12_char0_H1_presentation.json').read_text());ov=json.loads((ROOT/'research/benincasa/results/G12_coefficient_overlap_representatives.json').read_text());data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text())
lines=gzip.decompress((ROOT/pres['matrix_artifact']).read_bytes()).decode().splitlines();nr,nc,_=map(int,lines[1].split());raw=[{} for _ in range(nc)]
for line in lines[2:]:r,j,x=line.split();p,q=x.split('/');raw[int(j)-1][int(r)-1]=(int(p),int(q))
a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c};rows=[(i,j,d-i-j) for d in range(19) for i in range(d+1) for j in range(d-i+1)];ridx={e:i for i,e in enumerate(rows)}
base=[]
for col in ov['columns']:base.append({e:x for e,x in s.Poly(s.sympify(col['formula'],locals=L),a,b,c,domain=s.QQ).terms()})
qs=[b+c+1,a+c+1,b+c+2,a+c+2];N23=s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L);N31=s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L);target=s.Poly(s.expand(N23*qs[3]**3-N31*qs[2]**3),a,b,c,domain=s.QQ)
def add(v,B,p,insert):
 while v:
  z=max(v)
  if z not in B:
   if not insert:return False,v
   inv=pow(v[z],-1,p);B[z]={e:x*inv%p for e,x in v.items()};return True,{}
  t=v[z]
  for e,x in B[z].items():
   y=(v.get(e,0)-t*x)%p
   if y:v[e]=y
   else:v.pop(e,None)
 return True,{}
def qcoef(x,p):return int(x.p)%p*pow(int(x.q),-1,p)%p
results=[]
for prime in (32003,32009):
 start=time.perf_counter();B={}
 for col in raw:add({r:num%prime*pow(den,-1,prime)%prime for r,(num,den) in col.items()},B,prime,True)
 rank0=len(B);tv={ridx[e]:qcoef(x,prime) for e,x in target.terms()};minimum=None;profile=[]
 for degree in range(16):
  before=len(B)
  mons=[(i,j,degree-i-j) for i in range(degree+1) for j in range(degree-i+1)]
  for coeff in base:
   for m in mons:
    v={ridx[tuple(e[k]+m[k] for k in range(3))]:qcoef(x,prime) for e,x in coeff.items() if sum(e)+degree<=18}
    add(v,B,prime,True)
  inside,res=add(dict(tv),B,prime,False);profile.append({'weight_degree':degree,'new_rank':len(B)-before,'total_rank':len(B),'target_in_span':inside})
  if inside:minimum=degree;break
 results.append({'prime':prime,'rank_d0':rank0,'minimum_weight_degree':minimum,'final_rank':len(B),'elapsed_seconds':round(time.perf_counter()-start,3),'profile':profile})
resolution='++' if all(x['minimum_weight_degree'] is not None for x in results) and len({x['minimum_weight_degree'] for x in results})==1 else '-+'
checks={'two_primes':len(results)==2,'stable_minimum':resolution=='++','bounded_runtime':all(x['elapsed_seconds']<120 for x in results)};assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-polynomial-weighted-overlap-span.v1','prospective_action':'VC2e_polynomial_weighted_overlap_span','weight_ring':'Q[a,b,c] with degree filtration','test':'target in image(d0)+sum_edges Q[a,b,c]_{<=d}*[edge cofactor]','results':results,'resolution':resolution,'minimum_weight_degree':results[0]['minimum_weight_degree'],'conclusion':'The weighted overlap module reaches the odd target in both modular fibers at the same minimal degree.','qualification':'Modular span membership does not yet give an exact Q comparison or prove relative-boundary descent.','next':'reconstruct one sparse rational weighted-overlap comparison at the minimal degree, then verify exchange/path coherence.','checks':checks,'passed':True};(ROOT/'research/benincasa/results/G12_polynomial_weighted_overlap_span.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':resolution,'minimum_degree':out['minimum_weight_degree'],'runtimes':[x['elapsed_seconds'] for x in results],'next':out['next']}))
