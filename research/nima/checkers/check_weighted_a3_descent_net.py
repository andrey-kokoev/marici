"""Structural and evidence-snapshot validation for Benincasa's weighted A3 net."""
import argparse
import copy
import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/conjecture_net'))
from graph_metrics import MetricAction, MetricGraph
CONTRACT = 'research/conjecture_net/contracts/weighted-a3-descent-work-net.v1.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def sha(path):
    return sha256((ROOT / path).read_bytes()).hexdigest()


def sources(c):
    return {p for a in c['artifacts'] for p in a['paths']}


def validate(c, pins):
    nodes = c['conjectures']
    by = {n['id']: n for n in nodes}
    graph = MetricGraph(tuple(MetricAction(n['id'], frozenset(n['depends_on']),
        status='active' if n['status'] == 'open' else n['status']) for n in nodes))
    graph.validate()
    artifacts = {a['id'] for a in c['artifacts']}
    require(len(artifacts) == len(c['artifacts']), 'duplicate artifact')
    ports = {p['id']: p for p in c['witness_ports']}
    require(len(ports) == len(c['witness_ports']), 'duplicate port')
    available = set()
    for witness in c['available_witnesses']:
        name = witness['id']
        require(name in ports and name not in available, 'unknown/duplicate witness')
        require(witness['evidence'] and set(witness['evidence']) <= artifacts and witness['verification'], 'witness lacks evidence')
        require(all((ROOT / p).is_file() for p in ports[name]['required_files']), 'witness missing source data')
        available.add(name)
    for n in nodes:
        require(n['statement'] and n['scope'] and n['acceptance'] and n['falsifier'], 'missing typed test')
        require(n['outcome'] is None and set(n['evidence']) <= artifacts, 'outcome/evidence')
        require(set(n.get('precursor_evidence', [])) <= artifacts, 'unknown precursor evidence')
        if n.get('precursor_evidence'):
            require(n.get('precursor_scope'), 'unscoped precursor evidence')
        require(set(n['requires']) <= set(ports), 'unknown witness port')
        if n['status'] == 'resolved':
            require(n['verdict'] in ('constructed', 'rejected') and n['evidence'] and n['evidence_level'], 'unsupported disposition')
            require(all(by[d]['status'] == 'resolved' for d in n['depends_on']), 'unresolved predecessor')
            require(set(n['requires']) <= available, 'missing required witness')
        else:
            require(n['status'] == n['verdict'] == 'open' and n['next_action'] and n['deliverable'], 'unactionable node')
        for dep, verdict in n.get('required_verdicts', {}).items():
            require(dep in n['depends_on'] and verdict == 'constructed', 'assembly gate')
            if n['status'] == 'resolved':
                require(by[dep]['verdict'] == verdict, 'assembly from nonpositive witness')
    require(by['incidence-is-a3-compatibility']['verdict'] == 'rejected', 'lost incidence rejection')
    require(by['nine-facet-typing-audit']['verdict'] == 'constructed' and
            by['nine-facet-typing-audit']['evidence'] == ['comparison-audit', 'status'], 'typing audit confused with failed descent')
    review = c['prior_research_review']
    require(review['evidence'] and set(review['evidence']) <= artifacts and review['verification'], 'prior review evidence')
    controls = {x['id']: x for x in c['comparison_controls']}
    require(len(controls) == len(c['comparison_controls']) and set(controls) == {
        'superfunction-is-not-canonical-chart', 'K-versus-K0',
        'auxiliary-versus-physical-strata', 'source-switch-and-orientation-regressions'}, 'missing comparison control')
    for control in controls.values():
        require(control['evidence'] and set(control['evidence']) <= artifacts and control['obligation'], 'untyped comparison control')
    require(controls['superfunction-is-not-canonical-chart']['forbidden_promotion'], 'superfunction promotion control')
    require(controls['K-versus-K0']['positive_facet_input'] == 'K0' and
            controls['K-versus-K0']['cluster_positive_input'] == 'K', 'K/K0 conflation')
    require(controls['auxiliary-versus-physical-strata']['auxiliary_a3_counts'] ==
            {'PP':10, 'PN':8, 'NN':3, 'total':21}, 'auxiliary index drift')
    expected_precursors = {
        'untransported-simple-forms': {'endpoint-switch-superfunction', 'component-selector-and-matching', 'update-toggle-controls'},
        'composite-normalization-definition': {'component-selector-and-matching', 'endpoint-switch-superfunction', 'scalar-facet-augmentation', 'flat-cluster-shortcut-audit'},
        'weighted-codimension-two-cancellation': {'auxiliary-stratum-index', 'selected-orientation-control'},
    }
    for node, expected in expected_precursors.items():
        require(expected <= set(by[node].get('precursor_evidence', [])), 'lost precursor binding: ' + node)
    require(c['objective']['outcome'] is None and c['objective']['target'] == 'weighted-a3-canonical-descent', 'root')
    require(set(by[c['objective']['target']]['required_verdicts']) ==
        {'normalized-nine-to-divisor-map', 'weighted-codimension-two-cancellation'}, 'assembly bypass')
    require('negative-simple-difference-forms' in by['normalized-nine-to-divisor-map']['depends_on'], 'difference forms bypass')
    require('composite-normalization-definition' in by['normalized-nine-to-divisor-map']['depends_on'], 'normalization bypass')
    require('normalized-nine-to-divisor-map' in by['weighted-codimension-two-cancellation']['depends_on'], 'premature residues')
    require('oriented-source-atlas-materialized' in by['normalized-nine-to-divisor-map']['requires'], 'source bundle bypass')
    frontier = [n['id'] for n in nodes if n['status'] == 'open' and
                set(n['requires']) <= available and all(by[d]['status'] == 'resolved' for d in n['depends_on'])]
    require(c['frontier'] == frontier, 'stale frontier')
    require(c['recommended_start'] in frontier if frontier else c['recommended_start'] is None, 'invalid start')
    for a in c['attachments']:
        require(set(a['nodes']) <= {n['id'] for n in load(a['contract'])['conjectures']}, 'attachment')
    for a in c['cross_references']:
        require((ROOT / a['contract']).is_file(), 'cross reference')
    require(set(pins['source_sha256']) == sources(c), 'pin coverage')
    for p, h in pins['source_sha256'].items():
        require((ROOT / p).resolve().is_relative_to(ROOT) and sha(p) == h, 'source drift: ' + p)
    audit = load('research/benincasa/results/a3_facet_to_bcfw_boundary_comparison.json')
    require(audit['source_chain'] == {'history_cells':20, 'internal_shared_facets':40,
        'physical_rank7_source_facets':80, 'physical_target_divisors':20,
        'all_internal_cancellation_complete':True}, 'source count drift')
    require(audit['typing']['present_in_artifacts'] is False and
            audit['summary']['fully_authorized_nine_facet_preimages'] == 0, 'audit snapshot changed; review successors')
    return frontier


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', action='store_true')
    args = parser.parse_args()
    c = load(CONTRACT)
    pinpath = ROOT / c['source_pins']
    if args.pin:
        require(not pinpath.exists(), 'refusing implicit re-pin')
        data = {p: sha(p) for p in sorted(sources(c))}
        pinpath.write_text(json.dumps({'schema':'marici.weighted-a3-source-pins.v1', 'source_sha256':data}, indent=2)+'\n', encoding='utf-8')
    pins = load(pinpath)
    frontier = validate(c, pins)
    rejected = []
    for name in ('cycle','unknown-edge','lost-rejection','audit-as-refutation','difference-bypass',
                 'normalization-bypass','premature-residues','bundle-bypass','assembly-bypass',
                 'premature-assembly','stale-frontier','untyped-witness','stale-pin',
                 'unknown-precursor','lost-precursor','K0-replaced-by-K','lost-stratum-control',
                 'unscoped-precursor'):
        b, p = copy.deepcopy(c), copy.deepcopy(pins)
        by = {n['id']: n for n in b['conjectures']}
        if name == 'cycle': by['selected-chart-census']['depends_on'] = ['weighted-a3-canonical-descent']
        elif name == 'unknown-edge': by['selected-chart-census']['depends_on'] = ['absent']
        elif name == 'lost-rejection': by['incidence-is-a3-compatibility']['verdict'] = 'constructed'
        elif name == 'audit-as-refutation': by['nine-facet-typing-audit']['verdict'] = 'rejected'
        elif name == 'difference-bypass': by['normalized-nine-to-divisor-map']['depends_on'].remove('negative-simple-difference-forms')
        elif name == 'normalization-bypass': by['normalized-nine-to-divisor-map']['depends_on'].remove('composite-normalization-definition')
        elif name == 'premature-residues': by['weighted-codimension-two-cancellation']['depends_on'] = ['complete-bcfw-source-chain']
        elif name == 'bundle-bypass': by['normalized-nine-to-divisor-map']['requires'] = []
        elif name == 'assembly-bypass': by['weighted-a3-canonical-descent']['required_verdicts'] = {}
        elif name == 'premature-assembly': by['weighted-a3-canonical-descent'].update(status='resolved', verdict='constructed', evidence=['bcfw-completion'], evidence_level='receipt')
        elif name == 'stale-frontier': b['frontier'] = []
        elif name == 'untyped-witness': by['common-oriented-simple-charts']['requires'] = ['absent']
        elif name == 'unknown-precursor': by['untransported-simple-forms']['precursor_evidence'].append('absent')
        elif name == 'lost-precursor': by['untransported-simple-forms']['precursor_evidence'] = []
        elif name == 'K0-replaced-by-K': next(x for x in b['comparison_controls'] if x['id'] == 'K-versus-K0')['positive_facet_input'] = 'K'
        elif name == 'lost-stratum-control': b['comparison_controls'] = [x for x in b['comparison_controls'] if x['id'] != 'auxiliary-versus-physical-strata']
        elif name == 'unscoped-precursor': by['composite-normalization-definition']['precursor_scope'] = ''
        else: p['source_sha256'][next(iter(p['source_sha256']))] = '0'*64
        try:
            validate(b, p)
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError('hostile accepted: ' + name)
    require(sum(e['contract'] == CONTRACT for e in load('research/conjecture_net/registry.json')['nets']) == 1, 'registry')
    result = {'schema':'marici.weighted-a3-net-validation.v1','status':'pass',
        'node_count':len(c['conjectures']), 'frontier':frontier,
        'source_pin_count':len(sources(c)), 'rejected_hostiles':rejected,
        'missing_replay_inputs':[p for p in c['replay_inputs']['paths'] if not (ROOT/p).is_file()],
        'contract_sha256':sha(CONTRACT),'checker_sha256':sha(Path(__file__)),
        'pins_sha256':sha(pinpath),'source_suites_rerun':False}
    (ROOT/'research/nima/results/weighted-a3-descent-net-validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
