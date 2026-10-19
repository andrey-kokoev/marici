"""Source-bound spin fittings: distinguish covariant coherence from flatness."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve()
FIXTURE = ROOT / 'research/strominger/inputs/source-spin-loom-v1.json'
PACKET = ROOT / 'research/strominger/source-spin-loom.md'
MODEL = ROOT / 'research/strominger/scc-models/source-spin-loom-v1.json'
COMPILER = ROOT / 'research/aspect/scc/categorical_compiler.py'
OUT = ROOT / 'research/strominger/results/source-spin-loom'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


f = json.loads(FIXTURE.read_text(encoding='utf-8'))
geo = load('source_loom_spin', ROOT / f['interface_constructor'])
compiler = load('source_loom_scc', COMPILER)
A, I, ZERO = geo.A, geo.I, geo.ZERO
mm, adj, add, scale, rank = geo.mm, geo.adj, geo.add, geo.scale, geo.rank


def eye(n):
    return tuple(tuple(A(i == j) for j in range(n)) for i in range(n))


def act(matrix, vector):
    return tuple(geo.dot(row, vector) for row in matrix)


def minus(left, right):
    return add(left, scale(A(-1), right))


def encode(value):
    if isinstance(value, A):
        return value.record()
    if isinstance(value, dict):
        return {key: encode(v) for key, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def digest(value):
    return sha256(json.dumps(encode(value), sort_keys=True).encode()).hexdigest()


def loop(U, i, j, k):
    return mm(adj(U[i, k]), mm(U[j, k], U[i, j]))


def tetra(U, i, j, k, l):
    left = mm(loop(U, i, k, l), loop(U, i, j, k))
    right = mm(loop(U, i, j, l), mm(adj(U[i, j]), mm(loop(U, j, k, l), U[i, j])))
    naive = mm(loop(U, i, j, l), loop(U, j, k, l))
    return left, right, naive


def diagram(name, base, left, right):
    return {'id': name, 'objects': [{'id': f'fiber_{base}'}],
        'arrows': [{'id': side, 'source': f'fiber_{base}', 'target': f'fiber_{base}',
                    'map_token': digest(value), 'evaluated_map': encode(value)} for side, value in (('left', left), ('right', right))],
        'cells': [{'id': 'covariant_tetrahedron', 'kind': 'evaluated_based_comparison', 'routes': [['left'], ['right']], 'threshold': 'exact_zero'}],
        'obstructions': [], 'claims': [],
        'scope': 'Actual evaluated source spin-fold comparisons; no independently asserted higher-cell equivalence'}


def run(report):
    checks = report['checks']

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)

    source = json.loads((ROOT / f['source']).read_text(encoding='utf-8'))
    previous = json.loads((ROOT / f['prior_receipt']).read_text(encoding='utf-8'))
    vertices = [tuple(A(x) for x in v) + (ZERO,) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    vertices.append((ZERO, ZERO, ZERO, geo.S5))
    center = (ZERO, ZERO, ZERO, geo.S5 / 5)
    basis = tuple(zip(*(geo.sub(vertices[j], vertices[4]) for j in range(4))))
    check('canonical_frame_pulls_back_actual_source_metric', mm(adj(basis), basis) == tuple(tuple(A(x) for x in row) for row in source['metric']))
    check('source_has_one_five_cycle_generator', len(source['generators']) == 1 and source['seeds'] == [{'point':[0,0,0,0], 'role':'attachment_pole'}])
    rotation = eye(4)
    for j in range(1,5):
        n = tuple(x / (2 * geo.S2) for x in geo.sub(vertices[0], vertices[j]))
        reflection = tuple(tuple(A(i == k) - 2 * n[i] * n[k] for k in range(4)) for i in range(4))
        rotation = mm(reflection, rotation)
    generator = source['generators'][0]
    check('actual_source_affine_generator_is_intertwined', mm(rotation, basis) == mm(basis, tuple(tuple(A(x) for x in row) for row in generator['matrix'])) and act(basis, tuple(A(x) for x in generator['translation'])) == geo.sub(vertices[0], vertices[4]))
    check('rotation_cycles_all_five_retained_vertices', all(act(rotation, geo.sub(v, center)) == geo.sub(vertices[(i+1)%5], center) for i, v in enumerate(vertices)))
    normals = [tuple(-geo.S5 * x / 4 for x in geo.sub(v, center)) for v in vertices]
    check('geometric_normals_have_native_simplex_Gram_matrix', all(geo.dot(normals[i], normals[j]) == (A(1) if i == j else A(-1)/4) for i in range(5) for j in range(5)))
    results = []
    for chirality in (1, -1):
        tag = f'chirality_{chirality}'
        U, cosine = {}, geo.S2 * geo.S3 / 4
        for i, j in combinations(range(5), 2):
            k = tuple(x / (2 * cosine) for x in geo.chiral(geo.wedge(normals[i], normals[j]), chirality))
            u = add(scale(cosine, I), scale(-geo.CI, geo.pauli(k)))
            U[i, j], U[j, i] = u, adj(u)
            check(tag + f'_unitary_edge_{i}{j}', mm(adj(u), u) == I and u[0][0]*u[1][1]-u[0][1]*u[1][0] == 1)
        loops = {}
        for triple in combinations(range(5), 3):
            h = loop(U, *triple)
            defect = minus(h, I)
            name = ''.join(map(str, triple))
            check(tag + '_unitary_curved_loop_' + name, mm(adj(h), h) == I and rank(defect) == 2)
            loops[name] = {'base': triple[0], 'map': h, 'fixed_state_defect': defect, 'fixed_dimension': 2-rank(defect)}
        inherited = next(r for r in previous['chirality_results'] if r['chirality'] == chirality)
        check(tag + '_loop_matches_exact_prior_interface_receipt', encode(loops['012']['map']) == inherited['loop_matrix'])
        check(tag + '_prior_loop_trace_recovered', loops['012']['map'][0][0] + loops['012']['map'][1][1] == 2 * geo.S2 * geo.S3 / 9)
        frames = {i: U[i, 0] if i else I for i in range(5)}
        changed = {(i,j): mm(frames[j], mm(u, adj(frames[i]))) for (i,j),u in U.items()}
        check(tag + '_rooted_frame_tree_edges_become_identity', all(changed[0,i] == I for i in range(1,5)))
        check(tag + '_all_loop_maps_transport_by_their_own_base', all(loop(changed,*t) == mm(frames[t[0]], mm(loop(U,*t), adj(frames[t[0]]))) for t in combinations(range(5),3)))
        cells, naive_ranks = {}, Counter()
        for quad in combinations(range(5), 4):
            i,j,k,l = quad
            name = ''.join(map(str, quad))
            left,right,naive = tetra(U,*quad)
            defect = minus(left,right)
            check(tag + '_properly_based_tetrahedron_' + name, defect == scale(A(0),I))
            direct = mm(U[k,l], mm(U[j,k], U[i,j]))
            check(tag + '_same_complete_triple_transport_' + name, mm(U[i,l],left) == direct == mm(U[i,l],right))
            gl,gr,gn = tetra(changed,*quad)
            check(tag + '_tetrahedral_frame_covariance_' + name, gl == gr == mm(frames[i], mm(left,adj(frames[i]))))
            naive_rank = rank(minus(left,naive))
            naive_ranks[naive_rank] += 1
            if i == 0:
                check(tag + '_root_frame_removes_naively_unbased_defect_' + name, gl == gn)
            d = diagram(tag + '_' + name,i,left,right)
            compiled = compiler.compile_diagram(d)
            check(tag + '_compiled_actual_tetrahedron_' + name, compiled['passed'])
            cells[name] = {'base':i, 'left':left, 'right':right, 'defect':defect,
                'complete_triple_transport': direct, 'naive_unbased_right':naive,
                'naive_defect_rank':naive_rank, 'frame_changed_naive_defect':minus(gl,gn), 'compiled_cell':compiled}
            OUT.mkdir(parents=True, exist_ok=True)
            (OUT / (tag + '_' + name + '-diagram.json')).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
        left,right,_ = tetra(U,0,1,2,3)
        corrupted = scale(A(-1),left)
        check(tag + '_independent_face_flip_is_rank_two_source_corruption', rank(minus(corrupted,right)) == 2 and not compiler.compile_diagram(diagram('corrupted',0,corrupted,right))['passed'])
        plans = [('two_fittings',2,[(0,1)],2),('open_three',3,[(0,1),(1,2)],2),
            ('triangle',3,[(0,1),(1,2),(0,2)],0),('open_four',4,[(0,1),(1,2),(2,3)],2),
            ('tetrahedron_parallel',4,list(combinations(range(4),2)),0),
            ('five_chain',5,[(0,1),(1,2),(2,3),(3,4)],2),
            ('five_cell_parallel',5,list(combinations(range(5),2)),0)]
        parallel = {}
        for name,n,links,expected in plans:
            rows = []
            for i,j in links:
                for a in range(2):
                    row = [ZERO] * (2*n)
                    for b in range(2):
                        row[2*i+b] = -U[i,j][a][b]
                        row[2*j+b] = A(a == b)
                    rows.append(row)
            dimension = 2*n - rank(rows)
            check(tag + '_parallel_dimension_' + name, dimension == expected)
            parallel[name] = {'fittings':n, 'links':links, 'constraints':rows, 'dimension':dimension}
        results.append({'chirality':chirality,'edge_maps':[{'source':i,'target':j,'map':u} for (i,j),u in U.items()],
            'face_loops':loops,'tetrahedra':cells,'naive_defect_rank_census':dict(naive_ranks),
            'independent_frame_changes':frames,'parallel_matching':parallel})
    report.update({'classification':'source_higher_cells_fill_despite_parallel_state_obstruction',
        'chiralities':results,'source_vertices':vertices,'source_frame_basis':basis,
        'scientific_disposition':'In this existing source sector, curved loop transport and loss of globally parallel assignments coexist with fully coherent based tetrahedral comparisons. Do not identify curvature/flatness failure with a higher-coherence obstruction.',
        'native_scope':'Existing five-cell geometric spin interface only; no common P/N/E fittings, native144 replacement, molecular stability or size limit derived.'})


def main():
    paths = [HERE,FIXTURE,PACKET,MODEL,ROOT/f['source'],ROOT/f['interface_constructor'],ROOT/f['prior_receipt'],COMPILER]
    report = {'schema':'marici.strominger.source-spin-loom.verification.v1','recorded_at':datetime.now(timezone.utc).isoformat(),
              'checks':{},'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:
        run(report)
        report['status'] = 'pass'
    except Exception as error:
        report.update(status='fail',error=repr(error))
        raise
    finally:
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/'verification.json').write_text(json.dumps(encode(report),indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'status':report['status'],'classification':report.get('classification','execution_failure'),
                          'checks':len(report['checks']),'receipt':(OUT/'verification.json').relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
