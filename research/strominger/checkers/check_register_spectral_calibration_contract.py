"""Recover a register law from conditional spectra and occupations.

Uses prior checked examples as regression data, not as physical observations.
No synthetic values are admitted as source-selected measurements.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from check_neutron_canonical_occupied_closure import ROOT


def reconstruct(rv,rb,nv,nb):
    assert rv>0 and rb>0 and 0<=nv<=1 and 0<=nb<=1
    plus=rv*(1-2*nv);minus=rb*(2*nb-1)
    J=(plus+minus)/2;epsilon=(plus-minus)/2
    gv=rv*rv*nv*(1-nv);gb=rb*rb*nb*(1-nb)
    if gv!=gb:raise ValueError('conditional spectra do not share one mixing amplitude')
    assert J>epsilon>0
    return {'epsilon':epsilon,'J':J,'g_squared':gv,'gap':21*(rv-rb)/2}


def main():
    path=ROOT/'research/strominger/results/neutron-rest-gap-calibration.json'
    data=json.loads(path.read_text());assert data['status']=='passed'
    for p,h in data['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    rows=[]
    for trial in data['parameter_completions']:
        rv=F(trial['vacuum_register_gap']['0']);rb=F(trial['occupied_register_gap']['0'])
        nv=F(trial['inactive_occupation']['0']);nb=F(trial['matched_occupation']['0'])
        found=reconstruct(rv,rb,nv,nb)
        assert found['epsilon']==F(trial['epsilon']) and found['J']==F(trial['J'])
        assert found['g_squared']==F(trial['g'])**2 and found['gap']==F(trial['rest_gap']['0'])
        rows.append({'conditional_readouts':{'vacuum_gap':str(rv),'occupied_gap':str(rb),'vacuum_occupation':str(nv),'occupied_occupation':str(nb)},
                     'reconstructed':{k:str(v) for k,v in found.items()},'evidence_class':'previous supplied-law regression fixture, not a selected native readout'})
    try:reconstruct(F(17,10),F(1),F(1,65),F(4,5))
    except ValueError:pass
    else:raise AssertionError('mismatched vacuum spectrum and occupation accepted')
    result={'status':'passed','checks':['current spectral example provenance','both full parameter reconstructions','both exact gap reconstructions','incompatible conditional readouts rejected'],
            'reconstruction':{'epsilon':'[rv(1-2nv)-rb(2nb-1)]/2','J':'[rv(1-2nv)+rb(2nb-1)]/2',
                              'g_squared':'rv^2 nv(1-nv)=rb^2 nb(1-nb)','conditional_rest_gap':'21(rv-rb)/2'},
            'regressions':rows,
            'physical_calibration_contract':{'time_rate':'omega=theta_first/t_first, using a timed first-arrival and retained winding/orientation',
                'action_scale':'kappa=-calibrated_symplectic_area/unwrapped_horizontal_phase, under the separately implemented horizontal-transport protocol',
                'energy_conversion':'E_physical=kappa*omega*E_angular, only after matching the pulse and phase-action normalizations',
                'selection_status':'No admitted physical first-arrival, calibrated area or horizontal-loop source implementation has been supplied by the inspected packets.'},
            'scope':'Inverse identifiability and input contract, not a source-selected register spectrum or physical calibration.'}
    inputs=[path,Path(__file__).resolve(),ROOT/'research/nima/retained-clock-calibration-identifiability.md',ROOT/'research/voevodsky/checkers/check_seam_occupation_energy.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    out=ROOT/'research/strominger/results/register-spectral-calibration-contract.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','regressions':rows,'source_selected_spectrum_delivered':False,'physical_normalization_delivered':False},indent=2))

if __name__=='__main__':main()
