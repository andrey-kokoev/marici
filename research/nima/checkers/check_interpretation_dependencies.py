"""Bounded local Agda import audit; not an S4 derivation or signature freeze."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
AGDA = ROOT / 'research/nima/agda'
RESULT = ROOT / 'research/nima/results/interpretation-dependencies.json'
ROOTS = ('S4Aut', 'BoundaryGeneratedQuestions', 'RelationalCarrier',
         'OperandPairInterpretation', 'HistoryPathEdits', 'DGHistoryTransport',
         'DGFrameUpdates', 'DGCertificateTransport', 'DGActionComposition', 'DGActionInverse',
         'DGHistoryEditPolicy', 'PathLedgerInterpretations', 'InterpretationRegression')


def strip_comments(text):
    """Erase nested block and line comments, preserving positions/newlines."""
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith('{-', i):
            depth += 1
            out.extend('  ')
            i += 2
        elif depth and text.startswith('-}', i):
            depth -= 1
            out.extend('  ')
            i += 2
        elif depth:
            out.append('\n' if text[i] == '\n' else ' ')
            i += 1
        elif text.startswith('--', i):
            end = text.find('\n', i)
            end = len(text) if end < 0 else end
            out.extend(' ' * (end - i))
            i = end
        else:
            out.append(text[i])
            i += 1
    if depth:
        raise ValueError('unclosed block comment')
    return ''.join(out)


def imports(text):
    return sorted(set(re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)',
                                 strip_comments(text), re.MULTILINE)))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def receipt_matches(r, expected_root, closure_hashes):
    inventory = r.get('owner_source_inventory_sha256', {})
    return bool(r.get('passed') and r.get('ignore_interfaces')
                and r.get('source_sha256') == expected_root
                and all(inventory.get(k) == v for k, v in closure_hashes.items()))


def verify_aggregate_external():
    receipt = ROOT / 'research/nima/results/agda-InterpretationRegression.json'
    if not receipt.exists():
        return {'passed': False, 'reason': 'aggregate receipt missing'}
    r = json.loads(receipt.read_text(encoding='utf-8-sig'))
    library = Path(r['library'])
    inventory = r.get('library_source_inventory_sha256', {})
    current = {p.relative_to(library).as_posix(): sha(p) for p in library.rglob('*.agda') if p.is_file()}
    compiler = Path(r['command'])
    compiler_matches = compiler.is_file() and sha(compiler) == r.get('compiler_sha256')
    return {'passed': bool(r.get('passed') and r.get('ignore_interfaces')
                          and r.get('inputs_stable_during_check') and inventory
                          and inventory == current and compiler_matches),
            'library_sources': len(current), 'compiler_matches': compiler_matches,
            'receipt_sha256': sha(receipt),
            'boundary': 'Full Cubical .agda inventory checked; compiler built-in data and semantic derivability are NOT certified'}


def audit():
    nodes, external, missing = {}, set(), set()

    def visit(name):
        if name in nodes:
            return
        path = AGDA / (name.replace('.', '/') + '.agda')
        if not path.exists():
            (external if name.startswith(('Cubical.', 'Agda.')) else missing).add(name)
            return
        text = path.read_text(encoding='utf-8')
        code = strip_comments(text)
        deps = imports(text)
        options = re.findall(r'\{-#\s*OPTIONS\s+(.*?)#-\}', text, re.DOTALL)
        flags = sorted(set(' '.join(options).split()))
        findings = []
        if '--safe' not in flags:
            findings.append('missing_safe_option')
        for label, pattern in [('postulate', r'\bpostulate\b'),
                               ('hole', r'\{!!?'),
                               ('unsafe_pragma', r'\{-#\s*(?:TERMINATING|NON_TERMINATING|NO_POSITIVITY_CHECK)\b')]:
            if re.search(pattern, text if label == 'unsafe_pragma' else code):
                findings.append(label)
        if '?' in code:
            findings.append('question_mark_review')
        nodes[name] = {'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path),
                       'imports': deps, 'options': flags, 'findings': findings}
        for dep in deps:
            visit(dep)

    for root in ROOTS:
        visit(root)

    def closure(name, seen=None):
        seen = set() if seen is None else seen
        if name in seen or name not in nodes:
            return seen
        seen.add(name)
        for dep in nodes[name]['imports']:
            closure(dep, seen)
        return seen

    receipts = {}
    for root in ROOTS:
        local = sorted(closure(root))
        receipt = ROOT / f'research/nima/results/agda-{root}.json'
        evidence = {'local_closure': local, 'receipt_status': 'missing'}
        if receipt.exists():
            r = json.loads(receipt.read_text(encoding='utf-8-sig'))
            inventory = r.get('owner_source_inventory_sha256', {})
            stale = [m for m in local if inventory.get(m + '.agda') != nodes[m]['sha256']]
            evidence.update(receipt_status='matching_fresh_local_closure' if
                            receipt_matches(r, nodes[root]['sha256'],
                                            {m + '.agda': nodes[m]['sha256'] for m in local}) else 'unverified_or_stale',
                            stale_local_sources=stale,
                            compiler_sha256=r.get('compiler_sha256'),
                            receipt_sha256=sha(receipt))
        receipts[root] = evidence
    syntax_ok = not missing and not any(n['findings'] for n in nodes.values())
    receipts_ok = all(r['receipt_status'] == 'matching_fresh_local_closure' for r in receipts.values())
    external_evidence = verify_aggregate_external()
    return {'schema': 'marici.nima.interpretation-dependencies.v2',
            'scope': 'Local import graph plus aggregate compiler/Cubical source inventory binding; built-in data and semantic source derivability are NOT certified',
            'audit_passed': syntax_ok and receipts_ok and external_evidence['passed'],
            'external_inventory': external_evidence,
            'signature_status': 'unresolved',
            'conditional_interfaces': {
                'DGHistoryTransport.DGFragment': 'supplied graded operations, additive laws, action associativity and differential laws',
                'DGFrameUpdates.FrameAlgebra': 'supplied unit, subtraction, associativity, distributivity and cancellation',
                'DGCertificateTransport.CertificateAlgebra': 'supplied negation and unit action laws',
                'DGActionComposition.ActionAlgebra': 'supplied degree-two addition/action distributivity and associativity',
                'DGActionInverse.InverseAlgebra': 'supplied degree-two unit action, right negation action and additive cancellation',
                'DGHistoryEditPolicy.Policy': 'supplied FrameAlgebra, parent admission, declared readout, cost and permission predicate; arbitrary readout witness required',
                'HistoryPathEdits.Edits': 'supplied S, Q, observation, invariant, cost and permission policy'},
            'roots': receipts, 'nodes': dict(sorted(nodes.items())),
            'external_import_boundary': sorted(external), 'missing_local_imports': sorted(missing),
            'syntax_audit_passed': syntax_ok}


def self_test():
    assert imports('-- import Fake\nopen import Real.One\n{- import Bad {- x -} -}\nimport Real.Two as T') == ['Real.One', 'Real.Two']
    sample = 'a {- nested {- x -} -} b'
    clean = strip_comments(sample)
    assert len(clean) == len(sample) and clean.split() == ['a', 'b']
    r = {'passed': True, 'ignore_interfaces': True, 'source_sha256': 'root',
         'owner_source_inventory_sha256': {'Root.agda': 'root', 'Dep.agda': 'dep'}}
    expected = {'Root.agda': 'root', 'Dep.agda': 'dep'}
    assert receipt_matches(r, 'root', expected)
    assert not receipt_matches(r, 'changed-root', expected)
    assert not receipt_matches(r, 'root', dict(expected, **{'Dep.agda': 'changed'}))
    for key in ('passed', 'ignore_interfaces'):
        assert not receipt_matches(dict(r, **{key: False}), 'root', expected)
    assert not receipt_matches({}, 'root', expected)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    report = audit()
    if args.write:
        RESULT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'audit_passed': report['audit_passed'],
                      'external_inventory': report['external_inventory'],
                      'syntax_audit_passed': report['syntax_audit_passed'],
                      'local_sources': len(report['nodes']),
                      'external_boundary': len(report['external_import_boundary']),
                      'root_receipts': {k: v['receipt_status'] for k, v in report['roots'].items()},
                      'findings': {k: v['findings'] for k, v in report['nodes'].items() if v['findings']},
                      'missing': report['missing_local_imports']}, indent=2))
    raise SystemExit(0 if report['audit_passed'] else 1)
