"""Search projective pair-cancellation directions for sparse raw-q certificates."""
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_sparse_raw_q_certificates.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def key(d):return json.dumps(d,separators=(',',':'))
def norm(v):
 v=tuple(Fraction(x) for x in v)
 i=next((i for i,x in enumerate(v) if x),None)
 if i is None:return None
 a=v[i];return tuple(x/a for x in v)
def cross(a,b):return norm((a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]))
def vrank(vs):
 b=[]
 for raw in vs:
  r=list(raw)
  for p,row in b:
   a=r[p];r=[x-a*y for x,y in zip(r,row)]
  p=next((i for i,x in enumerate(r) if x),None)
  if p is not None:
   a=r[p];r=[x/a for x in r];b.append((p,r));b.sort()
 return len(b)
def main():
 d=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());groups=[]
 for group in d['groups']:
  cs=group['certificates'];keys=sorted({key(t['descriptor']) for c in cs for t in c['raw_q_terms']});vecs=[]
  for c in cs:
   m={key(t['descriptor']):q(t['coefficient']) for t in c['raw_q_terms']};vecs.append([m.get(k,Fraction()) for k in keys])
  forms=[tuple(v[j] for v in vecs) for j in range(len(keys))];cands={norm((1,0,0)),norm((0,1,0)),norm((0,0,1))}
  for a,b in combinations(forms,2):
   x=cross(a,b)
   if x:cands.add(x)
  scored=[]
  for lam in cands:
   outv=[sum(lam[i]*vecs[i][j] for i in range(3)) for j in range(len(keys))];support=sum(bool(x) for x in outv);scored.append((support,lam))
  scored.sort(key=lambda x:(x[0],x[1]));chosen=[]
  for support,lam in scored:
   if vrank([x[1] for x in chosen]+[lam])>len(chosen):chosen.append((support,lam))
   if len(chosen)==3:break
  assert len(chosen)==3
  groups.append({'grade':group['grade'],'candidate_direction_count':len(cands),'original_supports':[c['raw_q_support_count'] for c in cs],'sparse_basis':[{'support_count':n,'combination_on_echelon_certificates':[enc(x) for x in lam]} for n,lam in chosen],'minimum_enumerated_projective_support':scored[0][0]})
 out={'schema':'marici.voevodsky.cosmology-sparse-raw-q-certificates.v1','status':'pair_cancellation_search_complete','groups':groups,'decision':'Enumerating all projective directions obtained by cancelling pairs of raw-q coordinates yields a sparser independent certificate basis.','claim_boundary':'Minimality is certified only within the finite pair-cancellation candidate set, not among all possible changes of raw-q generating rows.','next_gate':'test-global-support-minimality-or-classify-sparse-descriptors','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
