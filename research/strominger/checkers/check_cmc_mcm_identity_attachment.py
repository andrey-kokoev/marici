"""Attach existing spectral identities to original five-role geometry and history."""
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
from itertools import combinations
import json,re,subprocess,sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
FIX=ROOT/'research/strominger/inputs/cmc-mcm-identity-attachment-v1.json'
OUT=ROOT/'research/strominger/results/cmc-mcm-identity-attachment/verification.json'
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
import check_triangle_half_phase as T
import check_record4_spectral_promotion as S
from check_twelve_triangle_positive_geometry import mean as source_mean3


def mean(points):
    # Existing barycenter helper is3D; explicitly extend it to the retained lift.
    return source_mean3(points)+(sum(p[3] for p in points)/len(points),)

def eye(n):return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def inv(a):
    n=len(a);a=[list(r)+list(e) for r,e in zip(a,eye(n))]
    for k in range(n):
        p=next(i for i in range(k,n) if a[i][k]);a[k],a[p]=a[p],a[k]
        divisor=a[k][k];a[k]=[x/divisor for x in a[k]]
        for i in range(n):
            if i!=k:
                factor=a[i][k];a[i]=[x-factor*y for x,y in zip(a[i],a[k])]
    return tuple(tuple(r[n:]) for r in a)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def real_columns(points):return tuple(tuple(p[i] for p in points) for i in range(len(points[0])))
def permutation(p):return tuple(tuple(F(i==p[j]) for j in range(len(p))) for i in range(len(p)))
def scalar_z(z):return {'real':str(z[0]),'imaginary_sqrt3_coefficient':str(z[1])}
def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x


