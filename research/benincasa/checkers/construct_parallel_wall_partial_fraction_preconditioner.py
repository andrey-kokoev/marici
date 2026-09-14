#!/usr/bin/env python3
"""Remove the mutual IBP cycles from the three shifted parallel wall pairs."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
u=s.symbols('u')
rows=[]
for m in range(1,4):
 for n in range(1,4):
  f=1/(u**m*(u+1)**n);apart=s.apart(f,u)
  denoms=[s.factor(x.as_numer_denom()[1]) for x in s.Add.make_args(apart)]
  separated=all(not (d.has(u) and s.rem(s.Poly(d,u),s.Poly(u,u))==0 and s.rem(s.Poly(d,u),s.Poly(u+1,u))==0) for d in denoms)
  # More directly every denominator is a pure power of u or u+1.
  pure=all(any(s.simplify(d/base**k)==1 for base in (u,u+1) for k in range(1,7)) for d in denoms)
  rows.append({'powers':[m,n],'identity':s.sstr(apart),'exact':s.simplify(f-apart)==0,'single_wall_terms_only':pure})
pairs=[{'walls':['g1','s23'],'relation':'s23=g1+1','normal':'b or c'},{'walls':['g2','s31'],'relation':'s31=g2+1','normal':'a or c'},{'walls':['g3','s12'],'relation':'s12=g3+1','normal':'a or b'}]
checks={'all_nine_power_pairs':len(rows)==9,'identities_exact':all(r['exact'] for r in rows),'all_terms_single_wall':all(r['single_wall_terms_only'] for r in rows),'three_source_pairs':len(pairs)==3,'covers_cubic_depth':rows[-1]['powers']==[3,3]}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.parallel-wall-partial-fraction-preconditioner.v1','rule':'Before applying H_q, decompose every product q^{-m}(q+1)^{-n} into a sum supported on q alone or q+1 alone.','parallel_pairs':pairs,'identities':rows,'termination_effect':'The apparent two-cycle q -> q+1 -> q is removed because no preconditioned summand contains both shifted parallel walls. This works through the complete observed pole depth three.','constructed_interface':'exact rational preconditioner for the g1/s23, g2/s31, and g3/s12 cycles','remaining_cycles':'couplings among nonparallel B, g, and K0 divisors still require a multigraded order or syzygy reduction.','next_task':'Build the post-preconditioning divisor dependency graph for the G12 pair and solve the strict weight inequalities; isolate any remaining directed cycle involving B12 or K0.','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/parallel_wall_partial_fraction_preconditioner.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'identities':len(rows),'pairs':[p['walls'] for p in pairs],'remaining':out['remaining_cycles']}))
