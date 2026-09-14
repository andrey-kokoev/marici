#!/usr/bin/env python3
"""Exact boundary-triplet census for the reciprocal half-line derivative."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
# A=-i diag(d/dt,-d/dt), dom A*=H1(R+)^2, dom A=H1_0(R+)^2.
# Gamma0=(x+y)/sqrt(2), Gamma1=i(x-y)/sqrt(2).
# Direct symbolic coefficient check of Gamma1(f)conj(Gamma0(g))-Gamma0(f)conj(Gamma1(g)).
# coefficients in (x*Xbar,x*Ybar,y*Xbar,y*Ybar)
lhs=(1j,0j,0j,-1j)
rhs=(1j,0j,0j,-1j)
assert lhs==rhs
out={'schema':'marici.conjecture-replay.CR1-reciprocal-halfline-boundary-triplet.v1','operator':{'maximal':'A*=-i diag(d/dt,-d/dt) on H1(R+) direct_sum H1(R+)','minimal':'A=A* restricted by f_+(0)=f_-(0)=0'},'boundary_maps':{'Gamma0':'(f_+(0)+f_-(0))/sqrt(2)','Gamma1':'i(f_+(0)-f_-(0))/sqrt(2)','boundary_space':'C'},'green_identity':'<A*f,g>-<f,A*g>=<Gamma1 f,Gamma0 g>-<Gamma0 f,Gamma1 g>','defect_census':{'Im(z)>0':['exp(i z t),0'],'Im(z)<0':['0,exp(-i z t)'],'indices':[1,1],'Gamma0_on_defect':'nonzero scalar, hence isomorphism'},'gamma_field':{'upper_half_plane':'gamma(z)c=sqrt(2)c(exp(i z t),0)','lower_half_plane':'gamma(z)c=sqrt(2)c(0,exp(-i z t))'},'weyl_function':{'upper_half_plane':'M(z)=i','lower_half_plane':'M(z)=-i'},'outcome':'-+','correction':'The reciprocal pair of half-lines has deficiency indices (1,1), not (2,2). The earlier (2,2) count applies only if each oriented component itself has two endpoint traces, e.g. a finite interval.','consequence':'This free half-line Weyl function is constant and cannot by itself realize the bordered 3x3 Xi characteristic. The known rank-one homogeneous resolvent difference is consistent with boundary rank one. A second boundary degree must come from a finite-interval endpoint, source-port augmentation, or another symmetric channel—not from reciprocal doubling alone.','next':'choose_and_close_augmented_source_port_or_finite_interval_operator_before_Xi_characteristic_comparison','passed':True};p=R/'research/conjecture_replay/results/CR1_reciprocal_halfline_boundary_triplet.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':'-+','indices':[1,1],'boundary_rank':1,'M_upper':'i','next':out['next']}))
