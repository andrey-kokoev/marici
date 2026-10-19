"""Fixed Garai paired-layer constructor on unchanged diamond, exact arithmetic."""
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
FIXTURE=ROOT/'research/strominger/inputs/garai-diamond-transfer-v1.json'
OUT=ROOT/'research/strominger/results/garai-diamond-transfer/verification.json'
UNIT=[tuple(int(i==j) for i in range(3)) for j in range(3)]
ZERO=(0,0,0)

def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def point(site):
    f,(i,j,k)=site
    return (2*(j+k)+f,2*(i+k)+f,2*(i+j)+f)
def triangle(level):return [(a,b,level-a-b) for a in range(level+1) for b in range(level-a+1)]
def neighbors(site):
    f,n=site
    return [(1-f,plus(n,tuple((1 if f else -1)*x for x in e))) for e in [ZERO]+UNIT]
def squared(a,b):return sum((x-y)**2 for x,y in zip(a,b))


def main():
    fixture=json.loads(FIXTURE.read_text(encoding='utf-8'));checks={};cases=[]
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    audit=json.loads((ROOT/fixture['paper_audit']).read_text(encoding='utf-8'))
    check('paper_count_audit_source_pins_current',audit['status']=='counting_identities_verified_not_physical_validation' and all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in audit['source_sha256'].items()))
    for n in fixture['n_cases']:
        tag=f'n{n}';sites=sorted([(1,v) for v in triangle(2*n-2)]+[(0,v) for v in triangle(2*n-1)])
        index={s:i for i,s in enumerate(sites)};V=len(sites);P=sum(f for f,v in sites);N=V-P
        coordinates=list(map(point,sites));adj=[set() for s in sites];halo=[]
        for i,s in enumerate(sites):
            actual=neighbors(s);corners=list(map(point,actual));center=coordinates[i]
            check(tag+f'_whole_coordination_tetrahedron_{i}',all(sum(v[j] for v in corners)==4*center[j] for j in range(3)) and all(squared(center,v)==3 for v in corners) and all(squared(a,b)==8 for a,b in combinations(corners,2)))
            for neighbor in actual:
                if neighbor in index:adj[i].add(index[neighbor])
                else:halo.append({'inside_index':i,'outside_site':neighbor,'outside_coordinate':point(neighbor)})
        edges=[(i,j) for i,row in enumerate(adj) for j in sorted(row) if i<j];E=len(edges)
        reached={0};queue=[0]
        for i in queue:
            for j in adj[i]:
                if j not in reached:reached.add(j);queue.append(j)
        check(tag+'_actual_patch_connected_and_original_edges_only',len(reached)==V and all(sites[i][0]!=sites[j][0] and squared(coordinates[i],coordinates[j])==3 and i in adj[j] for i,row in enumerate(adj) for j in row))
        heights={f:sorted({sum(coordinates[i]) for i,(family,v) in enumerate(sites) if family==f}) for f in (0,1)}
        check(tag+'_consecutive_triangular_planes',heights=={0:[8*n-4],1:[8*n-5]})
        check(tag+'_raw_Garai_4n_squared_count_survives',V==4*n*n)
        check(tag+'_source_roles_reject_half_protons',P==2*n*n-n and N==2*n*n+n and P!=2*n*n)
        check(tag+'_all_ports_retained_including_exterior_halo',E==3*P and len(halo)==4*V-2*E and all(len(adj[i])+sum(h['inside_index']==i for h in halo)==4 for i in range(V)))
        residues={(sites[i][0]==sites[j][0],squared(coordinates[i],coordinates[j])%8) for i,j in combinations(range(V),2)}
        check(tag+'_mixed_regular_tetrahedron_obstruction',all(r==(0 if same else 3) for same,r in residues))
        tau=[1-2*f for f,v in sites]
        read=lambda state:[(state[i]+state[j])/2 for i,j in edges]
        check(tag+'_internal_reader_erases_role_and_needs_one_scalar',all(tau[i]+tau[j]==0 for i,j in edges) and read(list(map(Q,tau)))==[0]*E and E-V+1==(2*n-1)*(n-1))
        role=list(map(Q,[s[0] for s in sites]))
        check(tag+'_opposite_role_scores_have_identical_internal_readout',read(role)==read([1-x for x in role])==[Q(1,2)]*E)
        incident=[[] for _ in sites]
        for e,(i,j) in enumerate(edges):incident[i].append((j,e));incident[j].append((i,e))
        def decode(y,root):
            state=[None]*V;state[0]=root;todo=[0]
            for i in todo:
                for j,e in incident[i]:
                    if state[j] is None:state[j]=2*y[e]-state[i];todo.append(j)
            assert all(state[i]+state[j]==2*y[e] for e,(i,j) in enumerate(edges))
            return state
        def decode_grade(y,alpha):
            b=decode(y,Q(0));base=sum(tau[i]*b[i] for i in range(V))/V
            root=(alpha-base)/tau[0]
            return [b[i]+Q(tau[i],tau[0])*root for i in range(V)]
        boundary=next(h for h in halo if h['inside_index']==0);known_exterior=Q(7,3)
        faithful=True
        for basis in range(V):
            state=[Q(int(i==basis)) for i in range(V)];y=read(state)
            alpha=sum(tau[i]*state[i] for i in range(V))/V
            boundary_mean=(state[0]+known_exterior)/2
            faithful=faithful and decode_grade(y,alpha)==state and decode(y,2*boundary_mean-known_exterior)==state
        check(tag+'_all_original_basis_states_reconstruct_with_one_retained_component',faithful)
        bP=4*P-E;bN=4*N-E
        check(tag+'_imbalance_is_boundary_slots_not_new_force',bN-bP==4*(N-P)==8*n)
        cases.append({'n':n,'target_half_count':2*n*n,'P':P,'N':N,'raw_sites':V,'edges':E,'internal_reader_rank':V-1,
          'reader_kernel':'one-dimensional span(tau); connected edge equations x_i+x_j=0 propagate from a root',
          'one_retained_scalar_packet_displayed_coordinates':E+1,'packet_independent_rank':V,'independent_edge_cycle_constraints':E-V+1,
          'P_missing_slots':bP,'N_missing_slots':bN,'layer_heights':heights,'sites':sites,'coordinates':coordinates,'internal_edges':edges,'exterior_ports':halo,
          'lost_role_mode':tau,'boundary_reference_example':{'port':boundary,'exterior_value':str(known_exterior),'assumption':'Exterior endpoint value is known/retained; this is not a closed isolated patch.'},
          'reconstruction':'Internal edge means plus alpha=sum(tau_i*f_i)/V, or one exterior-port mean with known exterior value; verified on EVERY source basis vector.'})
    # Rejection concerns a REGULAR mixed core, not every balanced four-site patch.
    core=[(0,(0,0,0)),(1,(0,0,0)),(0,(1,0,0)),(1,(1,-1,0))]
    cp=list(map(point,core));vectors=[tuple(x-y for x,y in zip(p,cp[0])) for p in cp[1:]]
    a,b,c=vectors
    determinant=a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
    core_lengths=sorted(squared(a,b) for a,b in combinations(cp,2))
    check('balanced_four_site_nonregular_core_is_not_ruled_out',sum(f for f,v in core)==2 and all(core[i+1] in neighbors(core[i]) for i in range(3)) and determinant!=0 and core_lengths==[3,3,3,8,8,11])
    paths=[HERE,FIXTURE,ROOT/fixture['source'],ROOT/fixture['paper'],ROOT/fixture['paper_audit']]
    report={'schema':'marici.strominger.garai-diamond-transfer.v1','recorded_at':datetime.now(timezone.utc).isoformat(),
      'status':'pass','classification':'raw_count_survives_faithful_transfer_rejected','hypothesis_status':'direct_faithful_transfer_rejected','checks':checks,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths},'cases':cases,
      'summary':[{k:c[k] for k in ['n','target_half_count','P','N','raw_sites','internal_reader_rank','packet_independent_rank']} for c in cases],
      'general_proofs':{
        'paired_layers':'A index level2n-1 has T_2n sites; B level2n-2 has T_(2n-1). Thus total4n^2 but P=2n^2-n,N=2n^2+n.',
        'regular_core':'For any two sites in the same diamond family, squared distance is0mod8; for opposite families it is3mod8. Every mixed tetrahedron has both pair types, so cannot be regular. This is not just a nearest-neighbor obstruction.',
        'faithful_reader':'Connectedness makes ker(edge endpoint means)=span(tau). One retained independent scalar restores all source states. Known-reference boundary access can supply it.'},
      'balanced_nonregular_core_control':{'sites':core,'coordinates':cp,'squared_pair_distances':core_lengths,'volume':str(Q(abs(determinant),6)),'scope':'A connected2P2N path with noncoplanar sites exists. Only its identification with a REGULAR tetrahedral core is rejected.'},
      'scope':'No forces, fitted geometry, physical spin/charge, nuclear stability or electronic orbital assignment. Both triangles and all coordination tetrahedra remain exact; arbitrary alternative growth rules are not excluded.',
      'enabled_next_test':'Grow graph-distance shells around one fixed A-B bond, using both endpoints symmetrically. Their exchange symmetry supplies a fixed balanced-growth candidate. Measure its actual counts and role-sensitive interface ranks; do not assume2n^2 or import an FCC mixed regular core.'}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'classification':report['classification'],'hypothesis_status':report['hypothesis_status'],'checks':len(checks),'summary':report['summary'],'receipt':OUT.relative_to(ROOT).as_posix()}))

if __name__=='__main__':main()