def main():
    f=json.loads(FIX.read_text(encoding='utf-8'));checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    js="import * as M from './"+f['geometry_source']+"';process.stdout.write(JSON.stringify({points:M.pentachoron,routes:M.routes.map(r=>({id:r.id,nodes:r.nodes,start:r.start})),walk:M.walk}));"
    snapshot=json.loads(subprocess.run(['node','--input-type=module','-e',js],cwd=ROOT,capture_output=True,text=True,timeout=15,check=True).stdout)
    text=(ROOT/f['geometry_source']).read_text(encoding='utf-8')
    names=['C0','M0','C1','M1','C2'];raw=snapshot['points']
    check('original_five_role_walk_and_symbolic_lift_source_retained',snapshot['walk']==f['original_walk'] and re.search(r'V4:\s*\[0,\s*0,\s*0,\s*Math.sqrt\(5\)\]',text) is not None and raw['C2'][:3]==[0,0,0])
    points=[tuple(F(x) for x in raw[n][:3])+(F(0),) for n in names[:4]]+[(F(0),F(0),F(0),F(1))]
    G=tuple(tuple(F((1,1,1,5)[i] if i==j else 0) for j in range(4)) for i in range(4))
    dot=lambda a,b:sum(a[i]*G[i][i]*b[i] for i in range(4))
    check('exact_original_regular_pentachoron_metric_not_projected_metric',all(dot(minus(a,b),minus(a,b))==8 for a,b in combinations(points,2)))
    b5=mean(points);facet_center=mean(points[:4]);project=lambda p:p[:3]
    check('fifth_vertex_body_center_and_facet_center_distinct_despite_same_projection',len({points[4],b5,facet_center})==3 and project(points[4])==project(b5)==project(facet_center))
    glide=json.loads((ROOT/f['glide_rival']).read_text(encoding='utf-8'))
    check('glide_rival_pins_current_but_its_C2_not_original_C2',glide['status']=='pass' and all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in glide['source_sha256'].items()) and tuple(glide['chain']['global_ledger']['C2'])!=project(points[4]))
    # Counting metric on five labels splits into centered geometry and total coefficient.
    H=real_columns([minus(p,b5)+(F(1),) for p in points]);Hi=inv(H)
    GH=tuple(tuple(F((1,1,1,5,F(4,5))[i] if i==j else 0) for j in range(5)) for i in range(5))
    check('source_counting_metric_equals_geometry_plus_retained_common_coordinate',T.mm(T.transpose(H),T.mm(GH,H))==T.scale(eye(5),F(4)) and T.mm(Hi,H)==eye(5))
    # First-seen geometric assembly and chronological occurrence readout are separate.
    unique=[]
    for n in snapshot['walk']:
        if n not in unique:unique.append(n)
    centers=[mean([points[names.index(v)] for v in unique[:k]]) for k in range(1,6)]
    increments=[minus(centers[k+1],centers[k]) for k in range(4)]
    check('barycenter_updates_add_displacements_and_recover_every_inserted_vertex',all(plus(centers[k],increments[k])==centers[k+1] and tuple((k+2)*centers[k+1][i]-(k+1)*centers[k][i] for i in range(4))==points[k+1] for k in range(4)))
    occurrence_centers=[mean([points[names.index(v)] for v in snapshot['walk'][:k]]) for k in range(1,7)]
    check('repeated_C1_retains_two_occurrences_without_sixth_vertex',snapshot['walk'][2]==snapshot['walk'][4]=='C1' and len(unique)==5 and occurrence_centers[-1]!=centers[-1])
    check('barycenter_contraction_requires_weight_and_index_to_recover_input',mean(points[:4])==facet_center and centers[-1]==b5 and len(set(centers))==5)
    walk_packets=[T.TwoPacket('walk:'+str(k),a,b) for k,(a,b) in enumerate(zip(snapshot['walk'],snapshot['walk'][1:]))]
    ledger=S.SpectralLedger();rows=[];Z=[];promoted=[];all_sources=[]
    GZ=T.zreal(GH)
    for route in snapshot['routes']:
        role=route['id'];order=[names.index(v) for v in route['nodes']];start=route['start'];packets=tuple(walk_packets[start:start+2])
        rejected=False
        try:ledger.record4(packets)
        except ValueError:rejected=True
        check(role+'_open_source_window_is_not_silently_called_a_cycle',rejected and [packets[0].source,packets[0].target,packets[1].target]==route['nodes'])
        closure=T.TwoPacket('declared-geometric-closure:'+role,route['nodes'][-1],route['nodes'][0])
        root=ledger.record4(packets+(closure,));cycle=ledger.validate_root(root)
        identities={mode:ledger.promote(root,mode) for mode in S.MODES}
        X=tuple(tuple(H[i][j] for j in order) for i in range(5));Z.append(X)
        check(role+'_all_three_source_modes_promoted_with_exact_occurrences',all(ledger.deconstruct(v)==packets+(closure,) and ledger.resolve(v) is root for v in identities.values()))
        parent_cycle=list(range(5))
        for j in range(3):parent_cycle[order[j]]=order[(j-1)%3]
        parent_cycle=T.mm(T.mm(H,permutation(parent_cycle)),Hi)
        geometric={mode:T.zmscale(T.zmm(T.zmm(T.zreal(X),v.projector),T.zmm(T.zreal(T.transpose(X)),GZ)),(F(1,4),F(0))) for mode,v in identities.items()}
        vectors={mode:T.zmm(T.zreal(X),tuple((z,) for z in ((S.ONE,)*3 if mode=='common' else (S.ONE,v.eigenvalue,T.zmul(v.eigenvalue,v.eigenvalue))))) for mode,v in identities.items()}
        check(role+'_geometric_mode_identities_idempotent_metric_selfadjoint',all(T.zmm(E,E)==E and T.zmm(S.dagger(E),GZ)==T.zmm(GZ,E) and S.ztrace(E)==S.ONE and T.zmm(E,vectors[mode])==vectors[mode] for mode,E in geometric.items()))
        check(role+'_original_cyclic_eigenvalue_transports_to_full_geometric_operator',all(T.zmm(T.zreal(parent_cycle),E)==T.zmscale(E,identities[mode].eigenvalue) for mode,E in geometric.items()))
        # All mode amplitudes AND both outside coordinates are retained.
        def encode(raw_state):
            column=tuple((raw_state[j],) for j in order)
            return {mode:T.zmm(v.projector,column) for mode,v in identities.items()},[(j,raw_state[j]) for j in range(5) if j not in order]
        def decode(packet):
            components,outside=packet;result=[None]*5
            for k,j in enumerate(order):
                value=(F(0),F(0))
                for mode in S.MODES:value=T.zadd(value,components[mode][k][0])
                result[j]=value
            for j,value in outside:result[j]=value
            return tuple(result)
        check(role+'_full_five_source_coordinates_roundtrip',all(decode(encode(tuple((F(j==k),F(0)) for j in range(5))))==tuple((F(j==k),F(0)) for j in range(5)) for k in range(5)))
        repeat=ledger.promote(root,'positive')
        check(role+'_spectral_reentry_keeps_identity_line_and_recovers_history',repeat.projector==identities['positive'].projector and repeat.label!=identities['positive'].label and ledger.deconstruct(repeat)==packets+(closure,))
        promoted.append(identities);all_sources.append((geometric,vectors,order))
        rows.append({'role':role,'ordered_vertices':route['nodes'],'walk_occurrence_ids':[p.label for p in packets],
          'explicit_extra_closure':closure.__dict__,'root':root.label,'anchor':mean([points[j] for j in order]),'cyclic_geometric_operator':parent_cycle,
          'mode_records':{mode:{'label':v.label,'eigenvalue':scalar_z(v.eigenvalue),'coefficient_projector':v.projector,'geometric_projector':geometric[mode],'source_window':v.window.__dict__} for mode,v in identities.items()}})
    check('equal_coefficient_projectors_do_not_merge_different_source_histories',promoted[0]['positive'].projector==promoted[1]['positive'].projector and promoted[0]['positive'].window!=promoted[1]['positive'].window)
    def full_map(p):return T.mm(T.mm(H,permutation(p)),Hi)
    transitions=[];phases=(S.ONE,S.OMEGA,T.zconj(S.OMEGA))
    composite=eye(5)
    for k in range(2):
        left=all_sources[k][2];right=all_sources[k+1][2];exit_vertex=next(iter(set(left)-set(right)));entry_vertex=next(iter(set(right)-set(left)))
        p=list(range(5));p[exit_vertex],p[entry_vertex]=entry_vertex,exit_vertex
        A=full_map(p);composite=T.mm(A,composite);Ai=inv(A);matches={}
        check(f'transition{k}_shared_and_uninvolved_source_identities_fixed',all(p[j]==j for j in range(5) if j not in (exit_vertex,entry_vertex)) and {p[j] for j in left}==set(right))
        check(f'transition{k}_exact_source_metric_and_barycenter_displacement',T.mm(T.transpose(A),T.mm(GH,A))==GH and T.mv(A,minus(rows[k]['anchor'],b5)+(F(1),))==minus(rows[k+1]['anchor'],b5)+(F(1),))
        for mode in S.MODES:
            image=T.zmm(T.zreal(A),all_sources[k][1][mode]);found=[]
            for target in S.MODES:
                for phase in phases:
                    if image==T.zmscale(all_sources[k+1][1][target],phase):found.append((target,phase))
            check(f'transition{k}_{mode}_phase_and_mode_transport_uniquely_recovered',len(found)==1)
            target,phase=found[0];matches[mode]={'target_mode':target,'phase':scalar_z(phase)}
            E=all_sources[k][0][mode]
            check(f'transition{k}_{mode}_whole_geometric_projector_square',T.zmm(T.zmm(T.zreal(A),E),T.zreal(Ai))==all_sources[k+1][0][target])
        source_cycle=rows[k]['cyclic_geometric_operator'];target_cycle=rows[k+1]['cyclic_geometric_operator']
        actual_target=target_cycle if k==0 else inv(target_cycle)
        check(f'transition{k}_whole_cyclic_operation_square_with_recorded_orientation',T.mm(A,source_cycle)==T.mm(actual_target,A))
        check(f'transition{k}_inverse_is_a_retained_two_cycle_word_not_a_new_primitive',inv(target_cycle)==T.mm(target_cycle,target_cycle))
        if k==1:check('NE_same_forward_cycle_square_rejected',T.mm(A,source_cycle)!=T.mm(target_cycle,A))
        delta=minus(rows[k+1]['anchor'],rows[k]['anchor'])
        transitions.append({'from':rows[k]['role'],'to':rows[k+1]['role'],'vertex_permutation':p,'frame_matrix_centered_homogeneous':A,'anchor_displacement':delta,'mode_transport':matches,'cyclic_target_convention':'forward' if k==0 else 'inverse: two retained forward cycles'})
    check('oppositely_traversed_NE_seam_flips_complex_branch_not_erased',transitions[0]['mode_transport']['positive']['target_mode']=='positive' and transitions[1]['mode_transport']['positive']['target_mode']=='negative')
    check('two_step_transport_recovers_every_parent_input_with_inverse',T.mm(inv(composite),composite)==eye(5) and all(T.mv(inv(composite),T.mv(composite,tuple(F(i==j) for i in range(5))))==tuple(F(i==j) for i in range(5)) for j in range(5)))
    # Wrongly demanding every forward positive mode stay positive is an explicit failed rival.
    E0=all_sources[0][0]['positive'];final=T.zmm(T.zmm(T.zreal(composite),E0),T.zreal(inv(composite)))
    check('retained_two_step_transport_matches_negative_E_branch_not_positive',final==all_sources[2][0]['negative'] and final!=all_sources[2][0]['positive'])
    check('full_five_vertex_source_has_no_global_C_M_exchange',sum(n.startswith('C') for n in names)==3 and sum(n.startswith('M') for n in names)==2)
    # Keep the previous facet anti-map as a relative map fixing the fifth identity mark.
    relative=[3,2,1,0,4]
    check('facet_duality_fixes_fifth_mark_but_is_not_uniform_global_type_swap',relative[4]==4 and all(names[relative[j]][0]!=names[j][0] for j in range(4)))
    paths=[HERE,FIX,ROOT/f['geometry_source'],ROOT/f['spectral_constructor'],ROOT/f['triangle_source'],ROOT/f['barycenter_source'],ROOT/'research/nima/checkers/check_twelve_triangle_positive_geometry.py',ROOT/f['glide_rival']]
    report={'schema':'marici.strominger.cmc-mcm-identity-attachment.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'status':'pass','classification':'retained_spectral_barycentric_identity_attached_conditionally_to_original_five_role_geometry','checks':checks,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths},'original_source_snapshot':snapshot,
      'exact_coordinate_encoding':'fourth component is coefficient of sqrt(5)','exact_points':dict(zip(names,points)),'spatial_metric':G,'homogeneous_metric':GH,
      'homogeneous_label_to_geometric_map':H,'inverse_map':Hi,'facet_center':facet_center,'whole_pentachoron_center':b5,'fifth_original_vertex':points[4],
      'first_seen_assembly':{'vertex_ids':unique,'barycenters':centers,'displacements':increments},'occurrence_walk_barycenters':occurrence_centers,
      'retained_walk_occurrences':[{'occurrence':k,'vertex_identity':n} for k,n in enumerate(snapshot['walk'])],
      'windows':rows,'transitions':transitions,'two_step_transport':composite,
      'conditional_boundary':['Closed-face adapters add geometric closure edges, not supplied native commands.','Maximal-fixed-complement frame comparisons are a declared rule.','All three modes and original source windows remain; no physical mode is selected.','Uniform C/M exchange is only available on the four-role facet; the fifth identity mark remains separate.','The original native1836 proton and neutron coefficient protocols are not replaced by these generic triangle modes.'],
      'enabled_next_test':'Compare the explicit closures, overlap-fixing frame maps and phase/branch switches with actual retained native P/N command and reader sources; preserve any non-admissibility or changed-full-task obstruction.',
      'physical_validation':False,'formal_outcome':None}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(serial(report),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','classification':report['classification'],'checks':len(checks),'walk':snapshot['walk'],'actual_original_vertices':5,'positive_mode_targets':[r['mode_transport']['positive'] for r in transitions],'native_command_attachment_derived':False,'receipt':OUT.relative_to(ROOT).as_posix()}))

if __name__=='__main__':main()
