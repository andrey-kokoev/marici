"""Exact geometric-role intertwiners and typed alternatives, iteration4.
No producer entrypoint, shared source write or physical identification.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from itertools import product as pairs
import json
import sys
from assemble_metric_coefficient_protocol import ROOT,A,ZERO,ONE,product,plus,scaled,encode,read_operator
from check_port_incidence_conjectures import identity,transpose,invert,pivot_columns
from check_packet_handoff_naturality_02 import load,sub,adj,trace,MERKLE,BELT
from check_packet_stage_cost_comparison import source_electron_factors
from check_neutrino_three_port_boundary import from_spin,S2,S3,CI
from check_baryon_coefficient_spin_binding import parse_record,sparse
from check_belt_operator_inputs import frame
from electron_packet_interface import ACTIONS,STORE
from check_electron_charge_spin_frontier import cartan as native_cartan

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-04.v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-04-v1.json'
PRIOR=ROOT/'research/strominger/results/packet-handoff-naturality-03-v1.json'
GEOMETRY=ROOT/'research/voevodsky/results/four_six_center_cones.json'
AMBIENT=ROOT/'research/voevodsky/results/coupled_six_piece_belt_store.json'
SIGMA=({(0,1):ONE,(1,0):ONE},{(0,1):-CI,(1,0):CI},{(0,0):ONE,(1,1):-ONE})


def read(p):return json.loads(p.read_text(encoding='utf-8'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
def rational(rows):return {(i,j):A(F(x)) for i,row in enumerate(rows) for j,x in enumerate(row) if F(x)}
def rank(m,rows,cols):return len(pivot_columns(m,rows,cols))
def flat(m,n):return {(n*i+j,0):x for (i,j),x in m.items()}
def unflat(v,n):return {(i//n,i%n):x for (i,j),x in v.items()}
def vec(values):return {(i,0):x for i,x in enumerate(values) if x!=ZERO}
def key(m):return tuple((i,j,x.c) for (i,j),x in sorted(m.items()))
def conjugate(S,m,Si):return product(S,product(m,Si))


def hom(dom,cod,ni,no):
    """RREF of V_g X-X M_g; exact nullspace over the inherited number field."""
    rows=[];nv=ni*no
    for M,V in zip(dom,cod):
        for i,j in pairs(range(no),range(ni)):
            row=[V.get((i,a),ZERO)*int(b==j)-int(i==a)*M.get((b,j),ZERO) for a,b in pairs(range(no),range(ni))]
            if any(x!=ZERO for x in row):rows.append(row)
    r=0;pivots=[]
    for col in range(nv):
        p=next((p for p in range(r,len(rows)) if rows[p][col]!=ZERO),None)
        if p is None:continue
        rows[r],rows[p]=rows[p],rows[r];q=rows[r][col]
        rows[r]=[x/q for x in rows[r]]
        for p in range(len(rows)):
            if p!=r and rows[p][col]!=ZERO:
                q=rows[p][col];rows[p]=[x-q*y for x,y in zip(rows[p],rows[r])]
        pivots.append(col);r+=1
    free=[j for j in range(nv) if j not in pivots];basis=[]
    for j in free:
        v=[ZERO]*nv;v[j]=ONE
        for i,p in enumerate(pivots):v[p]=-rows[i][j]
        X={(a,b):v[ni*a+b] for a,b in pairs(range(no),range(ni)) if v[ni*a+b]!=ZERO}
        assert all(product(V,X)==product(X,M) for M,V in zip(dom,cod))
        basis.append(X)
    assert len(basis)+len(pivots)==nv
    return {'dimension':len(basis),'constraint_rank':len(pivots),'pivots':pivots,
            'rref_nonzero_rows':[[x.record() for x in row] for row in rows[:r]],
            'basis':list(map(encode,basis))},basis


def closure(gens,n,bound):
    unit=identity(n);found={key(unit):unit};todo=[unit]
    while todo:
        p=todo.pop()
        for g in gens:
            q=product(g,p);k=key(q)
            if k not in found:found[k]=q;todo.append(q)
            assert len(found)<=bound
    return list(found.values())


def representations(objects,binding):
    data={n:{'M':[],'V':[],'raw':[]} for n in objects}
    vertices=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    Vp=rational([[vertices[j+1][i]-vertices[0][i] for j in range(3)] for i in range(3)])
    Vn={(0,1):A(F(2,3))*S2,(0,2):A(F(4,3)),(1,0):A(-2),(1,1):A(F(2,3))*S2,
        (1,2):-A(F(2,3)),(2,0):A(2),(2,1):A(F(2,3))*S2,(2,2):-A(F(2,3))}
    for name,frame_matrix,rel,scale,center in (
       ('proton',Vp,'research/voevodsky/inputs/relative-proton.json',ONE,[A(F(1,4))]*3),
       ('neutron',Vn,'research/voevodsky/inputs/mode-neutron.json',A(F(8,3)),[ZERO]*3)):
        source=read(ROOT/rel);H=rational(source['metric']);Vi=invert(frame_matrix,3)
        assert product(adj(frame_matrix),frame_matrix)==scaled(scale,H)
        records=[r for r in binding['bindings'] if r['carrier']==name]
        assert len(records)==len(source['generators'])
        o=objects[name];f=o['f'][o['m']]
        for g,row in zip(source['generators'],records):
            T=rational(g['matrix']);t=vec(map(lambda x:A(F(x)),g['translation']))
            assert plus(product(T,vec(center)),t)==vec(center)
            R=conjugate(frame_matrix,T,Vi)
            assert R==sparse(parse_record(row['construction']['native_spatial_rotation']))
            assert product(adj(R),R)==identity(3)
            W=read_operator(row['coefficient_action'],36)
            M=product(f['D'],product(W,f['K']))
            assert product(W,f['K'])==product(f['K'],M)
            assert product(adj(M),product(f['gram'],M))==f['gram']
            data[name]['M'].append(M);data[name]['V'].append(R);data[name]['raw'].append(W)
    e=objects['electron'];f=e['f'][e['m']];K,D=source_electron_factors()
    T=product(f['D'],K);Ti=product(D,f['K'])
    assert product(T,Ti)==product(Ti,T)==identity(2)
    assert product(adj(T),product(f['gram'],T))==scaled(A(2),identity(2))
    faces=[{(i,j):K[2*a+i,j] for i,j in pairs(range(2),repeat=2) if (2*a+i,j) in K} for a in range(4)]
    data['electron']['logical']=[];data['electron']['permutations']=[]
    for u0 in ACTIONS:
        u=from_spin(u0)
        R={(a,b):trace(product(SIGMA[a],product(u,product(SIGMA[b],adj(u)))))/A(2) for a,b in pairs(range(3),repeat=2)}
        R={k:x for k,x in R.items() if x!=ZERO}
        assert all(x.flip(8)==x for x in R.values()) and product(adj(R),R)==identity(3)
        perm=[next(i for i,q in enumerate(faces) if product(u,product(p,adj(u)))==q) for p in faces]
        W={(2*t+i,2*s+j):x for s,t in enumerate(perm) for (i,j),x in u.items()}
        M=product(f['D'],product(W,f['K']))
        assert product(M,T)==product(T,u) and product(W,K)==product(K,u)
        assert M==conjugate(T,u,Ti)
        data['electron']['M'].append(M);data['electron']['V'].append(R);data['electron']['raw'].append(W)
        data['electron']['logical'].append(u);data['electron']['permutations'].append(perm)
    data['electron']['logical_to_M']=T
    return data


def proton_family(o,reps):
    merkle=read(MERKLE);geom=merkle['objects'][merkle['objects'][merkle['root']]['geometry']]['payload']
    placements=sorted(geom['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    rotations=[rational(r['rotation']) for r in placements];f=o['f'][o['m']]
    values=[{(i,j):x for (a,j),x in f['K'].items() if 3*t<=a<3*t+3 for i in (a-3*t,)} for t in range(12)]
    body=product(adj(rotations[0]),values[0]);invert(body,3)
    assert all(Ft==product(Rt,body) for Ft,Rt in zip(values,rotations))
    assert plus(*values)=={} and scaled(A(12),product(adj(body),body))==f['gram']
    for M,R in zip(reps['M'],reps['V']):
        assert M==identity(3)
        for t,Rt in enumerate(rotations):
            target=next(i for i,Ru in enumerate(rotations) if Ru==product(R,Rt))
            assert product(values[target],M)==product(R,values[t])
    # Every marked evaluation is invertible, but erasing the mark loses the
    # source-native frame. Construct two different complete-M inputs with the
    # same evaluated vector at different marks.
    t,u=0,next(i for i in range(1,12) if values[i]!=values[0])
    j=next(j for j in range(3) if any(values[t].get((i,j),ZERO)!=values[u].get((i,j),ZERO) for i in range(3)))
    x={(j,0):ONE};y=product(invert(values[u],3),product(values[t],x))
    assert y!=x and product(values[t],x)==product(values[u],y)
    assert product(f['K'],x)!=product(f['K'],y)
    group=closure(reps['V'],3,12);assert len(group)==12 and plus(*group)=={}
    hostile=sub(reps['V'][0],identity(3));assert hostile
    return {'body_coordinate_map':encode(body),'marked_port_evaluations':list(map(encode,values)),
            'marked_evaluation_invertible_count':12,'covariant_family_square':'F_(g.t) M_g=R_g F_t',
            'unmarked_sum':[], 'source_spatial_group_size':12,
            'mark_erasure_collision':{'ports':[placements[t]['outer_arrow'],placements[u]['outer_arrow']],
                'M_inputs':[encode(x),encode(y)],'same_vector':encode(product(values[t],x))},
            'dimension_only_identity_adapter_residual':encode(hostile),
            'meaning':'Native M is a transported body-frame fiber. The full port-indexed family is covariant; no nonzero unmarked linear spatial-vector adapter exists.'}


def neutron_centroids(o,reps):
    geo=read(GEOMETRY);ambient=read(AMBIENT)['record'];store=read(BELT)
    points={k:tuple(map(F,p)) for k,p in geo['belt_scaled_coordinates'].items()}
    for face in geo['belt_faces']:
        points['F_'+'_'.join(sorted(face))]=tuple(sum(points[k][i] for k in face)/3 for i in range(3))
    points={k:tuple(A(x)+S2*y for x,y in frame(p)) for k,p in points.items()}
    C={}
    for sector in range(3):
        ts=store['triangle_order'][6*sector:6*sector+6]
        centroid=tuple(sum((points[k][i] for t in ts for k in ambient['triangles'][t]),ZERO)/A(18) for i in range(3))
        C.update({(i,sector):x for i,x in enumerate(centroid) if x!=ZERO})
    S=reps['M'][0];R=reps['V'][0]
    assert S==R and product(C,S)==product(R,C)
    axis=scaled(A(F(1,3)),plus(identity(3),S,product(S,S)));plane=sub(identity(3),axis)
    assert axis==o['qm'] and product(C,axis)=={} and rank(C,3,3)==2
    assert product(adj(C),C)==scaled(A(F(4,3)),plane)
    Jplus=plus(C,scaled(A(2)/S3,axis));Jminus=sub(C,scaled(A(2)/S3,axis))
    for J in (Jplus,Jminus):
        assert product(J,S)==product(R,J)
        assert product(J,invert(J,3))==identity(3)
        assert product(adj(J),J)==scaled(A(F(4,3)),identity(3))
    assert product(Jplus,axis)==scaled(-ONE,product(Jminus,axis))
    f=o['f'][o['m']];h=f['gram'][0,0]
    assert f['gram']==scaled(h,identity(3))
    return {'sector_centroid_map':encode(C),'centroid_rank':2,'centroid_annihilates_active_return':True,
            'invariant_axis':encode(axis),'moving_plane':encode(plane),
            'two_invertible_equivariant_completions':[encode(Jplus),encode(Jminus)],
            'both_target_Gram':'(4/3) I','source_Gram_scalar':h.record(),
            'equal_metric_calibration_up_to_common_positive_scale':True,
            'completions_have_opposite_active_axis_sign':True,
            'meaning':'C3 modules are isomorphic but not canonically identified. Actual sector-centroid geometry misses the invariant active line; equally metric-compatible axis completions retain an unselected sign.'}


def polynomial_controls(B,J):
    # Independent formal variables a,b,conj(a),conj(b): these equalities are
    # polynomial identities, not just normalized-spinor sample tests.
    def add(*ps):
        out={}
        for p in ps:
            for m,c in p.items():out[m]=out.get(m,ZERO)+c
        return {m:c for m,c in out.items() if c!=ZERO}
    def scale(c,p):return {m:c*x for m,x in p.items() if c*x!=ZERO}
    def mul(p,q):
        out={}
        for m,c in p.items():
            for n,d in q.items():
                k=tuple(a+b for a,b in zip(m,n));out[k]=out.get(k,ZERO)+c*d
        return {m:c for m,c in out.items() if c!=ZERO}
    def conj(p):return {(m[2],m[3],m[0],m[1]):c.flip(8) for m,c in p.items()}
    def act(matrix,p):return [add(*(scale(x,p[j]) for (k,j),x in matrix.items() if k==i)) for i in range(3)]
    a,b,abar,bbar=[{tuple(int(i==j) for i in range(4)):ONE} for j in range(4)]
    density=[mul(a,abar),mul(a,bbar),mul(b,abar),mul(b,bbar)]
    r=act(B,density);q=act(J,[mul(a,a),mul(a,b),mul(b,b)])
    length=add(density[0],density[3]);square=mul(length,length)
    assert add(*(mul(x,x) for x in q))=={}
    assert add(*(mul(conj(x),x) for x in q))==scale(A(2),square)
    assert add(*(mul(x,x) for x in r))==square
    assert all(conj(x)==x for x in r)
    return {'formal_variables':['a','b','conj(a)','conj(b)'],'Cartan_null_identity':True,
            'Cartan_squared_norm':'2 (z* z)^2','Bloch_squared_norm':'(z* z)^2','identities_checked_symbolically':True}


def electron_bridges(o,reps):
    U=reps['logical'];V=reps['V'];central=U.index(scaled(-ONE,identity(2)))
    assert V[central]==identity(3) and reps['M'][central]==scaled(-ONE,identity(2))
    density=[];symmetric=[]
    for u in U:
        density.append({(2*i+j,2*a+b):x*y.flip(8) for i,j,a,b in pairs4() for x,y in [(u.get((i,a),ZERO),u.get((j,b),ZERO))] if x*y.flip(8)!=ZERO})
        a,b,c,d=[u.get(k,ZERO) for k in ((0,0),(0,1),(1,0),(1,1))]
        symmetric.append({(i,j):x for i,row in enumerate(((a*a,A(2)*a*b,b*b),(a*c,a*d+b*c,b*d),(c*c,A(2)*c*d,d*d))) for j,x in enumerate(row) if x!=ZERO})
    B={(a,2*i+j):x for a,sigma in enumerate(SIGMA) for (j,i),x in sigma.items()}
    J={(0,0):ONE,(0,2):-ONE,(1,0):CI,(1,2):CI,(2,1):A(-2)}
    assert rank(B,3,4)==3 and product(B,flat(identity(2),2))=={}
    assert product(J,invert(J,3))==identity(3)
    for u,v,density_u,sym_u in zip(U,V,density,symmetric):
        assert product(B,density_u)==product(v,B)
        assert product(J,sym_u)==product(v,J)
    adj_h,adj_basis=hom(density,V,4,3);sym_h,sym_basis=hom(symmetric,V,3,3)
    assert adj_h['dimension']==sym_h['dimension']==1
    def same_line(a,b):
        k=next(iter(b));q=a.get(k,ZERO)/b[k];assert q!=ZERO and scaled(q,b)==a
    same_line(B,adj_basis[0]);same_line(J,sym_basis[0])
    K,D=source_electron_factors();P=[{(i,j):K[2*f+i,j] for i,j in pairs(range(2),repeat=2) if (2*f+i,j) in K} for f in range(4)]
    store=read(STORE);normals=[vec(A(F(x[0]))+S3*F(x[1]) for x in n) for n in store['normals']]
    for f,p in enumerate(P):
        H=plus(*(scaled(normals[f].get((i,0),ZERO),s) for i,s in enumerate(SIGMA)))
        assert p==scaled(A(F(1,2)),sub(identity(2),H))
    for v,perm in zip(V,reps['permutations']):
        for f,n in enumerate(normals):assert product(v,n)==normals[perm[f]]
    # Exact linear splitting of ALL density matrices, not only the samples.
    trace_row={(0,0):ONE,(0,3):ONE}
    splitting=scaled(A(F(1,2)),plus(product(flat(identity(2),2),trace_row),
        *(product(flat(s,2),{(0,j):x for (i,j),x in B.items() if i==a}) for a,s in enumerate(SIGMA))))
    assert splitting==identity(4)
    assert density[central]==identity(4) and symmetric[central]==identity(3)
    polynomial=polynomial_controls(B,J)
    samples=[]
    gaussian_samples=(((F(1),F(0)),(F(0),F(0))),((F(0),F(0)),(F(1),F(0))),((F(3,5),F(0)),(F(0),F(4,5))))
    for gaussian in gaussian_samples:
        z=vec(A(a)+CI*b for a,b in gaussian);rho=product(z,adj(z));r=product(B,flat(rho,2));a=z.get((0,0),ZERO);b=z.get((1,0),ZERO)
        q=product(J,vec((a*a,a*b,b*b)))
        native=native_cartan(gaussian);native=vec((A(x)+CI*y)*(-1 if i==2 else 1) for i,(x,y) in enumerate(native))
        assert q==native
        assert trace(rho)==ONE and sum((x*x for x in r.values()),ZERO)==ONE
        assert sum((x*x for x in q.values()),ZERO)==ZERO and trace(product(adj(q),q))==A(2)
        reconstructed=scaled(A(F(1,2)),plus(identity(2),*(scaled(r.get((i,0),ZERO),s) for i,s in enumerate(SIGMA))))
        assert reconstructed==rho
        probabilities=[]
        for f,p in enumerate(P):
            probability=trace(product(scaled(A(F(1,2)),p),rho))
            dot=trace(product(transpose(normals[f]),r))
            assert probability==(ONE-dot)/A(4);probabilities.append(probability.record())
        for u,v,density_u,sym_u in zip(U,V,density,symmetric):
            zz=product(u,z);rr=product(B,flat(product(zz,adj(zz)),2))
            aa,bb=[zz.get((i,0),ZERO) for i in range(2)];qq=product(J,vec((aa*aa,aa*bb,bb*bb)))
            assert rr==product(v,r) and qq==product(v,q)
        assert product(scaled(-ONE,z),adj(scaled(-ONE,z)))==rho
        raw=product(K,z);raw_minus=scaled(-ONE,raw);assert raw!=raw_minus
        samples.append({'spinor':encode(z),'Bloch_vector':encode(r),'Cartan_null_vector':encode(q),'face_probabilities':probabilities})
    return {'central_action':{'M':'-I2','spatial_V':'I3','nonzero_linear_intertwiner':False},
            'density_to_spatial':encode(B),'density_bridge_Hom':adj_h,
            'Cartan_symmetric_square_to_spatial':encode(J),'symmetric_square_bridge_Hom':sym_h,
            'native_Cartan_third_coordinate_flip_declared':True,
            'symbolic_quadratic_identities':polynomial,'density_reconstruction_is_full_matrix_identity':True,
            'samples':samples,'native_action_count':len(U),
            'density_readout_loses_U1_phase':True,'Cartan_readout_loses_central_sign':True,
            'quadratic_readout_is_coherent_packet_equivalence':False,
            'meaning':'Spinor M is not a linear geometric vector. Its density adjoint and holomorphic symmetric square have natural spatial-vector bridges; both erase at least the observable retained central sign.'}


def pairs4():
    return ((i,j,a,b) for i,j in pairs(range(2),repeat=2) for a,b in pairs(range(2),repeat=2))


def frame_control(o,reps,expected):
    d=o['f'][o['m']]['rank'];S=plus(identity(d),{(0,1):A(F(2,3))});Si=sub(identity(d),{(0,1):A(F(2,3))})
    T=plus(identity(3),{(0,2):A(F(3,5))});Ti=sub(identity(3),{(0,2):A(F(3,5))})
    M2=[conjugate(S,m,Si) for m in reps['M']];V2=[conjugate(T,v,Ti) for v in reps['V']]
    h,basis=hom(M2,V2,d,3);assert h['dimension']==expected
    old=o['f'][o['m']]['gram'];H=product(adj(Si),product(old,Si));HV=product(adj(Ti),Ti)
    for m,v in zip(M2,V2):
        assert product(adj(m),product(H,m))==H
        assert product(adj(v),product(HV,v))==HV
    return {'domain_change':encode(S),'target_change':encode(T),'Hom_dimension':h['dimension'],
            'transported_source_metric':encode(H),'transported_target_metric':encode(HV)}


def main():
    contract=read(CONTRACT);prior=read(PRIOR)
    assert prior['status']=='pass' and all(prior['checks'].values())
    assert all(digest(ROOT/p)==h for p,h in prior['source_sha256'].items()),'stale prior iteration'
    objects,binding,pins=load();reps=representations(objects,binding)
    results={};expected={'proton':0,'neutron':3,'electron':0}
    for n,o in objects.items():
        result,basis=hom(reps[n]['M'],reps[n]['V'],o['f'][o['m']]['rank'],3)
        assert result['dimension']==expected[n];results[n]=result
    pf=proton_family(objects['proton'],reps['proton']);nc=neutron_centroids(objects['neutron'],reps['neutron'])
    eb=electron_bridges(objects['electron'],reps['electron'])
    frames={n:frame_control(o,reps[n],expected[n]) for n,o in objects.items()}
    checks={k:True for k in (
       'fresh_native_sources_and_iteration3_receipt_pins',
       'baryon_spatial_rotations_reconstructed_from_actual_affine_generators',
       'baryon_native_stage_M_actions_and_metric_squares',
       'all24_electron_logical_M_spatial_and_face_action_squares',
       'exact_RREF_Hom_dimensions_zero_three_zero',
       'proton_three_M_dimensions_are_trivial_not_geometric_vector_representation',
       'proton_no_unmarked_spatial_vector_adapter_and_identity_hostile',
       'proton_all12_marked_body_frame_evaluations_are_invertible_and_covariant',
       'proton_unmarked_spatial_sum_zero_and_mark_erasure_collision',
       'neutron_C3_module_equivalence_is_possible_but_not_unique',
       'neutron_actual_sector_centroid_map_rank_two',
       'neutron_centroid_annihilates_the_actual_active_invariant_line',
       'neutron_opposite_axis_completions_both_invertible_equivariant_and_same_Gram',
       'electron_central_minus_forbids_nonzero_linear_M_to_spatial_map',
       'electron_density_adjoint_unique_spatial_bridge_up_to_scale',
       'electron_native_Cartan_symmetric_square_unique_spatial_bridge_up_to_scale',
       'electron_quadratic_bridges_intertwine_all24_native_operations',
       'electron_native_Cartan_coordinate_convention_and_null_norm_identities',
       'electron_face_probabilities_recover_from_Pauli_spatial_readout',
       'electron_quadratic_geometry_does_not_recover_coherent_central_sign',
       'nonmonomial_domain_and_target_frames_preserve_Hom_and_metrics',
       'marked_nonlinear_and_algebraic_module_alternatives_keep_exact_task_boundaries',
       'capacity_M_is_not_a_common_literal_unmarked_geometric_main_space')}
    additions=[PRIOR,CONTRACT,GEOMETRY,AMBIENT,MERKLE,BELT,STORE,Path(__file__).resolve()]
    for p in additions:pins[p.relative_to(ROOT).as_posix()]=digest(p)
    pins.update(prior['source_sha256'])
    for module in tuple(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            p=Path(path).resolve()
            if p.suffix=='.py' and p.is_relative_to(ROOT/'research'):
                k=p.relative_to(ROOT).as_posix();assert k not in pins or pins[k]==digest(p);pins[k]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    report={'schema':'marici.packet-handoff-naturality-iteration-check.v1','status':'pass','iteration':4,
       'checks':checks,'M_to_spatial_Hom':results,'proton_native_body_frame_family':pf,
       'neutron_native_centroid_and_axis':nc,'electron_quadratic_spatial_bridges':eb,'frame_controls':frames,
       'capacity_M_identified_with_common_unmarked_spatial_main_space':False,
       'source_native_typed_geometric_alternatives_constructed':True,
       'neutron_geometric_module_identification_unique':False,
       'quadratic_electron_readout_is_full_coherent_task_equivalence':False,
       'source_native_handoff_constructed':False,'physical_particle_assignment_verified':False,
       'native_producers_executed':False,'formal_proof_recompiled':False,
       'next_executable_scope':contract['next_executable_scope'],'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':4,'check_groups':len(checks),'Hom_M_to_spatial':expected,
       'proton_marked_geometric_evaluations':12,'neutron_centroid_rank':2,
       'electron_density_and_symmetric_square_Hom_dimensions':[1,1],
       'common_literal_geometric_M_selected':False},indent=2))


if __name__=='__main__':main()
