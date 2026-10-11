"""Uniform operation-defect energy for proton and intrinsic belt.

D -> (pi/4) D^sharp D extends Nima's involution generator when D=P-I.
For order-three/nonunitary operations this is a constraint-energy construction,
not a logarithm that must reproduce that operation at time one.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
from check_constraint_energy_accounting import identity, plus, times, compose, adjoint, trace
from check_coupled_six_piece_belt import R, Z, ONE, add, mul, conj, scale, norm, encoded
from check_belt_three_by_twelve import decode
from check_geometric_cycle_reversal import geo
from check_reversed_coefficient_attachment import SOURCE, verify, weight

BASE = Path(__file__).resolve().parents[1]
OMEGA = (R(F(-1,2)),R(F(1,2)))


def scalar_matrix(value,n):
    return {(i,i):value for i in range(n)}


def rational_rank(rows):
    if not rows:
        return 0
    a = [list(map(F,row)) for row in rows]
    pivot = 0
    for j in range(len(a[0])):
        k = next((i for i in range(pivot,len(a)) if a[i][j]),None)
        if k is None:
            continue
        a[pivot],a[k] = a[k],a[pivot]
        q = a[pivot][j]
        a[pivot] = [v/q for v in a[pivot]]
        for i in range(pivot+1,len(a)):
            q = a[i][j]
            if q:
                a[i] = [x-q*y for x,y in zip(a[i],a[pivot])]
        pivot += 1
    return pivot


def real_inverse2(a):
    determinant = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert determinant != 0
    return ((a[1][1]/determinant,-a[0][1]/determinant),
            (-a[1][0]/determinant,a[0][0]/determinant))


def real_mm(a,b):
    return tuple(tuple(sum((x*y for x,y in zip(row,col)),R()) for col in zip(*b)) for row in a)


def add_block(target,block,indices):
    for i,row in enumerate(block):
        for j,value in enumerate(row):
            if value != 0:
                target[indices[i],indices[j]] = (value if isinstance(value,R) else R(value),R())


def main():
    p_raw = SOURCE.read_bytes()
    source = json.loads(p_raw)
    certificate,arrows = verify(source)
    assert certificate['verified']
    objects = source['objects']
    geometry = objects[objects[source['root']]['geometry']]['payload']
    placements = sorted(geometry['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    edges = [r['outer_arrow'] for r in placements]
    points = dict(geo.POINTS)
    for face in ('ABC','ABD','ACD','BCD'):
        points['F_'+face] = geo.mean([points[v] for v in face])
    p_ops = {s:{} for s in ('L','G','N')}
    for row in arrows:
        i = 3*edges.index(row['target'][1])+'xyz'.index(row['target'][2])
        j = 3*edges.index(row['source'][1])+'xyz'.index(row['source'][2])
        value = weight(row)
        p_ops[{'raw':'L','local':'G','aligned':'N'}[row['source'][0]]][i,j] = (R(value[0]),R(value[1]))
    p_cycle,p_modes = {},[]
    for t,row in enumerate(placements):
        X = geo.transpose(tuple(points[v] for v in row['triangle']))
        A = geo.mm(geo.mm(X,geo.C),geo.inv(X))
        add_block(p_cycle,A,list(range(3*t,3*t+3)))
        v = geo.zmv(X,(geo.ONE,geo.OMEGA,geo.zmul(geo.OMEGA,geo.OMEGA)))
        p_modes.append([(R(z[0]),R(z[1])) for z in v])
    rotations = [tuple(tuple(F(v) for v in row) for row in r['rotation']) for r in placements]
    def action(rotation):
        out = {}
        for t,Rt in enumerate(rotations):
            dest = rotations.index(geo.mm(rotation,Rt))
            for a in range(3):
                for b in range(3):
                    if rotation[a][b]:
                        out[3*dest+a,3*t+b] = (R(rotation[a][b]),R())
        return out
    p_generators = [action(geo.rotation(p)) for p in ((1,2,0,3),(3,0,2,1))]
    group = {(0,1,2,3)}
    frontier = list(group)
    while frontier:
        p = frontier.pop()
        for g in ((1,2,0,3),(3,0,2,1)):
            q = geo.compose(g,p)
            if q not in group:
                group.add(q);frontier.append(q)
    assert len(group)==12
    assert times(F(1,12),plus(*(action(geo.rotation(p)) for p in group))) == p_ops['G']

    path = BASE/'results/belt_three_by_twelve_store.json'
    b_raw = path.read_bytes()
    store = json.loads(b_raw)
    d = tuple(F(c['d']) for c in store['coordinates'])
    b_ops = {s:{} for s in ('L','G','N')}
    for row in store['arrows']:
        b_ops[row['stage']][row['target'],row['source']] = scale(1/d[row['source']],decode(row['numerator']))
    z = [decode(c['selected_numerator']) for c in store['coordinates']]
    # The plane restriction of the original triangle cycle is fixed by
    # A r=-r/2-3s/2, A s=r/2-s/2 for v=r+i sqrt(3)s.
    # Numerator coordinates avoid adding arbitrary square-root bases.
    b_cycle = {}
    Cplane = ((R(F(-1,2)),R(F(1,2))),(R(F(-3,2)),R(F(-1,2))))
    for t in range(18):
        X = tuple((z[2*t+i][0],z[2*t+i][1]) for i in range(2))
        A = real_mm(real_mm(X,Cplane),real_inverse2(X))
        add_block(b_cycle,A,[2*t,2*t+1])
    b_rotation = {(((s+1)%3)*12+j,s*12+j):ONE for s in range(3) for j in range(12)}
    assert times(F(1,3),plus(identity(36),b_rotation,compose(b_rotation,b_rotation))) == b_ops['G']
    ambient = json.loads((BASE/'results/coupled_six_piece_belt_store.json').read_text())['record']
    b_triangles = [ambient['triangles'][t] for t in store['triangle_order']]
    result,energy_store = {},{}
    for name,ops,cycle,modes,triangles,groups,generators,metric in [
        ('proton',p_ops,p_cycle,p_modes,[r['triangle'] for r in placements],[[t] for t in range(12)],p_generators,(F(1),)*36),
        ('belt',b_ops,b_cycle,[z[2*t:2*t+2] for t in range(18)],b_triangles,[list(range(6*s,6*s+6)) for s in range(3)],[b_rotation],d)
    ]:
        n = 36
        width = len(modes[0])
        I = identity(n)
        assert compose(compose(cycle,cycle),cycle)==I
        assert compose(adjoint(cycle,metric),cycle)!=I
        mode_columns,local_lines = {},{}
        mode_norms = []
        for t,v in enumerate(modes):
            ns = sum((norm(v[i])/metric[width*t+i] for i in range(width)),R())
            mode_norms.append(ns)
            for i in range(width):
                mode_columns[width*t+i,t] = v[i]
                for j in range(width):
                    value = scale(1/(ns*metric[width*t+j]),mul(v[i],conj(v[j])))
                    if value != Z:
                        local_lines[width*t+i,width*t+j] = value
        defect = plus(cycle,times(-1,scalar_matrix(OMEGA,n)))
        assert compose(defect,mode_columns)=={}
        assert compose(local_lines,local_lines)==local_lines and adjoint(local_lines,metric)==local_lines
        assert trace(local_lines,n)==len(modes)
        phase_energy = compose(adjoint(defect,metric),defect)
        align_energy = {}
        for T in generators:
            assert compose(adjoint(T,metric),T)==I
            assert compose(compose(T,T),T)==I
            delta = plus(T,times(-1,I))
            align_energy = plus(align_energy,compose(adjoint(delta,metric),delta))
        native = plus(phase_energy,align_energy)
        assert compose(local_lines,ops['G'])==compose(ops['G'],local_lines)
        native_return = compose(local_lines,ops['G'])
        assert compose(native_return,native_return)==native_return
        assert compose(native,native_return)=={}
        native_rank = int(trace(native_return,n))
        assert native_rank == (1 if name=='proton' else 6)
        # Native character eigenspaces are one-dimensional per triangle:
        # C has simple cube-root eigenvalues; the plane restriction has both
        # nonreal simple cube-root eigenvalues. This establishes the kernel,
        # not just containment of the displayed return in it.
        # Stitch dimensionless amplitudes only across actual shared edges,
        # inside the declared local groups. No complete graph is inserted.
        seams = [(a,b) for group in groups for a,b in combinations(group,2)
                 if len(set(triangles[a]) & set(triangles[b]))==2]
        B = {}
        for e,(a,b) in enumerate(seams):
            for t,sign in ((a,1),(b,-1)):
                v = modes[t]
                ns = sum((norm(v[i])/metric[width*t+i] for i in range(width)),R())
                for i in range(width):
                    value = scale(sign/(metric[width*t+i]*ns),conj(v[i]))
                    if value != Z:
                        B[e,width*t+i] = value
        incidence = compose(B,mode_columns)
        integer_rows = []
        for e,(a,b) in enumerate(seams):
            row = [0]*len(modes);row[a]=1;row[b]=-1
            integer_rows.append(row)
            for t,x in enumerate(row):
                assert incidence.get((e,t),Z)==(R(x),R())
        incidence_rank = rational_rank(integer_rows)
        assert incidence_rank==len(modes)-len(groups)
        assert len(seams)==(0 if name=='proton' else 21)
        assert compose(B,ops['L'])=={}
        # Each equality row gives a canonical orthogonal mismatch projector.
        # Its Householder reflection is a constructed involutive seam map.
        # Nima's rule gives H_e/pi=P_e, so its contribution to 4H/pi is 4P_e.
        seam_energy = {}
        seam_records = []
        for e,(a,b) in enumerate(seams):
            row = {(0,j):v for (i,j),v in B.items() if i==e}
            sharp = {(j,0):scale(metric[j],conj(v)) for (_,j),v in row.items()}
            dual_norm = sum((metric[j]*norm(v) for (_,j),v in row.items()),R())
            assert dual_norm == 1/mode_norms[a]+1/mode_norms[b]
            projection = times(1/dual_norm,compose(sharp,row))
            assert compose(projection,projection)==projection
            assert adjoint(projection,metric)==projection and trace(projection,n)==1
            reflection = plus(I,times(-2,projection))
            assert compose(reflection,reflection)==I
            # A common rescaling of the source mode changes row normalization
            # but not the mismatch projector or its physical energy operator.
            assert times(4/dual_norm,compose(times(F(1,2),sharp),times(F(1,2),row)))==projection
            seam_energy = plus(seam_energy,times(4,projection))
            seam_records.append({'triangles':[a,b],'entries':[[i,j,encoded(value)] for (i,j),value in sorted(projection.items())]})
        assert trace(seam_energy,n)==4*len(seams)
        local_energy = plus(phase_energy,seam_energy)
        assert compose(local_energy,ops['L'])=={}
        assert adjoint(local_energy,metric)==local_energy
        assert compose(local_energy,ops['G'])==compose(ops['G'],local_energy)
        H = plus(local_energy,align_energy)
        assert adjoint(H,metric)==H and compose(H,ops['N'])=={}
        assert compose(ops['L'],ops['G'])==ops['N']
        # The native-phase kernel plus the incidence equations has dimension
        # equal to number of local groups, and contains im(L) of that rank.
        # Alignment then intersects it in exactly the checked rank-one N.
        assert trace(ops['L'],n)==len(groups) and trace(ops['N'],n)==1
        if name=='belt':
            W,decoder = {},{}
            for entry in store['embedding_entries']:
                target,src = entry['ambient_target'],entry['intrinsic_source']
                value = (R(*map(F,entry['numerator'])),R())
                W[target,src] = scale(1/metric[src],value)
                decoder[src,target] = value
            assert compose(decoder,W)==I
            ambient_H = compose(compose(W,H),decoder)
            assert compose(compose(decoder,ambient_H),W)==H
            assert compose(ambient_H,W)==compose(W,H)
        energy_store[name] = {'metric_denominators':list(map(str,metric)),
                             'operator':'4H/pi in numerator coordinates with inner product diag(1/d); the underlying physical coordinates are orthonormal',
                             'entries':[[i,j,encoded(value)] for (i,j),value in sorted(H.items())],
                             'native_energy_entries':[[i,j,encoded(value)] for (i,j),value in sorted(plus(phase_energy,align_energy).items())],
                             'return_entries':[[i,j,encoded(value)] for (i,j),value in sorted(ops['N'].items())],
                             'seam_projectors':seam_records}
        result[name] = {'native_triangle_cycles':len(modes),'native_alignment_generators':len(generators),
                        'triangle_cycles_unitary_in_retained_metric':False,
                        'phase_kernel_rank':len(modes),'native_phase_plus_alignment_kernel_rank':native_rank,
                        'within_group_shared_edges':len(seams),'independent_amplitude_constraints':incidence_rank,
                        'derived_local_kernel_rank':len(groups),'completed_kernel_rank':1,
                        'energy_rule':'H=(pi/4)*(phase_defects^sharp phase_defects + alignment_defects^sharp alignment_defects) + pi*sum(normalized shared-edge mismatch projectors)',
                        'seam_reflections_involutive':True,'seam_energy_common_mode_scale_invariant':True,
                        'seams':seams,'source_return_recovered':True,
                        'phase_energy_trace_in_4H_over_pi_units':str(trace(phase_energy,n)),
                        'alignment_energy_trace_in_4H_over_pi_units':str(trace(align_energy,n)),
                        'seam_energy_trace_in_4H_over_pi_units':str(trace(seam_energy,n)),
                        'total_energy_trace_in_4H_over_pi_units':str(trace(H,n))}
    # Compatibility with the Nima construction: for a self-adjoint involution
    # P, (P-I)^*(P-I)/4=(I-P)/2 exactly.
    P = {(i,i^1):ONE for i in range(4)}
    delta = plus(P,times(-1,identity(4)))
    assert times(F(1,4),compose(adjoint(delta,(F(1),)*4),delta)) == times(F(1,2),plus(identity(4),times(-1,P)))
    report = {'verification_passed':True,'construction':'uniform positive operation-defect lift; not unique selection or an order-three endpoint interpolation',
              'matches_nima_involution_generator_in_pi_units':True,'carriers':result,
              'new_interface_rule':'Equal coefficients of retained triangle modes across shared edges within declared local groups; use the canonical metric mismatch reflection for each seam.',
              'belt_coordinate_energy_intertwining':True,
              'rest_energy_or_neutron_mass_derived':False,
              'source_sha256':{'proton':sha256(p_raw).hexdigest(),'belt':sha256(b_raw).hexdigest()}}
    (BASE/'results/native_operation_energy_lift.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/native_operation_energy_lift_store.json').write_text(json.dumps({'source_sha256':report['source_sha256'],'carriers':energy_store},indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
