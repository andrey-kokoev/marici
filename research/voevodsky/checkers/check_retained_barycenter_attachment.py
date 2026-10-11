"""Explicit simplicial point attachment, with both full cell inventories.
Identifying the two marked vertices is a pushout, not a pullback. Coordinates
are an illustrative projection; they are tested, not assumed to embed it.
"""
from itertools import combinations, permutations
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
from check_proton_merkle_reassembly import POINTS, verify

BASE=Path(__file__).resolve().parents[1]
SOURCE=BASE/'results/proton_merkle_store.json'
ROOT='P:ABC'

def cells_of(maximal):
    return {tuple(c) for t in maximal for k in range(1,len(t)+1) for c in combinations(sorted(t),k)}

def subdivision(prefix):
    return [tuple(sorted(prefix+':'+''.join(sorted(p[:k])) for k in range(1,5))) for p in permutations('ABCD')]

def boundary(chain):
    result={}
    for c,value in chain.items():
        if len(c)<2: continue
        for i in range(len(c)):
            face=c[:i]+c[i+1:]
            result[face]=result.get(face,Q(0))+(-1)**i*value
    return {c:v for c,v in result.items() if v}

def rank_columns(columns):
    pivots={}
    for col in columns:
        v={i:Q(x) for i,x in col.items() if x}
        while v:
            p=min(v)
            if p not in pivots:
                d=v[p]; pivots[p]={i:x/d for i,x in v.items()}; break
            d=v[p]
            for i,x in pivots[p].items():
                v[i]=v.get(i,Q(0))-d*x
                if not v[i]: v.pop(i)
    return len(pivots)

def topology(cells):
    levels=[sorted(c for c in cells if len(c)==k+1) for k in range(4)]
    ranks=[0]
    for k in range(1,4):
        index={c:i for i,c in enumerate(levels[k-1])}
        ranks.append(rank_columns([{index[f]:v for f,v in boundary({c:1}).items()} for c in levels[k]]))
    ranks.append(0)
    return {'cells':list(map(len,levels)), 'boundary_ranks':ranks[1:4],
            'rational_betti':[len(levels[k])-ranks[k]-ranks[k+1] for k in range(4)]}

def link(cells,vertex):
    return {tuple(x for x in c if x!=vertex) for c in cells if vertex in c and len(c)>1}

def bary(label):
    return tuple(sum(Q(POINTS[v][i]) for v in label)/len(label) for i in range(3))

