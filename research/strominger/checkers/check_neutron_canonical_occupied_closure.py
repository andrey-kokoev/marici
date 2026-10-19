"""Exact occupied-state closure of the retained neutron pulse/rotation binding.

Thirteen coordinates faithfully cover six neutron rim modes, six bank feature
coefficients and the prepared native spectator. Compute the minimal generated
subspace; do not project evolving states onto the native rank-one return.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from check_source_pulse_particle_intertwiners import ROOT,eye,mm,transpose,difference,rank
from check_belt_interface_response import inverse


def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a):return [[c*x for x in r] for r in a]
def mv(a,v):return [sum(x*y for x,y in zip(r,v)) for r in a]
def columns(vs):return [list(r) for r in zip(*vs)]
def inner(a,M,b):return sum(x*y for x,y in zip(a,mv(M,b)))
def encoded(a):return [[str(x) for x in r] for r in a]
def independent(vs):
    basis=[]
    for v in vs:
        if not basis or rank(columns(basis+[v]))>len(basis):basis.append(v)
    return basis


def main():
    paths={k:ROOT/p for k,p in {
        'binding':'research/strominger/results/neutron-canonical-record-binding.json',
        'rotation':'research/strominger/results/neutron-canonical-rotation-frame.json',
        'native':'research/voevodsky/results/belt_three_by_twelve_store.json'}.items()}
    packets={k:json.loads(p.read_text()) for k,p in paths.items()};binding=packets['binding'];rotation=packets['rotation'];checks={}
    for name in ('binding','rotation'):
        assert packets[name]['status']=='passed'
        for p,h in packets[name]['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    checks['fresh_native_binding_and_rotation_receipts']=True
    ports=binding['source_label_to_native_port'];labels=[p['label'] for p in ports]
    perm=[labels.index(rotation['native_port_permutation'][k]) for k in labels]
    slots=[p['source_record_feature_slot'] for p in ports]
    G=[[F(10*int(i==j)+1) for j in range(4)] for i in range(4)]
    D=[[G[a//4][b//4]*G[a%4][b%4]/121 for b in slots] for a in slots]
    nu=F(binding['rim_mode_squared_norm']);S=F(binding['collective_mode_squared_norm']);beta=S/nu-6
    assert beta>0
    # x=(r_0..r_5,a_0..a_5,s), neutron=sum v_i r_i+s spectator,
    # bank=sum f_i a_i. The spectator is u/sqrt(nu)-sum v_i.
    M=[[F(0)]*13 for _ in range(13)]
    for i in range(6):
        M[i][i]=1
        for j in range(6):M[i+6][j+6]=D[i][j]
    M[12][12]=beta
    R=eye(13)
    for i in range(6):
        for j in range(6):R[i][j]=F(i==perm[j])
    assert mm(mm(R,R),R)==eye(13) and mm(mm(transpose(R),M),R)==M
    initial=[F(1)]*6+[F(0)]*6+[F(1)];budget=inner(initial,M,initial)
    assert budget==S/nu and mv(R,initial)==initial
    # The ambient coherent neutron is C3 invariant; its rim sum also rotates
    # into itself. Therefore this exact spectator line is invariant, not an
    # assumption that an arbitrary 30-dimensional complement is one-dimensional.
    native=packets['native'];nperm=rotation['native_coordinate_permutation']
    assert all(native['coordinates'][i]['selected_numerator']==native['coordinates'][j]['selected_numerator'] for i,j in enumerate(nperm))
    assert set(perm)==set(range(6))
    checks['faithful_13D_preparation_envelope_and_rotation']=True
    directions={};projectors={};pulses={}
    for t in range(3):
        for i,label in enumerate(labels):
            j=i
            for _ in range(t):j=perm[j]
            d=[F(k==j) for k in range(6)]+[-F(k==i) for k in range(6)]+[F(0)]
            assert inner(d,M,d)==2
            P=scale(F(1,2),mm(columns([d]),[mv(M,d)]))
            assert mm(P,P)==P and mm(transpose(P),M)==mm(M,P)
            E=difference(eye(13),scale(2,P))
            assert mm(E,E)==eye(13) and mm(mm(transpose(E),M),E)==M
            directions[label,t]=d;projectors[label,t]=P;pulses[label,t]=E
    # Compute the actual Krylov closure from the prepared neutron. No prechosen
    # 11D subspace is assumed. Rotation plus frame-zero pulses generate all.
    generators=[R]+[pulses[label,0] for label in labels]
    basis=[initial];cursor=0;witnesses=[{'kind':'prepared_coherent_neutron'}]
    while cursor<len(basis):
        v=basis[cursor]
        for gi,A in enumerate(generators):
            nxt=mv(A,v)
            if rank(columns(basis+[nxt]))>len(basis):
                basis.append(nxt);witnesses.append({'parent_basis_index':cursor,'generator':'native_rotation' if gi==0 else labels[gi-1]})
        cursor+=1
    B=columns(basis);dimension=len(basis);assert dimension==11
    metric=mm(mm(transpose(B),M),B)
    left=mm(mm(inverse(metric),transpose(B)),M)
    assert mm(left,B)==eye(dimension)
    compressed={}
    for name,A in [('native_rotation',R)]+[(f'{label}@{t}',E) for (label,t),E in pulses.items()]:
        small=mm(mm(left,A),B)
        assert mm(A,B)==mm(B,small)
        assert mm(mm(transpose(small),metric),small)==metric
        compressed[name]=small
    for P in projectors.values():assert mm(P,B)==mm(B,mm(mm(left,P),B))
    checks['minimal_11D_closure_generated_from_prepared_state']=True
    checks['all_18_pulses_and_rotation_exactly_intertwined']=True
    checks['closed_metric_and_continuous_projectors_preserved']=True
    # Explicit real canonical chart for the entire complex occupied closure:
    # z=q+i metric^-1 p/2. The inherited form is sum dq wedge dp.
    # h=q^T metric P q + p^T P metric^-1 p/4.
    Mi=inverse(metric);zero=[[F(0)]*dimension for _ in range(dimension)]
    J=[zero[i]+eye(dimension)[i] for i in range(dimension)]+[[-x for x in eye(dimension)[i]]+zero[i] for i in range(dimension)]
    realC=[eye(dimension)[i]+zero[i] for i in range(dimension)]
    imagC=[zero[i]+scale(F(1,2),Mi)[i] for i in range(dimension)]
    for name,E in compressed.items():
        if name=='native_rotation':continue
        P=scale(F(1,2),difference(eye(dimension),E))
        Hq=mm(metric,P);Hp=scale(F(1,4),mm(P,Mi))
        assert Hq==transpose(Hq) and Hp==transpose(Hp)
        Hreal=[Hq[i]+zero[i] for i in range(dimension)]+[zero[i]+Hp[i] for i in range(dimension)]
        A=scale(2,mm(J,Hreal))
        assert mm(realC,A)==mm(P,imagC) and mm(imagC,A)==scale(-1,mm(P,realC))
        assert add(mm(transpose(A),J),mm(J,A))==[[F(0)]*(2*dimension) for _ in range(2*dimension)]
    checks['explicit_22D_real_canonical_Hamiltonians_intertwined']=True
    # Separate the ten-dimensional active space and the single prepared fixed
    # component. This is a decomposition of the minimal closure, not a new H.
    active_basis=independent(list(directions.values()));assert len(active_basis)==10
    C=columns(active_basis);active_metric=mm(mm(transpose(C),M),C)
    active_projector=mm(mm(mm(C,inverse(active_metric)),transpose(C)),M)
    assert mm(active_projector,active_projector)==active_projector
    active=mv(active_projector,initial);fixed=[a-b for a,b in zip(initial,active)]
    assert fixed!=[F(0)]*13 and inner(fixed,M,active)==0
    assert mv(R,fixed)==fixed and all(mv(E,fixed)==fixed for E in pulses.values())
    assert rank(columns(active_basis+[fixed]))==11
    active_weight=inner(active,M,active)/budget;fixed_weight=inner(fixed,M,fixed)/budget
    assert active_weight+fixed_weight==1 and active_weight>0 and fixed_weight>0
    checks['ten_active_modes_and_one_retained_fixed_component']=True
    # Exact occupied neutron readout. Its native rank-one projector has zero
    # bank output. For the initial state it agrees with |initial><initial|/B.
    occupied=scale(1/budget,mm(columns([initial]),[mv(M,initial)]))
    assert mm(occupied,occupied)==occupied
    def report(v):
        full=inner(v,M,v)/budget
        bank=sum(v[6+i]*D[i][j]*v[6+j] for i in range(6) for j in range(6))/budget
        occupied_weight=inner(initial,M,v)**2/budget**2
        native=full-bank
        return {'full_budget':str(full),'native_coherent_weight':str(occupied_weight),
                'native_noncoherent_weight':str(native-occupied_weight),'record_bank_weight':str(bank)}
    after=mv(pulses['AB',0],initial);a=nu/S
    first=report(after)
    assert F(first['native_coherent_weight'])==(1-a)**2
    assert F(first['native_noncoherent_weight'])==a*(1-a)
    assert F(first['record_bank_weight'])==a
    assert mv(occupied,after)!=after
    assert inner(mv(occupied,after),M,mv(occupied,after))<budget
    checks['occupied_return_projection_is_lossy_after_first_pulse']=True
    # Mixed-frame history in the reduced space, preserving full diagnostics.
    history=[];state=list(initial);small=mv(left,state);t=0
    for serial,label in enumerate(['AB','BA']*3):
        P=projectors[label,t];energy=inner(state,M,mv(P,state))/budget
        before=list(state);state=mv(pulses[label,t],state)
        small=mv(compressed[f'{label}@{t}'],small)
        assert state==mv(B,small)
        after_pulse=list(state);state=mv(R,state);small=mv(compressed['native_rotation'],small)
        assert state==mv(B,small) and inner(state,M,state)==budget
        history.append({'occurrence':serial,'label':label,'frame':t,'pulse_energy':str(energy),
                        'before':list(map(str,before)),'after_pulse':list(map(str,after_pulse)),
                        'after_rotation':list(map(str,state)),'readout_after':report(state)})
        t=(t+1)%3
    for row in reversed(history):
        state=mv(mm(R,R),state);state=mv(pulses[row['label'],row['frame']],state)
        assert state==list(map(F,row['before']))
    assert state==initial
    checks['reduced_execution_and_full_reverse_recovery']=True
    assert history[0]['pulse_energy']==binding['unit_coherent_neutron_empty_record_bank']['each_port_energy']
    checks['prior_coherent_pulse_energy_reproduced']=True
    result={'status':'passed','checks':checks,
            'envelope':{'complex_dimension':13,'coordinate_order':['rim:'+k for k in labels]+['bank_feature:'+k for k in labels]+['prepared_native_spectator'],
                        'metric':encoded(M),'initial_coordinates':list(map(str,initial)),'initial_budget_before_normalizing':str(budget),
                        'scope':'Exact reachable envelope of the specified coherent-neutron/empty-bank preparation. Not a compression of arbitrary 52D input states.'},
            'minimal_closure':{'complex_dimension':dimension,'real_canonical_dimension':2*dimension,
                               'basis_columns':encoded(B),'basis_generation_witnesses':witnesses,
                               'metric':encoded(metric),'metric_left_inverse':encoded(left),
                               'generators':{k:encoded(v) for k,v in compressed.items()},
                               'active_complex_dimension':10,'prepared_fixed_complex_dimension':1,
                               'initial_active_weight':str(active_weight),'initial_fixed_weight':str(fixed_weight)},
            'canonical_chart':{'coordinates':'z=q+i metric^-1 p/2; q,p real dimension 11',
                               'symplectic_form':'sum_i dq_i wedge dp_i',
                               'pulse_projector':'P=(I-E)/2 for each stored pulse generator E',
                               'Hamiltonian':'h=q^T metric P q + p^T P metric^-1 p/4',
                               'flow':'xdot=2J Hreal x; complex form zdot=-iP z',
                               'action_primitive':'p dq-d(q^T p)/2',
                               'budget':'q^T metric q+p^T metric^-1 p/4'},
            'first_AB_pulse':first,'history':history,
            'interpretation':'The source pulse/record binding closes exactly, but not on the one-dimensional native occupied return. Pulse energy, occupation weight and conserved budget remain distinct.',
            'remaining_input':'A specified occupied-sector evolution/preparation or source-derived charging law is still needed for neutron rest energy. This checker introduces no autonomous summed Hamiltonian.'}
    bound=list(paths.values())+[Path(__file__).resolve(),Path(__file__).with_name('check_source_pulse_particle_intertwiners.py'),ROOT/'research/voevodsky/checkers/check_belt_interface_response.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bound}
    out=ROOT/'research/strominger/results/neutron-canonical-occupied-closure.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'minimal_complex_closure':dimension,'active_modes':10,
                      'initial_active_weight':str(active_weight),'initial_fixed_weight':str(fixed_weight),
                      'first_AB_pulse':first},indent=2))

if __name__=='__main__':main()
