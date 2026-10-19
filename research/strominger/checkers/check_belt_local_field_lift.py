"""Local Gram construction before global comparison; horizontal metric hostile."""
from pathlib import Path
from itertools import combinations
import json,hashlib
from check_opposite_branch_canonical import (ROOT,BASE,F,R,Z,ONE,decode,encoded,add,mul,conj,scale,norm,total,identity,compose,adjoint,entries,diag,dump,apply,plus,times,trace,real_mm,real_inverse2,add_block)
from check_belt_operator_inputs import mode,mean
from assemble_real_complex_arrows import decode as decode_source
from check_belt_axial_witness import mv,mm,add as madd,scale as mscale,I,prepare,sub as vsub
hashes={}
def read(p):
    raw=(ROOT/p).read_bytes();hashes[p]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def inv(z):assert z!=Z;return scale(1/norm(z),conj(z))
def minus(a,b):return add(a,scale(-1,b))
def inner(a,b,d):return total(scale(1/q,mul(conj(x),y)) for x,y,q in zip(a,b,d))
def mat(columns):return {(i,j):columns[j][i] for i in range(2) for j in range(2) if columns[j][i]!=Z}
def inv2(A):
    a,b,c,d=[A.get(k,Z) for k in ((0,0),(0,1),(1,0),(1,1))]
    q=inv(minus(mul(a,d),mul(b,c)))
    return {k:mul(q,x) for k,x in zip(((0,0),(0,1),(1,0),(1,1)),(d,scale(-1,b),scale(-1,c),a)) if x!=Z}
