"""Fresh isolated-target Agda check; no modification of the return-proof wrapper."""
from pathlib import Path
import hashlib
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOOLS = Path(os.environ['USERPROFILE']) / 'tools' / 'cubical-agda'
COMPILER = TOOLS / 'agda-2.8.0' / 'agda.exe'
LIBRARY = TOOLS / 'cubical-0.9'
SOURCE = ROOT / 'research/strominger/agda/FinitePayloadOccursCheck.agda'
OUT = ROOT / 'research/strominger/results/su32-static-payload-identification-v1'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def evidence():
    return {'source': digest(SOURCE), 'checker': digest(Path(__file__)),
            'compiler': digest(COMPILER),
            'library': {str(p.relative_to(LIBRARY)).replace('\\', '/'): digest(p)
                        for p in sorted(LIBRARY.rglob('*.agda'))}}


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    before = evidence()
    args = [str(COMPILER), '--safe', '--cubical', '--guardedness', '--ignore-interfaces',
            '-i', str(SOURCE.parent), '-i', str(LIBRARY), str(SOURCE)]
    done = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
    after = evidence()
    (OUT / 'agda.log').write_text(done.stdout + done.stderr, encoding='utf-8')
    result = {'schema': 'strominger.finite-payload-occurs.agda.v1',
              'module': 'FinitePayloadOccursCheck', 'args': args,
              'compiler_exit_code': done.returncode, 'ignore_interfaces': True,
              'inputs_stable_during_check': before == after,
              'passed': done.returncode == 0 and before == after,
              'source_inventory': after,
              'scope': 'Strict natural-number rank increase contradicts equality; JSON extraction is checked separately.'}
    (OUT / 'agda.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_inventory'}, indent=2))
    if not result['passed']:
        print(done.stdout + done.stderr)
        raise SystemExit(done.returncode or 43)
