"""Validate the successor net and its live pinned import; do not prove open goals."""
from pathlib import Path
import hashlib
import json
import sys

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / 'research/conjecture_net'))
from outcome_reference import SEMANTICS, OutcomeReferenceError, file_hash, load, require, resolve

CONTRACT = 'research/nima/contracts/completion-refinement-conjecture-net.v1.json'
OUT = REPO / 'research/nima/results/completion-refinement-conjecture-net.json'

def admit_addition_foundations(root, node, component, pins, external_pins):
    """Admit only this partial checkpoint; it cannot resolve the pi node."""
    require(node['id'] == 'completion-pi-half-turn'
            and component['id'] == 'trig-addition-foundations', 'unknown supporting component')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['schema'] == 'marici.nima.trig-addition-foundations-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id']
            and receipt['module'] == 'TickTrigPartialSumTransfer'
            and receipt['status'] == 'pass' and receipt['exit_code'] == 0
            and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
            and receipt['sources_stable'] and receipt['outcome'] is None
            and receipt['attempt_state'] == 'in_progress'
            and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
            and all(receipt[field] is True for field in (
                'distinct_input_coefficients_freshly_proved',
                'uniform_addition_defect_decay_freshly_proved',
                'rational_partial_sum_transfer_freshly_proved',
                'all_later_cutoffs', 'uniform_on_bounded_input_pairs'))
            and all(receipt[field] is False for field in (
                'completion_addition_laws_proved', 'arctangent_cayley_bridge_proved',
                'pi_endpoints_proved', 'standard_pi_identification_kernel_proved',
                'unitary_half_turn_proved', 'full_claim_proved'))
            and {'cosine-addition-coefficient', 'sine-addition-coefficient',
                 'AtRadius.cosine-addition-all-later', 'AtRadius.sine-addition-all-later',
                 'cosine-partial-sum-to-operational', 'sine-partial-sum-to-operational'}
                <= set(receipt['theorems']),
            'addition foundations lack fresh component closure or overclaim completion laws')
    require({'research/nima/agda/' + name + '.agda' for name in (
        'TickTrigAdditionCoefficients', 'TickTrigAdditionResidual', 'TickTrigPartialSumTransfer')}
        <= set(receipt['source_sha256']), 'unpinned addition foundation modules')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale supporting component evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale supporting component kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)


def admit_completion_trig_addition(root, node, component, pins, external_pins):
    """Addition now closes as a component; pi and regularity still do not."""
    require(node['id'] == 'completion-pi-half-turn'
            and component['id'] == 'completion-trig-addition', 'unknown supporting component')
    path = component['receipt']
    receipt = load(root, path)
    remaining = ['operational arctangent/Cayley bridge',
                 'standard-pi identification at the accepted formal level', 'MachinEndpoints']
    require(receipt['schema'] == 'marici.nima.completion-trig-addition-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id']
            and receipt['component_scope_id'] == 'operational-completion-trig-addition-all-inputs'
            and receipt['module'] == 'TickPhaseComposition'
            and receipt['status'] == 'pass' and receipt['exit_code'] == 0
            and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
            and receipt['sources_stable'] and receipt['outcome'] is None
            and receipt['attempt_state'] == 'in_progress'
            and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
            and all(receipt[field] is True for field in (
                'completion_addition_laws_proved', 'phase_addition_law_proved',
                'all_completion_inputs', 'all_completion_scales_and_times',
                'uses_operational_sine_cosine_and_phase'))
            and all(receipt[field] is False for field in (
                'assumed_addition_law', 'arctangent_cayley_bridge_proved', 'pi_endpoints_proved',
                'standard_pi_identification_kernel_proved', 'derivative_proved',
                'unitary_half_turn_proved', 'full_claim_proved'))
            and {'rational-cosine-addition', 'rational-sine-addition',
                 'completion-cosine-addition', 'completion-sine-addition',
                 'operational-phase-addition'} <= set(receipt['theorems'])
            and receipt['remaining_obligations'] == remaining,
            'completion addition lacks fresh unconditional closure or overclaims its scope')
    require({'research/nima/agda/' + name + '.agda' for name in (
        'TickCompletionRingContinuity', 'TickCompletionLimits', 'TickRationalTrigAddition',
        'TickCompletionTrigAddition', 'TickPhaseComposition')}
        <= set(receipt['source_sha256']), 'unpinned completion addition modules')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale supporting component evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale supporting component kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)
    return remaining


def admit_operational_cayley_grid(root, node, component, pins, external_pins):
    """Admit the checked grid bridge, never a pi or full half-turn outcome."""
    domain = 'nonnegative rational grid inputs N/(d+1) bounded by one half'
    require(node['id'] == 'completion-pi-half-turn'
            and component['id'] == 'operational-cayley-grid'
            and component.get('scope') == domain, 'unknown or overscoped Cayley component')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['module'] == 'TickOperationalCayleyIdentity'
            and receipt['status'] == 'pass' and receipt['exit_code'] == 0
            and receipt['fresh_dependency_check'] and receipt['sources_stable']
            and {'--safe', '--cubical', '--guardedness', '--ignore-interfaces'} <= set(receipt['command'])
            and receipt['operational_cayley_bridge_domain'] == domain
            and all(receipt[field] is True for field in (
                'operational_cayley_bridge_proved', 'concrete_cayley_invariant_constancy_proved',
                'operational_cayley_local_defect_bound_proved', 'quadratic_telescoping_criterion_proved',
                'completion_product_magnitude_bound_proved'))
            and all(receipt[field] is False for field in (
                'machin_endpoints_proved', 'unitary_half_turn_proved',
                'all_completion_increments_derivative_proved')),
            'Cayley bridge lacks fresh scoped closure or overclaims endpoints')
    require({'research/nima/agda/' + name + '.agda' for name in (
        'TickOperationalCayleyIdentity', 'TickCayleyInvariantConstancy',
        'TickCayleyInvariantStep', 'TickCayleyDyadicMesh', 'TickCayleyDyadicTelescoping',
        'TickCayleyInvariantRepresentation', 'TickCompletionTelescoping')}
        <= set(receipt['source_sha256']), 'unpinned Cayley proof modules')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale supporting component evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale supporting component kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)


