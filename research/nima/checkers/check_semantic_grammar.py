"""Census and exact execution checks for the path/word grammar extensions."""
import argparse
import ast
from contextlib import redirect_stdout
import copy
from dataclasses import replace
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import io
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'research/nima/generating-grammar'
MANIFEST = DIRECTORY / 'semantic-extensions.json'
TABLE = DIRECTORY / 'SEMANTIC-EXTENSIONS.md'
REPORT = DIRECTORY / 'semantic-extensions-verification.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def python_definitions(text):
    tree = ast.parse(text)
    names = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            names.append(node.name)
        elif isinstance(node, ast.ClassDef):
            names.extend(node.name + '.' + child.name for child in node.body
                         if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)))
    return sorted(names)


def word_definitions(text):
    """Census the declared layout of ComponentArithmetic, not a general Agda parser."""
    result = []
    module = None
    for raw in text.splitlines():
        line = raw.split('--', 1)[0].rstrip()
        if not line.strip():
            continue
        if line.startswith('module Readout '):
            module = 'Readout'
            continue
        if re.match(r'^module (?!ComponentArithmetic\b)', line):
            raise ValueError('new arithmetic module requires census support')
        if line.startswith('Word = '):
            result.append('Word')
            continue
        match = re.match(r'^( *)([A-Za-z][A-Za-z0-9-]*)\s*:', line)
        if match:
            indent, name = len(match[1]), match[2]
            require(indent in (0, 2), 'unexpected arithmetic declaration layout')
            require(indent != 2 or module == 'Readout', 'unbound arithmetic module')
            result.append(('Readout.' if indent else '') + name)
    require(len(result) == len(set(result)), 'duplicate arithmetic declaration')
    return sorted(result)


def load_sources(data):
    out = {}
    for name, relative in data['sources'].items():
        path = (ROOT / relative).resolve()
        require(path.is_relative_to(ROOT.resolve()) and path.is_file(), 'invalid extension source')
        out[name] = path.read_text(encoding='utf-8-sig')
    return out


def validate(data, text):
    require(data['schema_version'] == 1, 'unsupported semantic schema')
    counts = {}
    for key, discovered in [('path_operations', python_definitions(text['paths'])),
                            ('word_operations', word_definitions(text['words']))]:
        rows = data[key]
        ids = [r['id'] for r in rows]
        require(len(ids) == len(set(ids)), 'duplicate extension id')
        symbols = [s for r in rows for s in r['symbols']]
        require(len(symbols) == len(set(symbols)), 'duplicate classified symbol')
        require(set(symbols) == set(discovered), key + ' source coverage mismatch')
        for row in rows:
            for field in ('id', 'kind', 'rule'):
                require(isinstance(row[field], str) and bool(row[field].strip()), 'empty extension field')
            require(bool(row['symbols']), 'empty extension symbols')
            if key == 'path_operations':
                for field in ('signature', 'requires', 'native_status'):
                    require(bool(row[field]), 'missing path boundary')
        counts[key] = {'groups': len(rows), 'definitions': len(symbols)}
    require('multiply = endo' in text['words'], 'multiplication alias drift')
    require('execution = E.native-run' in text['bridge'], 'native expression bridge drift')
    return counts


def census_hostiles(data, text):
    tests = [
        ('path_operations source coverage mismatch', lambda d, t: d['path_operations'].pop()),
        ('word_operations source coverage mismatch', lambda d, t: d['word_operations'].pop()),
        ('path_operations source coverage mismatch', lambda d, t: t.update(paths=t['paths'] + '\ndef unclassified_operation():\n    pass\n')),
        ('word_operations source coverage mismatch', lambda d, t: t.update(words=t['words'] + '\nnew-operation : Word\nnew-operation = empty\n')),
        ('duplicate classified symbol', lambda d, t: d['path_operations'][0]['symbols'].append('identity')),
        ('multiplication alias drift', lambda d, t: t.update(words=t['words'].replace('multiply = endo', 'multiply = append'))),
    ]
    out = []
    for expected, mutate in tests:
        d, t = copy.deepcopy(data), dict(text)
        mutate(d, t)
        try:
            validate(d, t)
        except ValueError as error:
            require(str(error) == expected, 'wrong rejection: ' + str(error))
            out.append(expected)
        else:
            raise ValueError('hostile accepted: ' + expected)
    return out


