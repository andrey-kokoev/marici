"""Check naturality and involutivity of center transfer, then resolve its five marking transports against the literal row action."""
from pathlib import Path
import json
from ramsey_center_transfer_seed_binding import A,row,R,C,example,graph,hub
from ramsey_regular_two_switch import relation,iso
D=Path(__file__).parent
compose=lambda a,b:tuple(a[b[i]] for i in range(22))
def relabel(B,p):
 out=[0]*22
 for i in range(22):
  for j in range(22):
   if B[i]>>j&1:out[p[i]]|=1<<p[j]
 return out

def transfer(B):
 f=iso(B,C,relation(B),relation(C));assert f is not None;back={v:k for k,v in f.items()};out=B[:]
 for s in example['switches']:
  for i,j in s['removed']+s['added']:
   a,b=back[i],back[j];out[a]^=1<<b;out[b]^=1<<a
 return out,f
B,f=transfer(A);rowB,_=transfer(row);backB,_=transfer(B);assert backB==A and rowB==relabel(B,R);assert relabel(row,R)==A
# Five isomorphisms A -> B: choose one then compose with all root automorphisms.
K=iso(A,B,relation(A),relation(B));assert K is not None;K=tuple(K[i] for i in range(22));pC=json.loads((D/'ramsey_repair_cyclic_phase.json').read_text())[1]['unique_C5_generator'];back={v:k for k,v in f.items()};p=tuple(back[pC[f[i]]] for i in range(22));identity=tuple(range(22));g=identity;rows=[]
for phase in range(5):
 k=compose(K,g);assert relabel(A,k)==B;rows.append({'phase':phase,'permutation':k,'involutive':compose(k,k)==identity,'commutes_with_row':compose(k,R)==compose(R,k)});g=compose(p,g)
assert all(r['involutive'] for r in rows)
result={'transfer_squared_identity':True,'transfer_row_square_commutes':True,'mark_transports':rows,'commuting_transport_count':sum(r['commutes_with_row'] for r in rows)};(D/'ramsey_row_center_calculus.json').write_text(json.dumps(result,indent=2)+'\n');print('transport summary',[(r['phase'],r['involutive'],r['commutes_with_row']) for r in rows])
