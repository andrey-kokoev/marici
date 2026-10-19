"""Fresh Agda closure for source-bound native attachment actions.

Snapshot all included .agda sources before/after; source inventories are a
freshness boundary, not a proof that every snapshotted file was imported.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TOOLS = Path(os.environ.get('USERPROFILE', str(Path.home()))) / 'tools/cubical-agda'
COMPILER = TOOLS / 'agda-2.8.0/agda.exe'
LIBRARY = TOOLS / 'cubical-0.9'
SOURCE = ROOT / 'research/strominger/agda/NativeRelationAttachmentAction.agda'
INCLUDES = [SOURCE.parent, ROOT / 'research/nima/agda', ROOT / 'research/voevodsky/agda',
            ROOT / 'research/nima/adapters/native-application',
            ROOT / 'research/nima/adapters/application-extension', LIBRARY]
RESULTS = ROOT / 'research/strominger/results'

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def inventory():
    return {str(p.resolve()): digest(p) for directory in INCLUDES
            for p in sorted(directory.rglob('*.agda'))}

subprocess.run([sys.executable, str(ROOT / 'research/strominger/checkers/export_relation_packet_case.py'), '--check'], cwd=ROOT, check=True)
before = inventory()
compiler_hash = digest(COMPILER)
checker_hash = digest(Path(__file__))
command = [str(COMPILER), '--safe', '--cubical', '--guardedness',
           '--ignore-interfaces', '--transliterate']
for directory in INCLUDES:
    command.extend(['-i', str(directory)])
command.append(str(SOURCE))
run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                     encoding='utf-8', errors='replace', timeout=270)
RESULTS.mkdir(parents=True, exist_ok=True)
log = RESULTS / 'native-relation-attachment-action-agda-v1.log'
log.write_text(run.stdout + run.stderr, encoding='utf-8')
after = inventory()
stable = (before == after and digest(COMPILER) == compiler_hash
          and digest(Path(__file__)) == checker_hash)
result = {'schema': 'marici.native-relation-attachment-action.agda.v1',
          'passed': run.returncode == 0 and stable, 'exit_code': run.returncode,
          'ignore_interfaces': True, 'inputs_stable': stable,
          'command': command, 'source_sha256': digest(SOURCE),
          'compiler_sha256': compiler_hash, 'checker_sha256': checker_hash,
          'source_inventory': after,
          'inventory_scope': 'All .agda files in declared include roots; not a dependency graph',
          'log': str(log.relative_to(ROOT))}
(RESULTS / 'native-relation-attachment-action-agda-v1.json').write_text(
    json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k != 'source_inventory'}, indent=2))
print((run.stdout + run.stderr)[-4500:])
sys.exit(0 if result['passed'] else 1)
