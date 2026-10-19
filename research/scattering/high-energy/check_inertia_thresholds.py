"""Bounded lower-threshold robustness search, not an interval-certified gap."""
import argparse
import json
from pathlib import Path
from check_inertia_margin import audit as margin_audit
from high_energy_scattering_net import ROOT,HOME,digest
from receipt_replay import assert_receipt_matches

RESULT=HOME/'results/inertia-thresholds.v1.json'
NOTE=HOME/'INERTIA-THRESHOLD-SEARCH.md'


def audit():
    candidates=[]
    for threshold in (9.5,10.,12.,14.):
        row=margin_audit(threshold)
        assert row['band_gap_candidate_float']>2
        candidates.append(row)
    viable=[r for r in candidates if r['candidate_margin_positive']]
    # Fix this bounded set before seeing results; no adaptive cherry-picking.
    best=max(candidates,key=lambda r:r['factor_separation_candidate_float']/r['factor_residual_Frobenius_norm_float'])
    paths=[NOTE,Path(__file__),HOME/'check_inertia_margin.py',HOME/'receipt_replay.py']
    return {'schema':'marici.scattering.inertia-thresholds.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'fixed_total_thresholds':[9.5,10.,12.,14.],'candidates':candidates,
            'positive_float_margin_thresholds':[r['shift_threshold_total'] for r in viable],
            'best_threshold_by_margin_ratio':best['shift_threshold_total'],
            'best_separation_to_residual_ratio':best['factor_separation_candidate_float']/best['factor_residual_Frobenius_norm_float'],
            'spectral_gap_certified':False,'retained_response_basis_changed':False,
            'H7_disposition':'open; lower-gap factorization routes evaluated numerically, not certified'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','positive_float_margin_thresholds','best_threshold_by_margin_ratio','best_separation_to_residual_ratio','H7_disposition')}))


if __name__=='__main__':main()
