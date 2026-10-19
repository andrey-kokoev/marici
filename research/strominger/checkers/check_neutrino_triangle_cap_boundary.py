"""Arrow-first disk boundary and actual neutron-cap comparison. No spin/charge.
Only pure inherited assemblers run; old producers and gallery are untouched.
"""
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble,apply,subtract,dot_metric
from check_relative_geometry_mode_selection import select
from check_neutrino_arrow_seed_science import rank

CONTRACT=ROOT/'research/strominger/contracts/neutrino-triangle-cap-boundary.v1.json'
OUT=ROOT/'research/strominger/results/neutrino-triangle-cap-boundary-v1.json'
REGISTRY=ROOT/'research/strominger/results/neutrino_seed_candidates.json'
NEUTRON=ROOT/'research/voevodsky/inputs/mode-neutron.json'
PROTON=ROOT/'research/voevodsky/inputs/relative-proton.json'


def digest(p):return sha256(p.read_bytes()).hexdigest()
def generator(raw):return (tuple(tuple(map(F,row)) for row in raw['matrix']),tuple(map(F,raw['translation'])))
def mm(A,B):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def mv(A,v):return tuple(sum((x*y for x,y in zip(row,v)),F(0)) for row in A)
def tr(A):return list(map(list,zip(*A)))
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def centroid(points):return tuple(sum(p[k] for p in points)/len(points) for k in range(len(points[0])))
def score(p,source):
    G=[list(map(F,row)) for row in source['metric']]
    return sum((dot_metric(v,v,G) for raw in source['generators'] for v in [subtract(apply(generator(raw),p),p)]),F(0))
def parity(order):return (-1)**sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))


def boundaries(cells,nvertices):
    edges=sorted({tuple(sorted(edge)) for cell in cells for edge in combinations(cell,2)})
    B2=[[F(0)]*len(cells) for _ in edges]
    for j,cell in enumerate(cells):
        for k in range(3):
            face=cell[:k]+cell[k+1:]
            B2[edges.index(tuple(sorted(face)))][j]+=(-1)**k*parity(face)
    B1=[[F(int(v==b)-int(v==a)) for a,b in edges] for v in range(nvertices)]
    return edges,B1,B2


def scalar_add(a,b):return a[0]+b[0],a[1]+b[1]
def scalar_mul(a,b):return a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scalar_sum(xs):
    out=(F(0),F(0))
    for x in xs:out=scalar_add(out,x)
    return out


def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x


