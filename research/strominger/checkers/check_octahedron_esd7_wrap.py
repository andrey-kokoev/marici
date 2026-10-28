"""Exact finite wrap audit. No fitted particle counts or viewer mutations."""
from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import math
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research/strominger/results/octahedron-esd7-wrap'
CONTRACT = ROOT / 'research/strominger/contracts/octahedron-esd7-wrap-v1.json'


def det(m):
    a, b, c = m
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def transpose(a):
    return list(map(list,zip(*a)))


def multiply(a,b):
    return [[dot(row,col) for col in zip(*b)] for row in a]


def inverse(a):
    d = det(a)
    return [[F(det([[int(i==column) if j==row else a[i][j] for j in range(3)] for i in range(3)]),d) for column in range(3)] for row in range(3)]


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def mean(vs):
    return tuple(sum(F(v[i]) for v in vs)/len(vs) for i in range(len(vs[0])))


def key(vs):
    return tuple(sorted(tuple(v) for v in vs))


def faces_index(cells):
    out = defaultdict(list)
    for c in cells:
        for f in c['faces']:
            out[key(f)].append(c['id'])
    return out


def planes(cell):
    result = set()
    for face in cell['faces']:
        a, b, c = [v[:3] for v in face[:3]]
        u, v = sub(b, a), sub(c, a)
        n = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
        d = dot(n, a)
        if dot(n, tuple(sum(v[i] for v in cell['vertices']) for i in range(3))) > d*len(cell['vertices']):
            n, d = tuple(-x for x in n), -d
        coefficients = tuple(F(x) for x in (*n,d))
        denominator = math.lcm(*(x.denominator for x in coefficients))
        integers = tuple(int(x*denominator) for x in coefficients)
        g = math.gcd(*integers)
        result.add(tuple(x//g for x in integers))
    return sorted(result)


def polyhedron(ps):
    """All extreme points of a bounded rational intersection, exact Cramer tests."""
    vertices = set()
    for triple in combinations(ps, 3):
        ns, ds = [p[:3] for p in triple], [p[3] for p in triple]
        denominator = det(ns)
        if not denominator:
            continue
        nums = [det([[ds[i] if j == k else ns[i][j] for j in range(3)] for i in range(3)]) for k in range(3)]
        if denominator < 0:
            denominator, nums = -denominator, [-x for x in nums]
        if all(dot(p[:3], nums) <= p[3]*denominator for p in ps):
            vertices.add(tuple(F(x, denominator) for x in nums))
    vs = sorted(vertices)
    if len(vs) < 4 or not any(det([sub(v, vs[0]) for v in triple]) for triple in combinations(vs[1:], 3)):
        return None
    fs = set()
    for p in ps:
        face = key(v for v in vs if dot(p[:3], v) == p[3])
        if len(face) >= 3:
            fs.add(face)
    return vs, sorted(fs)


def volume(vs, fs):
    """Exact convex face ordering and unsigned centroid tetrahedra."""
    centre = mean(vs)
    result = F(0)
    for face in fs:
        fc = mean(face)
        u, v = sub(face[1], face[0]), sub(face[2], face[0])
        normal = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
        omit = next(i for i, x in enumerate(normal) if x)
        axes = [i for i in range(3) if i != omit]
        def compare(a, b):
            x, y = [a[i]-fc[i] for i in axes]
            X, Y = [b[i]-fc[i] for i in axes]
            h, H = (y < 0 or (y == 0 and x < 0)), (Y < 0 or (Y == 0 and X < 0))
            if h != H:
                return 1 if h else -1
            cross = x*Y-y*X
            return -1 if cross > 0 else 1 if cross < 0 else 0
        order = sorted(face, key=cmp_to_key(compare))
        for a, b in zip(order, order[1:]+order[:1]):
            result += abs(det([sub(fc, centre), sub(a, centre), sub(b, centre)]))/6
    return result


AXES = [(1,1,-1,-1), (1,-1,1,-1), (1,-1,-1,1)]
CENTRE = (F(1,2), F(1,2), F(1,2), F(-1,2))
HALF = F(7,2)


def axis_coords(q):
    return tuple(dot(sub(q, CENTRE), a)/(4*HALF) for a in AXES)


def wrap(q, branch=None):
    u, v, w = axis_coords(q)
    su, sv = branch or (1 if u >= 0 else -1, 1 if v >= 0 else -1)
    a, b = su*u, sv*v
    e, f = (1-a-b+w)/2, (1-a-b-w)/2
    beta = [e/2, e/2, f/2, f/2]
    beta[0 if su == 1 else 1] += a
    beta[2 if sv == 1 else 3] += b
    return tuple(2-7*x for x in beta)


def unwrap(q):
    b = tuple((2-F(x))/7 for x in q)
    u, v, w = b[0]-b[1], b[2]-b[3], 2*min(b[:2])-2*min(b[2:])
    return tuple(CENTRE[i]+HALF*sum(t*a[i] for t, a in zip((u,v,w), AXES)) for i in range(4))


def dual(q):
    return tuple(2*c-x for c, x in zip(CENTRE, q))


def main():
    contract = json.loads(CONTRACT.read_text())
    assert contract['obligation'].startswith('Forward realization')
    export = """
import {buildPESymmetricSector} from './research/strominger/pe-symmetric-sector.mjs';
import {buildFoldedFibration} from './research/realization-tower/fibration-folded-process.mjs';
const source=buildPESymmetricSector(3),target=buildFoldedFibration();
const minimal=c=>({id:c.id,role:c.role,kind:c.kind,vertices:c.vertices,faces:c.faces});
console.log(JSON.stringify({source:source.cells.map(minimal),target:target.geometry.map(minimal)}));
"""
    data = json.loads(subprocess.check_output(['node', '--input-type=module', '-e', export], cwd=ROOT, text=True))
    source, target = data['source'], data['target']
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
        assert condition, name
    check('source_native_679_target_native_175', len(source) == 679 and len(target) == 175)
    check('source_P_E_symmetric', Counter(c['role'] for c in source) == {'proton':224,'neutron':231,'electron':224})
    si, ti = faces_index(source), faces_index(target)
    sb, tb = {c['id']: c for c in source}, {c['id']: c for c in target}
    for label, index, byid in [('source', si, sb), ('target', ti, tb)]:
        check(label+'_faces_have_unique_owner_of_each_kind', all(len(ids)<=2 and len({byid[i]['kind'] for i in ids}) == len(ids) for ids in index.values()))
    neighbors = defaultdict(set)
    for ids in si.values():
        if len(ids) == 2:
            a, b = ids
            neighbors[a].add(b); neighbors[b].add(a)
    seen, queue = {source[0]['id']}, deque([source[0]['id']])
    while queue:
        for v in neighbors[queue.popleft()]-seen:
            seen.add(v); queue.append(v)
    check('source_face_connected', len(seen) == len(source))
    source_vertices = key({tuple(v) for c in source for v in c['vertices']})
    target_vertices = set(tuple(v) for c in target for v in c['vertices'])
    target_shapes = {key(c['vertices']) for c in target}
    root = next(c for c in source if c['kind']=='octahedron' and mean(c['vertices']) == CENTRE)
    c2 = tuple(int(2*x) for x in CENTRE)
    native_attempts, best, complete, sample_rejection = 0, 0, 0, None
    for t in target:
        if t['kind'] != 'octahedron':
            continue
        t2 = tuple(int(2*x) for x in mean(t['vertices']))
        for perm, sign in product(permutations(range(4)), (-1,1)):
            def transform(v):
                return tuple((t2[i]+sign*(2*v[perm[i]]-c2[perm[i]]))//2 for i in range(4))
            assert key(transform(v) for v in root['vertices']) == key(t['vertices'])
            mapped = {v: transform(v) for v in source_vertices}
            inside = {v for v, w in mapped.items() if w in target_vertices}
            covered = [c for c in source if all(tuple(v) in inside for v in c['vertices']) and key(mapped[tuple(v)] for v in c['vertices']) in target_shapes]
            best = max(best, len(covered)); native_attempts += 1
            complete += len(covered) == len(source)
            if sample_rejection is None:
                v = next(v for v in source_vertices if v not in inside)
                sample_rejection = {'target_root':t['id'], 'permutation':perm, 'sign':sign, 'source_vertex':v, 'image':mapped[v]}
    check('all_56_times_48_native_root_frames_tested', native_attempts == 56*48)
    check('no_complete_native_whole_cell_frame', complete == 0)
    # Each regular octahedron has precisely these 48 symmetries. A shared
    # tetrahedron/octahedron face has unique target owners of the two kinds;
    # its three fixed vertices determine the next regular solid. No reflected
    # same-side owner is available. Thus no new fold-frame choice occurs.
    basis = [(F(0),F(0),F(0),F(1))] + [tuple(F(int(i==j)) for i in range(4)) for j in range(3)]
    branch_determinants, chart_metrics = [], []
    native_metric = [[1+int(i==j) for j in range(3)] for i in range(3)]
    for branch in product((-1,1), repeat=2):
        origin = wrap(basis[0], branch)
        images = [sub(wrap(q, branch)[:3], origin[:3]) for q in basis[1:]]
        branch_determinants.append(det(images))
        a = transpose(images)
        ai = inverse(a)
        metric = multiply(transpose(ai),multiply(native_metric,ai))
        assert multiply(transpose(a),multiply(metric,a)) == native_metric
        assert det(metric) == 64
        chart_metrics.append({'branch':branch,'forward_matrix':a,'transported_metric':metric})
    check('transported_chart_metrics_preserve_source_norms', len(chart_metrics)==4)
    check('all_four_charts_have_same_nonzero_jacobian', len(set(branch_determinants)) == 1 and abs(branch_determinants[0]) == F(1,4))
    pieces, mapped_faces, source_volume = [], defaultdict(list), F(0)
    fragment_solids = []
    mapped_points, seam_samples = set(), 0
    for cell in source:
        ps = planes(cell)
        before = len(pieces)
        for su, sv in product((-1,1), repeat=2):
            clipped = polyhedron(ps+[(-su,-su,0,-su),(-sv,0,-sv,-sv)])
            if clipped is None:
                continue
            vs, fs = clipped
            vs4 = [(*v, 1-sum(v)) for v in vs]
            images = [wrap(q, (su,sv)) for q in vs4]
            assert all(sum(q)==1 and all(x<=2 for x in q) for q in images)
            assert all(unwrap(w)==q for q,w in zip(vs4,images))
            assert unwrap(wrap(mean(vs4))) == mean(vs4)
            source_volume += volume(vs, fs)
            ident = f"{cell['id']}@{su},{sv}"
            for face in fs:
                mapped_faces[key(wrap((*q,1-sum(q)),(su,sv)) for q in face)].append(ident)
            for q in vs4:
                u,v,_ = axis_coords(q)
                for alt in product((-1,1) if u==0 else (su,), (-1,1) if v==0 else (sv,)):
                    assert wrap(q,alt)==wrap(q,(su,sv))
                    seam_samples += alt != (su,sv)
            mapped_points.update(images)
            pieces.append({'id':ident,'source_id':cell['id'],'role':cell['role'],'branch':[su,sv], 'source_vertices':vs4,'target_vertices':images})
            fragment_solids.append({'id':ident,'source_id':cell['id'],'role':cell['role'],'branch':[su,sv], 'vertices':images, 'faces':[[wrap((*q,1-sum(q)),(su,sv)) for q in face] for face in fs]})
        assert len(pieces)>before
    check('all_source_records_retained', {p['source_id'] for p in pieces} == set(sb))
    check('shared_chart_seams_agree_exactly', seam_samples>0)
    check('fragment_faces_are_manifold', all(len(ids) in (1,2) for ids in mapped_faces.values()))
    boundary = [f for f, ids in mapped_faces.items() if len(ids)==1]
    check('all_boundary_fragments_land_on_ESD7_envelope', all(any(all(v[i]==2 for v in f) for i in range(4)) for f in boundary))
    native_volume = sum(4 if c['kind']=='octahedron' else 1 for c in source)*F(1,6)
    target_volume = sum(4 if c['kind']=='octahedron' else 1 for c in target)*F(1,6)
    check('exact_fragment_partition_volume', source_volume == native_volume)
    check('mapped_volume_exactly_target_volume', source_volume/4 == target_volume)
    check('exact_vertex_and_fragment_centroid_inverse', all(unwrap(wrap(q))==q for q in source_vertices))
    check('conjugated_duality_retains_every_vertex', all(unwrap(wrap(dual(q)))==dual(q) and wrap(dual(unwrap(wrap(dual(q)))))==wrap(q) for q in source_vertices))
    half_nodes = sorted(q for q in mapped_points if q not in target_vertices)
    check('reject_native_node_identification', len(half_nodes)>0)
    check('reject_unit_metric_preservation', any(sum(x*x for x in sub(wrap(f[0]),wrap(f[1]))) != 2 for c in source for f in c['faces']))
    recovered = defaultdict(set)
    for piece in pieces:
        recovered[piece['source_id']].update(unwrap(q) for q in piece['target_vertices'])
    check('original_cell_vertex_sets_recovered_from_tagged_images', all(key(recovered[c['id']])==key(c['vertices']) for c in source))
    def bbox(c):
        return [(min(v[i] for v in c['vertices']),max(v[i] for v in c['vertices'])) for i in range(4)]
    target_info = [(t, bbox(t), planes(t)) for t in target]
    restrictions, by_target_volume, by_source_volume = [], defaultdict(F), defaultdict(F)
    target_roles = defaultdict(set)
    for fragment in fragment_solids:
        fb, fp = bbox(fragment), planes(fragment)
        for t, box, tp in target_info:
            if not all(min(b,d)>max(a,c) for (a,b),(c,d) in zip(fb,box)):
                continue
            clipped = polyhedron(sorted(set(fp+tp)))
            if clipped is None:
                continue
            vs, fs = clipped
            v = volume(vs,fs)
            assert v>0
            points = [(*q,1-sum(q)) for q in vs]
            assert all(wrap(unwrap(q),fragment['branch'])==q for q in points)
            by_target_volume[t['id']] += v
            by_source_volume[fragment['source_id']] += v
            target_roles[t['id']].add(fragment['role'])
            restrictions.append({'source_id':fragment['source_id'],'source_role':fragment['role'], 'chart_fragment':fragment['id'],'branch':fragment['branch'],'target_id':t['id'],'volume':v,'target_vertices':points})
    check('every_native_target_cell_covered', set(by_target_volume)==set(tb))
    expected_target = {c['id']:F(4 if c['kind']=='octahedron' else 1,6) for c in target}
    expected_source = {c['id']:F(4 if c['kind']=='octahedron' else 1,24) for c in source}
    check('exact_full_volume_in_each_target_cell', dict(by_target_volume)==expected_target)
    check('exact_full_mapped_volume_of_each_source_cell', dict(by_source_volume)==expected_source)
    check('intersection_vertices_recover_through_chart_inverse', len(restrictions)>0)
    removed = restrictions[-1]
    damaged_source, damaged_target = dict(by_source_volume), dict(by_target_volume)
    damaged_source[removed['source_id']] -= removed['volume']
    damaged_target[removed['target_id']] -= removed['volume']
    check('deleting_one_restriction_breaks_both_coverage_contracts', damaged_source!=expected_source and damaged_target!=expected_target)
    check('target_single_role_collapse_detected', any(len(r)>1 for r in target_roles.values()))
    poles = [tuple(CENTRE[i]+sign*HALF*a[i] for i in range(4)) for a in AXES for sign in (1,-1)]
    check('opposite_source_poles_map_to_four_corners_and_two_midpoints', len({wrap(q) for q in poles})==6 and sum(q in target_vertices for q in map(wrap,poles))==4)
    report = {
        'status':'bounded-geometry-verified-native-fold-rejected',
        'obligation':contract['obligation'], 'checks':checks,
        'native':{'frames_tested':native_attempts,'complete_frames':complete,'maximum_whole_cell_overlap':best,'sample_rejection':sample_rejection},
        'piecewise_affine':{'source_records':len(source),'source_roles':dict(Counter(c['role'] for c in source)), 'chart_fragments':len(pieces),'split_source_cells':sum(n>1 for n in Counter(p['source_id'] for p in pieces).values()),'boundary_fragment_faces':len(boundary),'internal_fragment_faces':sum(len(ids)==2 for ids in mapped_faces.values()),'source_volume':source_volume,'target_volume':target_volume,'chart_determinants':branch_determinants,'chart_metrics':chart_metrics,'non_native_target_vertices':len(half_nodes),'non_native_vertex_example':half_nodes[0],'seam_comparisons':seam_samples,'pole_images':list(zip(poles,map(wrap,poles)))},
        'common_refinement':{'restriction_records':len(restrictions),'native_target_cells':len(by_target_volume),'retained_source_cells':len(by_source_volume),'target_role_mixture_histogram':dict(Counter('+'.join(sorted(r)) for r in target_roles.values())),'deleted_restriction_hostile':{'source_id':removed['source_id'],'target_id':removed['target_id'],'missing_volume':removed['volume']}},
        'scope':'Four-chart piecewise-affine homeomorphism onto the ESD7 envelope with a labelled common refinement over its native cells, not a whole-cell isometric fold. Source-cell and fragment records retained. No phase/witness transport, physical modes, isotope identification or stability theorem.',
        'input_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in [CONTRACT,Path(__file__),ROOT/'research/strominger/pe-symmetric-sector.mjs',ROOT/'research/realization-tower/fibration-folded-process.mjs',ROOT/'research/realization-tower/normal-ray-model.mjs']}
    }
    OUT.mkdir(parents=True,exist_ok=True)
    encode = lambda x: str(x) if isinstance(x,F) else (_ for _ in ()).throw(TypeError(type(x).__name__))
    (OUT/'verification.json').write_text(json.dumps(report,indent=2,default=encode)+'\n')
    (OUT/'retained-fragments.json').write_text(json.dumps(pieces,indent=2,default=encode)+'\n')
    (OUT/'native-cell-restrictions.json').write_text(json.dumps(restrictions,indent=2,default=encode)+'\n')
    print(json.dumps(report,indent=2,default=encode))


if __name__=='__main__':
    main()
