#!/usr/bin/env python3
"""Finite Douglas scout from the separate incoming/outgoing Clark Hardy Grams."""
import json,sys
from pathlib import Path
try:
 import mpmath as mp
 import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp;import numpy as np
sys.path.insert(0,str(Path(__file__).parent));from partial_douglas_constructor import construct
mp.mp.dps=80;pi=mp.pi
def xi(s):return mp.mpf('.5')*s*(s-1)*pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def X(z):return xi(mp.mpf('.5')+1j*z)
def E(z):return X(z)+1j*mp.diff(X,z)
def Es(z):return X(z)-1j*mp.diff(X,z)
def denom(z,w):return 2*pi*1j*(mp.conj(w)-z)
def gram(points,fun):
 G=np.array([[complex(fun(z)*mp.conj(fun(w))/denom(z,w)) for w in points] for z in points]);return (G+G.conj().T)/2
def feature(G):
 lam,U=np.linalg.eigh(G);tol=1e-12*max(1,float(np.max(abs(lam))))
 if float(lam[0]) < -tol:raise RuntimeError('source Hardy Gram unexpectedly indefinite')
 return np.sqrt(np.maximum(lam,0))[:,None]*U.conj().T
def packet(points):
 GA=gram(points,E);GB=gram(points,Es);AS=feature(GA);AB=feature(GB);r=construct(AS,AB,1e-9)
 return {'points':[[float(mp.re(z)),float(mp.im(z))] for z in points],
  'incoming_gram_min_eigenvalue':float(np.linalg.eigvalsh(GA)[0]),'outgoing_gram_min_eigenvalue':float(np.linalg.eigvalsh(GB)[0]),
  'difference_min_eigenvalue':float(np.linalg.eigvalsh(GA-GB)[0]),'douglas_status':r['status'],
  'operator_norm_C':r.get('operator_norm_C'),'factorization_residual':r.get('factorization_residual'),'gram_residual':r.get('gram_residual')}
sets=[
 [mp.mpc(0,.4),mp.mpc(3,.5),mp.mpc(7,.75),mp.mpc(12,1)],
 [mp.mpc(2,2),mp.mpc(8,3),mp.mpc(14,2),mp.mpc(20,4)],
 [mp.mpc(0,.4),mp.mpc(3,.5),mp.mpc(7,.75),mp.mpc(12,1),mp.mpc(18,1.25),mp.mpc(24,1.5)]]
packets=[packet(x) for x in sets]
out={'schema':'marici.voevodsky.source-clark-douglas-packets.v1','packets':packets,
 'construction':'A_S and A_B are factored separately from the incoming E and outgoing E* Hardy Gram matrices; they are not obtained by splitting the signed difference.',
 'all_constructed':all(x['douglas_status']=='CONSTRUCTED' for x in packets),'scope':'finite numerical scout only','rh_proved':False}
p=Path(__file__).parents[1]/'results'/'source_clark_douglas_packets.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
