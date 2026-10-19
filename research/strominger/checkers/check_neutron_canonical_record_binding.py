"""Faithful retained-record binding of source pulses to native neutron rim modes.

Declared address policy, not an identification with the free C3 rotation:
zip the live source registry with rim occurrences in the stored triangle order.
The original 16D source carrier becomes an explicit dynamical record bank;
its six independent record amplitudes are encoded in six native rim modes.
Every other neutron coordinate is retained as a spectator, not projected away.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from check_source_pulse_particle_intertwiners import ROOT,PACKETS
from check_belt_three_by_twelve import decode
from check_coupled_six_piece_belt import R,Z,ONE,add,mul,conj,scale,norm,total,encoded


def dot(a,b,weights):return total(scale(w,mul(conj(x),y)) for x,y,w in zip(a,b,weights))
def vadd(a,b):return [add(x,y) for x,y in zip(a,b)]
def vscale(c,v):return [mul(c,x) for x in v]
def scalar(x):
    assert x.b==0
    return x.a

def main():
    paths={name:ROOT/path for name,path in {
        'neutron':'research/strominger/results/neutron-arrow-native-bridge.json',
        'ambient':'research/voevodsky/results/coupled_six_piece_belt_store.json',
        'intrinsic':'research/voevodsky/results/belt_three_by_twelve_store.json',
        'source':'research/strominger/results/source-pulse-particle-intertwiners.json',
        'energy':'research/strominger/results/canonical-source-energy.json'}.items()}
    packets={k:json.loads(p.read_text()) for k,p in paths.items()};checks={}
    for name in ('neutron','source','energy'):
        obj=packets[name];assert obj['status']=='passed'
        for p,h in obj['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    native=packets['intrinsic'];ambient=packets['ambient'];bridge=packets['neutron']
    assert hashlib.sha256(json.dumps(ambient['record'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==ambient['root']
    assert native['source_root']==ambient['root']
    assert bridge['coordinates']==native['coordinates'] and bridge['triangle_order']==native['triangle_order']
    checks['live_native_and_source_bindings_valid']=True
    coordinates=native['coordinates'];triangles=ambient['record']['triangles'];order=native['triangle_order']
    # Use genuine lower/upper rim edges, not all triangles or surrogate ports.
    rim=[t for t in order if triangles[t][1][0]==triangles[t][2][0] and triangles[t][1][0] in 'LU']
    assert len(rim)==6 and len(set(rim))==6
    labels=[label for label,_,_ in PACKETS];ends={label:(a,b) for label,a,b in PACKETS}
    weights=[1/F(c['d']) for c in coordinates];full=[decode(c['selected_numerator']) for c in coordinates]
    modes={label:[z if c['triangle']==t else Z for z,c in zip(full,coordinates)] for label,t in zip(labels,rim)}
    norms={k:scalar(dot(v,v,weights)[0]) for k,v in modes.items()}
    assert len(set(norms.values()))==1;nu=next(iter(norms.values()));assert nu>0
    assert all(dot(modes[a],modes[b],weights)==((R(nu),R()) if a==b else Z) for a in labels for b in labels)
    checks['six_actual_rim_modes_orthogonal_with_common_norm']=True
    # Physical neutron numerator is N/sqrt(nu). This is a coordinate scaling,
    # not a change to its inherited metric: norm(N)=sum |N_j|²/(nu*d_j).
    neutron_weights=[w/nu for w in weights]
    G=[[F(10*int(i==j)+1) for j in range(4)] for i in range(4)]
    H=[[G[i//4][j//4]*G[i%4][j%4] for j in range(16)] for i in range(16)]
    slots={label:4*'ABCD'.index(a)+'ABCD'.index(b) for label,a,b in PACKETS}
    f={label:[(R(F(i==slot,11)),R()) for i in range(16)] for label,slot in slots.items()}
    def record_inner(x,y):return total(scale(H[i][j],mul(conj(x[i]),y[j])) for i in range(16) for j in range(16) if x[i]!=Z and y[j]!=Z)
    assert all(record_inner(f[a],f[a])==ONE for a in labels)
    gram=[[scalar(record_inner(f[a],f[b])[0])+F(a==b) for b in labels] for a in labels]
    assert [[str(x) for x in row] for row in gram]==packets['source']['source']['active_metric']
    def amplitudes(N):return [dot(modes[label],N,neutron_weights) for label in labels]
    def encode(y,r):
        N=[Z]*36
        for label,a in zip(labels,r):N=vadd(N,vscale(a,modes[label]))
        return N+list(y)
    def decode_target(state):
        N,y=state[:36],state[36:];r=amplitudes(N);image=encode(y,r)
        spectator=[add(a,scale(-1,b)) for a,b in zip(N,image[:36])]
        return list(y),r,spectator
    def inner(a,b):return add(dot(a[:36],b[:36],neutron_weights),record_inner(a[36:],b[36:]))
    def budget(a):
        out=inner(a,a);assert out[1]==0
        return scalar(out[0])
    def mismatch(label,state):return add(dot(modes[label],state[:36],neutron_weights),scale(-1,record_inner(f[label],state[36:])))
    def projector(label,state):
        delta=scale(F(1,2),mismatch(label,state))
        return vscale(delta,modes[label])+vscale(scale(-1,delta),f[label])
    def pulse(label,state,phase=(R(-1),R())):
        assert norm(phase)==1
        return vadd(state,vscale(add(phase,scale(-1,ONE)),projector(label,state)))
    def source_pulse(label,y,r,phase=(R(-1),R())):
        i=labels.index(label);delta=add(r[i],scale(-1,record_inner(f[label],y)))
        # Source projector has direction (-f_i,+e_i) and coefficient delta/2.
        factor=scale(F(1,2),mul(add(phase,scale(-1,ONE)),delta))
        yy=vadd(y,vscale(scale(-1,factor),f[label]));rr=list(r);rr[i]=add(rr[i],factor)
        return yy,rr
    def energy(label,state):return scalar(norm(mismatch(label,state)))/2
    # Validate all 22 source basis vectors, all six ports and a non-endpoint
    # pulse phase exp(-2pi i/3), exactly in Q(sqrt(2),i sqrt(3)).
    phase=(R(F(-1,2)),R(F(-1,2)))
    source_basis=[]
    for j in range(22):
        y=[ONE if i==j else Z for i in range(16)];r=[ONE if i+16==j else Z for i in range(6)]
        target=encode(y,r);source_basis.append(target)
        assert decode_target(target)==(y,r,[Z]*36)
        expected=add(record_inner(y,y),total(mul(conj(z),z) for z in r));assert inner(target,target)==expected
        for label in labels:
            for ph in ((R(-1),R()),phase):
                yy,rr=source_pulse(label,y,r,ph)
                assert pulse(label,target,ph)==encode(yy,rr)
    checks['all_six_pulses_intertwined_on_full_22D_source']=True
    # Gram comparison on an entire source basis proves the metric pairing,
    # not only agreement of the basis-vector norms.
    for i,a in enumerate(source_basis):
        for j,b in enumerate(source_basis):
            expected=H[i][j] if i<16 and j<16 else F(i==j) if i>=16 and j>=16 else F(0)
            assert inner(a,b)==(R(expected),R())
    checks['full_source_metric_pairing_preserved']=True
    # Test every ambient target coordinate, not just the encoded subspace.
    ambient_basis=[[ONE if i==j else Z for i in range(52)] for j in range(52)]
    for state in ambient_basis:
        y,r,spectator=decode_target(state);assert vadd(encode(y,r),spectator+[Z]*16)==state
        assert all(x==Z for x in amplitudes(spectator))
        for label in labels:
            P=projector(label,state);assert projector(label,P)==P
            assert inner(state,P)==(R(energy(label,state)),R())
            after=pulse(label,state)
            assert pulse(label,after)==state and budget(after)==budget(state)
            assert decode_target(after)[2]==spectator
            during=pulse(label,state,phase)
            assert budget(during)==budget(state) and energy(label,during)==energy(label,state)
            assert pulse(label,during,conj(phase))==state
    checks['all_52_coordinates_reconstructed_and_spectators_retained']=True
    checks['source_projector_energy_on_all_target_basis_vectors']=True
    checks['endpoint_and_nonendpoint_unitarity_and_inverse']=True
    # Self-adjointness follows from P=d d* M/2; verify its direction Gram
    # explicitly, which also reproduces every mixed pulse interaction.
    directions={label:modes[label]+vscale((R(-1),R()),f[label]) for label in labels}
    assert all(inner(directions[a],directions[b])==(R(gram[i][j]),R()) for i,a in enumerate(labels) for j,b in enumerate(labels))
    checks['all_port_direction_Gram_and_noncommutation_preserved']=True
    # Replay actual composable occurrences; retain full states and reverse them.
    initial=encode([Z]*16,[ONE if k==0 else Z for k in range(6)])
    assert labels[0]=='AB' and budget(initial)==1 and energy('AB',initial)==F(1,2)
    transferred=pulse('AB',initial)
    assert transferred[:36]==[Z]*36 and budget(transferred)==1
    assert budget(transferred[:36]+[Z]*16)==0
    checks['discarding_dynamic_record_bank_loses_the_entire_AB_excitation']=True
    history=[];state=initial
    word=['AB','BA','AB','BA']
    assert all(ends[a][1]==ends[b][0] for a,b in zip(word,word[1:]))
    def snapshot(v):return [encoded(x) for x in v]
    for serial,label in enumerate(word):
        before=state;state=pulse(label,state)
        history.append({'occurrence':serial,'label':label,'source':ends[label][0],'target':ends[label][1],
                        'native_triangle':rim[labels.index(label)],'energy':str(energy(label,before)),
                        'before':snapshot(before),'after':snapshot(state)})
        assert budget(state)==1
    assert [h['energy'] for h in history]==[s['pulse_energy'] for s in packets['energy']['history']]
    for h in reversed(history):
        state=pulse(h['label'],state);assert snapshot(state)==h['before']
    assert state==initial
    checks['full_occurrence_history_matches_prior_energy_and_reverses']=True
    # A genuine native coherent neutron state, with empty source record bank.
    # Norm S is inherited. Its unit-normalized rim overlap is sqrt(nu/S).
    S=scalar(dot(full,full,weights)[0]);coherent_energy=nu/(2*S)
    assert all(dot(v,full,weights)==(R(nu),R()) for v in modes.values())
    assert F(0)<6*nu/S<F(1)
    # Sample an exact unnormalized chart representative too, avoiding an
    # unnecessary extension by sqrt(nu/S). Normalize quadratic energies at end.
    coherent=full+[Z]*16;assert budget(coherent)==S/nu
    assert all(energy(label,coherent)/budget(coherent)==coherent_energy for label in labels)
    checks['native_coherent_preparation_energy_evaluated']=True
    mapping=[{'label':label,'source_endpoints':list(ends[label]),'triangle_index':t,'triangle':triangles[t],
              'source_record_feature_slot':slots[label],
              'native_support': [{'index':i,'axis':coordinates[i]['axis'],'d':coordinates[i]['d'],'numerator':encoded(z)} for i,z in enumerate(modes[label]) if z!=Z]}
             for label,t in zip(labels,rim)]
    result={'status':'passed','checks':checks,
            'policy':'Zip live source registry with genuine rim triangles in retained neutron triangle_order; an explicit address policy, not a derived vertex identification.',
            'source_dimension':22,'target_dimension':52,'native_neutron_dimension':36,'dynamical_source_record_bank_dimension':16,'native_spectator_dimension':30,
            'role_binding':'Source carrier y -> 16D record bank; source records r_i -> normalized native rim modes v_i. J(y,r)=(sum_i v_i r_i,y).',
            'source_label_to_native_port':mapping,'rim_mode_squared_norm':str(nu),'collective_mode_squared_norm':str(S),
            'target_coordinate_convention':'First 36 entries N have physical intrinsic coordinates N_j/sqrt(nu*d_j); last 16 entries y have unchanged source metric H.',
            'pulse_energy':'h_i=|<v_i,n>_neutron-<f_i,y>_source|^2/2',
            'pulse_projector':'P_i=direction_i direction_i^* M/2, direction_i=(v_i,-f_i)',
            'pulse_flow':'U_i(theta)=I+(exp(-i theta)-1)P_i',
            'unit_coherent_neutron_empty_record_bank':{'each_port_energy':str(coherent_energy),'full_budget':'1','addressed_native_weight':str(6*nu/S),'spectator_weight':str(1-6*nu/S)},
            'AB_preparation_history':history,
            'scope':'Exact conditional interaction binding. The record bank is dynamical and indispensable; this does not identify pulses with native L/G stages or C3 rotation, select the addressing policy or record preparation, or derive neutron rest energy.',
            'next_test':'Audit native C3 action on the six bound addresses and decide whether source port/address covariance requires enlargement. No C3 covariance is claimed here.'}
    bound=list(paths.values())+[Path(__file__).resolve(),ROOT/'research/nima/checkers/check_natural_tower_return.py',ROOT/'research/voevodsky/checkers/check_belt_three_by_twelve.py',ROOT/'research/voevodsky/checkers/check_coupled_six_piece_belt.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bound}
    out=ROOT/'research/strominger/results/neutron-canonical-record-binding.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'port_binding':[(m['label'],m['triangle']) for m in mapping],
                      'rim_norm':str(nu),'coherent_norm':str(S),'unit_coherent_neutron_each_port_energy':str(coherent_energy),
                      'native_spectator_weight':str(1-6*nu/S),'record_bank_dimension':16},indent=2))

if __name__=='__main__':main()
