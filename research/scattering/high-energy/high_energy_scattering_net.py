"""Source-pinned scattering net adapter; optional saved-kernel replay, not a solver."""
from __future__ import annotations
import argparse
from contextlib import redirect_stdout
import hashlib
import io
import json
from math import isclose
from pathlib import Path, PurePosixPath
import runpy
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[3]
HOME = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'research/conjecture_net'))
from graph_metrics import MetricAction, MetricGraph

CONTRACT = HOME / 'contracts/high-energy-scattering-conjecture-net.v1.json'
PINS = HOME / 'contracts/high-energy-source-pins.v1.json'
ARCHIVE = 'research/scattering/high-energy/pentachoron_full_response128_packet_bundle.zip'
MEMBERS = ['compare_response_spaces.py', 'baseline64/packet_kernels.npz',
           'results/response128/packet_kernels.npz', 'packet_comparison.json']
ARGUMENTS = ['--baseline', MEMBERS[1], '--new', MEMBERS[2], '--output', 'replayed_comparison.json']


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def source_path(name, root=ROOT):
    relative = PurePosixPath(name)
    require(not relative.is_absolute() and '..' not in relative.parts and '\\' not in name and ':' not in name,
            'unsafe evidence path')
    path = (root / name).resolve()
    require(path.is_relative_to((root / 'research/scattering/high-energy').resolve()), 'evidence outside source scope')
    return path


def validate(contract=None, pins=None, *, verify_sources=True, root=ROOT):
    contract = json.loads(CONTRACT.read_text()) if contract is None else contract
    pins = json.loads(PINS.read_text()) if pins is None else pins
    require(contract['id'] == 'scattering.high-energy.v1', 'wrong scattering net identity')
    require(contract['objective']['outcome'] is None and not contract['imports'], 'unreviewed root/proof import')
    require(all(value is False for value in contract['boundary'].values()), 'unsupported scientific promotion')
    require(contract['source_pins'] == 'research/scattering/high-energy/contracts/high-energy-source-pins.v1.json'
            and contract['adapter'] == 'research/scattering/high-energy/high_energy_scattering_net.py', 'net adapter/pins changed')
    claims = contract['conjectures']
    ids = {claim['id'] for claim in claims}
    require(len(ids) == len(claims) and contract['objective']['target'] in ids, 'duplicate/missing conjecture')
    for claim in claims:
        require(claim['outcome'] is None, 'historical report silently admitted as proof')
        require(claim['status'] in {'open', 'deferred_missing_source_map'}, 'unknown claim status')
        require(claim['evidence_status'] == 'historical_report_not_admitted_proof', 'historical verification upgrade')
        for evidence in claim['evidence']:
            source_path(evidence, root)
            require(evidence in pins['sources'], 'unpinned claim evidence')
    graph = MetricGraph(tuple(MetricAction(claim['id'], frozenset(claim['depends_on']),
                        frozenset(claim['requires']), status='pruned' if claim['status'].startswith('deferred') else 'active',
                        terminal=claim['id'] == contract['objective']['target']) for claim in claims),
                        frozenset(contract['interfaces']))
    graph.validate()
    actions = contract['actions']
    require(len(actions) == 1, 'unexpected executable action set')
    action = actions[0]
    require((action['id'], action['archive'], action['entrypoint'], action['members'], action['arguments']) ==
            ('replay-response128', ARCHIVE, MEMBERS[0], MEMBERS, ARGUMENTS), 'replay wiring/argv changed')
    require(action['claim'] in ids and all(action[key] is False for key in
            ('fresh_stationary_solve', 'full_scattering_matrix_computed', 'promotes_claim_outcome')), 'replay strength promotion')
    require(ARCHIVE in pins['sources'] and set(pins['archive_members'][ARCHIVE]) == set(MEMBERS), 'replay evidence incomplete')
    for name, pin in pins['sources'].items():
        path = source_path(name, root)
        require(pin['kind'] in {'source_archive', 'historical_source'}, 'unknown source evidence kind')
        if verify_sources:
            require(path.is_file() and path.stat().st_size == pin['bytes'] and digest(path) == pin['sha256'], 'stale source: ' + name)
    if verify_sources:
        with ZipFile(source_path(ARCHIVE, root)) as archive:
            for name, pin in pins['archive_members'][ARCHIVE].items():
                require(archive.getinfo(name).file_size == pin['bytes'] and
                        hashlib.sha256(archive.read(name)).hexdigest() == pin['sha256'], 'stale archive member: ' + name)
    return contract, pins, graph


