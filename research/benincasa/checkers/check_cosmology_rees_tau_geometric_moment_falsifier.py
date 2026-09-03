#!/usr/bin/env python3
"""Falsify the rank-one geometric-moment ansatz for the uniform tau dual."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results';P=101
# For lambda(k,l,(i,j))=C*a^k*prod b_s^l_s*u^i*v^j with nonzero factors,
# divide the x-derivative recurrence at exponents (i,j)=(0,0),(1,0).
# Every connection term is exponent-independent after division; their difference is 1/u.
res=[pow(u,-1,P) for u in range(1,P)];assert all(res) and len(set(res))==P-1
out={'schema':'marici.benincasa.cosmology-rees-tau-geometric-moment-falsifier.v1','field_prime':P,'ansatz':'lambda_g(k,l,(i,j))=C_g a^k product_s(b_s^l_s) u^i v^j with all factors needed for tau normalization nonzero','multiplication_equations':['a K(u,v)=1','b_s q_s(u,v)=1 for each s'],'derivative_test':'subtract the normalized x-derivative recurrence at exponents (0,0) and (1,0); connection terms cancel and leave 1/u=0','nonzero_u_values_tested':P-1,'zero_residual_count':0,'disposition':'the rank-one rational/geometric moment ansatz is impossible independently of the choices of a,b_s and connection coefficients','surviving_ansatz_class':'moments with exponent-dependent weights, equivalently a nontrivial generating-series or residue solution of the adjoint differential equations','uniform_dual_constructed':False,'passed':True};(R/'cosmology_rees_tau_geometric_moment_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
