"""Exact continuum gap certificate, with the full-sector zero-mode control.

No offset or new charging law is added. Positivity applies to the invariant
port-accessible subspace of the existing autonomous contact fixture.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib,json
from check_neutron_canonical_occupied_closure import ROOT,eye,mm,transpose,inverse,scale,difference,rank,encoded


def sqrt_bounds(x,bits=100):
    assert x>0
    unit=1<<bits;k=isqrt((x.numerator*unit*unit)//x.denominator)
    lo,hi=F(k,unit),F(k+1,unit)
    assert lo*lo<=x<=hi*hi
    return lo,hi


def inertia(a):
    a=[list(r) for r in a];positive=negative=0
    assert a==transpose(a)
    while a:
        p=a[0][0]
        if not p:raise ArithmeticError('zero pivot; refine rather than infer inertia')
        positive+=p>0;negative+=p<0
        a=[[a[i][j]-a[i][0]*a[0][j]/p for j in range(1,len(a))] for i in range(1,len(a))]
    return int(positive),int(negative)


def main():
    paths={k:ROOT/p for k,p in {
        'autonomous':'research/strominger/results/neutron-autonomous-rim-scattering.json',
        'finite':'research/strominger/results/neutron-two-rim-contact-binding.json',
        'source':'research/strominger/results/neutron-seam-control-transport.json',
        'memory':'research/strominger/results/neutron-comparison-memory.json'}.items()}
    data={k:json.loads(p.read_text()) for k,p in paths.items()};checks={}
    for obj in data.values():
        assert obj['status']=='passed'
        for p,h in obj['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    checks['fresh_autonomous_core_and_memory_sources']=True
    autonomous=data['autonomous'];assert autonomous['model']['lead_thresholds']==[.5,.5]
    assert all(autonomous['model'][k]==v for k,v in [('kinetic',1),('eta',2),('ell',1)])
    old=data['finite'];g=F(old['parameters']['g'])
    H=[list(map(F,r)) for r in old['full_joint_H_without_mu']]
    K=[r[2:] for r in H[2:]];W=scale(1/g,[r[:2] for r in H[2:]])
    M=[list(map(F,r[2:])) for r in old['source_metric'][2:]]
    T=scale(F(1,3),mm(transpose(W),M));assert mm(T,W)==eye(2)
    B=[list(map(F,r)) for r in autonomous['exact_bright_basis']]
    G=mm(mm(transpose(B),M),B);left=mm(mm(inverse(G),transpose(B)),M)
    Kb=mm(mm(left,K),B);Wb=mm(left,W);Tb=mm(T,B);C=mm(Wb,Tb)
    assert mm(K,B)==mm(B,Kb) and mm(B,Wb)==W
    checks['exact_invariant_bright_core_and_contact_reconstructed']=True
    # For E<Delta=1/2, minimizing both decaying exterior half-lines gives
    # F(E)=Kb+[2q/(q+1)] C-E I, q=sqrt(Delta-E).
    # The exterior H-E is positive; its Schur inertia equals that of F(E).
    def bounded_inertia(E,bits=100):
        qlo,qhi=sqrt_bounds(F(1,2)-E,bits)
        matrices=[];counts=[]
        for q in (qlo,qhi):
            coefficient=2*q/(1+q)
            f=[[Kb[i][j]+coefficient*C[i][j]-E*F(i==j) for j in range(5)] for i in range(5)]
            weighted=mm(G,f);matrices.append(weighted);counts.append(inertia(weighted))
        # G C is positive semidefinite: Wb is the G-adjoint of Tb up to 3.
        assert mm(G,C)==scale(3,mm(transpose(Tb),Tb))
        if counts[0]!=counts[1]:raise ArithmeticError('enclosure straddles crossing')
        return counts[0],qlo,qhi,matrices
    assert bounded_inertia(F(0))[0]==(5,0)
    assert bounded_inertia(F(499,1000))[0]==(3,2)
    checks['no_negative_bright_spectrum_and_two_levels_below_threshold']=True
    lo=F(0);hi=F(1,3)
    assert bounded_inertia(hi)[0]==(4,1)
    for _ in range(60):
        mid=(lo+hi)/2;counts=bounded_inertia(mid)[0]
        if counts==(5,0):lo=mid
        else:assert counts==(4,1);hi=mid
    lower,qll,qlh,lower_forms=bounded_inertia(lo)
    upper,qhl,qhh,upper_forms=bounded_inertia(hi)
    assert lo>0 and hi-lo<F(1,10**18) and lower==(5,0) and upper==(4,1)
    checks['strict_positive_lowest_gap_enclosed_by_exact_rational_inertia']=True
    # This is a gap only for the port-accessible continuum/core block. Every
    # original bank basis vector is still a same-sector normalizable zero mode
    # with no exterior tail or contact amplitude.
    bank=[[F(i==18+j) for i in range(24)] for j in range(6)]
    for v in bank:
        column=[[x] for x in v]
        assert mm(K,column)==[[F(0)] for _ in range(24)]
        assert mm(T,column)==[[F(0)] for _ in range(2)]
    checks['six_full_model_zero_energy_bank_states_retained']=True
    # The broader source operation family has access to these bank coordinates.
    # Do not declare a source-selected superselection rule merely from one
    # autonomous contact's dark space.
    leakage=[]
    for row in data['source']['source_pulses']:
        P=[list(map(F,r)) for r in row['projector']]
        to_bank=mm(P,B)[18:]
        leakage.append({'label':row['label'],'frame':row['frame'],'bank_leakage_rank':rank(to_bank)})
    assert all(r['bank_leakage_rank']>0 for r in leakage)
    checks['retained_source_pulses_do_not_protect_the_positive_gap_sector']=True
    result={'status':'passed','checks':checks,
        'positive_gap_scope':'Invariant rim-accessible sector of the already declared autonomous continuum fixture; no added baseline.',
        'gap_interval':{'lower':str(lo),'upper':str(hi),'approximate':float((lo+hi)/2),'units':'existing collective/rim model energy'},
        'proof':{'exterior_decay':'q=sqrt(1/2-E)','finite_Schur':'Kb+2q/(1+q)*C-E I',
                'lower_endpoint_inertia':lower,'upper_endpoint_inertia':upper,
                'q_bounds_at_lower':[str(qll),str(qlh)],'q_bounds_at_upper':[str(qhl),str(qhh)],
                'weighted_lower_endpoint_enclosures':[encoded(x) for x in lower_forms],
                'weighted_upper_endpoint_enclosures':[encoded(x) for x in upper_forms],
                'argument':'For E below the lead threshold the exterior block of H-E is positive. Schur inertia counts subthreshold eigenvalues. F(E) strictly decreases with E; exact endpoint inertias enclose the lowest eigenvalue.'},
        'full_retained_sector':{'strictly_positive_gap':False,'ground_energy':'0','explicit_bank_zero_states':6,
                               'source_pulse_bank_leakage':leakage},
        'rest_energy_disposition':'A positive localized excitation gap is now certified without an offset. A positive neutron-sector rest gap is not established: the full retained sector still has exact zero states, and the admitted source pulses connect the positive sector to the bank.',
        'next_obligation':'Determine whether a justified source operation supplies bank energy or a protected physical particle sector; do not erase zero modes or identify an accessible bound level with neutron rest mass by naming it.'}
    inputs=list(paths.values())+[Path(__file__).resolve()]
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    out=ROOT/'research/strominger/results/neutron-positive-gap-certificate.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'positive_accessible_gap':result['gap_interval'],
                     'full_sector_ground_energy':'0','protected_against_retained_source_pulses':False},indent=2))

if __name__=='__main__':main()
