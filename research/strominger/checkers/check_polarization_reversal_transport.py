#!/usr/bin/env python3
"""Metric-induced left/right reversal on the existing photon-like seed plane."""
from pathlib import Path
import hashlib
import json
import sympy as sp
ROOT=Path(__file__).resolve().parents[3]

def serialize(M):return [[str(sp.simplify(x)) for x in row] for row in M.tolist()]
def main():
    promotion_path=ROOT/'research/strominger/results/two_output_comparison_promotion.json'
    independence_path=ROOT/'research/strominger/results/two_output_cut_independence.json'
    promotion=json.loads(promotion_path.read_text());independence=json.loads(independence_path.read_text())
    base=promotion['example']
    U=sp.Matrix([[1,0],[-1,0],[sp.Rational(1,2),sp.Rational(1,2)],[-1,0],[1,0],[-sp.Rational(1,2),-sp.Rational(1,2)]])
    G=sp.diag(3,1);D=sp.diag(sp.sqrt(3),1)
    xp=sp.Matrix([1,sp.I*sp.sqrt(3)]);xm=sp.conjugate(xp)
    reports=[];checks={}
    for number,entry in enumerate(independence['results']):
        target=next(a for a in promotion['attempts'] if a['meeting_labels']==entry['meeting_labels'] and a['rule']==entry['rule'])
        witness=entry['equivalence'];reverse=witness['reverse_all_arrows_and_exchange_owners']
        for i,j in enumerate(witness['output_permutation']):
            K=sp.Matrix(base['outputs'][i]['continuation_matrix']);L=sp.Matrix(target['outputs'][j]['continuation_matrix'])
            J=sp.zeros(6)
            for col,row in enumerate(witness['occurrence_permutations'][i]):J[row,col]=1
            T=(U.T*U).inv()*U.T*K*U
            P=(K**2+2*K**3-K**5)/2
            # Counting pairing fixes the dual embedding V. The known plane metric
            # G makes W=V G its Riesz map, without selecting new output vectors.
            V=P.T*U*(U.T*U).inv();W=V*G
            lift=W if reverse else U
            raw=J*lift
            M=(U.T*U).inv()*U.T*raw
            pullback=sp.simplify(M.T*G*M)
            c=sp.simplify(pullback[0,0]/G[0,0])
            assert c>0 and pullback==c*G
            R=sp.simplify(M/sp.sqrt(c));Jones=sp.simplify(D*R*D.inv())
            prefix=f'{number}_{i}'
            checks[prefix+'_spectral_projector']=P*P==P and P.rank()==2 and K*P==P*K
            checks[prefix+'_dual_pairing']=V.T*U==sp.eye(2) and W.T*U==G
            checks[prefix+'_left_inverse_phase']=K.T*W==W*T.inv()
            checks[prefix+'_target_plane_exact']=sp.simplify(raw-U*M)==sp.zeros(6,2)
            checks[prefix+'_normalized_metric_isometry']=sp.simplify(R.H*G*R)==G
            expected=T.inv() if reverse else T
            checks[prefix+'_phase_intertwining']=sp.simplify(L*U*R-U*R*expected)==sp.zeros(6,2)
            checks[prefix+'_involution']=sp.simplify(R*R)==sp.eye(2)
            if reverse:
                checks[prefix+'_circular_swap']=sp.simplify(R*xp+sp.I*xm)==sp.zeros(2,1) and sp.simplify(R*xm-sp.I*xp)==sp.zeros(2,1)
            else:checks[prefix+'_same_polarization']=R==sp.eye(2)
            reports.append({'meeting_labels':entry['meeting_labels'],'rule':entry['rule'],'source_output':i,'target_output':j,'reverse':reverse,'raw_coordinate_map':serialize(M),'raw_metric_scale':str(c),'positive_normalization':str(1/sp.sqrt(c)),'normalized_coordinate_map':serialize(R),'jones_map':serialize(Jones),'phase_map':'omega <-> conjugate(omega)' if reverse else 'unchanged','source_projector':serialize(P),'dual_embedding':serialize(V),'riesz_embedding':serialize(W)})
    reversal=next(r for r in reports if r['reverse'])
    J=sp.Matrix([[0,-1],[-1,0]])
    qr,qi,pr,pi=sp.symbols('qr qi pr pi',real=True)
    q=qr+sp.I*qi;p=pr+sp.I*pi
    def stokes(q,p):return sp.Matrix([sp.expand_complex(sp.conjugate(q)*q+sp.conjugate(p)*p),sp.expand_complex(sp.conjugate(q)*q-sp.conjugate(p)*p),2*sp.re(sp.conjugate(q)*p),2*sp.im(sp.conjugate(q)*p)])
    S=stokes(q,p);after=stokes(-p,-q)
    checks['arbitrary_complex_polarization_stokes']=sp.simplify(after-sp.diag(1,-1,1,-1)*S)==sp.zeros(4,1)
    checks['twenty_output_maps_checked']=len(reports)==20
    checks['positive_metric_normalization_not_fitted']=all(r['raw_metric_scale']==('3' if r['reverse'] else '1') for r in reports)
    out={'schema':'marici.strominger.polarization-reversal-transport.v1','status':'passed' if all(checks.values()) else 'failed','scientific_disposition':'metric-induced seed polarization reversal swaps circular modes and preserves every polarization superposition norm','mode_plane':{'embedding':serialize(U),'metric':serialize(G),'spectral_projector_formula':'P=(K^2+2K^3-K^5)/2','dual_formula':'V=P^T U (U^T U)^-1','riesz_formula':'W=V G','duality':'V^T U=I; W^T U=G; K^T W=W T^-1'},'reversal':{'coordinate_map':reversal['normalized_coordinate_map'],'orthonormal_frame':'q=sqrt(3)a, p=b','jones_map':reversal['jones_map'],'circular_basis':'x_plus=(1,i sqrt(3)), x_minus=(1,-i sqrt(3))','circular_action':'x_plus -> -i x_minus; x_minus -> i x_plus','stokes_convention':'S=(|q|^2+|p|^2, |q|^2-|p|^2, 2 Re(conj(q)p), 2 Im(conj(q)p))','stokes_action':['S0','-S1','S2','-S3'],'two_reversals':'identity'},'normalization':{'raw_riesz_map':'M=[[0,-1],[-3,0]]','raw_pullback_metric':'M^T G M=3G','normalized_map':'R=M/sqrt(3)','meaning':'The positive factor is fixed by the existing source/target mode metric. Raw occurrence permutation alone is not this transport; the retained Riesz identification is essential.'},'checks':checks,'check_count':len(checks),'maps':reports,'scope':'Exact polarization of the previously constructed two-dimensional seed mode plane; the new result is its mode transport, not a spacetime dynamics or emission rate calculation.','source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),promotion_path,independence_path,ROOT/'research/nima/results/photon-two-packet-candidate.json']}}
    (ROOT/'research/strominger/results/polarization_reversal_transport.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'check_count':len(checks),'reversal':out['reversal'],'normalization':out['normalization']},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
