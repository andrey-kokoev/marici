"""Local source identities, candidate path bookkeeping and no-promotion tests."""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/scattering/seed-composition'
CONTRACT = BASE / 'contracts/seed-composition-work-net.v1.json'


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def validate(net, pins):
    expected = {
        'isotope-atlas-evidence': ('evidence', 'source_located', []),
        'arrow-seed-collection-evidence': ('evidence', 'source_located', []),
        'atlas-seed-source-correspondence': ('conjecture', 'open', ['isotope-atlas-evidence', 'arrow-seed-collection-evidence']),
        'three-vertex-overlap-candidate': ('candidate', 'candidate_recorded', ['arrow-seed-collection-evidence']),
        'admissible-composition-and-independent-separation': ('conjecture', 'open', ['atlas-seed-source-correspondence', 'three-vertex-overlap-candidate']),
        'physical-photon-channel-binding': ('conjecture', 'open', ['admissible-composition-and-independent-separation']),
        'source-faithful-seed-composition': ('conjecture', 'open', ['atlas-seed-source-correspondence', 'admissible-composition-and-independent-separation', 'physical-photon-channel-binding'])
    }
    if net['objective'] != {'target':'source-faithful-seed-composition','outcome':None} or any(net['boundary'].values()):
        raise ValueError('physical/formal root promotion')
    if net['registration'] != 'local_research_net_not_physical_admission':
        raise ValueError('unadmitted registration')
    if net['source_pins'] != 'research/scattering/seed-composition/contracts/source-pins.v1.json':
        raise ValueError('pins disconnected')
    if [n['id'] for n in net['conjectures']] != list(expected):
        raise ValueError('missing/reordered node')
    for n in net['conjectures']:
        if (n['kind'],n['status'],n['depends_on']) != expected[n['id']] or n['outcome'] is not None:
            raise ValueError('node promoted or dependency changed')
        if not set(n.get('evidence',[])) <= set(pins['source_sha256']):
            raise ValueError('unpinned evidence')
    if net['frontier'] != ['atlas-seed-source-correspondence','admissible-composition-and-independent-separation']:
        raise ValueError('frontier bypass')


def check_paths(c):
    if any(c['boundary'].values()) or c['identification_is_supplied_not_derived'] is not True:
        raise ValueError('candidate promoted')
    if c['primitive_cycles'] != {'electron':['A','B','C','D','E','A'], 'positron':['A','Ep','Dp','C','B','A']}:
        raise ValueError('primitive seeds changed')
    primitive = [edge for cycle in c['primitive_cycles'].values() for edge in zip(cycle,cycle[1:])]
    paths = {tuple(x['edge']):x['path'] for x in c['displayed_composites']}
    all_uses = []
    occurrences = 0
    for pair in c['displayed_triangle_pairs']:
        if len(pair) != 2 or any(len(t)!=4 or t[0]!=t[-1] or len(set(t[:-1]))!=3 for t in pair):
            raise ValueError('not two triangular cycles')
        edges = [edge for t in pair for edge in zip(t,t[1:])]
        if len(set(v for edge in edges for v in edge))!=4 or len({frozenset(edge) for edge in edges})!=5:
            raise ValueError('not shared-edge support')
        if sum((v,u) in edges for u,v in edges)!=2:
            raise ValueError('shared edge not oppositely directed')
        for edge in edges:
            path=paths.get(edge,list(edge))
            if (path[0],path[-1])!=edge:
                raise ValueError('path endpoint mismatch')
            expanded=list(zip(path,path[1:]))
            if not set(expanded)<=set(primitive):
                raise ValueError('new primitive hidden in composite')
            all_uses.extend(expanded)
        occurrences+=len(edges)
    actual={'vertices':len({v for e in primitive for v in e}),'primitive_occurrences':len(primitive), 'displayed_occurrences':occurrences,'expanded_primitive_usages':len(all_uses)}
    if actual!=c['expected_counts'] or actual!={'vertices':7,'primitive_occurrences':10,'displayed_occurrences':12,'expanded_primitive_usages':18} or set(all_uses)!=set(primitive):
        raise ValueError('retained count mismatch')
    expected=Counter({edge:3 if edge in {('A','B'),('B','C'),('C','B'),('B','A')} else 1 for edge in primitive})
    if Counter(all_uses)!=expected:
        raise ValueError('history reuse changed')
    return actual


def main():
    net=load(CONTRACT);pins=load(BASE/'contracts/source-pins.v1.json')
    validate(net,pins)
    for path,sha in pins['source_sha256'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=sha:
            raise ValueError('source changed: '+path)
    c=load(BASE/'three-vertex-candidate.v1.json');counts=check_paths(c)
    refused=0
    for key in net['boundary']:
        bad=copy.deepcopy(net);bad['boundary'][key]=True
        try: validate(bad,pins)
        except ValueError: refused+=1
        else: raise AssertionError('promotion accepted')
    for key in c['boundary']:
        bad=copy.deepcopy(c);bad['boundary'][key]=True
        try: check_paths(bad)
        except ValueError: refused+=1
        else: raise AssertionError('candidate promotion accepted')
    bad=copy.deepcopy(net);bad['conjectures'][4]['depends_on']=[]
    try: validate(bad,pins)
    except ValueError: refused+=1
    else: raise AssertionError('gate bypass accepted')
    print(json.dumps({'status':'pass','nodes':len(net['conjectures']),'pinned_sources':len(pins['source_sha256']),'candidate_counts':counts,'promotion_and_gate_hostiles_refused':refused,'source_suites_replayed':False}))


if __name__=='__main__':
    main()
