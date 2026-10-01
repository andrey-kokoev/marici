"""Source census of arithmetic completion and typed policy-boundary assessment."""
import argparse
import copy
from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'research/nima/generating-grammar'
MANIFEST = DIRECTORY / 'completions-and-policies.json'
TABLE = DIRECTORY / 'COMPLETIONS-AND-POLICIES.md'
REPORT = DIRECTORY / 'completion-verification.json'
POLICY_STATUSES = {'partial_realization', 'conditional_encoding', 'computation_not_identified',
                   'external_admission_policy', 'core_macro_with_external_policy'}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().lower()


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def declarations(text):
    """Layout census of public definitions, module schemas/aliases and data tags.

    Proof-local where declarations are not exported and are excluded. This
    checks the source layouts used by these files, not arbitrary Agda syntax.
    The Agda compiler remains the type/equation checker.
    """
    stack, definitions, schemas, aliases, datatypes = [], set(), [], [], {}
    current_data = None
    root_seen = False
    for raw in text.splitlines():
        line = raw.split('--', 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        body = line.strip()
        if current_data and indent <= current_data[0]:
            current_data = None
        if current_data:
            if indent == current_data[0] + 2:
                m = re.match(r'([\w-]+(?: +[\w-]+)*)\s*:', body)
                require(m is not None, 'unsupported datatype constructor layout')
                datatypes[current_data[1]].extend(m[1].split())
            continue
        while stack and indent <= stack[-1][0]:
            stack.pop()
        prefix = '.'.join(name for _, name in stack)
        qualify = lambda name: prefix + '.' + name if prefix else name
        module = re.match(r'module ([\w-]+)(.*)', body)
        if module:
            name, rest = module.groups()
            if not root_seen:
                require(indent == 0 and rest.strip() == 'where', 'unrecognized root module')
                root_seen = True
                continue
            if rest.lstrip().startswith('='):
                aliases.append(qualify(name))
            else:
                schemas.append(qualify(name))
                stack.append((indent, name))
            continue
        expected_indent = stack[-1][0] + 2 if stack else 0
        if indent != expected_indent:
            continue
        data = re.match(r'data ([\w-]+).*where$', body)
        if data:
            name = qualify(data[1])
            datatypes[name] = []
            current_data = (indent, name)
            continue
        signature = re.match(r'([\w-]+(?: +[\w-]+)*)\s*:', body)
        if signature:
            definitions.update(qualify(n) for n in signature[1].split())
            continue
        alias = re.match(r'([\w-]+)\s*=', body)
        if alias:
            definitions.add(qualify(alias[1]))
    return {'definitions': sorted(definitions), 'parameter_modules': sorted(schemas),
            'module_aliases': sorted(aliases), 'datatypes': datatypes}


def source_text(data):
    result = {}
    for key, relative in data['sources'].items():
        path = (ROOT / relative).resolve()
        require(path.is_relative_to(ROOT.resolve()) and path.is_file(), 'invalid completion source')
        result[key] = path.read_text(encoding='utf-8-sig')
    return result


def same(given, expected, label):
    require(len(given) == len(set(given)), 'duplicate ' + label)
    require(set(given) == set(expected), label + ' mismatch: ' + str(sorted(set(given) ^ set(expected))))


def policy_items(text):
    section = text.split('## State and operation ledger', 1)[1].split('\n## ', 1)[0]
    return [line.split('|')[1].strip() for line in section.splitlines()
            if line.startswith('| ') and line.split('|')[1].strip() != 'Operation']


def validate(data, text):
    require(data['schema_version'] == 1, 'unsupported completion schema')
    require(data['global_generation'] == 'open', 'global coverage cannot be promoted by census')
    counts = {}
    same([m['source'] for m in data['modules']],
         ['signed', 'rational', 'faithful', 'transport', 'bridge', 'macros'], 'completion module boundary')
    for module in data['modules']:
        key = module['source']
        found = declarations(text[key])
        names = [n for group in module['groups'] for n in group['symbols']]
        same(names, found['definitions'], key + ' definitions')
        for field in ('parameter_modules', 'module_aliases'):
            same(module[field], found[field], key + ' ' + field)
        require(module['datatypes'] == found['datatypes'], key + ' data constructor drift')
        for group in module['groups']:
            require(all(isinstance(group[f], str) and group[f].strip() for f in ('id', 'kind', 'rule')), 'empty completion group')
        counts[key] = {'definitions': len(names), 'parameter_modules': len(found['parameter_modules']),
                       'module_aliases': len(found['module_aliases']), 'datatypes': len(found['datatypes'])}
    assessments = data['policy_assessments']
    same([r['item'] for r in assessments], policy_items(text['policy']), 'policy coverage')
    native = load(DIRECTORY / 'native-core.json')
    rules = {r['tag'] for r in native['rules']}
    for row in assessments:
        require(row['status'] in POLICY_STATUSES, 'unsupported policy promotion')
        require(row['native_forms'] and set(row['native_forms']) <= rules, 'unknown native policy form')
        require(all(isinstance(row[f], str) and row[f].strip() for f in ('available', 'missing', 'test')), 'missing policy boundary')
    return {'modules': counts, 'total_definitions': sum(m['definitions'] for m in counts.values()), 'policy_rows': len(assessments)}


def hostiles(data, text):
    tests = [
        ('signed definitions mismatch:', lambda d, t: d['modules'][0]['groups'][0]['symbols'].pop()),
        ('rational definitions mismatch:', lambda d, t: t.update(rational=t['rational'] + '\nunclassified : Type\nunclassified = Rational\n')),
        ('policy coverage mismatch:', lambda d, t: d['policy_assessments'].pop()),
        ('unsupported policy promotion', lambda d, t: d['policy_assessments'][0].update(status='fully_derived')),
        ('global coverage cannot be promoted by census', lambda d, t: d.update(global_generation='closed')),
        ('unknown native policy form', lambda d, t: d['policy_assessments'][0].update(native_forms=['invented-kind'])),
    ]
    rejected = []
    for expected, mutate in tests:
        d, t = copy.deepcopy(data), dict(text)
        mutate(d, t)
        try:
            validate(d, t)
        except ValueError as error:
            require(str(error).startswith(expected), 'wrong rejection: ' + str(error))
            rejected.append(str(error))
        else:
            raise ValueError('bad completion manifest accepted')
    return rejected


def formal_evidence():
    import check_completed_component_arithmetic_receipt as audit
    with redirect_stdout(io.StringIO()):
        audit.main()
    receipt_path = ROOT / 'research/nima/results/completed-component-arithmetic-receipt.json'
    arithmetic = load(receipt_path)
    result = ROOT / 'research/nima/results'
    positive_path = result / 'agda-GeneratingGrammarMacros.json'
    audit_path = result / 'generating-grammar-macros-formal-audit.json'
    positive, macro_audit = load(positive_path), load(audit_path)
    require(positive['passed'] and positive['ignore_interfaces'], 'macros not freshly checked')
    require(macro_audit['positive_receipt_sha256'].lower() == digest(positive_path), 'macro audit mismatch')
    require(macro_audit['checker_sha256'].lower() == digest(ROOT / 'research/nima/checkers/check_generating_grammar_macros.ps1'), 'macro checker stale')
    require(macro_audit['negative_source_sha256'].lower() == digest(ROOT / 'research/nima/agda/negative/GeneratingGrammarMissingOperand.agda'), 'macro negative stale')
    log = result / 'agda-GeneratingGrammarMissingOperand.log'
    require(macro_audit['negative_log_sha256'].lower() == digest(log), 'macro negative log stale')
    require('[UnequalTerms]' in log.read_text(encoding='utf-8-sig') and macro_audit['negative_exit_code'] != 0, 'missing negative control')
    checked = {}
    def visit(name):
        path = ROOT / 'research/nima/agda' / (name.replace('.', '/') + '.agda')
        if name in checked or not path.is_file():
            return
        checked[name] = digest(path)
        require(positive['owner_source_inventory_sha256'][path.name].lower() == checked[name], 'macro import stale: ' + name)
        for imported in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)', path.read_text(encoding='utf-8'), re.M):
            visit(imported)
    visit('GeneratingGrammarMacros')
    return {'completed_arithmetic': {'status': arithmetic['status'], 'receipt_sha256': digest(receipt_path),
                                    'local_import_modules': len(arithmetic['local_import_closure']),
                                    'negative_controls': list(arithmetic['negative_control_log_sha256'])},
            'native_macros': {'status': 'passed', 'audit_sha256': digest(audit_path),
                              'local_import_closure': checked, 'missing_operand_rejected': True}}


