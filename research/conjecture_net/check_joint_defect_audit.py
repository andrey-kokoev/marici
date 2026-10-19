"""Joint source-bound interfaces, fixed-response hostile and uniform source test."""
import hashlib
import json
from pathlib import Path
from joint_defect_audit import ROOT, source_interfaces, rank, act, nullspace, response, source_probe, sparse

HOME = Path(__file__).resolve().parent
CONTRACT = HOME / 'contracts/joint-defect-audit.v1.json'
SOURCE_PATHS = [ROOT / name for name in (
    'research/nima/checkers/check_rung_transport_diagram.py',
    'research/nima/checkers/check_shared_leg_dg_realization.py',
    'research/nima/checkers/check_typed_assembly_boundary_adapter.py',
    'research/nima/checkers/check_comparison_slot_reference_assembly.py',
    'research/nima/checkers/check_family_incidence_structure.py',
    'research/nima/checkers/biclique_complex.py')]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_contract(contract):
    require(all(value is False for value in contract['boundary'].values()), 'joint interface boundary promotion')
    require(contract['predicted_exact_interfaces'] == {
        'assembly_boundary_rank': 28, 'family_incidence_rank': 47, 'joint_rank': 55,
        'assembly_kernel_dimension': 109, 'family_kernel_dimension': 90, 'joint_kernel_dimension': 82,
        'joint_plus_fixed_response_rank': 56, 'uniform_source_response_minimum_linear_rank': 137},
        'joint interface scope/prediction changed')


def audit():
    source = source_interfaces()
    b, d, f = source['assembly'], source['incidence'], source['fixed_response']
    joint = b + d
    completed = joint + f
    kb, kd, kj, kf = (nullspace(matrix) for matrix in (b, d, joint, completed))
    require((len(kb), len(kd), len(kj), len(kf)) == (109, 90, 82, 81), 'kernel comparison changed')
    for matrix, basis in ((b, kb), (d, kd), (joint, kj), (completed, kf)):
        require(all(not any(act(matrix, vector)) for vector in basis), 'nullspace vector does not annihilate source map')
        require(rank(basis) == len(basis), 'kernel basis not independent')
    require(len(kj) < min(len(kb), len(kd)), 'kernels unexpectedly nested')
    assembly_only = next(vector for vector in kb if any(act(d, vector)))
    family_only = next(vector for vector in kd if any(act(b, vector)))
    fixed_hostile = next(vector for vector in kj if any(act(f, vector)))
    boundary = source['boundary_source']
    rung = source['rung_source']
    assigned = rung['m']['values']
    rebuilt = boundary['residuals'](
        [assigned[f'ax{i}'] for i in range(11)], [assigned[f'ay{i}'] for i in range(11)],
        [assigned[f'sx{i}'] for i in range(4)], [assigned[f'sy{i}'] for i in range(4)], source['reference'])
    require(rebuilt == source['fixed_values'], 'actual fixed shared-leg response wiring changed')
    fixed_residual = response(fixed_hostile, rebuilt, boundary)
    require(fixed_residual != boundary['ZERO'] and not any(act(joint, fixed_hostile)), 'fixed-response sewing hostile failed')
    # Uniformly generate the whole source probe family from source slot labels.
    # No kernel, target scalar or response observation enters its constructor.
    kh = boundary['mul'](boundary['K'], boundary['H'])
    require(kh != boundary['ZERO'], 'mixed source response collapsed')
    tables = []
    for index, slot in enumerate(source['slots']):
        table = source_probe(source, slot)
        require(all(value == (kh if row == index else boundary['ZERO']) for row, value in enumerate(table)),
                'uniform two-leg probe does not isolate its original slot')
        tables.append(table)
    require(len(tables) == 137, 'uniform response probe family incomplete')
    variable_hostile = kf[0]
    selected = next(index for index, value in enumerate(variable_hostile) if value)
    variable_residual = response(variable_hostile, tables[selected], boundary)
    require(not any(act(completed, variable_hostile)) and variable_residual == boundary['scale'](variable_hostile[selected], kh)
            and variable_residual != boundary['ZERO'], 'fixed completion wrongly uniform under source variation')
    return {
        'bound_original_slot_labels': 137, 'assembly_cell_degree': 2, 'family_incidence_edge_degree': 1,
        'assembly_boundary_rank': 137 - len(kb), 'family_incidence_rank': 137 - len(kd),
        'joint_rank': 137 - len(kj), 'assembly_kernel_dimension': len(kb), 'family_kernel_dimension': len(kd),
        'joint_kernel_dimension': len(kj), 'assembly_kernel_visible_to_family_dimension': len(kb) - len(kj),
        'family_kernel_visible_to_assembly_dimension': len(kd) - len(kj),
        'joint_plus_fixed_response_rank': 137 - len(kf), 'fixed_completed_kernel_dimension': len(kf),
        'uniform_source_probe_count': 137, 'uniform_source_response_minimum_linear_rank': 137,
        'kernel_inclusion_hostiles': {'assembly_closed_but_family_visible': sparse(assembly_only),
                                     'family_invisible_but_assembly_nonclosed': sparse(family_only)},
        'fixed_source_sewing_hostile': {'coefficients': sparse(fixed_hostile),
            'response': [[str(value) for value in row] for row in fixed_residual]},
        'fixed_completion_nonuniform_hostile': {'coefficients': sparse(variable_hostile),
            'probe_slot': list(source['slots'][selected]),
            'mixed_response': [[str(value) for value in row] for row in variable_residual]},
        'joint_kernel_basis': [sparse(vector) for vector in kj],
        'governing_conjecture': 'falsified_on_the_unchanged_actual_shared_leg_assignment',
        'surviving_scope': 'The rank55 joint interface preserves additive assembly boundary and family incidence only; rank56 adds the frozen response, not uniform variable-source response.',
        'chain_map_constructed': False, 'physical_preparations_authorized': False, 'intended_T9_selected': False}


def main():
    validate_contract(json.loads(CONTRACT.read_text()))
    paths = SOURCE_PATHS + [CONTRACT, Path(__file__), HOME / 'joint_defect_audit.py',
                           HOME / 'marked137_endpoint_audit.py', HOME / 'source_overlap_screen.py',
                           HOME / 'exchange_source_bridge.py', HOME / 'pilot_carrier.py']
    pins = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    controls = audit()
    require(all(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected for path, expected in pins.items()),
            'joint-defect inputs changed during execution')
    receipt = {'schema': 'marici.conjecture-net.joint-defect-audit.v1', 'status': 'pass',
               'validation_only': True, 'outcome': None, 'root_outcome': None, 'source_sha256': pins,
               'controls': controls, 'governing_conjecture_falsified': True,
               'new_kernel_theorem_proved': False, 'physical_preparations_authorized': False,
               'programme_outcomes_promoted': False, 'shared_sources_and_results_regenerated': False}
    (HOME / 'results/joint-defect-audit.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'joint_rank': 55, 'joint_kernel': 82, 'fixed_response_completion_rank': 56,
                      'uniform_source_minimum_linear_rank': 137, 'joint_sewing_conjecture': 'falsified'}, indent=2))


if __name__ == '__main__':
    main()
