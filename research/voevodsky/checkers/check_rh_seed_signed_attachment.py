"""Faithful finite signed-form expressibility; deliberately no RH proof claim."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT,ZERO,ONE,eye,mzero,mm,mv,adj,madd,msub,rank,sparse,vector,norm,trace
from check_proton_single_probe_cycle import inverse
from check_proton_unitary_probe_repair import restore
from verify_proton_native_task_catalogue import realify,rank as qrank,multiply as qmm

def selectcols(A,indices):return [[row[j] for j in indices] for row in A]
def real(A):return [[(F(z),F(0)) for z in row] for row in A]
def qvalue(G,v):
    out=mm(mm(adj([[z] for z in v]),G),[[z] for z in v])
    return out[0][0]

def main():
    cp=ROOT/'research/voevodsky/inputs/rh-seed-signed-attachment-v1.json';contract=json.loads(cp.read_text())
    priorpath=ROOT/contract['source_result'];prior=json.loads(priorpath.read_text())
    for p,h in prior['source_hashes'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    K=restore(prior['hermitian_analysis']['K']);Ps=restore(prior['source_projector']);T=restore(prior['transient_operator'])
    chosen=[]
    for j in range(108):
        if rank(selectcols(Ps,chosen+[j]))>len(chosen):chosen.append(j)
        if len(chosen)==13:break
    X=selectcols(Ps,chosen);Y=mm(T,X);D=mm(adj(X),X)
    assert rank(X)==rank(Y)==13 and mm(adj(Y),Y)==D
    Z=mzero(13,13)
    assert mm(mm(adj(X),K),X)==mm(mm(adj(Y),K),Y)==Z
    halfD=[[(z[0]/2,z[1]/2) for z in r] for r in D]
    assert mm(mm(adj(X),K),Y)==halfD
    # For any Hermitian G, not just these examples: B=X+Y D^-1 G.
    def attach(G):
        n=len(G);Xn=selectcols(X,list(range(n)));Yn=selectcols(Y,list(range(n)))
        Dn=mm(adj(Xn),Xn)
        B=madd(Xn,mm(mm(Yn,inverse(Dn)),G))
        assert G==adj(G) and rank(B)==n and mm(mm(adj(B),K),B)==G
        return B
    positive=eye(3);bad=real([[1,F(-3,5),F(-3,5)],[F(-3,5),1,F(-3,5)],[F(-3,5),F(-3,5),1]])
    invisible=real([[1,0,0],[0,0,0],[0,0,0]])
    packets={}
    for name,G in [('positive',positive),('coherent_indefinite',bad),('positive_degenerate',invisible)]:
        B=attach(G)
        assert qrank(realify(sparse(B)))==6
        assert qmm(qmm(realify(sparse(adj(B))),realify(sparse(K))),realify(sparse(B)))==realify(sparse(G))
        # Two source-rooted triangles share Xpacket -> native B. Both chart
        # routes are constructed explicitly from supplied G, not independent
        # arithmetic and zero-side source objects.
        R=real([[1,1,0],[0,1,1],[0,0,1]]);Ri=inverse(R)
        Br=mm(B,Ri);Gr=mm(mm(adj(Ri),G),Ri)
        assert mm(Br,R)==B and mm(mm(adj(Br),K),Br)==Gr
        assert mm(mm(adj(R),Gr),R)==G
        packets[name]={'form':sparse(G),'attachment':sparse(B),'chart_change':sparse(R),
          'changed_chart_attachment':sparse(Br),'changed_chart_form':sparse(Gr),'triangles_commute':True}
    witness=[ONE]*3;value=qvalue(bad,witness)
    assert value==(F(-3,5),F(0)) and qvalue(K,mv(restore(packets['coherent_indefinite']['attachment']),witness))==value
    # Every 2x2 principal restriction is positive: determinant16/25 and diag1.
    for i in range(3):
        for j in range(i+1,3):assert bad[i][i][0]*bad[j][j][0]-bad[i][j][0]**2==F(16,25)
    v=[ZERO,ONE,ZERO];Bi=restore(packets['positive_degenerate']['attachment'])
    assert norm(mv(Bi,v))[0]>0 and qvalue(invisible,v)==ZERO
    # The construction also supports arbitrary dimension13 Hermitian data.
    G13=real([[F((i+1) if i==j else (1 if abs(i-j)==1 else 0)) for j in range(13)] for i in range(13)])
    B13=attach(G13)
    # Principal form restrictions commute, while this particular lift need
    # not do so as a vector map. This is a positive hostile against promotion.
    G2=[row[:2] for row in bad[:2]];B2=attach(G2);B3=restore(packets['coherent_indefinite']['attachment'])
    assert [row[:2] for row in B3]!=B2
    assert [row[:2] for row in bad[:2]]==G2
    instancepath=ROOT/contract['weil_source_contract'];instance=json.loads(instancepath.read_text())
    assert instance['external_source_verification_required'] is True
    missing=['independently source-derived prime/gamma/endpoint packet matrices',
             'independently source-derived zero-side packet matrices with certified tail comparison',
             'arithmetic-to-spectral shared-edge identity in the same packet conventions',
             'restriction-compatible seed attachment and a faithful completed carrier',
             'positivity for every source-admitted packet, not just a fixed finite dimension']
    files=[cp,priorpath,instancepath,Path(__file__),Path(__file__).with_name('check_proton_native_task_catalogue.py'),Path(__file__).with_name('check_proton_single_probe_cycle.py'),Path(__file__).with_name('check_proton_unitary_probe_repair.py'),Path(__file__).with_name('verify_proton_native_task_catalogue.py')]
    result={'status':'passed','verification_passed':True,'schema':'marici.voevodsky.rh-seed-signed-attachment.v1',
      'classification':'finite_signed_packet_expressibility_verified_actual_weil_attachment_and_completion_not_constructed',
      'active_obligation':contract['active_obligation'],'native_source_basis':sparse(X),'native_sink_basis':sparse(Y),
      'basis_gram':sparse(D),'formula':'B_G=X+Y D^-1 G, with Xdagger K Y=D/2; B_Gdagger K B_G=G',
      'universal_scope':'Every supplied Hermitian n-by-n G with n<=13, using the first n independent channel columns',
      'coefficient_attachment_injective':True,'packets':packets,'dimension13_attachment':sparse(B13),
      'negative_witness':vector(witness),'negative_value':vector([value]),'all_two_coordinate_principal_packets_positive':True,
      'positive_degenerate_nonzero_embedded_witness':vector(mv(Bi,v)),'faithful_linear_attachment_does_not_imply_faithful_quadratic_observation':True,
      'signed_principal_restrictions_cohere':True,'chosen_vector_lifts_are_restriction_compatible':False,
      'RH_proved':False,'actual_zeta_packet_computed':False,'independent_arithmetic_spectral_identity_verified':False,
      'weil_instance_external_verification_pending':True,'missing_source_objects':missing,'scope':contract['scope'],
      'source_hashes':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in files},'shared_sources_or_stores_modified':False}
    out=ROOT/'research/voevodsky/results/rh-seed-signed-attachment-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','universal_packet_dimension_up_to':13,'negative_value':str(value),
      'chart_triangles_commute_for_negative_packet':True,'vector_lifts_restriction_compatible':False,'actual_Weil_attachment':False,'RH_proved':False},indent=2))
if __name__=='__main__':main()
