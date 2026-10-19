# /// script
# dependencies = ["sympy"]
# ///
"""Distinguish retained branch provenance, outer wiring, and branch readouts.

Original fixture is frozen. A separate shared-leg-admissible all-unit control
proves branch means cannot universally factor through tag-merged mean tables.
It does not claim the control is an admitted physical preparation or evolution.
"""
from contextlib import redirect_stdout
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/T9-branch-task-binding.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_137_retained_endpoint_readout.py'))
m=prior['m']; rows=m['source']; E=m['E']; dg=m['m']
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def branch(row): return 'a' if row.label[1]<121 else 's'
def read_branches(retained):
    leaves=m['leaves'](retained)
    return {tag:dg['add'](m['mean'](tuple(row for row in leaves if branch(row)==tag)),dg['scale'](-1,m['physical_reference'].value)) for tag in ('a','s')}
def quotient(input_rows):
    first=m['incoming_promotion'](input_rows,1,'inherited')
    mapped=tuple(replace(family,target=('endpoint-readout',*family.members[0].target[1:])) for family in first)
    return m['incoming_promotion'](mapped,2,'inherited')
check('endpoint-readout-chain-fresh',prior['result']['verification_status']=='pass')
original_read=read_branches(rows)
profiles={}
for policy in ('inherited','common','endpoint-only'):
    final=quotient(rows) if policy=='endpoint-only' else m['incoming_promotion'](m['incoming_promotion'](rows,1,policy),2,policy)
    check('branch-provenance-retained/'+policy,m['leaves'](final)==rows)
    check('branch-reader-square/'+policy,read_branches(final)==original_read)
    uniform=all(len({branch(row) for row in m['leaves']((family,))})==1 for family in final)
    profiles[policy]={'rows':len(final),'branch_query_recovers_from_members':True,'branch_is_uniform_in_each_outer_family':uniform}
check('retention-does-not-select-inherited-policy',all(p['branch_query_recovers_from_members'] for p in profiles.values()))
check('outer-branch-constancy-is-stronger',profiles['inherited']['branch_is_uniform_in_each_outer_family'] and not profiles['common']['branch_is_uniform_in_each_outer_family'] and not profiles['endpoint-only']['branch_is_uniform_in_each_outer_family'])
check('original-J4-branch-decomposition',dg['add'](dg['scale'](F(121,137),original_read['a']),dg['scale'](F(16,137),original_read['s']))==m['read_at_four'](m['indexed'](rows,'target')))
# Fixed model itself has matching numeric values on16 arrow/state labels.
check('numeric-response-cannot-identify-branch-on-original-data',all(rows[11*i+j].value==rows[121+4*i+j].value for i,j in product(range(4),repeat=2)))

# Exact finite SHARED-LEG control, not independently edited137 residuals.
# Keep labels, endpoints, uniform weights and d=2I. Both preparations have
# the same16 endpoint-family means; all leg maps remain invertible.
n=[sum(edge[1]==u for edge in E) for u in range(4)]
check('actual-incoming-fibre-sizes',n==[3,2,3,3])
eps=F(1,10); I=dg['I']
baseline=[]; changed=[]
for index,row in enumerate(rows):
    tag=branch(row)
    if tag=='a':
        i,j=divmod(index,11)
        X=dg['scale'](1+eps/n[E[i][1]],I); Y=I
    else:
        i,j=divmod(index-121,4)
        X=I; Y=dg['scale'](1-eps*n[j],I)
    check('control-leg-invertibility/'+str(index),X[0][0]!=0 and Y[0][0]!=0)
    baseline.append(replace(row,value=I))
    changed.append(replace(row,value=dg['mul'](Y,X)))
baseline=tuple(baseline); changed=tuple(changed)
base_final=quotient(baseline); changed_final=quotient(changed)
check('all16-merged-mean-record-fields-identical',tuple((r.label,r.source,r.target,r.mass,r.value) for r in base_final)==tuple((r.label,r.source,r.target,r.mass,r.value) for r in changed_final))
check('control-J4-identical',m['read_at_four'](m['indexed'](base_final,'target'))==m['read_at_four'](m['indexed'](changed_final,'target')))
base_branches=read_branches(base_final); changed_branches=read_branches(changed_final)
check('branch-readouts-differ-despite-identical-outer-means',base_branches!=changed_branches)
check('exact-arrow-branch-shift',dg['add'](changed_branches['a'],dg['scale'](-1,base_branches['a']))==dg['scale'](F(4,11)*eps,I))
check('exact-state-branch-shift',dg['add'](changed_branches['s'],dg['scale'](-1,base_branches['s']))==dg['scale'](-F(11,4)*eps,I))
check('member-reader-still-separates-these-preparations',m['leaves'](base_final)!=m['leaves'](changed_final))
# This supplies a constructive native-class hostile, rather than relying on
# the independent writable137-record task assumed in older memory models.
def serial_matrix(a): return [[str(x) for x in row] for row in a]
result={
 'schema':'marici.nima.T9-branch-task-binding.v1','verification_status':'pass','checks':checks,
 'original_branch_readouts':{tag:serial_matrix(value) for tag,value in original_read.items()},
 'candidate_profiles':profiles,
 'source_semantics':'Arrow/state tags are part of the supplied disjoint-union source and retained leg-path provenance (U versus V).',
 'clarification':'Merging target keys is not erasure of branch provenance when members remain retained. Requiring branch-uniform OUTER families is an additional wiring/task requirement.',
 'shared_leg_control':{'epsilon':str(eps),'arrow_left_leg':'X_i=(1+epsilon/n_target(i))*I; arrow right legs=I',
                      'state_right_leg':'T_v=(1-epsilon*n_v)*I; state left legs=I',
                      'equal_outer_endpoint_mean_rows':16,'same_J4':True,
                      'arrow_branch_shift':str(F(4,11)*eps),'state_branch_shift':str(-F(11,4)*eps),
                      'independent_record_memory_assumed':False},
 'observation_obstruction':'No function of the16 tag-merged outer mean rows alone can recover both branch means for this shared-leg input class. The full retained packet can.',
 'conditional_selection':'If outer target queries must expose tagged endpoint fibres directly, use inherited keys within the tested context class. If inherited member readers are allowed, all tested policies preserve the branch task.',
 'intended_T9_identified':False,'objective_complete':False,
 'remaining_contract':'Does the protected branch question read retained members, or must it factor through the outer promoted mean/endpoint interface?',
 'scope':'All-unit controls are separate allowed shared-leg mathematical preparations, not perturbations claimed to be physical evolution of the frozen original fixture.',
 'inputs_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'check_137_retained_endpoint_readout.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} branch-task binding checks')
print('Every retained policy preserves branch queries; only inherited keeps every outer family branch-uniform.')
print('Exact shared-leg control: identical16 outer means and J4, but branch means shift by2/55 and-11/40.')
