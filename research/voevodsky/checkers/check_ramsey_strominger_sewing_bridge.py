"""Read-only applicability audit of Strominger's actual retained fixture."""
import hashlib
import itertools
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
V = 'research/voevodsky/'
S = 'research/strominger/results/'
PATHS = [V+'contracts/ramsey-strominger-sewing-bridge-attempt.v1.json',
         V+'results/ramsey-native-PN-overlap-span-input-v1.json',
         S+'channel-assembled-native-fixture.json',
         S+'strict-native-comparison.json',
         S+'strict-native-comparison-verification.json']

def load(p): return json.loads((ROOT/p).read_text())
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()

def main():
    contract, ramsey, fixture, comparison, receipt = map(load, PATHS)
    assert receipt['status'] == 'passed'
    for p,h in receipt['sourceHashes'].items():
        assert sha(p) == h, 'stale comparison input: '+p
    # Also check direct dependencies of the imported field-sewing receipt.
    sewing = load(S+'channel-assembled-field-sewing.json')
    for p,h in sewing['sourceHashes'].items():
        assert sha(p) == h, 'stale sewing input: '+p
    packets = {p['id']:p for p in fixture['packets']}
    charts = {c['index']:c for c in fixture['charts']}
    cells = {c['id']:c for c in fixture['cells']}
    root = packets[fixture['rootPacket']]
    root_chart = charts[root['chart']]
    vertices = cells[root_chart['cell']]['vertices']
    faces = [set(vertices)-{v} for v in vertices]
    root_packets = [p for p in packets.values()
                    if charts[p['chart']]['species'] == 'proton'
                    and set(cells[charts[p['chart']]['cell']]['vertices']) == set(vertices)]
    role_contexts = {tuple(sorted((v,k[0]) for k,v in charts[p['chart']]['aliases'].items()
                                  if v in vertices)) for p in root_packets}
    eligible = sorted({i for p in root_packets for i,f in enumerate(faces)
                       if sum(charts[p['chart']]['aliases'][k] in f for k in ['M0','M1']) == 2})
    matches = []
    for op in fixture['operations']:
        if op['kind'] != 'PN' or op['source'] not in {p['id'] for p in root_packets}:
            continue
        a,b = packets[op['source']],packets[op['target']]
        ca,cb = charts[a['chart']],charts[b['chart']]
        face = next(i for i,f in enumerate(faces) if f == set(op['face']))
        contexts, exact = [], []
        for port in ramsey['ports']:
            sa,sb = port['source'],port['target']
            if (set(port['faceVertices']) == set(op['face'])
                and sa['chart']['aliases'] == ca['aliases']
                and sb['chart']['aliases'] == cb['aliases']
                and sa['chart']['species'] == ca['species']
                and sb['chart']['species'] == cb['species']):
                key = [port['chart'],port['face']]
                contexts.append(key)
                if all(x['origin'] == y['origin'] and x['permutation'] == y['permutation']
                       for x,y in [(a,sa['packet']),(b,sb['packet'])]):
                    exact.append(key)
        assert contexts, 'native PN interface not context-matched to Ramsey ports'
        matches.append({'operation':op['id'],'source':a['id'],'target':b['id'],
                        'facet':face,'context_matches':contexts,'exact_state_matches':exact})
    supplied = sorted({m['facet'] for m in matches})
    missing = sorted(set(range(4))-set(supplied))
    assert len(role_contexts) == 1 and len(eligible) == 2
    assert supplied == eligible and len(missing) == 2
    # Preserve the imported coefficient witness even where its field word is empty.
    witness = comparison['retainedOrderFiveWitness']
    assert witness['fieldFactorWord'] == [] and witness['coefficientOrder'] == 5
    assert witness['coefficientPermutation'] != list(range(5))
    pair_table = {(p['source'],p['target']):p for p in comparison['pairs']}
    assert len(pair_table) == 196
    restricted_pairs = []
    for a,b in itertools.product(root_packets, repeat=2):
        p = pair_table[a['id'],b['id']]
        assert p['full44ReadoutSquare'] and p['fiveBindingSquare']
        restricted_pairs.append([a['id'],b['id']])
    out = {'schema':'marici.ramsey-strominger-sewing-bridge.audit.v1',
           'status':'existing-fixture-matches-two-facets-not-four',
           'scope_id':contract['scope_id'],
           'root_packets':[p['id'] for p in root_packets],
           'root_role_context_count':len(role_contexts),
           'root_PN_operation_matches':matches,
           'supplied_facets':supplied,'missing_facets':missing,
           'missing_opposite_vertices':[vertices[i] for i in missing],
           'imported_root_comparison_pairs':len(restricted_pairs),
           'retained_order_five_witness':witness,
           'four_facet_coverage':False,'general_extension_refuted':False,
           'native_WG_restriction_derivation_proved':False,'parent_descent_resolved':False,
           'verification':'live direct-input hashes and interface matching; imported matrix checks not rerun',
           'source_sha256':{p:sha(p) for p in PATHS+[V+'checkers/check_ramsey_strominger_sewing_bridge.py']}}
    (ROOT/(V+'results/ramsey-strominger-sewing-bridge-v1.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__ == '__main__': main()
