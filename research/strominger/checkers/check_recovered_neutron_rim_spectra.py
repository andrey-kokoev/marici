"""Recover actual neutron rim response spectra and bind to current operators.

No parity channel is relabelled vacuum/occupied, and no physical unit is added.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from check_neutron_canonical_occupied_closure import ROOT,rank,columns,mv,inverse,mm


def trim(p):
    while len(p)>1 and p[0]==0:p=p[1:]
    return p

def divmod_poly(a,b):
    a=trim(list(a));b=trim(list(b));q=[F(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b);c=a[0]/b[0];q[len(q)-1-k]+=c
        a=trim([x-y for x,y in zip(a,[c*z for z in b]+[F(0)]*k)])
    return trim(q),a

def gcd(a,b):
    while b!=[0]:a,b=b,divmod_poly(a,b)[1]
    return [x/a[0] for x in a]

def evaluate(p,x):
    out=F(0)
    for c in p:out=out*x+c
    return out


def main():
    paths={k:ROOT/p for k,p in {
        'rim':'research/voevodsky/results/deuterium_two_rim.json',
        'collective':'research/voevodsky/results/collective_carrier_spectrum.json',
        'transport':'research/strominger/results/neutron-seam-control-transport.json',
        'binding':'research/strominger/results/neutron-canonical-record-binding.json'}.items()}
    packets={k:json.loads(p.read_text()) for k,p in paths.items()};rim=packets['rim'];transport=packets['transport'];checks={}
    assert rim['verification_passed'] and transport['status']=='passed'
    for p,h in rim['source_sha256'].items():assert hashlib.sha256((ROOT/'research'/p).read_bytes()).hexdigest()==h,p
    for p,h in transport['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    checks['fresh_rim_and_current_neutron_operator_bindings']=True
    H=[list(map(F,r)) for r in transport['native_energy']]
    for row in transport['seam_controls']:
        P=[list(map(F,r)) for r in row['projector']]
        H=[[a+4*b for a,b in zip(r,s)] for r,s in zip(H,P)]
    # A direct unscaled comparison failed in the initial replay. The live
    # collective checker explicitly uses one quarter of the native lift.
    # Preserve and verify that factor; do not silently equate their units.
    rawK=[[sum(H[i][j+6*s] for s in range(3)) for j in range(6)] for i in range(6)]
    expected=[list(map(F,r)) for r in packets['collective']['belt_reduced_matrix']]
    assert rawK!=expected and rawK==[[4*x for x in r] for r in expected]
    K=[[x/4 for x in r] for r in rawK]
    for sector in range(3):
        assert [[sum(H[i+6*sector][j+6*s] for s in range(3))/4 for j in range(6)] for i in range(6)]==K
    checks['prior_one_quarter_normalization_explicitly_recovered']=True
    reports={}
    for sign,name in ((1,'equal_rims'),(-1,'opposite_rims')):
        old=rim['dynamic_response_channels'][name]
        A=[[K[i][j]+sign*K[i][j+3] for j in range(3)] for i in range(3)]
        assert A==[list(map(F,r)) for r in old['operator']]
        num=list(map(F,old['normalized_response_numerator_descending']));den=list(map(F,old['normalized_response_denominator_descending']))
        common=gcd(num,den);nr,rem=divmod_poly(num,common);assert rem==[0]
        dr,rem=divmod_poly(den,common);assert rem==[0]
        v=[F(0),F(1),F(0)];dimension=rank(columns([v,mv(A,v),mv(A,mv(A,v))]))
        assert dimension==len(dr)-1
        for t in (F(1,10),F(1),F(3)):
            shifted=[[A[i][j]+F(i==j)*t for j in range(3)] for i in range(3)]
            assert inverse(shifted)[1][1]==evaluate(nr,-t)/evaluate(dr,-t)
        reports[name]={'visible_dimension':dimension,'cancelled_factor':list(map(str,common)),
                       'response_numerator':list(map(str,nr)),'response_denominator':list(map(str,dr))}
    even=reports['equal_rims'];odd=reports['opposite_rims']
    assert even['visible_dimension']==2 and odd['visible_dimension']==3
    assert list(map(F,even['response_denominator']))==[F(1),-F(4485,3292),F(0)]
    assert list(map(F,even['response_numerator']))==[-F(1),F(2099,3292)]
    assert list(map(F,even['cancelled_factor']))==[F(1),-F(5391,3292)]
    checks['even_channel_dark_pole_cancelled_and_odd_channel_fully_visible']=True
    # R(z)=<v,(A-zI)^-1 v>. Its zero-mode weight is -residue at z=0.
    zero_weight=F(2099,4485)
    binding=packets['binding']['unit_coherent_neutron_empty_record_bank']
    assert zero_weight==F(binding['addressed_native_weight'])
    assert zero_weight/12==F(binding['each_port_energy'])
    checks['zero_pole_weight_recovers_current_rim_weight_and_pulse_expectation']=True
    # Isolate every odd-channel pole. Three disjoint sign-changing intervals
    # exhaust a cubic; exact rational bisection requires no decimal eigensolver.
    p=list(map(F,odd['response_denominator']));brackets=[]
    for i in range(400):
        lo,hi=F(i,100),F(i+1,100)
        if evaluate(p,lo)*evaluate(p,hi)<0:
            for _ in range(60):
                mid=(lo+hi)/2
                if evaluate(p,lo)*evaluate(p,mid)<0:hi=mid
                else:lo=mid
            assert evaluate(p,lo)*evaluate(p,hi)<0;brackets.append((lo,hi))
    assert len(brackets)==3 and all(lo>0 and hi-lo<F(1,10**18) for lo,hi in brackets)
    odd['visible_pole_intervals']=[{'lower':str(a),'upper':str(b),'approximate':float((a+b)/2)} for a,b in brackets]
    even['visible_poles']=['0','4485/3292'];even['dark_pole']='5391/3292';even['zero_mode_weight']=str(zero_weight)
    checks['all_three_odd_poles_certified_by_exact_rational_brackets']=True
    result={'status':'passed','checks':checks,'source_operator':'One quarter of the existing native constraint energy plus the sum of actual seam projectors, restricted to the retained C3-aligned sector.',
            'normalization_control':'Initial unscaled comparison failed; exact comparison proves native-lift operator is four times the historical collective/rim operator. This is the prior checker convention, not a fitted mass scale.',
            'channels':reports,'static_rim_stiffness':rim['effective_coefficient_exact'],
            'interpretation':'These are actual source-port response spectra, not two conditioned two-level register spectra. Equal/odd rim parity is not vacuum/particle occupation. The odd channel has three visible poles and cannot be replaced by a two-dimensional closed response.',
            'normalization':'Existing dimensionless native-generator unit; no physical time/action calibration introduced.',
            'next_test':'Use full matrix-valued two-rim response, with reference and residual retained, when testing an existing source interaction. Do not fit a two-state gap to one pole or to the static stiffness.'}
    inputs=list(paths.values())+[Path(__file__).resolve(),ROOT/'research/voevodsky/checkers/check_deuterium_two_rim.py',ROOT/'research/voevodsky/checkers/check_collective_carrier_spectrum.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    out=ROOT/'research/strominger/results/recovered-neutron-rim-spectra.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'channels':reports,'pulse_expectation_from_zero_pole_weight':str(zero_weight/12)},indent=2))

if __name__=='__main__':main()