def admit_machin_endpoint_reduction(root, node, component, pins, external_pins):
    """The input identities and reduction close; the rational gate does not."""
    require(node['id'] == 'completion-pi-half-turn'
            and component['id'] == 'machin-endpoint-reduction', 'unknown endpoint reduction component')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['schema'] == 'marici.nima.machin-endpoint-reduction-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id'] and receipt['module'] == 'TickMachinEndpointReduction'
            and receipt['status'] == 'pass' and receipt['exit_code'] == 0
            and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed'] and receipt['sources_stable']
            and receipt['outcome'] is None and receipt['attempt_state'] == 'in_progress'
            and {'--safe', '--cubical', '--guardedness', '--ignore-interfaces'} <= set(receipt['command'])
            and receipt['machin_input_cayley_identities_proved'] and receipt['endpoint_reduction_proved']
            and all(receipt[field] is False for field in ('rational_machin_gate_proved', 'pi_endpoints_proved',
                'standard_pi_identification_kernel_proved', 'unitary_half_turn_proved', 'full_claim_proved'))
            and {'fifth-completion-agreement', 'completion239-agreement', 'machin-fifth-cayley',
                 'machin239-cayley', 'machin-endpoints-from-rational'} <= set(receipt['theorems'])
            and receipt['remaining_obligations'] == ['standard-pi identification at the accepted formal level', 'MachinEndpoints']
            and component.get('next_gate') == receipt['next_gate'],
            'endpoint reduction lacks fresh conditional closure or overclaims endpoints')
    require({'research/nima/agda/TickMachinEndpointReduction.agda',
             'research/nima/agda/TickMachinCayleyInputs.agda'} <= set(receipt['source_sha256']),
            'unpinned endpoint reduction modules')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale supporting component evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale supporting component kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)


def admit_machin_endpoints(root, node, component, pins, external_pins):
    """Exact candidate endpoints are not yet identification with standard pi."""
    require(node['id'] == 'completion-pi-half-turn' and component['id'] == 'machin-endpoints',
            'unknown Machin endpoints component')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['schema'] == 'marici.nima.machin-endpoints-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id'] and receipt['module'] == 'TickMachinEndpoints'
            and receipt['status'] == 'pass' and receipt['exit_code'] == 0
            and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed'] and receipt['sources_stable']
            and receipt['outcome'] is None and receipt['attempt_state'] == 'in_progress'
            and {'--safe', '--cubical', '--guardedness', '--ignore-interfaces'} <= set(receipt['command'])
            and all(receipt[field] is True for field in ('rational_machin_gate_proved',
                'machin_endpoints_proved', 'machin_phase_half_turn_proved'))
            and all(receipt[field] is False for field in ('standard_pi_identification_kernel_proved',
                'unitary_half_turn_proved', 'full_claim_proved'))
            and {'rational-machin-gate', 'machin-endpoints', 'machin-phase-half-turn'} <= set(receipt['theorems'])
            and receipt['remaining_obligations'] == ['standard-pi identification at the accepted formal level'],
            'Machin endpoints lack fresh closure or overclaim standard pi')
    require({'research/nima/agda/' + name + '.agda' for name in (
        'TickMachinEndpoints', 'TickMachinRationalGate', 'TickCayleyRationalNormalization',
        'TickMachinEndpointReduction')} <= set(receipt['source_sha256']), 'unpinned Machin endpoint modules')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale supporting component evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale supporting component kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)


def admit_machin_reference_series(root, node, component, pins, external_pins):
    """A reference-limit comparison is conditional until its pi input is built."""
    require(node['id'] == 'completion-pi-half-turn' and component['id'] == 'machin-reference-series',
            'unknown reference-series component')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['schema'] == 'marici.nima.machin-reference-series-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id'] and receipt['module'] == 'TickMachinReferenceSeries'
            and receipt['status'] == 'pass' and receipt['exit_code'] == 0
            and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed'] and receipt['sources_stable']
            and receipt['outcome'] is None and receipt['attempt_state'] == 'in_progress'
            and {'--safe', '--cubical', '--guardedness', '--ignore-interfaces'} <= set(receipt['command'])
            and all(receipt[field] is True for field in ('common_cutoff_tail_bound_proved',
                'machin_series_convergence_proved', 'conditional_reference_identification_proved'))
            and all(receipt[field] is False for field in ('reference_pi_instantiated',
                'standard_pi_identification_kernel_proved', 'unitary_half_turn_proved', 'full_claim_proved'))
            and {'machin-tail-bound', 'machin-series-converges', 'reference-series-identification'} <= set(receipt['theorems'])
            and receipt['remaining_obligations'] == ['standard-pi identification at the accepted formal level'],
            'reference series lacks fresh conditional closure or overclaims identification')
    require('research/nima/agda/TickMachinReferenceSeries.agda' in receipt['source_sha256'],
            'unpinned reference-series module')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale supporting component evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale supporting component kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)


