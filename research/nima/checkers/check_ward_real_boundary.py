"""Verify a fresh native Rust boundary probe; no compiler subprocess wrapper.
Via structured-command, from repository root:
  python research/nima/checkers/check_ward_real_boundary.py --prepare
  cargo run --offline --manifest-path research/nima/checkers/ward-real-boundary-native/Cargo.toml --target-dir .ai/tmp/nima-ward-real-boundary-target
  python research/nima/checkers/check_ward_real_boundary.py
SCC checks this receipt verifier, not the complete original Ward audit.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import time

OWNER = Path(__file__).resolve().parents[1]
REPO = OWNER.parent.parent
SOURCE = OWNER/'check_two_open_pair_ward_naturality.rs'
PACKAGE = OWNER/'checkers/ward-real-boundary-native'
CONTRACT = OWNER/'contracts/ward-real-boundary.v1.json'
RAW = OWNER/'results/ward-real-boundary-native.json'
PREPARED = OWNER/'results/ward-real-boundary-prepared.json'
OUT = OWNER/'results/ward-real-boundary.json'
INPUTS = (SOURCE, CONTRACT, Path(__file__).resolve(), PACKAGE/'Cargo.toml',
          PACKAGE/'build.rs', PACKAGE/'src/main.rs')


def require(name, value):
    if not value:
        raise AssertionError(name)


def hashes():
    return {p.relative_to(REPO).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in INPUTS}


def fnv(data):
    value = 0xcbf29ce484222325
    for byte in data:
        value = ((value ^ byte) * 0x100000001b3) & ((1 << 64)-1)
    return f'{value:016x}'


def normalized_density(amplitude):
    norm2 = sum(x*x for x in amplitude)
    if norm2 == 0:
        raise ValueError('zero source amplitude cannot be normalized')
    return [[Fraction(x*y, norm2) for y in amplitude] for x in amplitude]


def prepare():
    OUT.unlink(missing_ok=True)
    RAW.unlink(missing_ok=True)
    PREPARED.unlink(missing_ok=True)
    PREPARED.parent.mkdir(parents=True, exist_ok=True)
    PREPARED.write_text(json.dumps({'prepared_ns': time.time_ns(), 'source_sha256': hashes()}, indent=2)+'\n')
    print('Prepared; old native and verified receipts removed. Execute the declared Cargo probe next.')


def main():
    OUT.unlink(missing_ok=True)
    prepared = json.loads(PREPARED.read_text())
    current_hashes = hashes()
    require('inputs-unchanged-since-prepare', current_hashes == prepared['source_sha256'])
    contract = json.loads(CONTRACT.read_text())
    require('contract-schema', contract['schema'] == 'marici.nima.ward-real-boundary.v1')
    raw = json.loads(RAW.read_text())
    require('native-result-schema', raw['schema'] == 'marici.nima.ward-real-boundary-native.v1')
    require('fresh-native-execution', int(raw['started_ns']) >= prepared['prepared_ns'])
    require('native-status', raw['status'] == 'pass')
    # This exactly mirrors the build's documentation-only conversion.
    native = '\n'.join('//'+line[3:] if line.startswith('//!') else line
                       for line in SOURCE.read_text().splitlines())+'\n'
    compiled = {'native_included': fnv(native.encode()),
                'main.rs': fnv((PACKAGE/'src/main.rs').read_bytes()),
                'build.rs': fnv((PACKAGE/'build.rs').read_bytes()),
                'Cargo.toml': fnv((PACKAGE/'Cargo.toml').read_bytes())}
    require('compiled-input-fingerprints', raw['compiled_fnv1a64'] == compiled)
    prediction = contract['predictions']
    require('complete-native-count', raw['tree_count'] == prediction['tree_count'] == 12
            and raw['tested_sectors'] == 12*prediction['sector_count_per_tree'] == 2916)
    rows = raw['trees']
    require('labelled-tree-coverage', len(rows) == 12 and len({r['mask'] for r in rows}) == 12)
    for row in rows:
        require('full-marked-sector-coverage', row['zero_sectors'] == 243 and row['boundary_value'] == 0)
        require('tree-open-slots', row['mask'].bit_count() == 4 and row['open_slots'] ==
                [slot for slot in range(6) if row['mask'] & (1 << slot) == 0])
    require('boundary-noncollapse-conjecture', raw['boundary_nonzero_sectors'] ==
            prediction['boundary_nonzero_sectors'] == 0)
    require('nonvacuity-control', raw['generic_nonzero_trees'] ==
            sum(int(r['generic_value']) != 0 for r in rows) > 0)
    require('a-zero-only-contrast-count', raw['a_zero_only_nonzero_trees'] ==
            sum(int(r['a_zero_only_value']) != 0 for r in rows))
    rejected_zero = False
    try:
        normalized_density((0, 0, 0, 0))
    except ValueError as error:
        rejected_zero = str(error) == 'zero source amplitude cannot be normalized'
    require('zero-normalization-refused', rejected_zero)
    good = normalized_density((1, 0, 0, 1))
    require('supplied-nonzero-normalization-control', sum(good[i][i] for i in range(4)) == 1
            and good[0][0] == good[0][3] == good[3][0] == good[3][3] == Fraction(1, 2))
    require('no-input-race', hashes() == current_hashes)
    result = {'schema': 'marici.nima.ward-real-boundary-result.v1', 'status': 'pass',
              'classification': 'real-collinear-physical-boundary-kills-every-native-tree-sector',
              'strength': 'exact original-Rust polynomial source execution on the boundary ideal, with a real-Lorentzian derivation of that ideal',
              'native_probe': raw, 'native_receipt_sha256': hashlib.sha256(RAW.read_bytes()).hexdigest(),
              'zero_normalization_refused': rejected_zero,
              'supplied_positive_control_density': [[str(v) for v in row] for row in good],
              'scope': contract['scope'], 'source_sha256': current_hashes,
              'verification_boundary': 'FNV1a64 compares compiled input snapshots; SHA256 pins live inputs and the native receipt. Not a compiler proof or physical calibration.'}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'classification': result['classification'],
                      'tested_sectors': raw['tested_sectors'],
                      'generic_nonzero_trees': raw['generic_nonzero_trees'],
                      'a_zero_only_nonzero_trees': raw['a_zero_only_nonzero_trees'],
                      'zero_normalization_refused': rejected_zero}, indent=2))


if __name__ == '__main__':
    if sys.argv[1:] == ['--prepare']:
        prepare()
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit('Use --prepare, or no arguments to verify the native receipt')
