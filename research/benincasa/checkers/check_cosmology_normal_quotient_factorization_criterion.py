#!/usr/bin/env python3
"""Exact factorization criterion for linear readouts on the p-normal quotient."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];src=json.loads((ROOT/'research/nima/results/cosmology_relative_c_kernel_section_no_go.json').read_text());p=src['p_covector'];E=src['E_covector']
def dot(a,b):return sum(x*y for x,y in zip(a,b))
tangent_basis=[[-1,1,0],[-3,0,1]];assert all(dot(p,v)==0 for v in tangent_basis);evals=[dot(E,v) for v in tangent_basis];assert evals==[0,-2]
minors=[p[i]*E[j]-p[j]*E[i] for i in range(3) for j in range(i+1,3)];assert minors==[0,-2,-2]
# nx+s*(-3,0,1) remains dp=1 and dc=-E takes every affine value -1+2s.
family={'normal':'(1-3s,0,s)','dp':'1','dc_on_graph':'-1+2s'}
out={'schema':'marici.benincasa.cosmology-normal-quotient-factorization-criterion.v1','theorem':'for nonzero covectors p and L over Q, L is constant on every affine fiber p(n)=1 iff ker(p) is contained in ker(L), equivalently L=lambda*p','proof_witness':{'p':p,'E':E,'basis_of_ker_p':tangent_basis,'E_on_basis':evals,'two_by_two_minors_of_p_E':minors},'application':'the frozen readout dc=-E does not factor through the one-dimensional p-normal quotient','unit_normal_family':family,'exact_residual':'the minors (0,-2,-2) have rank-two witness and E(-3,0,1)=-2; along dp=1, dc=-1+2s ranges over all rational values','consequence':'the ambiguity is an affine rational family, not merely the four sampled values and not a finite slice multiplicity','acceptance_test':'supply a source-derived section selecting one s, or replace E by a proved scalar multiple of p through an authorized readout map','passed':True};outp=ROOT/'research/benincasa/results/cosmology_normal_quotient_factorization_criterion.json';outp.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
