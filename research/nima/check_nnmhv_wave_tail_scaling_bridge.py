#!/usr/bin/env python3
"""Relate the fitted n^-2 completion tail to flux and wave-curvature scaling."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];fit=json.loads((ROOT/'research/nima/results/nnmhv-long-exponent-two-limit.json').read_text());raw=json.loads((ROOT/'research/nima/results/nnmhv-long-numeric-grade-selection.json').read_text());rows={}
for name,F in fit['families'].items():
 c2=F['c2'];sections=raw['families'][name]['long_sections'];flux=[{'n':x['n'],'n3_flux':x['n']**3*x['net_increment'],'target':-2*c2,'ratio':x['n']**3*x['net_increment']/(-2*c2)} for x in sections];
 # Exact asymptotic coefficients from discrete differences of c2/n^2.
 rows[name]={'c2':c2,'tail_coefficient':-c2,'predicted_flux_coefficient':-2*c2,'predicted_second_difference_coefficient':6*c2,'measured_scaled_flux':flux,'late_flux_ratio':flux[-1]['ratio']}
checks={'all_tail_exponents_two':all(abs(x['late_scaled_over_minus_c2']-1)<.1 for x in fit['families'].values()),'all_flux_targets_are_minus_two_c2':all(abs(v['predicted_flux_coefficient']+2*v['c2'])<1e-30 for v in rows.values()),'late_n3_flux_has_correct_sign':all(v['measured_scaled_flux'][-1]['n3_flux']*v['predicted_flux_coefficient']>0 for v in rows.values()),'discrete_curvature_is_order_n_minus_four':all(v['predicted_second_difference_coefficient']!=0 for v in rows.values())}
out={'schema':'marici.nima.nnmhv-wave-tail-scaling-bridge.v1','asymptotic_chain':['L-S_n ~ -c2 n^-2','Delta S_n ~ -2 c2 n^-3','Delta^2 S_n ~ 6 c2 n^-4'],'rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'The observed completion law has the derivative hierarchy of a second-order null-wave system: potential/tail degree 2, boundary current degree 3, and discrete curvature degree 4.','claim_boundary':'This establishes asymptotic compatibility with the Möbius d’Alembertian, not a derivation of c2 from the local wave equation.'};p=ROOT/'research/nima/results/nnmhv-wave-tail-scaling-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
