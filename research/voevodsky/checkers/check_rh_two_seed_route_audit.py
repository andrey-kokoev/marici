"""Iteration1: triangle/seam audit and same signed packet in two native seeds.
Rebuild operators, preserve neutron metric; no writes to source-owner stores.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_proton_native_task_catalogue import ROOT,ZERO,ONE,parse,eye,mzero,mm,mv,adj,madd,msub,rank,sparse,trace
from check_proton_single_probe_cycle import inverse
from check_proton_unitary_probe_repair import restore
from check_triangle_half_phase import TwoPacket,cycle_from_packets


def real(A):return [[(F(x),F(0)) for x in row] for row in A]
def diagonal(values):return [[(F(values[i]),F(0)) if i==j else ZERO for j in range(len(values))] for i in range(len(values))]
def multiply_scalar(A,q):return [[(q*x,q*y) for x,y in row] for row in A]
def blockdiag(blocks):
    sizes=[len(x) for x in blocks];out=mzero(sum(sizes),sum(sizes));offset=0
    for A,n in zip(blocks,sizes):
        for i in range(n):
            for j in range(n):out[offset+i][offset+j]=A[i][j]
        offset+=n
    return out

def columns(A,indices):return [[row[j] for j in indices] for row in A]
def rounded(values,digits):
    den=10**digits
    return [[(F(round(F(x)*den),den),F(0)) for x in row] for row in values]
def build(name,operators,metric):
    L,G,N=operators;n=len(L);M=diagonal(metric)
    for A in (L,G,N):assert mm(A,A)==A and mm(adj(A),M)==mm(M,A)
    assert mm(L,G)==mm(G,L)==N
    A,B=msub(L,N),msub(G,N);assert mm(A,B)==mm(B,A)==mzero(n,n)
    W=mzero(3*n,3*n);T=mzero(3*n,3*n)
    for i in range(n):
        for j in range(n):
            W[n+i][j]=L[i][j];W[2*n+i][n+j]=G[i][j];W[i][2*n+j]=N[i][j]
            T[n+i][j]=A[i][j];T[2*n+i][n+j]=B[i][j]
    Ms=blockdiag([M]*3)
    # Hermitian FORM is Ms K=(Ms W+Wdagger Ms)/2; avoids pretending
    # neutron numerator coordinates have Euclidean metric.
    H=multiply_scalar(madd(mm(Ms,W),mm(adj(W),Ms)),F(1,2))
    assert H==adj(H)
    Ps=blockdiag([A,B,mzero(n,n)])
    selected=[]
    for j in range(3*n):
        if rank(columns(Ps,selected+[j]))>len(selected):selected.append(j)
        if len(selected)==3:break
    X=columns(Ps,selected);Y=mm(T,X);D=mm(mm(adj(X),Ms),X)
    assert rank(X)==rank(Y)==3 and mm(mm(adj(Y),Ms),Y)==D
    assert mm(mm(adj(X),Ms),Y)==mzero(3,3)
    assert mm(mm(adj(X),H),X)==mm(mm(adj(Y),H),Y)==mzero(3,3)
    assert mm(mm(adj(X),H),Y)==multiply_scalar(D,F(1,2))
    assert mm(W,X)==Y and mm(W,Y)==mzero(3*n,3)
    decoder=mm(mm(inverse(D),adj(X)),Ms)
    def attach(Gpacket):
        attached=madd(X,mm(mm(Y,inverse(D)),Gpacket))
        assert rank(attached)==3 and mm(mm(adj(attached),H),attached)==Gpacket
        assert mm(decoder,attached)==eye(3)
        return attached
    ranks=[int(trace(op)[0]) for op in (L,G,N)]
    assert all(trace(op)[1]==0 and trace(op)[0].denominator==1 for op in (L,G,N))
    return {'name':name,'operators':operators,'W':W,'H':H,'Ms':Ms,'X':X,'Y':Y,'D':D,'selected':selected,'ranks':ranks,'decoder':decoder,'attach':attach}


def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/rh-two-seed-route-audit-v1.json';c=json.loads(cp.read_text())
    files={k:ROOT/c[k] for k in ('proton','neutron','packet','certification','weil_source')}
    _,pop=parse(json.loads(files['proton'].read_text()));proton=build('protonlike',pop,[F(1)]*36)
    ns=json.loads(files['neutron'].read_text());d=[F(x['d']) for x in ns['coordinates']];assert len(d)==36 and all(x>0 for x in d)
    nop=[mzero(36,36) for _ in range(3)]
    for arrow in ns['arrows']:
        a,b,im,jm=map(F,arrow['numerator']);assert b==jm==0
        i,j=arrow['target'],arrow['source'];stage='LGN'.index(arrow['stage'])
        # u_i are numerator coordinates, physical u_i/sqrt(d_i).
        # Their metric is1/d_i; operator numerator_ij/d_source.
        nop[stage][i][j]=(a/d[j],im/d[j])
    neutron=build('neutron',nop,[1/x for x in d])
    assert proton['ranks']==[12,3,1] and neutron['ranks']==[3,12,1]
    packet=json.loads(files['packet'].read_text());cert=json.loads(files['certification'].read_text())
    assert packet['status']==cert['status']=='passed'
    G=restore(packet['rounded_packet']);scout=packet['calculations'][-1]
    assert rounded(scout['arithmetic_packet'],packet['parameters']['rounding_decimal_places'])==G
    Z=rounded(scout['finite_zero_packet'],packet['parameters']['rounding_decimal_places'])
    assert Z==G # equality ONLY after30-place rounding, not analytic identity.
    bad=real([[1,F(-3,5),F(-3,5)],[F(-3,5),1,F(-3,5)],[F(-3,5),F(-3,5),1]])
    forms={'rounded_arithmetic':G,'rounded_16_zero_scout':Z,'signed_hostile_not_a_Weil_packet':bad}
    stored={};transport={}
    for name,form in forms.items():
        bp=proton['attach'](form);bn=neutron['attach'](form)
        J=mm(bn,proton['decoder']);assert mm(J,bp)==bn
        assert mm(mm(adj(mm(J,bp)),neutron['H']),mm(J,bp))==form
        left=mm(J,mm(proton['W'],bp));right=mm(neutron['W'],mm(J,bp))
        assert left==mzero(108,3) and right==neutron['Y'] and left!=right
        stored[name]={'form':sparse(form),'proton_attachment':sparse(bp),'neutron_attachment':sparse(bn)}
        transport[name]={'map':sparse(J),'packet_intertwining':True,'signed_form_preserved_on_packet':True,
                         'native_W_intertwining':False,'native_intertwining_defect':sparse(msub(left,right)),
                         'this_decoder_map_failure_is_a_no_go_for_every_possible_map':False}
    witness=real([[1],[1],[1]])
    assert mm(mm(adj(witness),bad),witness)==[[(F(-3,5),F(0))]]
    # Source primitives compute a cyclic permutation, not prime/gamma/zero
    # evaluation. Test the actual oriented seam and its independent failure.
    left_packets=tuple(TwoPacket(label,a,b) for label,a,b in (('AB','A','B'),('BC','B','C'),('CA','C','A')))
    right_packets=tuple(TwoPacket(label,a,b) for label,a,b in (('BA','B','A'),('AD','A','D'),('DB','D','B')))
    C=cycle_from_packets(left_packets);assert cycle_from_packets(right_packets)==C
    R1=real([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0]])
    R2=real([[-1,0,0,0,0],[0,0,0,1,0],[0,0,0,0,1]])
    Cr=real(C);x=real([[0],[1],[0],[0],[0]])
    assert mm(mm(Cr,R1),x)[0][0]==ONE and mm(mm(Cr,R2),x)[0][0]==ZERO
    mirror=real([[1,0,0],[0,1,0],[0,0,1],[0,-1,0],[0,0,-1]])
    assert mm(R1,mirror)==eye(3) and mm(R2,mirror)==multiply_scalar(eye(3),-1)
    # Spectral hostile: off-line quartet u=+-20pi+-i/4, t=1/10.
    # Half-divisor Gaussian sum=-2 exp[-t((20pi)^2-1/16)]<0.
    # Replacing u by real ordinates gives+2exp[-t(20pi)^2]>0.
    # This is a hypothetical divisor, not a claim about actual zeta zeros.
    assert 2*F(1,10)*F(20)*F(1,4)==1 # cosine angle pi, hence sign-1.
    assert cert['analytic_arithmetic_packet_positive_definite'] is True
    assert cert['zero_side_exhaustion_certified'] is False and cert['seed_face_operation_attachment_constructed'] is False
    result={'schema':'marici.rh-two-seed-route-audit.v1','passed':True,'iteration':1,
      'actual_seed_triangles':{'left_occurrences':c['source_roles']['left_seed_cycle'],'right_occurrences':c['source_roles']['right_seed_cycle'],
        'local_cycle_matrix':[[str(x) for x in row] for row in C],'restrictions':[sparse(R1),sparse(R2)],
        'local_cycle_executes_arithmetic_or_zeros':False,'seam':'BA=-AB on one oriented cochain; two occurrences retained',
        'independent_cycle_seam_counterexample':{'input':['0','1','0','0','0'],'left_proposed_AB':'1','right_proposed_AB':'0'},
        'mirror_compatible_carrier':sparse(mirror)},
      'intended_RH_routes':c['target_RH_roles'],
      'native_metrics':{'proton':[str(x) for x in [F(1)]*36],'neutron':[str(1/x) for x in d]},
      'native_ranks':{'proton':proton['ranks'],'neutron':neutron['ranks']},
      'native_packet_channels':{s['name']:{'selected_source_columns':s['selected'],'source':sparse(s['X']),'sink':sparse(s['Y']),'gram':sparse(s['D'])} for s in (proton,neutron)},
      'same_signed_packets_in_both_carriers':stored,'packet_transport_tests':transport,
      'stage_preserving_unitary_native_W_equivalence_possible':False,
      'rank_obstruction':'An invertible stage-preserving intertwiner would require rank Lp=rank Ln, but12!=3; full unsigned/mixed-stage equivalence is a different question.',
      'hypothetical_offcritical_divisor_control':{'u':'+-20pi+-i/4','t':'1/10','full_half_divisor_value':'-2 exp[-((20pi)^2-1/16)/10]<0',
         'real_ordinate_substitution':'2 exp[-(20pi)^2/10]>0','actual_zeta_zeros_asserted':False},
      'rounded_arithmetic_equals_rounded_scout':True,'analytic_arithmetic_packet_certified_positive':True,
      'full_zero_divisor_certified':False,'external_Weil_normalization_verified':cert['external_explicit_formula_authority_verified'],
      'arithmetic_and_spectral_operations_realized_on_actual_faces':False,'same_RH_comparison_survives_as_native_processing_in_both':False,
      'last_flag_means_not_established_not_impossibility_of_every_enlarged_adapter':True,
      'next_nonredundant_obligation':'Construct source-labelled endpoint/gamma/prime/zero operations and a retained seam carrier, then test actual six occurrence histories in each native address/metric/frame, not just Bdagger H B.',
      'RH_proved':False,'shared_sources_modified':False,'scope':c['scope']}
    bound=[cp,*files.values(),Path(__file__),Path(__file__).with_name('check_proton_native_task_catalogue.py'),ROOT/'research/nima/checkers/check_triangle_half_phase.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in bound}
    out=base/'results/rh-two-seed-route-audit-v1.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'same_finite_signed_packet_in_both':True,'native_stage_ranks':result['native_ranks'],
      'packet_decoder_transports_native_processing':False,'actual_RH_faces_constructed':False,'offcritical_control_preserves_negative_sign':True},indent=2))
if __name__=='__main__':main()
