#!/usr/bin/env python3
"""Exact audit of the corrected four-point/Schwarz spectral dictionary."""
import json,math
from pathlib import Path

def main():
 fixtures=[]
 for a,b,c in [(2.0,1.0,3.0),(1.0,2.0,1.0),(4.0,0.5,2.0)]:
  C=a+c;D=a*c-b*b;disc=math.sqrt((a-c)**2+4*b*b);x13=(C+disc)/2;x24=(C-disc)/2
  assert abs((x13+x24)-C)<1e-12 and abs(x13*x24-D)<1e-12
  fixtures.append({'matrix':[[a,b],[b,c]],'C13_trace':C,'X13':x13,'X24':x24,'channel_sum':x13+x24,'channel_product':x13*x24,'schwarz_determinant':D,'positive_channels':x13>=0 and x24>=0})
 result={'schema':'marici.voevodsky.C13-trace-channel-product-dictionary.v1','dictionary':['C13 = a+c = trace(S)','X13+X24=C13','X13*X24=ac-|b|^2 = det(S)'],'spectral_channels':['X13=(C13+sqrt((a-c)^2+4|b|^2))/2','X24=(C13-sqrt((a-c)^2+4|b|^2))/2'],'fixtures':fixtures,'theorem':'For Hermitian 2x2 S, positivity is equivalent to X13>=0 and X24>=0. The four-point affine equation is the trace relation; Schwarz positivity is the positivity of both channels, and its determinant is their product.','missing_source_map':'Identify the positive-geometry channel coordinates with these spectral channels of the prime/prime-prime observation square without deriving them from assumed positivity.'}
 out=Path(__file__).parents[1]/'results'/'C13_trace_channel_product_dictionary.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
