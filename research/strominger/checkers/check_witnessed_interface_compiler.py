"""One exact metric/residual construction for transport, seams and bank pulses."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from check_neutron_canonical_occupied_closure import inverse,rank
from check_belt_local_field_lift import (ROOT,BASE,decode,conj,mul,norm,mat,inv2,inner,inv,compose,adjoint,Z)

def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):
    out=[[F(0) for _ in b[0]] for _ in a]
    for i,row in enumerate(a):
        for k,x in enumerate(row):
            if x:
                for j,y in enumerate(b[k]):
                    if y:out[i][j]+=x*y
    return out
def plus(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(q,a):return [[q*x for x in r] for r in a]
def minus(a,b):return plus(a,scale(-1,b))
def mv(a,v):return [sum(x*y for x,y in zip(r,v)) for r in a]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def blockdiag(a,b):return [r+[F(0)]*len(b) for r in a]+[[F(0)]*len(a)+r for r in b]
def enc(a):return [[str(x) for x in r] for r in a]
def rat(a):return [[F(x) for x in r] for r in a]
hashes={}
def read(p):
    raw=(ROOT/p).read_bytes();hashes[p]=hashlib.sha256(raw).hexdigest();return json.loads(raw)

def compile_interface(M,B):
    """No dispatch on interface kind and no target operator input."""
    n=len(M);k=len(B);Mi=inverse(M)
    G=mm(mm(B,Mi),tr(B));Gamma=inverse(G)
    A=mm(mm(Mi,tr(B)),Gamma);Q=mm(A,B);N=minus(eye(n),Q)
    U=[N[i]+A[i] for i in range(n)]+[B[i]+[F(0)]*k for i in range(k)]
    metric=blockdiag(M,Gamma)
    assert mm(B,A)==eye(k) and mm(Q,Q)==Q
    assert mm(tr(Q),M)==mm(M,Q)
    assert mm(U,U)==eye(n+k) and mm(mm(tr(U),metric),U)==metric
    # Ready-memory state x -> (Nx,Bx); energy Q moves into the record.
    assert mm(mm(tr(B),Gamma),B)==mm(M,Q)
    return {'input_metric':M,'residual':B,'memory_metric':Gamma,'injection':A,'projector':Q,'reflection':minus(eye(n),scale(2,Q)),'swap':U}

def realify(B):
    out=[[F(0)]*4 for _ in range(4)]
    for (i,j),(a,b) in B.items():
        assert a.b==b.b==0
        out[i][j]=a.a;out[i][j+2]=-3*b.a;out[i+2][j]=b.a;out[i+2][j+2]=a.a
    return out

def main():
    read('research/strominger/inputs/witnessed-interface-compiler-protocol-v1.json')
    src=read('research/strominger/results/neutron-seam-control-transport.json');assert src['status']=='passed'
    binding=read('research/strominger/results/neutron-canonical-record-binding.json')
    native=read('research/voevodsky/results/belt_three_by_twelve_store.json')
    lift=read('research/strominger/results/belt-local-field-lift/verification.json');assert lift['status']=='pass'
    M=rat(src['metric']);Rot=rat(src['native_rotation']);order=native['triangle_order']
    contracts={};seams=[];B=[];gammas=[]
    for i,s in enumerate(src['seam_controls']):
        a,b=s['ordered_triangle_positions'];row=[F(j==a)-F(j==b) for j in range(24)]
        c=compile_interface(M,[row]);assert c['projector']==rat(s['projector'])
        seams.append(c);B.append(row);gammas.append(c['memory_metric'][0][0]);contracts[f'seam:{i}']=c
    assert len(seams)==21 and rank(B)==15
    slots={p['label']:j for j,p in enumerate(binding['source_label_to_native_port'])}
    ports={p['label']:order.index(p['triangle_index']) for p in binding['source_label_to_native_port']}
    for pulse in src['source_pulses']:
        label=pulse['label'];v=[F(0)]*24;v[ports[label]]=1;v[18+slots[label]]=-1
        for _ in range(pulse['frame']):v=mv(Rot,v)
        row=mv(tr(M),v)
        c=compile_interface(M,[row]);assert c['projector']==rat(pulse['projector'])
        contracts[f'pulse:{label}@{pulse["frame"]}']=c
    assert len(src['source_pulses'])==18
    # Full field transports on the twelve actual ports, not only mode labels.
    d=[F(c['d']) for c in native['coordinates']];z=[decode(c['selected_numerator']) for c in native['coordinates']]
    word=[order.index(t) for t in lift['metric_port_loop']];hol=eye(4)
    for i,(a,b) in enumerate(zip(word,word[1:])):
        wa,wb=z[2*a:2*a+2],z[2*b:2*b+2];da,db=d[2*a:2*a+2],d[2*b:2*b+2]
        ca=inner(wa,tuple(map(conj,wa)),da);cb=inner(wb,tuple(map(conj,wb)),db)
        q=mul(ca,inv(cb));T=compose(mat((wb,tuple(mul(q,conj(x)) for x in wb))),inv2(mat((wa,tuple(map(conj,wa))))))
        T=realify(T);hol=mm(T,hol)
        ma=[[F(0)]*4 for _ in range(4)];mb=[[F(0)]*4 for _ in range(4)]
        for k in range(4):ma[k][k]=F(1 if k<2 else 3)/da[k%2];mb[k][k]=F(1 if k<2 else 3)/db[k%2]
        assert mm(mm(tr(T),mb),T)==ma
        residual=[[-x for x in T[j]]+eye(4)[j] for j in range(4)]
        c=compile_interface(blockdiag(ma,mb),residual)
        graph=eye(4)+T
        assert mm(c['projector'],graph)==[[F(0)]*4 for _ in range(8)]
        Ti=inverse(T)
        exchange=[[F(0)]*4+Ti[j] for j in range(4)]+[T[j]+[F(0)]*4 for j in range(4)]
        assert c['reflection']==exchange
        contracts[f'transport:{i}']=c
    assert hol==eye(4)
    # Reuse the earlier occurrence-memory space and its derived metric.
    oldmemory=read('research/strominger/results/neutron-comparison-memory.json')
    Gamma=[[gammas[i]*F(i==j) for j in range(21)] for i in range(21)]
    memory_operator=mm(mm(mm(B,inverse(M)),tr(B)),Gamma)
    assert B==rat(oldmemory['residual_incidence']) and Gamma==rat(oldmemory['memory_metric'])
    assert memory_operator==rat(oldmemory['rational_memory_operator'])
    assert rank(memory_operator)==15 and len(memory_operator)-rank(memory_operator)==6
    fullmetric=blockdiag(M,Gamma)
    def write(i,state):
        x=state[:24];m=state[24+i];c=seams[i]
        residual=dot(B[i],x);v=[a[0] for a in c['injection']]
        out=list(state);out[:24]=[a+b*(m-residual) for a,b in zip(x,v)];out[24+i]=residual
        return out
    def budget(x):return dot(x,mv(fullmetric,x))
    # Full rational basis probes plus a mixed state, not just the dark coherent mode.
    initial=[F((i%5)-2, i+1) for i in range(24)]+[F(0)]*21;state=initial;steps=[];E=budget(state)
    sequence=[0,1,2,6,7,13,20,0]
    for i in sequence:
        out=write(i,state);assert budget(out)==E and write(i,out)==state
        steps.append({'interface':i,'input':list(map(str,state)),'output':list(map(str,out))});state=out
    assert any(state[24:])
    retained=state[:];dropped=state[:24]+[F(0)]*21
    for i in reversed(sequence):state=write(i,state);dropped=write(i,dropped)
    assert state==initial and dropped!=initial
    # New local storage gates do not silently become commuting simultaneous encoders.
    assert write(1,write(0,initial))!=write(0,write(1,initial))
    # Neither norm nor energy of one stored residual establishes conservation
    # of the UNCHANGED total native plus occurrence-memory Hamiltonian.
    S=[[F(0)]*24 for _ in range(24)]
    for c in seams:S=plus(S,c['projector'])
    K=plus(scale(F(1,4),rat(src['native_energy'])),S)
    Hfixed=blockdiag(K,memory_operator)
    energy=lambda x:dot(x,mv(fullmetric,mv(Hfixed,x)))
    witness=None
    for i in range(24):
        x=[F(j==i) for j in range(45)];y=write(0,x)
        delta=energy(y)-energy(x)
        if delta:witness={'basis_input':i,'write_interface':0,'energy_change':str(delta)};break
    assert witness is not None
    # Occupied source-bank feature Gram is positive/nondegenerate, hence rank6.
    bankGram=[r[18:] for r in M[18:]];protected=rank(bankGram);assert protected==6
    spare=16-protected;assert spare==10 and spare<rank(B)
    # On all arbitrary bank inputs, requiring the16D bank fixed pointwise
    # leaves no write port at all: unitary orthogonality forbids cross blocks.
    checks={'one_compiler_recovers_all21_seam_projectors':True,'same_compiler_recovers_all18_bank_pulses':True,
      'same_compiler_handles12_full_field_graph_interfaces':True,'full12_port_transport_loop_retained':True,
      'existing21_slot_memory_metric_and_operator_reproduced':True,'local_record_swaps_unitary_and_involutive':True,
      'ordered_writes_reverse_with_complete_memory':True,'deletion_and_commutation_hostiles_detected':True,
      'unchanged_total_energy_conservation_rejected':True,'simultaneous15_residual_storage_exceeds10_spare_bank_directions':True}
    for p in [Path(__file__),BASE/'checkers/check_belt_local_field_lift.py',BASE/'checkers/check_neutron_canonical_occupied_closure.py']:
        hashes[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    out=BASE/'results/witnessed-interface-compiler';out.mkdir(parents=True,exist_ok=True)
    (out/'contracts.json').write_text(json.dumps({name:{k:enc(v) for k,v in c.items()} for name,c in contracts.items()},indent=2)+'\n')
    (out/'history.json').write_text(json.dumps(steps,indent=2)+'\n')
    result={'status':'pass','checks':checks,'source_hashes':hashes,'compiled_interfaces':len(contracts),
      'dimensions':{'source_envelope_complex':24,'existing_full_bank_complex':16,'protected_bank_feature_span_complex':protected,'unused_orthogonal_bank_complex':spare,'independent_seam_residuals_complex':rank(B),'reused_occurrence_memory_complex':21,'occurrence_dependencies':6},
      'unchanged_total_energy_counterexample':witness,
      'scope':'Common normalized residual/energy/record compiler; source comparisons and metrics are inputs. New sequential record writes retain existing memory slots, are reversible, but are not the old simultaneous polar encoder or an energy-conserving execution of the unchanged autonomous Hamiltonian. No physical-time law, new bank fit, or full arbitrary52D bank reduction is inferred.'}
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'interfaces':len(contracts),'energy_counterexample':witness,'spare_bank':spare,'residual_rank':rank(B)}))
if __name__=='__main__':main()