def admit_written_pi_identification(root, node, component, pins, external_pins):
    """Record the semantic proof without silently accepting mixed-level closure."""
    require(node['id'] == 'completion-pi-half-turn' and component['id'] == 'standard-real-identification-written',
            'unknown written identification component')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['schema'] == 'marici.nima.standard-pi-identification-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id'] and receipt['status'] == 'pass'
            and receipt['sources_stable'] and receipt['outcome'] is None
            and receipt['written_standard_real_identification_proved'] is True
            and receipt['standard_pi_identification_kernel_proved'] is False
            and receipt['operational_endpoints_kernel_proved'] is True
            and receipt['reference_series_convergence_kernel_proved'] is True
            and receipt['mixed_level_acceptance_required'] is True
            and receipt['full_claim_promoted'] is False and receipt['unitary_half_turn_proved'] is False
            and receipt['imported_reference_outcome'] == '++'
            and receipt['exact_arithmetic_audit']['status'] == 'pass'
            and receipt['proof'] == 'research/nima/standard-pi-identification.md'
            and receipt['proof'] in receipt['source_sha256']
            and set(receipt['fresh_kernel_stages']) == {
                'research/nima/results/machin-endpoints-fresh.json',
                'research/nima/results/machin-reference-series-fresh.json'},
            'written identification is missing evidence or overclaims kernel verification')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale supporting component evidence: ' + source)
    for source, expected in receipt['external_dependency_sha256'].items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale supporting component kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(receipt['external_dependency_sha256'])


def admit_phase_derivative_reduction(root, node, component, pins, external_pins):
    require(node['id'] == 'completion-phase-metric-regularity'
            and component['id'] == 'phase-derivative-origin-reduction', 'wrong derivative reduction node')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['schema'] == 'marici.nima.phase-derivative-reduction-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id'] and receipt['status'] == 'pass'
            and receipt['exit_code'] == 0 and receipt['sources_stable']
            and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
            and receipt['origin_reduction_freshly_proved'] is True
            and receipt['all_completion_scales_times_and_increments'] is True
            and receipt['outcome'] is None and receipt['attempt_state'] == 'in_progress'
            and receipt['local_derivative_bound_proved'] is False
            and receipt['derivative_proved'] is False and receipt['full_metric_regularity_proved'] is False
            and receipt['unitary_half_turn_proved'] is False
            and receipt['module'] == 'TickPhaseDerivativeReduction'
            and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
            and {'phase-remainder-factor', 'complex-norm-product', 'phase-remainder-norm-local',
                 'local-bound-to-phase-derivative', 'phase-derivative-to-local-bound',
                 'origin-derivative-to-all-times'} <= set(receipt['theorems'])
            and 'research/nima/agda/TickPhaseDerivativeReduction.agda' in receipt['source_sha256'],
            'derivative reduction lacks fresh closure or overclaims the remaining analytic estimate')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale derivative reduction evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale derivative reduction kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)


def admit_completion_order_limits(root, node, component, pins, external_pins):
    require(node['id'] == 'completion-phase-metric-regularity'
            and component['id'] == 'completion-order-limit-transfer', 'wrong order transfer node')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['schema'] == 'marici.nima.completion-order-limits-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id'] and receipt['status'] == 'pass'
            and receipt['exit_code'] == 0 and receipt['sources_stable']
            and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
            and receipt['order_transfer_freshly_proved'] is True
            and receipt['moving_increment_factor_preserved'] is True
            and receipt['requires_nonzero_increment'] is False
            and receipt['outcome'] is None and receipt['attempt_state'] == 'in_progress'
            and receipt['rational_derivative_estimate_proved'] is False
            and receipt['local_derivative_bound_proved'] is False
            and receipt['derivative_proved'] is False and receipt['full_metric_regularity_proved'] is False
            and receipt['unitary_half_turn_proved'] is False
            and receipt['module'] == 'TickCompletionOrderLimits'
            and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
            and {'rational-limit-nonnegative', 'rational-limit-order',
                 'rational-moving-product-converges', 'rational-quadratic-bound-limit'} <= set(receipt['theorems'])
            and 'research/nima/agda/TickCompletionOrderLimits.agda' in receipt['source_sha256'],
            'order transfer lacks fresh closure or overclaims the analytic derivative estimate')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale order transfer evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale order transfer kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)


def admit_rational_phase_bound(root, node, component, pins, external_pins):
    require(node['id'] == 'completion-phase-metric-regularity'
            and component['id'] == 'rational-phase-relative-bound', 'wrong rational relative bound node')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['schema'] == 'marici.nima.rational-phase-derivative-bound-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id'] and receipt['status'] == 'pass'
            and receipt['exit_code'] == 0 and receipt['sources_stable']
            and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
            and receipt['rational_relative_bound_freshly_proved'] is True
            and receipt['independent_finite_cutoffs'] is True
            and receipt['rational_input_operational_limit_proved'] is True
            and receipt['explicit_radius_budget_required'] is True
            and receipt['all_completion_inputs_proved'] is False
            and receipt['outcome'] is None and receipt['attempt_state'] == 'in_progress'
            and receipt['local_derivative_bound_proved'] is False
            and receipt['derivative_proved'] is False and receipt['full_metric_regularity_proved'] is False
            and receipt['unitary_half_turn_proved'] is False
            and receipt['module'] == 'TickRationalPhaseDerivativeBound'
            and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
            and {'cosine-partial-quadratic', 'sine-partial-quadratic', 'scaled-relative-residual-bound',
                 'cosine-residual-converges', 'sine-residual-converges',
                 'rational-operational-relative-bound'} <= set(receipt['theorems'])
            and {'research/nima/agda/TickTrigRelativeRemainder.agda',
                 'research/nima/agda/TickRationalPhaseDerivativeBound.agda'} <= set(receipt['source_sha256']),
            'rational bound lacks fresh closure or overclaims completion-valued differentiation')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale rational bound evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale rational bound kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)


