"""Collect net infrastructure/data without relocating hash-pinned originals.

Run --refresh to update the collection explicitly, or --check to detect drift.
Snapshots retain repository-relative layout; execute checkers at original paths.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
HOME = ROOT / 'research/conjecture_net'
SUFFIXES = {'.py', '.json', '.jsonl', '.md', '.agda', '.rzk', '.yaml', '.yml', '.txt'}
TOKENS = ('conjecture-net', 'conjecture_net', 'completion-refinement',
          'completion_refinement', 'retained-reaggregation', 'retained_reaggregation',
          'closure-planning', 'closure_planning', 'bridge-planning', 'bridge_planning',
          'local-core-information', 'local_core_information', 'operational-whole-return-export',
          'operational_whole_return_export', 'operational-whole-return-downstream',
          'export_completed_local_lift', 'export_operational_whole_return',
          'interaction-net', 'interaction_net')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path):
    return path.relative_to(ROOT).as_posix()


def admissible(path):
    return (path.is_file() and path.suffix in SUFFIXES and
            '__pycache__' not in path.parts and not path.is_relative_to(HOME / 'collection'))


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)


def discover():
    selected = {}
    for path in (ROOT / 'research').rglob('*'):
        if not admissible(path) or path.is_relative_to(HOME):
            continue
        name = relative(path)
        if (name.startswith('research/conjecture_replay/') or
                name.startswith('research/nima/exports/') or
                name.startswith('research/nima/contracts/imports/') or
                any(token in path.name for token in TOKENS)):
            selected[name] = 'net/replay/export infrastructure or data'
        elif path.suffix in {'.py', '.md', '.json'}:
            text = path.read_text(encoding='utf-8', errors='replace')
            if any(token in text for token in ('research/conjecture_net', 'from outcome_reference import',
                                               'from bayesian_outcome_planner import',
                                               'interaction-net-state-contract', 'conjecture-net.v',
                                               'conjecture-net-contract', '"after_snapshot"')):
                selected[name] = 'shared net infrastructure consumer'
    # Follow concrete repository/local file references, including hash-pinned
    # evidence closures. Never fetch external dependencies or reinterpret claims.
    queue = sorted(selected)
    while queue:
        name = queue.pop()
        path = ROOT / name
        text = path.read_text(encoding='utf-8', errors='replace')
        references = set(re.findall(r'research/[A-Za-z0-9_./-]+\.[A-Za-z0-9]+', text))
        if path.suffix == '.json':
            try:
                references.update(strings(json.loads(text)))
            except (ValueError, TypeError):
                pass
        for ref in sorted(references):
            if len(ref) > 500 or '\n' in ref or not Path(ref).suffix:
                continue
            # JSON receipts also use owner-relative paths, e.g. agda/X.agda.
            candidates = [ROOT / ref, path.parent / ref]
            if len(path.relative_to(ROOT).parts) >= 3:
                candidates.append(ROOT / Path(*path.relative_to(ROOT).parts[:2]) / ref)
            for candidate in candidates:
                try:
                    candidate = candidate.resolve()
                    if not candidate.is_relative_to(ROOT) or candidate.is_relative_to(HOME):
                        continue
                    if not admissible(candidate):
                        continue
                except (OSError, ValueError):
                    continue
                target = relative(candidate)
                if target not in selected:
                    selected[target] = 'referenced evidence/dependency from ' + name
                    queue.append(target)
                break
    return selected


def registry(selected):
    nets, graphs = [], []
    candidates = set(selected) | {relative(path) for path in (HOME / 'contracts').glob('*.json')}
    for name in sorted(candidates):
        if not name.endswith('.json'):
            continue
        try:
            data = json.loads((ROOT / name).read_text(encoding='utf-8'))
        except (ValueError, UnicodeError):
            continue
        if not isinstance(data, dict):
            continue
        schema = str(data.get('schema', '')).lower()
        classification = None
        if ('/contracts/' in name and isinstance(data.get('conjectures'), list)
                and ('conjecture-net' in schema or 'conjecture-net' in name)):
            classification = 'conjecture-net contract'
        elif ('/contracts/' in name and schema.endswith('foundational-attachments.v1')
              and (isinstance(data.get('connections'), list) or isinstance(data.get('attachments'), list))):
            classification = 'typed foundational attachment index (not an independent conjecture net)'
        elif '/contracts/' in name and ('interaction-net-state' in schema or 'interaction-net-state' in name):
            classification = 'versioned interaction-net state contract'
        elif '/contracts/' in name and ('interaction-net' in schema or 'interaction-net' in name):
            classification = 'interaction-net infrastructure contract (not an independent conjecture net)'
        elif isinstance(data.get('after_snapshot'), dict) and isinstance(data['after_snapshot'].get('actions'), list):
            classification = 'replay action-net snapshot (not an independent net contract)'
        elif isinstance(data.get('conjectures'), list):
            classification = 'conjecture inventory (net relationships require inspection)'
        if classification:
            nets.append({'id': data.get('id', data.get('net_id', data.get('schema'))),
                         'classification': classification,
                         'contract': name,
                         'collected_contract': None if (ROOT / name).is_relative_to(HOME) else 'collection/' + name,
                         'declared_schema': data.get('schema'),
                         'status': 'not evaluated by collection',
                         'imports': data.get('imports', [])})
        if name.startswith('research/conjecture_replay/') and (
                'graph' in Path(name).name or 'event' in Path(name).name or
                'history' in Path(name).name):
            graphs.append({'source': name, 'collected': 'collection/' + name,
                           'classification': 'replay graph/event artifact; not automatically a net contract'})
    programmes = []
    for path in sorted((HOME / 'contracts').glob('programme-hierarchy.v*.json')):
        data = json.loads(path.read_text(encoding='utf-8'))
        programmes.append({'id': data['id'], 'contract': relative(path),
                           'phase': data.get('phase'), 'root': data['root']['id'],
                           'classification': 'programme conjecture template; not admitted proof',
                           'status': 'not evaluated by collection'})
    return {'schema': 'marici.conjecture-net.registry.v1', 'nets': nets,
            'programme_hierarchies': programmes,
            'replay_graph_and_event_artifacts': graphs,
            'boundary': 'Discovery and provenance only. Entries include versions, infrastructure, snapshots and inventories, not a count of independent nets. No copied status is live validation or proof admission.'}


def build(refresh=False):
    selected = discover()
    entries = []
    errors = []
    for name, reason in sorted(selected.items()):
        source = ROOT / name
        target = HOME / 'collection' / name
        source_hash = digest(source)
        if refresh:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
        if not target.exists() or digest(target) != source_hash:
            errors.append('missing/stale collection: ' + name)
        entries.append({'source': name, 'collected': 'collection/' + name,
                        'sha256': source_hash, 'reason': reason})
    documents = {
        'inventory.json': {'schema': 'marici.conjecture-net.collection.v1',
                           'mode': 'byte-identical snapshots; originals retained for pinned consumers',
                           'files': entries},
        'registry.json': registry(selected),
    }
    for name, data in documents.items():
        content = json.dumps(data, indent=2, sort_keys=True) + '\n'
        target = HOME / name
        if refresh:
            target.write_text(content, encoding='utf-8')
        elif not target.exists() or target.read_text(encoding='utf-8') != content:
            errors.append('missing/stale index: ' + name)
    expected = {entry['collected'] for entry in entries}
    if (HOME / 'collection').exists():
        for path in (HOME / 'collection').rglob('*'):
            if path.is_file() and path.relative_to(HOME).as_posix() not in expected:
                errors.append('unindexed snapshot (not automatically deleted): ' + str(path))
    return {'status': 'fail' if errors else 'pass', 'collected_files': len(entries),
            'registry_entries': len(documents['registry.json']['nets']), 'errors': errors}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--refresh', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = build(refresh=args.refresh)
    print(json.dumps(result, indent=2))
    raise SystemExit(result['status'] != 'pass')