def main():
    contract=json.loads(CONTRACT.read_text(encoding='utf-8'))
    registry=json.loads(REGISTRY.read_text(encoding='utf-8'))
    source=registry['candidates'][0]['source']
    assert source['seeds'][0]['role']=='carrier'
    geometry=assemble(source)
    assert geometry['dimension']==2 and len(geometry['vertices'])==3
    assert len(geometry['supporting_facets'])==len(geometry['cone_cells'])==3
    assert not geometry['retained_attachment_interfaces']
    nsource=json.loads(NEUTRON.read_text(encoding='utf-8'))
    neutron,_=select(nsource)
    assert neutron['dimension']==3 and len(neutron['external_interfaces'])==2
    assert len(neutron['carrier_facets'])==6
    pins={str(p.relative_to(ROOT)).replace('\\','/'):digest(p) for p in (CONTRACT,REGISTRY,NEUTRON,PROTON,Path(__file__).resolve())}
    for rel in contract['authoritative_sources']:
        pins[rel]=digest(ROOT/rel)
    for module in tuple(sys.modules.values()):
        file=getattr(module,'__file__',None)
        if file:
            p=Path(file).resolve()
            if p.is_relative_to(ROOT/'research') and p.suffix=='.py':pins[p.relative_to(ROOT).as_posix()]=digest(p)
    vertices=[tuple(map(F,p)) for p in geometry['vertices']]
    c=geometry['center_vertex_id'];points=vertices+[tuple(map(F,geometry['center']))]
    assert c==3
    cells=[list(cell) for cell in geometry['cone_cells']]
    edges,B1,B2=boundaries(cells,4)
    assert len(edges)==6 and rank(B2)==3
    assert mm(B1,B2)==[[F(0)]*3 for _ in range(4)]
    radial=[i for i,e in enumerate(edges) if c in e]
    outer=[i for i,e in enumerate(edges) if c not in e]
    assert len(radial)==len(outer)==3 and rank([B2[i] for i in radial])==2
    D=[F(1)]*3;b=mv(B2,D)
    assert all(b[i]==0 for i in radial) and all(abs(b[i])==1 for i in outer)
    g=generator(source['generators'][0]);index={p:i for i,p in enumerate(points)}
    vp=[index[apply(g,p)] for p in points]
    assert vp[c]==c and all(vp[vp[vp[i]]]==i for i in range(4))
    T0=[[F(i==vp[j]) for j in range(4)] for i in range(4)]
    T1=[[F(0)]*6 for _ in range(6)]
    for j,e in enumerate(edges):
        target=[vp[a] for a in e]
        T1[edges.index(tuple(sorted(target)))][j]=parity(target)
    T2=[[F(0)]*3 for _ in range(3)]
    for j,cell in enumerate(cells):
        target=[vp[a] for a in cell]
        k=next(k for k,other in enumerate(cells) if sorted(other)==sorted(target))
        positions=[cells[k].index(v) for v in target]
        T2[k][j]=parity(positions)
    assert mm(B2,T2)==mm(T1,B2) and mm(B1,T1)==mm(T0,B1)
    assert mm(mm(T1,T1),T1)==eye(6) and mv(T2,D)==tuple(D)
    q0=tuple(map(F,source['seeds'][0]['point']))
    ordered=[q0,apply(g,q0),apply(g,apply(g,q0))]
    assert ordered==[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
    orbit=[vertices.index(p) for p in ordered]
    arrow_edges=[(orbit[i],orbit[(i+1)%3]) for i in range(3)]
    oriented_b=[b[edges.index(tuple(sorted(e)))]*parity(e) for e in arrow_edges]
    orientation=oriented_b[0]
    assert oriented_b==[orientation]*3 and orientation in (-1,1)
    decoder=[orientation/F(3)]*3
    assert sum(x*y for x,y in zip(decoder,oriented_b))==1
    # The fixed source filling archive recovers lambda*D. This is not recovery
    # of an arbitrary filling from an unlabelled boundary or an unfilled loop.
    for coefficient in (F(-2),F(0),F(2,3)):
        output=[coefficient*x for x in oriented_b]
        assert sum(x*y for x,y in zip(decoder,output))==coefficient
    Bcycle=[[F(int(v==(i+1)%3)-int(v==i)) for i in range(3)] for v in range(3)]
    assert rank(Bcycle)==2 and mv(Bcycle,[F(1)]*3)==(F(0),)*3
    one=(F(1),F(0));omega=(F(-1,2),F(1,2));omega2=scalar_mul(omega,omega)
    mode_residuals=[]
    for eig,mode in ((omega,[one,omega,omega2]),(omega2,[one,omega2,omega])):
        assert mode[1:]+mode[:1]==[scalar_mul(eig,x) for x in mode]
        residual=[scalar_sum((a*x[0],a*x[1]) for a,x in zip(row,mode)) for row in Bcycle]
        assert any(x!=(F(0),F(0)) for x in residual)
        mode_residuals.append({'pullback_eigenvalue':eig,'edge_mode':mode,'vertex_boundary':residual})

    oldG=[list(map(F,row)) for row in source['metric']]
    Gn=[list(map(F,row)) for row in nsource['metric']]
    A,bg=g;An,bn=generator(nsource['generators'][0])
    nv=[tuple(map(F,p)) for p in neutron['vertices']]
    caps=[]
    for cap in neutron['external_interfaces']:
        assert len(cap)==3
        p0=nv[min(cap)];p1=apply((An,bn),p0);p2=apply((An,bn),p1)
        assert apply((An,bn),p2)==p0
        assert {nv.index(p) for p in (p0,p1,p2)}==set(cap)
        J=[[p1[a]-p0[a],p2[a]-p0[a]] for a in range(3)]
        assert mm(An,J)==mm(J,A)
        assert apply((An,bn),p0)==tuple(x+y for x,y in zip(mv(J,bg),p0))
        induced=mm(tr(J),mm(Gn,J))
        assert induced==[[F(3,8)*x for x in row] for row in oldG] and induced!=oldG
        assert all(dot_metric(subtract(a,b),subtract(a,b),Gn)==3 for a,b in combinations((p0,p1,p2),2))
        cap_center=centroid((p0,p1,p2))
        assert score(cap_center,nsource)==0
        edge_scores=[score(centroid((a,b)),nsource) for a,b in ((p0,p1),(p1,p2),(p2,p0))]
        assert edge_scores==[F(3,4)]*3
        derived=deepcopy(source);derived['metric']=[[str(x) for x in row] for row in induced]
        selected,_=select(derived)
        assert selected['dimension']==2 and len(selected['carrier_facets'])==3
        assert all(F(row['score'])==F(3,4) for row in selected['mode_scores'])
        assert not selected['retained_attachment_interfaces']
        mapped_center=tuple(x+y for x,y in zip(mv(J,tuple(map(F,geometry['center']))),p0))
        assert mapped_center==cap_center
        caps.append({'neutron_cap_vertex_ids':cap,'ordered_orbit_vertices':[p0,p1,p2],
            'embedding_linear_part':J,'embedding_translation':p0,'induced_metric':induced,
            'old_metric_scale_ratio':F(3,8),'original_fixed_scale_isometry':False,
            'cap_derived_source':derived,'cap_centroid':cap_center,'cap_centroid_score':F(0),
            'edge_centroid_scores':edge_scores,
            'intrinsic_dimensions':{'standalone_main_disk':2,'edge':1,'neutron_ambient':3},
            'relative_codimensions':{'disk_in_its_own_carrier':0,'edges_in_disk':1,'disk_cap_in_neutron':1,'edges_in_neutron':2},
            'center_coning_image':'Retained subdivision of this reserved cap using its own centroid, not the neutron bulk center.',
            'new_attachment_or_weak_vertex_admitted':False})
    tri_selected,_=select(source)
    assert all(F(x['score'])==2 for x in tri_selected['mode_scores'])
    marked=deepcopy(source);marked['seeds'][0]['role']='attachment_pole'
    attached=assemble(marked)['retained_attachment_interfaces']
    assert len(attached)==1 and len(attached[0])==2
    assert all(len(f)==2 for f in geometry['supporting_facets'])
    # Ordinary proton-face control: the same local1-to3 boundary is not unique.
    proton=json.loads(PROTON.read_text(encoding='utf-8'))
    gp=generator(proton['generators'][0]);r0=tuple(map(F,proton['seeds'][0]['point']))
    r1=apply(gp,r0);r2=apply(gp,r1)
    assert apply(gp,r2)==r0
    Jp=[[r1[a]-r0[a],r2[a]-r0[a]] for a in range(3)]
    Gp=[list(map(F,row)) for row in proton['metric']]
    assert mm(tr(Jp),mm(Gp,Jp))==oldG
    assert mm(gp[0],Jp)==mm(Jp,A)
    checks={k:True for k in (
        'existing_arrow_first_source_replayed_without_parked_spin_decoration',
        'actual_cone_boundary_squared_zero_and_exact_chain_ranks',
        'one_global_disk_chain_from_radial_cancellation',
        'signed_three_edge_ports_recover_source_specific_global_coefficient',
        'source_cycle_intertwines_all_chain_boundaries_and_returns_in_three',
        'actual_neutron_selector_finds_two_fixed_triangular_caps',
        'both_affine_cap_maps_intertwine_actual_source_generators',
        'old_fixed_scale_isometry_fails_by_exact_three_over_eight',
        'derived_cap_scale_has_exact_metric_and_edge_selector_scores',
        'relative_disk_edge_codimensions_are_source_typed',
        'nontrivial_cyclic_characters_have_nonzero_vertex_boundary',
        'inherited_attachment_is_no_port_or_one_edge_not_whole_disk',
        'ordinary_proton_face_has_same_local_boundary_template')}
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'source changed during check'
    report={'schema':'marici.neutrino-triangle-cap-boundary-check.v1','status':'pass','checks':checks,
        'triangle_source':source,'geometry':geometry,'chain_interface':{'cone_cells':cells,'edges':edges,
            'vertex_boundary_matrix':B1,'cone_boundary_matrix':B2,'global_disk_coefficients':D,
            'oriented_arrow_edges':arrow_edges,'outer_boundary_coefficients':oriented_b,
            'relative_arrow_orientation_sign':orientation,'global_coefficient_decoder':decoder,
            'retained_filling_required':True,'inherited_external_attachment_count':0,
            'source_vertex_permutation':vp,'edge_pushforward':T1,'cone_pushforward':T2},
        'nontrivial_character_boundary_residuals':mode_residuals,'neutron_caps':caps,
        'proton_face_control':{'vertices':[r0,r1,r2],'induced_metric':oldG,'same_local_boundary_template':True},
        'geometric_neutrino_candidate_preexisted':True,'parked_spin_charge_decoration_imported':False,
        'source_relative_geometric_codimension_constructed':True,
        'physical_spacetime_embedding_or_neutrino_identification':False,
        'spin_charge_flavor_or_mass_derived':False,'new_weak_attachment_admitted':False,
        'old_producers_or_gallery_modified':False,'formal_proof_recompiled':False,'source_sha256':pins}
    OUT.write_text(json.dumps(serial(report),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','check_groups':len(checks),'main_to_boundary_ports':[1,3],
        'neutron_cap_candidates':2,'source_disk_dimension':2,'edge_dimension':1,
        'old_metric_to_cap_ratio':'3/8','nontrivial_modes_closed':False,
        'inherited_attachment_ports':0,'physical_neutrino_identified':False},indent=2))


if __name__=='__main__':main()
