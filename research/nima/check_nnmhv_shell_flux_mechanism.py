#!/usr/bin/env python3
"""Decompose net cutoff flux into terminal insertion and prior-shell reflow."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/nnmhv-long-numeric-grade-selection.json').read_text());rows={}
for name,data in src['families'].items():
 vals=[]
 for r in data['long_sections']:
  vals.append({'n':r['n'],'net_increment':r['net_increment'],'terminal_insertion':r['terminal_shell'],'prior_shell_reflow':r['prior_shell_reflow'],'reflow_fraction':r['prior_shell_reflow']/r['net_increment']})
 rows[name]=vals
late=[v[-1]['reflow_fraction'] for v in rows.values()];checks={'exact_numeric_decomposition':all(abs(r['net_increment']-r['terminal_insertion']-r['prior_shell_reflow'])<1e-20 for v in rows.values() for r in v),'mechanism_is_transition_dependent':max(late)-min(late)>0.8,'quadratic_quartic_reflow_dominated':rows['quadratic_quartic'][-1]['reflow_fraction']>0.99,'cubic_quadratic_insertion_dominated':rows['cubic_quadratic'][-1]['reflow_fraction']<0.05}
out={'schema':'marici.nima.nnmhv-shell-flux-mechanism.v1','families':rows,'checks':checks,'passed':all(checks.values()),'explanation':'The n^-3 net shell law is a total Stokes flux. It combines terminal-history insertion with reflow of every retained history under section-dependent momentum closure; their shares depend on transition orientation.'};p=ROOT/'research/nima/results/nnmhv-shell-flux-mechanism.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
