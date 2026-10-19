# /// script
# dependencies = ["sympy"]
# ///
"""Bind the actual common-endpoint assembly to retained carrier-index rows.

The adapter is a two-column table map with retained original rows. It is NOT
an endpoint-faithful directed-graph functor or a selected physical T9.
"""
from contextlib import redirect_stdout
from dataclasses import replace
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/assembly-vs-carrier-endpoint-roles.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    bound=runpy.run_path(str(HERE/'check_geometric_record_endpoint_binding.py'))
    typed=runpy.run_path(str(HERE/'check_typed_assembly_boundary_adapter.py'))
m=bound['m']; dg=m['m']; original=m['source']
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('existing-geometric-record-binding-fresh',bound['result']['verification_status']=='pass')
check('actual-DG-reference-endpoints',dg['arrows']['d'][:2]==('A','B'))
# Inspect ACTUAL leg signatures in the shared-leg DG model, not invented types.
all_slots=[]
for tag,size,mid in (('a',11,'U'),('s',4,'V')):
    for i,j in product(range(size),repeat=2):
        left,right=dg['arrows'][f'{tag}x{i}'],dg['arrows'][f'{tag}y{j}']
        check('actual-shared-leg-endpoints/'+str((tag,i,j)),left[:2]==('A',mid) and right[:2]==(mid,'B'))
        value=dg['mul'](dg['values'][f'{tag}y{j}'],dg['values'][f'{tag}x{i}'])
        row=original[len(all_slots)]
        check('actual-shared-leg-row-value/'+str((tag,i,j)),value==row.value)
        all_slots.append((tag,i,j))
check('both-existing-assembly-domain-enumerations-match',len(all_slots)==len(typed['slots'])==137)

A=('assembly-object','A'); B=('assembly-object','B')
# Keep an explicit original-row packet in EACH endpoint-role wrapper.
assembly=tuple(replace(row,source=A,target=B,members=(row,)) for row in original)
check('source-role-map-retains-original-rows',m['leaves'](assembly)==original)
check('source-role-map-retains-values-and-masses',all(a.value==b.value and a.mass==b.mass for a,b in zip(assembly,original)))
check('assembly-labels-remain-distinct',len({row.label for row in assembly})==137)
check('assembly-endpoint-uniqueness-is-not-valid',len({(row.source,row.target) for row in assembly})==1)
check('same-original-J4-before-promotion',m['read_at_four'](m['indexed'](assembly,'target'))==m['read_at_four'](m['indexed'](original,'target')))

profiles={}
for input_name,rows in (('carrier-index',original),('common-assembly',assembly)):
    profiles[input_name]={}
    for policy in ('inherited','common'):
        first=m['incoming_promotion'](rows,1,policy)
        final=m['incoming_promotion'](first,2,policy)
        check('original-leaf-recovery/'+input_name+'/'+policy,m['leaves'](final)==original)
        check('unchanged-J4/'+input_name+'/'+policy,m['read_at_four'](m['indexed'](final,'target'))==m['read_at_four'](m['indexed'](original,'target')))
        profiles[input_name][policy]=[len(rows),len(first),len(final)]
check('assembly-promotes137_to1_to1_under_both_policies',profiles['common-assembly']=={'inherited':[137,1,1],'common':[137,1,1]})
check('carrier-signatures-remain-original',profiles['carrier-index']=={'inherited':[137,32,32],'common':[137,32,1]})

# Explicit operation-domain comparison. Equality of numeric Hom(A,B) values
# does not imply an operation-reflecting binding of carrier keys.
def return_support(rows):
    return {(a.label,b.label) for a,b in product(rows,repeat=2) if a.target==b.target}
def forward_support(rows):
    return {(a.label,b.label) for a,b in product(rows,repeat=2) if a.target==b.source}
old=return_support(original); new=return_support(assembly)
old_forward=forward_support(original); new_forward=forward_support(assembly)
check('reference-return-domain-is-preserved-but-not-reflected',old<new and len(old)==977 and len(new)==18769)
check('literal-forward-domain-is-not-preserved',len(old_forward)==916 and not new_forward)
a,b=next((a,b) for a,b in product(original,repeat=2) if a.target!=b.target)
check('real-cross-fibre-reflection-witness',(a.label,b.label) in new-old)

# Original carrier ports occur in both columns. A single graph-object map
# cannot send each such port to A as a source and B as a target when A!=B.
source_ports={row.source for row in original}; target_ports={row.target for row in original}
shared_port=min(source_ports&target_ports,key=repr)
check('single-carrier-object-map-contradiction',source_ports==target_ports and len(source_ports)==32 and A!=B)
# Separate-column table maps are allowed, but collapse endpoint uniqueness.
# An optional source-label refinement repairs uniqueness by CHANGING the
# endpoint contract rather than establishing the original common A->B type.
refined=tuple(replace(row,source=('labelled-assembly-source',row.label)) for row in assembly)
check('labelled-source-refinement-restores-uniqueness',len({(row.source,row.target) for row in refined})==137)
check('labelled-source-refinement-still-admits-all-return-pairs',return_support(refined)==new)
check('labelled-source-refinement-is-not-literal-common-A',any(row.source!=A for row in refined))

result={
 'schema':'marici.nima.assembly-vs-carrier-endpoint-roles.v1','verification_status':'pass','checks':checks,
 'actual_source_endpoints':'All137 shared-leg composites A->B; direct reference d:A->B; intermediate objects U and V remain distinct.',
 'adapter':'Retained role wrapper: label/value/mass unchanged; source=A,target=B; original carrier-index row retained as member.',
 'tower_profiles':profiles,
 'operation_domains':{'carrier_reference_return':977,'assembly_reference_return':18769,
                      'added_reference_return_pairs':17792,'carrier_literal_forward':916,'assembly_literal_forward':0},
 'reflection_witness':{'labels':[a.label,b.label],'original_targets':[a.target,b.target]},
 'graph_map_obstruction_port':shared_port,
 'binding_status':'Exact value/label/member/J4 binding exists as a retained two-column table adapter, NOT as an operation-reflecting carrier graph functor.',
 'T9_consequence':'If rung12 endpoints are actual common assembly A,B, the unchanged two-incoming former yields137->1->1, not137->32->1. The32 first families encode carrier-index columns.',
 'uniqueness_scope':'Parallel assembly maps are legitimate rows unless endpoint uniqueness is required. Refining source by label changes their endpoint semantics.',
 'intended_T9_identified':False,'objective_complete':False,
 'next_selection':'Specify whether the rung table columns denote carrier indices or assembly endpoints, and whether T9 is fibre regrouping or assembly of parallel comparisons.',
 'inputs_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'check_shared_leg_dg_realization.py',HERE/'check_rung_transport_diagram.py',HERE/'check_typed_assembly_boundary_adapter.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} actual assembly/carrier endpoint-role checks')
print('Common assembly endpoints give137->1->1; carrier-index endpoints give137->32->32 or137->32->1.')
print('Original J4 agrees, but endpoint uniqueness and both operation-domain contracts do not.')
