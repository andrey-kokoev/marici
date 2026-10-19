"""Metric-aware neutronlike native-task audit and comparison to protonlike.
Fresh isolated intrinsic producer replay, no mutation of shared source stores.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from fractions import Fraction as F
from hashlib import sha256
from collections import Counter
import contextlib,io,json,random,sys
from check_proton_native_task_catalogue import ROOT,ZERO,ONE,eye,mzero,mm,mv,adj,madd,msub,mul,div,rank,nullspace,sparse,vector
from check_proton_single_probe_cycle import inverse
from verify_proton_native_task_catalogue import realify,rank as qrank,multiply as qmm
BASE=ROOT/'research/voevodsky'


def blocks(entries):
    A=mzero(108,108)
    for (r,c),B in entries.items():
        for i in range(36):
            for j in range(36):A[36*r+i][36*c+j]=B[i][j]
    return A

def sc(A,a):return [[mul(z,(F(a),F(0))) for z in row] for row in A]
def restore(p):
    A=mzero(*p['shape'])
    for i,j,x,y in p['entries']:A[i][j]=(F(x),F(y))
    return A

def main():
    cp=BASE/'inputs/neutron-native-relationship-tasks-v1.json';contract=json.loads(cp.read_text());storepath=ROOT/contract['native_store']
    original=storepath.read_bytes();store=json.loads(original)
    # Fresh geometry/frame/numerator replay into temporary owner-local outputs.
    import check_belt_three_by_twelve as producer
    saved=producer.BASE
    with TemporaryDirectory(prefix='neutron-native-task-') as temp:
        sandbox=Path(temp);(sandbox/'results').mkdir()
        for name in ('coupled_six_piece_belt_store.json','four_six_center_cones.json'):
            (sandbox/'results'/name).write_bytes((BASE/'results'/name).read_bytes())
        producer.BASE=sandbox
        try:
            with contextlib.redirect_stdout(io.StringIO()):producer.main()
        finally:producer.BASE=saved
        replay=json.loads((sandbox/'results/belt_three_by_twelve_store.json').read_text())
        replay_report=json.loads((sandbox/'results/belt_three_by_twelve.json').read_text())
    assert replay==store and replay_report['verification_passed'] and storepath.read_bytes()==original
    d=[F(c['d']) for c in store['coordinates']];metric=[1/x for x in d];M=mzero(36,36)
    for i,m in enumerate(metric):assert m>0;M[i][i]=(m,F(0))
    ops=[mzero(36,36) for _ in range(3)];seen=set();counts=Counter()
    for row in store['arrows']:
        k='LGN'.index(row['stage']);i,j=row['target'],row['source'];a,b,c,e=map(F,row['numerator'])
        assert b==e==0,'unexpected sqrt2 extension';assert (k,i,j) not in seen
        seen.add((k,i,j));counts[k]+=1;ops[k][i][j]=(a/d[j],c/d[j])
    L,G,N=ops;I=eye(36);Z=mzero(36,36)
    def sharp(A,weights):return [[mul(z,(weights[j]/weights[i],F(0))) for j,z in enumerate(r)] for i,r in enumerate(adj(A))]
    for A,r in ((L,3),(G,12),(N,1)):
        assert mm(A,A)==A and sharp(A,metric)==A and rank(A)==r
    assert mm(L,G)==mm(G,L)==N and mm(N,mm(G,L))==N
    # Negative control: printed numerator chart is not Euclidean-orthogonal.
    assert adj(L)!=L and adj(N)!=N
    diagnostics=[msub(I,L),msub(L,N),N]
    assert [rank(A) for A in diagnostics]==[33,2,1]
    for i,A in enumerate(diagnostics):
        assert sharp(A,metric)==A and mm(A,A)==A
        for j,B in enumerate(diagnostics):
            if i!=j:assert mm(A,B)==Z
    checks=['isolated_intrinsic_producer_all_coefficient_replay','native_metric_and_33_2_1_diagnostics']

    W=blocks({(1,0):L,(2,1):G,(0,2):N});P=blocks({(0,0):N,(1,1):N,(2,2):N});mw=metric*3
    Wsharp=sharp(W,mw);T=msub(W,mm(W,P));Ts=sharp(T,mw)
    Ps=blocks({(0,0):msub(L,N),(1,1):msub(G,N)})
    Pd=blocks({(1,1):msub(L,N),(2,2):msub(G,N)})
    Pz=msub(msub(msub(eye(108),P),Ps),Pd)
    assert mm(mm(W,W),W)==P and mm(T,T)==mzero(108,108)
    assert mm(Ts,T)==Ps and mm(T,Ts)==Pd
    assert [rank(A) for A in (W,mm(W,W),P,Ps,Pd,Pz)]==[16,3,3,13,13,79]
    K=sc(madd(W,Wsharp),F(1,2));paircross=madd(T,Ts);pair=madd(Ps,Pd)
    Eplus=sc(madd(pair,paircross),F(1,2));Eminus=sc(msub(pair,paircross),F(1,2))
    E1=sc(mm(P,madd(madd(eye(108),W),mm(W,W))),F(1,3))
    Emin=madd(Eminus,msub(P,E1));spectral=[(F(1),E1,1),(F(1,2),Eplus,13),(F(-1,2),Emin,15),(F(0),Pz,79)]
    for lam,E,r in spectral:assert rank(E)==r and mm(E,E)==E and mm(K,E)==sc(E,lam)
    checks.append('metric_sharp_staged_channels_and_same_aggregate_hermitian_spectrum')

    b=[row[0] for row in N];b=[div(z,b[0]) for z in b];B=mzero(36,3);C=mzero(3,36)
    for t in range(3):
        v=b[12*t:12*t+12];assert all(z!=ZERO for z in v)
        gram=mm(mm(adj([[z] for z in v]),[[M[12*t+i][12*t+j] for j in range(12)] for i in range(12)]),[[z] for z in v])[0][0]
        for i,z in enumerate(v):
            B[12*t+i][t]=z;C[t][12*t+i]=div(mul((z[0],-z[1]),(metric[12*t+i],F(0))),gram)
    assert mm(B,C)==L and mm(C,B)==eye(3)
    J=[[(F(1,3),F(0))]*3 for _ in range(3)]
    assert mm(G,B)==mm(B,J) and mm(N,B)==mm(B,J)
    assert mm(mm(B,J),C)==N
    def observe(anchors):return [A[j] for A in (I,L,N) for j in anchors]
    def predicted(anchors):
        sizes=[sum(12*t+i in anchors for i in range(12)) for t in range(3)]
        return sum(0 if k==0 else min(12,k+1) for k in sizes)+int(0<sizes.count(0)<3)
    profiles=[];rng=random.Random(1836)
    masks=[[],list(range(36)),[12*t for t in range(3)], [12*t+i for t in range(3) for i in range(11)],list(range(12))]
    masks += [[i for i in range(36) if rng.randrange(4)<p] for p in (1,2,3) for _ in range(8)]
    for anchors in masks:
        r=rank(observe(anchors));assert r==predicted(set(anchors))
        profiles.append({'addresses':anchors,'rank':r})
    # All12 choices of omitted coordinate in each sector; decoder is blockwise.
    decoder=None;measurement=None;raw=None;local=None
    for sector in range(3):
        for missing in range(12):
            omissions=[11]*3;omissions[sector]=missing
            rr=[12*t+i for t in range(3) for i in range(12) if i!=omissions[t]]
            ll=[next(12*t+i for i in range(12) if i!=omissions[t]) for t in range(3)]
            slots={i:j for j,i in enumerate(rr)};D=mzero(36,36)
            for i,j in slots.items():D[i][j]=ONE
            for t in range(3):
                k=12*t+omissions[t];j=ll[t];den=L[j][k];assert den!=ZERO
                D[k][33+t]=div(ONE,den)
                for i in range(12*t,12*t+12):
                    if i!=k:D[k][slots[i]]=div((-L[j][i][0],-L[j][i][1]),den)
            O=[I[j] for j in rr]+[L[j] for j in ll];assert mm(D,O)==I
            if omissions==[11]*3:decoder,measurement,raw,local=D,O,rr,ll
    assert rank(observe(raw))==36
    deletions=[]
    for j in raw:
        O=observe([i for i in raw if i!=j]);assert rank(O)==35
        w=nullspace(O)[0];assert mv(O,w)==[ZERO]*len(O)
        deletions.append({'removed':j,'kernel':vector(w)})
    checks.append('all_mask_rank_formula_33_address_decoder_and_every_minimal_address_deletion')

    # Real source C3 rotates paired-face sectors and preserves intrinsic slots.
    U=mzero(36,36)
    for i in range(36):U[(i+12)%36][i]=ONE
    assert mm(mm(U,U),U)==I and sharp(U,metric)==adj(U)
    for A in (L,G,N):assert mm(U,A)==mm(A,U)
    single=[mm(A,V)[0] for V in (I,U,mm(U,U)) for A in (I,L,N)]
    assert rank(single)==6 and rank(mm(single,B))==3
    checks.append('source_C3_fixed_probe_six_raw_modes_and_all_three_admitted_amplitudes')

    # Actual lower/lower and upper/upper rim triangles from native geometry.
    packet=json.loads((BASE/'results/coupled_six_piece_belt_store.json').read_text())
    triangles=packet['record']['triangles']
    rim_triangles=[i for i,t in enumerate(triangles) if (t[1].startswith('L') and t[2].startswith('L')) or (t[1].startswith('U') and t[2].startswith('U'))]
    assert len(rim_triangles)==6
    rim=[i for i,c in enumerate(store['coordinates']) if c['triangle'] in rim_triangles]
    assert [sum(i//12==s for i in rim) for s in range(3)]==[4,4,4]
    Orim=observe(rim);assert rank(Orim)==15 and rank(mm(Orim,B))==3
    kernel=nullspace(Orim);assert len(kernel)==21
    assert all(mv(L,w)==[ZERO]*36 for w in kernel)
    checks.append('actual_six_rim_triangle_visibility_and_21_hidden_locally_rejected_modes')

    # Repeat the same finite Gaussian rounded-packet attachment, but with the
    # NEUTRON metric and source/sink columns, never a copied proton B matrix.
    signedM=blocks({(0,0):M,(1,1):M,(2,2):M});Kform=mm(signedM,K)
    assert adj(Kform)==Kform
    indices=[]
    for j in range(108):
        trial=[[row[i] for i in indices+[j]] for row in Ps]
        if rank(trial)>len(indices):indices.append(j)
        if len(indices)==3:break
    X=[[row[i] for i in indices] for row in Ps];Y=mm(T,X);D=mm(mm(adj(X),signedM),X)
    assert mm(mm(adj(X),Kform),Y)==sc(D,F(1,2))
    arithmeticpath=BASE/'results/rh-gaussian-seed-packet-v1.json';arith=json.loads(arithmeticpath.read_text());Ga=restore(arith['rounded_packet'])
    Ba=madd(X,mm(mm(Y,inverse(D)),Ga))
    assert mm(mm(adj(Ba),Kform),Ba)==Ga and rank(Ba)==3
    # Independent arithmetic checks for the complete decoder and pullback.
    assert qmm(realify(sparse(decoder)),realify(sparse(measurement)))==realify(sparse(I))
    assert qmm(qmm(realify(sparse(adj(Ba))),realify(sparse(Kform))),realify(sparse(Ba)))==realify(sparse(Ga))
    assert qrank(realify(sparse(Orim)))==30
    checks.append('metric_correct_same_rounded_Weil_packet_attachment_and_independent_rational_audit')
    paths=[cp,storepath,ROOT/contract['producer'],BASE/'results/coupled_six_piece_belt_store.json',BASE/'results/four_six_center_cones.json',BASE/'checkers/check_coupled_six_piece_belt.py',BASE/'checkers/check_belt_operator_inputs.py',arithmeticpath,Path(__file__),Path(__file__).with_name('check_proton_native_task_catalogue.py'),Path(__file__).with_name('check_proton_single_probe_cycle.py'),Path(__file__).with_name('verify_proton_native_task_catalogue.py')]
    result={'status':'passed','verification_passed':True,'schema':'marici.voevodsky.neutron-native-relationship-tasks.v1',
      'classification':'exact_metric_aware_neutron_task_catalogue_and_cross_carrier_distinctions',
      'checks':[{'name':c,'passed':True} for c in checks],'active_obligation':contract['active_obligation'],
      'isolated_producer_replay':True,'coordinate_records':store['coordinates'],'triangle_order':store['triangle_order'],
      'metric_diagonal':[str(x) for x in metric],'native_operators':{s:sparse(A) for s,A in zip('LGN',ops)},
      'stage_supports':[counts[i] for i in range(3)],'projector_ranks':[3,12,1],'diagnostic_dimensions':[33,2,1],
      'local_mode_encoder':sparse(B),'local_mode_decoder':sparse(C),
      'staged':{'W':sparse(W),'K_metric_sharp':sparse(K),'K_sesquilinear_form':sparse(Kform),'source':sparse(Ps),'sink':sparse(Pd),
         'power_ranks':[16,3,3],'dimensions':[3,13,13,79],'source_channel_split':[2,11],
         'hermitian_spectrum':[[str(lam),r] for lam,_,r in spectral]},
      'observation_theorem':{'formula':'sum d(k_s)+indicator(0<number_empty_sectors<3), d(0)=0,d(k>0)=min(12,k+1)',
         'full_recovery_iff':'at least11 addresses in each of3 sectors','minimum_addresses':33,
         'profiles':profiles,'raw_addresses':raw,'local_addresses':local,'decoder':sparse(decoder),'measurement':sparse(measurement),
         'all_12_power_3_single_omission_layouts':'proved by blockwise decoder identities','deletion_witnesses':deletions},
      'rotation_probe':{'one_address_C3_native_rank':6,'one_address_C3_locally_admitted_rank':3,'source_action':sparse(U)},
      'rim_probe':{'triangle_indices':rim_triangles,'coordinate_addresses':rim,'full_input_rank':15,'locally_admitted_rank':3,
          'hidden_dimension':21,'every_hidden_direction_is_locally_rejected':True,'kernel_basis':[vector(w) for w in kernel]},
      'rounded_arithmetic_attachment':{'input_packet':sparse(Ga),'neutron_attachment':sparse(Ba),'exact_metric_signed_pullback':True,
          'independent_rational_check':True,'source_selected_RH_realization':False},
      'proton_comparison':{'supports':[108,432,1296],'ranks':[12,3,1],'diagnostics':[24,11,1],'minimum_addresses':24,
         'same_staged_rank_spectrum_and_signed_packet_capacity':True,'same_stage_preserving_tasks':False},
      'source_hashes':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths},
      'scope':contract['scope'],'shared_sources_or_stores_modified':False}
    out=BASE/'results/neutron-native-relationship-tasks-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'supports':result['stage_supports'],'ranks':result['projector_ranks'],
                     'diagnostic_dimensions':[33,2,1],'minimum_addresses':33,'rim_raw_rank':15,'rim_admitted_rank':3,
                     'same_rounded_Weil_packet_attached':True},indent=2))
if __name__=='__main__':main()
