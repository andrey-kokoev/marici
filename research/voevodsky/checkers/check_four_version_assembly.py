"""Actual construction-record square, not maps between compressed end states.
Build every endpoint from one seed. Reference coefficient stores are read only
by the comparison harness, never by the constructors below.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from copy import deepcopy
from hashlib import sha256
import json
import check_coupled_six_piece_belt as c
from check_belt_operator_inputs import frame,action,mode,mean
from check_belt_three_by_twelve import sparse_product
from check_four_six_center_cones import outward,squared
from check_particle_construction_routes import R,cast,ident,scale,adj,trace,cross,dot,sub,projector,sum_m,return_matrix,encode,decode3
from check_signed_belt_tetrahedral_parent import norminv
from check_electron_charge_spin_frontier import ga,gs,gm,gmm,G0
BASE=Path(__file__).resolve().parents[1]
SEED=BASE/'contracts/four-version-assembly-seed.json'
def digest(o):return sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def point_strings(p):return {k:list(map(str,v)) for k,v in p.items()}
def point_values(p):return {k:tuple(map(F,v)) for k,v in p.items()}
def tetrahedron(seed):
    return {'kind':'tetrahedron','points':point_strings(point_values(seed['tetrahedron'])),
        'faces':deepcopy(seed['ordered_tetrahedral_faces']),'signs':[1]*4,'metric':[1,1,1]}

def belt_geometry(t,seed):
    assert t['kind']=='tetrahedron'
    old=point_values(t['points']);display=point_values(seed['display_template_scaled'])
    # Derive and APPLY the explicitly declared seed-to-display similarity.
    M=tuple(tuple(sum(display[k][i]*old[k][j] for k in old)/4 for j in range(3)) for i in range(3))
    placed={k:tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3)) for k,v in old.items()}
    assert placed==display
    assert dot(M[0],cross(M[1],M[2]))==-F(3,32)
    assert {squared(placed[a],placed[b],(3,2,1)) for a,b in combinations(old,2)}=={3}
    gap=F(seed['gap']);assert gap==F(7,10) # Current exact coefficient field.
    points={'O':(F(0),)*3}
    for i,label in enumerate(seed['base_labels']):
        x,y,z=placed[label];assert y==-F(1,4)
        points['U'+str(i)]=(x,gap/2,z)
        points['L'+str(i)]=(x,-gap/2,-z)
    upper=['U0','U1','U2'];lower=['L0','L1','L2']
    stitches={(u,l) for u in upper for l in sorted(lower,key=lambda l:squared(points[u],points[l],(3,1,1)))[:2]}
    faces=[outward([u]+sorted(l for a,l in stitches if a==u),points) for u in upper]
    faces += [outward([l]+sorted(u for u,b in stitches if b==l),points) for l in lower]
    signs=[1 if mean([points[k] for k in f])[1]>0 else -1 for f in faces]
    return {'kind':'belt','points':point_strings(points),'faces':list(map(list,faces)),
        'signs':signs,'metric':[3,1,1],'seed_placement_matrix':list(map(lambda r:list(map(str,r)),M))}

def assemble_modes(vectors,metric,transports):
    """Shared weighted local-mode / alignment / return assembler for P and N."""
    g=len(vectors);m=len(metric);D=tuple(tuple(metric[i] if i==j else F(0) for j in range(m)) for i in range(m))
    k=sum(c.norm(v)/d for v,d in zip(vectors[0],metric));assert c.positive(k)
    for v,A in zip(vectors,transports):
        assert c.mv(A,vectors[0])==v and c.mm(c.mm(A,D),c.transpose(A))==D
        assert sum(c.norm(x)/d for x,d in zip(v,metric))==k
    u=tuple(x for v in vectors for x in v);ds=tuple(metric)*g
    L={(m*t+i,m*t+j):c.scale(1/k,c.mul(a,c.conj(b))) for t,v in enumerate(vectors) for i,a in enumerate(v) for j,b in enumerate(v) if a!=c.Z and b!=c.Z}
    G={}
    for i,A in enumerate(transports):
        for j,B in enumerate(transports):
            block=c.mm(c.mm(A,D),c.transpose(B))
            G.update({(m*i+a,m*j+b):(c.R(x/g),c.R()) for a,row in enumerate(block) for b,x in enumerate(row) if x})
    N={(i,j):c.scale(1/(g*k),c.mul(a,c.conj(b))) for i,a in enumerate(u) for j,b in enumerate(u) if a!=c.Z and b!=c.Z}
    assert sum(c.norm(x)/d for x,d in zip(u,ds))==g*k # Exact rank-one projector normalization.
    assert sparse_product(G,L,ds)==sparse_product(L,G,ds)==N
    return L,G,N

def assemble_proton(body,seed):
    assert seed['reference_triangle']==['F_ABC','A','B']
    points=point_values(body['points']);old=dict(points)
    for f in combinations('ABCD',3):points['F_'+''.join(f)]=mean([points[k] for k in f])
    group={(0,1,2,3)};pending=list(group)
    while pending:
        q=pending.pop()
        for g in seed['tetrahedral_generators']:
            p=tuple(g[q[i]] for i in range(4))
            if p not in group:group.add(p);pending.append(p)
    assert len(group)==12
    character=(c.ONE,(c.R(-F(1,2)),c.R(F(1,2))),(c.R(-F(1,2)),c.R(-F(1,2))))
    records=[];vectors=[];rotations=[];labels=[]
    for p in sorted(group):
        a,b,d=('ABCD'[p[i]] for i in range(3));tri=('F_'+''.join(sorted((a,b,d))),a,b)
        rot=tuple(tuple(sum(old['ABCD'[p[k]]][i]*old['ABCD'[k]][j] for k in range(4))/4 for j in range(3)) for i in range(3))
        vectors.append(c.mv(c.transpose(tuple(points[k] for k in tri)),character));rotations.append(rot);labels.append(a+b)
        records.append({'outer_arrow':a+b,'triangle':list(tri),'rotation':[list(map(str,r)) for r in rot]})
    L,G,N=assemble_modes(vectors,(F(1),)*3,rotations)
    arrows=[]
    for s,m in [('L',L),('G',G),('N',N)]:
        for (i,j),z in m.items():arrows.append({'stage':s,'target':[labels[i//3],'xyz'[i%3]],'source':[labels[j//3],'xyz'[j%3]],'coefficient':c.encoded(z)})
    return {'kind':'cyclic','coordinates':'Cartesian tetrahedral source frame','triangles':records,'arrows':sorted(arrows,key=lambda r:(r['stage'],r['target'],r['source']))}

def assemble_neutron(body,seed):
    points=point_values(body['points']);faces=body['faces'];triangles=[];owners=[]
    for i,f in enumerate(faces):
        centre='F_'+'_'.join(sorted(f));points[centre]=mean([points[k] for k in f])
        triangles.extend((centre,f[j],f[(j+1)%3]) for j in range(3));owners.extend([i]*3)
    coords={k:frame(v) for k,v in points.items()};inverse={v:k for k,v in coords.items()}
    rot=((F(0),F(0),F(1)),(F(1),F(0),F(0)),(F(0),F(1),F(0)))
    rename={k:inverse[action(rot,v)] for k,v in coords.items()};indices={t:i for i,t in enumerate(triangles)}
    perm=[indices[tuple(rename[k] for k in t)] for t in triangles]
    faceperm=[next(j for j,f in enumerate(faces) if set(f)=={rename[k] for k in face}) for face in faces]
    adjacent=[j for j in range(1,6) if len(set(faces[0])&set(faces[j]))==2]
    pair=(0,adjacent[0]);pairs=[]
    for _ in range(3):pairs.append(pair);pair=tuple(faceperm[i] for i in pair)
    ref=[i for i in range(18) if owners[i] in pairs[0]]
    order=ref+[perm[i] for i in ref]+[perm[perm[i]] for i in ref]
    assert sorted(order)==list(range(18))
    planes=[]
    for t in triangles:
        rr,ss=mode(t,points);r=tuple(c.R(*v) for v in rr);s=tuple(c.R(*v) for v in ss)
        a=sum(v*v for v in s);b=sum(v*w for v,w in zip(r,s));assert a.b==b.b==0
        a,b=a.a,b.a;v=tuple(x-b/a*y for x,y in zip(r,s));beta=sum(x*x for x in v);assert beta.b==0
        planes.append({'d':(a,beta.a),'z':((c.R(b),c.R(a)),(c.R(beta.a),c.R()))})
    coordinates=[{'triangle':t,'axis':a,'d':str(planes[t]['d'][a]),'selected_numerator':c.encoded(planes[t]['z'][a])} for t in order for a in range(2)]
    ds=tuple(F(v['d']) for v in coordinates)
    z=tuple((planes[t]['z'][a] if body['signs'][owners[t]]==1 else c.conj(planes[t]['z'][a])) for t in order for a in range(2))
    assert ds[:12]==ds[12:24]==ds[24:] and z[:12]==z[12:24]==z[24:]
    I12=tuple(tuple(F(int(i==j)) for j in range(12)) for i in range(12))
    L,G,N=assemble_modes([z[i:i+12] for i in range(0,36,12)],ds[:12],[I12]*3)
    return {'kind':'cyclic','coordinates':coordinates,'triangle_order':order,'triangles':list(map(list,triangles)),
        'pairs':list(map(list,pairs)),'selected_numerators':[c.encoded(v) for v in z],
        'arrows':[{'stage':s,'target':i,'source':j,'numerator':c.encoded(v)} for s,m in [('L',L),('G',G),('N',N)] for (i,j),v in sorted(m.items())]}

def assemble_spinor(body,seed,erase_signs=False):
    pp=point_values(body['points'])
    points={k:((R((0,v[0],0,0)),cast(v[1]),cast(v[2])) if body['kind']=='belt' else tuple(map(cast,v))) for k,v in pp.items()}
    normals=[]
    for f in body['faces']:
        a,b,c0=[points[k] for k in f];v=cross(sub(b,a),sub(c0,a));q=dot(v,v)
        assert all(x==0 for x in q.c[1:]);n=tuple(x*norminv(q.c[0]) for x in v);assert dot(n,n)==1;normals.append(n)
    signs=[1]*len(normals) if erase_signs else body['signs']
    ps=[projector(n,s) for n,s in zip(normals,signs)];S=sum_m(ps)
    determinant=ga(gm(S[0][0],S[1][1]),gs(-1,gm(S[0][1],S[1][0])))
    assert determinant[1]==0 and all(x==0 for x in determinant[0].c[1:]) and determinant[0].c[0]>0
    inv=scale(1/determinant[0].c[0],((S[1][1],gs(-1,S[0][1])),(gs(-1,S[1][0]),S[0][0])))
    size=2*len(ps);N=return_matrix(ps,inv)
    L=tuple(tuple(ps[i//2][i%2][j%2] if i//2==j//2 else G0 for j in range(size)) for i in range(size))
    assert gmm(N,N)==N and adj(N)==N and trace(N)==(cast(2),cast(0)) and gmm(N,L)==N
    return {'kind':'spinor','normals':[[list(map(str,x.c)) for x in n] for n in normals],
        'frame_operator':[[encode(z) for z in row] for row in S],'frame_inverse':[[encode(z) for z in row] for row in inv],
        'arrows':[{'stage':s,'target':i,'source':j,'weight':encode(m[i][j])} for s,m in [('L',L),('G',N),('N',N)] for i in range(size) for j in range(size) if m[i][j]!=G0]}

def construct(seed,body,carrier):
    protocol=assemble_spinor(body,seed) if carrier=='spinor' else (assemble_proton(body,seed) if body['kind']=='tetrahedron' else assemble_neutron(body,seed))
    return {'seed':deepcopy(seed),'geometry':deepcopy(body),'carrier':carrier,'protocol':protocol}
def belting(record):return construct(record['seed'],belt_geometry(record['geometry'],record['seed']),record['carrier'])
def spinorize(record):return construct(record['seed'],record['geometry'],'spinor')
def convert(record,body_kind,carrier):
    """Edit the retained recipe and REBUILD; never invert a final state."""
    out=record
    if out['geometry']['kind']!=body_kind:
        out=belting(out) if body_kind=='belt' else construct(out['seed'],tetrahedron(out['seed']),out['carrier'])
    if out['carrier']!=carrier:out=construct(out['seed'],out['geometry'],carrier)
    return out

def main():
    seed_raw=SEED.read_bytes();seed=json.loads(seed_raw)
    # Both paths execute actual intermediate assemblers. No reference output
    # artifact is available to these functions.
    P=construct(seed,tetrahedron(seed),'cyclic')
    E=spinorize(P);X_via_E=belting(E)
    N=belting(P);X_via_N=spinorize(N)
    assert X_via_E==X_via_N and digest(X_via_E)==digest(X_via_N)
    # Read the existing endpoints ONLY NOW, for independent full comparison.
    paths={'P':c.PROTON,'N':BASE/'results/opposite_branch_belt_store.json',
        'E':BASE/'results/electron_tetrahedral_spinor_store.json','X':BASE/'results/conditional_fourth_spinor_store.json',
        'geometry':BASE/'results/four_six_center_cones.json'}
    raw={k:p.read_bytes() for k,p in paths.items()};expected={k:json.loads(v) for k,v in raw.items()}
    verified,pr=c.verify_proton(expected['P']);assert verified['verified']
    sm={'raw':'L','local':'G','aligned':'N'}
    pa=[{'stage':sm[r['source'][0]],'target':list(r['target'][1:]),'source':list(r['source'][1:]),
        'coefficient':c.encoded((c.R(F(r['weight_real'])),c.R(F(r['weight_imag_sqrt3']))))} for r in pr]
    assert P['protocol']['arrows']==sorted(pa,key=lambda r:(r['stage'],r['target'],r['source']))
    pn=N['protocol'];assert pn['arrows']==expected['N']['arrows'] and pn['coordinates']==expected['N']['coordinates'] and pn['selected_numerators']==expected['N']['selected_numerators']
    assert N['geometry']['signs']==expected['N']['face_signs']
    assert N['geometry']['points']==expected['geometry']['belt_scaled_coordinates'] and N['geometry']['faces']==expected['geometry']['belt_faces']
    ea=[{**a,'weight':encode(decode3(a['weight']))} for a in expected['E']['arrows']]
    assert E['protocol']['arrows']==ea
    assert X_via_N['protocol']['arrows']==expected['X']['arrows']
    assert X_via_N['protocol']['frame_operator']==expected['X']['frame_operator'] and X_via_N['protocol']['frame_inverse']==expected['X']['frame_inverse']
    # Two deliberate wrong reconstructions cannot pass the square.
    wrong=assemble_spinor(N['geometry'],seed,erase_signs=True)
    assert wrong['arrows']!=X_via_E['protocol']['arrows'] and len(wrong['arrows'])==264
    from check_fourth_construction_bridge import decode,matrix
    mx=matrix(X_via_E['protocol']['arrows'],12,'N')
    old_inverse=tuple(tuple(decode(z) for z in row) for row in E['protocol']['frame_inverse'])
    lx=matrix(X_via_E['protocol']['arrows'],12,'L')
    ps=[tuple(tuple(lx[2*i+a][2*i+b] for b in range(2)) for a in range(2)) for i in range(6)]
    stale=return_matrix(ps,old_inverse);assert stale!=mx and gmm(stale,stale)!=stale
    # State-only records cannot run these procedures; missing geometry is not
    # guessed from dimensions or fitted from a desired output.
    rejected=False
    try:spinorize({'protocol':P['protocol']})
    except KeyError:rejected=True
    assert rejected
    results={'P':P,'N':N,'E':E,'X':X_via_E}
    def to(record,label):
        target=results[label]
        return convert(record,target['geometry']['kind'],target['carrier'])
    edges={(a,b):to(results[a],b) for a,b in combinations(('P','N','E','X'),2)}
    assert all(result==results[b] for (a,b),result in edges.items())
    assert all(to(result,a)==results[a] for (a,b),result in edges.items())
    faces={}
    for a,b,c0 in combinations(('P','N','E','X'),3):
        via=to(edges[a,b],c0);assert via==edges[a,c0]
        faces[a+b+c0]={'direct':a+c0,'via':[a+b,b+c0],'same_construction_content':True,'result_sha256':digest(via)}
    diagram={'id':'voevodsky-four-version-construction-instance','objects':[{'id':k,'type':'complete_construction_record_at_frozen_seed'} for k in results],
        'arrows':[{'id':a+b,'source':a,'target':b,'map_token':digest(v),'semantics':'Executed result at this fixed construction input, not a function on arbitrary states.'} for (a,b),v in edges.items()]+[{'id':f,'source':f[0],'target':f[-1],'map_token':v['result_sha256']} for f,v in faces.items()],
        'cells':[{'id':f,'routes':[[v['direct']],[f]],'witness':'Independent execution and full construction-content comparison in check_four_version_assembly.py'} for f,v in faces.items()],
        'obstructions':[],'claims':[{'id':'frozen_recipe_route_agreement','requires':['four_rebuilt_sources','four_executed_faces']},{'id':'unique_physical_four_particle_law','requires':['source_selection_of_recipe_parameters','physical_identification']}],
        'available_witnesses':['four_rebuilt_sources','four_executed_faces'],
        'higher_coherence':[{'id':'arbitrary_state_transport_or_physical_identity','degree':3,'state':'unsupported'}]}
    (BASE/'contracts/four-version-assembly-diagram.json').write_text(json.dumps(diagram,indent=2)+'\n',encoding='utf-8')
    checks={'all_four_protocols_reconstructed_without_reference_coefficients':True,
        'proton_all_1836_coefficients_match':len(pa)==1836,
        'neutron_all_1836_coefficients_and_intrinsic_coordinates_match':len(pn['arrows'])==1836,
        'electron_all_144_coefficients_match':len(ea)==144,
        'fourth_all_312_coefficients_match':len(mx)==12 and len(X_via_E['protocol']['arrows'])==312,
        'both_routes_same_complete_construction_content':X_via_E==X_via_N,
        'all_six_recipe_comparisons_rebuild_the_correct_endpoint':all(v==results[b] for (a,b),v in edges.items()),
        'all_six_reverse_recipe_edits_restore_source_content':True,
        'all_four_triangular_routes_agree':all(v['same_construction_content'] for v in faces.values()),
        'retained_belt_geometry_and_branch_signs_match':True,
        'sign_erasure_breaks_route_agreement':wrong['arrows']!=X_via_E['protocol']['arrows'],
        'copied_electron_normalization_breaks_return':gmm(stale,stale)!=stale,
        'state_only_input_rejected':rejected,
        'seed_and_reference_files_unchanged':SEED.read_bytes()==seed_raw and all(p.read_bytes()==raw[k] for k,p in paths.items())}
    report={'verification_passed':all(checks.values()),'checks':checks,
        'classification':'exact_commuting_reconstruction_square_on_retained_construction_records',
        'source_operation':'B constructs the signed belt and reassembles the current carrier; S replaces the local carrier by signed Pauli projections and reassembles.',
        'routes':[['P','S','E','B','X'],['P','B','N','S','X']],
        'four_faces':faces,
        'reverse_operation_scope':'Restore the retained seed geometry or cyclic recipe and rebuild. These are inverses of recipe edits on the four generated records, not physical reversals or recovery from compressed states.',
        'endpoint_content_sha256':{k:digest(v) for k,v in results.items()},
        'fourth_via_E_sha256':digest(X_via_E),'fourth_via_N_sha256':digest(X_via_N),
        'support_counts':{k:len(v['protocol']['arrows']) for k,v in results.items()},
        'common_start':str(SEED.relative_to(BASE.parent.parent)).replace('\\','/'),
        'supplied_choices':['labelled tetrahedron and primitive cyclic generators','explicit display placement and raw frame conventions','gap 7/10','first C3-invariant adjacent matching','alternating belt branch rule','signed Pauli carrier rule and fresh frame normalization'],
        'comparison_scope':'Geometry, labels, signs, seed choices, coordinates and all coefficients at the endpoint are compared. Execution histories remain distinct and are recorded as separate routes.',
        'not_claimed':'No lossless linear map between unlike selected-state dimensions; no unique derivation of the supplied choices; no physical particle-identification; six-edge agreement is at the declared construction-record level only.',
        'source_sha256':{k:sha256(v).hexdigest() for k,v in raw.items()},'seed_sha256':sha256(seed_raw).hexdigest(),'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/four_version_assembly.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/four_version_assembly_records.json').write_text(json.dumps(results,separators=(',',':'))+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)
if __name__=='__main__':main()
