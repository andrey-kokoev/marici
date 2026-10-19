"""Single-link logical kernel and full fold-retaining geometric pullback.
These are two separately typed constructions, not an implicit identification of
the spinor state with the potential boundary sphere. Shared stores read only.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT,parse
from check_electron_tetrahedral_spinor import D,ga,gs,gm,gc,gt,gmm,spin,G0,G1,ident,adj,sm,act,norm,encode
from check_host_coefficient_pullback import source_host,lifts
from check_projector_fold_sheets import verify as verify_atlas,parameters
from check_fold_coefficient_attachment import mode,direction
from potential_complex_pullback import depth,complex_cells,betti_mod2


def decode(z):return D(*map(F,z[0])),D(*map(F,z[1]))
def neg(z):return gs(-1,z)
def mat(a):return [[encode(z) for z in r] for r in a]
def determinant2(a):return ga(gm(a[0][0],a[1][1]),neg(gm(a[0][1],a[1][0])))
def ginv(z):
    denominator=gm(gc(z),z)[0];return tuple(x/denominator for x in gc(z))
def inverse2(a):
    d=ginv(determinant2(a))
    return tuple(tuple(gm(d,z) for z in row) for row in ((a[1][1],neg(a[0][1])),(neg(a[1][0]),a[0][0])))
def rational_rank(rows):
    rows=[list(r) for r in rows];rank=0
    for j in range(len(rows[0])):
        p=next((i for i in range(rank,len(rows)) if rows[i][j]),None)
        if p is None:continue
        rows[rank],rows[p]=rows[p],rows[rank];d=rows[rank][j];rows[rank]=[x/d for x in rows[rank]]
        for i in range(rank+1,len(rows)):
            if rows[i][j]:
                v=rows[i][j];rows[i]=[x-v*y for x,y in zip(rows[i],rows[rank])]
        rank+=1
        if rank==len(rows):break
    return rank


def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/proton-electron-single-link-potential-v1.json';c=json.loads(cp.read_text())
    pp,ep,ap=[ROOT/c[k] for k in ('proton','electron','potential_atlas')]
    pstore=json.loads(pp.read_text());ports,(Lp,Gp,Np)=parse(pstore)
    e=json.loads(ep.read_text());P=[tuple(tuple(decode(z) for z in row) for row in face) for face in e['face_projectors']]
    E=tuple(row for face in P for row in face) # unnormalized encoder, E*E=2I
    ops={s:[[G0]*8 for _ in range(8)] for s in 'LGN'}
    for row in e['arrows']:ops[row['stage']][row['target']][row['source']]=decode(row['weight'])
    for s,A in ops.items():assert gmm(A,E)==E
    assert gmm(adj(E),E)==sm(2,ident(2))
    ell=E[0];dark=(neg(ell[1]),ell[0]);bright=tuple(gc(z) for z in ell)
    assert act((ell,),dark)==(G0,) and norm(dark)==norm(bright) and norm(dark)!=0
    x=tuple(ga(a,b) for a,b in zip(bright,dark));y=tuple(ga(a,neg(b)) for a,b in zip(bright,dark))
    assert x!=y and norm(x)==norm(y) and act((ell,),x)==act((ell,),y)
    ex,ey=act(E,x),act(E,y)
    for A in ops.values():assert act(A,ex)==ex and act(A,ey)==ey
    # Invariant unit relation carries only norm. Orthogonal companion does
    # not signify a second occupied electron.
    companion=lambda z:(neg(gc(z[1])),gc(z[0]))
    pairing=lambda z,w:ga(gm(z[0],w[1]),neg(gm(z[1],w[0])))
    assert pairing(x,companion(x))==pairing(y,companion(y))==(norm(x),D())
    pport=ports.index(('AB','x'));host=[(D(z[0]),D(0,z[1])) for z in [r[pport] for r in Np]]
    assert any(z!=G0 for z in host)
    # Rank-one projected link: output = Np e_ABx * ell z. The raw primitive
    # itself has only one supported coefficient; normalization not altered.
    assert tuple(gm(z,act((ell,),x)[0]) for z in host)==tuple(gm(z,act((ell,),y)[0]) for z in host)
    qi=(F(0),F(1),F(0),F(0));qj=(F(0),F(0),F(1),F(0))
    options=[]
    for q in (qi,qj):
        U=spin(q);second=gmm((ell,),U)[0];O=(ell,second)
        if determinant2(O)!=G0:
            inv=inverse2(O);assert gmm(inv,O)==ident(2)
            options.append({'quaternion':list(map(str,q)),'logical_action':mat(U),'observation':mat(O),'inverse':mat(inv)})
    assert options
    # A scalar norm alone is invariant; a fixed complex arrow is not an
    # invariant SU2 scalar. Rotating the state while holding the link fixed
    # explicitly extends the interaction/readout schedule.
    assert act((ell,),x)!=act((gmm((ell,),spin(qi))[0],),x) or act((ell,),y)!=act((gmm((ell,),spin(qi))[0],),y)

    atlas_packet=json.loads(ap.read_text());verify_atlas(atlas_packet)
    atlas=atlas_packet['record'];hostT=source_host(atlas_packet);p,n,recovery=parameters(atlas_packet['source'])
    tv=hostT['vertices'];bv=atlas['vertices'];faceowners=atlas['original_fold_owners']
    # Product triangulation with global vertex orders, ensuring shared-face
    # staircase compatibility. T is a2-disk; B is the complete refined2-sphere.
    vertices={f'T:{t}|B:{b}':{'host':t,'potential':b,'depth':str(depth(tuple(map(F,tv[t])))),
                    'mode_vertex':atlas['projection'][b]} for t in tv for b in bv}
    maximal=[];owners=[]
    for tf in hostT['maximal_simplices']:
        ta=sorted(tf)
        for bf,owner in zip(atlas['oriented_faces'],faceowners):
            ba=sorted(bf)
            for horizontal in combinations(range(4),2):
                i=j=0;path=[f'T:{ta[i]}|B:{ba[j]}']
                for step in range(4):
                    if step in horizontal:i+=1
                    else:j+=1
                    path.append(f'T:{ta[i]}|B:{ba[j]}')
                maximal.append(path);owners.append(owner)
    assert len(maximal)==1296 and len(vertices)==140 and len({tuple(o) for o in owners})==24
    for cell in maximal:
        coordinates=[tuple(map(F,tv[vertices[v]['host']]))+tuple(map(F,bv[vertices[v]['potential']]['barycentric'])) for v in cell]
        difference=[[x-y for x,y in zip(z,coordinates[0])] for z in coordinates[1:]]
        assert rational_rank(difference)==4
        # A generic point of EVERY maximal cell checks both retained maps:
        # x is its independent location; potential v carries its own Gamma(v).
        weights=[F(k,15) for k in (1,2,3,4,5)]
        point=tuple(sum(w*z[i] for w,z in zip(weights,coordinates)) for i in range(7));hx=depth(point[:3]);v=point[3:]
        assert hx==sum(w*F(vertices[k]['depth']) for w,k in zip(weights,cell))
        z=mode(p,direction(v))
        image_values=[atlas['image']['vertices'][vertices[k]['mode_vertex']]['value'] for k in cell]
        interpolated=tuple(tuple(sum(w*F(value[a][b]) for w,value in zip(weights,image_values)) for b in range(2)) for a in range(3))
        assert tuple(z)==interpolated
        # In the free-mode pullback the interface t equals h(x) and z equals
        # the independently checked potential image; both projections retain x,v.
        assert hx>=0 and hx<=1
    q=(F(1,3),)*3
    assert depth(q)==0
    # Product maximal4-cells do not lie in this2-fiber; select all product
    # cells at fixed host barycentre instead of falsely selecting only maxima.
    fiber_faces=[[f'T:012|B:{v}' for v in face] for face in atlas['oriented_faces']]
    assert len(fiber_faces)==36 and betti_mod2(fiber_faces)==[1,0,1]
    assert betti_mod2(maximal)==[1,0,1,0,0]
    assert len(lifts(q))==2 and len({tuple(o) for o in owners})==24
    fixed=json.loads((base/'results/host_coefficient_pullback_store.json').read_text())
    fixedowners={tuple(o) for o in fixed['record']['original_fold_owners']}
    assert len(fixedowners)==8
    # Fold witness and mode remain distinct: source atlas supplies actual
    # different vertices with the same image (not just a counting argument).
    bymode={}
    for b,image in atlas['projection'].items():bymode.setdefault(image,[]).append(b)
    collision=next((image,vs[:2]) for image,vs in bymode.items() if len(vs)>1)
    assert collision[1][0]!=collision[1][1]
    result={'status':'passed','verification_passed':True,'schema':'marici.voevodsky.proton-electron-single-link-potential.v1',
      'classification':'candidate_single_coefficient_link_kernel_and_fold_retaining_free_mode_pullback',
      'active_obligation':c['active_obligation'],'link':{'source':['electron_raw','face0','spin0'],'target':['proton_raw','AB','x'],'weight':'1',
        'logical_covector':mat((ell,)),'logical_dark_vector':[encode(z) for z in dark],
        'pair_x':[encode(z) for z in x],'pair_y':[encode(z) for z in y],
        'equal_logical_norm_squared':[str(norm(x).a),str(norm(x).b)],'same_link_reading':[encode(z) for z in act((ell,),x)],
        'same_persistent_norm_relation':True,'both_inputs_fixed_by_every_native_electron_stage':True,
        'projected_logical_rank':1,'hidden_logical_dimension':1,'two_source_rotation_reading_decoders':options},
      'potential_pullback':{'formula':'{((x,z),(t,v)):t=h_T(x),z=Gamma(v)} is isomorphic to T x B',
        'vertices':vertices,'maximal_simplices':maximal,'fold_owners':owners,'counts':{str(k):len(v) for k,v in complex_cells(maximal).items()},
        'maximum_affine_dimension':4,'betti_mod2':[1,0,1,0,0],'retained_original_fold_interiors':24,
        'at_host_barycentre':{'complete_potential_boundary_retained':True,'potential_atlas_vertices':20,'triangles':36,'betti_mod2':[1,0,1]},
        'fixed_position_comparison':{'retained_fold_interiors':8,'omitted':16,'centre_direction_fibre_cardinality':2},
        'same_mode_distinct_potential_witness':{'mode_vertex':collision[0],'potential_vertices':collision[1]}},
      'spinor_to_potential_realization_map_constructed':False,'potential_mode_to_single_link_scalar_map_constructed':False,
      'coupling_endpoint_or_strength_source_selected':False,'hermitian_reciprocal_interaction_constructed':False,
      'physical_electron_proton_binding_derived':False,'scope':c['scope'],'shared_sources_or_stores_modified':False}
    paths=[cp,pp,ep,ap,base/'results/host_coefficient_pullback_store.json',Path(__file__),base/'checkers/check_electron_tetrahedral_spinor.py',base/'checkers/check_host_coefficient_pullback.py',base/'checkers/check_projector_fold_sheets.py',base/'checkers/check_fold_coefficient_attachment.py',base/'checkers/potential_complex_pullback.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}
    out=base/'results/proton-electron-single-link-potential-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','one_link_hidden_electron_dimension':1,'same_norm_pair':True,
       'retained_fold_interiors':24,'previous_fixed_position_retained':8,'potential_real_dimension':4,
       'spinor_potential_identification':False},indent=2))
if __name__=='__main__':main()
