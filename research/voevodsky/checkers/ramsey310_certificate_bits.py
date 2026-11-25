"""Exact all-pair labels, local residual training / parent-12 family holdout.
uv run --with numpy --with igraph python ... . Costs start at the eligible-library interface.
"""
from ramsey310_smallset_holdout import D,F,json,eligible,decode,additions
from itertools import combinations,islice
from math import log2,exp
from time import perf_counter_ns
from statistics import mean,median
P=list(combinations(range(26),2));base=json.loads((D/'ramsey310_matching_degree3_types.json').read_text())[0]
def changed(A,path):
 a=A.copy()
 for i,j,x,y in path:a[i]^=1<<j;a[j]^=1<<i;a[x]|=1<<y;a[y]|=1<<x
 return a
fresh=changed(base,[(18,9,25,17),(15,13,7,4)])
def data():
 for i,r in enumerate(json.loads((D/'ramsey310_s3_local_transfer_r10.json').read_text())['uncut']):
  A=changed(base,r['path']);rows=json.loads((D/f'ramsey310_s3_all_ports_{i}_replay.json').read_text());yield from ((f'local{i}.{j}','local',*eligible(A,s['E'])) for j,s in enumerate(rows))
 for glob in ['batch','shell2','parent12']:
  for f in sorted(D.glob(f'ramsey310_smallset_{glob}_*.json')):
   r=json.loads(f.read_text());
   if not r['survivors']:continue
   e=r['edit'];A=changed(fresh,[e] if glob=='batch' else e) if glob!='parent12' else next(islice(additions(decode((D/'ramsey38_26_e73_hog.g6').read_bytes().splitlines()[11])),e[1],None));
   for j,s in enumerate(r['survivors']):yield f'{glob}.{r["index"]}.{j}',('test' if glob=='parent12' else 'local'),*eligible(A,s['E'])

def prepare(C):return [sum(1<<j for j,s in enumerate(C) if s>>v&1) for v in range(26)]
def cert(d,M,n,i,j):
 x=(M[i]&M[j]).bit_count();z=n-(M[i]|M[j]).bit_count();return not max(0,6-z)+max(0,6-(n-x))<=d[i]+d[j]<=min(6,x)+min(6,n-z)
def scores(d,M,n):
 # Deviation from demand predicted by sampling six rows uniformly, ignoring correlation.
 v=[6*x.bit_count()/n-y for x,y in zip(M,d)];return [abs(v[i]+v[j]) for i,j in P]
def prob(sc,t):
 m=max(sc);w=[exp(t*(x-m)) for x in sc];z=sum(w);return [.1/325+.9*x/z for x in w]
def bits(sc,good,t):return -log2(sum(probability for probability,g in zip(prob(sc,t),good) if g))
def main():
 rows=[]
 for id,split,d,C in data():
  M=prepare(C);n=len(C);g=[cert(d,M,n,*p) for p in P];sc=scores(d,M,n);rows.append((id,split,d,C,g,sc))
 train=[r for r in rows if r[1]=='local' and any(r[4])];t=min([0,.25,.5,1,2,4],key=lambda t:sum(bits(r[5],r[4],t) for r in train));out=[]
 for id,split,d,C,g,sc in rows:
  ix=sorted(range(325),key=lambda i:-sc[i]);k=sum(g);n=len(C);tim=[]
  for ranked in [False,True]:
   tt=[]
   for _ in range(21):
    start=perf_counter_ns();M=prepare(C);order=range(325)
    if ranked:ss=scores(d,M,n);order=sorted(order,key=lambda i:-ss[i])
    for j in order:
     if cert(d,M,n,*P[j]):break
    tt.append((perf_counter_ns()-start)/1000)
   tim.append(median(tt))
  out.append(dict(id=id,split=split,pairs=[p for p,y in zip(P,g) if y],uniform_bits=log2(325/k) if k else None,model_bits=bits(sc,g,t) if k else None,uniform_expected=326/(k+1) if k else 325,ranked_checks=next((j for j,i in enumerate(ix,1) if g[i]),325),lex_checks=next((j for j,y in enumerate(g,1) if y),325),lex_ranked_us=tim))
 for spl in ['local','test']:
  z=[a for a in out if a['split']==spl];good=[a for a in z if a['pairs']];print(spl,len(z),len(good),'t',t,'bits',*[mean(a[k] for a in good) for k in ['uniform_bits','model_bits']],'checks',*[mean(a[k] for a in z) for k in ['uniform_expected','lex_checks','ranked_checks']],'us',*[mean(a['lex_ranked_us'][k] for a in z) for k in [0,1]])
  if spl=='test':print([(a['id'],a['pairs'],a['ranked_checks']) for a in z])
 (D/'ramsey310_certificate_bits.json').write_text(json.dumps(dict(temperature_multiplier=t,cases=out)))
if __name__=='__main__':main()