def block(A,t):return {(i-2*t,j-2*t):v for (i,j),v in A.items() if i//2==j//2==t}
def encodeR(x):return [str(x.a),str(x.b)]

def main():
    read('research/strominger/inputs/belt-local-field-lift-protocol-v1.json')
    source=read('research/strominger/inputs/neutron-real-complex-arrows.json')
    geo=read('research/voevodsky/results/four_six_center_cones.json')
    ambient=read('research/voevodsky/results/coupled_six_piece_belt_store.json')['record']
    old=read('research/voevodsky/results/belt_three_by_twelve_store.json')
    decoded,sp,_=decode_source(source);rot=tuple(tuple(map(F,row)) for row in decoded['generators'][0]['matrix'])
    proj=mscale(F(1,3),madd(I,rot,mm(rot,rot)))
    centers=[mv(proj,sp[s['vertex']]) for s in source['seeds']]
    ax=vsub(centers[1],centers[0]);axis=(ax[2],ax[0],ax[1])
    points={k:tuple(map(F,v)) for k,v in geo['belt_scaled_coordinates'].items()}
    signs=prepare(points,geo['belt_faces'],axis)['signs']
    for face in geo['belt_faces']:points['F_'+'_'.join(sorted(face))]=mean([points[k] for k in face])
    planes=[]
    for tri in ambient['triangles']:
        rr,ss=mode(tuple(tri),points);r=tuple(R(*v) for v in rr);s=tuple(R(*v) for v in ss)
        a=sum(x*x for x in s);b=sum(x*y for x,y in zip(r,s));assert a.b==b.b==0
        a,b=a.a,b.a;v=tuple(x-(b/a)*y for x,y in zip(r,s));beta=sum(x*x for x in v);assert beta.b==0
        beta=beta.a;planes.append(((a,beta),((R(b),R(a)),(R(beta),R()))))
    order=old['triangle_order'];d=tuple(x for t in order for x in planes[t][0]);z=tuple(x for t in order for x in planes[t][1])
    assert d==tuple(F(c['d']) for c in old['coordinates']) and z==tuple(decode(c['selected_numerator']) for c in old['coordinates'])
    chirality=[signs[ambient['face_owners'][t]] for t in order]
    J={};C={};frames=[];newframes=[];kappas=[];newz=[];phases=[]
    Cplane=((R(F(-1,2)),R(F(1,2))),(R(F(-3,2)),R(F(-1,2))))
    for t in range(18):
        w=z[2*t:2*t+2];bar=tuple(map(conj,w));dd=d[2*t:2*t+2]
        V=mat((w,bar));Vi=inv2(V);assert compose(V,Vi)==identity(2)
        c=inner(w,bar,dd);n=inner(w,w,dd);assert n[1]==0 and c!=Z
        kappas.append(norm(c)/(n[0]*n[0]));q=mul(c,inv(conj(c)))
        target=mat((bar,tuple(mul(q,x) for x in w)))
        local=identity(2) if chirality[t]==1 else compose(target,Vi)
        ww=w if chirality[t]==1 else bar;newz.extend(ww)
        assert compose(adjoint(local,dd),local)==identity(2) and apply(local,w,2)==ww
        for (i,j),v in local.items():J[2*t+i,2*t+j]=v
        frames.append(V);newframes.append(compose(local,V));phases.append(encoded(q))
        X=tuple((w[i][0],w[i][1]) for i in range(2))
        add_block(C,real_mm(real_mm(X,Cplane),real_inverse2(X)),[2*t,2*t+1])
    newz=tuple(newz);Js=adjoint(J,d)
    assert compose(Js,J)==identity(36) and apply(J,z,36)==newz
    C2=compose(C,C);Cnew={e:v for e,v in C.items() if chirality[e[0]//2]==1}
    Cnew.update({e:v for e,v in C2.items() if chirality[e[0]//2]==-1})
    assert compose(J,C)==compose(Cnew,J)
    # Only now inspect independently stored target/global comparisons.
    target=read('research/voevodsky/results/opposite_branch_belt_store.json')
    known=read('research/strominger/results/opposite-branch-cycle-lift/operators.json')
    assert newz==tuple(map(decode,target['selected_numerators'])) and J==entries(known['forwardLift'])
    for stage in ('L','G','N'):
        ops=[{(a['target'],a['source']):scale(1/d[a['source']],decode(a['numerator'])) for a in store['arrows'] if a['stage']==stage} for store in (old,target)]
        assert compose(ops[1],J)==compose(J,ops[0])
    rotation_packet=read('research/strominger/results/neutron-canonical-rotation-frame.json')
    T={(j,i):ONE for i,j in enumerate(rotation_packet['native_coordinate_permutation'])}
    assert compose(T,J)==compose(J,T)
    canonical=read('research/strominger/results/opposite-branch-canonical/operators.json')
    eold=read('research/voevodsky/results/native_operation_energy_lift_store.json')['carriers']['belt']
    H0=entries(eold['entries']);H1=entries(canonical['signedCharacterHamiltonianIn4HOverPiUnits'])
    assert compose(H1,J)==compose(J,H0)
    triangles=[set(ambient['triangles'][t]) for t in order]
    seams=[(a,b) for s in range(3) for a,b in combinations(range(6*s,6*s+6),2) if len(triangles[a]&triangles[b])==2]
    assert len(seams)==21
    def seam(v,a,b):
        row={}
        for t,sgn in ((a,1),(b,-1)):
            nn=sum(norm(v[2*t+k])/d[2*t+k] for k in range(2))
            for k in range(2):row[0,2*t+k]=scale(sgn/(d[2*t+k]*nn),conj(v[2*t+k]))
        sharp={(j,0):scale(d[j],conj(x)) for (_,j),x in row.items()}
        dual=sum(d[j]*norm(x) for (_,j),x in row.items())
        return times(1/dual,compose(sharp,row))
    for (a,b),stored in zip(seams,eold['seam_projectors']):
        A=seam(z,a,b);B=seam(newz,a,b)
        assert A==entries(stored['entries']) and compose(B,J)==compose(J,A)
    J52={**J,**{(i,i):ONE for i in range(36,52)}}
    u=tuple(map(decode,canonical['nativeDiagonalAdapter']))+(ONE,)*16
    U=diag(u);Us=diag(tuple(map(conj,u)))
    for data in canonical['canonicalProjectors'].values():
        B=entries(data);A=compose(compose(Us,B),U)
        assert compose(B,J52)==compose(J52,A)
    # Full neighboring-plane transport from local eigenframes: flat and
    # cycle-intertwining, but not assumed to preserve different plane metrics.
    rows=[];obstructed=[];raw_nonisometric=[]
    for a,b in seams:
        B=compose(frames[b],inv2(frames[a]));Bn=compose(newframes[b],inv2(newframes[a]))
        assert compose(B,block(C,a))==compose(block(C,b),B)
        assert compose(Bn,block(J,a))==compose(block(J,b),B)
        # Rectangular metric adjoint: source d_a and target d_b.
        sharp={(j,i):scale(d[2*a+j]/d[2*b+i],conj(v)) for (i,j),v in B.items()}
        iso=compose(sharp,B)==identity(2)
        if not iso:raw_nonisometric.append((a,b))
        if kappas[a]!=kappas[b]:obstructed.append((a,b))
        rows.append({'triangles':[order[a],order[b]],'raw_eigenframe_isometry':iso,'normalized_cross_Gram_equal':kappas[a]==kappas[b],
          'source_kappa':encodeR(kappas[a]),'target_kappa':encodeR(kappas[b])})
    assert obstructed
    # The six coarse-face interfaces are a smaller, differently typed set.
    # Their incident small triangles are congruent. Test them separately;
    # do not mistake the within-face obstructions for cross-face failures.
    crossface=[]
    for a,b in combinations(range(18),2):
        oa,ob=ambient['face_owners'][order[a]],ambient['face_owners'][order[b]]
        if oa==ob or len(triangles[a]&triangles[b])!=2:continue
        wa,wb=z[2*a:2*a+2],z[2*b:2*b+2]
        da,db=d[2*a:2*a+2],d[2*b:2*b+2]
        ca=inner(wa,tuple(map(conj,wa)),da);cb=inner(wb,tuple(map(conj,wb)),db)
        assert inner(wa,wa,da)==inner(wb,wb,db) and kappas[a]==kappas[b]
        q=mul(ca,inv(cb));assert norm(q)==1
        B=compose(mat((wb,tuple(mul(q,conj(x)) for x in wb))),inv2(frames[a]))
        sharp={(j,i):scale(da[j]/db[i],conj(v)) for (i,j),v in B.items()}
        assert compose(sharp,B)==identity(2)
        assert compose(B,block(C,a))==compose(block(C,b),B)
        Bn=compose(compose(block(J,b),B),adjoint(block(J,a),da))
        assert compose(Bn,block(J,a))==compose(block(J,b),B)
        crossface.append({'faces':[oa,ob],'triangles':[order[a],order[b]],'source_transport':dump(B),'target_transport':dump(Bn)})
    assert len(crossface)==6
    # Consecutive cross-face edges meet DIFFERENT triangle ports in a face;
    # a face-label loop alone is not a composable full-plane route.
    incident={i:[] for i in range(6)}
    for row in crossface:
        for f,t in zip(row['faces'],row['triangles']):incident[f].append(t)
    assert all(len(ts)==2 and ts[0]!=ts[1] for ts in incident.values())
    # Supply the actual within-face port changes, not identity-by-face-label.
    # Both lateral ports have the same Gram shape, even though the third
    # triangle of that face generally does not.
    port_edges=[tuple(order.index(t) for t in row['triangles']) for row in crossface]
    port_edges += [tuple(order.index(t) for t in ts) for ts in incident.values()]
    neighbors={a:[] for edge in port_edges for a in edge}
    for a,b in port_edges:neighbors[a].append(b);neighbors[b].append(a)
    assert len(neighbors)==12 and all(len(ns)==2 for ns in neighbors.values())
    def metric_port_map(a,b):
        wa,wb=z[2*a:2*a+2],z[2*b:2*b+2];da,db=d[2*a:2*a+2],d[2*b:2*b+2]
        ca=inner(wa,tuple(map(conj,wa)),da);cb=inner(wb,tuple(map(conj,wb)),db)
        assert inner(wa,wa,da)==inner(wb,wb,db) and kappas[a]==kappas[b]
        q=mul(ca,inv(cb));B=compose(mat((wb,tuple(mul(q,conj(x)) for x in wb))),inv2(frames[a]))
        sharp={(j,i):scale(da[j]/db[i],conj(v)) for (i,j),v in B.items()}
        assert compose(sharp,B)==identity(2) and compose(B,block(C,a))==compose(block(C,b),B)
        return B
    start=min(neighbors);current=start;previous=None;holonomy=identity(2);newholonomy=identity(2);portword=[start]
    for _ in range(12):
        nxt=next(n for n in neighbors[current] if n!=previous)
        B=metric_port_map(current,nxt)
        Bn=compose(compose(block(J,nxt),B),adjoint(block(J,current),d[2*current:2*current+2]))
        holonomy=compose(B,holonomy);newholonomy=compose(Bn,newholonomy)
        previous,current=current,nxt;portword.append(current)
    assert current==start and len(set(portword[:-1]))==12
    assert holonomy==newholonomy==identity(2)
    # All triangle routes in each six-plane patch close for these frame maps,
    # including nonedge comparison routes. This is algebraic flatness, not metric compatibility.
    route_count=0
    for sector in range(3):
        for a,b,c in product3(range(6*sector,6*sector+6)):
            ab=compose(frames[b],inv2(frames[a]));bc=compose(frames[c],inv2(frames[b]));ac=compose(frames[c],inv2(frames[a]))
            assert compose(bc,ab)==ac
            route_count+=1
    checks={'geometric_modes_and_metrics_independently_reconstructed':True,'axis_selects_local_branch_before_target_load':True,
      'local_Gram_isometries_recover_global_adapter':True,'native_L_G_N_and_C3_intertwine':True,'full_cycles_and_native_energy_intertwine':True,
      'all21_independently_rebuilt_seams_intertwine':True,'all18_full_bank_projectors_intertwine':True,
      'horizontal_frame_maps_flat_and_vertical_square_commutes':True,'full_plane_unitary_cycle_transport_has_Gram_obstructions':True,
      'all6_cross_face_ports_have_unitary_cycle_intertwiners':True,
      'coarse_face_loop_requires_distinct_port_connections':True,
      'completed12_port_metric_cycle_has_identity_holonomy':True}
    for p in [Path(__file__),BASE/'checkers/check_belt_axial_witness.py',ROOT/'research/voevodsky/checkers/check_belt_operator_inputs.py']:
        hashes[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    out=BASE/'results/belt-local-field-lift';out.mkdir(parents=True,exist_ok=True)
    result={'status':'pass','checks':checks,'source_hashes':hashes,'local_to_global_adapter':dump(J),
      'face_signs':list(signs),'horizontal_seams':rows,'cross_face_interfaces':crossface,'face_incident_triangle_ports':incident,'metric_port_loop':[order[t] for t in portword],'metric_loop_holonomy':dump(holonomy),'horizontal_cycle_unitary_obstructions':len(obstructed),
      'raw_horizontal_nonisometries':len(raw_nonisometric),'exact_frame_route_squares':route_count,
      'disposition':{'vertical':'Source-local metric converters and axial modes assemble to the independently verified global cycle adapter; energy,21 seams,18 bank pulses transport.',
       'horizontal':'Flat eigenframe transport is not generally metric-preserving. Unequal normalized conjugate-eigenline Gram overlaps obstruct ANY unitary cycle intertwiner on the full planes.',
       'scope':'No equivalence between different triangle planes is inferred from the valid branch conversion at each same plane. Full-plane isometric local-system conjecture fails; original seam constraints survive.'}}
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'cycle_unitary_obstructions':len(obstructed),'raw_nonisometries':len(raw_nonisometric),'route_squares':route_count}))
def product3(xs):
    from itertools import product
    return product(xs,repeat=3)
if __name__=='__main__':main()
