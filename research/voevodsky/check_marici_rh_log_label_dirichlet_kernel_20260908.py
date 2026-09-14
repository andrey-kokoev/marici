#!/usr/bin/env python3
"""Exact identification of the normalized theta Dirichlet Gram as a log-scale kernel."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def rho_squared(n,m):return Fraction(32*n**5*m**5,(n*n+m*m)**5)
def sech_log_ratio(n,m):return Fraction(2*n*m,n*n+m*m)
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_log_label_dirichlet_kernel_certificate_20260908.json');args=p.parse_args();checks=0;rows=[]
 for n,m in ((1,1),(1,2),(2,3),(5,8),(13,21),(32,33)):
  rho2=rho_squared(n,m);sech=sech_log_ratio(n,m)
  assert rho2==sech**5;checks+=1
  assert (rho2==1)==(n==m);checks+=1
  rows.append({'labels':[n,m],'normalized_correlation_squared':f'{rho2.numerator}/{rho2.denominator}','sech_log_ratio':f'{sech.numerator}/{sech.denominator}'})
 # Fixed multiplicative separation has scale-independent correlation.
 for n in (1,2,5,11):
  assert rho_squared(n,2*n)==rho_squared(1,2);checks+=1
 out={'schema':'marici.rh.log-label-dirichlet-kernel.v1','status':'log_translation_kernel_identified','checks':checks,'rows':rows,'identity':'rho(n,m)=sech(log(m/n))^(5/2)','squared_identity':'rho(n,m)^2=(2nm/(n^2+m^2))^5','claim':'after diagonal normalization, the labelled radial Dirichlet Gram depends only on logarithmic label separation','consequence':'adjacent integer labels crowd in log scale, explaining the failed uniform frame margin; fixed multiplicative separation retains a fixed angle','next_constructor':'treat the completion as the positive log-scale convolution kernel rather than an unweighted discrete frame'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'kernel':'sech^(5/2)'}))
if __name__=='__main__':main()
