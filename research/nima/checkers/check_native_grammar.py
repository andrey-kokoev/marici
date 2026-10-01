"""Source-bound census of the native grammar; Agda receipts are separate evidence."""
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'research/nima/generating-grammar'
MANIFEST = DIRECTORY / 'native-core.json'
TABLE = DIRECTORY / 'NATIVE-CORE.md'
REPORT = DIRECTORY / 'native-core-verification.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def constructors(text, datatype):
    """Read an explicitly delimited, layout-style Agda data declaration.

    This is a declaration census, not an Agda parser or proof checker. Unexpected
    declaration layout is rejected; comments do not count as constructors.
    """
    lines = text.splitlines()
    starts = [(i, len(m[1])) for i, line in enumerate(lines)
              if (m := re.match(r'^( *)data ' + re.escape(datatype) + r'\b.*\bwhere\s*$', line))]
    require(len(starts) == 1, 'ambiguous or missing datatype: ' + datatype)
    start, indent = starts[0]
    names = []
    for line in lines[start + 1:]:
        line = line.split('--', 1)[0].rstrip()
        if not line.strip():
            continue
        depth = len(line) - len(line.lstrip())
        if depth <= indent:
            break
        if depth != indent + 2:
            continue
        match = re.match(r'([A-Za-z_][A-Za-z0-9_-]*(?: +[A-Za-z_][A-Za-z0-9_-]*)*)\s*:', line.strip())
        require(match is not None, 'unsupported constructor layout: ' + line)
        names.extend(match[1].split())
    require(bool(names) and len(names) == len(set(names)), 'empty or duplicate constructors: ' + datatype)
    return names


def same(actual, expected, label):
    require(len(actual) == len(set(actual)), 'duplicate ' + label)
    require(set(actual) == set(expected), label + ' coverage mismatch')


def clauses(text, function, suffix):
    return set(re.findall(r'^  ' + re.escape(function) + r' \(?([A-Za-z][A-Za-z0-9_-]*' + suffix + r')\b', text, re.M))


def sources(data):
    result = {}
    for key, relative in data['sources'].items():
        path = (ROOT / relative).resolve()
        require(path.is_relative_to(ROOT.resolve()) and path.is_file(), 'missing or unsafe source: ' + relative)
        result[key] = path.read_text(encoding='utf-8-sig')
    return result


def validate(data, text):
    require(data['schema_version'] == 1, 'unsupported native schema')
    require(data['global_marici_coverage'] == 'open', 'global promotion requires independent coverage evidence')
    headers = [h['tag'] for h in data['headers']]
    rules = [r['tag'] for r in data['rules']]
    derivations = [d['tag'] for d in data['derivations']]
    same(headers, constructors(text['nodes'], 'Header'), 'native headers')
    same([data['formation']['constructor']], constructors(text['nodes'], 'Node'), 'node constructors')
    same([h['legacy'] for h in data['headers']], constructors(text['legacy_nodes'], 'Code'), 'legacy codes')
    same(rules, constructors(text['rules'], 'Kind'), 'native rules')
    same([r['legacy'] for r in data['rules']], constructors(text['legacy_rules'], 'Rule'), 'legacy rules')
    same(derivations, constructors(text['resolve'], 'Resolve'), 'native derivations')
    same(derivations, constructors(text['legacy_rules'], 'Resolve'), 'legacy derivations')
    for function in ('Arity', 'Inputs', 'Result'):
        same(list(clauses(text['nodes'], function, '-header')), headers, 'header ' + function)
    for function in ('Parameters', 'Arity', 'input', 'output'):
        same(list(clauses(text['rules'], function, '-kind')), rules, 'rule ' + function)
    for row in data['rules']:
        pattern = r'Iso.fun old-tagged \(R\.' + re.escape(row['legacy']) + r'\b[^\n]*= ' + re.escape(row['tag']) + r'\b'
        require(re.search(pattern, text['rules']) is not None, 'legacy/native rule mapping mismatch')
        for field in ('parameters', 'ports', 'premises', 'output', 'supplied'):
            require(isinstance(row[field], str) and row[field].strip(), 'empty rule field: ' + field)
    for row in data['headers']:
        for field in ('parameters', 'ports', 'inputs', 'result'):
            require(isinstance(row[field], str) and row[field].strip(), 'empty header field: ' + field)
    for witness in data['coverage_witnesses']:
        require(re.search(r'^  ' + re.escape(witness['symbol']) + r'\s*:', text[witness['source']], re.M) is not None,
                'missing coverage witness: ' + witness['symbol'])
    bridge = data['amplitude_interpretation']
    exprs = [x['tag'] for x in bridge['constructors']]
    same(exprs, constructors(text['amplitude'], 'Expr'), 'amplitude expressions')
    same(bridge['modes'], constructors(text['amplitude'], 'Mode'), 'amplitude modes')
    for row in bridge['constructors']:
        require(set(row['uses']) <= set(rules + derivations), 'unknown bridge rule')
        require(re.search(r'^  native-run \(?' + re.escape(row['tag']) + r'\b', text['amplitude'], re.M) is not None,
                'missing expression translation')
    require('execution = E.native-run' in text['arithmetic_bridge'], 'arithmetic bridge no longer uses native-run')
    return {'headers': len(headers), 'rule_schemas': len(rules), 'resolve_constructors': len(derivations),
            'amplitude_expression_forms': len(exprs), 'amplitude_modes': len(bridge['modes'])}


