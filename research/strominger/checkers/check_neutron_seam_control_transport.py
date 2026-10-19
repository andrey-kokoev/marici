"""Transport actual native seam controls into the retained neutron/bank binding.

No neutral-register Hamiltonian or rest-energy normalization is added. Exact
mode compression first verifies each full native operator; generated closure
then retains every mode reached by seams, source pulses and native rotation.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from check_neutron_canonical_occupied_closure import ROOT,eye,mm,transpose,difference,rank,inverse,scale,columns,mv,inner,encoded
from check_neutron_rest_energy_preflight import nullspace
from check_neutron_canonical_record_binding import dot,scalar
from check_coupled_six_piece_belt import R,Z,ONE,add,mul,conj,scale as cscale,norm,total
from check_belt_three_by_twelve import decode


def main():
    paths={k:ROOT/p for k,p in {
        'preflight':'research/strominger/results/neutron-rest-energy-preflight.json',
        'binding':'research/strominger/results/neutron-canonical-record-binding.json',
        'rotation':'research/strominger/results/neutron-canonical-rotation-frame.json',
        'native':'research/voevodsky/results/belt_three_by_twelve_store.json',
        'lift':'research/voevodsky/results/native_operation_energy_lift_store.json'}.items()}
    packets={k:json.loads(p.read_text()) for k,p in paths.items()};checks={}
    assert packets['preflight']['status']=='passed'
    for p,h in packets['preflight']['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    checks['fresh_preflight_and_native_lift_receipt']=True
    native=packets['native'];binding=packets['binding'];rotation=packets['rotation'];belt=packets['lift']['carriers']['belt']
    coords=native['coordinates'];order=native['triangle_order'];index={t:i for i,t in enumerate(order)}
    denominators=[F(c['d']) for c in coords]
    assert denominators==list(map(F,belt['metric_denominators']))
    full=[decode(c['selected_numerator']) for c in coords]
    modes=[[v if j//2==t else Z for j,v in enumerate(full)] for t in range(18)]
    mode_norms=[scalar(dot(v,v,[1/d for d in denominators])[0]) for v in modes]
    nu=F(binding['rim_mode_squared_norm']);weights=[v/nu for v in mode_norms]
    def apply_native(entries,v):
        out=[Z]*36
        for i,j,a in entries:out[i]=add(out[i],mul(decode(a),v[j]))
        return out
    def compress(entries):
        out=[[F(0)]*18 for _ in range(18)]
        for j,v in enumerate(modes):
            image=apply_native(entries,v)
            for t in range(18):
                z=modes[t][2*t];value=cscale(1/norm(z),mul(conj(z),image[2*t]))
                assert value[1]==0 and value[0].b==0
                out[t][j]=value[0].a
                assert all(image[k]==cscale(value[0],modes[t][k]) for k in (2*t,2*t+1))
        return out
    seams=[(row['triangles'],compress(row['entries'])) for row in belt['seam_projectors']]
    Hnative=compress(belt['native_energy_entries']);N=compress(belt['return_entries'])
    assert len(seams)==21 and rank(N)==1 and mm(N,N)==N
    W=[[weights[i]*F(i==j) for j in range(18)] for i in range(18)]
    for _,P in seams:
        assert rank(P)==1 and mm(P,P)==P and mm(transpose(P),W)==mm(W,P)
        assert mm(P,N)==[[F(0)]*18 for _ in range(18)]
    assert mm(transpose(Hnative),W)==mm(W,Hnative) and mm(Hnative,N)==[[F(0)]*18 for _ in range(18)]
    checks['all_21_full_native_seam_actions_exactly_compressed']=True
    checks['native_constraint_and_return_actions_exactly_compressed']=True
    ports=binding['source_label_to_native_port'];labels=[p['label'] for p in ports];rim=[index[p['triangle_index']] for p in ports]
    slots=[p['source_record_feature_slot'] for p in ports]
    G=[[F(10*int(i==j)+1) for j in range(4)] for i in range(4)]
    D=[[G[a//4][b//4]*G[a%4][b%4]/121 for b in slots] for a in slots]
    M=[[F(0)]*24 for _ in range(24)]
    for i in range(18):M[i][i]=weights[i]
    for i in range(6):
        for j in range(6):M[18+i][18+j]=D[i][j]
    def extend(A):return [r+[F(0)]*6 for r in A]+[[F(0)]*24 for _ in range(6)]
    target_seams=[extend(P) for _,P in seams];target_native=extend(Hnative);target_N=extend(N)
    permutation=rotation['native_coordinate_permutation'];tp=[permutation[2*i]//2 for i in range(18)]
    assert all(permutation[2*i+1]//2==tp[i] for i in range(18))
    Rot=eye(24)
    for i in range(18):
        for j in range(18):Rot[i][j]=F(i==tp[j])
    assert mm(mm(Rot,Rot),Rot)==eye(24) and mm(mm(transpose(Rot),M),Rot)==M
    projectors=[];pulses=[]
    for t in range(3):
        for i,label in enumerate(labels):
            j=rim[i]
            for _ in range(t):j=tp[j]
            d=[F(k==j) for k in range(18)]+[-F(k==i) for k in range(6)]
            assert inner(d,M,d)==2
            P=scale(F(1,2),mm(columns([d]),[mv(M,d)]))
            projectors.append((label,t,P));pulses.append(difference(eye(24),scale(2,P)))
    checks['all_source_pulses_and_rotation_retained_on_24D_envelope']=True
    initial=[F(1)]*18+[F(0)]*6;budget=inner(initial,M,initial)
    assert budget==F(binding['collective_mode_squared_norm'])/nu
    generators=[Rot]+pulses[:6]+target_seams+[target_native]
    names=['rotation']+[f'pulse:{k}' for k in labels]+[f'seam:{a}-{b}' for (a,b),_ in seams]+['native_energy']
    # Incremental exact echelon test avoids repeating a full rank decomposition
    # for the hundreds of generated images. Record raw independent witnesses.
    echelon={};basis=[];witnesses=[]
    def admit(v,witness):
        row=list(v)
        for p,b in sorted(echelon.items()):
            coefficient=row[p]
            if coefficient:row=[x-coefficient*y for x,y in zip(row,b)]
        p=next((i for i,x in enumerate(row) if x),None)
        if p is None:return False
        coefficient=row[p];echelon[p]=[x/coefficient for x in row]
        basis.append(list(v));witnesses.append(witness);return True
    admit(initial,{'preparation':'coherent_neutron_empty_bank'});cursor=0
    while cursor<len(basis):
        for name,A in zip(names,generators):admit(mv(A,basis[cursor]),{'parent':cursor,'operator':name})
        cursor+=1
    assert len(basis)==24 and rank(columns(basis))==24
    checks['minimal_joint_closure_is_full_24_complex_dimensions']=True
    # C3 covariance of the actual seam family, now within the full bank-retained
    # representation. Bank coordinates remain unchanged by the rotation.
    invRot=mm(Rot,Rot)
    for A in target_seams:
        image=mm(mm(Rot,A),invRot)
        assert image in target_seams
    checks['transported_seam_family_covariant_under_actual_rotation']=True
    # Old native constraint zero-space extends by all six bank features.
    # It is not a stationary sector of the source pulse interaction.
    constraints=[r for P in target_seams for r in P]+target_native
    ground=nullspace(constraints,24);assert len(ground)==7
    pulse_rows=[r for _,_,P in projectors for r in P]
    joint=nullspace(constraints+pulse_rows,24);assert len(joint)==1
    assert mv(Rot,joint[0])==joint[0]
    assert any(rank(columns(ground+[mv(P,v)]))>len(ground) for _,_,P in projectors for v in ground)
    checks['old_constraint_zero_sector_not_invariant_under_source_pulses']=True
    # c_native is the literal extension of the old occupied-carrier support,
    # not a supplied assignment of particle charge to the source bank.
    c=[[F(i==j and i<18) for j in range(24)] for i in range(24)]
    ranks=[rank(difference(mm(c,P),mm(P,c))) for _,_,P in projectors]
    assert set(ranks)=={2}
    checks['old_native_carrier_sector_not_conserved_by_bound_pulses']=True
    first=mv(pulses[0],initial)
    native_cost=inner(first,M,mv(target_native,first))/budget
    seam_costs=[inner(first,M,mv(P,first))/budget for P in target_seams]
    assert native_cost>0 and sum(seam_costs)>0
    assert all(inner(initial,M,mv(P,initial))==0 for P in target_seams)
    checks['first_source_pulse_excites_actual_native_and_seam_defects']=True
    result={'status':'passed','checks':checks,'coordinate_order':['native_triangle:'+str(t) for t in order]+['bank_feature:'+k for k in labels],
            'complex_dimension':24,'metric':encoded(M),'initial_coordinates':list(map(str,initial)),
            'source_pulses':[{'label':label,'frame':t,'projector':encoded(P)} for label,t,P in projectors],
            'native_rotation':encoded(Rot),'native_energy':encoded(target_native),'native_return':encoded(target_N),
            'seam_controls':[{'ordered_triangle_positions':edge,'actual_native_triangle_indices':[order[i] for i in edge],
                             'projector':encoded(P)} for (edge,_),P in zip(seams,target_seams)],
            'closure_generation':{'basis_columns':encoded(columns(basis)),'witnesses':witnesses},
            'old_constraint_common_kernel_dimension':7,'including_source_pulse_constraints_kernel_dimension':1,
            'native_carrier_projector_commutator_ranks':ranks,
            'first_AB_pulse':{'native_constraint_expectation':str(native_cost),
                             'sum_of_actual_seam_projector_expectations':str(sum(seam_costs)),
                             'per_seam_expectations':list(map(str,seam_costs))},
            'disposition':'The 21 seam controls transport exactly, but their joint dynamics enlarges the closure to 24 complex modes. The prior model\'s conserved native-carrier sector is not conserved by these pulses; its 21/4 cannot be reused as this coupled system\'s rest energy without a new explicit sector/record Hamiltonian contract.',
            'next_test':'Compare charge assignments for the dynamical bank against existing charge-compatible source constructions before selecting any autonomous occupied-sector energy law.'}
    bound=list(paths.values())+[Path(__file__).resolve(),Path(__file__).with_name('check_neutron_rest_energy_preflight.py'),ROOT/'research/voevodsky/checkers/check_native_operation_energy_lift.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bound}
    out=ROOT/'research/strominger/results/neutron-seam-control-transport.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'seam_controls':21,'minimal_complex_closure':24,
                     'old_constraint_common_kernel_dimension':7,'pulse_and_constraint_common_kernel_dimension':1,
                     'native_carrier_commutator_rank':2,'first_AB_pulse':result['first_AB_pulse']},indent=2))

if __name__=='__main__':main()
