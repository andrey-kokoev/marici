"""Neutral seam-register dressing of the constructed belt return.

Exact local spectral certificates and actual noncommuting seam-projector checks
prove the many-register ground state without enumerating 36*2^21 dimensions.
The coupling law is explicit new model input; it is not a fitted neutron mass.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from check_constraint_energy_accounting import identity, plus, times, compose, adjoint, trace
from check_coupled_six_piece_belt import ONE
from check_belt_three_by_twelve import decode
from check_pentachoron_spin_interfaces import A, S2, S5, I, add, scale, mm, adj

BASE = Path(__file__).resolve().parents[1]


def matrix(entries):
    return {(i,j):decode(v) for i,j,v in entries}


def local_certificate(epsilon,J,g,rplus,rminus):
    # Inactive interface or vacuum: S=0. Matched occupied carrier: S=1.
    # n=diag(0,1), h(S)=epsilon*n+J*(n-S)^2-g*X.
    inactive = ((A(0),A(-g)),(A(-g),A(epsilon+J)))
    matched = ((A(J),A(-g)),(A(-g),A(epsilon)))
    assert rplus*rplus == A((epsilon+J)**2+4*g*g)
    assert rminus*rminus == A((J-epsilon)**2+4*g*g)
    ev = (A(epsilon+J)-rplus)/2
    eb = (A(epsilon+J)-rminus)/2
    delta = eb-ev
    assert delta*(rplus+rminus)==A(2*epsilon*J)
    projections = []
    for H,low,gap in ((inactive,ev,rplus),(matched,eb,rminus)):
        P = scale(gap.inverse(),add(scale(low+gap,I),scale(A(-1),H)))
        assert adj(P)==P and mm(P,P)==P and P[0][0]+P[1][1]==1
        assert mm(H,P)==scale(low,P)
        assert add(H,scale(-low,I))==scale(gap,add(I,scale(A(-1),P)))
        projections.append(P)
    return {'inactive_ground':ev,'matched_ground':eb,'relative_seam_energy':delta,
            'inactive_occupation':projections[0][1][1],'matched_occupation':projections[1][1][1]}


def main():
    path = BASE/'results/native_operation_energy_lift_store.json'
    raw = path.read_bytes()
    store = json.loads(raw)
    belt = store['carriers']['belt']
    metric = tuple(map(F,belt['metric_denominators']))
    N = matrix(belt['return_entries'])
    native = matrix(belt['native_energy_entries'])
    full = matrix(belt['entries'])
    seams = [(tuple(row['triangles']),matrix(row['entries'])) for row in belt['seam_projectors']]
    assert len(seams)==21 and trace(N,36)==1 and compose(N,N)==N
    assert compose(native,N)=={}
    assert plus(native,*(times(4,p) for _,p in seams))==full
    for _,p in seams:
        assert trace(p,36)==1 and compose(p,p)==p and adjoint(p,metric)==p
        assert compose(p,N)=={}
    assert compose(seams[0][1],seams[1][1]) != compose(seams[1][1],seams[0][1])
    # Native sector rotation carries the seam projectors and their neutral
    # register labels together; identical register parameters preserve C3.
    rotation = {(((s+1)%3)*12+j,s*12+j):ONE for s in range(3) for j in range(12)}
    inverse = adjoint(rotation,metric)
    by_edge = dict(seams)
    for (a,b),p in seams:
        image = tuple(sorted(((a+6)%18,(b+6)%18)))
        assert compose(compose(rotation,p),inverse)==by_edge[image]
    assert compose(compose(rotation,N),inverse)==N
    assert compose(compose(rotation,native),inverse)==native
    assert store['carriers']['proton']['seam_projectors']==[]

    epsilon,J,kappa = F(1,4),F(1,2),F(1)
    # Square roots all lie in the already implemented exact number field.
    trials = [(F(0),A(F(3,4)),A(F(1,4))),
              (F(1,8),S2*S5/4,S2/4),
              (F(3,8),3*S2/4,S2*S5/4)]
    outputs = []
    for g,rplus,rminus in trials:
        certificate = local_certificate(epsilon,J,g,rplus,rminus)
        # For J>epsilon>0 and nonnegative g, the positive roots satisfy
        # rplus>=J+epsilon, rminus>=J-epsilon, hence 0<delta<=epsilon<kappa.
        assert epsilon>0 and J>epsilon and kappa>epsilon
        if g==0:
            assert certificate['relative_seam_energy']==A(epsilon)
            assert certificate['inactive_occupation']==A(0)
            assert certificate['matched_occupation']==A(1)
        # Per-edge ground bound on a carrier mismatch eigenvalue p=0 or 1:
        # p=0 has minimum eb; p=1 has minimum kappa+ev > eb.
        delta = certificate['relative_seam_energy']
        assert (A(kappa)+certificate['inactive_ground']-certificate['matched_ground']) == A(kappa)-delta
        outputs.append({'epsilon':str(epsilon),'J':str(J),'kappa':str(kappa),'g':str(g),
                        **{key:value.record() for key,value in certificate.items()},
                        'twenty_one_seam_increment':(21*delta).record()})
    # A defect-only occupation rule does not dress the matched state: when
    # its control is P_e, all seam controls vanish on N.
    assert all(compose(p,N)=={} for _,p in seams)
    report = {
        'verification_passed':True,
        'source_seams':21,'source_seam_projectors_commute':False,
        'native_rotation_covariance':True,
        'coupling':'epsilon*n_e + J*(n_e-S_e)^2 - g*X_e; S_e=c-P_e with P_e extended by zero in the vacuum',
        'carrier_energy':'H_native + kappa*sum P_e inside c=1; vacuum c=0 has no carrier defects',
        'scope':'Constructed neutral-register Hamiltonian with a supplied conserved carrier sector, shared record parameters and vacuum subtraction; no physical mass calibration.',
        'ground_carrier_return':'N, unchanged by record mixing when kappa>delta',
        'relative_energy_per_seam':'delta=[sqrt((J+epsilon)^2+4g^2)-sqrt((J-epsilon)^2+4g^2)]/2',
        'sufficient_ground_condition':'J>epsilon>0, kappa>epsilon, g>=0; then 0<delta<=epsilon<kappa',
        'zero_mixing_occupied_seams':21,
        'positive_mixing_occupations':'Coherent partial occupation, computed from the exact two-level ground projector',
        'intrinsic_increment':'21*delta relative to the inactive-register ground and equal bare carrier baselines',
        'defect_control_rule_increment_on_N':'0; P_e N=0, so defect-only records remain in their inactive state',
        'radical_basis':'coefficient masks: sqrt(2), sqrt(3), sqrt(5), i',
        'exact_trials':outputs,
        'physical_neutron_mass_predicted':False,
        'next_gate':'Identify the satisfied-interface coupling and the elementary record gap in the source; compare its vacuum-subtracted spectrum and responses with the other particle sectors.',
        'source_sha256':sha256(raw).hexdigest()
    }
    (BASE/'results/seam_occupation_energy.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
