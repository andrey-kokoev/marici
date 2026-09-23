"""Dependency-sensitive retention across hypothetical primitive-row edit."""
from pathlib import Path
import json
leaf_support={'a':{'x-low','x-high'},'b':{'y-low','y-high'},'c':{'x-high'},'d':{'y-high'}}
changed={'x-high'};affected={k for k,v in leaf_support.items() if v&changed}
assert affected=={'a','c'}
# Explicit proof DAG dependencies, separate from syntactic rotation tags.
D={'ab-proof':{'a','b'},'cd-proof':{'c','d'},'composite-proof':{'ab-proof','cd-proof'},
   'short-rotation-syntax':set(),'thin-bracket-reachability':{'short-rotation-syntax'},
   'source-bound-thin-evidence':{'composite-proof','thin-bracket-reachability'}}
def invalid(node,seen=()):
 if node in seen:raise ValueError('CYCLIC_SUPPORT')
 if node in leaf_support:return node in affected
 return any(invalid(x,seen+(node,)) for x in D[node])
statuses={k:('stale' if invalid(k) else 'retain') for k in (*leaf_support,*D)}
assert statuses['a']==statuses['c']=='stale' and statuses['b']==statuses['d']=='retain'
assert statuses['composite-proof']=='stale' and statuses['source-bound-thin-evidence']=='stale'
assert statuses['short-rotation-syntax']==statuses['thin-bracket-reachability']=='retain'
# Generation must bind source-rooted evidence. Pure bracket reachability has
# a different type and cannot be upgraded to proof evidence.
old_generation='manifest:[0,1]^2';new_generation='manifest:[0,2]x[0,1]'
def consume(node,generation,kind):
 if kind=='source-bound-evidence' and generation!=new_generation:raise PermissionError('STALE_SOURCE_GENERATION')
 if kind=='source-bound-evidence' and statuses[node]=='stale':raise PermissionError('REVERIFY_PROOF_DEPENDENCIES')
 if kind=='bracket-reachability' and node=='thin-bracket-reachability':return 'syntactic_only'
 return 'verified_mathematics_only'
for generation in (old_generation,new_generation):
 try:consume('source-bound-thin-evidence',generation,'source-bound-evidence')
 except PermissionError:pass
 else:raise AssertionError('stale source-bound evidence admitted')
assert consume('thin-bracket-reachability',old_generation,'bracket-reachability')=='syntactic_only'
report={'passed':True,'changed_row':'x-high','statuses':statuses,'old_generation_source_evidence_refused':True,'new_generation_unreverified_composite_refused':True,'syntactic_thin_arrow_retained_with_reduced_type':True,'scope':'Hypothetical source edit and declared DAG; root dependency assertions are locally checked, not externally authenticated, and no real revocation or analytic role map occurs.'}
out=Path(__file__).resolve().parents[1]/'results/source-edit-dependency-cache.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
