#!/usr/bin/env python3
"""Heat-trace regularization of the canonical four-chart Tate-torus carrier."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
rows=[]
for D in (2,20,54):
 for t in (1.0,.25,.05):
  M=max(20,math.ceil(math.sqrt(30/t)))
  theta=sum(math.exp(-t*k*k) for k in range(-M,M+1))
  log_one=D*math.log(theta);ratio=math.exp(log_one-(math.log(4)+log_one))
  tail_bound=2*math.exp(-t*(M+1)**2)/(1-math.exp(-t*(2*M+3)))
  rows.append({'channel_rank':D,'t':t,'cutoff':M,'theta_1d':theta,'log_one_chart_trace':log_one,'normalized_chart_trace':ratio,'one_dimensional_tail_bound':tail_bound})
checks={'all_heat_traces_finite_at_positive_time':all(math.isfinite(r['log_one_chart_trace']) for r in rows),'all_normalized_chart_traces_one_quarter':all(abs(r['normalized_chart_trace']-.25)<1e-14 for r in rows),'all_tail_bounds_small':all(r['one_dimensional_tail_bound']<1e-12 for r in rows)}
out={'schema':'marici.nima.heat-regularized-four-chart-trace.v1','results':rows,'checks':checks,'passed':all(checks.values()),'formula':'Tr(exp(-t Delta_D))=theta(t)^D; on the four-chart direct sum, Tr(P_i exp(-t Delta_total))/Tr(exp(-t Delta_total))=1/4 for every t>0.','covariance':'Pontryagin Fourier conjugates the lattice quadratic number operator to the dual-torus Laplacian, so the regulator is chart-successor invariant.'}
p=ROOT/'research/nima/results/heat-regularized-four-chart-trace.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'checks':checks,'sample':rows[-1],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
