"""Test the explicit registry bridge and preserve all unproved analytical gates."""
from pathlib import Path
from itertools import product
import copy
import hashlib
import json
from esd7_attachment_channel import produce, decode
from esd7_analytical_binding import bind, folded_simplex

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/strominger/results/'
REGISTRY = 'research/voevodsky/results/esd7_tetrahedron_prototype_registry.json'
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def rejects(assembly, registry):
    try:
        bind(assembly, registry)
    except ValueError:
        return True
    return False


def main():
    assembly = decode(produce(7))
    registry = json.loads((ROOT/REGISTRY).read_text())
    result = bind(assembly,registry)
    check('fresh geometry equals the prior generated attachment output', assembly == json.loads((ROOT/BASE/'esd7-channel-generated-assembly.json').read_text()))
    check('all343 source prototype records bind bijectively to actual generated tetrahedra',
          len(result['assignments']) == len({a['tetrahedron'] for a in result['assignments']}) == 343)
    check('binding is not a positional zip of unrelated IDs', any(
        row['tetrahedron'] != f'T{i:03d}' for i,index in enumerate(product(range(7),repeat=3))
        for row in result['assignments'] if row['index'] == list(index)))
    reverse_registry = copy.deepcopy(registry); reverse_registry['cells'].reverse()
    check('registry row permutation does not alter binding', bind(assembly,reverse_registry) == result)
    check('all784 shared face objects retain their full local contexts',
          len(result['faceBindings']) == 784 and sum(len(f['localContexts']) for f in result['faceBindings']) == 4*343)
    check('all588 internal face comparisons remain explicit obligations',
          sum(f['comparisonRequired'] for f in result['faceBindings']) == 588 and
          all(not f['comparisonDischarged'] for f in result['faceBindings']))
    check('both orientation signs are retained by the folding bridge', {a['orientation'] for a in result['assignments']} == {-1,1})
    check('source decay budgets retained on all343 H234 roles',
          all(a['H234DecayWitness'] for a in result['assignments']))
    check('no source label or unique-filler claim is imported as a computed filler',
          not result['sourceHigherCoherenceClaimsImportedAsProof'] and
          all(not a['fillerInstalled'] for a in result['assignments']) and
          all(not f['homotopyInstalled'] for f in result['faceBindings']))
    check('full114 channel, analytical coherence and global field transport stay unestablished',
          all(result[k] is False for k in ['full114ChannelEstablished','analyticalCoherenceDischarged','globalFieldTransportEstablished']))
    for scale in [1,2,3,4,5,6,7]:
        geometry = decode(produce(scale)); vertices = {v['id']:tuple(v['cumulative']) for v in geometry['vertices']}
        target = {tuple(vertices[v] for v in t['vertices']) for t in geometry['tetrahedra']}
        image = [folded_simplex(i) for i in product(range(scale),repeat=3)]
        check(f'sorting bridge bijective at scale{scale}', len(image) == len(set(image)) and set(image) == target)
    mutations = [
        ('duplicate registry index',lambda r:r['cells'].__setitem__(1,copy.deepcopy(r['cells'][0]))),
        ('missing registry record',lambda r:r['cells'].pop()),
        ('ID/index disagreement',lambda r:r['cells'][0].__setitem__('id','esd7:6,6,6')),
        ('out of range index',lambda r:r['cells'][0].__setitem__('index',[7,0,0])),
        ('unbound prototype variant',lambda r:r['cells'][0]['face_prototypes'].__setitem__('H123','identity')),
        ('insufficient decay budget',lambda r:r['cells'][0]['H234_decay_witness']['source_orders_for_target_orders'].__setitem__('1',0)),
    ]
    for name,mutate in mutations:
        bad = copy.deepcopy(registry); mutate(bad)
        check('reject '+name,rejects(assembly,bad))
    bad = copy.deepcopy(assembly); bad['triangles'][0]['homotopyObligation']['direct'] = bad['triangles'][0]['homotopyObligation']['composite'][0]
    check('reject mismatched face route endpoints',rejects(bad,registry))
    artifact = BASE+'esd7-analytical-prototype-binding.json'
    (ROOT/artifact).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    inputs = [REGISTRY,artifact,BASE+'esd7-channel-generated-assembly.json',
              'research/strominger/checkers/esd7_attachment_channel.py',
              'research/strominger/checkers/esd7_analytical_binding.py',
              'research/strominger/checkers/check_esd7_analytical_binding.py',
              'research/voevodsky/checkers/check_esd7_tetrahedron_prototype_registry.py']
    report = {'status':'passed','checks':checks,'check_count':len(checks),
              'boundTetrahedra':343,'boundFaces':784,'sharedFaceComparisons':588,
              'distinctRoleSharedFaces':sum(f['comparisonRequired'] and f['distinctLocalRoles'] for f in result['faceBindings']),
              'sharedRolePairs':result['sharedRolePairs'],'registryBridgeEstablished':True,
              'analyticalCoherenceDischarged':False,'globalFieldTransportEstablished':False,'full114ChannelEstablished':False,
              'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
              'scope':'Finite explicit prototype-registry bridge and boundary typing. Source analytical claims are retained as provenance, not replayed proofs or installed native field maps. Distinct face roles require comparison; they do not by themselves prove incompatibility.'}
    (ROOT/BASE/'esd7-analytical-binding-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','boundTetrahedra','sharedFaceComparisons','distinctRoleSharedFaces','sharedRolePairs']}))


if __name__ == '__main__':
    main()
