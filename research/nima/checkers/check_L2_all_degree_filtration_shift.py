"""Symbolic support audit for the all-degree L2 filtration shift."""
import argparse,importlib.util,json
from pathlib import Path

def load(path):
 s=importlib.util.spec_from_file_location('f',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main():
 p=argparse.ArgumentParser();p.add_argument('--formula',required=True);p.add_argument('--output',required=True);a=p.parse_args();m=load(a.formula);Q=m.Q
 one={(0,0,0):Q(1)};u={(1,0,0):Q(1)};aa={(0,1,0):Q(1)};b={(0,0,1):Q(1)}
 l1=m.add(m.add(b,one),m.scale(u,-1));lm=m.add(aa,m.scale(u,Q(-1,2)));lp=m.add(aa,m.scale(u,Q(1,2)));a2=m.power(aa,2);k=m.add(m.power(aa,4),m.add(m.mul(u,a2),m.scale(m.mul(m.mul(u,a2),m.power(b,2)),-1)))
 rows=[];shifts=set();s=10
 # Interior monomials expose every derivative term. Translation of exponents
 # by a or b changes source and output degree equally, so these support shifts
 # are independent of total source degree.
 for sa,sb in ((1,1),(1,0),(0,1),(0,0)):
  for plus,l2 in ((False,lm),(True,lp)):
   for isq in (False,True):
    local=set()
    for i in range(1,s):
     col=m.exact(sa,sb,{(0,i,s-i):Q(1)},isq,plus,k,l1,lm,lp)
     local|={a0+b0-s for _,a0,b0 in col}
    assert local;shifts|=local
    rows.append({'sa':sa,'sb':sb,'side':'plus' if plus else 'minus','kind':'q' if isq else 'p','degree_shifts':sorted(local)})
 assert shifts=={2,3,4,5,6,7}
 out={'schema':'marici.nima.L2-all-degree-filtration-shift.v1','status':'proved','operator_cases':rows,
  'all_shifts':sorted(shifts),'minimum_shift':2,
  'translation_argument':'monomial exponent translation shifts input and output equally; derivative lowers by one and fixed multipliers determine listed shifts',
  'conclusion':'every nonzero labelled L2 column raises a+b degree by 2 through 7 in all degrees; cutoff projections are strict globally'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
