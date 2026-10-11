"""Bridge retained generated geometry to existing phase/seam energy records.

Reconstruct local complex modes from ordered triangle corners, match the native
return and all seam projectors, and check existing occupation controls. Test
centroid-only and electron attachment obstructions rather than filling them by
new weights. Existing character, local grouping and native operations remain
explicit adapter inputs.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json

from check_common_assembly_symmetry import BASE, load_targets, inverse, determinant
from check_relative_geometry_sources import match_target
from check_relative_geometry_mode_selection import select
from assemble_relative_geometry import apply as affine_apply
from check_coupled_six_piece_belt import R, Z, ONE, add, mul, conj, scale, norm, total, encoded
from check_belt_three_by_twelve import decode
from check_belt_operator_inputs import frame
from check_constraint_energy_accounting import identity, plus, times, compose, adjoint, trace
from check_native_operation_energy_lift import geo, real_inverse2, real_mm, OMEGA
from check_reversed_coefficient_attachment import SOURCE, verify


def matrix(entries):
    return {(i,j):decode(value) for i,j,value in entries}


def projector(v, denominators):
    norm_squared = sum((norm(z)/d for z,d in zip(v,denominators)),R())
    assert norm_squared != 0
    return {(i,j):scale(1/(norm_squared*denominators[j]),mul(a,conj(b)))
            for i,a in enumerate(v) for j,b in enumerate(v) if a != Z and b != Z}


def affine_adapter(source_points, target_points):
    d = len(source_points[0])
    base = source_points[0]
    chosen = next(indices for indices in combinations(range(1,len(source_points)),d)
                  if determinant([[source_points[j][i]-base[i] for j in indices] for i in range(d)]))
    M = [[source_points[j][i]-base[i] for j in chosen] for i in range(d)]
    inv = inverse(M)
    T = tuple(tuple(sum((target_points[chosen[k]][a]-target_points[0][a])*inv[k][b] for k in range(d))
                    for b in range(d)) for a in range(d))
    shift = tuple(target_points[0][i]-sum(T[i][j]*base[j] for j in range(d)) for i in range(d))
    def transform(point):
        return tuple(sum(T[i][j]*point[j] for j in range(d))+shift[i] for i in range(d))
    assert all(transform(p)==q for p,q in zip(source_points,target_points))
    return T, transform


def triangle_modes(output, comparison, labels, native_vertices, native_triangles, G):
    p = comparison['vertex_correspondence']
    source_points = [tuple(map(F,v)) for v in output['vertices']]
    target_points = [native_vertices[labels[i]] for i in p]
    T, transform = affine_adapter(source_points,target_points)
    transported = {labels[p[i]]:transform(v) for i,v in enumerate(source_points)}
    metric_pullback = [[sum(T[k][i]*T[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    ratio = metric_pullback[0][0]/F(G[0][0])
    assert all(metric_pullback[i][j] == ratio*F(G[i][j]) for i in range(3) for j in range(3))
    admitted = {frozenset(labels[p[i]] for i in f) for f in output['carrier_facets']}
    modes, ordered_corners = [], []
    for f,a,b in native_triangles:
        face = tuple(f[2:]) if len(labels)==4 else tuple(f[2:].split('_'))
        assert frozenset(face) in admitted and a in face and b in face
        center = tuple(sum(transported[k][i] for k in face)/3 for i in range(3))
        va,vb = transported[a],transported[b]
        v = tuple((center[i]-(va[i]+vb[i])/2,(va[i]-vb[i])/2) for i in range(3))
        # Orientation reversal retains the centroid but conjugates the mode.
        reverse = tuple((center[i]-(va[i]+vb[i])/2,(vb[i]-va[i])/2) for i in range(3))
        assert reverse == tuple(conj(z) for z in v)
        assert projector(v,(F(1),)*3) != projector(reverse,(F(1),)*3)
        modes.append(v)
        ordered_corners.append((center,va,vb))
    assert len(modes)==3*len(admitted)
    return modes, ratio, T, ordered_corners


def reconstruct_seams(modes, denominators, triangles, groups):
    width = len(modes[0])
    reconstructed = {}
    norms = [sum((norm(v[i])/denominators[width*t+i] for i in range(width)),R()) for t,v in enumerate(modes)]
    for group in groups:
        for a,b in combinations(group,2):
            if len(set(triangles[a]) & set(triangles[b])) != 2:
                continue
            row = {}
            for t,sign in ((a,1),(b,-1)):
                for i,z in enumerate(modes[t]):
                    row[0,width*t+i] = scale(sign/(denominators[width*t+i]*norms[t]),conj(z))
            sharp = {(j,0):scale(denominators[j],conj(z)) for (_,j),z in row.items()}
            dual_norm = sum((denominators[j]*norm(z) for (_,j),z in row.items()),R())
            projection = times(1/dual_norm,compose(sharp,row))
            assert compose(projection,projection)==projection
            reconstructed[(a,b)] = projection
    return reconstructed


def native_bridge(targets):
    source = json.loads(SOURCE.read_text())
    certificate,_ = verify(source)
    assert certificate['verified']
    objects = source['objects']
    geometry = objects[objects[source['root']]['geometry']]['payload']
    placements = sorted(geometry['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    p_triangles = [tuple(row['triangle']) for row in placements]
    geometry_path = BASE/'results/four_six_center_cones.json'
    belt_geometry = json.loads(geometry_path.read_text())
    b_labels = [k for k in belt_geometry['belt_scaled_coordinates'] if k!='O']
    intrinsic_path = BASE/'results/belt_three_by_twelve_store.json'
    intrinsic = json.loads(intrinsic_path.read_text())
    ambient_path = BASE/'results/coupled_six_piece_belt_store.json'
    ambient = json.loads(ambient_path.read_text())['record']
    b_triangles = [tuple(ambient['triangles'][t]) for t in intrinsic['triangle_order']]
    energy_path = BASE/'results/native_operation_energy_lift_store.json'
    energy = json.loads(energy_path.read_text())['carriers']
    reports = {}
    for name,source_file,target_name,labels,vertices,triangles in [
        ('proton','relative-proton.json','proton',list('ABCD'),
         {k:tuple(R(x) for x in v) for k,v in geo.POINTS.items()},p_triangles),
        ('belt','mode-neutron.json','neutron_belt',b_labels,
         {k:tuple(R(*x) for x in frame(tuple(map(F,belt_geometry['belt_scaled_coordinates'][k])))) for k in b_labels},b_triangles),
    ]:
        proposed = json.loads((BASE/'inputs'/source_file).read_text())
        output,_ = select(proposed)
        comparison = match_target(output,targets[target_name])
        assert comparison is not None
        ambient_modes,ratio,T,corners = triangle_modes(output,comparison,labels,vertices,triangles,proposed['metric'])
        native = energy[name]
        denominators = tuple(map(F,native['metric_denominators']))
        if name=='proton':
            assert ratio == 1
            modes = ambient_modes
            groups = [[i] for i in range(12)]
        else:
            assert ratio == F(8,3)
            # Existing exact plane decoder: numerator coordinates, metric 1/d.
            full_ambient = [Z]*54
            for slot,t in enumerate(intrinsic['triangle_order']):
                full_ambient[3*t:3*t+3] = ambient_modes[slot]
            assert full_ambient == [decode(v) for v in ambient['collective_vector']]
            z = [Z]*36
            for entry in intrinsic['embedding_entries']:
                i,a = entry['intrinsic_source'],entry['ambient_target']
                coefficient = R(*map(F,entry['numerator']))
                z[i] = add(z[i],scale(coefficient,full_ambient[a]))
            assert z == [decode(c['selected_numerator']) for c in intrinsic['coordinates']]
            assert sum((norm(z[i])/denominators[i] for i in range(36)),R()) == sum((norm(x) for x in full_ambient),R())
            modes = [tuple(z[2*t:2*t+2]) for t in range(18)]
            groups = [list(range(6*s,6*s+6)) for s in range(3)]
        v = tuple(z for mode in modes for z in mode)
        N = projector(v,denominators)
        assert N == matrix(native['return_entries'])
        Hnative, Hfull = matrix(native['native_energy_entries']),matrix(native['entries'])
        assert compose(Hnative,N)=={} and compose(Hfull,N)=={}
        # Rebuild every native local cyclic operation from the retained corners
        # or their exact plane decoder, not from a desired energy spectrum.
        cycle = {}
        width = len(modes[0])
        for t,mode in enumerate(modes):
            if name == 'proton':
                assert all(x.b == 0 for point in corners[t] for x in point)
                X = geo.transpose(tuple(tuple(x.a for x in point) for point in corners[t]))
                A = tuple(tuple(R(x) for x in row) for row in geo.mm(geo.mm(X,geo.C),geo.inv(X)))
            else:
                X = tuple((z[0],z[1]) for z in mode)
                C = ((R(F(-1,2)),R(F(1,2))),(R(F(-3,2)),R(F(-1,2))))
                A = real_mm(real_mm(X,C),real_inverse2(X))
            for i,row in enumerate(A):
                for j,value in enumerate(row):
                    if value:
                        cycle[width*t+i,width*t+j] = (value,R())
        I = identity(36)
        assert compose(compose(cycle,cycle),cycle)==I
        assert compose(adjoint(cycle,denominators),cycle)!=I
        defect = plus(cycle,times(-1,{(i,i):OMEGA for i in range(36)}))
        phase_energy = compose(adjoint(defect,denominators),defect)
        column = {(i,0):z for i,z in enumerate(v) if z != Z}
        assert compose(defect,column)=={} and compose(phase_energy,N)=={}
        # Native alignment acts on the full retained coefficient field, not on
        # one isolated facet centroid. Keep that operation distinction explicit.
        if name == 'proton':
            rotations = [tuple(tuple(F(x) for x in row) for row in record['rotation']) for record in placements]
            alignment_actions = []
            for permutation in ((1,2,0,3),(3,0,2,1)):
                rotation = geo.rotation(permutation)
                action = {}
                for t,Rt in enumerate(rotations):
                    destination = rotations.index(geo.mm(rotation,Rt))
                    for i in range(3):
                        for j in range(3):
                            if rotation[i][j]:
                                action[3*destination+i,3*t+j] = (R(rotation[i][j]),R())
                alignment_actions.append(action)
        else:
            alignment_actions = [{(((s+1)%3)*12+j,s*12+j):ONE for s in range(3) for j in range(12)}]
        alignment_energy = {}
        for action in alignment_actions:
            assert compose(adjoint(action,denominators),action)==I
            delta = plus(action,times(-1,I))
            term = compose(adjoint(delta,denominators),delta)
            fixed = times(F(1,3),plus(I,action,compose(action,action)))
            assert compose(fixed,fixed)==fixed and adjoint(fixed,denominators)==fixed
            assert term == times(3,plus(I,times(-1,fixed)))
            alignment_energy = plus(alignment_energy,term)
        assert plus(phase_energy,alignment_energy)==Hnative
        seams = reconstruct_seams(modes,denominators,triangles,groups)
        stored_seams = {tuple(record['triangles']):matrix(record['entries']) for record in native['seam_projectors']}
        assert seams == stored_seams
        assert plus(Hnative,*(times(4,p) for p in seams.values()))==Hfull
        for P in seams.values():
            assert compose(P,N)=={}
            assert compose(plus(identity(36),times(-1,P)),N)==N
            assert adjoint(P,denominators)==P
        geometric_seams = sum(len(set(a)&set(b))==2 for a,b in combinations(triangles,2))
        reports[name] = {'selected_geometric_facets':len(output['carrier_facets']),
                         'reconstructed_native_triangle_modes':len(modes),
                         'native_coordinate_metric_denominators_retained':True,
                         'native_frame_squared_scale':str(ratio.a),
                         'exact_native_return_reconstructed':True,
                         'native_constraint_energy_on_return':'0',
                         'native_phase_and_alignment_H_reconstructed_exactly':True,
                         'unitary_alignment_energy_equals_three_times_nonfixed_mode_projector':True,
                         'local_cycles_order_three':True,
                         'local_cycles_unitary_in_native_metric':False,
                         'unitary_centroid_motion_cannot_be_identified_with_native_local_cycle_by_isometric_conjugacy':True,
                         'geometric_shared_edges':geometric_seams,
                         'source_grouping_seam_projectors':len(seams),
                         'all_native_seam_projectors_reconstructed_exactly':True,
                         'satisfied_interface_controls_fix_return':True,
                         'centroid_alone_does_not_determine_chirality':True,
                         'added_adapter_data':['native ordered triangle corners and selected character omega',
                                               'native coordinate frame and intrinsic plane decoder where applicable',
                                               'native within-group seam admission and alignment operations'],
                         'not_claimed':'Centroid modes are not identified with native triangle-character modes; equal geometry alone does not select the native grouping or energy law.'}
    assert reports['proton']['source_grouping_seam_projectors']==0
    assert reports['belt']['source_grouping_seam_projectors']==21
    return reports,[SOURCE,geometry_path,intrinsic_path,ambient_path,energy_path]


def electron_gate(targets):
    path = BASE/'inputs/relative-electron.json'
    source = json.loads(path.read_text())
    output,_ = select(source)
    assert match_target(output,targets['electron_pentachoron']) is not None
    vertices = [tuple(map(F,p)) for p in output['vertices']]
    inverse_map = {p:i for i,p in enumerate(vertices)}
    raw = source['generators'][0]
    g = ([[F(x) for x in row] for row in raw['matrix']],tuple(map(F,raw['translation'])))
    permutation = [inverse_map[affine_apply(g,p)] for p in vertices]
    initial = frozenset(output['retained_attachment_interfaces'][0])
    current, history = initial, []
    for _ in range(5):
        current = frozenset(permutation[i] for i in current)
        history.append(sorted(current))
    assert all(frozenset(f)!=initial for f in history[:4]) and current==initial
    return {'status':'blocked_for_fixed_attachment_restriction',
            'five_cycle_preserves_existing_spinor_attachment_cell':False,
            'attachment_cell_orbit_length':5, 'attachment_history':history,
            'missing_map':'Transport from the existing tetrahedral spinor to all five boundary cells, with source-compatible character, metric and energy intertwining.',
            'scope':'No five-cell spinor or electron energy operator inferred from the centroid motion.'}


def main():
    targets,evidence = load_targets()
    bridge,paths = native_bridge(targets)
    # Reuse the already checked occupation certificate; verify exact binding to
    # the current native energy store, rather than trusting a stale receipt.
    occupation_path = BASE/'results/seam_occupation_energy.json'
    occupation = json.loads(occupation_path.read_text())
    assert occupation['verification_passed'] and occupation['source_seams']==21
    native_path = BASE/'results/native_operation_energy_lift_store.json'
    assert occupation['source_sha256'] == sha256(native_path.read_bytes()).hexdigest()
    assert occupation['zero_mixing_occupied_seams']==21
    for path in paths+[occupation_path,BASE/'results/native_operation_energy_lift.json']:
        evidence[str(path.relative_to(BASE.parent))] = sha256(path.read_bytes()).hexdigest()
    for filename in ('relative-proton.json','mode-neutron.json','relative-electron.json'):
        path = BASE/'inputs'/filename
        evidence[str(path.relative_to(BASE.parent))] = sha256(path.read_bytes()).hexdigest()
    report = {'status':'partial_bridge_checked', 'proton_and_belt':bridge,
              'persistent_occupation_link':{'existing_coupling':'epsilon*n + J*(n-S)^2 - g*X; S=c-P',
                  'existing_record_count':21, 'coherent_carrier_constraint_energy':'0',
                  'positive_stored_energy':'21*delta relative to the same inactive-register reference',
                  'zero_mixing_fixture':{'epsilon':'1/4','J':'1/2','kappa':'1','g':'0','stored_increment':'21/4'},
                  'condition':'kappa>delta; the source occupation law and conserved carrier sector are retained assumptions',
                  'new_energy_weights_fitted':False},
              'electron_gate':electron_gate(targets), 'sources':evidence,
              'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
              'conclusion':'Generated full geometric records recover the existing proton/belt local phase modes, collective return and all native seam projectors after explicit native adapters. Complex character alone is not stored rest energy: constraint energy is zero while the existing occupied-register law gives positive vacuum-relative energy. Centroid-only identification and fixed-cell restriction of the electron five-cycle fail.',
              'scope':'No new mass prediction, no derived occupation ontology or stage gaps, and no shared three-species energy closure. Previously failed mass comparisons remain applicable.'}
    (BASE/'results/geometric_phase_energy_bridge.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