def path_tests():
    # Import only the existing implementation; silence its historical import-time diagnostics.
    with redirect_stdout(io.StringIO()):
        import retained_path_successor as p
    observations, rejected = [], []

    def rejects(name, fragment, operation):
        try:
            operation()
        except ValueError as error:
            require(fragment in str(error), 'wrong runtime rejection: ' + name + ': ' + str(error))
            rejected.append(name)
        else:
            raise ValueError('invalid path request accepted: ' + name)

    packets = (('b', 0, 0), ('a', 0, 0))
    plus = ((F(1, 2), F(1, 2)), (F(1, 2), F(1, 2)))
    minus = ((F(1, 2), F(-1, 2)), (F(-1, 2), F(1, 2)))
    descriptors = (p.SpectralDescriptor('common', 1, (2, 0), (plus, p.zero(2))),
                   p.SpectralDescriptor('contrast', 1, (0, 0), (minus, p.zero(2))))
    ledger = p.RetainedSuccessorLedger(packets, descriptors)
    root = ledger.root
    child = ledger.successor(root)
    grandchild = ledger.successor(child)
    require(p.apply(p.identity(2), (F(2), F(3))) == (F(2), F(3)), 'identity application')
    require(root.word_length == 1 and child.word_length == 2, 'word length')
    require(ledger.deconstruct(root) == packets, 'root deconstruction')
    parent, pieces = ledger.deconstruct(child)
    require(parent is root and tuple(a + (b,) for a, b in pieces) == child.paths, 'extension deconstruction')
    for stage in (root, child, grandchild):
        for direction in ('source', 'target'):
            require(ledger.deconstruct_family(ledger.family(stage, direction)) == stage.paths, 'index inverse lost order')
    observations.append('source/target indexing restores exact stage order and full parallel primitive IDs')

    root_values = (F(3), F(5))
    lifted = ledger.encode(root, grandchild, root_values)
    require(ledger.decode(root, grandchild, lifted) == root_values, 'chain inverse')
    l, a = ledger.transition(root, grandchild)
    require(p.mm(a, l) == p.identity(2), 'chain A L not identity')
    require(ledger.transition(root, root) == (p.identity(2), p.identity(2)), 'identity chain')
    observations.append('ancestor transition A L=I and encode/decode inverse on image')

    # Check the split identity on an exact basis, then a nontrivial rational combination.
    for stage in (child, grandchild):
        n = len(stage.paths)
        vectors = [tuple(F(i == j) for i in range(n)) for j in range(n)]
        vectors.append(tuple(F(i - 2, i + 1) for i in range(n)))
        for vector in vectors:
            means, detail = ledger.split_payload(stage, vector)
            require(not any(p.apply(stage.step_decoder, detail)), 'split remainder outside kernel')
            require(ledger.reassemble_payload(stage, means, detail) == vector, 'split inverse')
    observations.append('split/reassemble is identity on child bases and rational controls; remainders have zero sibling mean')
    siblings = [j for j, parent_slot in enumerate(child.parent_slots) if parent_slot == 0]
    kernel_witness = tuple(F(j == siblings[0]) - F(j == siblings[1]) for j in range(len(child.paths)))
    require(any(kernel_witness) and not any(p.apply(child.step_decoder, kernel_witness)), 'missing noninjective decoder witness')
    observations.append('nonzero sibling contrast has zero average: the full decoder cannot be substituted for a native equivalence')
    outside = (F(1), F(0), F(0), F(0))
    rejects('decode outside image', 'outside the requested transition image', lambda: ledger.decode(root, child, outside))
    rejects('nonzero-mean remainder', 'zero mean', lambda: ledger.reassemble_payload(child, (0, 0), (1, 1, 1, 1)))
    rejects('root split', 'no preceding extension', lambda: ledger.split_payload(root, (1, 2)))
    rejects('root reassemble', 'no preceding extension', lambda: ledger.reassemble_payload(root, (1, 2), (0, 0)))
    rejects('reversed ancestor chain', 'ancestor chain', lambda: ledger.transition(child, root))

    left = ledger.retain_payload(root, (2, 3))
    right = ledger.retain_path_payload(root.paths, (5, 7))
    product = ledger.compose_payloads(left, right)
    stored, slots = ledger.deconstruct_payload(product)
    require(stored[0] is left and stored[1] is right, 'parent identity lost')
    require(product.values == tuple(left.values[i] * right.values[j] for i, j in slots), 'bilinear rule')
    require(ledger.compose_primitive_payloads(child, (2, 3), (5, 7)) == product.values, 'primitive wrapper')
    require(all(b.rank_at_most_one for b in ledger.composition_blocks(left, right, product)), 'product failed rank test')
    candidate_values = tuple(F(i == j) for i, j in slots)
    candidate = ledger.retain_path_payload(product.paths, candidate_values)
    require(not all(b.rank_at_most_one for b in ledger.composition_blocks(left, right, candidate)), 'rank-two candidate hidden')
    third = ledger.retain_payload(root, (11, 13))
    bracket_left = ledger.compose_payloads(product, third)
    bracket_right = ledger.compose_payloads(left, ledger.compose_payloads(right, third))
    require((bracket_left.paths, bracket_left.values) == (bracket_right.paths, bracket_right.values), 'bilinear associativity')
    require(ledger.assembly_history(bracket_left) != ledger.assembly_history(bracket_right), 'assembly tree erased')
    observations.append('bilinear composition preserves exact operands/cut; equal associative readouts retain different assembly trees')
    observations.append('rank-one eligibility distinguishes a rank-two candidate without rewriting its preparation')
    require(ledger.summarize(child, product.values) == p.apply(child.summary, product.values), 'summary mismatch')

    modes = [ledger.inherit(child, d.name) for d in descriptors]
    image_projector = p.mm(child.origin_lift, child.origin_decoder)
    projectors = [ledger.inherited_projector(m)[0] for m in modes]
    require(p.add(*projectors) == image_projector, 'spectral projectors do not sum to lift-image projector')
    child_lift = ledger.encode(root, child, root_values)
    reads = [ledger.read_mode(m, child_lift)[0] for m in modes]
    require(tuple(x + y for x, y in zip(*reads)) == child_lift, 'spectral reconstruction')
    rejects('spectral ambient input', 'outside the requested transition image', lambda: ledger.read_mode(modes[0], outside))
    observations.append('inherited modes reconstruct only the declared lift image, not ambient child identity')

    foreign = p.RetainedSuccessorLedger(packets)
    rejects('foreign stage', 'foreign or substituted', lambda: ledger.resolve(foreign.root))
    rejects('forged equal stage', 'foreign or substituted', lambda: ledger.resolve(replace(root)))
    rejects('forged payload', 'foreign or substituted', lambda: ledger.resolve_payload(replace(left)))
    rejects('forged mode', 'foreign or substituted', lambda: ledger.resolve_mode(replace(modes[0])))
    rejects('forged family', 'foreign or substituted', lambda: ledger.deconstruct_family(replace(ledger.family(root, 'source'))))
    rejects('untyped index direction', 'Explicit source or target', lambda: ledger.family(root, 'label'))
    rejects('float coefficients', 'exact rational', lambda: ledger.retain_payload(root, (1.0, 2)))
    rejects('coefficient dimension', 'registered dimension', lambda: ledger.retain_payload(root, (1,)))
    rejects('matrix dimension', 'dimension mismatch', lambda: p.apply(p.identity(2), (F(1),)))
    rejects('duplicate primitive ID', 'must be unique', lambda: p.RetainedSuccessorLedger((('a', 0, 0), ('a', 0, 1))))
    rejects('missing descriptor', 'No registered origin descriptor', lambda: ledger.inherit(root, 'missing'))
    rejects('incomplete spectrum', 'Incomplete spectral reconstruction', lambda: p.RetainedSuccessorLedger(packets, descriptors[:1]))
    rejects('primitive product at wrong stage', 'direct successor', lambda: ledger.compose_primitive_payloads(grandchild, (1, 2), (3, 4)))
    rejects('wrong factor-test domain', 'complete composition domain', lambda: ledger.composition_blocks(left, right, third))
    sink = p.RetainedSuccessorLedger((('ab', 0, 1),))
    rejects('sink successor', 'no extension', lambda: sink.successor(sink.root))
    disconnected = p.RetainedSuccessorLedger((('ab', 0, 1), ('cd', 2, 3)))
    x = disconnected.retain_path_payload((disconnected.root.paths[0],), (0,))
    y = disconnected.retain_path_payload((disconnected.root.paths[1],), (1,))
    empty = disconnected.compose_payloads(x, y)
    require(empty.paths == empty.values == () and ledger.resolve_payload(left) is left, 'empty product vs zero slot')
    require(x.paths and x.values == (F(0),), 'zero slot dropped')
    rejects('unsewn supplied path', 'unsewn endpoint', lambda: disconnected.retain_path_payload((x.paths[0] + y.paths[0],), (1,)))
    rejects('empty supplied family', 'Nonempty family', lambda: disconnected.retain_path_payload((), ()))
    observations.append('structurally empty product differs from retained zero-coefficient word')
    return {'fixture': 'two parallel self-loop primitives, plus sink/disconnected controls',
            'passed': observations, 'rejections': rejected,
            'noninjective_decoder_witness': [str(v) for v in kernel_witness],
            'scope': 'Exact finite fixtures and basis checks, not a universal Python type-safety proof or native Resolve interpretation'}


