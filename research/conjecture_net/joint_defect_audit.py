"""Source-bound coefficient interfaces at distinct assembly/incidence grades."""
from contextlib import redirect_stdout
from fractions import Fraction as F
from functools import lru_cache
import io
from pathlib import Path
import runpy
import sys
from marked137_endpoint_audit import ROOT, CHECKERS, source_table
from source_overlap_screen import nullspace


def rank(rows):
    return len(rows[0]) - len(nullspace(rows))


def act(rows, vector):
    return [sum((value * coefficient for value, coefficient in zip(row, vector)), F(0)) for row in rows]


def dense(columns, count):
    return [[F(column.get(row, 0)) for column in columns] for row in range(count)]


@lru_cache(maxsize=1)
def source_interfaces():
    old_path = list(sys.path)
    try:
        sys.path.insert(0, str(CHECKERS))
        with redirect_stdout(io.StringIO()):
            boundary = runpy.run_path(str(CHECKERS / 'check_typed_assembly_boundary_adapter.py'))
            incidence = runpy.run_path(str(CHECKERS / 'check_family_incidence_structure.py'))
            rung = source_table()
    finally:
        sys.path[:] = old_path
    # Bind actual leaf order, directed edges and source/target decorations.
    if rung['E'] != incidence['edges'] or any(len(items) != 137 for items in
            (rung['source'], boundary['slots'], incidence['slots'], incidence['ends'])):
        raise ValueError('source slot inventory mismatch')
    tags = {'arrow': 'a', 'state': 's'}
    for index, ((kind, i, j), (kind2, a, b), (u, v), row) in enumerate(zip(
            boundary['slots'], incidence['slots'], incidence['ends'], rung['source'])):
        expected = (kind, incidence['edges'][i], incidence['edges'][j]) if kind == 'arrow' else (kind, i, j)
        if (kind2, a, b) != expected or row.label != ('leaf', index):
            raise ValueError('retained label/order binding failed')
        if row.source != (tags[u[1][0]],) + u[1][1:] or row.target != (tags[v[1][0]],) + v[1][1:]:
            raise ValueError('family-incidence endpoint binding failed')
    vertices = sorted(incidence['adjacency'], key=repr)
    vertex_index = {vertex: i for i, vertex in enumerate(vertices)}
    columns = [{vertex_index[u]: F(1), vertex_index[v]: F(-1)} for u, v in incidence['ends']]
    b = dense(boundary['B2'], 31)
    d = dense(columns, 64)
    reference = rung['m']['values']['d']
    fixed_values = [boundary['add'](row.value, boundary['scale'](-1, reference)) for row in rung['source']]
    fixed = [[matrix[i][j] for matrix in fixed_values] for i in range(2) for j in range(2)]
    return {'boundary_source': boundary, 'incidence_source': incidence, 'rung_source': rung,
            'assembly': b, 'incidence': d, 'fixed_response': fixed, 'fixed_values': fixed_values,
            'slots': boundary['slots'], 'reference': reference}


def response(vector, values, source):
    return source['evaluate']({index: value for index, value in enumerate(vector) if value}, values)


def source_probe(source, slot):
    """Four typed source preparations, uniformly indexed before any kernel test."""
    boundary = source['boundary_source']
    i2, h, k = boundary['I'], boundary['H'], boundary['K']
    kind, left, right = slot
    tables = []
    for left_on, right_on in ((0, 0), (1, 0), (0, 1), (1, 1)):
        x, y, s, t = [i2] * 11, [i2] * 11, [i2] * 4, [i2] * 4
        first, second = (x, y) if kind == 'arrow' else (s, t)
        if left_on:
            first[left] = boundary['add'](i2, h)
        if right_on:
            second[right] = boundary['add'](i2, k)
        tables.append(boundary['residuals'](x, y, s, t, source['reference']))
    return [boundary['add'](boundary['add'](both, neither), boundary['scale'](-1, boundary['add'](only_left, only_right)))
            for neither, only_left, only_right, both in zip(*tables)]


def sparse(vector):
    return {str(index): str(value) for index, value in enumerate(vector) if value}
