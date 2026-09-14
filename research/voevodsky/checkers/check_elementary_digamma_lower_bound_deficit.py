#!/usr/bin/env python3
"""Special-function-free lower enclosure for one rank-two gamma deficit."""
import json,math
from pathlib import Path

def lower_repsi(u,M=2):
 a=.25;b=u/2
 partial=sum(b*b/((k+a)*((k+a)**2+b*b)) for k in range(M))
 tail=.5*math.log1p(b*b/(a+M)**2)
 psi_quarter=-0.5772156649015329-math.pi/2-3*math.log(2)
 return psi_quarter+partial+tail
def midpoint(f,U,N):
 h=U/N;values=[f((k+.5)*h) for k in range(N)]
 return h*sum(values),h*sum(abs(v) for v in values)
def main():
 sigma=.005;d=.25;t=2*sigma;U=math.sqrt(35/t);N=1200000
 gamma_raw,gamma_abs=midpoint(lambda u:math.exp(-t*u*u)*lower_repsi(u)*(1-math.cos(d*u)),U,N)
 gamma_lower=gamma_raw/(2*math.pi);gamma_abs/=2*math.pi
 scout=json.loads((Path(__file__).parents[1]/'results'/'two_translate_weil_deficit_scout.json').read_text())
 row=next(r for r in scout['rows'] if r['sigma']==sigma and r['d']==d)
 nongamma=sum(v for k,v in row['parts'].items() if k!='gamma_integral')
 center=gamma_lower+nongamma
 # Coarse derivative envelope for the elementary lower integrand.
 A=21+2*U;Aprime=20;Mlip=(4*t*U*A+2*Aprime+A*d)/(2*math.pi);h=U/N
 quadrature_error=Mlip*U*h/4
 gamma_tail=2.4e-14
 eps=2**-53;ops_per_panel=40;gamma_rounding=(ops_per_panel*N*eps)/(1-ops_per_panel*N*eps)*gamma_abs
 # Include a much larger reserve for libm transcendental calls and finite prime accumulation.
 finite_allowance=max(1e-6,100*gamma_rounding)
 lower=center-quadrature_error-gamma_tail-finite_allowance
 assert lower>0
 result={'schema':'marici.voevodsky.elementary-digamma-lower-bound-deficit.v2','sigma':sigma,'d':d,'pointwise_bound':'Keep correction terms k=0,1 exactly; bound k>=2 by its decreasing integral','special_function_calls':False,'midpoint_panels':N,'elementary_gamma_lower_center':gamma_lower,'other_source_terms':nongamma,'deficit_center':center,'quadrature_error_bound':quadrature_error,'gamma_tail_allowance':gamma_tail,'absolute_gamma_integral_accumulation':gamma_abs,'standard_rounding_bound':gamma_rounding,'finite_evaluation_allowance':finite_allowance,'final_lower_bound':lower,'strictly_positive':True,'publication_interval_certificate':False,'conclusion':'One rank-two source inequality has a positive enclosure without finite digamma evaluation; directed rounding of elementary functions remains.'}
 out=Path(__file__).parents[1]/'results'/'elementary_digamma_lower_bound_deficit.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
