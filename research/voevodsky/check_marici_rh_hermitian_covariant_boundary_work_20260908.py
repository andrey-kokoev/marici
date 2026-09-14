#!/usr/bin/env python3
"""Exact complex Hermitian extension of the covariant graph boundary identity."""
import argparse,json
from pathlib import Path
import sympy as s

def norm2(z):return s.expand(z*s.conjugate(z))
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_hermitian_covariant_boundary_work_certificate_20260908.json');args=p.parse_args();u=s.symbols('u',real=True);x=s.Function('x',real=True)(u);y=s.Function('y',real=True)(u);h=x+s.I*y;checks=0
 xm,ym=s.diff(x,u)-x/2,s.diff(y,u)-y/2
 xp,yp=s.diff(x,u)+x/2,s.diff(y,u)+y/2
 residual=s.expand(xm*xm+ym*ym-xp*xp-yp*yp+s.diff(x*x+y*y,u))
 assert residual==0;checks+=1
 # Polarization with two complex states: the real Hermitian part is the
 # derivative of Re(conj(f)g).
 a,b,c,d=[s.Function(k,real=True)(u) for k in ('a','b','c','d')];f=a+s.I*b;g=c+s.I*d
 polarized=s.expand(
  (s.diff(a,u)-a/2)*(s.diff(c,u)-c/2)+(s.diff(b,u)-b/2)*(s.diff(d,u)-d/2)
  -(s.diff(a,u)+a/2)*(s.diff(c,u)+c/2)-(s.diff(b,u)+b/2)*(s.diff(d,u)+d/2)
  +s.diff(a*c+b*d,u))
 assert polarized==0;checks+=1
 out={'schema':'marici.rh.hermitian-covariant-boundary-work.v1','status':'complex_hermitian_identity_exact','checks':checks,'identity':'||D_-h||^2-||D_+h||^2=-d_u |h|^2','polarized_identity':'Re< D_-f,D_-g>-Re<D_+f,D_+g>=-d_u Re< f,g>','orientation':'integrated graph difference equals |h(q0)|^2-|h(q1)|^2, the negative endpoint-current change','claim':'the reciprocal covariant graph construction supplies an exact Hermitian boundary current with no real-slice restriction','boundary':'matching the two independent theta sheets, forcing work term 2R, and the declared D_bw sign convention remains open'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'orientation':out['orientation']}))
if __name__=='__main__':main()
