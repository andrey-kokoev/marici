#!/usr/bin/env python3
"""Arb-certified positivity of every principal minor of one four-point Clark packet."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_flint'))
from flint import arb,acb,acb_series,ctx
ctx.prec=384
I=acb(0,1); HALF=arb(1)/2; PI=arb.pi()
def xi_jet(s):
 x=acb_series([s,1],2); y=(x*(x-1)/2)* (-(x/2)*PI.log()).exp()*(x/2).gamma()*x.zeta(); return y[0],y[1]
def E(z):
 x,xp=xi_jet(HALF-I*z);return x+xp
def theta(z):return E(z.conjugate()).conjugate()/E(z)
def K(z,w):return (1-theta(z)*theta(w).conjugate())/(-I*(z-w.conjugate()))
def parity(p):return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
def det(A):
 n=len(A); out=acb(0)
 for p in itertools.permutations(range(n)):
  x=acb(parity(p))
  for i,j in enumerate(p):x*=A[i][j]
  out+=x
 return out
packet_specs=[
 [('0','.4'),('3','.5'),('7','.75'),('12','1')],
 [('2','2'),('8','3'),('14','2'),('20','4')],
 [('5','.25'),('12','.5'),('20','.75'),('28','1')],
]
packets=[];passed=True
for spec in packet_specs:
 points=[acb(x,y) for x,y in spec];G=[[K(z,w) for w in points] for z in points];minors=[];packet_ok=True
 for n in range(1,5):
  for idx in itertools.combinations(range(4),n):
   d=det([[G[i][j] for j in idx] for i in idx]);ok=d.imag.contains(0) and float(d.real.lower())>0
   packet_ok &= ok;minors.append({'indices':list(idx),'order':n,'determinant':str(d),'strictly_positive':ok})
 passed &= packet_ok;packets.append({'points':[[float(x),float(y)] for x,y in spec],'principal_minors':minors,'all_15_principal_minors_strictly_positive':packet_ok})
out={'schema':'marici.voevodsky.xi-clark-four-point-certified-packets.v2','precision_bits':ctx.prec,
 'packets':packets,'packet_count':len(packets),'principal_minor_count':sum(len(x['principal_minors']) for x in packets),'all_packets_strictly_positive_definite':passed,
 'conclusion':'Each listed four-point Clark Gram packet is rigorously positive definite.',
 'scope':'Finite packets only; no continuum, all-rung, Schur, or RH claim.','passed':passed,'rh_proved':False}
p=ROOT/'research/voevodsky/results/xi_clark_four_point_certified_packet.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'schema':out['schema'],'precision_bits':ctx.prec,'packet_count':len(packets),'minor_count':out['principal_minor_count'],'all_positive':passed,'scope':out['scope']},indent=2))
raise SystemExit(0 if passed else 1)
