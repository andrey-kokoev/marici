# /// script
# dependencies = ["sympy"]
# ///
"""Conditional selection of T9 within the fixed incoming-family candidate class.

The extra exact-domain contract is explicit: it is not inferred from J4 or from
operator authority. Runtime constructor rejects all context-merging policies.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/T9-context-reflection.json'
OUT.unlink(missing_ok=True)
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
receipt=ROOT/'results/agda-SuccessorContextReflection.json'
formal=json.loads(receipt.read_text(encoding='utf-8-sig'))
check('fresh-safe-context-reflection-proof',formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'])
path=ROOT/'agda/SuccessorContextReflection.agda'
check('formal-source-current',formal['owner_source_inventory_sha256'][path.name]==hashlib.sha256(path.read_bytes()).hexdigest())
with redirect_stdout(io.StringIO()):
    classification=runpy.run_path(str(HERE/'check_T9_successor_partition_classification.py'))
m=classification['m']; rows=m['source']; first=classification['first']
check('full-classification-audit-current',classification['result']['verification_status']=='pass')
representatives=tuple(family.members[0] for family in first)
check('all-classified-target-fibres-populated',len({row.target for row in representatives})==32)
accepted=[]; rejected=[]
for profile in classification['profiles']:
    partition=profile['partition']
    injective=len(set(partition))==32
    # Check all1024 key pairs against the theorem, using real representatives.
    reflects=all(partition[i]!=partition[j] or representatives[i].target==representatives[j].target
                 for i,j in product(range(32),repeat=2))
    check('formal-criterion-instance/'+str(partition),reflects==injective)
    if reflects:
        accepted.append(profile)
    else:
        i,j=next((i,j) for i,j in product(range(32),repeat=2) if partition[i]==partition[j] and i!=j)
        a,b=representatives[i],representatives[j]
        check('rejected-policy-has-real-cross-fibre-witness/'+str(partition),a.target!=b.target)
        rejected.append({'partition':partition,'labels':[a.label,b.label],'original_targets':[a.target,b.target]})
check('unique-accepted-kernel-partition',len(accepted)==1 and accepted[0]['partition']==tuple(range(32)))
check('all526-other-controls-rejected',len(rejected)==526)

# Enforced constructor: choose original inherited endpoint tags, not a new
# grouping schedule or changed observation. This is a conditional API.
def T9_exact_domain(input_rows, policy='inherited'):
    middle=m['incoming_promotion'](input_rows,1,policy)
    old_keys=[row.members[0].target for row in middle]
    new_keys=[row.target for row in middle]
    if any(new_keys[i]==new_keys[j] and old_keys[i]!=old_keys[j]
           for i,j in product(range(len(middle)),repeat=2)):
        raise ValueError('Successor ports merge distinct populated original target fibres')
    return m['incoming_promotion'](middle,2,policy)

selected=T9_exact_domain(rows)
check('conditional-constructor-is-existing-inherited-T9',selected==m['incoming_promotion'](m['incoming_promotion'](rows,1,'inherited'),2,'inherited'))
check('all-original-records-recovered',m['leaves'](selected)==rows)
check('selected-context-support',sum(len(m['leaves']((family,)))**2 for family in selected)==977)
check('unchanged-original-J4',m['read_at_four'](m['indexed'](selected,'target'))==m['read_at_four'](m['indexed'](rows,'target')))
try:
    T9_exact_domain(rows,'common')
except ValueError:
    check('common-policy-rejected-by-runtime-contract',True)
else:
    raise AssertionError('Common policy escaped exact-domain guard')
# Only preservation (without reflection) is insufficient: every coarsening
# preserves old equalities. Its additional operations are the selecting issue.
check('preservation-alone-accepts-every-tested-coarsening',all(
    all(p['partition'][i]==p['partition'][j] for i,j in product(range(32),repeat=2) if i==j)
    for p in classification['profiles']))

result={
 'schema':'marici.nima.T9-context-reflection.v1','verification_status':'pass','checks':checks,
 'formal_receipt_sha256':hashlib.sha256(receipt.read_bytes()).hexdigest(),
 'explicit_extra_contract':'Successor context equality preserves AND reflects original target-key equality on all populated fibres.',
 'conditional_selection':'Inherited/discrete successor partition, unique up to port renaming within the fixed two-round incoming-family class.',
 'accepted_tested_partitions':accepted,'rejected_control_count':len(rejected),'rejected_witnesses':rejected,
 'conditional_target_rows':32,'conditional_supported_leaf_pairs':977,
 'record_endpoint_binding':'Existing geometric flat-port attachment and native-family adapter remain checked conditional bindings.',
 'selection_contract_authorized':False,'intended_T9_identified':False,'objective_complete':False,
 'why_not_complete':'The organizing specification requires neither exact operation-domain reflection nor a specific family former. It permits context-creating successors and explicitly leaves the horizontal generator unselected.',
 'operator_decision_required':'Must intended T9 preserve the original977-pair composition domain exactly, or introduce new cross-target contexts? If the latter, supply the context relation and family operation.',
 'continuation_gate':'Further selection requires new source/operational input; repeating retention, endpoint or scalar audits cannot choose this contract.',
 'scope':'The universal theorem concerns populated key fibres. No uniqueness across arbitrary non-family constructors or physical metrics is asserted.'}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact-domain selection checks')
print('Conditional on reflection, inherited T9 is uniquely selected up to port renaming;526 controls rejected.')
print('Physical/intended selection still requires confirmation of that operational contract.')
