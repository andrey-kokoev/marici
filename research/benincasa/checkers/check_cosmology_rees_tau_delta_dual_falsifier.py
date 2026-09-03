#!/usr/bin/env python3
"""Falsify the coordinate-delta candidate for a uniform tau dual."""
import contextlib,io,json,runpy
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
rows=g['construct'](8);base=(0,1,1,1,1,1,(0,0));tau_col=(1,base);hits=[]
for label,row in rows.items():
 if tau_col in row:hits.append((label,row[tau_col]))
assert hits
families=Counter(label[1][0] for label,_ in hits)
out={'schema':'marici.benincasa.cosmology-rees-tau-delta-dual-falsifier.v1','candidate':'coordinate delta supported only on the grade-one tau representative','cutoff_tested':8,'relation_rows_with_nonzero_tau_coordinate':len(hits),'hit_families':dict(families),'sample_hits':[{'label':repr(k),'coefficient':str(v)} for k,v in hits[:8]],'candidate_vanishes_on_relations':False,'disposition':'delta_tau is not a quotient functional; any dual certificate must include compensating coordinates satisfying the parametric adjoint recurrences','uniform_dual_constructed':False,'exact_residual':'finite echelon reduction proves some Q8 dual exists, but neither its changing support nor delta_tau supplies a cutoff-independent finite rule','next_acceptance_test':'derive and solve the adjoint recurrences induced separately by twisted_derivative, K_multiplication, and q_multiplication rows, with normalization lambda(tau)=1','passed':True};(R/'cosmology_rees_tau_delta_dual_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
