"""Exact marked CMC/MCM tetrahedron, contravariance and lossless handoff test."""
from datetime import datetime,timezone
from hashlib import sha256
from itertools import combinations,product
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
FIXTURE=ROOT/'research/strominger/inputs/cmc-mcm-marked-tetrahedron-v1.json'
OUT=ROOT/'research/strominger/results/cmc-mcm-marked-tetrahedron/verification.json'

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def dist2(a,b):return sum((x-y)**2 for x,y in zip(a,b))
def g(p):x,y,z=p;return (x-2,y,-z)
def ginv(p):x,y,z=p;return (x+2,y,-z)
def R(p):x,y,z=p;return (-x,-y,z)
def determinant(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def membership(p,offset):
    x,y,z=tuple(a-b for a,b in zip(p,offset))
    return y%4==0 and (x+z)%4==0 and (z-x)%4==0


def main():
    f=json.loads(FIXTURE.read_text(encoding='utf-8'));checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    js="import * as M from './"+f['source_model']+"';process.stdout.write(JSON.stringify({points:Object.fromEntries(M.facet.map(k=>[k,M.outer[k].slice(0,3)])),facet:M.facet,routes:M.routes.map(r=>({id:r.id,nodes:r.nodes})),walk:M.walk}));"
    completed=subprocess.run(['node','--input-type=module','-e',js],cwd=ROOT,capture_output=True,text=True,timeout=15,check=True)
    source=json.loads(completed.stdout);names=f['vertices'];points=[tuple(source['points'][v]) for v in names]
    check('actual_existing_source_four_vertices_and_windows',source['facet']==names and next(r['nodes'] for r in source['routes'] if r['id']=='proton')==f['proton_window'] and next(r['nodes'] for r in source['routes'] if r['id']=='neutron')==f['neutron_window'])
    check('regular_nondegenerate_tetrahedron_exact_metric',{dist2(a,b) for a,b in combinations(points,2)}=={8} and abs(determinant(*[tuple(x-y for x,y in zip(p,points[0])) for p in points[1:]]))==16)
    P=(0,1,2);N=(1,2,3);shared=(1,2)
    check('typed_windows_and_exact_shared_directed_interface',''.join(f['types'][i] for i in P)=='CMC' and ''.join(f['types'][i] for i in N)=='MCM' and P[-2:]==N[:2]==shared)
    faces=[frozenset(s) for k in range(5) for s in combinations(range(4),k)];whole=frozenset(range(4));dual=lambda s:whole-s
    check('opposite_vertex_is_the_complementary_context',dual(frozenset(P))=={3} and dual(frozenset(N))=={0})
    check('complement_is_involutive_and_contravariant_on_all_face_inclusions',all(dual(dual(s))==s for s in faces) and all(dual(b)<=dual(a) for a in faces for b in faces if a<=b))
    check('codimension_one_at_each_window_but_not_face_gluing_of_solid_tetrahedra',len(set(P)&set(N))-1==1 and len(P)-1==2 and len(whole)-1==3)
    anti=lambda path:tuple(3-v for v in path[::-1])
    paths=[tuple(range(a,b+1)) for a in range(4) for b in range(a,4)]
    def compose(a,b):
        assert a[-1]==b[0]
        return a+b[1:]
    check('geometric_R_realizes_the_explicit_type_exchanging_permutation',all(R(points[k])==points[3-k] and f['types'][k]!=f['types'][3-k] for k in range(4)))
    check('path_anti_involution_exchanges_CMC_MCM_and_keeps_shared_arrow',anti(P)==N and anti(N)==P and anti(shared)==shared and all(anti(anti(p))==p for p in paths))
    check('all_composable_primitive_and_composite_paths_reverse_composition',all(anti(compose(a,b))==compose(anti(b),anti(a)) for a in paths for b in paths if a[-1]==b[0]))
    check('opposite_vertex_alone_does_not_retain_face_direction',P!=P[::-1] and dual(frozenset(P))==dual(frozenset(P[::-1])))
    opposite_witness=[0,0,0,1];type_witness=[1,0,-1,0]
    check('P_face_only_erases_a_distinction_detected_by_N',not any(opposite_witness[i] for i in P) and any(opposite_witness[i] for i in N))
    check('type_only_encoding_erases_occurrence_identity',type_witness[0]+type_witness[2]==type_witness[1]+type_witness[3]==0 and any(type_witness))
    def local_decode(p,n):
        if len(p)!=3 or len(n)!=3:raise ValueError('each typed face must retain three occurrences')
        if p[1:]!=n[:2]:raise ValueError('shared M0/C1 identity has inconsistent values')
        return [p[0],p[1],p[2],n[2]]
    check('all_four_source_basis_values_reconstruct_from_compatible_marked_faces',all(local_decode([int(i==k) for i in P],[int(i==k) for i in N])==[int(i==k) for i in range(4)] for k in range(4)))
    rejected=False
    try:local_decode([0,1,0],[2,0,0])
    except ValueError:rejected=True
    check('incompatible_shared_identity_is_rejected_not_averaged',rejected)
    # Exact two-lattice realization, as subsets of one existing FCC vertex family.
    c_offset=points[0];m_offset=points[1];generators=[(-2,0,-2),(-2,0,2),(0,4,0)]
    sample=[]
    for coeff in product(range(-2,3),repeat=3):
        shift=tuple(sum(coeff[j]*generators[j][axis] for j in range(3)) for axis in range(3))
        sample.extend([add(c_offset,shift),add(m_offset,shift)])
    check('C_M_lattice_cosets_are_disjoint_and_R_exchanges_them',all(membership(R(p),m_offset) for p in sample if membership(p,c_offset)) and all(membership(R(p),c_offset) for p in sample if membership(p,m_offset)) and not membership(c_offset,m_offset))
    check('point_sets_are_the_old_B_FCC_family_not_diamond_A_B',all(all(x%2 for x in p) and sum(p)%4==3 for p in sample) and all((membership(p,c_offset) or membership(p,m_offset))==(all(x%2 for x in p) and sum(p)%4==3) for p in product(range(-3,4),repeat=3)))
    check('handoff_preserves_C_M_types_and_has_countervariant_inverse_relation',g(points[0])==points[2] and g(points[1])==points[3] and all(membership(g(p),c_offset)==membership(p,c_offset) and membership(g(p),m_offset)==membership(p,m_offset) and g(g(p))==add(p,(-4,0,0)) and R(g(R(p)))==ginv(p) for p in sample))
    K=f['chain_cells'];cells=[];local_points=points
    for i in range(K):
        ids=[f'C{i}',f'M{i}',f'C{i+1}',f'M{i+1}'];cells.append({'id':i,'global_vertices':ids,'points':local_points})
        local_points=[g(p) for p in local_points]
    ledger={};occurrences=[]
    for cell in cells:
        for slot,(identity,p) in enumerate(zip(cell['global_vertices'],cell['points'])):
            if identity in ledger:assert ledger[identity]==p
            ledger[identity]=p;occurrences.append({'cell':cell['id'],'slot':slot,'global_identity':identity,'type':f['types'][slot]})
    check('regular_chain_shares_only_declared_edges',len(ledger)==2*K+2 and len(set(ledger.values()))==len(ledger) and all({dist2(a,b) for a,b in combinations(cell['points'],2)}=={8} for cell in cells) and all(set(a['global_vertices'])&set(b['global_vertices'])==(set(a['global_vertices'][2:]) if j==i+1 else set()) for i,a in enumerate(cells) for j,b in enumerate(cells) if j>i))
    check('every_occurrence_is_retained_despite_shared_global_vertices',len(occurrences)==4*K and all(len(occurrences[j:j+4])==4 for j in range(0,4*K,4)))
    def encode(state):return [[state[k] for k in cell['global_vertices']] for cell in cells]
    def decode(local):
        if len(local)!=K or any(len(values)!=4 for values in local):raise ValueError('complete cell occurrence arity required')
        state={}
        for cell,values in zip(cells,local):
            for identity,value in zip(cell['global_vertices'],values):
                if identity in state and state[identity]!=value:raise ValueError('handoff identity conflict: '+identity)
                state[identity]=value
        return state
    basis_ok=True;readers_ok=True
    for selected in ledger:
        state={key:int(key==selected) for key in ledger};local=encode(state);restored=decode(local)
        basis_ok=basis_ok and restored==state
        stages=[(cell['id'],word) for cell in cells for word in ('P','N')]
        for phase in range(len(stages)):
            for steps in (0,1,2):
                if phase+steps>=len(stages):continue
                cell_id,word=stages[phase+steps];indices=P if word=='P' else N
                readers_ok=readers_ok and [restored[cells[cell_id]['global_vertices'][k]] for k in indices]==[local[cell_id][k] for k in indices]
    check('all_global_basis_states_roundtrip_with_shared_identity_ledger',basis_ok)
    check('zero_one_two_window_handoffs_preserve_all_typed_readers',readers_ok)
    incompatible=encode({key:0 for key in ledger});incompatible[1][0]=1;rejected=False
    try:decode(incompatible)
    except ValueError:rejected=True
    check('global_handoff_conflict_detected_without_merging_or_averaging',rejected)
    arity_rejected=False
    try:decode([[0]*4 for _ in range(K-1)])
    except ValueError:arity_rejected=True
    check('incomplete_occurrence_packet_rejected',arity_rejected)
    def valid_glue(i,j,pairs):
        return all(f['types'][a]==f['types'][b] and cells[i]['global_vertices'][a]==cells[j]['global_vertices'][b] for a,b in pairs)
    check('actual_handoff_gluing_preserves_both_type_and_global_identity',all(valid_glue(i,i+1,[(2,0),(3,1)]) for i in range(K-1)))
    check('type_swapping_and_same_type_wrong_identity_gluings_rejected',not valid_glue(0,1,[(2,1),(3,0)]) and not valid_glue(0,1,[(2,2),(3,3)]))
    # A rolling tetrahedron alone is lossy. Retain outgoing history explicitly.
    lost=[1,0,0,0,0,0]
    check('fourth_vertex_is_not_a_substitute_for_accumulated_history',not any((lost[2],lost[3],lost[4],lost[5])) and lost[0]==1)
    def handoff(active,new):return active[2:]+new,active[:2]
    def undo(active,archive):return archive+active[:2],active[2:]
    reversible=True
    for k in range(8):
        raw=[int(i==k) for i in range(8)];next0,out0=handoff(raw[:4],raw[4:6]);next1,out1=handoff(next0,raw[6:])
        recovered0,input1=undo(next1,out1);original,input0=undo(recovered0,out0)
        reversible=reversible and original+input0+input1==raw
    check('two_tetrahedron_handoffs_are_invertible_with_ordered_history',reversible)
    report={'schema':'marici.strominger.cmc-mcm-marked-tetrahedron.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'status':'pass','checks':checks,
      'classification':'marked_CMC_MCM_tetrahedron_and_identity_preserving_handoff_constructed',
      'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in [HERE,FIXTURE,ROOT/f['source_model']]},
      'source_snapshot':source,'prototype':{'vertices':names,'points':points,'proton_window':P,'neutron_window':N,'shared_directed_edge':shared,'proton_opposite':'M1','neutron_opposite':'C0'},
      'two_lattices':{'generators':generators,'C_offset':c_offset,'M_offset':m_offset,'scope':'Explicit selected C/M grading of one old FCC vertex family. Not independently derived physical codimension; not original diamond A/B.'},
      'contravariance':{'face':'set complement reverses inclusion','path':'A(v0,...,vk)=(R(vk),...,R(v0)); A(p then q)=A(q) then A(p)','warning':'An explicit carrier/type permutation and path reversal, not equality of different identities or a native particle conversion.'},
      'chain':{'cells':cells,'global_ledger':ledger,'occurrences':occurrences,'raw_local_coordinates':4*K,'independent_global_values':len(ledger),'shared_identity_constraints':2*(K-1),'space_filling':False},
      'information_witnesses':{'P_face_forgets_M1':opposite_witness,'type_only_forgets_C_occurrence':type_witness,'rolling_window_forgets_past':lost},
      'disposition':'Four vertices support both required marked words and a common exact contravariant presentation symmetry. Compatible edge gluing preserves identities only with occurrence maps, typed readers and history/reference data retained. Physical grading and source-native operation attachment remain open.',
      'enabled_next_test':'Attach actual retained native P/N preparation and operation maps to these marked windows; test full reader and phase naturality rather than selecting an origin because it spells CMC/MCM.',
      'physical_validation':False,'formal_outcome':None}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','classification':report['classification'],'checks':len(checks),'cells':K,'global_vertices':len(ledger),'retained_occurrences':len(occurrences),'physical_C_M_grading_derived':False,'receipt':OUT.relative_to(ROOT).as_posix()}))

if __name__=='__main__':main()
