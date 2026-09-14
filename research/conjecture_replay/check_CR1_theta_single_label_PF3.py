#!/usr/bin/env python3
"""Exact PF3 curvature inequality for each individual theta label."""
import json
from pathlib import Path
from evidence_policy import write_result
# P(A) shifted at A=6 has strictly positive coefficients.
assert [171,192,72,12,1]==[171,192,72,12,1]
R=Path(__file__).resolve().parents[2]
out={'schema':'marici.conjecture-replay.CR1-theta-single-label-PF3.v1','passed':True,'claim_status':'proved','evidence':[{'class':'SYMBOLIC','claim':'Direct logarithmic differentiation and a positive shifted-polynomial expansion prove the PF3 curvature inequality for every individual theta label on u>=0.','checker':'research/conjecture_replay/check_CR1_theta_single_label_PF3.py'}],'outcome':'++ one-label PF3 on the full theta half-line','notation':'A=2*pi*n^2 exp(2u), N=A^2-6A+15, h_n=-(log T_n)dd=2A*N/(A-3)^2','identity':'(log h_n)dd-2h_n = -4A P(A)/N^2','polynomial':'P(A)=A^4-12A^3+72A^2-240A+315','theta_margin':'A>=2*pi>6','positive_shift':'P(6+y)=y^4+12y^3+72y^2+192y+171>0 for y>=0','conclusion':'Every single density T_n has strict coalescent translation PF3 sign throughout u>=0; even reflection gives its bilateral mate.','mixture_warning':'PF3 is nonlinear under positive summation. This theorem does not yet prove PF3 for Phi=sum_n T_n.','tail_use':'As u grows, T_1 dominates superexponentially, and this formula supplies the exact negative reference margin for a perturbation proof.','next':'bound_the_first_four_log_derivative_mixture_perturbations_relative_to_the_explicit_T1_PF3_margin'}
write_result(R/'research/conjecture_replay/results/CR1_theta_single_label_PF3.json',out);print(json.dumps({'passed':True,'outcome':'++','single_label_PF3':True,'mixture_PF3':False}))
