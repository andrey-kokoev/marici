"""Replay ChatGPT's checker read-only and compare its cells to the live target.

Outputs only under research/nima/results. This is exact computation, not Rzk
verification or authentication of the commit claimed by the incoming report.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
INCOMING = ROOT / 'research/chatgpt/mixed-normal-chern-comparision/check_mixed_normal_chern_comparison.py'
TARGET = ROOT / 'research/voevodsky/check_ringed_alexandrov_pc_target.py'
REPORT = INCOMING.with_name('mixed_normal_chern_comparison.md')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require(ok, detail):
    if not ok:
        raise AssertionError(detail)


def main():
    started = time.monotonic()
    before = {p.relative_to(ROOT).as_posix(): digest(p) for p in (INCOMING, TARGET, REPORT)}
    incoming = load('nima_incoming_mixed_normal', INCOMING)
    target = load('nima_live_loaded_target', TARGET)
    incoming.verify_local_graphs()
    incoming.verify_koszul()
    star, counts = incoming.verify_loaded()
    hom = incoming.verify_derived_hom()
    require(sum(incoming.CHECKS.values()) == 2755, 'Incoming check count changed')

    cells = [(f, h) for f in target.faces() for h in target.subsets(f)]
    require(cells == incoming.CELLS, 'Incoming and live cell ordering differ')
    require(incoming.D == target.DIAGONALS, 'Diagonal/coefficient ordering differs')
    for index, cell in enumerate(cells):
        reference = {(incoming.INDEX[c], m[0] + m[1]): v
                     for (c, m), v in target.boundary(cell).items()}
        require(reference == incoming.boundary(index, cech=True), f'Boundary mismatch at {index}')
        require(target.degree(cell) == incoming.degree(index), f'Degree mismatch at {index}')
        require(target.localization_set(cell) == cell[0] - cell[1], f'Localization mismatch at {index}')

    # All source and target degrees lie in [0,3], hence all Hom degrees in [-3,3].
    require(all(0 <= incoming.degree(i) <= 3 for i in range(len(cells))), 'Unexpected cochain amplitude')
    outside = {str(n): len(incoming.hom_basis(n)) for n in (-3, -2, -1)}
    require(not any(outside.values()), 'Omitted negative-degree homogeneous maps')
    for index in incoming.VERTICES:
        require(all(j in incoming.VERTICES for j, _ in incoming.boundary(index)), 'Endpoints are not a subcomplex')

    operators = {}
    for name, op in [('T', lambda i: incoming.T(i, True)), ('H', incoming.H), ('radial_defect', incoming.radial_defect)]:
        operators[name] = [dict(incoming.encode_hom((i, j, m)), coefficient=c)
                           for i in range(len(cells)) for (j, m), c in op(i).items()]
    for relative, expected in before.items():
        require(digest(ROOT / relative) == expected, f'Input changed during replay: {relative}')
    result = {
        'schema': 'marici.nima.mixed_normal_chern_replay.v1',
        'status': 'passed',
        'input_sha256': before,
        'input_hashes_match_before_after': True,
        'claimed_commit_authenticated': False,
        'incoming_checks': dict(sorted(incoming.CHECKS.items())),
        'incoming_total_checks': sum(incoming.CHECKS.values()),
        'live_cech_columns_compared': len(cells),
        'negative_degree_slice_dimensions': outside,
        'finite_endpoint_relative_generators': len(cells) - len(incoming.VERTICES),
        'endpoint_packets_are_subcomplex': True,
        'mixed_star_cells': len(star),
        'operator_columns_T_H_R': counts,
        'Hom': hom,
        'operators': operators,
        'duration_ms': round(1000 * (time.monotonic() - started)),
        'rzk_instantiation': 'not performed',
        'normalization_connector_composite': 'not computed',
        'scope': 'Incoming exact calculation replayed; all Cech columns matched to live source; no physical or infinity-groupoid identification'
    }
    out = ROOT / 'research/nima/results/mixed-normal-chern-replay.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in (
        'status', 'incoming_total_checks', 'live_cech_columns_compared',
        'negative_degree_slice_dimensions', 'finite_endpoint_relative_generators',
        'operator_columns_T_H_R', 'duration_ms')}))
    print(out.relative_to(ROOT).as_posix())


if __name__ == '__main__':
    main()
