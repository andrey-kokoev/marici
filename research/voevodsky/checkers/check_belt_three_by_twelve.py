"""Test the (g,m)=(3,12) conjecture using intrinsic real triangle planes.
No duplicated records: each of 18 triangles contributes its two planar axes.
Exact coefficients are stored as z_ij/sqrt(d_i*d_j), with rational positive d.
The original 54-coordinate interface conversion is counted separately.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
from check_coupled_six_piece_belt import R,Z,ONE,add,mul,conj,scale,norm,total,encoded
from check_belt_operator_inputs import frame,action,mode,mean

BASE=Path(__file__).resolve().parents[1]

def decode(z):
    a,b,c,d=map(Q,z);return (R(a,b),R(c,d))
def sparse_product(a,b,metric):
    byrow={}
    for (i,j),z in b.items():byrow.setdefault(i,[]).append((j,z))
    out={}
    for (i,k),z in a.items():
        for j,w in byrow.get(k,[]):out[i,j]=add(out.get((i,j),Z),scale(1/metric[k],mul(z,w)))
    return {e:z for e,z in out.items() if z!=Z}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rational(a):
    assert a.b==0
    return a.a

def main():
    source_path=BASE/'results/coupled_six_piece_belt_store.json';geometry_path=BASE/'results/four_six_center_cones.json'
    source_raw=source_path.read_bytes();packet=json.loads(source_raw);source=packet['record']
    assert sha256(json.dumps(source,sort_keys=True,separators=(',',':')).encode()).hexdigest()==packet['root']
    geometry_raw=geometry_path.read_bytes();geometry=json.loads(geometry_raw)
    assert sha256(geometry_raw).hexdigest()==source['geometry_sha256']
    triangles=list(map(tuple,source['triangles']));index={t:i for i,t in enumerate(triangles)}
    faces=geometry['belt_faces'];owners=source['face_owners']
    points={k:tuple(map(Q,v)) for k,v in geometry['belt_scaled_coordinates'].items()}
    for f in faces:points['F_'+'_'.join(sorted(f))]=mean([points[k] for k in f])
    coords={k:frame(v) for k,v in points.items()};inverse={v:k for k,v in coords.items()}
    rotation=((Q(0),Q(0),Q(1)),(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)))
    rename={k:inverse[action(rotation,v)] for k,v in coords.items()}
    perm=[index[tuple(rename[v] for v in t)] for t in triangles]
    face_perm=[next(j for j,f in enumerate(faces) if set(f)=={rename[v] for v in face}) for face in faces]
    adjacent=[j for j in range(1,6) if len(set(faces[0])&set(faces[j]))==2]
    assert len(adjacent)==2
    matchings=[]
    for j in adjacent:
        pairs=[];pair=(0,j)
        for _ in range(3):pairs.append(pair);pair=tuple(face_perm[i] for i in pair)
        assert sorted(i for p in pairs for i in p)==list(range(6))
        matchings.append(pairs)
    # First geometrically adjacent matching, not a choice based on coefficient
    # count. Both C3-invariant matchings are checked for the same result below.
    pair=matchings[0][0];reference=[i for i in range(18) if owners[i] in pair]
    order=reference+[perm[i] for i in reference]+[perm[perm[i]] for i in reference]
    assert len(reference)==6 and sorted(order)==list(range(18))
    planes=[]
    for t in triangles:
        rr,ss=mode(t,points);r=tuple(R(*x) for x in rr);s=tuple(R(*x) for x in ss)
        a=rational(dot(s,s));b=rational(dot(r,s));assert a>0
        v=tuple(x-(b/a)*y for x,y in zip(r,s));beta=rational(dot(v,v));assert beta>0 and dot(v,s)==0
        # E1=s/sqrt(a), E2=v/sqrt(beta) are real orthonormal axes.
        # The physical intrinsic coordinates are z0/sqrt(a), z1/sqrt(beta).
        numerators=((R(b),R(a)),(R(beta),R()))
        planes.append({'columns':(s,v),'d':(a,beta),'z':numerators})
    for t in range(18):
        for axis in range(2):
            rotated=tuple(sum(rotation[a][b]*planes[t]['columns'][axis][b] for b in range(3)) for a in range(3))
            assert rotated==planes[perm[t]]['columns'][axis]
    d=tuple(x for t in order for x in planes[t]['d'])
    z=tuple(x for t in order for x in planes[t]['z'])
    assert d[:12]==d[12:24]==d[24:] and z[:12]==z[12:24]==z[24:]
    assert all(x!=Z for x in z)
    reference_norm=sum(norm(z[i])/d[i] for i in range(12));full_norm=3*reference_norm
    assert reference_norm.b==0 and reference_norm.a>0
    # All numerators refer to physical orthonormal coordinates. Matrix
    # multiplication divides each summand by the intermediate d_k.
    L={(i,j):scale(1/reference_norm,mul(z[i],conj(z[j]))) for i in range(36) for j in range(36) if i//12==j//12}
    G={(i,j):(R(d[i]/3),R()) for i in range(36) for j in range(36) if i%12==j%12}
    N={(i,j):scale(1/full_norm,mul(z[i],conj(z[j]))) for i in range(36) for j in range(36)}
    assert sparse_product(G,L,d)==sparse_product(L,G,d)==N
    assert sparse_product(N,N,d)==N
    used=[set(),set(),set()];cycle_sum=Z;cycles=0
    for (i,k),g in G.items():
        for j in range(12*(k//12),12*(k//12+1)):
            w=scale(1/(d[j]*d[i]*d[k]),mul(N[j,i],mul(g,L[k,j])))
            assert w[1]==0 and w[0].b==0 and w[0].a>0
            cycle_sum=add(cycle_sum,w);cycles+=1
            used[0].add((k,j));used[1].add((i,k));used[2].add((j,i))
    assert cycle_sum==ONE and all(set(m)==s for m,s in zip((L,G,N),used))
    # Ambient embedding: numerator W[a,i] has physical coefficient
    # W[a,i]/sqrt(d_i). Its transpose is the input projection.
    W={}
    for slot,t in enumerate(order):
        for k,column in enumerate(planes[t]['columns']):
            for a,value in enumerate(column):
                if value:W[3*t+a,2*slot+k]=value
    recovered=[Z]*54
    for (a,i),w in W.items():recovered[a]=add(recovered[a],scale(w/d[i],z[i]))
    ambient=tuple(decode(v) for v in source['collective_vector'])
    assert tuple(recovered)==ambient and sum(norm(v) for v in ambient)==full_norm
    # W*W=I follows blockwise from the exact plane Gram checks; together with
    # W u_intrinsic=u_ambient it proves W N_intrinsic W*=N_ambient on ALL inputs.
    original_N={(3*a['target'][1]+'xyz'.index(a['target'][2]),3*a['source'][1]+'xyz'.index(a['source'][2])):decode(a['coefficient'])
                for a in source['arrows'] if a['stage']=='N'}
    reconstructed={(i,j):scale(1/full_norm,mul(recovered[i],conj(recovered[j]))) for i in range(54) for j in range(54)}
    assert reconstructed==original_N
    # A genuine discarded direction exists at every triangle: the real normal
    # to its plane. The embedding is not a bijective relabelling of 54 ports.
    assert len(d)==36 and len(ambient)==54
    # Both adjacent-pair choices give the same repeated full-support 12-vector
    # structure and the same interface support, without requiring equal phases
    # between vectors from different triangles by arbitrary fitting.
    for matching in matchings:
        ref=[i for i in range(18) if owners[i] in matching[0]]
        alt=ref+[perm[i] for i in ref]+[perm[perm[i]] for i in ref]
        az=tuple(v for i in alt for v in planes[i]['z']);ad=tuple(v for i in alt for v in planes[i]['d'])
        assert sorted(alt)==list(range(18)) and az[:12]==az[12:24]==az[24:] and ad[:12]==ad[12:24]==ad[24:]
    checks={
        'three_adjacent_face_pairs_cover_actual_six_piece_belt':len(matchings)==2,
        'no_triangle_is_duplicated_or_omitted':sorted(order)==list(range(18)),
        'each_triangle_supplies_two_real_orthonormal_plane_axes':len(planes)==18,
        'each_rotating_sector_has_twelve_full_support_coordinates':len(z)==36 and all(v!=Z for v in z),
        'co_rotating_charts_give_identity_monomial_transport':z[:12]==z[12:24]==z[24:],
        'actual_spatial_rotation_transports_each_derived_plane_frame':all(tuple(sum(rotation[a][b]*planes[t]['columns'][axis][b] for b in range(3)) for a in range(3))==planes[perm[t]]['columns'][axis] for t in range(18) for axis in range(2)),
        'same_full_return_after_local_and_alignment_stages':sparse_product(G,L,d)==N,
        'collective_return_is_idempotent':sparse_product(N,N,d)==N,
        'all_1836_arrows_have_positive_fixed_weight_deletion_certificate':cycle_sum==ONE and all(set(m)==s for m,s in zip((L,G,N),used)),
        'original_ambient_collective_operator_recovered_exactly':reconstructed==original_N,
        'two_matching_choices_both_admit_three_by_twelve':True,
        'intrinsic_interface_reduces_54_ambient_to_36_plane_coordinates':len(d)==36,
        'original_artifacts_unchanged':source_path.read_bytes()==source_raw and geometry_path.read_bytes()==geometry_raw,
    }
    counts={'L':len(L),'G':len(G),'N':len(N),'total':sum(map(len,(L,G,N)))}
    assert counts=={'L':432,'G':108,'N':1296,'total':1836}
    report={'verification_passed':all(checks.values()),'checks':checks,'source_root':packet['root'],
        'conjecture':'three placements with twelve intrinsic coordinates each',
        'counts':counts,'typed_core_ports':108,'positive_closed_cycles':cycles,'closed_cycle_trace':'1',
        'adjacent_face_matchings':matchings,'triangle_order_by_sector':[order[i:i+6] for i in range(0,18,6)],
        'co_rotating_representation':'rho(C3)=I_12; the action on sector placements is the nontrivial three-cycle',
        'intrinsic_norm_squared':str(full_norm.a),
        'conversion_counts':{'ambient_to_intrinsic':len(W),'intrinsic_to_ambient':len(W),'core_plus_both':1836+2*len(W)},
        'outcome':'A source-derived 1836-arrow (3,12) intrinsic-plane realization exists and reproduces the full ambient collective return through its explicit interface maps.',
        'qualification':'This changes the internal coordinates and local stage: 3 sector-wide rank-one selections replace 18 triangle selections. It is not a relabelling or deletion inside the old 5346-arrow graph. A fixed original ambient interface requires the additional counted maps.',
        'not_established':'a physical neutron identity, mass, or a source rule uniquely preferring this implementation over the original ambient-coordinate one',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    store={'source_root':packet['root'],'triangle_order':order,'coordinates':[{'triangle':t,'axis':a,'d':str(planes[t]['d'][a]),'selected_numerator':encoded(planes[t]['z'][a])} for t in order for a in range(2)],
        'coefficient_convention':'entry numerator / sqrt(d_target*d_source); numerator basis (1,sqrt(2),i*sqrt(3),i*sqrt(6))',
        'arrows':[{'stage':s,'target':i,'source':j,'numerator':encoded(v)} for s,m in zip(('L','G','N'),(L,G,N)) for (i,j),v in sorted(m.items())],
        'embedding_entries':[{'ambient_target':a,'intrinsic_source':i,'numerator':[str(v.a),str(v.b)],'denominator_radicand':str(d[i])} for (a,i),v in sorted(W.items())]}
    assert len(store['arrows'])==len({(a['stage'],a['source'],a['target']) for a in store['arrows']})==1836
    replay=json.loads(json.dumps(store));restored={s:{} for s in ('L','G','N')}
    for a in replay['arrows']:restored[a['stage']][a['target'],a['source']]=decode(a['numerator'])
    assert (restored['L'],restored['G'],restored['N'])==(L,G,N)
    (BASE/'results/belt_three_by_twelve_store.json').write_text(json.dumps(store,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/belt_three_by_twelve.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