def validate_programme():
    old = json.loads((ROOT / 'research/conjecture_net/contracts/programme-hierarchy.v14.json').read_text())
    new = json.loads((ROOT / 'research/conjecture_net/contracts/programme-hierarchy.v15.json').read_text())
    changed = {'schema', 'id', 'phase', 'predecessor', 'scattering_conjecture_nets'}
    require({k: v for k, v in old.items() if k not in changed} == {k: v for k, v in new.items() if k not in changed},
            'unrelated programme fields changed')
    require(new['phase'] == 'high_energy_scattering_net_source_wiring', 'wrong scattering phase')
    links = new['scattering_conjecture_nets']
    require(len(links) == 1 and links[0]['id'] == 'scattering.high-energy.v1' and
            links[0]['contract'] == CONTRACT.relative_to(ROOT).as_posix() and links[0]['source_pins'] == PINS.relative_to(ROOT).as_posix(),
            'programme scattering provenance changed')
    require(links[0]['proof_bearing'] is False and links[0]['discharges_parent_obligation'] is False and
            links[0]['outcome'] is None and links[0]['relation'] == 'candidate_scattering_testbed_not_proof_import',
            'candidate scattering link promoted')
    require(set(links[0]['target_obligations']) <= {x['id'] for x in old['obligations']}, 'unknown programme target')


def prepare(workspace, pins):
    workspace = workspace.resolve()
    require(workspace.is_relative_to((ROOT / '.ai/tmp').resolve()), 'workspace must be under repository .ai/tmp')
    with ZipFile(source_path(ARCHIVE)) as archive:
        for name in MEMBERS:
            pin = pins['archive_members'][ARCHIVE][name]
            relative = PurePosixPath(name)
            require(not relative.is_absolute() and '..' not in relative.parts and ':' not in name and '\\' not in name,
                    'unsafe archive member')
            target = workspace / name
            require(target.resolve().is_relative_to(workspace), 'archive member escapes workspace')
            data = archive.read(name)
            require(len(data) == pin['bytes'] and hashlib.sha256(data).hexdigest() == pin['sha256'], 'archive member drift')
            require(not target.exists() or target.read_bytes() == data, 'workspace input collision: ' + name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    return workspace


def compare_replay(current, saved):
    require(len(current['rows']) == len(saved['rows']) == 2, 'wrong replay rows')
    residuals = []
    for new, old in zip(current['rows'], saved['rows']):
        require(new['stride'] == old['stride'], 'replay stride changed')
        for side in ('baseline64', 'response128'):
            require(new[side]['energy_nodes'] == old[side]['energy_nodes'], 'replay energy grid changed')
            for key in ('packet_center', 'packet_RMS', 'peak_occupation', 'peak_transport',
                        'whole_packet_transport', 'product_probability', 'residence_integral'):
                residual = abs(new[side][key] - old[side][key])
                require(isclose(new[side][key], old[side][key], rel_tol=1e-9, abs_tol=1e-10), 'replay discrepancy: ' + side + '/' + key)
                residuals.append(residual)
    return max(residuals)


def replay(workspace, pins):
    workspace = prepare(workspace, pins)
    original = list(sys.argv)
    try:
        sys.argv = [str(workspace / MEMBERS[0])] + [value if value.startswith('--') else str(workspace / value) for value in ARGUMENTS]
        with redirect_stdout(io.StringIO()):
            runpy.run_path(str(workspace / MEMBERS[0]), run_name='__main__')
    finally:
        sys.argv[:] = original
    result = json.loads((workspace / 'replayed_comparison.json').read_text())
    residual = compare_replay(result, json.loads((workspace / 'packet_comparison.json').read_text()))
    fine, coarse = (row['response128']['peak_transport'] for row in result['rows'])
    return {'kind': 'fresh_saved_kernel_replay_not_stationary_solve', 'status': 'pass',
            'maximum_saved_readout_absolute_residual': residual,
            'response128_peak_transport': fine,
            'energy_subsampling_peak_change_percent': 100 * abs(coarse - fine) / abs(fine),
            'comparison': result, 'workspace': workspace.relative_to(ROOT).as_posix(),
            'claim_outcomes_promoted': False, 'full_S_computed': False, 'continuum_certified': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay', action='store_true', help='Run the existing64/128 kernel comparison in process; requires NumPy/SciPy.')
    parser.add_argument('--workspace', type=Path, default=ROOT / '.ai/tmp/high-energy-scattering-replay')
    args = parser.parse_args()
    contract, pins, graph = validate()
    validate_programme()
    receipt = {'schema': 'marici.scattering.high-energy-net-wiring-result.v1', 'status': 'pass',
               'validation_only': True, 'net': contract['id'], 'conjectures': len(contract['conjectures']),
               'source_files_verified': len(pins['sources']), 'metrics': graph.metrics(),
               'frontier': [a.name for a in graph.actions if a.status == 'active' and not a.dependencies and a.requires <= graph.interfaces],
               'deferred_claims': [c['id'] for c in contract['conjectures'] if c['status'].startswith('deferred')],
               'executable_actions': [a['id'] for a in contract['actions']], 'root_outcome': None,
               'source_sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in
                                 (CONTRACT, PINS, Path(__file__), ROOT / 'research/conjecture_net/graph_metrics.py')}}
    if args.replay:
        receipt['replay'] = replay(args.workspace, pins)
        # Source files remain intact even when the archived script writes workspace outputs.
        validate()
    output = HOME / 'results' / ('high-energy-net-replay.json' if args.replay else 'high-energy-net-wiring.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in receipt.items() if key not in {'source_sha256', 'replay'}}, indent=2))
    if args.replay:
        print(json.dumps({key: value for key, value in receipt['replay'].items() if key != 'comparison'}, indent=2))


if __name__ == '__main__':
    main()
