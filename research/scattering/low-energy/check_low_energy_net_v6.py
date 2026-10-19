"""Validate the reviewed v6 C12 resolution, preserving all prior scopes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import resolve_c12_v6 as resolution

ROOT=Path(__file__).resolve().parents[3]
HOME=Path(__file__).resolve().parent
RESULT=HOME/'results/low-energy-conjectures.v6.json'


def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def validate(new,old):
    assert new['schema']=='marici.scattering.low-energy-conjectures.v6'
    assert new['conjectures'][:11]==old['conjectures'][:11] and len(new['conjectures'])==12
    assert new['models']==old['models'] and new['edges']==old['edges']
    node=new['conjectures'][-1];prior=old['conjectures'][-1]
    assert {k:v for k,v in node.items() if k not in ('status','result','next_action')}=={
        k:v for k,v in prior.items() if k not in ('status','result','next_action')},'C12 scope changed'
    assert node['status']=='established' and node['result']['certificate']==resolution.REVIEW
    assert node['result']['certificate_sha256']==sha(ROOT/resolution.REVIEW)
    budget=node['result']['protocol_accounting']
    assert budget['total_effort_units']==budget['used_effort_units']==2 and budget['remaining_effort_units']==0
    assert new['resolution']['C1_C11_or_edges_changed'] is False
    assert new['resolution']['physical_outcome_admitted'] is False


def build():
    new=load(ROOT/resolution.NEW);old=load(ROOT/resolution.OLD);validate(new,old)
    assert new==resolution.contract(),'v6 differs from reviewed resolution'
    ledger=load(ROOT/resolution.LEDGER)
    assert ledger['effort_units_used']==2 and ledger['remaining_effort_units']==0 and ledger['automatic_renewal_allowed'] is False
    for p,h in ledger['source_sha256'].items():assert sha(ROOT/p)==h
    controls=[]
    for name in ('change-C1','erase-C12-quantifier','restore-budget','swap-proof-receipt'):
        bad=copy.deepcopy(new)
        if name=='change-C1':bad['conjectures'][0]['status']='refuted'
        elif name=='erase-C12-quantifier':bad['conjectures'][-1]['quantifiers']='A limit exists.'
        elif name=='restore-budget':bad['conjectures'][-1]['result']['protocol_accounting']['remaining_effort_units']=2
        else:bad['conjectures'][-1]['result']['certificate']=old['conjectures'][0]['result']['certificate']
        try:validate(bad,old)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile resolution accepted: '+name)
    for script in ('check_low_energy_net_v5.py','check_pentachoron_threshold_review.py'):
        p=subprocess.run([sys.executable,str(HOME/script),'--check'],capture_output=True,text=True,timeout=180)
        assert p.returncode==0,p.stdout+p.stderr
    paths={Path(__file__),Path(resolution.__file__),ROOT/resolution.NEW,ROOT/resolution.OLD,
           ROOT/resolution.REVIEW,ROOT/resolution.PROOF,ROOT/resolution.LEDGER}
    review=load(ROOT/resolution.REVIEW);paths.update(ROOT/p for p in review['source_sha256'])
    for node in new['conjectures']:paths.update(ROOT/p for p in node['sources'])
    return {'schema':'marici.scattering.low-energy-conjectures-receipt.v6','status':'pass',
        'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(paths)},
        'propositions':12,'disposed_propositions':12,'open_propositions':[],
        'C12':'established','C1_C11_and_edges_unchanged':True,
        'C12_protocol':{'used_units':2,'remaining_units':0,'renewed':False},
        'analytic_argument_machine_formalized':False,'programme_coverage_complete':False,
        'physical_outcomes_admitted':False,'hostile_controls_refused':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert load(RESULT)==r,'stale v6 receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','propositions','disposed_propositions','C12','C12_protocol','hostile_controls_refused')}))


if __name__=='__main__':main()
