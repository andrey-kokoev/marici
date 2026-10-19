"""Attach the full source two-rim response to the existing internal-channel law.

Two retained same-particle auxiliaries, identical Delta and g. Full 24D source
neutron/bank sector is retained. No fitted gap or physical unit is selected.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from check_neutron_canonical_occupied_closure import ROOT,eye,mm,transpose,difference,inverse,scale,columns,encoded
from check_neutron_charge_completed_rest_gap import psd_rank
from check_collective_carrier_spectrum import characteristic
from check_recovered_neutron_rim_spectra import gcd,divmod_poly


def polynomial_product(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def evaluate(a,x):
    out=F(0)
    for c in reversed(a):out=out*x+c
    return out


def main():
    paths={k:ROOT/p for k,p in {
        'rim':'research/strominger/results/recovered-neutron-rim-spectra.json',
        'source':'research/strominger/results/neutron-seam-control-transport.json',
        'prior':'research/voevodsky/charge-compatible-internal-contact.md'}.items()}
    data={k:json.loads(p.read_text()) for k,p in paths.items() if k!='prior'};checks={}
    for obj in data.values():
        assert obj['status']=='passed'
        for p,h in obj['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    src=data['source'];rim=data['rim'];checks['fresh_source_and_rim_receipts']=True
    M=[list(map(F,r)) for r in src['metric']]
    K=scale(F(1,4),[list(map(F,r)) for r in src['native_energy']])
    for s in src['seam_controls']:
        P=[list(map(F,r)) for r in s['projector']]
        K=[[x+y for x,y in zip(r,t)] for r,t in zip(K,P)]
    assert psd_rank(mm(M,K))==17
    # Retain actual lower/upper C3 collective rim modes. Their raw coefficients
    # are ones on three triangles, each of norm one in the existing chart.
    groups=([1,7,13],[4,10,16])
    W=[[F(i in group) for group in groups] for i in range(24)]
    T=scale(F(1,3),mm(transpose(W),M))
    assert mm(T,W)==eye(2)
    assert mm(mm(transpose(W),M),W)==scale(3,eye(2))
    Delta=g=F(1,2) # Prior common internal-channel comparison fixture.
    H=[[(Delta if i==j else F(0)) for j in range(2)]+[g*x for x in T[i]] for i in range(2)]
    H += [[g*x for x in W[i]]+K[i] for i in range(24)]
    metric=[r+[F(0)]*24 for r in scale(3,eye(2))]+[[F(0)]*2+r for r in M]
    assert mm(transpose(H),metric)==mm(metric,H)
    checks['two_normalized_rim_contacts_and_full_26D_metric_hermiticity']=True
    # Exact aligned-sector embedding: 2 auxiliaries + 6 repeated triangle
    # coefficients. No bank or unaligned native coordinate is deleted from H.
    B=[[F(i==j) for j in range(8)] for i in range(2)]
    B += [[F(0)]*2+[F(i%6==j) for j in range(6)] for i in range(18)]
    B += [[F(0)]*8 for _ in range(6)]
    reduced_metric=mm(mm(transpose(B),metric),B)
    left=mm(mm(inverse(reduced_metric),transpose(B)),metric)
    small=mm(mm(left,H),B)
    assert mm(H,B)==mm(B,small)
    reducedK=[r[2:] for r in small[2:]]
    checks['full_source_retained_with_exact_8D_contact_reduction']=True
    even=([F(2099,3292),F(1)],[F(0),F(4485,3292),F(1)])
    odd=([F(23644249,10837264),F(5391,1646),F(1)],
         [F(6431463,10837264),F(44361887,10837264),F(4),F(1)])
    # Verify the rational functions algebraically, not just at sample x.
    swap=[[F(j==(i+3)%6) for j in range(6)] for i in range(6)]
    assert mm(swap,reducedK)==mm(reducedK,swap)
    for sign,pair in ((1,even),(-1,odd)):
        Ablock=[[reducedK[i][j]+sign*reducedK[i][j+3] for j in range(3)] for i in range(3)]
        den=characteristic(Ablock)
        num=[-x for x in characteristic([[Ablock[i][j] for j in (0,2)] for i in (0,2)])]
        common=gcd(num,den);num,rem=divmod_poly(num,common);assert rem==[0]
        den,rem=divmod_poly(den,common);assert rem==[0]
        # Convert R(z) to R(-x), both in ascending coefficients.
        xn=[v*(-1)**i for i,v in enumerate(reversed(num))]
        xd=[v*(-1)**i for i,v in enumerate(reversed(den))]
        assert polynomial_product(xn,pair[1])==polynomial_product(pair[0],xd)
    checks['full_rational_response_identities_verified_algebraically']=True
    def response(pair,x):return evaluate(pair[0],x)/evaluate(pair[1],x)
    samples=[]
    for x in (F(1,10),F(1),F(3)):
        shifted=[[a+F(i==j)*x for j,a in enumerate(r)] for i,r in enumerate(reducedK)]
        inv=inverse(shifted);R=[[inv[i][j] for j in (1,4)] for i in (1,4)]
        re,ro=response(even,x),response(odd,x)
        assert R==[[(re+ro)/2,(re-ro)/2],[(re-ro)/2,(re+ro)/2]]
        assert R[0][1]>0
        # Exact full-H Schur complement, not a pole-only approximation.
        Hx=[[a+F(i==j)*x for j,a in enumerate(r)] for i,r in enumerate(H)]
        lower=[r[2:] for r in Hx[2:]]
        schur=difference([r[:2] for r in Hx[:2]],mm(mm([r[2:] for r in Hx[:2]],inverse(lower)),[r[:2] for r in Hx[2:]]))
        assert schur==difference(scale(Delta+x,eye(2)),scale(g*g,R))
        samples.append({'x':str(x),'rim_response':encoded(R),'self_energy':encoded(scale(g*g,R))})
    checks['full_two_port_self_energy_matches_all_recovered_response_poles']=True
    # R_even(x)>R_odd(x) for all x>0, certified by positive coefficients of
    # the cross-multiplied numerator and positive denominator coefficients.
    lhs=polynomial_product(even[0],odd[1]);rhs=polynomial_product(odd[0],even[1])
    numerator=[a-b for a,b in zip(lhs,rhs)]
    assert all(c>=0 for c in numerator) and any(c>0 for c in numerator)
    checks['interport_coupling_nonzero_and_even_response_strictly_larger']=True
    brackets={}
    for name,pair in [('even',even),('odd',odd)]:
        def secular(x):return (Delta+x)*evaluate(pair[1],x)-g*g*evaluate(pair[0],x)
        lo=F(0);hi=F(1);assert secular(lo)<0<secular(hi)
        # Response is a positive spectral measure resolvent for x>0, hence
        # strictly decreasing; Delta+x increases. Each positive root is unique.
        for _ in range(65):
            mid=(lo+hi)/2
            if secular(mid)<0:lo=mid
            else:hi=mid
        assert secular(lo)<0<secular(hi)
        brackets[name]=(lo,hi)
    assert brackets['even'][0]>brackets['odd'][1]
    # Full-matrix lower-bound certification includes all unobserved directions.
    hi=brackets['even'][1]
    shifted=[[a+F(i==j)*hi for j,a in enumerate(r)] for i,r in enumerate(H)]
    assert psd_rank(mm(metric,shifted))==26
    checks['ground_shift_bracket_and_full_26D_positive_definite_bound']=True
    thresholds=Delta/response(odd,F(0));assert g*g>thresholds
    # Reuse the original illustrative baseline, explicitly not a selected mass.
    mu=F(1,4);assert mu>brackets['even'][1]
    reports={name:{'shift_lower':str(lo),'shift_upper':str(hi),'shift_approximate':float((lo+hi)/2),
                   'energy_lower_at_mu_quarter':str(mu-hi),'energy_upper_at_mu_quarter':str(mu-lo),
                   'energy_approximate_at_mu_quarter':float(mu-(lo+hi)/2)} for name,(lo,hi) in brackets.items()}
    result={'status':'passed','checks':checks,'source_metric':encoded(metric),'full_joint_H_without_mu':encoded(H),
            'retained_complex_dimension':26,'two_auxiliary_metric':'3 I2; their normalized profiles are the actual collective lower/upper rim modes',
            'aligned_embedding':encoded(B),'aligned_joint_H':encoded(small),'aligned_metric':encoded(reduced_metric),
            'law':'H=mu I+[[Delta I2,g T],[g W,K]], with all bank and native spectators retained.',
            'contact_rule_scope':'Two-channel extension of the prior internal-channel law at the actual source rim ports; equal Delta,g and the attachment itself remain explicit constructor inputs.',
            'parameters':{'Delta':str(Delta),'g':str(g),'illustrative_mu':str(mu)},
            'source_operator_unit':'K=H_native/4+sum seam projectors, as fixed in the recovered collective-response checker.',
            'response_samples':samples,'response_difference_numerator_ascending':list(map(str,numerator)),
            'conditional_dressed_energies':reports,'odd_negative_state_condition':'g^2>Delta/R_odd(0)',
            'odd_threshold_g_squared':str(thresholds),
            'common_vacuum':'Separate zero-energy empty sector; auxiliary channels have the same declared particle label as the neutron/bank sector.',
            'interpretation':'Full response matching succeeds without replacing the odd channel by a two-state register. The shifts are conditional dressing energies, not source-selected neutron rest energies; mu, Delta, g and physical units remain inputs.'}
    inputs=list(paths.values())+[Path(__file__).resolve(),ROOT/'research/strominger/checkers/check_neutron_charge_completed_rest_gap.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    out=ROOT/'research/strominger/results/neutron-two-rim-contact-binding.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'retained_complex_dimension':26,'matched_response':'full 2x2, nonzero off-diagonal',
                      'parameters':result['parameters'],'conditional_dressed_energies':reports,'odd_threshold_g_squared':str(thresholds)},indent=2))

if __name__=='__main__':main()