def admit_completion_relative_bound(root, node, component, pins, external_pins):
    require(node['id'] == 'completion-phase-metric-regularity'
            and component['id'] == 'bounded-completion-relative-bound', 'wrong completion relative bound node')
    path = component['receipt']
    receipt = load(root, path)
    require(receipt['schema'] == 'marici.nima.completion-relative-bound-result.v1'
            and receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
            and receipt['component'] == component['id'] and receipt['status'] == 'pass'
            and receipt['exit_code'] == 0 and receipt['sources_stable']
            and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
            and receipt['bounded_completion_relative_bound_freshly_proved'] is True
            and receipt['completion_valued_scales_and_increments'] is True
            and receipt['explicit_radius_budget_and_eventual_bounds_required'] is True
            and receipt['dyadic_modulus_constructed'] is False
            and receipt['outcome'] is None and receipt['attempt_state'] == 'in_progress'
            and receipt['local_derivative_bound_proved'] is False
            and receipt['derivative_proved'] is False and receipt['full_metric_regularity_proved'] is False
            and receipt['unitary_half_turn_proved'] is False
            and receipt['module'] == 'TickCompletionRelativeBound'
            and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
            and {'completion-limit-nonnegative', 'completion-limit-order', 'bounded-rational-order-density',
                 'bounded-completion-relative-bound'} <= set(receipt['theorems'])
            and {'research/nima/agda/TickCompletionClosedOrder.agda',
                 'research/nima/agda/TickCompletionRelativeBound.agda'} <= set(receipt['source_sha256']),
            'completion bound lacks fresh closure or overclaims derivative modulus')
    for source, expected in receipt['source_sha256'].items():
        require(file_hash(root, source) == expected, 'stale completion bound evidence: ' + source)
    external = dict(receipt['external_dependency_sha256'])
    external[receipt['command'][0]] = receipt['compiler_sha256']
    for source, expected in external.items():
        require(hashlib.sha256(Path(source).read_bytes()).hexdigest() == expected,
                'stale completion bound kernel/library evidence: ' + source)
    pins.update(receipt['source_sha256'])
    pins[path] = file_hash(root, path)
    external_pins.update(external)


