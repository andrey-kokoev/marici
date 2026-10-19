"""Exact nonparallel modes under the INHERITED squared-mismatch functional."""
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve()
FIXTURE = ROOT / 'research/strominger/inputs/nonparallel-spin-loom-v1.json'
PACKET = ROOT / 'research/strominger/nonparallel-spin-loom.md'
MODEL = ROOT / 'research/strominger/scc-models/nonparallel-spin-loom-v1.json'
COMPILER = ROOT / 'research/aspect/scc/categorical_compiler.py'
OUT = ROOT / 'research/strominger/results/nonparallel-spin-loom'
f = json.loads(FIXTURE.read_text(encoding='utf-8'))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


g = load('nonparallel_native_spin', ROOT / f['arithmetic_constructor'])
compiler = load('nonparallel_scc', COMPILER)
A, ZERO, ONE, I = g.A, g.ZERO, g.ONE, g.I
mm, adj, add, scale = g.mm, g.adj, g.add, g.scale


def eye(n):
    return tuple(tuple(A(i == j) for j in range(n)) for i in range(n))


def decode(matrix):
    return tuple(tuple(A(tuple(F(v.get(str(i), '0')) for i in range(16))) for v in row) for row in matrix)


def encode(value):
    if isinstance(value, A):
        return value.record()
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def minus(a, b):
    return add(a, scale(A(-1), b))


def act(m, v):
    return tuple(g.dot(row, v) for row in m)


def norm(v):
    return sum((x.flip(8) * x for x in v), ZERO)


def trace(m):
    return sum((m[i][i] for i in range(len(m))), ZERO)


def problem(cells, U):
    position = {cell: i for i, cell in enumerate(cells)}
    rows = []
    for i, j in combinations(cells, 2):
        for a in range(2):
            row = [ZERO] * (2 * len(cells))
            for b in range(2):
                row[2 * position[i] + b] = -U[i, j][a][b]
                row[2 * position[j] + b] = A(a == b)
            rows.append(tuple(row))
    C = tuple(rows)
    return C, mm(adj(C), C) if C else scale(ZERO, eye(2 * len(cells)))


def witness(cells, U, P):
    column = next(j for j in range(len(P)) if P[j][j] != ZERO)
    v = tuple(row[column] for row in P)
    site = {str(cell): v[2*i:2*i+2] for i, cell in enumerate(cells)}
    seams = []
    for i, j in combinations(cells, 2):
        moved = act(U[i,j], site[str(i)])
        mismatch = tuple(x-y for x,y in zip(site[str(j)], moved))
        seams.append({'source':i, 'target':j, 'mismatch':mismatch, 'squared_cost':norm(mismatch)})
    return {'vector':v, 'cell_components':site, 'squared_norm':norm(v),
            'seams':seams, 'total_squared_mismatch':sum((s['squared_cost'] for s in seams),ZERO)}


