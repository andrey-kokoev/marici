"""Record explanation status without rewriting the frozen source-model net."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HOME = Path(__file__).resolve().parent
NET = ROOT / 'research/scattering/high-energy/contracts/high-energy-scattering-conjecture-net.v1.json'
LEDGER_BINDING = HOME / 'contracts/ledger4320-reference-boundary-net.v1.json'
ASSESSMENT = HOME / 'contracts/high-energy-scattering-explanation-status.v1.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(status):
    require(status['assessment'] == 'physical_scattering_not_yet_explained' and status['root_outcome'] is None,
            'explanation/root status promoted')
    expected_sources = {NET.relative_to(ROOT).as_posix(), LEDGER_BINDING.relative_to(ROOT).as_posix(),
                        'research/scattering/high-energy/results/high-energy-net-replay.json'}
    require(set(status['source_sha256']) == expected_sources, 'explanation source pins incomplete')
    for name, expected in status['source_sha256'].items():
        path = (ROOT / name).resolve()
        require(path.is_relative_to(ROOT) and sha(path) == expected, 'stale explanation source: ' + name)
    net = json.loads(NET.read_text())
    require(status['source_net']['id'] == net['id'] and status['source_net']['contract'] == NET.relative_to(ROOT).as_posix(), 'wrong source net')
    require(net['objective']['outcome'] is None, 'source root no longer unresolved')
    ids = {c['id'] for c in net['conjectures']}
    expected_gaps = {
        'numerical-error-and-completion': {'energy-quadrature-convergence', 'omitted-response-control', 'spatial-continuum-control'},
        'physical-source-justification': {'conditional-full-spinor-switch', 'autonomous-conservative-model'},
        'physical-preparation-calibration-and-identification': {'physical-calibration-and-species', 'high-energy-scattering-target'}}
    gaps = status['remaining_gaps']
    require(len(gaps) == 3 and {gap['id'] for gap in gaps} == set(expected_gaps), 'explanation gap set changed')
    for gap in gaps:
        require(set(gap['related_conjectures']) == expected_gaps[gap['id']] and set(gap['related_conjectures']) <= ids
                and gap['status'] == 'unresolved', 'gap missing or silently closed')
    require(all(value is False for value in status['boundary'].values()), 'explanation evidence strength promotion')
    require(status['ledger4320']['software_transport_selected'] is True and
            status['ledger4320']['physical_reference_boundary_closed'] is False, 'software/physical boundary conflated')
    return True


def create(path, value):
    content = json.dumps(value, indent=2, sort_keys=True) + '\n'
    if path.exists():
        require(path.read_text() == content, 'refusing implicit assessment replacement')
    else:
        path.write_text(content, encoding='utf-8')


def main():
    replay = ROOT / 'research/scattering/high-energy/results/high-energy-net-replay.json'
    status = {
        'schema': 'marici.conjecture-net.scattering-explanation-assessment.v1',
        'id': 'scattering.high-energy.explanation-status.v1',
        'source_net': {'id': 'scattering.high-energy.v1', 'contract': NET.relative_to(ROOT).as_posix()},
        'assessment': 'physical_scattering_not_yet_explained', 'root_outcome': None,
        'supplied_scope': {
            'kind': 'conditional_model_behavior',
            'statement': 'The declared model supplies coherent flux into its record channels and packet readouts conditional on its switching/contact rules, preparation and numerical truncations.',
            'verification': 'Historical source calculations plus a fresh saved-kernel readout replay; not a new full scattering solve or empirical identification.'},
        'remaining_gaps': [
            {'id': 'numerical-error-and-completion', 'status': 'unresolved',
             'related_conjectures': ['energy-quadrature-convergence', 'omitted-response-control', 'spatial-continuum-control'],
             'missing': 'Independent energy sampling, corrected-residual omitted-mode bounds and spatial/continuum error control.',
             'acceptance': 'Perform17-to33 sampling at fixed128 response directions; separately bound omitted response and establish the declared spatial completion.'},
            {'id': 'physical-source-justification', 'status': 'unresolved',
             'related_conjectures': ['conditional-full-spinor-switch', 'autonomous-conservative-model'],
             'missing': 'Independent source justification for the added switching and contact rules; conditional algebraic consistency is insufficient.',
             'acceptance': 'Derive or independently substantiate the actual operators, coefficients and admitted physical operations without fitting them from desired scattering readouts.'},
            {'id': 'physical-preparation-calibration-and-identification', 'status': 'unresolved',
             'related_conjectures': ['physical-calibration-and-species', 'high-energy-scattering-target'],
             'missing': 'Physical preparation, dimensional scales, particle/record and detector maps.',
             'acceptance': 'Supply and validate preparation/instrument records, scale calibration and species/detector identifications on the model records.'}],
        'ledger4320': {'binding': LEDGER_BINDING.relative_to(ROOT).as_posix(),
                      'software_transport_selected': True, 'physical_reference_boundary_closed': False,
                      'scope': 'Exact-domain software transport does not discharge scattering source justification, convergence or physical calibration.'},
        'disposition': 'Explanation attempt organized and conditional readouts supplied; physical explanation remains unestablished, not refuted.',
        'coherence_obligation': 'attachment_of_existing_source_and_ledger_scopes',
        'source_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in (NET, LEDGER_BINDING, replay)},
        'boundary': {'conditional_readout_is_physical_explanation': False, 'wiring_is_proof': False,
                     'software_transport_is_physical_scattering': False, 'physical_scattering_refuted': False,
                     'programme_obligation_discharged': False, 'authority_only_waiting_leaf_created': False}}
    validate(status)
    create(ASSESSMENT, status)
    previous = HOME / 'contracts/programme-hierarchy.v16.json'
    hierarchy = json.loads(previous.read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v17',
                     id='marici.relational-carrier-physics-programme.v17',
                     phase='scattering_physical_explanation_status_recorded', predecessor=previous.relative_to(ROOT).as_posix())
    hierarchy['scattering_explanation_assessments'] = [{
        'source_net': 'scattering.high-energy.v1', 'assessment': ASSESSMENT.relative_to(ROOT).as_posix(),
        'status': status['assessment'], 'outcome': None, 'proof_bearing': False,
        'discharges_parent_obligation': False, 'remaining_gap_ids': [g['id'] for g in status['remaining_gaps']]}]
    create(HOME / 'contracts/programme-hierarchy.v17.json', hierarchy)
    from collect import registry
    inventory = json.loads((HOME / 'inventory.json').read_text())
    selected = {entry['source']: entry['reason'] for entry in inventory['files']}
    (HOME / 'registry.json').write_text(json.dumps(registry(selected), indent=2, sort_keys=True) + '\n', encoding='utf-8')
    result = {'schema': 'marici.conjecture-net.scattering-explanation-status-result.v1', 'status': 'pass',
              'validation_only': True, 'assessment': status['assessment'], 'root_outcome': None,
              'remaining_gap_count': 3, 'assessment_sha256': sha(ASSESSMENT), 'checker_sha256': sha(Path(__file__))}
    (HOME / 'results/scattering-explanation-status.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
