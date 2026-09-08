"""Read-only replay of the incoming connector normal-variation calculation."""
from pathlib import Path
import json
import time
from check_mixed_normal_chern_import import ROOT, TARGET, load, digest, require

SOURCE = ROOT / 'research/chatgpt/mixed-connector-normal-variation/check_mixed_connector_normal_variation.py'
REPORT = SOURCE.with_name('mixed_connector_normal_variation.md')


def main():
    started = time.monotonic()
    inputs = {p.relative_to(ROOT).as_posix(): digest(p) for p in (SOURCE, REPORT, TARGET)}
    s = load('nima_connector_variation_input', SOURCE)
    live = load('nima_connector_live_target', TARGET)
    s.verify_loaded()
    hom = s.verify_derived_hom()
    s.verify_connections()
    horizontal = s.verify_horizontal_source()
    normal = s.verify_blowdown_normal_packet()
    local = s.verify_closed_star_connector()
    require(sum(s.CHECKS.values()) == 82427, 'Unexpected incoming assertion count')
    require(horizontal['elementary_homotopy_seed_maps'] == 1380, 'Seed census differs')
    require(horizontal['seed_maps_with_long_horizontal_endpoint_values'] == 1260, 'Endpoint-horizontal seed census differs')
    cells = [(f,h) for f in live.faces() for h in live.subsets(f)]
    require(cells == s.CELLS, 'Live cell table differs')
    for i,cell in enumerate(cells):
        reference = {(s.INDEX[c],m[0]+m[1]):a for (c,m),a in live.boundary(cell).items()}
        require(reference == s.boundary(i,True), f'Live target boundary mismatch at {i}')
    for path,expected in inputs.items():
        require(digest(ROOT / path) == expected, f'Input changed: {path}')
    result = {
        'schema': 'marici.nima.mixed_connector_variation_replay.v1',
        'status': 'passed', 'input_sha256': inputs,
        'input_hashes_match_before_after': True,
        'claimed_commit_authenticated': False,
        'total_checks': sum(s.CHECKS.values()), 'checks': dict(sorted(s.CHECKS.items())),
        'live_cech_columns_compared': len(cells),
        'target_Hom_negative_control': hom,
        'flat_source_tests': horizontal,
        'exceptional_normal_charts': normal,
        'closed_star_and_five_rows': local,
        'duration_ms': round(1000 * (time.monotonic()-started)),
        'rzk_verification_of_new_identities': False,
        'full_spatial_connector': 'not supplied or computed',
        'scope': 'Exact replay and live-target comparison; no raw-to-collapsed Gysin identification or Q-homotopy chosen'
    }
    out = ROOT / 'research/nima/results/mixed-connector-variation-replay.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','total_checks','live_cech_columns_compared','duration_ms')}))
    print(out.relative_to(ROOT).as_posix())


if __name__ == '__main__':
    main()
