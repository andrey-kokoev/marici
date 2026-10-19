"""Validate the v5 admission without promoting C12 or changing C1-C11."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import admit_v5

ROOT=Path(__file__).resolve().parents[3]
HOME=Path(__file__).resolve().parent
RESULT=HOME/'results/low-energy-conjectures.v5.json'


def load(path):return json.loads(path.read_text(encoding='utf-8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(current,old,draft):
    assert current['schema']=='marici.scattering.low-energy-conjectures.v5'
    assert current['conjectures'][:11]==old['conjectures'],'historical proposition changed'
    assert current['edges']==old['edges'],'historical premise/target/successor edges changed'
    assert len(current['conjectures'])==12
    for key,value in old['models'].items():assert current['models'][key]==value
    node=current['conjectures'][-1]
    assert node['id']==admit_v5.ID and node['label']=='C12' and node['status']=='open'
    assert 'result' not in node,'unreviewed C12 outcome'
    assert node['statement']==node['quantifiers']==draft['statement']
    assert node['falsifier']==draft['falsifier'] and node['first_test']==draft['first_test']
    assert node['model']=='pentachoron_contact'
    assert node['prerequisite_certificates']==[draft['ground_certificate']]
    assert not any(e['to']==node['id'] for e in current['edges']),'C12 has no borrowed v4 truth premises'
    assert current['admission']['existing_proposition_outcomes_changed'] is False
    assert current['admission']['new_proof_or_physical_outcome_admitted'] is False


def build():
    old=load(ROOT/admit_v5.OLD);current=load(ROOT/admit_v5.NEW);draft=load(ROOT/admit_v5.DRAFT)
    validate(current,old,draft)
    assert current==admit_v5.contract(),'unreviewed admission drift'
    controls=[]
    for name in ('change-C1','promote-C12','borrow-refuted-premise','erase-quantifiers'):
        bad=copy.deepcopy(current)
        if name=='change-C1':bad['conjectures'][0]['status']='refuted'
        elif name=='promote-C12':bad['conjectures'][-1]['status']='established'
        elif name=='borrow-refuted-premise':bad['edges'].append({'from':old['conjectures'][2]['id'],'to':admit_v5.ID,'kind':'premise'})
        else:bad['conjectures'][-1]['quantifiers']='A threshold limit exists.'
        try:validate(bad,old,draft)
        except AssertionError:controls.append(name)
        else:raise AssertionError('hostile v5 accepted: '+name)
    # Fresh headless checks verify actual supporting math, not just pass flags.
    for script in ('check_low_energy_net_v4.py','check_pentachoron_ground_sector.py'):
        p=subprocess.run([sys.executable,str(HOME/script),'--check'],capture_output=True,text=True,timeout=120)
        assert p.returncode==0,script+': '+p.stderr+p.stdout
    paths={Path(__file__),Path(admit_v5.__file__),ROOT/admit_v5.OLD,ROOT/admit_v5.NEW,ROOT/admit_v5.DRAFT,
           HOME/'check_low_energy_net_v4.py',HOME/'check_pentachoron_ground_sector.py'}
    for node in current['conjectures']:paths.update(ROOT/p for p in node['sources'])
    return {'schema':'marici.scattering.low-energy-conjectures-receipt.v5','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(paths)},
            'propositions':12,'disposed_historical_propositions':11,'open_propositions':['C12'],
            'historical_nodes_and_edges_preserved':True,'new_proposition_outcomes_admitted':False,
            'C12_bright_threshold_regular':None,'fresh_support_checks':['v4 scoped net','pentachoron exact ground sector'],
            'hostile_controls_refused':controls,'physical_outcomes_admitted':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert load(RESULT)==r,'stale v5 receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','propositions','open_propositions','historical_nodes_and_edges_preserved','new_proposition_outcomes_admitted','hostile_controls_refused')}))


if __name__=='__main__':main()
