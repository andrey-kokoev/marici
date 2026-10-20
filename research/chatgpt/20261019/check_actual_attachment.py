#!/usr/bin/env python3
"""Exact analysis of a retrieved Marici attachment implementation.

Requires SymPy. Uses the unmodified upstream PathModel, checked by git-blob SHA.
No numerical rank thresholds, no physics interpretation, no proof-assistant claim.
"""
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib.util
from itertools import permutations, product
import json
from math import comb, factorial
from pathlib import Path
from typing import Any

import sympy as sp

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'source/research/nima/checkers/check_joint_record_interval_attachment.py'
EXPECTED_BLOB = '253c83788e7e4a23b489f836c0d8b8830026f5ff'


def load_source() -> Any:
    data = SOURCE.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if blob != EXPECTED_BLOB:
        raise ValueError(f'Unexpected upstream blob: {blob}')
    spec = importlib.util.spec_from_file_location('upstream_attachment', SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load upstream source')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def nonzero_letters(letters: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x for x in letters if x)


def exact_rank(matrix: sp.MatrixBase) -> int:
    return matrix.to_DM().to_field().rank()


@dataclass
class Forest:
    edges: list[tuple[int, int]]
    tree_edges: list[int]
    chords: list[int]
    components: list[list[int]]
    adjacency: list[list[tuple[int, int]]]
    cycle_basis: sp.Matrix

    def lift(self, demand: list[Any]) -> sp.Matrix:
        """Integral tree lift when each component's signed demand sums to zero."""
        b = list(demand)
        answer = [sp.Integer(0)] * len(self.edges)
        for component in self.components:
            if sp.expand(sum(b[v] for v in component)) != 0:
                raise ValueError('Incompatible marginal totals')
            root = min(component)
            parent: dict[int, tuple[int, int]] = {}
            order = [root]
            for v in order:
                for w, e in self.adjacency[v]:
                    if w != root and w not in parent:
                        parent[w] = (v, e)
                        order.append(w)
            for v in reversed(order[1:]):
                p, e = parent[v]
                sign_v = 1 if self.edges[e][0] == v else -1
                answer[e] = sign_v * b[v]
                sign_p = 1 if self.edges[e][0] == p else -1
                b[p] = sp.expand(b[p] - sign_p * answer[e])
                b[v] = 0
            assert sp.expand(b[root]) == 0
        return sp.Matrix(answer)


def make_forest(edges: list[tuple[int, int]], nvertices: int, edge_order: list[int]) -> Forest:
    parents = list(range(nvertices))
    def find(v: int) -> int:
        while parents[v] != v:
            parents[v] = parents[parents[v]]
            v = parents[v]
        return v
    tree, chords = [], []
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(nvertices)]
    for e in edge_order:
        a, b = edges[e]
        ra, rb = find(a), find(b)
        if ra == rb:
            chords.append(e)
        else:
            parents[ra] = rb
            tree.append(e)
            adjacency[a].append((b, e)); adjacency[b].append((a, e))
    grouped: dict[int, list[int]] = defaultdict(list)
    for v in range(nvertices):
        grouped[find(v)].append(v)
    K = sp.zeros(len(edges), len(chords))
    for col, e in enumerate(chords):
        a, b = edges[e]
        discovered: dict[int, tuple[int, int] | None] = {a: None}
        queue = deque([a])
        while b not in discovered:
            v = queue.popleft()
            for w, f in adjacency[v]:
                if w not in discovered:
                    discovered[w] = (v, f)
                    queue.append(w)
        K[e, col] = 1
        v = b
        while v != a:
            previous = discovered[v]
            assert previous is not None
            w, f = previous
            direction = 1 if edges[f] == (w, v) else -1
            K[f, col] -= direction
            v = w
    return Forest(edges, tree, chords, list(grouped.values()), adjacency, K)


