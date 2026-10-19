"""RB1 cycle 1: exact radical shift of the already-certified binary native H."""
import argparse
import json
from pathlib import Path
import numpy as np
from flint import arb,ctx
from high_energy_scattering_net import ROOT,HOME,digest
from receipt_replay import assert_receipt_matches

CERT=HOME/'results/verified-binary-inertia.v1.json'
META=ROOT/'.ai/tmp/scattering-h6-response33/calculation/runs/h6_response33/metadata.npz'
NOTE=HOME/'H7-REFERENCE-BRIDGE.md'
RESULT=HOME/'results/exact-pose-reference.v1.json'


def upper(x):return float(np.nextafter(float(x.upper()),np.inf))
def lower(x):return float(np.nextafter(float(x.lower()),-np.inf))


def audit():
    ctx.prec=128;cert=json.loads(CERT.read_text(encoding='utf-8'))
    for path,value in cert['source_sha256'].items():assert digest(ROOT/path)==value
    assert cert['binary_shifted_H_inertia_certified']
    pose=(3-arb(5).sqrt())/2;exact_shift=10-pose
    error=abs(arb(cert['binary_shift'])-exact_shift)
    separation=arb(cert['verified_inertia_perturbation_margin_lower'])-error.upper()
    assert separation.lower()>0
    with np.load(META,allow_pickle=False) as md:e0=float(md['e0'])
    conditional_gap=exact_shift-arb(e0)-arb(351)/100
    assert conditional_gap.lower()>2
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',CERT,META]
    return {'schema':'marici.scattering.exact-pose-reference.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'exact_pose_ball':str(pose),'exact_shift_ball':str(exact_shift),
            'shift_difference_upper':upper(error),'shifted_binary_H_separation_lower':lower(separation),
            'exact_radical_shift_binary_H_inertia_certified':True,'negative_inertia':cert['negative_inertia'],'zero_inertia':0,
            'conditional_band_gap_stored_e0_lower':lower(conditional_gap),
            'binary_energy_origin':e0,'source_assembly_certified':False,'true_ground_energy_enclosed':False,
            'retained_spectral_frame_certified':False,'full_band_coupled_inverse_certified':False,
            'RB1_execution_cycles_spent':1,'RB1_execution_cycles_remaining':1,
            'H7_disposition':'open; exact pose shift bridged for binary native H, source/frame and coupled inverse remain'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=audit()
    if a.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),r)
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','shift_difference_upper','negative_inertia','conditional_band_gap_stored_e0_lower','H7_disposition')}))


if __name__=='__main__':main()