def rejection_tests(data, text):
    tests = [
        ('native headers coverage mismatch', lambda d, t: d['headers'].pop()),
        ('native rules coverage mismatch', lambda d, t: d['rules'].pop()),
        ('native derivations coverage mismatch', lambda d, t: d['derivations'].pop()),
        ('legacy/native rule mapping mismatch', lambda d, t: d['rules'][0].update(legacy='Pi-rule') or d['rules'][1].update(legacy='E-rule')),
        ('amplitude expressions coverage mismatch', lambda d, t: d['amplitude_interpretation']['constructors'].pop()),
        ('global promotion requires independent coverage evidence', lambda d, t: d.update(global_marici_coverage='closed')),
        ('native rules coverage mismatch', lambda d, t: t.update(rules=t['rules'].replace('  data Kind : Type where', '  data Kind : Type where\n    extra-kind : Kind'))),
        ('rule output coverage mismatch', lambda d, t: t.update(rules=t['rules'].replace('  output (higher-kind ,', '  removed-output (higher-kind ,'))),
    ]
    out = []
    for expected, mutation in tests:
        d, t = copy.deepcopy(data), dict(text)
        mutation(d, t)
        try:
            validate(d, t)
        except ValueError as error:
            require(str(error) == expected, 'wrong rejection: ' + str(error))
            out.append(expected)
        else:
            raise ValueError('malformed grammar accepted: ' + expected)
    return out


