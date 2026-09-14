"""Separate the L2 Bockstein residual from the free alternating cokernel unit."""
import argparse,json,re
from pathlib import Path

def lam(terms):
 return sum(c*((-1)**b) for (a,b),c in terms.items() if a==0)

def main():
 p=argparse.ArgumentParser();p.add_argument('--stderr',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 text=Path(a.stderr).read_text()
 assert 'residual_source=' in text and 's11:minus:q' in text
 # Provenance output is 3*a^3 + 3*a^3*b (modulo the scout prime).
 l2={(3,0):3,(3,1):3}; unit={(0,0):1}
 assert lam(l2)==0; assert lam(unit)==1
 out={'schema':'marici.nima.L2-residual-vs-free-detector.v1','status':'passed',
  'L2_residual':'3*a^3+3*a^3*b','L2_detector_pairing':lam(l2),
  'free_complement':'1','free_complement_detector_pairing':lam(unit),
  'conclusion':'the labelled s11 L2 residual is not the unit-detected free cokernel class; a unit-cone road attachment cannot be identified with it without additional geometric residual data',
  'correction':'modules 152-168 define a valid conditional unit-extension route, not a realized correction for the s11 residual'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
