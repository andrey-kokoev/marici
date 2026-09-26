"""Exact parallel endpoint/label grouping and competing residual meanings."""
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT/'research/nima'


def encode(rows):
    branches = []
    for endpoint in (1, 2):
        grouped = defaultdict(lambda: defaultdict(list))
        for identity, row in enumerate(rows):
            grouped[row[endpoint]][row[0]].append((identity, row))
        branches.append({port: {label: tuple(fiber) for label, fiber in labels.items()}
                         for port, labels in grouped.items()})
    return tuple(branches)


def decode(packet):
    recovered = []
    for endpoint, branch in enumerate(packet, 1):
        rows = {}
        for port, labels in branch.items():
            for label, fiber in labels.items():
                for identity, row in fiber:
                    if identity in rows or row[0] != label or row[endpoint] != port:
                        raise ValueError('invalid fiber membership or duplicate identity')
                    rows[identity] = row
        if set(rows) != set(range(len(rows))):
            raise ValueError('noncanonical row identity set')
        recovered.append(rows)
    if len(recovered) != 2 or recovered[0] != recovered[1]:
        raise ValueError('parallel branches do not retain the same rows')
    return tuple(recovered[0][i] for i in range(len(recovered[0])))


def tagged_C(presentation):
    tag, data = presentation
    if tag == 'raw':
        return 'grouped', encode(data)
    if tag == 'grouped':
        rows = decode(data)
        if encode(rows) != data:
            raise ValueError('outside canonical grouped image')
        return 'raw', rows
    raise ValueError('undeclared presentation sort')


def marginals(rows):
    return Counter((label, source) for label, source, target in rows), Counter(
        (label, target) for label, source, target in rows)


def label_only_join(rows):
    incoming, outgoing = marginals(rows)
    return frozenset((label, source, target) for label, source in incoming
                     for other_label, target in outgoing if label == other_label)


def transpose(m):
    return tuple(zip(*m))


def subtract(a, b):
    return tuple(tuple(x-y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(a, factor):
    return tuple(tuple(factor*x for x in row) for row in a)


def residual(a):
    return subtract(a, transpose(a))


def main():
    out = OWNER/'results/parallel-label-fibration.json'
    out.unlink(missing_ok=True)
    alphabet = tuple(product(range(2), repeat=3))  # label, input, output
    cases = 0
    for n in range(5):
        for rows in product(alphabet, repeat=n):
            packet = encode(rows)
            assert decode(packet) == rows
            for presentation in (('raw', rows), ('grouped', packet)):
                assert tagged_C(tagged_C(presentation)) == presentation
            closure = label_only_join(rows)
            assert set(rows) <= closure
            assert label_only_join(tuple(closure)) == closure
            if len({row[0] for row in rows}) == len(rows):
                assert closure == frozenset(rows)  # unique labels already act as row keys
            cases += 1
    diagonal = ((0, 0, 0), (0, 1, 1))
    crossed = ((0, 0, 1), (0, 1, 0))
    assert marginals(diagonal) == marginals(crossed)
    assert encode(diagonal) != encode(crossed)
    assert label_only_join(diagonal) == label_only_join(crossed)
    assert label_only_join(tuple(label_only_join(diagonal))) != frozenset(diagonal)
    try:
        decode((encode(diagonal)[0], encode(crossed)[1]))
    except ValueError:
        pass
    else:
        raise AssertionError('incompatible parallel views silently accepted')

    for entries in product((-1, 0, 1), repeat=4):
        matrix = (entries[:2], entries[2:])
        assert transpose(transpose(matrix)) == matrix
        assert residual(transpose(matrix)) == scale(residual(matrix), -1)
        assert residual(residual(matrix)) == scale(residual(matrix), 2)
    asymmetric = ((0, 1), (0, 0))
    assert residual(asymmetric) != ((0, 0), (0, 0))

    receipt_path = OWNER/'results/agda-ParallelLabelFibration.json'
    receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces']
    checked = {}
    def visit(module):
        path = OWNER/'agda'/(module.replace('.', '/')+'.agda')
        if not path.exists() or module in checked:
            return
        checked[module] = hashlib.sha256(path.read_bytes()).hexdigest()
        assert checked[module] == receipt['owner_source_inventory_sha256'][path.name].lower()
        for dep in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)', path.read_text(encoding='utf-8'), re.M):
            visit(dep)
    visit('ParallelLabelFibration')
    result = {
        'schema': 'marici.nima.parallel-label-fibration.v1',
        'status': 'lossless_inverse_exists_involution_requires_reverse_rule',
        'exhaustive_ordered_tables': cases,
        'finite_domain': '0..4 rows, two labels, two inputs, two outputs; identities distinguish duplicate triples',
        'lossless_roundtrip': True, 'tagged_involution': True,
        'raw_grouping_is_endomorphism': False,
        'incompatible_parallel_packet_rejected': True,
        'label_marginal_collision': {'first': diagonal, 'second': crossed,
                                     'common_label_only_join': sorted(label_only_join(diagonal))},
        'label_join_is_idempotent_not_involutive': True,
        'unique_labels_recover_support_without_extra_row_ids': True,
        'transpose_residual_control_matrices': 81,
        'residual_conventions': {'return_route': 'R(C(I))=-R(I)', 'iterate_residual': 'R(R(I))=2R(I)',
                                'assumption': 'linear involution on a common additive representation'},
        'local_formal_import_sha256': checked,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Formal individual nested-fiber recovery and tagged single-branch involution; exhaustive paired finite packet tests. No physical residual, generating function or coupling selector.'
    }
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'tables': cases, 'marginal_collision': True,
                      'matrix_controls': 81}))


if __name__ == '__main__':
    main()
