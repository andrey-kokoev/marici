#!/usr/bin/env python3
"""Symbolic physical/spurious pole audit on a coherent one-parameter family."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle,momentum_conserving_kinematics,transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories,terminal_r_state
z=s.symbols('z');lams=[(1,1),(1,2),(2,1),(1,3),(3,2),(2,5)];tildes=[(1,2),(2,3),(3,5),(5,z)];lam,til,x=momentum_conserving_kinematics(lams,tildes);eps=s.Matrix([[0,1],[-1,0]]);h=compile_nnmhv_histories(6)[0];state=terminal_r_state(h)
_,o=generalized_r(lam,x,6,(),h.outer_pair,lam[1].T*eps,lam[5].T*eps);_,i=generalized_r(lam,x,6,h.inner_prefix,h.inner_pair,transport_spinor(lam,x,state.lower_spinor.vertices),transport_spinor(lam,x,state.upper_spinor.vertices));target=(2,3,4,5);M=s.Matrix([[lam[j][0] for j in target],[lam[j][1] for j in target],[o['xi_coefficients'].get(j,0) for j in target],[i['xi_coefficients'].get(j,0) for j in target]])
ptA=s.prod(angle(lam,j,1 if j==6 else j+1) for j in range(1,7));history=s.cancel(o['prefactor']*i['prefactor']*M.det()**4/ptA)
def sq(a,b):return s.factor(s.det(s.Matrix.hstack(til[a],til[b])))
adjacent={f'[{j},{1 if j==6 else j+1}]':sq(j,1 if j==6 else j+1) for j in range(1,7)};ptS=s.prod(adjacent.values());anti=s.cancel(sq(1,6)**4/ptS);num,den=map(s.factor,s.fraction(history));anum,aden=map(s.factor,s.fraction(anti))
raw_factors=[s.factor(v) for v in o['denominator_factors']+i['denominator_factors']];raw_product=s.factor(s.prod(raw_factors)*ptA)
def canon(v):return str(s.Poly(v,z).monic().as_expr())
raw_irreds={canon(base) for base,power in s.factor_list(raw_product)[1] if base.has(z)};final_irreds={canon(base) for base,power in s.factor_list(den)[1] if base.has(z)};cancelled=sorted(raw_irreds-final_irreds)
physical_survivors={name:str(s.factor(v)) for name,v in adjacent.items() if s.rem(den,s.factor(v),z)==0 and s.degree(v,z)>0};residues={}
for name,v in adjacent.items():
 if s.degree(v,z)==1 and name in physical_survivors:
  root=s.solve(v,z)[0];residues[name]=str(s.factor(s.limit(v*history,z,root)))
checks={'symbolic_history_equals_antimhv':s.factor(history-anti)==0,'spurious_parameter_factors_cancel':len(cancelled)>0,'only_physical_factors_survive':final_irreds.issubset({canon(v) for v in adjacent.values() if v.has(z)}),'physical_poles_survive':len(physical_survivors)>0,'tested_physical_residues_nonzero':len(residues)>0 and all(s.sympify(v)!=0 for v in residues.values())}
out={'schema':'marici.nima.six-point-n2mhv-poles.v1','parameter':'z','history_component':str(history),'antimhv_component':str(anti),'raw_parameter_dependent_factors':sorted(raw_irreds),'cancelled_spurious_factors':cancelled,'final_denominator_factors':sorted(final_irreds),'surviving_physical_brackets':physical_survivors,'physical_residues':residues,'checks':checks,'passed':all(checks.values()),'scope':'Symbolic one-parameter exact audit of one nonzero full-amplitude component.'}
p=ROOT/'research/nima/results/six-point-n2mhv-poles.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
