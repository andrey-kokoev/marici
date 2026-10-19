"""Explicit C12 resolution successor; v5 and admission forecasts stay frozen."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/conjecture_net'))
import plan_low_energy as adapter

OLD='research/scattering/low-energy/contracts/low-energy-scattering-conjectures.v5.json'
NEW='research/scattering/low-energy/contracts/low-energy-scattering-conjectures.v6.json'
REVIEW='research/scattering/low-energy/results/pentachoron-threshold-review.v1.json'
PROOF='research/scattering/low-energy/PENTACHORON-THRESHOLD-REVIEW.md'
LEDGER='research/scattering/low-energy/contracts/pentachoron-threshold-attempt2.v1.json'
PLANNING='research/conjecture_net/contracts/low-energy-test-planning.v4.json'
CARDS='research/conjecture_net/contracts/low-energy-action-cards.v4.json'


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()


def contract():
    review=load(REVIEW);assert review['scope_verdict']=='established'
    assert review['protocol']=={'initial_effort_units':2,'used_effort_units':2,'remaining_effort_units':0,'renewed':False}
    for path,h in review['source_sha256'].items():assert sha(path)==h,'stale reviewed proof: '+path
    old=load(OLD);new=copy.deepcopy(old);node=new['conjectures'][-1]
    assert node['label']=='C12' and node['status']=='open'
    assert node['statement']==review['statement'] and node['quantifiers']==review['quantifiers']
    node['status']='established'
    node['result']={'certificate':REVIEW,'certificate_sha256':sha(REVIEW),'proof':PROOF,
        'checker':'research/scattering/low-energy/check_pentachoron_threshold_review.py',
        'argument':'Exact full-rank ground/contact pairing and invertible H_C-theta give only the dark threshold kernel. A fixed reducing complement and uniform Neumann bound yield C=4a and the energy-normalized packet inequality.',
        'protocol_accounting':{'total_effort_units':2,'used_effort_units':2,'remaining_effort_units':0,'attempt_record':LEDGER}}
    node['next_action']='Resolved in the fixed contact fixture. Replay the source-bound certificates after changes. Higher thresholds, different contacts, local capture and physical binding remain separate questions; no protocol renewal is implied.'
    new.update(schema='marici.scattering.low-energy-conjectures.v6',supersedes=OLD,historical_proposition_contract=OLD,
        next_test='Use the shared live workbench. All twelve declared propositions have dispositions; coverage review remains separate and the original programme is not closed.')
    new['resolution']={'proposition':'C12','previous_contract':OLD,'previous_sha256':sha(OLD),
        'previous_status':'open','new_status':'established','review_receipt':REVIEW,
        'C1_C11_or_edges_changed':False,'physical_outcome_admitted':False,'protocol_renewed':False}
    return new


def remaining_objects(new):
    ledger={'schema':'marici.scattering.low-energy-C12-attempt.v1','proposition':'low-energy:'+new['conjectures'][-1]['id'],
        'initial_total_effort_units':2,'effort_units_used':2,'remaining_effort_units':0,
        'attempt_result':'accepted_scoped_proof','proposition_status':'established','automatic_renewal_allowed':False,
        'high_energy_protocol_units_used':0,'previous_attempt':'research/scattering/low-energy/contracts/pentachoron-threshold-attempt1.v1.json',
        'source_sha256':{p:sha(p) for p in (NEW,REVIEW,PROOF,'research/scattering/low-energy/contracts/pentachoron-threshold-attempt1.v1.json')}}
    model=copy.deepcopy(load('research/conjecture_net/contracts/low-energy-test-planning.v3.json'))
    cards=copy.deepcopy(load('research/conjecture_net/contracts/low-energy-action-cards.v3.json'))
    initial=adapter.planning.initial(adapter.adapt(new),{'low-energy':NEW})
    assert initial['conjectures'][:11]==model['conjectures'][:11]
    model['conjectures'][-1]=initial['conjectures'][-1]
    model['contracts']={'low-energy':NEW};model['source_sha256']={NEW:sha(NEW)}
    model['extension']={'supersedes':'research/conjecture_net/contracts/low-energy-test-planning.v3.json',
        'scope':'C12 resolved; forecast/cost now not_applicable, not a calibrated probability. Eleven historical rows unchanged.',
        'attempt_record':LEDGER}
    cards['cards']=[c for c in cards['cards'] if c['id']!=ledger['proposition']]
    cards['source_sha256']={NEW:sha(NEW)}
    return ledger,model,cards


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();new=contract()
    if a.check:assert load(NEW)==new,'unreviewed v6 change'
    else:
        if (ROOT/NEW).exists():assert load(NEW)==new,'refusing to overwrite changed v6'
        (ROOT/NEW).write_text(json.dumps(new,indent=2)+'\n',encoding='utf-8')
    for path,obj in zip((LEDGER,PLANNING,CARDS),remaining_objects(new)):
        if a.check:assert load(path)==obj,'stale resolution/planning snapshot: '+path
        else:
            if (ROOT/path).exists():assert load(path)==obj,'refusing to overwrite edited snapshot'
            (ROOT/path).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','C12':'established','C1_C11_changed':False,'used_units':2,'remaining_units':0}))


if __name__=='__main__':main()
