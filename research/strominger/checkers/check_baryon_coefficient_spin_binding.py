"""Actual affine generators -> native mode actions -> conditional spin squares."""
from hashlib import sha256
from pathlib import Path
from fractions import Fraction as F
import json
import sys
from check_baryon_geometric_spin_lifts import (ROOT,A,ZERO,ONE,matrix,inverse,mm,act,identity,lift_order3,record,scale)
from check_rank_one_return_packets import LineInterface
from assemble_metric_coefficient_protocol import product,sharp,encode

def digest(p):return sha256(p.read_bytes()).hexdigest()
def sparse(M):return {(i,j):v for i,row in enumerate(M) for j,v in enumerate(row) if v!=ZERO}
def dense(M,n):return tuple(tuple(M.get((i,j),ZERO) for j in range(n)) for i in range(n))
def tensor(M,U):return {(2*i+a,2*j+b):x*y for (i,j),x in M.items() for a,row in enumerate(U) for b,y in enumerate(row) if x*y!=ZERO}
def field_real_pair(x):
    c=[F(0)]*16;c[0]=F(x[0]);c[1]=F(x[1]);return A(tuple(c))
def parse_record(M):return tuple(tuple(A(tuple(F(x.get(str(i),'0')) for i in range(16))) for x in row) for row in M)
def first_hostile(P):
    for j in range(36):
        col=tuple(P.get((i,j),ZERO) for i in range(36))
        if col!=tuple(ONE if i==j else ZERO for i in range(36)):
            i=next(i for i in range(36) if col[i]!=(ONE if i==j else ZERO))
            return {'input_coordinate':j,'reader_coordinate':i,'actual_next':col[i].record(),'identity_next':(ONE if i==j else ZERO).record()}
    raise AssertionError('source mode action unexpectedly identity')

