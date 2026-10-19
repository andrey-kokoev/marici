"""Create source-pinned scattering contract and candidate programme attachment.

Does not execute solvers, reinterpret historical receipts, or refresh snapshots.
"""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[2]
HOME = ROOT / 'research/scattering/high-energy'
REPLAY_MEMBERS = ['compare_response_spaces.py', 'baseline64/packet_kernels.npz',
                  'results/response128/packet_kernels.npz', 'packet_comparison.json']


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def create(path, value):
    content = json.dumps(value, indent=2, sort_keys=True) + '\n'
    if path.exists():
        if path.read_text(encoding='utf-8') != content:
            raise ValueError('Refusing implicit replacement: ' + str(path))
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')


def main():
    sources = sorted([p for p in HOME.iterdir() if p.suffix in {'.md', '.py', '.json', '.zip'}
                      and p.name != 'high_energy_scattering_net.py' and p.name != 'CONJECTURE-NET.md'])
    evidence = {'schema': 'marici.scattering.high-energy-source-pins.v1',
                'sources': {p.relative_to(ROOT).as_posix(): {'sha256': digest(p), 'bytes': p.stat().st_size,
                            'kind': 'source_archive' if p.suffix == '.zip' else 'historical_source'} for p in sources},
                'archive_members': {}, 'boundary': 'Integrity pins, not acceptance of historical numerical claims. Binary archives remain at original paths; collector does not copy them.'}
    archive = HOME / 'pentachoron_full_response128_packet_bundle.zip'
    with ZipFile(archive) as z:
        evidence['archive_members'][archive.relative_to(ROOT).as_posix()] = {
            name: {'sha256': hashlib.sha256(z.read(name)).hexdigest(), 'bytes': z.getinfo(name).file_size}
            for name in REPLAY_MEMBERS}
    create(HOME / 'contracts/high-energy-source-pins.v1.json', evidence)
    claims = []

    def claim(name, statement, dependencies, notes, acceptance, status='open'):
        claims.append({'id': name, 'statement': statement, 'scope_id': name + '.source-model.v1',
                       'depends_on': dependencies, 'requires': ['pinned-source-artifacts'],
                       'outcome': None, 'status': status, 'acceptance': acceptance,
                       'evidence': ['research/scattering/high-energy/' + note for note in notes],
                       'evidence_status': 'historical_report_not_admitted_proof'})

    claim('native-endpoint-realization', 'Retained native records, endpoint geometry and cycle operators implement the stated model at their declared poses.', [],
          ['pentachoron_quantum_hinge_note.md', 'pentachoron_geometric_split_note.md'],
          'Reconstruct source endpoint operators and retained cycle records; do not identify sectors by dimension alone.')
    claim('conditional-full-spinor-switch', 'The explicitly extended full-spinor rule sews the additional face switches without discarding complementary selected-line amplitudes.',
          ['native-endpoint-realization'], ['pentachoron_open_product_flux_note.md'],
          'Replay projector/involution identities and preserve7/9,7/9,1/9 selected-line obstructions; the extension remains an assumption.')
    claim('autonomous-conservative-model', 'The declared contacts, kinetic terms and native records define the lower-bounded conservative model with common model energy.',
          ['conditional-full-spinor-switch'], ['pentachoron_open_product_flux_note.md', 'pentachoron_relativistic_kinetics_note.md'],
          'Validate complete diagonal/off-diagonal forms, domains, flux balance and the specified kinetic convention separately.')
    claim('asymptotic-record-flux', 'The conditional open model carries coherent asymptotic flux into its2+8 product-record leads.',
          ['autonomous-conservative-model'], ['joint_pose_scattering_note.md', 'pentachoron_open_product_flux_note.md'],
          'Rebuild outgoing kernels and finite-model scattering equations; record leads are not identified with independently occupied species.')
    claim('packet-current-readout', 'Coherent packet fields obey the declared strain continuity identity, with internal transport distinct from entry/release selection.',
          ['asymptotic-record-flux'], ['time_resolved_strain_note.md', 'strain_diagnostics_note.md'],
          'Reconstruct complex fields and continuity before probabilities; distinguish peak, whole-packet and finite-window diagnostics.')
    claim('energy-dependent-transport', 'The sampled source model has nonmonotone internal transport and cutoff-dependent reversal structure, rather than a universal monotone compression law.',
          ['packet-current-readout'], ['broad_energy_sweep_note.md', 'strain_sign_transition_note.md'],
          'Reproduce the matched-cutoff comparisons; finite roots and samples do not certify a continuum threshold.')
    claim('energy-quadrature-convergence', 'The128-direction packet readouts are stable under independently increased energy sampling with a stated error criterion.',
          ['packet-current-readout'], ['response128_packet_note.md'],
          'Hold source/grid/response hierarchy fixed and perform17-to33 sampling; the existing9-node14.244725% change is not a convergence certificate.')
    claim('omitted-response-control', 'A corrected-residual response hierarchy and omitted-tail estimate bound contributions outside the retained response space.',
          ['packet-current-readout'], ['omitted_mode_estimate_note.md', 'closed_mode_feedback_note.md', 'response128_packet_note.md'],
          'Rebuild from the corrected residual and justify a named norm/error bound;64-to128 agreement alone is insufficient.')
    claim('spatial-continuum-control', 'Spatial, angular and mode refinements converge in a declared topology with controlled readout error.',
          ['energy-quadrature-convergence', 'omitted-response-control'],
          ['matched_spatial_note.md', 'spatial_after_angular_note.md', 'strain_spatial_refinement_note.md'],
          'Separate each refinement axis and supply completion/cofinality and error controls; finite differences are not bounds.')
    claim('physical-calibration-and-species', 'An independently sourced dimensional calibration and state/record map identify the model preparation and leads with physical scattering species.', [],
          ['pentachoron_relativistic_kinetics_note.md', 'response128_packet_note.md'],
          'Provide dimensional scale, physical preparation/instrument and species maps; a2:8 record partition supplies none of them.', status='deferred_missing_source_map')
    claim('high-energy-scattering-target', 'The retained source model yields convergence-controlled scattering predictions in its declared regime, with physical interpretation only through the explicit calibration/species map.',
          ['energy-dependent-transport', 'spatial-continuum-control', 'physical-calibration-and-species'],
          ['response128_packet_note.md'], 'All dependency scopes and verification levels must be explicitly accepted; no root promotion from replay or registry admission.')
    contract = {
        'schema': 'marici.scattering.high-energy-conjecture-net.v1', 'id': 'scattering.high-energy.v1',
        'owner': 'marici.Nima', 'outcome_semantics': 'proof-attempt-outcomes-v1',
        'objective': {'target': 'high-energy-scattering-target', 'outcome': None,
                      'scope': 'Conditional pentachoron quantum-configuration model; physical calibration and continuum control unresolved.'},
        'operator_stimulus': {'wording': 'wire it up', 'target': 'research/scattering/high-energy', 'status': 'direct_instruction_not_scientific_evidence'},
        'coherence_obligation': 'forward_realization_of_source_pinned_dependency_graph',
        'source_pins': 'research/scattering/high-energy/contracts/high-energy-source-pins.v1.json',
        'adapter': 'research/scattering/high-energy/high_energy_scattering_net.py',
        'conjectures': claims, 'imports': [],
        'dependency_semantics': 'Obligation prerequisites, not identities or transported proof links between different source grids, kinetic conventions or preparations.',
        'interfaces': ['pinned-source-artifacts'],
        'actions': [{'id': 'replay-response128', 'kind': 'saved_complex_kernel_readout_replay',
                     'claim': 'packet-current-readout', 'archive': archive.relative_to(ROOT).as_posix(),
                     'entrypoint': REPLAY_MEMBERS[0], 'members': REPLAY_MEMBERS,
                     'arguments': ['--baseline', REPLAY_MEMBERS[1], '--new', REPLAY_MEMBERS[2], '--output', 'replayed_comparison.json'],
                     'dependencies': ['numpy', 'scipy'], 'fresh_stationary_solve': False,
                     'full_scattering_matrix_computed': False, 'promotes_claim_outcome': False}],
        'issue_boundary': {
            'problem': 'Scattering notes and bundles lack an executable dependency/evidence net.',
            'bold_conjecture': 'The retained model supports convergence-controlled coherent record scattering over its declared source regime.',
            'rivals': ['selected-line sewing without the extension', 'universal monotone energy-to-compression law',
                       'prepared-column orthogonality implies full-S unitarity', 'fixed-hierarchy agreement bounds the entire omitted space'],
            'risky_consequences': ['Independent energy and corrected-residual refinements preserve readouts within declared tolerances.'],
            'strongest_falsifier': 'Hold128 response directions fixed and increase energy sampling17-to33; independently rebuild the omitted response hierarchy from its corrected residual.',
            'disposition': 'Net wiring and a saved-kernel replay are executable; convergence and physical identification are not proved.'},
        'boundary': {'historical_receipts_auto_admitted': False, 'replay_is_fresh_scattering_solve': False,
                     'prepared_columns_are_full_S': False, 'continuum_certified': False,
                     'physical_calibration_supplied': False, 'programme_obligation_discharged': False}}
    create(HOME / 'contracts/high-energy-scattering-conjecture-net.v1.json', contract)
    previous_path = ROOT / 'research/conjecture_net/contracts/programme-hierarchy.v14.json'
    hierarchy = json.loads(previous_path.read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v15', id='marici.relational-carrier-physics-programme.v15',
                     phase='high_energy_scattering_net_source_wiring', predecessor=previous_path.relative_to(ROOT).as_posix())
    hierarchy['scattering_conjecture_nets'] = [{
        'id': contract['id'], 'contract': 'research/scattering/high-energy/contracts/high-energy-scattering-conjecture-net.v1.json',
        'source_pins': contract['source_pins'], 'adapter': contract['adapter'],
        'target_obligations': ['physical-sector-realizations', 'empirical-recovery'],
        'relation': 'candidate_scattering_testbed_not_proof_import',
        'proof_bearing': False, 'discharges_parent_obligation': False, 'outcome': None}]
    create(ROOT / 'research/conjecture_net/contracts/programme-hierarchy.v15.json', hierarchy)
    print(json.dumps({'status': 'wired', 'net': contract['id'], 'conjectures': len(claims),
                      'source_files_pinned': len(sources), 'programme': 'v15', 'root_outcome': None}))


if __name__ == '__main__':
    main()