def render(data):
    def row(values):
        return '| ' + ' | '.join(str(v).replace('|', '\\|').replace('\n', ' ') for v in values) + ' |'
    lines = ['# Implemented native generating grammar', '',
             'Generated from `native-core.json`; source definitions, not this transcription, govern the types.', '',
             '## Formation', '', '```text', data['formation']['rule'], data['formation']['graph'],
             data['formation']['package'], '```', '', data['formation']['quantifiers'], '',
             '| Header | Parameters | Ports | Child types | Result type |', '|---|---|---|---|---|']
    lines += [row([h[k] for k in ('tag', 'parameters', 'ports', 'inputs', 'result')]) for h in data['headers']]
    lines += ['', '## Rule schemas', '',
              'Each application requires derivations at ALL its premise ports. Universe lifts are suppressed in this table, not in the source.', '',
              '| Rule | Parameters | Premises | Output |', '|---|---|---|---|']
    lines += [row([r[k] for k in ('tag', 'parameters', 'premises', 'output')]) for r in data['rules']]
    lines += ['', '## Retained derivations', '', '```text']
    lines += [d['rule'] for d in data['derivations']]
    lines += ['```', '', data['source_policy']['rule'], '', data['source_policy']['empty_policy'], '',
              '## Equality and coverage', '', data['formation']['equality'], '',
              'The source supplies package/rule/port and retained-closure equivalences with the legacy system. '
              'This covers all constructors of the named datatypes, not arbitrary repository operations.', '',
              '## Existing amplitude interpretation', '', '| Expression | Native derivation |', '|---|---|']
    lines += [row([r['tag'], r['translation']]) for r in data['amplitude_interpretation']['constructors']]
    lines += ['', data['amplitude_interpretation']['nonclaim'], '', '## External boundaries', '']
    lines += ['- ' + x for x in data['external_boundaries']]
    lines += ['', '## Sources', '']
    lines += [f'- [{key}](../../../{path})' for key, path in data['sources'].items()]
    return '\n'.join(lines) + '\n'


def formal_receipts(data):
    """Report compiler evidence only if receipts match current source inventories."""
    path = ROOT / 'research/nima/results/agda-NativeTableRegression.json'
    audit = ROOT / 'research/nima/results/native-table-formal-audit.json'
    if not path.is_file() or not audit.is_file():
        return {'status': 'missing', 'mathematical_verification': False}
    receipt = json.loads(path.read_text(encoding='utf-8-sig'))
    controls = json.loads(audit.read_text(encoding='utf-8-sig'))
    checked_keys = ('nodes', 'rules', 'resolve', 'closure', 'legacy_nodes', 'legacy_rules')
    inventory = receipt['owner_source_inventory_sha256']
    matched = all(inventory.get(Path(data['sources'][k]).name, '').lower() == sha(ROOT / data['sources'][k])
                  for k in checked_keys)
    controls_match = all(c['source_sha256'].lower() == sha(ROOT / 'research/nima/agda/negative' / (c['module'] + '.agda'))
                         for c in controls['controls'])
    valid = (receipt['passed'] and receipt['ignore_interfaces'] and matched and controls_match
             and controls['positive_receipt_sha256'].lower() == sha(path)
             and len(controls['controls']) == 6 and all(c['correctly_rejected'] for c in controls['controls']))
    return {'status': 'source_matched' if valid else 'stale_or_failed', 'mathematical_verification': bool(valid),
            'scope': 'Existing NativeTableRegression import closure and six rejection controls; not amplitude or component bridge compilation',
            'positive_receipt': str(path.relative_to(ROOT)), 'positive_sha256': sha(path),
            'audit_receipt': str(audit.relative_to(ROOT)), 'audit_sha256': sha(audit),
            'finished_at': receipt['finished_at']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--require-formal', action='store_true')
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    text = sources(data)
    counts = validate(data, text)
    tests = rejection_tests(data, text) if args.self_test else []
    table = render(data)
    formal = formal_receipts(data)
    if args.require_formal:
        require(formal['mathematical_verification'], 'source-matched formal evidence unavailable')
    if args.write:
        TABLE.write_text(table, encoding='utf-8')
    else:
        require(TABLE.is_file() and TABLE.read_text(encoding='utf-8') == table, 'native table stale')
    report = {'schema': 'marici.native_grammar.census.v1', 'status': 'passed',
              'checked_at': datetime.now(timezone.utc).isoformat(), 'counts': counts,
              'scope': 'Exhaustive declaration census and rule-clause coverage for the named datatypes; prose signatures are not machine typechecked',
              'global_marici_coverage': 'open', 'rejections': tests, 'formal': formal,
              'manifest_sha256': sha(MANIFEST), 'checker_sha256': sha(Path(__file__)), 'table_sha256': sha(TABLE),
              'sources': {k: {'path': p, 'sha256': sha(ROOT / p)} for k, p in data['sources'].items()}}
    if args.write:
        REPORT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
