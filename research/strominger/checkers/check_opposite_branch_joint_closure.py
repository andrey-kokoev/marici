"""Joint native-energy/source-pulse closure, no prescribed target dimension.
Uses the already source-checked branch adapter; all arithmetic is exact.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from check_opposite_branch_canonical import (ROOT,BASE,R,Z,ONE,decode,encoded,scale,conj,norm,add,total,identity,compose,cmat,entries,diag,dump)
from check_neutron_canonical_occupied_closure import mm,transpose,inverse,rank
hashes={}
def read(p):
    raw=(ROOT/p).read_bytes();hashes[p]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def rational(A,n):
    out=[[F(0)]*n for _ in range(n)]
    for (i,j),v in A.items():
        assert v[1]==0 and v[0].b==0
        out[i][j]=v[0].a
    return out
def mv(A,v):return [sum(a*x for a,x in zip(row,v)) for row in A]
def enc(A):return [[str(x) for x in row] for row in A]
def sub(A,B):return [[a-b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def columns(vs):return list(map(list,zip(*vs)))

def main():
    read('research/strominger/inputs/opposite-branch-joint-closure-protocol-v1.json')
    prior=read('research/strominger/results/opposite-branch-canonical/verification.json');assert prior['status']=='pass'
    for p,h in prior['sourceHashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    packet=read('research/strominger/results/opposite-branch-canonical/operators.json')
    native=read('research/voevodsky/results/belt_three_by_twelve_store.json')
    branch=read('research/voevodsky/results/opposite_branch_belt_store.json')
    binding=read('research/strominger/results/neutron-canonical-record-binding.json')
    closure=read('research/strominger/results/neutron-canonical-occupied-closure.json')
    rotation=read('research/strominger/results/neutron-canonical-rotation-frame.json')
    oldenergy=read('research/voevodsky/results/native_operation_energy_lift_store.json')['carriers']['belt']
    coords=native['coordinates'];d=[F(c['d']) for c in coords];nu=F(binding['rim_mode_squared_norm'])
    zz=list(map(decode,branch['selected_numerators']));z=[decode(c['selected_numerator']) for c in coords]
    u=tuple(map(decode,packet['nativeDiagonalAdapter']))+(ONE,)*16;U=diag(u);Us=diag(tuple(map(conj,u)))
    ports=binding['source_label_to_native_port'];labels=[p['label'] for p in ports]
    H4=[[F(10*int(i==j)+1) for j in range(4)] for i in range(4)]
    Hbank=[[H4[i//4][j//4]*H4[i%4][j%4] for j in range(16)] for i in range(16)]
    slots=[p['source_record_feature_slot'] for p in ports]
    G=[[Hbank[a][b]/121 for b in slots] for a in slots];Gi=inverse(G)
    assert G==[[F(x) for x in row[6:12]] for row in closure['envelope']['metric'][6:12]]
    norms=[sum((norm(z[2*t+k])/d[2*t+k] for k in range(2)),R()) for t in range(18)]
    assert all(x.b==0 and x.a>0 for x in norms);norms=[x.a for x in norms]
    def envelope(v):
        E={(i,i//2):x for i,x in enumerate(v)}
        E.update({(36+slot,18+j):(R(F(1,11)),R()) for j,slot in enumerate(slots)})
        L={(t,2*t+k):scale(1/(norms[t]*d[2*t+k]),conj(v[2*t+k])) for t in range(18) for k in range(2)}
        for i in range(6):
            for j in range(16):
                q=sum(Gi[i][k]*Hbank[slots[k]][j]/11 for k in range(6))
                if q:L[18+i,36+j]=(R(q),R())
        assert compose(L,E)==identity(24)
        return E,L
    E,L=envelope(z);EE,LL=envelope(zz);assert compose(U,E)==EE
    M=[[F(0)]*24 for _ in range(24)]
    for i in range(18):M[i][i]=norms[i]/nu
    for i in range(6):
        for j in range(6):M[18+i][18+j]=G[i][j]
    Hnew=entries(packet['signedCharacterHamiltonianIn4HOverPiUnits']);Hold=entries(oldenergy['entries'])
    Kn=compose(compose(LL,Hnew),EE);Ko=compose(compose(L,Hold),E)
    assert Kn==Ko and compose(Hnew,EE)==compose(EE,Kn) and compose(Hold,E)==compose(E,Ko)
    K=rational(Kn,24);assert mm(transpose(K),M)==mm(M,K)
    T={(j,i):ONE for i,j in enumerate(rotation['native_coordinate_permutation'])};T.update({(i,i):ONE for i in range(36,52)})
    RR=compose(compose(LL,T),EE);assert compose(T,EE)==compose(EE,RR)
    Rot=rational(RR,24);assert mm(mm(transpose(Rot),M),Rot)==M
    projectors={}
    for key,data in packet['canonicalProjectors'].items():
        P=entries(data);small=compose(compose(LL,P),EE)
        assert compose(P,EE)==compose(EE,small)
        old=compose(compose(Us,P),U)
        assert compose(old,E)==compose(E,small)
        A=rational(small,24);assert mm(A,A)==A and mm(transpose(A),M)==mm(M,A)
        projectors[key]=A
    checks={'full_52D_native_energy_C3_and_18_pulses_have_same_24D_envelope':True}
    # First test the old 11D subfamily closure, without changing its basis.
    E13=[[F(0)]*13 for _ in range(24)]
    rim_indices=[native['triangle_order'].index(p['triangle_index']) for p in ports]
    for j,t in enumerate(rim_indices):E13[t][j]=1
    for j in range(6):E13[18+j][6+j]=1
    for t in range(18):E13[t][12]=F(t not in rim_indices)
    B11=mm(E13,[[F(x) for x in row] for row in closure['minimal_closure']['basis_columns']])
    assert rank(B11)==11
    HB=mm(K,B11);one_step_rank=rank([a+b for a,b in zip(B11,HB)])
    assert one_step_rank>11
    checks['old_11D_pulse_only_closure_fails_native_energy_invariance']=True
    # Source-generated minimal span. Echelon reduction changes basis only by
    # linear combinations of already generated vectors; no readout fitting.
    initial=[F(1)]*18+[F(0)]*6
    generators=[Rot,K]+[projectors[f'{label}@0'] for label in labels]
    basis=[];pivots=[];witnesses=[]
    def admit(v,witness):
        v=list(v)
        for p,b in zip(pivots,basis):
            q=v[p]
            if q:v=[x-q*y for x,y in zip(v,b)]
        p=next((i for i,x in enumerate(v) if x),None)
        if p is None:return
        q=v[p];basis.append([x/q for x in v]);pivots.append(p);witnesses.append(witness)
    admit(initial,{'kind':'specified_coherent_preparation'})
    cursor=0
    while cursor<len(basis):
        for gi,A in enumerate(generators):admit(mv(A,basis[cursor]),{'basis_parent':cursor,'generator':gi})
        cursor+=1
    B=columns(basis);dim=len(basis);assert rank(B)==dim
    pivot_matrix=[[B[i][j] for j in range(dim)] for i in pivots]
    pi=inverse(pivot_matrix)
    left=[[F(0)]*24 for _ in range(dim)]
    for i in range(dim):
        for j,p in enumerate(pivots):left[i][p]=pi[i][j]
    assert mm(left,B)==[[F(i==j) for j in range(dim)] for i in range(dim)]
    metric=mm(mm(transpose(B),M),B)
    compressed={}
    for name,A in [('native_energy',K),('native_C3',Rot)]+list(projectors.items()):
        small=mm(mm(left,A),B)
        assert mm(A,B)==mm(B,small),name
        if name=='native_C3':assert mm(mm(transpose(small),metric),small)==metric
        else:assert mm(transpose(small),metric)==mm(metric,small)
        compressed[name]=small
    assert mv(B,mv(left,initial))==initial
    assert mm(B,mm(left,B11))==B11
    Full=compose(EE,cmat(B));assert compose(Us,Full)==compose(E,cmat(B))
    for key,A in projectors.items():
        P=entries(packet['canonicalProjectors'][key])
        assert compose(P,Full)==compose(Full,cmat(compressed[key]))
    assert compose(Hnew,Full)==compose(Full,cmat(compressed['native_energy']))
    checks['minimal_joint_closure_generated_and_all_20_generators_intertwined']=True
    checks['both_branches_share_exact_closed_metric_and_full_reconstruction']=True
    # Every direction at nonzero frame is obtained by native C3 conjugation.
    for label in labels:
        P=projectors[label+'@0']
        for frame in range(3):
            assert P==projectors[f'{label}@{frame}']
            P=mm(mm(Rot,P),mm(Rot,Rot))
    checks['six_frame_zero_pulses_and_C3_generate_all_18_addresses']=True
    # Preserve the common fixed sector rather than declaring a full rest gap.
    stack=K+[row for A in projectors.values() for row in A]
    common_kernel=24-rank(stack)
    stack_small=compressed['native_energy']+[row for key,A in compressed.items() if '@' in key for row in A]
    fixed=dim-rank(stack_small)
    checks['joint_common_zero_sector_retained']=True
    source=Path(__file__);hashes[source.relative_to(ROOT).as_posix()]=hashlib.sha256(source.read_bytes()).hexdigest()
    out=BASE/'results/opposite-branch-joint-closure';out.mkdir(parents=True,exist_ok=True)
    matrices={'envelopeMetric':enc(M),'minimalBasisColumns':enc(B),'generationWitnesses':witnesses,'metric':enc(metric),'leftInverse':enc(left),'initialCoordinates':list(map(str,mv(left,initial))),'generators':{k:enc(A) for k,A in compressed.items()},'full52DNativeBankEmbedding':dump(Full)}
    (out/'operators.json').write_text(json.dumps(matrices,indent=2)+'\n')
    result={'schema':'marici.opposite-branch-joint-closure.v1','status':'pass','checks':checks,'sourceHashes':hashes,
      'dimensions':{'preparedEnvelopeComplex':24,'pulseOnlyClosureComplex':11,'oldClosurePlusOneNativeEnergyImageRank':one_step_rank,'jointMinimalClosureComplex':dim,'jointRealCanonical':2*dim,'unreachedEnvelopeComplementComplex':24-dim,'commonZeroSectorEnvelopeComplex':common_kernel,'commonZeroSectorReachableComplex':fixed},
      'disposition':'The source-only 11D closure does not include native energy. The exactly generated joint closure transports with the signed-character branch adapter. No autonomous sum, physical branch selection, dissipation, rest gap or nuclear binding is inferred.'}
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'dimensions':result['dimensions']}))

if __name__=='__main__':main()