def render(data):
    def row(values):
        return '| ' + ' | '.join(str(v).replace('|', '\\|').replace('\n', ' ') for v in values) + ' |'
    lines = ['# Computational grammar extensions', '',
             'Generated from `semantic-extensions.json`. These are source-defined computational operations, not extra native rule tags.', '',
             '## Retained-path grammar', '', data['path_grammar']['context'], '', '```text']
    lines += data['path_grammar']['productions']
    lines += ['```', '', data['path_grammar']['closure'], '',
              '| Operation | Source definitions | Kind | Signature | Rule / restriction |', '|---|---|---|---|---|']
    lines += [row([r['id'], ', '.join(r['symbols']), r['kind'], r['signature'], r['rule'] + ' Requires: ' + r['requires']])
              for r in data['path_operations']]
    lines += ['', '### Equations', ''] + ['- ' + x for x in data['path_grammar']['equations']]
    lines += ['', '## Component arithmetic', '', data['word_grammar']['production'], '', '```text']
    lines += data['word_grammar']['equations']
    lines += ['```', '', '| Operation | Source definitions | Kind | Rule |', '|---|---|---|---|']
    lines += [row([r['id'], ', '.join(r['symbols']), r['kind'], r['rule']]) for r in data['word_operations']]
    lines += ['', '## Native relationship', '']
    lines += ['- **' + k + '**: ' + v for k, v in data['native_relationship'].items()]
    lines += ['', data['word_grammar']['geometric_boundary'], '', '## Coverage boundary', '']
    lines += ['- ' + x for x in data['limits']]
    return '\n'.join(lines) + '\n'