def main():
    prereq=ROOT/'research/strominger/results/baryon-geometric-spin-lifts-v1.json'
    prior=json.loads(prereq.read_text(encoding='utf-8'));assert prior['status']=='pass'
    pins=dict(prior['source_sha256']);pins[prereq.relative_to(ROOT).as_posix()]=digest(prereq)
    additions=[Path(__file__).resolve(),ROOT/'research/voevodsky/results/belt_three_by_twelve_store.json',
               ROOT/'research/voevodsky/results/coupled_six_piece_belt_store.json',ROOT/'research/voevodsky/results/four_six_center_cones.json',
               ROOT/'research/voevodsky/results/proton_merkle_store.json']
    for p in additions:
        key=p.relative_to(ROOT).as_posix()
        if key in pins:assert pins[key]==digest(p),'stale imported source '+key
        pins[key]=digest(p)
    for module in tuple(sys.modules.values()):
        file=getattr(module,'__file__',None)
        if file:
            p=Path(file).resolve()
            if p.suffix=='.py' and p.is_relative_to(ROOT/'research'):
                key=p.relative_to(ROOT).as_posix()
                if key in pins:assert pins[key]==digest(p),'stale module '+key
                pins[key]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'stale prerequisite'
    sources={n:json.loads((ROOT/prior['carriers'][n]['source']).read_text(encoding='utf-8')) for n in ('proton','neutron')}
    fs={n:LineInterface(ROOT/f'research/strominger/results/common-three-carrier-protocol/{n}.json') for n in sources}
    actions={};construction={}
    # Exact source0/e1/e2/e3 -> retained native A/B/C/D correspondence.
    native_vertices=matrix(((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)))
    V=tuple(tuple(native_vertices[j+1][i]-native_vertices[0][i] for j in range(3)) for i in range(3))
    Vinv=inverse(V)
    assert mm(tuple(zip(*V)),V)==matrix(sources['proton']['metric'])
    merkle=json.loads((ROOT/'research/voevodsky/results/proton_merkle_store.json').read_text(encoding='utf-8'))
    geom=merkle['objects'][merkle['objects'][merkle['root']]['geometry']]['payload']
    placements=sorted(geom['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    assert [r['outer_arrow']+':'+a for r in placements for a in 'xyz']==fs['proton'].data['source']['coordinates']
    rotation_table=[matrix(r['rotation']) for r in placements]
    for index,g in enumerate(sources['proton']['generators']):
        T=matrix(g['matrix']);t=tuple(A(F(x)) for x in g['translation'])
        mapped=[]
        for j,v in enumerate(((ZERO,ZERO,ZERO),(ONE,ZERO,ZERO),(ZERO,ONE,ZERO),(ZERO,ZERO,ONE))):
            q=tuple(x+y for x,y in zip(act(T,v),t))
            target=tuple(x+y for x,y in zip(act(V,q),native_vertices[0]))
            mapped.append(native_vertices.index(target))
        R=mm(mm(V,T),Vinv);P={}
        for slot,Rt in enumerate(rotation_table):
            destination=rotation_table.index(mm(R,Rt))
            for i,row in enumerate(R):
                for j,x in enumerate(row):
                    if x!=ZERO:P[3*destination+i,3*slot+j]=x
        actions['proton',index]=P
        construction['proton',index]={'vertex_permutation':mapped,'native_spatial_rotation':record(R)}
    # Actual source-neutron Cartesian frame, then actual plane embedding/decoder.
    S2=A(tuple(F(i==1) for i in range(16)))
    Vn=((ZERO,A(F(2,3))*S2,A(F(4,3))),(-A(2),A(F(2,3))*S2,-A(F(2,3))),(A(2),A(F(2,3))*S2,-A(F(2,3))))
    source=sources['neutron'];T=matrix(source['generators'][0]['matrix']);R=mm(mm(Vn,T),inverse(Vn))
    assert mm(tuple(zip(*Vn)),Vn)==scale(A(F(8,3)),matrix(source['metric']))
    assert R==matrix(((0,0,1),(1,0,0),(0,1,0)))
    ambient=json.loads((ROOT/'research/voevodsky/results/coupled_six_piece_belt_store.json').read_text(encoding='utf-8'))['record']
    geometry=json.loads((ROOT/'research/voevodsky/results/four_six_center_cones.json').read_text(encoding='utf-8'))
    intrinsic=json.loads((ROOT/'research/voevodsky/results/belt_three_by_twelve_store.json').read_text(encoding='utf-8'))
    points={k:tuple(A(F(x)) for x in v) for k,v in geometry['belt_scaled_coordinates'].items()}
    assert all(tuple(A(F(x)) for x in seed['point']) in points.values() for seed in source['seeds'])
    for face in geometry['belt_faces']:
        points['F_'+'_'.join(sorted(face))]=tuple(sum((points[k][i] for k in face),ZERO)/A(3) for i in range(3))
    rename={k:next(label for label,q in points.items() if q==act(T,v)) for k,v in points.items()}
    triangles=[tuple(t) for t in ambient['triangles']]
    permutation=[triangles.index(tuple(rename[k] for k in t)) for t in triangles]
    Pambient={(3*permutation[t]+i,3*t+j):x for t in range(18) for i,row in enumerate(R) for j,x in enumerate(row) if x!=ZERO}
    W={(r['ambient_target'],r['intrinsic_source']):field_real_pair(r['numerator']) for r in intrinsic['embedding_entries']}
    d=tuple(F(c['d']) for c in intrinsic['coordinates'])
    Emb={k:x/A(d[k[1]]) for k,x in W.items()};Dec={(j,i):x for (i,j),x in W.items()}
    assert product(Dec,Emb)==sparse(identity(36))
    P=product(product(Dec,Pambient),Emb)
    assert product(Pambient,Emb)==product(Emb,P)
    # The familiar sector shift is now derived, not assumed to represent this generator.
    sector_shift={(((s+1)%3)*12+j,s*12+j):ONE for s in range(3) for j in range(12)}
    assert P==sector_shift
    actions['neutron',0]=P
    construction['neutron',0]={'native_spatial_rotation':record(R),'ambient_triangle_permutation':permutation,
                              'intrinsic_sector_shift':1,'embedding_square':'P_ambient Emb=Emb P_intrinsic'}
    checks={'proton_actual_source_vertex_dictionary_and_native_port_order':True,
            'neutron_actual_spatial_and_plane_embedding_square':True}
    rows=[]
    for (name,index),P in actions.items():
        f=fs[name];N=f.ops['N'];I36=sparse(identity(36));column={(i,0):x for i,x in enumerate(f.column) if x!=ZERO}
        row={(0,j):x for j,x in enumerate(f.row) if x!=ZERO}
        assert P!=I36 and product(product(P,P),P)==I36 and sharp(P,f.metric)==product(P,P)
        assert product(P,column)==column and product(row,P)==row
        assert product(P,N)==product(N,P)==N
        for stage in ('L','G'):
            assert product(P,f.ops[stage])==product(f.ops[stage],P)
        chi=ONE
        Ktilde={(2*i+a,a):x for i,x in enumerate(f.column) for a in range(2) if x!=ZERO}
        Dtilde={(a,2*i+a):x for i,x in enumerate(f.row) for a in range(2) if x!=ZERO}
        U=parse_record(prior['carriers'][name]['generators'][index]['positive_scalar_spin_lift'])
        for sign in (ONE,-ONE):
            spin=scale(sign,U);S=tensor(P,spin)
            assert product(S,Ktilde)==product(Ktilde,sparse(spin))
            assert product(Dtilde,S)==product(sparse(spin),Dtilde)
        # Identity substitution passes the line square but fails a retained raw-mode reader.
        assert product(I36,column)==column
        hostile=first_hostile(P)
        rows.append({'carrier':name,'source_generator':index,'construction':construction[name,index],
                     'coefficient_action':encode(P),'line_character':chi.record(),'identity_substitution_hostile':hostile,
                     'spin_square':'(P tensor (+/-U)) K_tilde=K_tilde (+/-U)','lift_choice_selected':False})
        checks[name+'_generator'+str(index)+'_actual_mode_action_and_unit_line_character']=True
        checks[name+'_generator'+str(index)+'_both_spin_squares_and_identity_erasure_hostile']=True
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    checks['all_upstream_native_sources_and_receipts_unchanged']=True
    report={'schema':'marici.baryon-coefficient-spin-binding.v1','status':'pass','checks':checks,'bindings':rows,
      'scope':'Actual native36-mode spatial-alignment transport and conditional doubled spin action for all actual source generators; not local cyclic-mode phase or physical interaction.',
      'line_characters':'all three tested source spatial generators have chi=1, but are nonidentity coefficient actions',
      'remaining':['source-supported lift/frame selection','charge/magnetic/internal coupling and resource law','primitive operation implementation/cost'],
      'source_sha256':pins,'native_producers_executed':False,'formal_proof_recompiled':False,'physical_coupling_claim':False}
    (ROOT/'research/strominger/results/baryon-coefficient-spin-binding-v1.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('bindings','source_sha256')},indent=2))
if __name__=='__main__':main()
