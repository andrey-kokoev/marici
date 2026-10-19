"""Record C12's first effort unit and a remaining-review planning snapshot.

Replaying this recorder does not spend another unit. Historical v2 forecasts and
admission records are preserved; v3 estimates condition on the first result.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HOME=Path(__file__).resolve().parent
KEY='low-energy:pentachoron-bright-threshold-regularity'
LEDGER='research/scattering/low-energy/contracts/pentachoron-threshold-attempt1.v1.json'
FORECAST='research/conjecture_net/contracts/low-energy-test-planning.v3.json'
CARDS='research/conjecture_net/contracts/low-energy-action-cards.v3.json'
KERNEL='research/scattering/low-energy/results/pentachoron-threshold-kernel.v1.json'
PROOF='research/scattering/low-energy/PENTACHORON-THRESHOLD-PROOF.md'
ACTION=('Use the one remaining C12 effort unit to independently review the threshold proof draft: re-read the source junction and flux convention, replay the exact ground and kernel certificates, and verify the square-root-free kernel argument, fixed dark-reducing complement, uniform inverse estimate, flux-factor cancellation and packet norm. Stop at a complete scoped proof, a concrete counterexample, or exhaustion of this final unit. Any unresolved sign/domain/normalization gap is inconclusive. Do not repeat the completed kernel search, silently renew the budget, or treat its pass as a C12 verdict.')


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()


def build():
    kernel=load(KERNEL)
    assert kernel['status']=='pass' and kernel['full_threshold_nullity']==2
    assert kernel['dark_reduced_threshold_block_invertible'] is True
    assert kernel['uniform_small_k_bound_reviewed'] is False and kernel['C12_outcome'] is None
    for p,h in kernel['source_sha256'].items():assert sha(p)==h,'stale kernel evidence: '+p
    ledger={'schema':'marici.scattering.low-energy-C12-attempt.v1','proposition':KEY,
            'initial_total_effort_units':2,'effort_units_used':1,'remaining_effort_units':1,
            'attempt_result':'inconclusive_pending_uniform_proof_review','proposition_status':'open',
            'completed':'Exact threshold kernel equals the two automatic dark directions; reduced block invertibility certified. Uniform argument drafted, not yet reviewed.',
            'remaining_action':ACTION,'automatic_renewal_allowed':False,'high_energy_protocol_units_used':0,
            'source_sha256':{p:sha(p) for p in (KERNEL,PROOF,'research/scattering/low-energy/record_c12_attempt1.py')},
            'new_proposition_outcome_admitted':False}
    model=copy.deepcopy(load('research/conjecture_net/contracts/low-energy-test-planning.v2.json'))
    cards=copy.deepcopy(load('research/conjecture_net/contracts/low-energy-action-cards.v2.json'))
    row=next(r for r in model['conjectures'] if r['id']==KEY)
    row['test'].update(next_action=ACTION,protocol_status='specified')
    basis='Assistant subjective re-elicitation after C12 effort unit 1; forecast of the remaining proof review, not theorem truth or independent calibration.'
    row['probability'].update(status='estimated',values={'accepted':.8,'rejected':.02,'inconclusive':.18},
        conditioning='Exact threshold-kernel criterion passed; full uniform-bound/flux/packet proof still awaits review.',
        uncertainty='A normalization, reducing-space or analytic-domain gap can overturn the draft; no assumption of independent test outcomes.',basis=basis)
    row['probability']['reason']=None
    row['test_cost'].update(status='estimated',assistant_effort_units=1,basis='One of the original two effort units remains; no renewed budget.',reason=None)
    model['extension']={'supersedes':'research/conjecture_net/contracts/low-energy-test-planning.v2.json',
                        'scope':'C12 remaining-review reforecast only; eleven historical rows unchanged.',
                        'attempt_record':LEDGER}
    card=next(r for r in cards['cards'] if r['id']==KEY)
    card.update(first_action=ACTION,stop_rule=ACTION)
    card['reuse_sources']=list(dict.fromkeys(card['reuse_sources']+[PROOF,KERNEL,LEDGER]))
    card['protocol_accounting']={'initial_effort_units':2,'used_effort_units':1,'remaining_effort_units':1,'attempt_record':LEDGER}
    assert model['conjectures'][:11]==load('research/conjecture_net/contracts/low-energy-test-planning.v2.json')['conjectures'][:11]
    return ledger,model,cards


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();objects=build()
    for path,value in zip((LEDGER,FORECAST,CARDS),objects):
        if a.check:assert load(path)==value,'stale attempt/planning snapshot: '+path
        else:
            if (ROOT/path).exists():assert load(path)==value,'refusing to overwrite changed attempt snapshot'
            (ROOT/path).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','C12':'open','effort_units_used':1,'remaining_effort_units':1,'high_energy_units_used':0}))


if __name__=='__main__':main()
