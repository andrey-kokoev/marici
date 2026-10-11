"""Axiom-only bounded runs in both stroke conventions; no published proofs loaded."""
from pathlib import Path
import sys
import json
import hashlib
import time
import copy

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/nima/checkers'))
import fresh_equational_search as search
import check_fresh_equations as checker
import emit_fresh_equations as emitter

x, y, z = 'x0', 'x1', 'x2'
axioms = {
    'original': ((((x, y), z), (x, ((x, z), x))), z),
    'reversed': ((((x, (y, x)), x), (y, (z, x))), y),
}
OUT = ROOT / 'research/voevodsky/results/wg-ucc-audit'
summary = {}
for convention, axiom in axioms.items():
    started = time.monotonic()
    packet = search.complete(axiom, seconds=60, max_facts=1000, max_weight=80)
    packet['provenance'] = {
        'premises': 'only the displayed single axiom',
        'strategy': 'existing weight/age completion; standard basis goals unchanged',
        'primary_target': 'commutativity',
        'convention': convention,
        'prover_sha256': hashlib.sha256(Path(search.__file__).read_bytes()).hexdigest(),
        'published_proof_loaded': False,
    }
    path = OUT / f'commutativity-search-{convention}.json'
    path.write_text(json.dumps(packet, separators=(',', ':')) + '\n', encoding='utf-8')
    loaded = json.loads(path.read_text(encoding='utf-8'))
    checked = checker.verify(loaded, expected_input=axiom)
    module = 'CommutativitySearch' + convention.capitalize()
    agda_dir = ROOT / 'research/voevodsky/agda'
    agda_dir.mkdir(exist_ok=True)
    (agda_dir / (module + '.agda')).write_text(
        emitter.emit(loaded).replace('module FreshEquationalConsequences where',
                                     'module ' + module + ' where'), encoding='utf-8')
    hostile = copy.deepcopy(loaded)
    assert len(hostile['records']) > 1
    hostile['records'][1]['equation'] = ['x0', 'x1']
    try:
        checker.verify(hostile, expected_input=axiom)
    except ValueError:
        mutation_rejected = True
    else:
        raise AssertionError('mutated conclusion accepted')
    summary[convention] = {
        'status': packet['status'], 'statistics': packet['statistics'],
        'verification': checked, 'mutation_rejected': mutation_rejected,
        'elapsed_seconds': time.monotonic() - started,
        'certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    print(convention, json.dumps(summary[convention]), flush=True)
(OUT / 'commutativity-search-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
