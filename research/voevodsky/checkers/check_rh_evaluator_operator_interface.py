"""Iteration3: executable evaluator operators, typed paths and bank no-go.
Rational score configurations are labels, not native coherent amplitudes.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys
from check_proton_native_task_catalogue import ROOT
from check_proton_unitary_probe_repair import restore
from check_rh_two_seed_route_audit import rounded
from check_rh_term_resolved_seam import PAIRS
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from check_source_pulse_particle_intertwiners import eye,mm,transpose,difference,rank,PACKETS

SIZE=15
ENDPOINTS={'AB':('A','B'),'BC':('B','C'),'CA':('C','A'),'BA':('B','A'),'AD':('A','D'),'DB':('D','B')}
def zero(n,m):return [[F(0) for _ in range(m)] for _ in range(n)]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def sub(A,B):return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,q):return [[q*x for x in row] for row in A]
def mv(A,x):return tuple(sum(a*b for a,b in zip(row,x)) for row in A)
def product(word,ops):
    out=eye(SIZE)
    for label in word:out=mm(ops[label],out)
    return out
def strings(A):return [[str(x) for x in row] for row in A]
def composable(word,start):
    place=start
    for label in word:
        a,b=ENDPOINTS[label]
        if a!=place:return False
        place=b
    return True

def apply_basis(ket,label,ops,inverse=False):
    place,x=ket;a,b=ENDPOINTS[label]
    if inverse:a,b=b,a
    assert place==a
    N=sub(ops[label],eye(SIZE));A=sub(eye(SIZE),N) if inverse else ops[label]
    return b,mv(A,x)
def superpose_action(state,label,ops,inverse=False):
    result={}
    for ket,amplitude in state.items():
        target=apply_basis(ket,label,ops,inverse)
        result[target]=result.get(target,F(0))+amplitude
    return {k:v for k,v in result.items() if v}
def inner(a,b):return sum(x*b.get(k,F(0)) for k,x in a.items())


def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/rh-evaluator-operator-interface-v1.json';contract=json.loads(cp.read_text())
    files={k:ROOT/contract[k] for k in ('prior','packet','source_pulses','neutron_bank')}
    prior=json.loads(files['prior'].read_text());assert prior['passed']
    assert ENDPOINTS=={label:(a,b) for label,a,b in PACKETS}
    for path,h in prior['source_hashes'].items():assert sha256(Path(path).read_bytes()).hexdigest()==h,path
    packet=json.loads(files['packet'].read_text());assert packet['status']=='passed'
    terms=('endpoint','gamma_with_infinite_tail','prime_with_infinite_tail')
    matrices={k:restore(prior['term_midpoint_forms'][k]) for k in terms}
    rows=[[G[i][j][0] for i,j in PAIRS] for G in matrices.values()]
    assert all(G[i][j][1]==0 for G in matrices.values() for i in range(3) for j in range(3))
    Z=rounded(packet['calculations'][-1]['finite_zero_packet'],packet['parameters']['rounding_decimal_places'])
    spectral=[Z[i][j][0] for i,j in PAIRS]
    I=eye(SIZE);ops={label:eye(SIZE) for label in ENDPOINTS}
    for k,row in enumerate(rows):
        for j,x in enumerate(row):ops['BC'][6+k][j]+=x
    for j in (6,7,8,13):ops['CA'][9][j]+=1
    for j,x in enumerate(spectral):ops['AD'][10][j]+=x
    for j in (10,12,14):ops['DB'][11][j]+=1
    nilpotents={k:sub(A,I) for k,A in ops.items()}
    for label,N in nilpotents.items():
        assert mm(N,N)==zero(SIZE,SIZE)
        assert mm(ops[label],sub(I,N))==mm(sub(I,N),ops[label])==I
    left=contract['route_order']['arithmetic_root_A'];right=contract['route_order']['spectral_root_A'];combined=contract['route_order']['combined_root_A']
    assert composable(left,'A') and composable(right,'A') and composable(combined,'A')
    invalid=['AB','BC','CA','BA','AD','DB'];assert not composable(invalid,'A')
    L,R=product(left,ops),product(right,ops)
    assert mm(L,R)==mm(R,L)
    for A in (L,R):
        N=sub(A,I);assert mm(mm(N,N),N)==zero(SIZE,SIZE)
    # Prepared query embedding keeps three independent correction values.
    # Their true values come from source/zero certification, not this model.
    prep=zero(SIZE,9)
    for i in range(6):prep[i][i]=1
    for out,index in ((12,6),(13,7),(14,8)):prep[out][index]=1
    qa=[F(i==9) for i in range(SIZE)];qz=[F(i==11) for i in range(SIZE)]
    comparison=sub(mm([qa],mm(L,prep)),mm([qz],mm(R,prep)))[0]
    arithmetic=[sum(row[k] for row in rows) for k in range(6)]
    assert comparison==[arithmetic[k]-spectral[k] for k in range(6)]+[F(-1),F(1),F(-1)]
    assert comparison[-3:]==[-1,1,-1]
    # Check exact intermediate histories and adjoint-direction recovery on
    # every coordinate, plus prepared nonzero-query correction controls.
    controls=[tuple(F(i==j) for i in range(SIZE)) for j in range(SIZE)]
    controls.extend([mv(prep,(F(1),F(0),F(0),F(0),F(0),F(0),tail,ea,ez))
                     for tail,ea,ez in ((F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(-2),F(1,3),F(-1,7)))])
    histories=[]
    for x in controls:
        ket=('A',x);history=[]
        for label in combined:
            before=ket;ket=apply_basis(ket,label,ops)
            history.append({'occurrence':label,'from':before[0],'to':ket[0],
                'before':list(map(str,before[1])),'after':list(map(str,ket[1]))})
            assert ket[1][:6]==x[:6] and ket[1][12:]==x[12:]
        for step in reversed(history):ket=apply_basis(ket,step['occurrence'],ops,inverse=True)
        assert ket==('A',x)
        histories.append(history)
    # Actual inherited active pulses are involutions with positive Gram.
    source=json.loads(files['source_pulses'].read_text());bank=json.loads(files['neutron_bank'].read_text())
    assert source['status']==bank['status']=='passed'
    K=[[F(x) for x in row] for row in source['source']['active_metric']]
    pulses={k:[[F(x) for x in row] for row in A] for k,A in source['source']['active_pulses'].items()}
    for label,E in pulses.items():assert mm(E,E)==eye(6) and mm(mm(transpose(E),K),E)==K
    assert K==transpose(K) and all(K[i][i]>sum(abs(K[i][j]) for j in range(6) if i!=j) for i in range(6))
    # Closed composable loops also exclude vertex-dependent encoders, not
    # just a single global J used at both ends of a shear edge.
    closed_obstructions=[]
    x0=tuple(F(i==0) for i in range(SIZE))
    for word,A,output,coefficient in ((left,L,9,arithmetic[0]),(right,R,11,spectral[0])):
        target_loop=eye(6)
        for label in word:target_loop=mm(pulses[label],target_loop)
        assert mm(mm(transpose(target_loop),K),target_loop)==K
        N=sub(A,I);N2=mm(N,N);assert rank(N2)>0
        assert mm(A,A)!=A
        orbit=[]
        for n in (1,2,5,10):
            power=add(add(I,scale(N,n)),scale(N2,F(n*(n-1),2)))
            state=mv(power,x0)
            assert state[output]==F(n*(n+1),2)*coefficient
            assert composable(word*n,'A')
            orbit.append({'cycle_count':n,'output':str(state[output])})
        closed_obstructions.append({'word':word,'native_active_pulse_loop':strings(target_loop),
          'nilpotent_square_rank':rank(N2),'exact_orbit':orbit,
          'injective_vertex_dependent_coherent_unitary_intertwiner_possible':False,
          'native_idempotent_return_intertwiner_possible':False})
    obstructions=[]
    for label in ('BC','CA','AD','DB'):
        A=ops[label];N=nilpotents[label];assert rank(N)>0
        assert sub(mm(A,A),I)==scale(N,2)
        assert sub(mm(A,A),A)==N
        # If E J=J A and E²=I, then J(A²-I)=0. A²-I=2N
        # is nonzero, excluding every injective J, not just a fitted map.
        obstructions.append({'occurrence':label,'nilpotent_rank':rank(N),
            'involution_intertwiner_requires':'J(2N)=0','idempotent_intertwiner_requires':'JN=0',
            'injective_coherent_amplitude_intertwiner_possible':False})
    # Even an arbitrary positive-metric unitary target cannot intertwine a
    # nontrivial finite-dimensional unipotent: its orbit would have unbounded
    # norm in the induced positive metric. Demonstrate exact coordinate growth.
    N=nilpotents['BC'];j=next(j for j in range(SIZE) if any(row[j] for row in N));x=tuple(F(i==j) for i in range(SIZE))
    nx=mv(N,x);growth=[]
    for n in (1,2,5,10):
        power=add(I,scale(N,n));state=mv(power,x)
        assert state==tuple(a+n*b for a,b in zip(x,nx))
        assert sum(y*y for y in state)==1+n*n*sum(y*y for y in nx)
        growth.append({'power':n,'coordinate_norm_squared':str(sum(y*y for y in state))})
    # A different, explicit carrier fixes the unitarity issue: on l2(Q^15),
    # rational configurations are orthonormal BASIS LABELS. Bijective shears
    # permute basis vectors, so norm is conserved even when coordinate labels
    # grow. This is a countably infinite bank, not the existing finite bank.
    for label in ops:
        src=ENDPOINTS[label][0]
        a={(src,controls[0]):F(3,5),(src,controls[1]):F(4,5)}
        b={(src,controls[1]):F(2,3),(src,controls[2]):F(-1,3)}
        aa=superpose_action(a,label,ops);bb=superpose_action(b,label,ops)
        assert inner(aa,aa)==inner(a,a) and inner(aa,bb)==inner(a,b)
        assert superpose_action(aa,label,ops,inverse=True)==a
    # The common directed edge and its reverse are actual adjoints in this
    # typed configuration model; they transport records without imposing a
    # false equality of arithmetic and spectral outputs.
    for x in controls:
        ket=('A',x);assert apply_basis(apply_basis(ket,'AB',ops),'BA',ops)==ket
    # Native carriers may tensor this SAME new processor as a spectator bank.
    # This is a valid completion, but it does not turn native arrows into
    # evaluators or make native projector stages invertible.
    contexts={}
    for name,key in (('protonlike','proton'),('neutron','neutron')):
        route=json.loads((base/'results/rh-two-seed-route-audit-v1.json').read_text())
        metric=[F(x) for x in route['native_metrics'][key]];assert len(metric)==36 and all(x>0 for x in metric)
        for label in ops:
            for i in (0,12,35):
                norm_before=metric[i]*(F(3,5)**2+F(4,5)**2)
                src=ENDPOINTS[label][0]
                a={(src,controls[0]):F(3,5),(src,controls[1]):F(4,5)}
                after=superpose_action(a,label,ops)
                assert metric[i]*inner(after,after)==norm_before
        contexts[name]={'native_complex_coordinates':36,'native_metric_retained':True,
            'processor':'I_native tensor typed configuration permutation',
            'all_native_coordinates_spectators':True,'native_pulses_or_LGN_replaced':False}
    result={'schema':'marici.rh-evaluator-operator-interface.v1','passed':True,'iteration':3,
       'registers':['w00','w01','w02','w11','w12','w22','endpoint','gamma','prime','arithmetic_output','finite_scout','spectral_output','full_divisor_tail','arithmetic_correction','scout_correction'],
       'operators':{k:strings(A) for k,A in ops.items()},'left_cycle':left,'right_cycle':right,'combined_cycle':combined,
       'iteration2_two_roots_are_one_composable_history':False,'corrected_histories':histories,
       'comparison_covector_on_prepared_query':list(map(str,comparison)),
       'comparison_formula':'(arithmetic_midpoint-scout_rounding).w + arithmetic_error - scout_error - full_divisor_tail',
       'two_loop_operators_commute':True,'commuting_loops_force_RH_equality':False,
       'unknown_corrections_assigned_actual_zero':False,'tail_defined_from_arithmetic_residual':False,
       'finite_coherent_operator_obstructions':obstructions,'closed_composable_cycle_obstructions':closed_obstructions,'unipotent_growth_control':growth,
       'existing_neutron_bank_dimension':bank['target_dimension'],'existing_neutron_bank_implements_RH_shears':False,
       'configuration_completion':{'carrier':'direct sum over A,B,C,D of l2(Q^15)',
          'every_edge_is_typed_unitary_between_vertex_subspaces':True,'AB_and_BA_are_adjoint':True,
          'configuration_coordinates_are_native_amplitudes':False,'linear_amplitude_embedding_of_score_coordinates':False,
          'inverse_recovery_uses_dagger_arrows_not_all_present_as_seed_primitives':True,
          'native_contexts':contexts,'new_countably_infinite_processor_supplied':True},
       'same_surrogate_evaluator_processing_survives_in_both_extended_contexts':True,
       'original_native_seed_operations_compute_RH':False,'full_RH_seam_equality_certified':False,'RH_proved':False,
       'next_nonredundant_obligation':'Construct elementary source-labelled operations generating endpoint, gamma and prime records before final matrix input, and compare the full-divisor boundary in an independently verified convention. A spectator query machine is not native arithmetic realization.',
       'scope':contract['scope'],'source_stores_modified':False}
    bound=[cp,*files.values(),Path(__file__),base/'results/rh-two-seed-route-audit-v1.json',ROOT/'research/strominger/checkers/check_source_pulse_particle_intertwiners.py',ROOT/'research/nima/checkers/check_natural_tower_return.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in bound}
    (base/'results/rh-evaluator-operator-interface-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'typed_histories':len(histories),'corrected_shared_root_path':combined,
      'existing_finite_amplitude_pulses_implement_evaluators':False,'new_configuration_bank_unitary':True,
      'same_processor_in_both_extended_contexts':True,'full_RH_comparison_certified':False},indent=2))
if __name__=='__main__':main()