def render(data):
    def row(values):
        return '| ' + ' | '.join(str(x).replace('|', '\\|').replace('\n', ' ') for x in values) + ' |'
    out = ['# Arithmetic completion and policy interpretation', '',
           'Generated from `completions-and-policies.json`. Source definitions and compiled witnesses govern claims.', '',
           '## Coefficient grammar', '', '```text']
    for field in ('carriers', 'relations', 'operations'):
        out.extend(data['arithmetic_grammar'][field])
    out += ['```', '', data['arithmetic_grammar']['descent'], '', data['arithmetic_grammar']['native_execution'], '',
            data['arithmetic_grammar']['inputs'], '', data['arithmetic_grammar']['inverse_boundary'], '',
            '## Exhaustive public-definition coverage', '',
            'Proof-local where helpers are not public definitions. Module schemas and aliases are also checked against source.', '']
    for module in data['modules']:
        out += [f"### {module['source']}", '', '| Group | Kind | Definitions | Rule |', '|---|---|---|---|']
        out += [row([g['id'], g['kind'], ', '.join(g['symbols']), g['rule']]) for g in module['groups']]
        out.append('')
    out += ['## Policy audit: all nine source rows', '',
            'A native encoding or a retention macro does not establish a derivation of the entire policy operation.', '',
            '| Operation | Status | Available native correspondence | Remaining input / adapter |', '|---|---|---|---|']
    out += [row([r['item'], r['status'], r['available'], r['missing']]) for r in data['policy_assessments']]
    out += ['', '## Boundary', '', data['coverage_boundary']['closed'], '', data['coverage_boundary']['open'], '',
            data['coverage_boundary']['prohibited_shortcut'], '', 'Next executable: ' + data['coverage_boundary']['next_executable'], '']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--require-formal', action='store_true', help='explicit spelling of the default source-bound evidence check')
    mode.add_argument('--metadata-only', action='store_true', help='skip proof receipts for isolated census work')
    args = parser.parse_args()
    data = load(MANIFEST)
    text = source_text(data)
    counts = validate(data, text)
    rejections = hostiles(data, text) if args.self_test else []
    evidence = formal_evidence() if not args.metadata_only else {'status': 'not_requested'}
    table = render(data)
    if args.write:
        TABLE.write_text(table, encoding='utf-8')
    else:
        require(TABLE.is_file() and TABLE.read_text(encoding='utf-8') == table, 'completion table stale')
    report = {'schema': 'marici.grammar_completion_audit.v1', 'status': 'passed',
              'checked_at': datetime.now(timezone.utc).isoformat(), 'counts': counts, 'rejections': rejections,
              'formal': evidence, 'global_generation': 'open', 'manifest_sha256': digest(MANIFEST),
              'checker_sha256': digest(Path(__file__)), 'table_sha256': digest(TABLE),
              'sources': {k: {'path': p, 'sha256': digest(ROOT / p)} for k, p in data['sources'].items()}}
    if args.write:
        REPORT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
