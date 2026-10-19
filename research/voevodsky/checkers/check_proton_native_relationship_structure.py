"""Decompose only the actual stage-typed transfer list; no synthesized controls."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT,ZERO,ONE,eye,mzero,mm,mv,adj,madd,msub,mul,rank,trace,parse,sparse,vector,norm
from verify_proton_native_task_catalogue import realify,rank as qrank,multiply as qmm
from assemble_triangle_arrow_source import assemble

def scale(A,c):return [[mul(z,c) for z in r] for r in A]
def blocks(entries,n=36):
    out=mzero(3*n,3*n)
    for (r,c),A in entries.items():
        for i in range(n):
            for j in range(n):out[r*n+i][c*n+j]=A[i][j]
    return out

def main():
    cp=ROOT/'research/voevodsky/inputs/proton-native-relationship-structure-v1.json';contract=json.loads(cp.read_text())
    sp=ROOT/contract['source'];mp=ROOT/contract['manifest'];report,records=assemble(json.loads(sp.read_text()))
    assert records==json.loads(mp.read_text())
    ports,(L,G,N)=parse(records);I=eye(108);Z=mzero(108,108)
    W=blocks({(1,0):L,(2,1):G,(0,2):N});Wd=adj(W);W2=mm(W,W);W3=mm(W2,W)
    assert sum(z!=ZERO for r in W for z in r)==1836
    P=blocks({(0,0):N,(1,1):N,(2,2):N})
    assert W3==P
    # W^4 = W P, not W on transient inputs.
    assert mm(W3,W)==mm(W,P) and mm(W3,W3)==P
    assert mm(W,P)==mm(P,W)
    T=msub(W,mm(W,P));Td=adj(T)
    Ps=blocks({(0,0):msub(L,N),(1,1):msub(G,N)})
    Pd=blocks({(1,1):msub(L,N),(2,2):msub(G,N)})
    Pz=msub(msub(msub(I,P),Ps),Pd)
    for Q,d in ((P,3),(Ps,13),(Pd,13),(Pz,79)):
        assert adj(Q)==Q and mm(Q,Q)==Q and rank(Q)==d
    for Q in (P,Ps,Pd,Pz):
        for R in (P,Ps,Pd,Pz):
            if Q is not R:assert mm(Q,R)==Z
    assert mm(T,T)==Z and mm(Td,T)==Ps and mm(T,Td)==Pd
    assert mm(T,Ps)==T and mm(Pd,T)==T and mm(W,Pz)==Z
    assert mm(W,Ps)==T and mm(W,Pd)==Z
    assert rank(W)==16 and rank(W2)==rank(W3)==3
    assert mm(Wd,W)==madd(P,Ps) and mm(W,Wd)==madd(P,Pd)
    checks=['fresh_all_entry_reconstruction','orthogonal_recurrent_source_sink_zero_decomposition','exact_directed_partial_isometry_and_composition_ranks']

    omega=(F(-1,2),F(1,2));omega2=mul(omega,omega)
    recurrent=[]
    for lam in (ONE,omega,omega2):
        # lambda^-1 = conjugate(lambda) for roots of unity.
        invlam=(lam[0],-lam[1]);E=scale(mm(P,madd(madd(I,scale(W,invlam)),scale(W2,mul(invlam,invlam)))),(F(1,3),F(0)))
        assert adj(E)==E and mm(E,E)==E and rank(E)==1 and mm(W,E)==scale(E,lam)
        recurrent.append(E)
    assert madd(madd(*recurrent[:2]),recurrent[2])==P
    for i,E in enumerate(recurrent):
        for j,R in enumerate(recurrent):
            if i!=j:assert mm(E,R)==Z
    checks.append('three_exact_collective_phase_projectors')

    # Hermitian quadratures are analytical constructions, not admitted native
    # reverse transfers or selected dynamics. W is recoverable from both.
    K=scale(madd(W,Wd),(F(1,2),F(0)))
    Y=scale(msub(W,Wd),(F(0),F(-1,6))) # 1/(2 sqrt(-3))
    assert adj(K)==K and adj(Y)==Y and madd(K,scale(Y,(F(0),F(1))))==W
    comm=msub(mm(K,Y),mm(Y,K));expected=scale(msub(Ps,Pd),(F(0),F(-1,6)))
    assert comm==expected and trace(comm)==ZERO and rank(comm)==26
    # Orthogonal Hermitian-part spectrum: two signs on thirteen one-way pairs
    # and the symmetric parts of the three recurrent root-of-unity eigenvalues.
    Ppair=madd(Ps,Pd);paircross=madd(T,Td)
    Eplus=scale(madd(Ppair,paircross),(F(1,2),F(0)))
    Eminus=scale(msub(Ppair,paircross),(F(1,2),F(0)))
    spectral=[(ONE,recurrent[0],1),((F(1,2),F(0)),Eplus,13),
              ((F(-1,2),F(0)),madd(Eminus,madd(recurrent[1],recurrent[2])),15),(ZERO,Pz,79)]
    reconstruction=Z
    for lam,E,d in spectral:
        assert adj(E)==E and mm(E,E)==E and rank(E)==d and mm(K,E)==scale(E,lam)
        reconstruction=madd(reconstruction,scale(E,lam))
    assert reconstruction==K
    for i,(_,E,_) in enumerate(spectral):
        for j,(_,R,_) in enumerate(spectral):
            if i!=j:assert mm(E,R)==Z
    checks.append('hermitian_quadratures_exact_spectrum_and_noncanonical_commutator')

    # Concrete native state moved forward, lost at next application, and sent
    # backward by the derived adjoint. It illustrates what a Hermitian part adds.
    j=next(i for i in range(108) if Ps[i][i]!=ZERO)
    x=[row[j] for row in Ps];y=mv(W,x)
    assert norm(x)==norm(y)!=ZERO and mv(W,y)==[ZERO]*108 and mv(Wd,y)==x
    assert mv(K,y)==[(z[0]/2,z[1]/2) for z in x]
    checks.append('explicit_one_way_channel_and_adjoint_reverse_witness')

    # Independent rational verification: exact products and full ranks. All
    # retained data concern the native list, not only its support pattern.
    qW=realify(sparse(W));qP=realify(sparse(P));qT=realify(sparse(T))
    assert qmm(qmm(qW,qW),qW)==qP
    assert qmm(qT,qT)==[[F(0)]*216 for _ in range(216)]
    assert qrank(qW)==32 and qrank(qT)==26
    checks.append('independent_rational_realification')
    files=[cp,sp,mp,Path(__file__),Path(__file__).with_name('check_proton_native_task_catalogue.py'),Path(__file__).with_name('verify_proton_native_task_catalogue.py'),ROOT/'research/nima/checkers/assemble_triangle_arrow_source.py',ROOT/'research/nima/checkers/check_twelve_triangle_positive_geometry.py',ROOT/'research/nima/checkers/check_triangle_half_phase.py',ROOT/'research/nima/checkers/check_collective_four_state_identity.py']
    result={'status':'passed','verification_passed':True,'schema':'marici.voevodsky.native-relationship-structure.v1',
      'classification':'exact_native_transfer_invariant_decomposition_not_physical_hamiltonian_selection',
      'active_obligation':contract['active_obligation'],'checks':[{'name':c,'passed':True} for c in checks],
      'stage_ports':[[s,*p] for s in ('raw','local','aligned') for p in ports],
      'operator':sparse(W),'collective_stage_projector':sparse(P),'transient_operator':sparse(T),
      'source_projector':sparse(Ps),'sink_projector':sparse(Pd),'immediately_zero_projector':sparse(Pz),
      'dimensions':{'recurrent':3,'one_way_source':13,'one_way_sink':13,'immediately_zero':79},
      'one_way_channels':{'raw_to_local_locally_valid_disagreement':11,'local_to_aligned_frame_consistent_but_locally_invalid':2},
      'power_ranks':[16,3,3],'native_is_hermitian':False,'native_is_normal':False,'native_is_invertible':False,
      'recurrent_eigenvalues':['1','omega','omega^2'],'recurrent_eigenprojectors':[sparse(E) for E in recurrent],
      'transient_Jordan_blocks':{'size_2':13,'size_1':79},
      'hermitian_analysis':{'K':sparse(K),'Y':sparse(Y),'commutator':sparse(comm),'commutator_rank':26,
         'spectrum_K':[{'eigenvalue':[str(v) for v in lam],'multiplicity':d,'projector':sparse(E)} for lam,E,d in spectral],
         'reverse_relationships_are_new_primitive_operations':False,'physical_hamiltonian_selected':False,
         'canonical_scalar_commutator':False},
      'one_way_example':{'input':vector(x),'output':vector(y),'norm_squared':vector([norm(x)]),
         'second_application_zero':True,'adjoint_recovers_input_from_output':True},
      'source_hashes':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in files},
      'shared_sources_or_stores_modified':False,'scope':contract['scope']}
    out=ROOT/'research/voevodsky/results/proton-native-relationship-structure-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'dimensions':result['dimensions'],'power_ranks':result['power_ranks'],
       'spectrum_K':[(str(lam),d) for lam,_,d in spectral]},indent=2))
if __name__=='__main__':main()