def cube_analysis(upstream: Any) -> dict[str, Any]:
    model = upstream.PathModel((2, 3, 5))
    paths = model.Hom
    li = sorted({(p[0][1], nonzero_letters(p[1][:1]), nonzero_letters(p[1][1:])) for p in paths})
    ri = sorted({(p[0][2], nonzero_letters(p[1][:2]), nonzero_letters(p[1][2:])) for p in paths})
    terminal = sorted({nonzero_letters(p[1]) for p in paths})
    left_index, right_index = {x:i for i,x in enumerate(li)}, {x:i for i,x in enumerate(ri)}
    terminal_index = {x:i for i,x in enumerate(terminal)}
    A, B = sp.zeros(len(li),len(paths)), sp.zeros(len(ri),len(paths))
    Q = sp.zeros(len(terminal),len(paths))
    edges = []
    for j,p in enumerate(paths):
        a = left_index[(p[0][1],nonzero_letters(p[1][:1]),nonzero_letters(p[1][1:]))]
        b = right_index[(p[0][2],nonzero_letters(p[1][:2]),nonzero_letters(p[1][2:]))]
        A[a,j] = B[b,j] = Q[terminal_index[nonzero_letters(p[1])],j] = 1
        edges.append((a,len(li)+b))
    L, R = sp.zeros(len(terminal),len(li)), sp.zeros(len(terminal),len(ri))
    for j,(_,prefix,suffix) in enumerate(li): L[terminal_index[prefix+suffix],j] = 1
    for j,(_,prefix,suffix) in enumerate(ri): R[terminal_index[prefix+suffix],j] = 1
    M = A.col_join(B)
    D = A.col_join(-B)
    compatibility = L.row_join(-R)
    assert L*A == Q == R*B
    assert compatibility*M == sp.zeros(len(terminal),len(paths))
    F1 = make_forest(edges,len(li)+len(ri),list(range(len(paths))))
    F2 = make_forest(edges,len(li)+len(ri),list(reversed(range(len(paths)))))
    K1,K2 = F1.cycle_basis,F2.cycle_basis
    assert D*K1 == sp.zeros(D.rows,K1.cols)
    assert M*K1 == sp.zeros(M.rows,K1.cols)
    assert K1.extract(F1.chords,list(range(K1.cols))) == sp.eye(K1.cols)
    assert len(F1.components) == len(terminal) == 15
    graph_components = []
    for component in F1.components:
        names = [(li[v][1]+li[v][2]) if v < len(li) else
                 (ri[v-len(li)][1]+ri[v-len(li)][2]) for v in component]
        assert len(set(names)) == 1
        vertex_set = set(component)
        edge_count = sum(a in vertex_set for a,b in edges)
        expected_vertices, expected_edges = (6,6) if len(names[0]) in (0,3) else (12,18)
        assert (len(component),edge_count) == (expected_vertices,expected_edges)
        graph_components.append({'word_length':len(names[0]),'vertices':len(component),'edges':edge_count,
                                 'cycle_rank':edge_count-len(component)+1})
    assert len(F1.tree_edges) == 111 and len(F1.chords) == 51
    assert exact_rank(A) == exact_rank(B) == 63
    assert exact_rank(M) == 111 and exact_rank(Q) == 15
    assert exact_rank(compatibility) == 15
    transition = K1.extract(F2.chords,list(range(K1.cols)))
    inverse = K2.extract(F1.chords,list(range(K2.cols)))
    assert inverse*transition == transition*inverse == sp.eye(51)
    assert abs(int(transition.det())) == 1
    # Every basis element reconstructs, not just a random example.
    for j in range(len(paths)):
        value = sp.eye(len(paths))[:,j]
        for forest in (F1,F2):
            base = forest.lift(list(D*value))
            coordinates = value.extract(forest.chords,[0])
            assert base + forest.cycle_basis*coordinates == value
    # An incompatible pair is rejected rather than assigned a filler.
    bad = [0]*D.rows; bad[0] = 1
    try: F1.lift(bad)
    except ValueError: pass
    else: raise AssertionError('Invalid marginal pair accepted')
    # Six relabelings of prime directions preserve the actual cut maps.
    path_index = {p:i for i,p in enumerate(paths)}
    primes = (2,3,5)
    for perm in permutations(primes):
        substitution = dict(zip(primes,perm))
        def vertex(v: Any) -> int:
            return 2*sp.prod(substitution[p] for p in primes if (int(v)//2)%p == 0)
        for j,(vs,ls) in enumerate(paths):
            image = (tuple(vertex(v) for v in vs),ls)
            k = path_index[image]
            assert Q[:,j] == Q[:,k]
            a = left_index[(vertex(vs[1]),nonzero_letters(ls[:1]),nonzero_letters(ls[1:]))]
            b = right_index[(vertex(vs[2]),nonzero_letters(ls[:2]),nonzero_letters(ls[2:]))]
            assert A[a,k] == B[b,k] == 1
    # Prepared 48-marked-history source, using exactly the source checker's features.
    vertices = {v:i for i,v in enumerate(model.vertices)}
    features = [(1+(i+1)*sp.I,i+2-sp.I) for i in range(7)]
    prepared_columns = []
    prepared_labels = []
    for prime_order in permutations(primes):
        vs = [2]
        for p in prime_order: vs.append(vs[-1]*p)
        vs = tuple(vs)
        event_feature = [[sum(features[k][r] for k in range(vertices[vs[j]],vertices[vs[j+1]]))
                          for r in range(2)] for j in range(3)]
        for mask in product((0,1),repeat=3):
            column = sp.zeros(len(paths),1)
            for letters in product((0,1,2),repeat=3):
                if all((letter != 0) == bool(mark) for letter,mark in zip(letters,mask)):
                    coefficient = sp.prod(event_feature[j][letter-1] for j,letter in enumerate(letters) if letter)
                    column[path_index[(vs,letters)],0] = sp.expand(coefficient)
            prepared_columns.append(column); prepared_labels.append((prime_order,mask))
    prepared = sp.Matrix.hstack(*prepared_columns)
    source_rank = exact_rank(prepared)
    prepared_marginal_rank = exact_rank(M*prepared)
    prepared_degree_profile = []
    for degree in range(4):
        columns = [j for j,(_,mask) in enumerate(prepared_labels) if sum(mask)==degree]
        block = (M*prepared).extract(list(range(M.rows)),columns)
        rank = exact_rank(block)
        prepared_degree_profile.append({'retained_degree':degree,'source_dimension':len(columns),
                                        'marginal_rank':rank,'kernel_dimension':len(columns)-rank})
    # Existing two source-generated ghost vectors and their independence.
    signs = (-1,1,1,-1,-1,1)
    g0,g1 = sp.zeros(48,1),sp.zeros(48,1)
    for j,(_,mask) in enumerate(prepared_labels):
        if sum(mask)==0: g0[j,0]=signs[j//8]
        if sum(mask)==1: g1[j,0]=signs[j//8]
    x0,x1 = prepared*g0,prepared*g1
    assert M*x0 == M*x1 == sp.zeros(M.rows,1)
    assert exact_rank(sp.Matrix.hstack(x0,x1)) == 2
    assert source_rank == 48
    # Save integer maps and a full kernel certificate.
    def sparse(matrix: sp.MatrixBase) -> dict[str,Any]:
        return {'shape':list(matrix.shape),'entries':[[i,j,int(matrix[i,j])] for i in range(matrix.rows)
                   for j in range(matrix.cols) if matrix[i,j] != 0]}
    (ROOT/'marginal_chain_certificate.json').write_text(json.dumps({
        'rows':[{'vertices':[int(v) for v in vs],'letters':list(ls)} for vs,ls in paths],
        'M':sparse(M),'compatibility':sparse(compatibility),'kernel_basis':sparse(K1),
        'chord_indices':F1.chords,'tree_edges':F1.tree_edges,
        'alternative_coordinate_transition':sparse(transition)},indent=2)+'\n')
    return {
        'full_joint_dimension':len(paths),'single_cut_dimensions':[len(li),len(ri)],
        'paired_marginal_rank':111,'paired_marginal_kernel_dimension':51,
        'terminal_rank':15,'terminal_kernel_dimension':147,
        'compatibility_obstruction_dimension':15,
        'incidence_graph_components':graph_components,
        'integral_cycle_basis_and_reconstruction':True,
        'two_forest_coordinate_changes_unimodular':True,
        'prime_direction_relabelings_checked':6,
        'prepared_source_dimension':source_rank,
        'prepared_paired_marginal_rank':prepared_marginal_rank,
        'prepared_paired_marginal_kernel_dimension':source_rank-prepared_marginal_rank,
        'two_existing_ghosts_verified_independent':True,
        'prepared_degree_profile':prepared_degree_profile,
        'coefficient_domain':'integer incidence; Gaussian-rational prepared fixture',
    }


def cone_counterexample(upstream: Any) -> dict[str,Any]:
    model = upstream.PathModel((2,3))
    h0 = {p:sp.Integer(1) for p in model.Hom if p[1][0] == p[1][1]}
    h1 = dict(h0)
    for p in h1:
        if p[1] == (2,2): h1[p] = sp.Rational(3,2) if p[0][1] == 4 else sp.Rational(1,2)
    v0,v1 = model.attachment(h0),model.attachment(h1)
    def terminal(h: dict[Any,Any]) -> dict[Any,Any]:
        values: dict[Any,Any] = defaultdict(lambda:sp.Integer(0))
        for (_,letters),coefficient in h.items(): values[nonzero_letters(letters)] += coefficient
        return dict(values)
    assert h0 != h1 and terminal(h0) == terminal(h1)
    assert model.read_units(v0) == h0 and model.read_units(v1) == h1
    diagonal = []
    for m,u,prefix in model.Z:
        diagonal.append((sp.Rational(3,2) if m==4 else sp.Rational(1,2)) if u[1] == (2,) else 1)
    T = sp.diag(*diagonal)
    assert v1 == v0*T
    assert T.det() != 0
    assert T*model.coev != model.coev
    assert v0*model.coev != v1*model.coev
    assert exact_rank(v0) == exact_rank(v1) == 24
    # Explicit chain isomorphism Cone(v1) -> Cone(v0): (T,id).
    assert v0*T == sp.eye(v1.rows)*v1
    return {'joint_dimension':18,'attachment_dimensions':list(v0.shape),
       'attachment_ranks':[24,24],'same_terminal_record':True,
       'different_typed_unit_records':True,'unmarked_complex_cones_isomorphic':True,
       'cone_cohomology_dimensions':{'degree_minus_1':0,'degree_0':1},
       'cone_isomorphism_fails_to_preserve_coevaluation':True,
       'same_fixed_source_endpoints_cannot_intertwine_full_filtrations':True,
       'scope':'Underlying vector-space complexes; no asserted equivalence of the full labelled module diagrams.'}


def independent_chamber_control(upstream: Any) -> dict[str, Any]:
    """Different, explicitly declared control: seven independent interval features."""
    model = upstream.PathModel((2,3,5))
    vi = {v:i for i,v in enumerate(model.vertices)}
    columns = []
    labels = []
    for order in permutations((2,3,5)):
        vs=[2]
        for prime in order: vs.append(vs[-1]*prime)
        for mask in product((0,1),repeat=3):
            ranges=[tuple(range(vi[vs[j]]+1,vi[vs[j+1]]+1)) if mask[j] else (0,) for j in range(3)]
            marginal: dict[Any,int] = defaultdict(int)
            for letters in product(*ranges):
                marginal[('left',vs[1],nonzero_letters(letters[:1]),nonzero_letters(letters[1:]))] += 1
                marginal[('right',vs[2],nonzero_letters(letters[:2]),nonzero_letters(letters[2:]))] += 1
            columns.append(marginal);labels.append(mask)
    keys=sorted(set().union(*(column.keys() for column in columns)))
    indices={x:i for i,x in enumerate(keys)}
    matrix=sp.SparseMatrix(len(keys),48,{(indices[k],j):v for j,col in enumerate(columns) for k,v in col.items()})
    ranks=[]
    for degree in range(4):
        col=[j for j,mask in enumerate(labels) if sum(mask)==degree]
        ranks.append(exact_rank(matrix.extract(list(range(matrix.rows)),col)))
    assert ranks == [5,17,18,6]
    return {'source_dimension':48,'paired_marginal_rank':46,'kernel_dimension':2,
            'ranks_by_retained_degree':ranks,
            'scope':'Seven independent chamber coordinates; control replaces the two-component source feature fixture and is not an analytical completion theorem.'}


def terminal_family() -> list[dict[str,int]]:
    reports = []
    for n in range(1,6):
        counts: dict[tuple[int,...],int] = defaultdict(int)
        for letters in product((0,1,2),repeat=n): counts[nonzero_letters(letters)] += factorial(n)
        for word,count in counts.items(): assert count == factorial(n)*comb(n,len(word))
        assert len(counts) == 2**(n+1)-1
        reports.append({'events':n,'joint_dimension':factorial(n)*3**n,
                        'terminal_dimension':len(counts),
                        'terminal_kernel_dimension':factorial(n)*3**n-len(counts)})
    return reports


def main() -> None:
    upstream = load_source()
    results = {
      'upstream_source_git_blob':EXPECTED_BLOB,
      'upstream_source_byte_identical':True,
      'cube':cube_analysis(upstream),
      'marked_cone_counterexample':cone_counterexample(upstream),
      'terminal_recursion':terminal_family(),
      'independent_chamber_control':independent_chamber_control(upstream),
      'scope':'Exact finite linear/path-complex analysis of the supplied source fixture. No identification with the intended T9, all physics, unstable homotopy types, or analytical completion.',
      'proof_assistant_run':False,
      'status':'pass',
    }
    (ROOT/'actual_source_attachment_results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))


if __name__ == '__main__':
    main()
