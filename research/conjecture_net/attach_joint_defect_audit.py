"""Attach a falsified sewing candidate and its surviving coefficient interfaces."""
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent


if __name__ == '__main__':
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v13.json').read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v14',
                     id='marici.relational-carrier-physics-programme.v14',
                     phase='joint_defect_interface_and_response_noncollapse',
                     predecessor='research/conjecture_net/contracts/programme-hierarchy.v13.json')
    hierarchy['joint_defect_interfaces'] = [{
        'id': 'joint-assembly-family-defect-audit-v1',
        'contract': 'research/conjecture_net/contracts/joint-defect-audit.v1.json',
        'implementation': 'research/conjecture_net/joint_defect_audit.py',
        'receipt': 'research/conjecture_net/results/joint-defect-audit.json',
        'source_stratum': 'rational comparison-chain coefficients on the137 bound source slot labels',
        'assembly_boundary_rank': 28, 'family_incidence_rank': 47,
        'joint_rank': 55, 'joint_kernel_dimension': 82, 'frozen_response_completion_rank': 56,
        'uniform_source_response_minimum_linear_rank': 137,
        'status': 'joint_structural_sewing_conjecture_falsified_by_unchanged_source',
        'surviving_scope': 'Joint boundary/incidence quotient only; a frozen response completion is not uniform over source legs.',
        'chain_map_constructed': False, 'physical_preparations_authorized': False,
        'intended_T9_selected': False, 'proof_bearing': False, 'discharges_parent_obligation': False,
        'admission_status': 'not_admitted_as_new_programme_proof_link'
    }]
    content = json.dumps(hierarchy, indent=2, sort_keys=True) + '\n'
    destination = HOME / 'contracts/programme-hierarchy.v14.json'
    if destination.exists() and destination.read_text() != content:
        raise ValueError('Refusing implicit joint-defect hierarchy correction')
    if not destination.exists():
        destination.write_text(content, encoding='utf-8')
    print('Recorded v14: structural coefficient quotient retained; full-response sewing candidate falsified.')
