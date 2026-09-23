"""Adjacent independent proof events admit a typed local swap, not identity."""
from hashlib import sha256
from pathlib import Path
import json
manifest='square-primitive-rows-v1'
deps={'ev-Z':(), 'ev-W':('ev-Z',),'ev-V':('ev-Z',),'ev-T':('ev-W','ev-V')}
first=('ev-Z','ev-W','ev-V','ev-T')
def valid(trace):
 seen=set()
 for e in trace:
  if e in seen or e not in deps or not set(deps[e])<=seen:return False
  seen.add(e)
 return seen==set(deps)
def ancestors(e):
 result=set(deps[e])
 for d in deps[e]:result|=ancestors(d)
 return result
def digest(parts):return sha256(repr(parts).encode()).hexdigest()
def certify(trace,index,source_manifest):
 if source_manifest!=manifest:raise ValueError('STALE_MANIFEST')
 if not valid(trace) or index<0 or index>=len(trace)-1:raise ValueError('INVALID_TRACE')
 a,b=trace[index:index+2]
 if a in ancestors(b) or b in ancestors(a):raise ValueError('DEPENDENT_SWAP')
 out=trace[:index]+(b,a)+trace[index+2:]
 if not valid(out):raise ValueError('INVALID_SWAPPED_TRACE')
 return out,{'left_event':a,'right_event':b,'prefix_digest':digest(trace[:index]),'predecessors':{a:deps[a],b:deps[b]},'manifest':manifest,'source_trace_digest':digest(trace),'target_trace_digest':digest(out)}
assert valid(first)
second,cert=certify(first,1,manifest)
assert second==('ev-Z','ev-V','ev-W','ev-T') and cert['predecessors']=={'ev-W':('ev-Z',),'ev-V':('ev-Z',)}
back,_=certify(second,1,manifest);assert back==first
for trace,index,m,error in ((first,0,manifest,'DEPENDENT_SWAP'),(first,2,manifest,'DEPENDENT_SWAP'),(first,1,'old-manifest','STALE_MANIFEST'),(('ev-W','ev-Z','ev-V','ev-T'),1,manifest,'INVALID_TRACE')):
 try:certify(trace,index,m)
 except ValueError as err:assert str(err)==error
 else:raise AssertionError('bad swap accepted')
report={'passed':True,'allowed_swap':'ev-W <-> ev-V after ev-Z','retained_certificate_fields':sorted(cert),'dependent_swaps_refused':2,'stale_manifest_and_invalid_trace_refused':True,'same_DAG_not_identical_histories':True,'scope':'Synthetic square proof event IDs, local adjacent independence under frozen DAG. Swap certificate defines proposed trace equivalence, not observed execution, owner attestation or analytic role mapping.'}
out=Path(__file__).resolve().parents[1]/'results/square-trace-swap.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
