"""Exact, typed full-field comparisons. No face sewing or PN equation imposed."""
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from math import gcd
from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'strominger/checkers'))
from exact_multiradical import Radical as R


def inverse(x, max_basis=256):
    """Exact multiquadratic inverse by sign conjugation; no prime factoring."""
    if x == 0:
        raise ValueError('zero anchor divisor')
    if set(x.d) <= {1}:
        return R(1 / x.d[1])
    def square_class(a, b):
        g = gcd(abs(a), abs(b))
        return (abs(a)//g)*(abs(b)//g)*(-1 if (a < 0) != (b < 0) else 1)
    coordinates = {1: 0}
    generators = 0
    for k in x.d:
        if k not in coordinates:
            if 2*len(coordinates) > max_basis:
                raise ValueError('anchor field exceeds exact inversion budget')
            bit = 1 << generators
            coordinates.update({square_class(a, k): mask ^ bit for a, mask in list(coordinates.items())})
            generators += 1
    bit = 1
    conjugate = R({k: -v if coordinates[k] & bit else v for k, v in x.d.items()})
    return conjugate * inverse(x * conjugate, max_basis)


def binding_digest(descriptor):
    return sha256(json.dumps(descriptor, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def ports(descriptor):
    result = []
    for carrier in descriptor['carriers']:
        for port in carrier['ports']:
            assert port['dimension'] == len(port['metric'])
            assert all(Fraction(x) > 0 for x in port['metric'])
            result.append((carrier['id'], port))
    assert len({p['id'] for _, p in result}) == len(result)
    return result


def prepare(descriptor, values):
    """values maps labelled patch ports to full coordinate vectors.

    C[target,source] = q_target q_source^dagger H_source.
    A single retained amplitude anchors the common phase of the whole pair.
    """
    ps = ports(descriptor)
    assert set(values) == {p['id'] for _, p in ps}
    for _, p in ps:
        assert len(values[p['id']]) == p['dimension']
    blocks = {}
    anchor = None
    for _, p in ps:
        q = values[p['id']]
        if anchor is None:
            anchor = next(({'port': p['id'], 'coordinate': i, 'value': x.record()}
                           for i, x in enumerate(q) if x != 0), None)
        blocks[p['id']] = {}
        for _, s in ps:
            blocks[p['id']][s['id']] = [
                [(x*y.conj()*Fraction(s['metric'][j])).record()
                 for j, y in enumerate(values[s['id']])] for x in q]
    return {'schema': 'marici.nima.anchored-contact-comparison.v1',
            'bindingDigest': binding_digest(descriptor), 'descriptor': deepcopy(descriptor),
            'blocks': blocks, 'anchor': anchor,
            'scope': 'Full typed source-coordinate comparisons; no identification of fibers, physical measurement or face-sewing equality.'}


def restore(record):
    return R({int(k): Fraction(v) for k, v in record.items()})


def recover(packet, expected_descriptor):
    """Validate complete port coverage and every block, then reconstruct fields."""
    assert packet['schema'] == 'marici.nima.anchored-contact-comparison.v1'
    assert packet['descriptor'] == expected_descriptor
    assert packet['bindingDigest'] == binding_digest(expected_descriptor)
    ps = ports(expected_descriptor)
    by_id = {p['id']: p for _, p in ps}
    blocks = packet['blocks']
    assert set(blocks) == set(by_id)
    for target, row in blocks.items():
        assert set(row) == set(by_id)
        for source, matrix in row.items():
            assert len(matrix) == by_id[target]['dimension']
            assert all(len(r) == by_id[source]['dimension'] for r in matrix)
    anchor = packet['anchor']
    if anchor is None:
        assert all(not restore(x).d for row in blocks.values() for mat in row.values()
                   for r in mat for x in r)
        values = {p['id']: [R() for _ in range(p['dimension'])] for _, p in ps}
    else:
        a, j, value = anchor['port'], anchor['coordinate'], restore(anchor['value'])
        assert a in by_id and type(j) is int and 0 <= j < by_id[a]['dimension']
        assert value != 0
        inv = inverse(value.conj()*Fraction(by_id[a]['metric'][j]))
        values = {p['id']: [restore(row[j])*inv for row in blocks[p['id']][a]] for _, p in ps}
        assert values[a][j] == value
    # Do not trust just the anchor column: check all self and cross comparisons.
    rebuilt = prepare(expected_descriptor, values)
    assert rebuilt['blocks'] == blocks
    return values
