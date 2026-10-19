"""Validate a research attachment, never promote source reports to proof outcomes."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / 'research/nima/contracts/scattering-strominger-update.v1.json'
RESULT = ROOT / 'research/nima/results/scattering-strominger-update.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs(c):
    return sorted({c['base_net'], c['base_assessment']} | {s for n in c['nodes'] for s in n['sources']})


def validate(c, pins):
    require(c['root_outcome'] is None and c['assessment'] == 'physical_scattering_not_yet_explained', 'root promoted')
    require(all(v is False for v in c['boundary'].values()), 'boundary promoted')
    require(set(pins['source_sha256']) == set(inputs(c)), 'source pin set changed')
    for name, sha in pins['source_sha256'].items():
        p = (ROOT / name).resolve()
        require(p.is_relative_to(ROOT) and digest(p) == sha, 'source drift: ' + name)
    net = json.loads((ROOT / c['base_net']).read_text())
    status = json.loads((ROOT / c['base_assessment']).read_text())
    require(net['objective']['outcome'] is None and status['root_outcome'] is None, 'base status changed')
    require(set(c['unchanged_gaps']) == {g['id'] for g in status['remaining_gaps']}, 'gap erased')
    require(all(g['status'] == 'unresolved' for g in status['remaining_gaps']), 'base gap closed')
    ids = {n['id'] for n in c['nodes']}
    require(len(ids) == len(c['nodes']), 'duplicate nodes')
    base_ids = {n['id'] for n in net['conjectures']}
    seen = set()
    for n in c['nodes']:
        require(n['outcome'] is None, 'unreviewed proof import')
        require(set(n['depends_on']) <= seen, 'dependency missing, cyclic or out of order')
        require(set(n['related_base_conjectures']) <= base_ids, 'unknown base attachment')
        require(n['sources'] and n['next_gate'] and n['finding'], 'unscoped attachment')
        seen.add(n['id'])
    require(next(n for n in c['nodes'] if n['id'] == 'old-cycle-native-obstruction')['status'] == 'reported_obstruction', 'old obstruction erased')
    require(next(n for n in c['nodes'] if n['id'] == 'scattering-hamiltonian-bridge')['status'] == 'open_missing_operation_map', 'bridge assumed')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pin', action='store_true', help='Create initial source pins; never replace existing pins.')
    args = parser.parse_args()
    c = json.loads(CONTRACT.read_text())
    path = ROOT / c['source_pins']
    if args.pin:
        require(not path.exists(), 'refusing implicit re-pin')
        path.write_text(json.dumps({'schema': 'marici.scattering.research-overlay-pins.v1',
                                   'source_sha256': {name: digest(ROOT / name) for name in inputs(c)}}, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    pins = json.loads(path.read_text())
    validate(c, pins)
    hostiles = []
    for kind in ('root', 'proof', 'dependency', 'base-id', 'obstruction', 'bridge', 'gap', 'source-pin'):
        bad, bp = copy.deepcopy(c), copy.deepcopy(pins)
        if kind == 'root': bad['root_outcome'] = '++'
        elif kind == 'proof': bad['nodes'][0]['outcome'] = '++'
        elif kind == 'dependency': bad['nodes'][0]['depends_on'] = [bad['nodes'][-1]['id']]
        elif kind == 'base-id': bad['nodes'][0]['related_base_conjectures'] = ['invented']
        elif kind == 'obstruction': bad['nodes'][7]['status'] = 'closed'
        elif kind == 'bridge': bad['nodes'][-1]['status'] = 'closed'
        elif kind == 'gap': bad['unchanged_gaps'].pop()
        else: bp['source_sha256'][c['base_net']] = '0' * 64
        try:
            validate(bad, bp)
        except ValueError:
            hostiles.append(kind)
        else:
            raise AssertionError('hostile accepted: ' + kind)
    result = {'schema': 'marici.scattering.research-overlay-validation.v1', 'status': 'pass',
              'validation_only': True, 'node_count': len(c['nodes']), 'pinned_source_count': len(inputs(c)),
              'rejected_hostiles': hostiles, 'contract_sha256': digest(CONTRACT), 'pins_sha256': digest(path),
              'checker_sha256': digest(Path(__file__)), 'source_suites_rerun': False,
              'scattering_amplitudes_recomputed': False, 'root_outcome': None}
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
