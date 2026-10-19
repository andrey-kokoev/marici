"""Audit a freshly downloaded authoritative physical target, not a mass prediction."""
from pathlib import Path
from decimal import Decimal as D,getcontext
from datetime import datetime,timezone
import hashlib,json,re
getcontext().prec=60
ROOT=Path(__file__).resolve().parents[3]


def main():
    root=ROOT/'research/strominger/results'
    source=root/'physical-neutron-reference/codata-allascii.txt'
    text=source.read_text();assert '2022 CODATA adjustment' in text
    def row(name):
        lines=[line for line in text.splitlines() if re.split(r' {2,}',line.strip())[0]==name]
        assert len(lines)==1,name
        parts=re.split(r' {2,}',lines[0].strip())
        return {'value':D(parts[1].replace(' ','')),
                'uncertainty':D(0) if parts[2]=='(exact)' else D(parts[2].replace(' ','')),
                'unit':parts[3],'source_line':lines[0]}
    mass=row('neutron mass');energy=row('neutron mass energy equivalent');mev=row('neutron mass energy equivalent in MeV')
    speed=row('speed of light in vacuum');charge=row('elementary charge')
    assert speed['uncertainty']==charge['uncertainty']==0
    joules_per_MeV=charge['value']*D(10)**6
    from_mass=mass['value']*speed['value']**2
    from_mev=mev['value']*joules_per_MeV
    # The three entries are rounded reports of the same constant, not three
    # independent experiments. Compare their last reported decimal places.
    assert abs(from_mass-energy['value'])<D('0.00000000001e-10')
    assert abs(from_mev-energy['value'])<D('0.00000000001e-10')
    assert mass['value']-100*mass['uncertainty']>0
    assert mev['value']==D('939.56542194') and mev['uncertainty']==D('0.00000048')
    receipt=root/'neutron-source-action-rest-gap.json';model=json.loads(receipt.read_text())
    assert model['status']=='passed'
    for p,h in model['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    def rational(s):
        a,b=s.split('/');return D(a)/D(b)
    lo=rational(model['gap_interval']['lower']);hi=rational(model['gap_interval']['upper'])
    E0=(lo+hi)/2
    fitted_scale=mev['value']/E0
    assert abs(fitted_scale*E0-mev['value'])<D('1e-50')
    result={'status':'passed','checks':{'authoritative_CODATA_snapshot_identified':True,
        'SI_mass_and_energy_conversions_agree_to_display_rounding':True,
        'positive_physical_reference_far_exceeds_standard_uncertainty':True,
        'model_calibration_distinguished_from_prediction':True},
        'source_url':'https://physics.nist.gov/cuu/Constants/Table/allascii.txt',
        'reference':'2022 CODATA adjustment, NIST complete listing',
        'snapshot_file_mtime_utc':datetime.fromtimestamp(source.stat().st_mtime,timezone.utc).isoformat(),
        'retrieval_note':'Individual CGI constant pages returned HTTP 403. The complete NIST table was successfully retrieved directly over HTTPS.',
        'physical_neutron':{'mass_kg':str(mass['value']),'mass_standard_uncertainty_kg':str(mass['uncertainty']),
            'rest_energy_J':str(energy['value']),'rest_energy_standard_uncertainty_J':str(energy['uncertainty']),
            'rest_energy_MeV':str(mev['value']),'rest_energy_standard_uncertainty_MeV':str(mev['uncertainty'])},
        'exact_conversion':{'c_m_per_s':str(speed['value']),'joules_per_MeV':str(joules_per_MeV)},
        'source_lines':[mass['source_line'],energy['source_line'],mev['source_line']],
        'nonprediction_control':{'model_dimensionless_energy':str(E0),
            'energy_unit_MeV_required_to_fit_neutron':str(fitted_scale),
            'interpretation':'This unit is computed FROM the measured neutron energy, so agreement would be calibration by construction, not a derivation or independent test. It has NOT been applied to the model inputs.'},
        'disposition':'The physical neutron rest energy is established here by an authoritative experimental adjustment. The repository model does not independently derive it.'}
    inputs=[source,receipt,Path(__file__).resolve()]
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    (root/'physical-neutron-rest-energy.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','physical_neutron':result['physical_neutron'],
                     'fitting_not_prediction':result['nonprediction_control']},indent=2))

if __name__=='__main__':main()
