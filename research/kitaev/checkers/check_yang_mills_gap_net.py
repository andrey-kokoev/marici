"""Dependency-free exact hostiles and by-reference work-net validation; no YM solver."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from copy import deepcopy
import argparse
import json

ROOT = Path(__file__).resolve().parents[3]
NET = 'research/kitaev/contracts/yang-mills-gap-net.v1.json'
OVERLAY = 'research/kitaev/contracts/yang-mills-foundational-attachments.v1.json'
OUT = ROOT / 'research/kitaev/results/yang-mills-gap-net-v1.json'

def require(ok, message):
    if not ok:
        raise ValueError(message)

def path(name):
    p = (ROOT / name).resolve()
    require(p.is_relative_to(ROOT), 'repository-relative path required')
    return p

def load(name):
    return json.loads(path(name).read_text(encoding='utf-8'))

def digest(name):
    return sha256(path(name).read_bytes()).hexdigest()

def ids(c):
    out = {n['id'] for n in c.get('conjectures', []) + c.get('obligations', [])}
    if isinstance(c.get('root'), dict):
        out.add(c['root']['id'])
    return out

def hostiles():
    collapse = [{'N': n, 'finite_gap': str(F(1, n)), 'normalized_excitation_energy': str(F(1, n))} for n in (1, 2, 4, 16, 256)]
    require(all(F(r['finite_gap']) > 0 for r in collapse), 'finite positivity control')
    # Family proof: for every epsilon>0 choose N>1/epsilon. Tests regress its formula.
    require(F(collapse[-1]['finite_gap']) < F(1, 100), 'gap-collapse residual')
    hidden = {'H_diagonal': ['0', '1', '1/256'], 'D_diagonal': [0, 1, 0], 'hidden_state': [0, 0, 1], 'hidden_norm_squared': '1', 'hidden_energy': '1/256', 'hidden_detection_squared': '0'}
    # H=(1,-1)^T(1,-1) is PSD; both coordinate costs are 1 but (1,1) is null.
    require(F(1)-2*F(1)+F(1) == 0, 'collective cancellation hostile')
    positive_samples = 0
    for x in range(-2, 3):
        for y in range(-2, 3):
            for z in range(-2, 3):
                require(2*F(y)**2+3*F(z)**2 >= 2*(F(y)**2+F(z)**2), 'positive detector control')
                positive_samples += 1
    return {
        'finite_gap_collapse': collapse,
        'all_N_argument': 'H_N=diag(0,1,1/2,...,1/N); all finite gaps are positive, while the compatible infinite diagonal operator has eigenvalues accumulating at zero.',
        'blind_detector': hidden,
        'collective_cost_hostile': {'PSD_matrix': [[1, -1], [-1, 1]], 'coordinate_costs': [1, 1], 'collective_vector': [1, 1], 'norm_squared': 2, 'energy': 0},
        'unit_conversion_hostile': {'bare_gap': '1', 'conversion_factor': '1/N', 'physical_gap': '1/N'},
        'positive_control': {'H': [0, 2, 3], 'P_vac': [1, 0, 0], 'D': [0, 1, 1], 'c': '1', 'epsilon': '2', 'Delta': '2', 'exact_vector_regressions': positive_samples, 'proof': 'q_H-2*||(I-P_vac)psi||^2=|psi_2|^2>=0 for every vector.'},
        'scope': 'Toy spectral/form models, not Yang-Mills or a physical atomic source.'
    }

def validate(c, a, refs, hodge):
    require(c['id'] == 'yang-mills-witnessed-gap-work-v1' and c['owner'] == 'marici.Kitaev' and c['iteration'] == 10, 'net identity/revision')
    prior = load(c['predecessor']['contract_snapshot'])
    require(prior['iteration'] == c['iteration'] - 1 and prior['source_pins'] == c['predecessor']['source_pins'], 'predecessor identity')
    require(c['classical_problem']['status'] == 'open' and c['classical_problem']['outcome'] is None and c['objective']['outcome'] is None, 'unreviewed theorem outcome')
    require(c['research_hypothesis']['status'] == 'open' and c['research_hypothesis']['outcome'] is None, 'hypothesis promoted')
    require(all(v is False for v in c['boundary'].values()) and all(v is False for v in a['boundary'].values()), 'boundary promotion')
    require(c['atomic_gap_branch']['source_selected'] is False and c['atomic_gap_branch']['source_H'] is None, 'unreviewed atomic source')
    nodes = c['conjectures']; by = {n['id']: n for n in nodes}
    require(len(by) == len(nodes) and c['objective']['target'] in by, 'node identity')
    visiting, done = set(), set()
    def visit(k):
        require(k in by, 'unknown prerequisite')
        require(k not in visiting, 'dependency cycle')
        if k in done:
            return
        visiting.add(k)
        for p in by[k]['depends_on']:
            visit(p)
        visiting.remove(k); done.add(k)
    for n in nodes:
        visit(n['id'])
        require(set(n['required_verdicts']) == set(n['depends_on']) and all(v == 'constructed' for v in n['required_verdicts'].values()), 'constructed prerequisite gate')
        require(n['outcome'] is None and n['statement'] and n['acceptance'] and n['falsifier'], 'scientific gate/outcome')
        if n['id'] == 'finite-positive-gap-controls':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and n['evidence'] == ['initial-hostiles'], 'controls evidence')
        elif n['id'] == 'spectral-scope':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and n['evidence'] == ['spectral-scope-su2'] and n['resolution_kind'] == 'selected_SU2_target_definition_and_single_plaquette_source_test', 'scope evidence')
        elif n['id'] == 'spectral-packet-dictionary':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and n['evidence'] == ['shared-link-packet'] and n['resolution_kind'] == 'seven_link_SU2_polynomial_packet_and_covariant_electric_detector', 'dictionary evidence')
        elif n['id'] == 'finite-gauge-source':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and n['evidence'] == ['ground-state-transfer'] and n['resolution_kind'] == 'finite_open_cubic_SU2_Hamiltonian_and_temporal_heat_kernel_transfer', 'finite source evidence')
        elif n['id'] == 'quotient-descent':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and n['evidence'] == ['quotient-descent-packet'] and n['resolution_kind'] == 'finite_SU2_orbit_measure_and_closed_horizontal_covariant_detector', 'quotient evidence')
        elif n['id'] == 'faithful-excitation-detection':
            require(n['status'] == 'resolved' and n['verdict'] == 'constructed' and n['evidence'] == ['uniform-detection'] and n['resolution_kind'] == 'uniform_finite_SU2_small_r_detection_by_actual_density_curvature', 'uniform finite-source detection evidence')
        else:
            require(n['status'] == n['verdict'] == 'open' and n['evidence'] == [], 'unreviewed witness closure')
    require('atomic-to-gauge-source-comparison' not in by['reviewed-gap-assembly']['depends_on'], 'atomic bridge imposed on independent YM route')
    require(by['reviewed-gap-assembly']['requires'] == ['independent-existence-and-gap-review'], 'review bypass')
    ready = [n['id'] for n in nodes if n['status'] == 'open' and not n['requires'] and all(by[d]['verdict'] == 'constructed' for d in n['depends_on'])]
    require(ready == c['ready_frontier'] == ['atomic-source-selection', 'continuum-correlation-construction', 'uniform-energy-cost'], 'stale frontier')
    require(a['work_net'] == NET and a['contracts']['gap'] == NET, 'overlay identity')
    require(a['contracts']['parent'] == hodge['contracts']['parent'] and a['contracts']['math'] == hodge['contracts']['math'] and a['contracts']['identity'] == hodge['contracts']['identity'], 'Hodge reference destinations changed')
    connection_ids = set()
    for e in a['connections']:
        require(e['id'] not in connection_ids, 'duplicate connection')
        connection_ids.add(e['id'])
        require(e['type'] in ('research_reference', 'candidate_review'), 'reference type')
        require(e['proof_bearing'] is False and e['discharges_target'] is False and e['blocks_local_research'] is False, 'reference proof promotion')
        require(e['source_node'] in ids(refs[e['source_net']]) and e['target_node'] in ids(refs[e['target_net']]), 'unresolved node reference')
        if e['target_net'] == 'gap' and e['target_port'] != 'physical-target-context':
            require(e['target_port'] in by[e['target_node']]['external_inputs'], 'undeclared local reference port')
    # Mirror all seven Hodge routes, including return-review directions, not just its main root.
    mapping = {'spectral-scope': 'scope-and-cycle-map', 'spectral-packet-dictionary': 'packet-coherence-dictionary', 'completion-stable-separation': 'rational-survival', 'reviewed-gap-assembly': 'counterexample-assembly'}
    def signature(e, gap=False):
        sn, tn = e['source_net'], e['target_net']; s, t = e['source_node'], e['target_node']
        if gap:
            if sn == 'gap': sn, s = 'hodge', mapping.get(s, s)
            if tn == 'gap': tn, t = 'hodge', mapping.get(t, t)
        return sn, s, tn, t, e['type']
    require({signature(e) for e in hodge['connections']} <= {signature(e, True) for e in a['connections']}, 'missing Hodge-equivalent reference/review link')
    index = a['reciprocal_index']; branches = refs['identity'][index['field']]
    matches = [b for b in branches if b['id'] == index['id']]
    require(len(matches) == 1, 'reciprocal branch index')
    b = matches[0]
    require(b['contract'] == NET and b['attachment_model'] == OVERLAY and b['node'] in by and b['proof_bearing'] is False and b['discharges_parent'] is False and b['outcome'] is None, 'reciprocal index promotion')
    require(len(a['external_obligations']) == 1 and a['external_obligations'][0]['available'] is False, 'external review availability')
    return ready

def negative_controls(c, a, refs, hodge):
    mutations = [
        ('theorem promotion', lambda x,y: x['boundary'].__setitem__('Yang_Mills_proved', True)),
        ('proof-bearing reference', lambda x,y: y['connections'][0].__setitem__('proof_bearing', True)),
        ('missing mirrored link', lambda x,y: y['connections'].pop(4)),
        ('cycle', lambda x,y: x['conjectures'][0]['depends_on'].append('reviewed-gap-assembly')),
        ('unknown reference', lambda x,y: y['connections'][0].__setitem__('source_node','invented-node')),
        ('false atomic source', lambda x,y: x['atomic_gap_branch'].__setitem__('source_selected', True)),
        ('invented gap witness', lambda x,y: x['conjectures'][4].update(status='resolved',verdict='constructed')),
        ('review bypass', lambda x,y: x['conjectures'][-1].__setitem__('requires', [])),
        ('rejected prerequisite admitted', lambda x,y: x['conjectures'][3]['required_verdicts'].__setitem__('finite-positive-gap-controls','rejected')),
        ('stale frontier', lambda x,y: x.__setitem__('ready_frontier',['reviewed-gap-assembly']))
    ]
    results = []
    for label, mutate in mutations:
        cc, aa = deepcopy(c), deepcopy(a); mutate(cc, aa)
        try:
            validate(cc, aa, {**refs, 'gap': cc}, hodge)
        except (ValueError, KeyError) as e:
            results.append({'control':label,'rejected':True,'diagnostic':str(e)})
        else:
            raise ValueError('corruption accepted: '+label)
    return results

def run(pin=False):
    c, a = load(NET), load(OVERLAY)
    refs = {key: c if key == 'gap' else load(name) for key, name in a['contracts'].items()}
    hodge = load(a['pattern_reference'])
    ready = validate(c, a, refs, hodge)
    controls = hostiles(); negative = negative_controls(c, a, refs, hodge)
    from check_yang_mills_spectral_scope import report as scope_report
    scope = scope_report()
    require(scope['passed'] and load('research/kitaev/results/yang-mills-spectral-scope-su2-v1.json') == scope, 'scope receipt stale')
    from check_yang_mills_shared_link_packet import report as shared_report
    shared = shared_report()
    require(shared['passed'] and shared['dictionary_gate_constructed'] and not shared['finite_gauge_source_gate_closed'] and load('research/kitaev/results/yang-mills-shared-link-packet-v1.json') == shared, 'shared-link receipt stale or overpromoted')
    from check_yang_mills_ground_state_transfer import report as ground_report
    ground = ground_report()
    require(ground['passed'] and ground['finite_gauge_source_constructed'] and not ground['volume_uniform_gap_proved'] and not ground['continuum_gap_proved'] and load('research/kitaev/results/yang-mills-ground-state-transfer-v1.json') == ground, 'ground/transfer receipt stale or overpromoted')
    from check_yang_mills_quotient_descent import report as quotient_report
    quotient = quotient_report()
    require(quotient['passed'] and quotient['quotient_descent_constructed'] and not quotient['weight_fixture_is_actual_ground_state'] and not quotient['volume_uniform_detection_proved'] and not quotient['continuum_gap_proved'] and load('research/kitaev/results/yang-mills-quotient-descent-v1.json') == quotient, 'quotient receipt stale or overpromoted')
    from check_yang_mills_ground_density_test import report as density_report
    density = density_report()
    require(density['passed'] and density['individual_plaquette_density_shortcut_rejected'] and not density['conditional_tensorization_proved_for_source'] and not density['volume_uniform_detection_proved'] and not density['continuum_gap_proved'] and load('research/kitaev/results/yang-mills-ground-density-test-v1.json') == density, 'density receipt stale or conditional premises promoted')
    from check_yang_mills_linked_density import report as linked_report
    linked = linked_report()
    require(linked['passed'] and linked['all_box_second_order_coefficient_constructed'] and not linked['uniform_remainder_proved'] and not linked['actual_source_uniform_influence_proved'] and not linked['conditional_tensorization_proved_for_source'] and not linked['volume_uniform_detection_proved'] and load('research/kitaev/results/yang-mills-linked-density-v1.json') == linked, 'linked receipt stale or Taylor surrogate promoted to source theorem')
    from check_yang_mills_remainder_equation import report as remainder_report
    remainder = remainder_report()
    require(remainder['passed'] and remainder['exact_log_remainder_equation_constructed'] and remainder['sup_norm_only_contraction_rejected'] and not remainder['uniform_remainder_proved'] and not remainder['convergent_cluster_expansion_proved'] and not remainder['volume_uniform_detection_proved'] and load('research/kitaev/results/yang-mills-remainder-equation-v1.json') == remainder, 'remainder receipt stale or formal recursion promoted to convergence')
    from check_yang_mills_weighted_fourier import report as weighted_report
    weighted = weighted_report()
    require(weighted['passed'] and weighted['weighted_global_nonlinear_bound_constructed'] and weighted['global_actual_ground_fixed_point_constructed'] and not weighted['anchored_contraction_proved'] and not weighted['fixed_coupling_uniform_remainder_proved'] and not weighted['volume_uniform_detection_proved'] and load('research/kitaev/results/yang-mills-weighted-fourier-v1.json') == weighted, 'weighted receipt stale or shrinking global window promoted to uniform theorem')
    from check_yang_mills_anchored_casimir import report as anchored_report
    anchored = anchored_report()
    require(anchored['passed'] and anchored['uniform_anchored_contraction_constructed'] and anchored['actual_source_uniform_remainder_proved'] and anchored['actual_source_uniform_influence_proved'] and not anchored['volume_uniform_detection_proved'] and not anchored['continuum_gap_proved'] and load('research/kitaev/results/yang-mills-anchored-casimir-v1.json') == anchored, 'anchored receipt stale or influence promoted to physical gap')
    from check_yang_mills_uniform_detection import report as detection_report
    detection = detection_report()
    require(detection['passed'] and detection['volume_uniform_finite_source_detection_proved'] and detection['finite_source_volume_uniform_gap_proved'] and not detection['weak_coupling_regime_covered'] and not detection['physical_energy_scaling_proved'] and not detection['continuum_gap_proved'] and load('research/kitaev/results/yang-mills-uniform-detection-v1.json') == detection, 'detection receipt stale or finite-source theorem promoted to continuum')
    artifacts = [x for x in c['artifacts'] if x['id'] in ('spectral-scope-su2', 'shared-link-packet', 'ground-state-transfer', 'quotient-descent-packet', 'ground-density-test', 'linked-density', 'remainder-equation', 'weighted-fourier', 'anchored-casimir', 'uniform-detection')]
    require(len(artifacts) == 10, 'scientific artifact census')
    extra_sources = [x[k] for x in artifacts for k in ('contract', 'note', 'checker', 'receipt')] + list(c['predecessor'].get(k) for k in ('contract_snapshot', 'validation_snapshot', 'source_pins'))
    sources = sorted(set([NET, OVERLAY, c['guide'], a['pattern_reference'], 'research/kitaev/checkers/check_yang_mills_gap_net.py', 'research/kitaev/scc-models/yang-mills-witnessed-gap-v1.json', 'research/kitaev/yang-mills-scc-continuum-mass-gap-microprogram.md', 'research/voevodsky/witness-sensitive-route-realization-v1.md'] + list(a['contracts'].values()) + extra_sources))
    hashes = {name:digest(name) for name in sources}
    pins = path(c['source_pins'])
    snapshot = {'schema':'marici.yang-mills-gap-source-pins.v1','sha256':hashes}
    if pin:
        require(not pins.exists(), 'source snapshot already exists; use explicit successor, never overwrite')
        pins.parent.mkdir(parents=True, exist_ok=True); pins.write_text(json.dumps(snapshot,indent=2)+'\n',encoding='utf-8')
    require(pins.exists() and load(c['source_pins']) == snapshot, 'source pins stale or missing')
    links = []
    for e in a['connections']:
        source = next((n for n in refs[e['source_net']].get('conjectures', []) if n['id'] == e['source_node']), {})
        links.append({'id':e['id'],'type':e['type'],'reference_resolves':True,'candidate_witness_available':source.get('verdict') == 'constructed' if e['type'] == 'candidate_review' else None,'target_discharged':False})
    report = {'schema':'marici.yang-mills-gap-net-result.v1','passed':True,'verification':'written_SU2_theorems_with_exact_regressions_and_structural_validation','ready_frontier':ready,'node_count':len(c['conjectures']),'iteration':c['iteration'],'scope_result':{'electric_gap':'3*kappa','magnetic_lower_bound':'3*kappa-lambda','continuum_gap_proved':False},'dictionary_result':{'shared_spin_energies':['9*kappa/2','13*kappa/2'],'naive_product_residual_squared':'3*kappa^2/4','magnetic_detector_faithful':False},'ground_transfer_result':{'actual_vacuum_detector_faithful_at_fixed_graph':True,'explicit_gap':ground['explicit_gap'],'temporal_reflection_positive_transfer':True,'volume_uniform_gap_proved':False,'continuum_gap_proved':False},'quotient_result':{'closed_covariant_horizontal_target':True,'hidden_mixed_loop_norm_squared':'3/4','volume_uniform_detection_proved':False},'density_result':{'equal_trace_log_density_difference_r2':'8/351','individual_plaquette_density_rejected':True,'conditional_tensorization_proved_for_source':False,'gate_closed':False},'linked_result':{'all_box_second_order_coefficient_constructed':True,'Taylor_surrogate_TV_row_bound':'8*abs(r)+175*r^2/26','uniform_actual_source_remainder_proved':False,'gate_closed':False},'remainder_result':{'exact_log_equation_constructed':True,'sup_norm_only_contraction_rejected':True,'convergent_cluster_expansion_proved':False,'gate_closed':False},'weighted_result':{'global_quadratic_bound':'3','global_window':'abs(r)*P<1/96','anchored_contraction_proved':False,'gate_closed':False},'anchored_result':{'coupling_window':'0<=lambda/kappa<27/262144','uniform_actual_source_remainder_proved':True,'actual_source_uniform_influence_proved':True,'volume_uniform_detection_proved':False,'gate_closed':False},'uniform_detection_result':{'coupling_window':detection['coupling_window'],'detector_constant':'5/64','finite_source_gap':'5*kappa/64','continuum_gap_proved':False,'physical_energy_scaling_proved':False},'connections':links,'hostiles':controls,'corruption_controls':negative,'source_pins':c['source_pins'],'outcome':None,'Yang_Mills_proved':False,'positive_atomic_gap_proved':False}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'nodes':report['node_count'],'links':len(links),'corruptions_rejected':len(negative),'ready_frontier':ready,'receipt':str(OUT.relative_to(ROOT))},indent=2))

if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--pin',action='store_true');run(parser.parse_args().pin)