def run(report):
    source = json.loads((ROOT / f['source_receipt']).read_text(encoding='utf-8'))
    checks = report['checks']

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)

    check('source_receipt_passed', source['status'] == 'pass' and all(source['checks'].values()))
    check('every_transitive_source_pin_current', all(sha256((ROOT/p).read_bytes()).hexdigest() == h for p,h in source['source_sha256'].items()))
    k = g.S2 * g.S3 / 3
    check('certified_positive_root_ordering_bounds', k*k == A(2)/3 and F(4,5)**2 < F(2,3) < F(5,6)**2)
    expressions = {'0':ZERO, '2':A(2), '1-kappa':A(1)-k, '3-kappa':A(3)-k,
        '2+2*kappa':A(2)+2*k, '3-3*kappa':A(3)-3*k, '3+2*kappa':A(3)+2*k,
        '4-3*kappa':A(4)-3*k, '4+2*kappa':A(4)+2*k}
    results = []
    for chiral in source['chiralities']:
        chirality = chiral['chirality']
        prefix = f'chirality_{chirality}'
        U = {(r['source'],r['target']):decode(r['map']) for r in chiral['edge_maps']}
        check(prefix + '_all_inherited_edges_unitary', all(mm(adj(u),u) == I for u in U.values()))
        cases = []
        full_ground = full_H = None
        for n in f['group_sizes']:
            spectral_data = [(expressions[code], multiplicity) for code,multiplicity in f['predicted_spectra'][str(n)]]
            for cells in combinations(range(5), n):
                name = prefix + '_' + ''.join(map(str,cells))
                C,H = problem(cells,U)
                E = eye(2*n)
                check(name + '_actual_mismatch_form_Hermitian', adj(H) == H)
                total = scale(ZERO,E)
                operators = []
                for index,(value,multiplicity) in enumerate(spectral_data):
                    P = E
                    for j,(other,_) in enumerate(spectral_data):
                        if j != index:
                            P = scale((value-other).inverse(), mm(P,minus(H,scale(other,E))))
                    check(name + f'_spectral_projector_{index}', adj(P) == P and mm(P,P) == P and mm(H,P) == scale(value,P) and trace(P) == multiplicity)
                    total = add(total,P)
                    operators.append({'eigenvalue':value,'multiplicity':multiplicity,'projector':P})
                check(name + '_full_spectrum_complete', total == E)
                ground = operators[0]
                w = witness(cells,U,ground['projector'])
                check(name + '_nonzero_pattern_has_predicted_cost', w['squared_norm'] != ZERO and act(H,w['vector']) == tuple(ground['eigenvalue']*x for x in w['vector']) and w['total_squared_mismatch'] == ground['eigenvalue']*w['squared_norm'])
                cases.append({'cells':cells,'constraint_matrix':C,'H':H,'spectral_decomposition':operators,'ground_pattern':w})
                if n == 5:
                    full_ground,full_H = ground['projector'],H
        constant = tuple(tuple(A(F(1,5)) if i%2 == j%2 else ZERO for j in range(10)) for i in range(10))
        complement = minus(full_ground,constant)
        doublets = {}
        for name,P in [('constant',constant),('complementary',complement)]:
            check(prefix + '_' + name + '_orthogonal_ground_doublet', adj(P)==P and mm(P,P)==P and trace(P)==2 and mm(full_H,P)==scale(A(4)-3*k,P))
            W = tuple(tuple(g.S5*row[8+j] for j in range(2)) for row in P)
            check(prefix + '_' + name + '_faithful_attachment_encoding', mm(adj(W),W)==I and mm(W,adj(W))==P)
            check(prefix + '_' + name + '_every_cell_gets_faithful_scaled_doublet', all(mm(adj(W[2*i:2*i+2]),W[2*i:2*i+2])==scale(A(F(1,5)),I) for i in range(5)))
            patterns=[]
            for j in range(2):
                v=tuple(row[j] for row in W)
                check(prefix + '_' + name + f'_normalized_pattern_{j}', norm(v)==ONE and act(full_H,v)==tuple((A(4)-3*k)*x for x in v))
                patterns.append({'vector':v,'cell_components':{str(i):v[2*i:2*i+2] for i in range(5)},'squared_norm':norm(v)})
            doublets[name]={'projector':P,'isometric_encoding':W,'basis_patterns':patterns}
        check(prefix + '_neither_doublet_is_silently_selected', mm(constant,complement)==scale(ZERO,eye(10)) and add(constant,complement)==full_ground)
        frames={int(i):decode(value) for i,value in chiral['independent_frame_changes'].items()}
        changed={(i,j):mm(frames[j],mm(u,adj(frames[i]))) for (i,j),u in U.items()}
        _,new_H=problem(tuple(range(5)),changed)
        G=tuple(tuple(frames[i//2][i%2][j%2] if i//2==j//2 else ZERO for j in range(10)) for i in range(10))
        transported_H=mm(G,mm(full_H,adj(G)))
        new_ground=mm(G,mm(full_ground,adj(G)))
        check(prefix + '_rebuilt_form_is_frame_covariant', new_H==transported_H)
        check(prefix + '_full_lowest_space_is_frame_covariant', mm(new_H,new_ground)==scale(A(4)-3*k,new_ground) and trace(new_ground)==4)
        value=lambda matrix:sha256(json.dumps(encode(matrix),sort_keys=True).encode()).hexdigest()
        d={'id':prefix+'_nonparallel_covariance','objects':[{'id':'changed_10_component_fiber'}],
            'arrows':[{'id':side,'source':'changed_10_component_fiber','target':'changed_10_component_fiber','evaluated_map':encode(matrix),'map_token':value(matrix)} for side,matrix in [('rebuilt',new_H),('transported',transported_H)]],
            'cells':[{'id':'source_frame_covariance','routes':[['rebuilt'],['transported']],'threshold':'exact_zero'}], 'obstructions':[],'claims':[]}
        compiled=compiler.compile_diagram(d)
        check(prefix+'_SCC_evaluated_covariance_cell',compiled['passed'])
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/(prefix+'-diagram.json')).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
        results.append({'chirality':chirality,'cases':cases,'full_group_doublets':doublets,'frame_changed_H':new_H,'frame_changed_ground_projector':new_ground,'compiled_covariance':compiled})
    report.update({'classification':'source_nonparallel_patterns_survive_all_available_fitting_groups',
        'kappa':k,'chiralities':results,'case_count':sum(len(r['cases']) for r in results),
        'disposition':'Nonparallel lowest patterns survive all source fitting groups. Closing seams gives positive cost, not a forbidden configuration; full group retains two degenerate doublets.',
        'nonpromotion':'Inherited dimensionless mismatch functional, not physical bonding energy or an exclusion budget. Five is the input complex size, not a maximum coherent region. No unified P/N/E identification.'})


def main():
    paths=[HERE,FIXTURE,PACKET,MODEL,ROOT/f['source_receipt'],ROOT/f['arithmetic_constructor'],COMPILER]
    report={'schema':'marici.strominger.nonparallel-spin-loom.verification.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'checks':{},'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:
        run(report)
        report['status']='pass'
    except Exception as error:
        report.update(status='fail',error=repr(error))
        raise
    finally:
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/'verification.json').write_text(json.dumps(encode(report),indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'status':report['status'],'classification':report.get('classification','execution_failure'),'checks':len(report['checks']),'cases':report.get('case_count'),'receipt':(OUT/'verification.json').relative_to(ROOT).as_posix()}))


if __name__=='__main__':
    main()
