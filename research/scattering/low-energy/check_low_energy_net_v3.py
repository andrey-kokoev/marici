"""Validate v3 external seed obligation and preserve all v2 research gates."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
from check_low_energy_net_v2 import validate as validate_v2

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT/'research/scattering/low-energy/contracts/low-energy-scattering-work-net.v3.json'
PINS = ROOT/'research/scattering/low-energy/contracts/low-energy-scattering-source-pins.v3.json'
SEED = 'research/scattering/seed-composition/contracts/seed-composition-work-net.v1.json'
EXTERNAL = 'seed-composition-external-obligation'
PHOTON = 'electron-positron-two-three-photon-channel-realization'


def load(p):
    return json.loads(p.read_text(encoding='utf-8'))


def validate(net,pins):
    if net['schema']!='marici.scattering.low-energy-work-net.v3' or net['supersedes']!='research/scattering/low-energy/contracts/low-energy-scattering-work-net.v2.json' or net['source_pins']!=PINS.relative_to(ROOT).as_posix():
        raise ValueError('v3 version/pins mismatch')
    nodes={n['id']:n for n in net['conjectures']}
    if len(nodes)!=12 or len(net['conjectures'])!=12:
        raise ValueError('node omission/duplication')
    ext=nodes[EXTERNAL]
    if ext['status']!='open' or ext['verdict']!='open' or ext['outcome'] is not None or ext['depends_on']!=['branch-scope-and-source-inventory']:
        raise ValueError('external obligation promoted')
    expected={'contract':SEED,'node':'admissible-composition-and-independent-separation','relation':'scoped_research_prerequisite_not_proof_import'}
    if ext['external_dependency']!=expected or SEED not in ext['evidence'] or not set(ext['evidence'])<=set(pins['source_sha256']):
        raise ValueError('external attachment broken')
    if nodes[PHOTON]['depends_on']!=['shape-merge-split-two-three-output-candidate',EXTERNAL] or net['frontier'][-1]!=EXTERNAL:
        raise ValueError('photon dependency bypass')
    ids=[n['id'] for n in net['conjectures']]
    if ids.index(EXTERNAL)>=ids.index(PHOTON):
        raise ValueError('external prerequisite ordering')
    # Restrict to the predecessor subgraph; no inherited gate may disappear.
    projected=copy.deepcopy(net)
    projected['schema']='marici.scattering.low-energy-work-net.v2'
    projected['supersedes']='research/scattering/low-energy/contracts/low-energy-scattering-work-net.v1.json'
    projected['source_pins']='research/scattering/low-energy/contracts/low-energy-scattering-source-pins.v2.json'
    projected['conjectures']=[n for n in projected['conjectures'] if n['id']!=EXTERNAL]
    for n in projected['conjectures']:
        if n['id']==PHOTON:n['depends_on'].remove(EXTERNAL)
    projected['frontier'].pop()
    validate_v2(projected,pins)


def main():
    net,pins=load(CONTRACT),load(PINS)
    validate(net,pins)
    for p,h in pins['source_sha256'].items():
        if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:
            raise ValueError('stale source: '+p)
    seed=load(ROOT/SEED)
    if not any(n['id']=='admissible-composition-and-independent-separation' and n['status']=='open' for n in seed['conjectures']):
        raise ValueError('producer gate not found at scoped status')
    spec=importlib.util.spec_from_file_location('seed_net',ROOT/'research/scattering/seed-composition/check_seed_composition_net.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.main()
    rejected=0
    for kind in ('remove_dependency','promote_external','physical','root'):
        bad=copy.deepcopy(net);nodes={n['id']:n for n in bad['conjectures']}
        if kind=='remove_dependency':nodes[PHOTON]['depends_on'].remove(EXTERNAL)
        elif kind=='promote_external':nodes[EXTERNAL]['outcome']='++'
        elif kind=='physical':bad['boundary']['two_photon_channel_physically_identified']=True
        else:bad['objective']['outcome']='++'
        try:validate(bad,pins)
        except ValueError:rejected+=1
        else:raise AssertionError('hostile accepted: '+kind)
    print(json.dumps({'status':'pass','nodes':len(net['conjectures']),'pinned_sources':len(pins['source_sha256']),'external_producer_validated':SEED,'hostiles_refused':rejected}))


if __name__=='__main__':main()
