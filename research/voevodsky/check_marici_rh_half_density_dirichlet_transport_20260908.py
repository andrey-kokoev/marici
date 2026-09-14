#!/usr/bin/env python3
"""Exact transport of the radial Dirichlet form to logarithmic half-density coordinates."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_half_density_dirichlet_transport_certificate_20260908.json');args=p.parse_args();r,u=s.symbols('r u',positive=True,real=True);checks=0
 f=s.Function('f');h=s.exp(u/2)*f(s.exp(u))
 covariant=s.simplify(s.diff(h,u)-h/2)
 expected=s.exp(3*u/2)*s.Subs(s.Derivative(f(r),r),r,s.exp(u))
 assert s.simplify(covariant-expected)==0;checks+=1
 # With r=e^u, du=dr/r, so |D_u h|^2 du becomes |f'(r)|^2 r^2 dr.
 jacobian_density=s.simplify((s.exp(3*u/2))**2/s.exp(u))
 assert jacobian_density==s.exp(2*u);checks+=1
 # Concrete theta Gaussian verifies the transported positive value.
 phi=s.exp(-s.pi*r*r);radial=s.integrate(s.diff(phi,r)**2*r*r,(r,0,s.oo))
 assert s.simplify(radial-3*s.sqrt(2)/16)==0;checks+=1
 hu=s.exp(u/2)*s.exp(-s.pi*s.exp(2*u));Du=s.simplify(s.diff(hu,u)-hu/2)
 assert s.simplify(Du+2*s.pi*s.exp(s.Rational(5,2)*u)*s.exp(-s.pi*s.exp(2*u)))==0;checks+=1
 out={'schema':'marici.rh.half-density-dirichlet-transport.v1','status':'exact_positive_form_transport','checks':checks,'map':'h(u)=exp(u/2)f(exp(u))','covariant_derivative':'(d_u-1/2)h=exp(3u/2)f_prime(exp(u))','form_identity':'integral_R |f_prime(r)|^2 r^2 dr = integral_Rlog |(d_u-1/2)h(u)|^2 du','gaussian_value':'3*sqrt(2)/16','claim':'the positive radial theta form transports exactly to a logarithmic half-density graph norm','consequence':'comparison with the two-sheet Green work should use the covariant derivative d_u-1/2, not a bare pointwise multiplier','boundary':'the reciprocal two-sheet sewing and equality with D_bw are not yet proved'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'operator':'d_u-1/2'}))
if __name__=='__main__':main()