def arithmetic_receipt():
    # Reuse the existing import-closure audit rather than inventing a second proof backend.
    import check_native_component_arithmetic_receipt as audit
    with redirect_stdout(io.StringIO()):
        audit.main()
    path = ROOT / 'research/nima/results/native-component-arithmetic-receipt.json'
    receipt = json.loads(path.read_text())
    return {'status': receipt['status'], 'receipt': str(path.relative_to(ROOT)), 'sha256': digest(path),
            'negative_controls': receipt['negative_controls'], 'local_import_modules': len(receipt['local_import_closure'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--require-formal', action='store_true')
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    text = load_sources(data)
    counts = validate(data, text)
    hostiles = census_hostiles(data, text) if args.self_test else []
    execution = path_tests()
    formal = arithmetic_receipt() if args.require_formal else {'status': 'not_requested'}
    table = render(data)
    if args.write:
        TABLE.write_text(table, encoding='utf-8')
    else:
        require(TABLE.is_file() and TABLE.read_text(encoding='utf-8') == table, 'extension table stale')
    report = {'schema': 'marici.semantic_grammar.v1', 'status': 'passed',
              'checked_at': datetime.now(timezone.utc).isoformat(), 'counts': counts,
              'census_hostiles': hostiles, 'path_execution': execution, 'arithmetic_formal': formal,
              'manifest_sha256': digest(MANIFEST), 'checker_sha256': digest(Path(__file__)), 'table_sha256': digest(TABLE),
              'sources': {k: {'path': p, 'sha256': digest(ROOT / p)} for k, p in data['sources'].items()},
              'global_marici_coverage': 'open', 'path_native_operational_bridge': 'open'}
    if args.write:
        REPORT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
