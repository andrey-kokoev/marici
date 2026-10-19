"""H7 source radial quadrature/norm binding; the gap and full inverse remain uncertified."""
import argparse
from receipt_replay import assert_receipt_matches
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.fft import dct
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate

CASE=ROOT/'.ai/tmp/scattering-h6-response33/calculation/runs/h6_response33'
SOURCE=ROOT/'.ai/tmp/scattering-response128/relativistic_entrance.py'
NOTE=HOME/'RADIAL-RESOLVENT-ENVELOPE.md'
RESULT=HOME/'results/radial-envelope.v1.json'


def audit():
    historical_validate()
    # Verify the inspected short-path copy against the actual regenerated source.
    engine=ROOT/'.ai/tmp/scattering-h6-response33/calculation/cache/source_work/engine'
    original=next(engine.rglob('relativistic_entrance.py'))
    import os
    if os.name=='nt':original=Path(chr(92)*2+'?'+chr(92)+str(original.resolve()))
    assert original.read_bytes()==SOURCE.read_bytes()
    code=SOURCE.read_text(encoding='utf-8')
    for term in ('N=2**(tail_power+step_power)','f=window/(z-kinetic(k,rho))','moments=dct(f,type=1)','np.arange(2*n)*2**tail_power'):
        assert term in code
    with np.load(CASE/'metadata.npz',allow_pickle=False) as md:
        mass=md['mass'];e0=float(md['e0']);cpose=float(md['cpose'])
    assert np.all(mass>=0) and np.any(mass==0)
    collection=json.loads((CASE/'collection.json').read_text(encoding='utf-8'))
    assert all(row['nD']==32 and row['rho']==1 for row in collection['rows'])
    n,m,N=32,512,65536;h=.3
    y=np.pi*np.arange(N+1)/m;window=np.sinc(y/(2*np.pi))**2
    weights=np.ones(N+1);weights[[0,-1]]=.5
    cosines=np.cos(y[:,None]*(np.arange(n)[None,:]+.5))
    C=(cosines.T*(2/m*weights*window))@cosines
    moments=dct(window,type=1)[np.arange(2*n)*128]/1024
    i=np.arange(n);C_dct=moments[abs(i[:,None]-i[None,:])]+moments[i[:,None]+i[None,:]+1]
    correspondence=float(np.max(abs(C-C_dct)));assert correspondence<1e-11
    spectrum=np.linalg.eigvalsh(C)
    assert spectrum.min()>-1e-11 and spectrum.max()<1+1e-11
    # Closed-source quadrature at a declared test offset; not a full-band test.
    z=-9.;k=y/h;kinetic=2*k*k/(np.sqrt(1+k*k)+1)
    negative_green=(cosines.T*(2/m*weights*window/(kinetic-z)))@cosines
    order_defect=C/9-negative_green
    assert np.linalg.eigvalsh(order_defect).min()>-1e-11
    assert np.linalg.eigvalsh(negative_green).max()<=1/9+1e-11
    paths=[HOME/'receipt_replay.py',SOURCE,NOTE,Path(__file__),CASE/'metadata.npz',CASE/'collection.json',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.radial-envelope.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'radial_cells':n,'cell_width':h,'cosine_frame_length':m*h,'quadrature_intervals':N,
            'source_DCT_versus_Gram_max_defect':correspondence,'Gram_numerical_eigenvalue_interval':[float(spectrum.min()),float(spectrum.max())],
            'analytic_Gram_bound':'0 <= C_N <= I by Bessel for normalized cell indicators in the Neumann cosine basis',
            'closed_Green_envelope':'||G_Q420|| <= 1/Delta conditional on certified invariant-complement gap Delta>=2 rho',
            'downstream_max_occupation_mass':float(mass.max()),'zero_mass_trace_slots':int(np.count_nonzero(mass==0)),
            'solver_norm':'Euclidean normalized raw entrance and all downstream coefficient slots, including algebraic traces',
            'downstream_physical_reconstruction_factor':float(np.sqrt(mass.max())),
            'radial_K_band':[3.09,3.51],'operator_energy_band':[e0+3.09,e0+3.51],
            'displayed_total_energy_band':[e0+3.09+cpose,e0+3.51+cpose],
            'source_gap_certified':False,'full_coupled_inverse_certified':False,
            'H7_disposition':'open; solver norm and conditional raw closed-radial envelope now explicit'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    result=audit()
    if args.check:
        old=json.loads(RESULT.read_text(encoding='utf-8'))
        assert_receipt_matches(old,result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','Gram_numerical_eigenvalue_interval','downstream_physical_reconstruction_factor','H7_disposition')}))


if __name__=='__main__':main()