def validate(root, net):
    require(net['schema'] == 'marici.nima.completion-refinement-conjecture-net.v1', 'wrong successor schema')
    require(net['outcome_semantics'] == SEMANTICS, 'wrong successor outcome semantics')
    imports = net['imports']
    nodes = net['conjectures']
    ids = [n['id'] for n in imports + nodes]
    require(len(ids) == len(set(ids)), 'duplicate node IDs')
    require(net['objective']['target'] in {n['id'] for n in nodes}, 'target must be a local goal')
    # Admit only the specifically validated proof/attempt certificates.
    pins = {}
    external_pins = {}
    admitted_proofs = []
    in_progress = {}
    paused = {}
    for node in nodes:
        completed_pi = node['id'] == 'completion-pi-half-turn' and node['outcome'] == '++'
        completed_regularity = node['id'] == 'completion-phase-metric-regularity' and node['outcome'] == '++'
        progress = node.get('progress') or node.get('completed_progress')
        if progress:
            require(node['id'] in ('completion-phase-metric-regularity', 'completion-pi-half-turn')
                    and (node['outcome'] is None or ((completed_pi or completed_regularity) and not node.get('progress')))
                    and progress['attempt_state'] in ('in_progress', 'paused')
                    and progress['active_action'] == 'prove/' + node['id'],
                    'invalid in-progress component declaration')
            if progress['attempt_state'] == 'paused':
                require(bool(progress.get('pause_reason')), 'paused attempt needs an explicit reason')
            receipt_path = progress['component_receipt']
            receipt = load(root, receipt_path)
            require(receipt['claim'] == node['id'] and receipt['scope_id'] == node['scope_id']
                    and receipt['status'] == 'pass' and receipt['exit_code'] == 0
                    and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
                    and receipt['sources_stable']
                    and receipt['outcome'] is None and receipt['attempt_state'] == 'in_progress'
                    and receipt['unitary_half_turn_proved'] is False
                    and {'--safe', '--ignore-interfaces'} <= set(receipt['command']),
                    'checkpoint lacks fresh component closure or overclaims its goal')
            if node['id'] == 'completion-phase-metric-regularity':
                require(progress['completed_component'] == 'metric-continuity'
                        and progress['remaining_obligations'] == ['PhaseDerivativeLaw']
                        and receipt['schema'] == 'marici.nima.phase-metric-continuity-result.v1'
                        and receipt['metric_continuity_freshly_proved']
                        and receipt['derivative_definition_checked'] and receipt['all_completion_scales_and_times']
                        and receipt['derivative_proved'] is False and receipt['full_metric_regularity_proved'] is False
                        and receipt['module'] == 'TickPhaseMetricRegularity'
                        and {'within-representatives', 'within-separated', 'nearby-exponent-bound',
                             'operational-phase-metric-continuous'} <= set(receipt['theorems']),
                        'continuity checkpoint lacks fresh component closure or overclaims regularity')
            else:
                require(progress['completed_component'] == 'convergent-Machin-candidate'
                        and receipt['schema'] == 'marici.nima.machin-pi-candidate-result.v1'
                        and receipt['convergent_machin_candidate_freshly_constructed']
                        and receipt['assumed_arctangent_or_pi_constant'] is False
                        and receipt['pi_endpoints_proved'] is False and receipt['full_claim_proved'] is False
                        and receipt['standard_pi_identification_kernel_proved'] is False
                        and receipt['module'] == 'TickMachinPiEndpointContract'
                        and receipt['exact_arithmetic_audit']['status'] == 'pass'
                        and {'atan-later-error', 'machin-pi-formula', 'Certificate.sibling-rotation',
                             'machin-endpoints-to-phase'} <= set(receipt['theorems']),
                        'Machin checkpoint lacks fresh component closure or overclaims pi endpoints')
            require(node['definition_module'] in receipt['source_sha256'], 'unpinned component definition')
            for path, expected in receipt['source_sha256'].items():
                require(file_hash(root, path) == expected, 'stale component evidence: ' + path)
            external = dict(receipt['external_dependency_sha256'])
            external[receipt['command'][0]] = receipt['compiler_sha256']
            for path, expected in external.items():
                require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected,
                        'stale component kernel/library evidence: ' + path)
            pins.update(receipt['source_sha256'])
            pins[receipt_path] = file_hash(root, receipt_path)
            external_pins.update(external)
            supporting = progress.get('supporting_components', [])
            require(len({c['id'] for c in supporting}) == len(supporting), 'duplicate supporting component')
            expected_remaining = receipt.get('remaining_obligations')
            for component in supporting:
                if component['id'] == 'bounded-completion-relative-bound':
                    admit_completion_relative_bound(root, node, component, pins, external_pins)
                elif component['id'] == 'rational-phase-relative-bound':
                    admit_rational_phase_bound(root, node, component, pins, external_pins)
                elif component['id'] == 'completion-order-limit-transfer':
                    admit_completion_order_limits(root, node, component, pins, external_pins)
                elif component['id'] == 'phase-derivative-origin-reduction':
                    admit_phase_derivative_reduction(root, node, component, pins, external_pins)
                elif component['id'] == 'standard-real-identification-written':
                    admit_written_pi_identification(root, node, component, pins, external_pins)
                elif component['id'] == 'machin-reference-series':
                    admit_machin_reference_series(root, node, component, pins, external_pins)
                elif component['id'] == 'machin-endpoints':
                    admit_machin_endpoints(root, node, component, pins, external_pins)
                elif component['id'] == 'machin-endpoint-reduction':
                    admit_machin_endpoint_reduction(root, node, component, pins, external_pins)
                elif component['id'] == 'operational-cayley-grid':
                    admit_operational_cayley_grid(root, node, component, pins, external_pins)
                elif component['id'] == 'completion-trig-addition':
                    expected_remaining = admit_completion_trig_addition(root, node, component, pins, external_pins)
                else:
                    admit_addition_foundations(root, node, component, pins, external_pins)
            if node['id'] == 'completion-pi-half-turn':
                if any(c['id'] == 'machin-endpoint-reduction' for c in supporting):
                    require(any(c['id'] == 'operational-cayley-grid' for c in supporting),
                            'pi remaining obligations require admitted Cayley bridge before endpoint reduction')
                if any(c['id'] == 'operational-cayley-grid' for c in supporting):
                    require(any(c['id'] == 'completion-trig-addition' for c in supporting),
                            'pi remaining obligations require admitted completion addition before Cayley')
                    expected_remaining = [obligation for obligation in expected_remaining
                                          if obligation != 'operational arctangent/Cayley bridge']
                if any(c['id'] == 'machin-endpoints' for c in supporting):
                    require(any(c['id'] == 'machin-endpoint-reduction' for c in supporting),
                            'pi remaining obligations require admitted endpoint reduction')
                    expected_remaining = [obligation for obligation in expected_remaining if obligation != 'MachinEndpoints']
                require(progress['remaining_obligations'] == expected_remaining,
                        'pi remaining obligations do not match the latest admitted component')
            if not (completed_pi or completed_regularity):
                (in_progress if progress['attempt_state'] == 'in_progress' else paused)[node['id']] = progress
        if node['outcome'] is None:
            continue
        norm_proof = node['id'] == 'completion-phase-unit-norm' and node['outcome'] == '++'
        incomplete = node['id'] == 'operational-unitary-half-turn' and node['outcome'] == '+-'
        flow_proof = node['id'] == 'completion-unit-circle-flow' and node['outcome'] == '++'
        half_turn_proof = node['id'] == 'operational-unitary-half-turn' and node['outcome'] == '++'
        whole_return_proof = node['id'] == net['objective']['target'] and node['outcome'] == '++'
        require(norm_proof or completed_pi or completed_regularity or flow_proof or half_turn_proof or whole_return_proof or incomplete, 'new resolutions require explicit proof-receipt admission')
        attempt = node['attempts'][-1]
        receipt = load(root, attempt['receipt'])
        require(attempt['intent'] == 'prove' and attempt['outcome'] == receipt.get('outcome') == node['outcome']
                and receipt.get('claim') == node['id'] and receipt.get('scope_id') == node['scope_id'],
                'proof/attempt claim mismatch')
        if completed_pi:
            acceptance_path = receipt['acceptance']
            acceptance = load(root, acceptance_path)
            require(receipt['schema'] == 'marici.nima.pi-mixed-level-accepted-result.v1'
                    and receipt['status'] == 'pass' and receipt['mixed_level_accepted'] is True
                    and receipt['operational_endpoints_kernel_proved'] is True
                    and receipt['standard_pi_identification_written_proved'] is True
                    and receipt['standard_pi_identification_kernel_proved'] is False
                    and receipt['full_claim_proved_at_accepted_level'] is True
                    and receipt['unitary_half_turn_proved'] is False
                    and receipt['remaining_pi_obligations_at_accepted_level'] == []
                    and acceptance['schema'] == 'marici.nima.pi-mixed-level-acceptance.v1'
                    and acceptance['claim'] == node['id'] and acceptance['scope_id'] == node['scope_id']
                    and acceptance['accepted'] is True
                    and acceptance['operator_instruction'] == 'accept mixed-level certificate'
                    and acceptance['accepted_verification']['standard_pi_identification_kernel_proved'] is False
                    and acceptance['evidence'] == receipt['evidence']
                    and acceptance_path in receipt['source_sha256']
                    and receipt['evidence'] in receipt['source_sha256'],
                    'pi closure requires explicit scoped mixed-level acceptance, not kernel overclaim')
            admit_written_pi_identification(root, node,
                {'id': 'standard-real-identification-written', 'receipt': receipt['evidence']}, pins, external_pins)
            admit_machin_endpoints(root, node,
                {'id': 'machin-endpoints', 'receipt': 'research/nima/results/machin-endpoints-fresh.json'}, pins, external_pins)
            for path, expected in receipt['external_dependency_sha256'].items():
                require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected, 'stale kernel/library evidence: ' + path)
            external_pins.update(receipt['external_dependency_sha256'])
            admitted_proofs.append(node['id'])
        elif completed_regularity:
            require(receipt['schema'] == 'marici.nima.constructed-phase-derivative-result.v1'
                    and receipt['status'] == 'pass' and receipt['exit_code'] == 0
                    and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
                    and receipt['sources_stable'] and receipt['dyadic_modulus_constructed'] is True
                    and receipt['local_derivative_bound_proved'] is True
                    and receipt['derivative_proved'] is True and receipt['full_metric_regularity_proved'] is True
                    and receipt['all_completion_scales_times_and_increments'] is True
                    and receipt['unitary_half_turn_proved'] is False
                    and receipt['remaining_regularity_obligations'] == []
                    and receipt['module'] == 'TickConstructedPhaseDerivative'
                    and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
                    and {'modulus-small-angle', 'modulus-quadratic-budget', 'ball-eventual-magnitude',
                         'local-residual-identification', 'constructed-local-phase-derivative-bound',
                         'operational-phase-derivative', 'operational-phase-metric-regularity'} <= set(receipt['theorems'])
                    and node['proof_module'] in receipt['source_sha256']
                    and node['definition_module'] in receipt['source_sha256'],
                    'regularity proof lacks fresh all-input derivative closure')
            external = dict(receipt['external_dependency_sha256'])
            external[receipt['command'][0]] = receipt['compiler_sha256']
            for path, expected in external.items():
                require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected,
                        'stale regularity kernel/library evidence: ' + path)
            external_pins.update(external)
            admitted_proofs.append(node['id'])
        elif flow_proof:
            require(receipt['schema'] == 'marici.nima.constructed-unit-circle-flow-result.v1'
                    and receipt['status'] == 'pass' and receipt['exit_code'] == 0
                    and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
                    and receipt['sources_stable'] and receipt['unit_circle_flow_proved'] is True
                    and receipt['same_operational_phase'] is True
                    and receipt['all_completion_scales_times_and_increments'] is True
                    and receipt['norm_continuity_and_derivative_proved'] is True
                    and receipt['unitary_half_turn_proved'] is False
                    and receipt['module'] == 'TickConstructedUnitCircleFlow'
                    and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
                    and {'unit-norm-law-definition', 'regularity-law-definition',
                         'OperationalUnitCircleFlow', 'operational-unit-circle-flow'} <= set(receipt['theorems'])
                    and node['proof_module'] in receipt['source_sha256'],
                    'flow proof lacks fresh same-phase closure')
            external = dict(receipt['external_dependency_sha256'])
            external[receipt['command'][0]] = receipt['compiler_sha256']
            for path, expected in external.items():
                require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected,
                        'stale flow kernel/library evidence: ' + path)
            external_pins.update(external)
            admitted_proofs.append(node['id'])
        elif half_turn_proof:
            pi_path = 'research/nima/results/pi-mixed-level-accepted.json'
            require(receipt['schema'] == 'marici.nima.constructed-unitary-half-turn-result.v1'
                    and receipt['status'] == 'pass' and receipt['exit_code'] == 0
                    and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
                    and receipt['sources_stable'] and receipt['operational_half_turn_kernel_proved'] is True
                    and receipt['unitary_half_turn_proved_at_accepted_level'] is True
                    and receipt['same_operational_phase_and_machin_candidate'] is True
                    and receipt['standard_pi_identification_kernel_proved'] is False
                    and receipt['mixed_level_accepted'] is True and receipt['whole_return_proved'] is False
                    and receipt['pi_identification_receipt'] == pi_path
                    and pi_path in receipt['source_sha256']
                    and {'completion-pi-half-turn', 'completion-unit-circle-flow'} <= set(admitted_proofs)
                    and receipt['module'] == 'TickConstructedUnitaryHalfTurn'
                    and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
                    and {'machin-start-law-definition', 'machin-finish-law-definition',
                         'OperationalMachinHalfTurn', 'operational-machin-half-turn'} <= set(receipt['theorems'])
                    and node['proof_module'] in receipt['source_sha256'],
                    'half-turn lacks fresh same-phase closure or overclaims identification/whole-return')
            external = dict(receipt['external_dependency_sha256'])
            external[receipt['command'][0]] = receipt['compiler_sha256']
            for path, expected in external.items():
                require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected,
                        'stale half-turn kernel/library evidence: ' + path)
            external_pins.update(external)
            admitted_proofs.append(node['id'])
        elif whole_return_proof:
            acceptance_path = 'research/nima/contracts/whole-return-mixed-level-acceptance.v1.json'
            evidence_path = 'research/nima/results/standard-spectral-correspondence.json'
            kernel_path = 'research/nima/results/operational-whole-return-kernel-fresh.json'
            acceptance = load(root, acceptance_path)
            evidence = load(root, evidence_path)
            kernel = load(root, kernel_path)
            require(receipt['schema'] == 'marici.nima.whole-return-mixed-level-accepted-result.v1'
                    and receipt['status'] == 'pass' and receipt['acceptance'] == acceptance_path
                    and receipt['evidence'] == evidence_path and receipt['kernel_receipt'] == kernel_path
                    and receipt['operational_kernel_bundle_proved'] is True
                    and receipt['standard_real_correspondence_written_proved'] is True
                    and receipt['semantic_correspondence_kernel_proved'] is False
                    and receipt['mixed_level_accepted'] is True and receipt['full_claim_proved_at_accepted_level'] is True
                    and receipt['C1_at_seam_claimed'] is False and receipt['remaining_obligations_at_accepted_level'] == []
                    and acceptance['schema'] == 'marici.nima.whole-return-mixed-level-acceptance.v1'
                    and acceptance['accepted'] is True and acceptance['operator_instruction'] == 'yes'
                    and acceptance['claim'] == node['id'] and acceptance['scope_id'] == node['scope_id']
                    and acceptance['evidence'] == evidence_path
                    and acceptance['accepted_verification'] == {
                        'operational_kernel_bundle_proved': True, 'standard_real_correspondence_written_proved': True,
                        'semantic_correspondence_kernel_proved': False, 'C1_at_seam_claimed': False}
                    and set(node['depends_on']) <= set(admitted_proofs) | {item['id'] for item in imports}
                    and {acceptance_path, evidence_path, kernel_path, node['proof_module']} <= set(receipt['source_sha256']),
                    'whole-return requires explicit scoped mixed acceptance without kernel/seam overclaim for proof-receipt admission')
            require(evidence['schema'] == 'marici.nima.standard-spectral-correspondence-result.v1'
                    and evidence['status'] == 'pass' and evidence['fresh_closure_completed'] and evidence['sources_stable']
                    and evidence['written_semantic_correspondence_supplied'] is True
                    and evidence['operational_kernel_bundle_proved'] is True
                    and evidence['semantic_correspondence_kernel_proved'] is False
                    and evidence['additional_mixed_level_accepted'] is False and evidence['target_outcome'] is None
                    and kernel['schema'] == 'marici.nima.operational-whole-return-kernel-result.v1'
                    and kernel['status'] == 'pass' and kernel['exit_code'] == 0
                    and kernel['fresh_dependency_check'] and kernel['fresh_closure_completed'] and kernel['sources_stable']
                    and kernel['operational_kernel_bundle_proved'] is True and kernel['whole_return_proved'] is False
                    and kernel['standard_real_phase_interpretation_proved'] is False
                    and kernel['module'] == 'TickOperationalWholeReturnKernel'
                    and {'--safe', '--ignore-interfaces'} <= set(kernel['command'])
                    and {'LocalLaws', 'ReturnLaws', 'GeneratorLaws', 'CoherenceLaws', 'FactorLaws',
                         'CovarianceLaws', 'StructuralLaws', 'OperationalWholeReturnKernel',
                         'operational-whole-return-kernel'} <= set(kernel['theorems']),
                    'whole-return lacks fresh operational bundle and written semantic evidence')
            for supporting in (evidence, kernel):
                require(all(receipt['source_sha256'].get(p) == h for p, h in supporting['source_sha256'].items()),
                        'whole-return omits dependency pins')
                require(all(receipt['external_dependency_sha256'].get(p) == h for p, h in supporting['external_dependency_sha256'].items()),
                        'whole-return omits external pins')
                require(receipt['external_dependency_sha256'].get(kernel['command'][0]) == supporting['compiler_sha256'],
                        'whole-return compiler pin missing')
            for path, expected in receipt['external_dependency_sha256'].items():
                require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected,
                        'stale whole-return kernel/library evidence: ' + path)
            external_pins.update(receipt['external_dependency_sha256'])
            admitted_proofs.append(node['id'])
        elif norm_proof:
            require(receipt['schema'] == 'marici.nima.constructed-scheduled-norm-result.v1'
                    and receipt['status'] == 'pass' and receipt['exit_code'] == 0
                    and receipt['fresh_dependency_check'] and receipt['fresh_closure_completed']
                    and receipt['sources_stable'] and receipt['completion_unit_norm_freshly_proved']
                    and receipt['norm_bound_is_assumed_input'] is False
                    and receipt['uniform_on_bounded_moving_inputs']
                    and receipt['unitary_half_turn_proved'] is False
                    and receipt['module'] == 'TickConstructedScheduledNorm'
                    and {'--safe', '--ignore-interfaces'} <= set(receipt['command'])
                    and {'constructed-scheduled-norm-bound', 'operational-phase-unit-norm'} <= set(receipt['theorems']),
                    'norm proof lacks fresh unconditional closure')
            require(node['proof_module'] in receipt['source_sha256'], 'unpinned norm theorem module')
            external = dict(receipt['external_dependency_sha256'])
            external[receipt['command'][0]] = receipt['compiler_sha256']
            for path, expected in external.items():
                require(hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected, 'stale kernel/library evidence: ' + path)
            external_pins.update(external)
            admitted_proofs.append(node['id'])
        else:
            require(receipt['intent'] == 'prove' and receipt['status'] == 'incomplete_proof_attempt'
                    and receipt['full_claim_proved'] is False and receipt['full_claim_refuted'] is False,
                    'invalid incomplete-attempt receipt')
        for path, expected in receipt['source_sha256'].items():
            require(file_hash(root, path) == expected, 'stale proof/attempt evidence: ' + path)
        pins.update(receipt['source_sha256'])
        pins[attempt['receipt']] = file_hash(root, attempt['receipt'])
    resolved = {}
    for item in imports:
        path = item['outcome_pointer']
        pointer = load(root, path)
        resolved[item['id']] = resolve(root, pointer)
        export = load(root, pointer['export']['path'])
        pins.update(export['artifact_sha256'])
        for artifact in (path, pointer['export']['path'], pointer['head']):
            pins[artifact] = file_hash(root, artifact)
    pending = {n['id']: set(n['depends_on']) for n in nodes}
    require(all(d <= set(ids) for d in pending.values()), 'unknown dependency')
    visited = set(resolved)
    while pending:
        ready = {name for name, deps in pending.items() if deps <= visited}
        require(bool(ready), 'cyclic proof-route dependencies')
        visited.update(ready)
        pending = {name: deps for name, deps in pending.items() if name not in ready}
    facts = {name for name, r in resolved.items() if r['proposition_truth'] is True}
    facts.update(admitted_proofs)
    unresolved = [n for n in nodes if n['outcome'] in (None, '+-', '--')]
    frontier = [n['id'] for n in unresolved if set(n['depends_on']) <= facts]
    blocked = {n['id']: [d for d in n['depends_on'] if d not in facts] for n in unresolved if n['id'] not in frontier}
    require(net['planner']['recommended_action'] is None, 'recommendation must come from the computed planning receipt')
    require(net['planner']['status'] == 'subjective_uncalibrated_planning_only'
            and net['planner']['parameters_estimated'] and net['planner']['empirically_calibrated'] is False,
            'planning parameters must be explicitly subjective')
    return {
        'schema': 'marici.nima.completion-refinement-net-result.v1',
        'status': 'pass', 'validation_only': True, 'net_id': net['id'],
        'net_state': 'positive_terminal' if net['objective']['target'] in facts else 'active_nonterminal',
        'target': net['objective']['target'],
        'target_outcome': '++' if net['objective']['target'] in facts else None,
        'terminal': net['objective']['target'] in facts,
        'imports': resolved, 'local_outcomes': {n['id']: n['outcome'] for n in nodes},
        'ready_proof_frontier': frontier, 'blocked_on': blocked,
        'locally_proved_claims': admitted_proofs, 'in_progress': in_progress, 'paused': paused,
        'local_verification_levels': {n['id']: n['verification_level'] for n in nodes if n.get('verification_level')},
        'outcome_counts': {'++': len(facts), '+-': sum(n['outcome'] == '+-' for n in nodes),
                           'in_progress': len(in_progress), 'paused': len(paused),
                           'unattempted': sum(n['outcome'] is None and not n.get('progress') for n in nodes)},
        'recommended_action': None, 'ranking_status': 'structural_validation_planning_receipt_not_loaded',
        'imported_proof_does_not_close_target': True,
        'boundary': 'Validates live theorem-specific receipts and references. Accepted written semantic correspondence is not relabeled kernel-proved.',
        'source_sha256': pins, 'external_dependency_sha256': external_pins,
    }

