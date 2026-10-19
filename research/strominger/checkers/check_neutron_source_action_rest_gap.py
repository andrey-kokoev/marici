"""Conditional full-sector rest-gap completion using actual source actions.

NEW LAW: H_core=K+beta*(sum of the 18 source projectors)/3. This
stationary action is not the original time-ordered pulse programme. No scalar
rest offset is used, and no source-selected beta or physical unit is claimed.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq
from check_neutron_canonical_occupied_closure import ROOT,eye,mm,transpose,inverse,scale,difference,rank,encoded,add
from check_neutron_positive_gap_certificate import sqrt_bounds,inertia
from check_neutron_autonomous_rim_scattering import Contact


def main():
    root=ROOT/'research/strominger/results'
    paths={k:root/p for k,p in {'source':'neutron-seam-control-transport.json','finite':'neutron-two-rim-contact-binding.json',
                              'gap':'neutron-positive-gap-certificate.json','autonomous':'neutron-autonomous-rim-scattering.json'}.items()}
    data={k:json.loads(p.read_text()) for k,p in paths.items()};checks={}
    for obj in data.values():
        assert obj['status']=='passed'
        for p,h in obj['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    src=data['source'];old=data['finite']
    M=[list(map(F,r)) for r in src['metric']];R=[list(map(F,r)) for r in src['native_rotation']]
    H=[list(map(F,r)) for r in old['full_joint_H_without_mu']]
    K=[r[2:] for r in H[2:]];W=scale(1/F(old['parameters']['g']),[r[:2] for r in H[2:]])
    T=scale(F(1,3),mm(transpose(W),M))
    source_action=[[F(0)]*24 for _ in range(24)]
    for row in src['source_pulses']:
        P=[list(map(F,r)) for r in row['projector']]
        assert mm(P,P)==P and mm(transpose(P),M)==mm(M,P)
        source_action=add(source_action,scale(F(1,3),P))
    assert mm(source_action,R)==mm(R,source_action)
    checks['actual_positive_source_generators_and_frame_average']=True
    # Positivity for EVERY beta>0 follows from the common-kernel test, not from
    # tuning the fixture beta=1: all three summands are positive forms.
    assert rank(K)==17 and rank(add(K,source_action))==23
    assert rank(add(add(K,source_action),mm(W,T)))==24
    checks['no_common_zero_vector_of_native_source_and_contact_forms']=True
    # All subthreshold states lie in the 12D C3-invariant core. The entire
    # complementary 12D native sector remains and has energy at least 3/4.
    Pc=scale(F(1,3),add(add(eye(24),R),mm(R,R)))
    A0=scale(F(1,4),[list(map(F,r)) for r in src['native_energy']])
    assert A0==scale(F(3,4),difference(eye(24),Pc))
    B=[[F(i<18 and i%6==j) if j<6 else F(i==18+j-6) for j in range(12)] for i in range(24)]
    G=mm(mm(transpose(B),M),B);left=mm(mm(inverse(G),transpose(B)),M)
    assert mm(B,left)==Pc and mm(Pc,W)==W
    Knew=add(K,source_action);Kb=mm(mm(left,Knew),B);C=mm(mm(left,W),mm(T,B))
    assert mm(Knew,B)==mm(B,Kb)
    assert mm(G,C)==scale(3,mm(transpose(mm(T,B)),mm(T,B)))
    checks['retained_12D_complement_bounded_above_search_window']=True
    def certify(E):
        qlo,qhi=sqrt_bounds(F(1,2)-E,90);counts=[];forms=[]
        for q in (qlo,qhi):
            Fmatrix=[[Kb[i][j]+2*q/(1+q)*C[i][j]-E*F(i==j) for j in range(12)] for i in range(12)]
            weighted=mm(G,Fmatrix);counts.append(inertia(weighted));forms.append(weighted)
        assert counts[0]==counts[1],(E,counts)
        return counts[0],forms
    assert certify(F(0))[0]==(12,0)
    lo=F(0);hi=F(499,1000);assert certify(hi)[0][1]>0
    for _ in range(48):
        mid=(lo+hi)/2
        if certify(mid)[0][1]==0:lo=mid
        else:hi=mid
    assert lo>0 and hi-lo<F(1,10**14)
    low_inertia,low_forms=certify(lo);high_inertia,high_forms=certify(hi)
    checks['full_sector_lowest_gap_certified_by_exact_rational_inertia']=True
    # Numerical state only supplements the rational energy certificate.
    L=np.linalg.cholesky(np.array(M,float)).T
    Kw=L@np.array(K,float)@np.linalg.inv(L);Aw=L@np.array(source_action,float)@np.linalg.inv(L)
    Ww=L@np.array(W,float)/np.sqrt(3.)
    Hfull=Kw+Aw
    E=float((lo+hi)/2);q=np.sqrt(.5-E)
    schur=Hfull+2*q/(1+q)*Ww@Ww.T-E*np.eye(24)
    ev,v=eigh(schur);c=v[:,np.argmin(abs(ev))]
    a=Ww.T@c/(1+q);normalization=np.dot(c,c)+np.dot(a,a)/q
    c/=np.sqrt(normalization);a/=np.sqrt(normalization)
    ledger={'old_native_and_seam_energy':float(c@Kw@c),'source_action_energy':float(c@Aw@c),
            'contact_energy':float(2*np.linalg.norm(a-Ww.T@c)**2),
            'exterior_kinetic_energy':float(q*np.dot(a,a)),
            'exterior_threshold_energy':float(.5*np.dot(a,a)/q)}
    assert min(ledger.values())>-1e-12 and abs(sum(ledger.values())-E)<1e-12
    checks['normalized_bound_state_and_all_energy_terms_accounted']=True
    scan=[]
    for beta in (.01,.1,.5,1.,2.,10.):
        def smallest(E):
            q=np.sqrt(.5-E)
            return eigh(Kw+beta*Aw+2*q/(1+q)*Ww@Ww.T-E*np.eye(24),eigvals_only=True)[0]
        assert smallest(0)>0
        e=brentq(smallest,0,.499999999,xtol=1e-13)
        scan.append({'beta':beta,'lowest_energy':float(e)})
    # Existing interface solver now includes all 24 source-energized core modes.
    scatter=Contact(Hfull,Ww,[.5,.5]);max_unitarity=0.
    for Etest in (.51,.8,1.13,2.,3.,4.5):
        s=scatter.scatter(Etest);max_unitarity=max(max_unitarity,s['unitarity'])
        assert s['unitarity']<1e-9 and s['core_residual']<1e-9
    checks['completed_autonomous_contact_remains_flux_conserving']=True
    # Quantify nonuniqueness: a bank trial vector costs beta times a fixed
    # finite action, so no beta-independent strictly positive gap follows.
    trials=[mm(mm(transpose([[F(i==j)] for i in range(24)]),mm(M,source_action)),[[F(i==j)] for i in range(24)])[0][0]/M[j][j] for j in range(18,24)]
    assert all(x>0 for x in trials)
    result={'status':'passed','checks':checks,
        'new_law':'K_completed=K+beta*(1/3)*sum_{label,frame} P_source(label,frame)',
        'admission':'Explicit stationary completion. Not derived from the unchanged ordered-pulse programme; beta and activation as a rest-energy term are not source-selected.',
        'fixture':{'beta':'1','kinetic':'1','contact_eta':'2','contact_length':'1','lead_threshold':'1/2','additive_rest_offset':'0'},
        'positive_for_every_beta_gt_zero':True,'exact_common_kernel_dimension':0,
        'full_retained_core_dimension':24,'low_energy_core_dimension':12,'retained_complement_energy_lower_bound':'3/4',
        'gap_interval':{'lower':str(lo),'upper':str(hi),'approximate':float((lo+hi)/2)},
        'endpoint_inertias':[low_inertia,high_inertia],
        'source_action':encoded(source_action),'lower_endpoint_schur_enclosures':[encoded(x) for x in low_forms],
        'upper_endpoint_schur_enclosures':[encoded(x) for x in high_forms],
        'normalized_bound_state_energy_ledger':ledger,
        'core_norm':float(c@c),'exterior_norm':float(np.dot(a,a)/q),
        'beta_sensitivity':scan,'bank_trial_upper_bound_coefficients':list(map(str,trials)),
        'scattering_unitarity_maximum':max_unitarity,
        'rest_scope':'Positive lowest stationary energy for a fully retained neutron-labelled internal/contact model under the stated new law. Not an established physical neutron mass or a source-selected rest law.',
        'scale_limit':'As beta tends to zero, bank trial vectors force the gap to zero. Geometry alone therefore does not supply a universal positive numerical rest value.'}
    outfile=root/'neutron-source-action-rest-gap.npz'
    np.savez_compressed(outfile,core_operator=Hfull,source_action=Aw,contact=Ww,bound_core=c,bound_boundary=a,bound_energy=float((lo+hi)/2),metric=np.array(M,float),whitening=L)
    result['npz_sha256']=hashlib.sha256(outfile.read_bytes()).hexdigest()
    inputs=list(paths.values())+[Path(__file__).resolve(),ROOT/'research/strominger/checkers/check_neutron_positive_gap_certificate.py',ROOT/'research/strominger/checkers/check_neutron_autonomous_rim_scattering.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    (root/'neutron-source-action-rest-gap.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'full_sector_gap':result['gap_interval'],'ledger':ledger,'beta_sensitivity':scan},indent=2))

if __name__=='__main__':main()
