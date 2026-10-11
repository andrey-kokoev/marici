"""Symmetric bridge port and a conditional vacuum stability test.

Source fixes port overlaps/response. A neutral reference level and exchange
coupling are explicit test inputs, not a derived particle-creation interaction.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
from check_belt_interface_response import inverse, mm

BASE=Path(__file__).resolve().parents[1]


def main():
    path=BASE/'results/collective_carrier_spectrum.json'
    raw=path.read_bytes();source=json.loads(raw)
    K=[[F(x) for x in row] for row in source['belt_reduced_matrix']]
    even=[[K[i][j]+K[i][j+3] for j in range(3)] for i in range(3)]
    roots=list(map(F,source['belt_face_even_energies_exact']))
    I=[[F(i==j) for j in range(3)] for i in range(3)]
    projectors=[];weights=[]
    for root in roots:
        P=[row[:] for row in I]
        for other in roots:
            if root!=other:
                factor=[[(even[i][j]-other*int(i==j))/(root-other) for j in range(3)] for i in range(3)]
                P=mm(P,factor)
        assert mm(P,P)==P
        assert mm(even,P)==[[root*x for x in row] for row in P]
        projectors.append(P);weights.append(P[0][0])
    assert weights==[F(1193,4485),F(2099,8970),F(1,2)]
    assert sum(weights)==1 and all(w>0 for w in weights)
    assert all(sum(P[i][j] for P in projectors)==I[i][j] for i in range(3) for j in range(3))
    def response(mu):
        assert mu>0
        return sum(w/(root+mu) for root,w in zip(roots,weights))
    for mu in (F(1),F(1,2),F(1,7)):
        shifted=[[even[i][j]+mu*int(i==j) for j in range(3)] for i in range(3)]
        assert inverse(shifted)[0][0]==response(mu)
    # Source symmetric contact does not act entirely inside the coherent line:
    # its squared overlap is r0 and its leakage weight is 1-r0.
    r0=weights[0]
    leakage=r0*(1-r0)
    assert leakage>0
    trials=[]
    for epsilon,g in ((F(1),F(1,10)),(F(1),F(1,2)),(F(1),F(1))):
        # In the one-excitation exchange block, a coherent carrier trial plus
        # reference amplitude -g*sqrt(r0)/epsilon has this negative quotient.
        rayleigh=-g*g*r0*epsilon/(epsilon*epsilon+g*g*r0)
        assert rayleigh<0
        # For a supplied common carrier offset mu>0, Schur positivity is
        # exactly epsilon >= g^2 S_plus(-mu). S is strictly decreasing from
        # infinity to zero, giving a unique threshold (not a selected mass).
        lo=F(0);hi=F(1)
        while g*g*response(hi)>epsilon:hi*=2
        for _ in range(70):
            mid=(lo+hi)/2
            if g*g*response(mid)>epsilon:lo=mid
            else:hi=mid
        assert lo>0 and g*g*response(lo)>epsilon>=g*g*response(hi)
        trials.append({'reference_gap':str(epsilon),'exchange_strength':str(g),
                       'negative_rayleigh_quotient_at_zero_carrier_offset':str(rayleigh),
                       'offset_threshold_interval':[str(lo),str(hi)],
                       'offset_threshold_decimal':float((lo+hi)/2),
                       'threshold_meaning':'Zero eigenvalue of the coupled excitation block; above it the block is positive, below it the putative empty vacuum is not a ground state.'})
    report={
        'verification_passed':True,
        'port':'unit symmetric combination of bridge-endpoint modes 0 and 3; use the C3-aligned contact',
        'new_internal_tensor_factors':0,
        'even_mode_energies':list(map(str,roots)),
        'spectral_weights':list(map(str,weights)),
        'coherent_mode_overlap_squared':str(r0),
        'contact_density_leakage_norm_squared_on_coherent_mode':str(leakage),
        'response':'S_plus(z)=sum_j r_j/(lambda_j-z)',
        'coherent_zero_pole_residue':str(r0),
        'reference_coupling':'One-excitation block [[epsilon,g<w|],[g|w>,K+mu I]], with an empty zero-excitation reference vacuum of energy zero. This neutral exchange law is supplied.',
        'zero_offset_vacuum_stable':False,
        'stability_condition':'mu>0 and epsilon>=g^2*S_plus(-mu), for epsilon>0 and g!=0',
        'threshold_is_positive_rest_mass':False,
        'threshold_note':'At equality the excitation gap is zero, so selecting marginal stability does not derive a nonzero mass.',
        'trials_are_not_mass_fits':True,'illustrative_trials':trials,
        'prior_reused':['photon-source-emission.md: distinguish the empty vacuum from an excitation-transfer block and retain source energy inputs','mass-gap-symmetry-and-protected-kernel.md: offsets are not fixed by internal symmetry','belt-interface-response-and-prior-audit.md: source-specific resolvent and retained coordinates'],
        'scope':'The source supplies an occupation-sensitive port and its response. It does not supply the reference field, charge law, coupling, positive offset or physical vacuum identification.',
        'source_sha256':sha256(raw).hexdigest()}
    (BASE/'results/belt_coherent_port_vacuum.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
