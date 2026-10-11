"""Charge-compatible internal-channel completion of common contact dressing.

Charge/baryon labels and the shared internal-channel law are declared inputs.
Actual contact spectra are inherited unchanged; no mass data select parameters.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

BASE=Path(__file__).resolve().parents[1]


def main():
    path=BASE/'results/common_contact_dressing.json'
    raw=path.read_bytes();source=json.loads(raw)
    assert source['verification_passed']
    certificate=list(map(F,source['positive_response_difference_numerator_descending']))
    assert all(x>=0 for x in certificate) and any(x>0 for x in certificate)
    spectra={s:list(zip(map(F,source[s+'_poles']),map(F,source[s+'_weights']))) for s in ('proton','belt')}
    spectra={s:[(e,w) for e,w in rows if w] for s,rows in spectra.items()}
    Delta,g=F(1,2),F(1,2)
    def response(rows,x):return sum(w/(e+x) for e,w in rows)
    intervals={}
    for name,rows in spectra.items():
        lo=F(0);hi=F(1)
        while Delta+hi<g*g*response(rows,hi):hi*=2
        for _ in range(80):
            mid=(lo+hi)/2
            if Delta+mid<g*g*response(rows,mid):lo=mid
            else:hi=mid
        assert Delta+lo<g*g*response(rows,lo)
        assert Delta+hi>=g*g*response(rows,hi)
        intervals[name]=(lo,hi)
    plo,phi=intervals['proton'];blo,bhi=intervals['belt']
    assert plo>bhi>0
    # Retain the observable spectral coordinates with Gram diag(weights).
    # The omitted source modes are dark spectators of nonnegative energy.
    # In each species block the aux channel has the SAME Q and B as its carrier.
    presentations=[]
    for mu in (F(1,4),F(1,2),F(1)):
        assert mu>phi
        Q=[0];B=[0];metric=[F(1)];H={(0,0):F(0)}
        for name,charge in (('proton',1),('belt',0)):
            rows=spectra[name];start=len(Q)
            Q.extend([charge]*(1+len(rows)));B.extend([1]*(1+len(rows)))
            metric.extend([F(1)]+[w for _,w in rows])
            H[start,start]=mu+Delta
            for j,(energy,w) in enumerate(rows,start+1):
                H[j,j]=mu+energy
                H[start,j]=g*w;H[j,start]=g
            assert mu+Delta>g*g*response(rows,mu)
        assert len(Q)==12
        for (i,j),value in H.items():
            assert metric[i]*value==metric[j]*H.get((j,i),F(0))
            assert (Q[i]-Q[j])*value==0
            assert (B[i]-B[j])*value==0
        p_interval=(mu-phi,mu-plo);b_interval=(mu-bhi,mu-blo)
        difference=(b_interval[0]-p_interval[1],b_interval[1]-p_interval[0])
        assert difference==(plo-bhi,phi-blo)
        presentations.append({'common_bare_offset':str(mu),
                              'reference_level':str(mu+Delta),
                              'proton_energy':float(sum(p_interval)/2),
                              'belt_energy':float(sum(b_interval)/2),
                              'belt_minus_proton':float(sum(difference)/2),
                              'empty_reference_stable':True,
                              'Q_and_B_commute_with_H':True})
    r0_difference=spectra['proton'][0][1]-spectra['belt'][0][1]
    assert r0_difference==F(2099,26910)
    first_moment_difference=sum(e*w for e,w in spectra['belt'])-sum(e*w for e,w in spectra['proton'])
    assert first_moment_difference==F(2099,3292)
    report={
        'verification_passed':True,
        'new_law':'Internal auxiliary channel with the same supplied Q and B as its particle; shared gap Delta and coupling g. No cross-species or vacuum-to-particle exchange.',
        'block':'H_s=mu I + [[Delta,g<w_s|],[g|w_s>,K_s]]',
        'declared_labels':{'vacuum':{'Q':0,'B':0},'proton_and_its_auxiliary':{'Q':1,'B':1},'belt_and_its_auxiliary':{'Q':0,'B':1}},
        'labels_derived_from_geometry':False,
        'reference_field_microscopically_constructed':False,
        'bright_reduced_direct_sum_dimension':12,'full_carriers_plus_auxiliaries_plus_vacuum_dimension':75,
        'relative_shift_equation':'Delta+x_s=g^2*R_s(x_s), x_s>0; E_s=mu-x_s',
        'general_order':'x_proton>x_belt, so E_belt-E_proton>0 for any shared Delta>0, g!=0 and mu>x_proton',
        'splitting_independent_of_common_mu':True,
        'shared_illustrative_parameters':{'Delta':str(Delta),'g':str(g)},
        'binding_shift_intervals':{s:list(map(str,interval)) for s,interval in intervals.items()},
        'common_offset_controls':presentations,
        'weak_coupling_splitting':'(2099/26910)*g^2/Delta + O(g^4), at fixed Delta>0',
        'strong_coupling_splitting_limit':'2099/6584, at fixed Delta as |g| tends to infinity; keeping the vacuum stable requires a correspondingly large common mu',
        'scope':'A consistent internal-channel completion of the existing conditional comparison, not a derivation of baryon number, physical charges, mediator, clock scale or neutron mass.',
        'source_sha256':sha256(raw).hexdigest()}
    (BASE/'results/charge_compatible_contact.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