def main():
    try:
        net = load(REPO, CONTRACT)
        result = validate(REPO, net)
        planning = load(REPO, net['planner']['result'])
        require(planning['status'] == 'pass' and planning['planning_only']
                and planning['scientific_outcomes_changed'] is False
                and planning['estimate_status'] == 'subjective_uncalibrated_planning_only'
                and planning['objective']['target'] == result['target'], 'invalid planning receipt')
        for path, expected in planning['source_sha256'].items():
            require(file_hash(REPO, path) == expected, 'stale planning evidence: ' + path)
        require(planning['external_dependency_sha256'] == result['external_dependency_sha256'], 'planning proof context changed')
        result['source_sha256'].update(planning['source_sha256'])
        result['source_sha256'][net['planner']['result']] = file_hash(REPO, net['planner']['result'])
        result['recommended_action'] = planning['continuation_action'] or planning['central']['first_action']
        result['ranking_status'] = ('in_progress_preserve_attempt_budget' if result['in_progress']
                                    else 'paused_checkpoint_resume' if planning['continuation_action'] and planning['continuation_action'].startswith('resume/')
                                    else 'subjective_model_ranked_not_calibrated')
        result['planner'] = {'estimate_status': planning['estimate_status'], 'objective': planning['objective'],
                             'central': planning['central'], 'result': net['planner']['result'],
                             'sensitivity_first_actions': planning['sensitivity']['first_action_counts'],
                             'recommendation_stable': planning['sensitivity']['recommendation_stable'],
                             'forecast_scope': planning['forecast_scope'],
                             'continuation_action': planning['continuation_action']}
        for path in (CONTRACT, 'research/nima/checkers/check_completion_refinement_net.py',
                     'research/conjecture_net/outcome_reference.py'):
            result['source_sha256'][path] = file_hash(REPO, path)
    except (OutcomeReferenceError, OSError, KeyError, TypeError, ValueError) as error:
        # Do not leave a previous successful consumer receipt looking current.
        result = {'schema': 'marici.nima.completion-refinement-net-result.v1',
                  'status': 'blocked', 'net_state': 'invalid_reference_or_contract',
                  'target_outcome': None, 'terminal': False, 'scientific_outcome_recorded': False,
                  'error': str(error)}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('source_sha256', 'external_dependency_sha256')}, indent=2))
    raise SystemExit(0 if result['status'] == 'pass' else 1)

if __name__ == '__main__':
    main()
