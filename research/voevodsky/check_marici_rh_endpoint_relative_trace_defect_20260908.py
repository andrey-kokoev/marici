#!/usr/bin/env python3
"""Exact coefficient-sensitive trace-defect identity for endpoint translation."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_endpoint_relative_trace_defect_certificate_20260908.json');a=p.parse_args();f0,fa,Ga=s.symbols('f0 fa Ga');checks=0
 left=fa*Ga       # E0 S_a M_f G = f(a)G(a)
 right=f0*Ga      # E0 M_f S_a G = f(0)G(a)
 defect=s.expand(left-right);expected=s.expand((fa-f0)*Ga)
 assert s.expand(defect-expected)==0;checks+=1
 assert defect.subs({fa:f0})==0;checks+=1
 assert defect.subs({Ga:0})==0;checks+=1
 hostiles=[]
 for values in ((1,2,3),(-2,5,7),(0,1,-4)):
  value=defect.subs(dict(zip((f0,fa,Ga),values)))
  assert value!=0;checks+=1
  hostiles.append({'f0':values[0],'fa':values[1],'Ga':values[2],'defect':int(value)})
 out={'schema':'marici.rh.endpoint-relative-trace-defect.v1','status':'relative_trace_defect_exact','checks':checks,'identity':'E0 S_a M_f G - E0 M_f S_a G = (f(a)-f(0))G(a)','symbolic_defect':str(defect),'hostiles':hostiles,'claim':'endpoint evaluation is not cyclic on the coefficient-sensitive translation crossed product; its exact defect is the transported coefficient boundary','disposition':'retain this Hochschild-style boundary term in the graded groupoid determinant instead of imposing an ordinary trace','boundary':'does not yet totalize the defect with primitive, square, seam, and archimedean anomaly lines'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'symbolic_defect':str(defect)}))
if __name__=='__main__':main()
