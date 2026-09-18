#!/usr/bin/env python3
"""Exact two-branch check for the four-mass auxiliary twistors A,B."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_constructors import four_bracket as br,four_mass_auxiliary_branches
# Generic integer columns, deliberately not a rational-normal-curve specialization.
Z={1:s.Matrix([1,0,2,1]),2:s.Matrix([0,1,1,3]),3:s.Matrix([2,1,0,1]),4:s.Matrix([1,3,1,0]),5:s.Matrix([3,0,1,2]),6:s.Matrix([1,2,4,1]),7:s.Matrix([2,3,1,5]),8:s.Matrix([4,1,3,2])}
branches=four_mass_auxiliary_branches(*(Z[i] for i in range(1,9)))
rows=[]
for a,b,A,B in branches:
 # Incidence formulations of A=(78) cap (56B), B=(34) cap (12A).
 rows.append({'alpha':str(a),'beta':str(b),'A_on_78':br(A,Z[7],Z[8],Z[1])==0,'A_in_56B':s.simplify(br(A,Z[5],Z[6],B))==0,'B_on_34':br(B,Z[3],Z[4],Z[1])==0,'B_in_12A':s.simplify(br(B,Z[1],Z[2],A))==0})
checks={'exactly_two_branches':len(branches)==2,'branches_distinct':s.simplify(branches[0][0]-branches[1][0])!=0,'all_incidence_relations':all(all(r[k] for k in ('A_on_78','A_in_56B','B_on_34','B_in_12A')) for r in rows),'quadratic_algebraic_roots_retained':any('sqrt' in r['alpha'] or 'I' in r['alpha'] for r in rows)}
out={'schema':'marici.nima.four-mass-auxiliary-branches.v1','source':'arXiv:1212.5605, equation four_mass_explicit_solution following Table g2n_yangian_invariants','system':['A=Z7+alpha Z8','B=Z3+beta Z4','A=(78)cap(56B)','B=(34)cap(12A)'],'branches':rows,'checks':checks,'passed':all(checks.values()),'scope':'Exact algebraic solution and incidence verification at one generic integer momentum-twistor configuration.'}
p=ROOT/'research/nima/results/four-mass-auxiliary-branches.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