def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def main():
    original=SOURCE.read_bytes(); source=json.loads(original); evidence,_=verify(source)
    host_max=subdivision('P'); electron_original=subdivision('E')
    inclusion=lambda v:ROOT if v=='E:ABCD' else v
    electron_max=[tuple(sorted(map(inclusion,t))) for t in electron_original]
    host=cells_of(host_max); electron=cells_of(electron_max); joined=host|electron
    host_link=link(host,ROOT); electron_link=link(electron,ROOT); joined_link=link(joined,ROOT)
    records={name:topology(cells) for name,cells in [('host',host),('electron',electron),('joined',joined),
        ('host_root_link',host_link),('electron_root_link',electron_link),('joined_root_link',joined_link)]}
    translation=bary('ABC'); coords={}
    for cell in joined:
        for vertex in cell:
            side,label=vertex.split(':')
            p=bary(label)
            coords[vertex]=p if side=='P' else tuple(x+y for x,y in zip(p,translation))
    chain={}
    for side,maximal in [(1,host_max),(-1,electron_max)]:
        for t in maximal:
            a,b,c,d=[coords[v] for v in t]
            delta=det(tuple(x-y for x,y in zip(b,a)),tuple(x-y for x,y in zip(c,a)),tuple(x-y for x,y in zip(d,a)))
            assert delta
            chain[t]=side*(1 if delta>0 else -1)
    surface=boundary(chain)
    owners={face:sum(set(face)<set(t) for t in host_max+electron_max) for face in joined if len(face)==3}
    # A point strictly inside both ordinary spatial tetrahedra. The abstract
    # copies remain distinct away from their identified root.
    witness=tuple(Q(9,10)*x for x in translation)
    host_bary=tuple((1+sum(Q(POINTS[v][i])*witness[i] for i in range(3)))/4 for v in 'ABCD')
    displacement=tuple(x-y for x,y in zip(witness,translation))
    electron_bary=tuple((1+sum(Q(POINTS[v][i])*displacement[i] for i in range(3)))/4 for v in 'ABCD')
    checks={
        'proton_source_verified':evidence['verified'],
        'both_twenty_four_sector_inventories_retained':len(host_max)==len(electron_max)==24,
        'host_inclusion_preserves_all_cells':host<=joined,
        'electron_inclusion_is_injective_on_all_cells':len(electron)==len(cells_of(electron_original)),
        'intersection_is_only_identified_barycenter_vertex':host&electron=={(ROOT,)},
        'union_is_closed_under_faces':cells_of(host_max+electron_max)==joined,
        'joined_cell_counts':records['joined']['cells']==[29,100,120,48],
        'joined_rational_homology_is_connected_and_acyclic':records['joined']['rational_betti']==[1,0,0,0],
        'no_unpaired_internal_triangular_faces':all(x in (1,2) for x in owners.values()),
        'oriented_boundary_is_exactly_two_outer_surfaces':len(surface)==48 and set(surface)=={f for f,n in owners.items() if n==1},
        'surface_has_no_boundary_edges':not boundary(surface),
        'host_root_link_is_acyclic_disk_candidate':records['host_root_link']['cells']==[7,12,6,0] and records['host_root_link']['rational_betti']==[1,0,0,0],
        'electron_root_link_is_subdivided_sphere':records['electron_root_link']['cells']==[14,36,24,0] and records['electron_root_link']['rational_betti']==[1,0,1,0],
        'joined_root_link_is_disconnected':records['joined_root_link']['rational_betti']==[2,0,1,0],
        'projected_solids_have_strict_interior_overlap':all(x>0 for x in host_bary+electron_bary),
        'source_unchanged':SOURCE.read_bytes()==original,
    }
    packet={
        'kind':'retained-barycenter-point-pushout',
        'source_root':source['root'],
        'attachment':{'host_vertex':ROOT,'electron_vertex':'E:ABCD','identification':inclusion('E:ABCD'),
            'operation':'pushout of two vertex inclusions','scale':'equal original tetrahedron edge lengths'},
        'host_maximal_simplices':host_max,'electron_original_maximal_simplices':electron_original,
        'electron_attached_maximal_simplices':electron_max,
        'cells_by_dimension':[[list(c) for c in sorted(joined) if len(c)==k+1] for k in range(4)],
        'outward_electron_flags':[[inclusion('E:'+''.join(sorted(p[:k]))) for k in (4,3,2,1)] for p in permutations('ABCD')],
        'display_coordinates':{v:list(map(str,p)) for v,p in sorted(coords.items())},
        'display_warning':'not an embedding: only the root is identified abstractly, but the projected solid interiors overlap',
    }
    payload=json.dumps(packet,sort_keys=True,separators=(',',':'))
    result={'verification_passed':all(checks.values()),'checks':checks,'topology':records,
        'projection_overlap_witness':{'xyz':list(map(str,witness)), 'host_barycentric':list(map(str,host_bary)),
            'electron_barycentric':list(map(str,electron_bary))},
        'conclusions':{'cell_closure':'no additional cells required',
            'root_neighborhood':'nonmanifold: disk link disjoint from sphere link',
            'ordinary_spatial_embedding':'impossible with electron barycenter interior at host boundary and otherwise disjoint solids',
            'isotope_distinction':'not supplied by point identification'},
        'source_sha256':sha256(original).hexdigest(),'packet_sha256':sha256(payload.encode()).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/retained_barycenter_attachment_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/retained_barycenter_attachment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
