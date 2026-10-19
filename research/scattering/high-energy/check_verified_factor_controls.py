"""Exact hostile controls for H7 VF1; no source certificate inferred."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from high_energy_scattering_net import ROOT,HOME,digest

NOTE=HOME/'H7-VERIFIED-FACTOR-SUCCESSOR.md'
RESULT=HOME/'results/verified-factor-controls.v1.json'


def audit():
    # Exact U=diag(1,1/2), lambda=(1,-1) and D=U diag(lambda) U*.
    # Gram defect 3/4 reduces separation to 1/4. Assuming U unitary
    # would falsely use 1, admitting a singular perturbation of size 1/4.
    gram=F(3,4);candidate=(1-gram)*F(1)
    assert candidate==F(1,4)
    D=[F(1),-F(1,4)];perturbation=[F(0),F(1,4)]
    assert D[1]+perturbation[1]==0
    assert max(abs(v) for v in perturbation)==candidate
    assert not max(abs(v) for v in perturbation)<candidate
    # Certified count alone need not control an inverse: same inertia,
    # arbitrarily large inverse as positive epsilon tends to zero.
    eps=F(1,10**12);inverse_norm=1/eps
    assert inverse_norm>10**10
    # Separation factorization example L=[[1,0],[2,1]], D=diag(1,-1).
    # ||L^-1||_F²=6 gives a valid 1/6 separation lower bound.
    # B=[[1,2],[2,3]], B^-1=[[-3,2],[2,-1]] has Frobenius²=18<=36.
    ell2=F(6);d=F(1);separation=d/ell2
    assert F(18)<=ell2**2/d**2
    residual=F(1,100);assert residual<separation
    # A stage-1 certificate is not the full claim, and any missing coverage
    # must prevent acceptance even if other booleans are favorable.
    required=('binary_inertia','source_reference','frame_transfer','coupled_full_band_inverse')
    stage1={k:k=='binary_inertia' for k in required}
    assert not all(stage1.values())
    for missing in required:
        flags=dict.fromkeys(required,True);flags[missing]=False
        assert not all(flags.values())
    paths=[NOTE,Path(__file__),HOME/'results/ball-factor-residual.v1.json',HOME/'results/inverse-factor-reconstruction.v1.json']
    return {'schema':'marici.scattering.verified-factor-controls.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'exact_controls':{'nonunitary_frame_separation':str(candidate),'count_only_inverse_norm':str(inverse_norm),
                              'valid_factor_separation':str(separation),'valid_residual':str(residual)},
            'hostiles_refused':['ignore-Gram-defect','nonstrict-perturbation-margin','count-implies-inverse-bound','partial-gate-implies-H7'],
            'source_H7_certified':False,'VF1_execution_cycles_spent':0,'VF1_execution_budget':3}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=audit()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale VF1 controls'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','hostiles_refused':r['hostiles_refused'],'source_H7_certified':False}))


if __name__=='__main__':main()
