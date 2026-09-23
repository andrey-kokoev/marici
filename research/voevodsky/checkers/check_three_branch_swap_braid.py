"""Three independent square proof events satisfy endpoint braid, not path identity."""
from hashlib import sha256
from pathlib import Path
import json
deps={'Z':(), 'W':('Z',),'V':('Z',),'U':('Z',),'T':('W','V','U')}
manifest='square-row-derivation-manifest-v1'
def hashtrace(t):return sha256(repr(t).encode()).hexdigest()[:16]
def valid(t):
 seen=set()
 for x in t:
  if x in seen or not set(deps[x])<=seen:return False
  seen.add(x)
 return seen==set(deps)
def swap(t,i):
 assert valid(t)
 a,b=t[i:i+2]
 if a in deps[b] or b in deps[a]:raise ValueError('DEPENDENT_SWAP')
 nxt=t[:i]+(b,a)+t[i+2:]
 assert valid(nxt)
 return nxt,{'events':(a,b),'source':hashtrace(t),'target':hashtrace(nxt),'predecessors':(deps[a],deps[b]),'manifest':manifest}
initial=('Z','W','V','U','T')
def run(indices):
 t=initial;edges=[]
 for i in indices:
  t,e=swap(t,i);edges.append(e)
 return t,edges
left,l=run((1,2,1));right,r=run((2,1,2))
assert left==right==('Z','U','V','W','T') and l!=r
assert [x['events'] for x in l]==[('W','V'),('W','U'),('V','U')]
assert [x['events'] for x in r]==[('V','U'),('W','U'),('W','V')]
assert l[0]['source']==r[0]['source'] and l[-1]['target']==r[-1]['target']
try:swap(initial,0)
except ValueError as err:assert str(err)=='DEPENDENT_SWAP'
else:raise AssertionError('Z/W swapped')
report={'passed':True,'three_branch_braid_endpoint_equal':True,'different_swap_certificate_sequences':True,'pairwise_shared_predecessor':'Z','braid_square_status':'candidate higher coherence only; no equality of swap-proof histories inferred','dependent_swap_refused':True,'scope':'Synthetic source-rooted event DAG and frozen manifest, not actual event observation, publisher authority or analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/three-branch-swap-braid.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
