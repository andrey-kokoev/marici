"""Isolated hostiles against the actual native-receipt verifier; standard library."""
import importlib.util
import json
from pathlib import Path
import tempfile

OWNER = Path(__file__).resolve().parents[1]
CHECKER = OWNER/'checkers/check_ward_real_boundary.py'
OUT = OWNER/'results/ward-real-boundary-failure-lifecycle.json'


def load():
    spec = importlib.util.spec_from_file_location('boundary_receipt_verifier', CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    OUT.unlink(missing_ok=True)
    baseline = load()
    live = {p: p.read_bytes() for p in (baseline.SOURCE, baseline.OUT, baseline.RAW, baseline.PREPARED)}
    raw = json.loads(live[baseline.RAW])
    tested = []
    with tempfile.TemporaryDirectory(prefix='ward-boundary-hostiles-', dir=OWNER/'results') as directory:
        directory = Path(directory)
        for name, expected in (
            ('compiled-input-change', 'compiled-input-fingerprints'),
            ('source-sector-drop', 'full-marked-sector-coverage'),
            ('stale-native-run', 'fresh-native-execution'),
            ('fabricated-zero-normalization', 'zero-normalization-refused'),
        ):
            module = load()
            module.OUT = directory/'verified.json'
            module.RAW = directory/'native.json'
            hostile = json.loads(json.dumps(raw))
            if name == 'compiled-input-change':
                hostile['compiled_fnv1a64']['native_included'] = '0000000000000000'
            elif name == 'source-sector-drop':
                hostile['trees'][0]['zero_sectors'] -= 1
            elif name == 'stale-native-run':
                hostile['started_ns'] = '0'
            else:
                good = module.normalized_density((1, 0, 0, 1))
                module.normalized_density = lambda amplitude: good
            module.RAW.write_text(json.dumps(hostile))
            module.OUT.write_bytes(live[baseline.OUT])
            try:
                module.main()
            except AssertionError as error:
                assert str(error) == expected, (name, str(error))
            else:
                raise AssertionError('Hostile accepted: '+name)
            assert not module.OUT.exists(), 'Stale success survived: '+name
            tested.append(name)
        module = load()
        module.OUT, module.RAW, module.PREPARED = [directory/name for name in ('verified.json', 'native.json', 'prepared.json')]
        for path in (module.OUT, module.RAW, module.PREPARED):
            path.write_text('{"status":"pass"}')
        module.INPUTS = (directory/'absent-source',)
        try:
            module.prepare()
        except FileNotFoundError:
            pass
        else:
            raise AssertionError('Missing prepare input accepted')
        assert all(not path.exists() for path in (module.OUT, module.RAW, module.PREPARED))
        tested.append('prepare-failure-clears-all-old-receipts')
    assert all(p.read_bytes() == data for p, data in live.items())
    result = {'status': 'pass', 'hostiles_rejected': tested, 'stale_success_survivors': 0,
              'live_source_and_receipts_unchanged': True}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
