"""Exact support for the rim continuum resolvent and analytic completeness proof."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_rim_bound_sector as bound
from check_low_energy_net_v4 import determinant

ROOT=bound.ROOT;HOME=Path(__file__).resolve().parent
PROOF=HOME/'RIM-COMPLETENESS.md'
RESULT=HOME/'results/rim-completeness.v1.json'
mm,tr,eye,add,scale=bound.mm,bound.tr,bound.eye,bound.add,bound.scale


def verify_mismatch(A,Cinv,sign=-1):
    assert add(eye(2),scale(2*sign,mm(A,Cinv)))==scale(-sign,Cinv),'wrong contact mismatch'


def build():
    point=bound.build()
    assert point==bound.load(bound.RESULT),'stale point-sector input; do not silently renew it'
    src=bound.load(ROOT/bound.SOURCE)
    full=[[Q(v) for v in row] for row in src['full_joint_H_without_mu']]
    K=[row[2:] for row in full[2:]]
    M=[[Q(v) for v in row[2:]] for row in src['source_metric'][2:]]
    B=[[v/Q(src['parameters']['g']) for v in row[:2]] for row in full[2:]]
    S=scale(Q(1,3),mm(tr(B),M));P=mm(B,S);theta=Q(1,2)
    # L(q)=L0+q L1+q^2 I+q^3 I: monic determinant of degree 72.
    constant=add(K,scale(-theta,eye(24)))
    coefficients=[constant,add(constant,scale(2,P)),eye(24),eye(24)]
    assert coefficients[3]==eye(24) and determinant(constant)!=0
    reports=[];controls=[]
    for q in (Q(1),Q(2)):
        z=theta-q*q;core=add(K,scale(-z,eye(24)));J=bound.inverse(core)
        assert mm(core,J)==mm(J,core)==eye(24)
        assert mm(M,J)==tr(mm(M,J)) and bound.inertia(mm(M,core))==(24,0,0)
        core_response=mm(mm(S,J),B)
        A=add(scale(1/(2*q),eye(2)),core_response)
        C=add(eye(2),scale(2,A));Cinv=bound.inverse(C)
        assert mm(C,Cinv)==mm(Cinv,C)==eye(2)
        assert bound.inertia(A)==bound.inertia(C)==(2,0,0)
        gamma_gram=add(scale(1/(4*q**3),eye(2)),mm(mm(mm(S,J),J),B))
        assert bound.inertia(gamma_gram)==(2,0,0)
        verify_mismatch(A,Cinv)
        core_correction=scale(2,mm(mm(J,B),Cinv))
        assert mm(core,core_correction)==scale(2,mm(B,Cinv))
        L=[[sum((coefficients[k][i][j]*q**k for k in range(4)),Q(0)) for j in range(24)] for i in range(24)]
        expected=add(scale(q+1,core),scale(2*q,P));assert L==expected
        lhs=determinant(L);rhs=q*q*(q+1)**22*determinant(core)*determinant(C)
        assert lhs==rhs and lhs!=0
        assert bound.inertia(mm(M,L))==(24,0,0)
        if q==1:
            for name in ('omit-free-Green-trace','reverse-Krein-sign','declare-entire-Hilbert-space-ac'):
                try:
                    if name=='omit-free-Green-trace':verify_mismatch(A,bound.inverse(add(eye(2),scale(2,core_response))))
                    elif name=='reverse-Krein-sign':verify_mismatch(A,Cinv,sign=1)
                    else:assert point['total_point_subspace_dimension']==0
                except AssertionError:controls.append(name)
                else:raise AssertionError('hostile accepted: '+name)
        reports.append({'q':str(q),'z':str(z),'A':bound.encode(A),'C':bound.encode(C),
            'C_inverse':bound.encode(Cinv),'Gamma_Gram':bound.encode(gamma_gram),
            'determinant_identity_verified':True,'boundary_mismatch_verified':True,'core_cancellation_verified':True})
    paths={ROOT/p for p in point['source_sha256']}
    paths.update((bound.RESULT,Path(__file__),PROOF,HOME/'test_rim_completeness.py'))
    return {'schema':'marici.scattering.rim-completeness.v1','status':'pass',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'core_dimension':24,'free_field':'L2(R,C2)','free_energy_fiber_multiplicity':4,
        'resolvent_comparison_energy':'-1/2','resolvent_difference_rank':2,
        'bounded_operator_difference_claimed':False,'finite_checks':reports,
        'secular_polynomial_determinant_degree':72,'secular_polynomial_monic':True,
        'no_singular_continuous_spectrum':True,'wave_operators_exist_and_complete_on_ac':True,
        'full_point_dimension':point['total_point_subspace_dimension'],
        'all_nonpoint_states_have_free_outgoing_asymptote':True,
        'all_central_preparations_escape':False,
        'wave_operator_theorem':'Trace-class resolvent-comparable semibounded pair; Kato-Rosenblum plus Birman invariance principle.',
        'no_sc_argument':'Dense compactly supported lead/core test vectors; meromorphic square-root boundary resolvents with finitely many exceptional energies.',
        'analytic_argument_machine_formalized':False,'source_stationary_solver_replayed':False,
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert bound.load(RESULT)==r,'stale rim completeness receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    keys=('status','resolvent_difference_rank','full_point_dimension','no_singular_continuous_spectrum',
          'wave_operators_exist_and_complete_on_ac','analytic_argument_machine_formalized','hostile_controls_refused')
    print(json.dumps({k:r[k] for k in keys}))


if __name__=='__main__':main()
