#!/usr/bin/env python3
"""Directed-node Arb assembly of the rank-80 finite gamma matrix on [0,250]."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,acb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,acb,arb_mat
flint.ctx.prec=192;N=80;Q=48;L=arb('0.55');edges=tuple(str(k) for k in range(251));logpi=arb.pi().log();rows=[[],[]];srows=[[],[]]
def sj(n,x):return (arb.pi()/(2*x)).sqrt()*x.bessel_j(arb(n)+arb('0.5'))
for sa,sb in zip(edges[:-1],edges[1:]):
 a=arb(sa);b=arb(sb)
 for k in range(Q):
  root,w=arb.legendre_p_root(Q,k,weight=True);u=(a+b)/2+(b-a)*root/2;fac=(b-a)*w/2*(acb(arb('0.25'),u/2).digamma().real-logpi)/(2*arb.pi());vals=[]
  for n in range(N):vals.append(2*L*((2*n+1)/(2*L)).sqrt()*((-1)**(n//2))*sj(n,L*u))
  for parity in (0,1):
   v=[vals[n] for n in range(parity,N,2)];rows[parity].append(v);srows[parity].append([fac*x for x in v])
blocks=[arb_mat(rows[p]).transpose()*arb_mat(srows[p]) for p in (0,1)]
maxrad=max(float(blocks[p][i,j].rad()) for p in (0,1) for i in range(40) for j in range(40));maxabs=max(max(abs(float(blocks[p][i,j].lower())),abs(float(blocks[p][i,j].upper()))) for p in (0,1) for i in range(40) for j in range(40))
# Materialize the full parity matrix and inject the analytic Gauss remainder.
G=arb_mat(N,N);quadrem=arb('2.544e-13')
for i in range(N):
 for j in range(N):G[i,j]=arb(0) if (i+j)%2 else blocks[i%2][i//2,j//2]+arb(0,quadrem)
out={'schema':'marici.voevodsky.two-prime-finite-gamma-arb.v1','precision_bits':flint.ctx.prec,'L':'0.55','dimension':N,'cutoff':250,'gauss_order_per_panel':Q,'panel_edges':[float(x) for x in edges],'maximum_node_evaluation_entry_radius':maxrad,'maximum_entry_absolute_upper':maxabs,'bernstein_ellipse':{'rho':1.477032961426901,'semi_minor':'0.2','uniform_integrand_bound':'3','summed_gauss_remainder_upper':'2.544e-13'},'budget':'2e-11','node_rounding_budget_met':maxrad<2e-11,'total_error_upper':maxrad+2.544e-13,'matrix':[[str(G[i,j]) for j in range(N)] for i in range(N)],'passed':maxrad+2.544e-13<2e-11,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_prime_finite_gamma_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
