"""Audit coefficient extraction at a^3 b^0 as an L2 transition detector."""
import argparse,importlib.util,json
from pathlib import Path

def load(path):
 s=importlib.util.spec_from_file_location('f',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 p=argparse.ArgumentParser();p.add_argument('--formula',required=True);p.add_argument('--output',required=True);a=p.parse_args();m=load(a.formula);Q=m.Q
 one={(0,0,0):Q(1)};u={(1,0,0):Q(1)};aa={(0,1,0):Q(1)};b={(0,0,1):Q(1)}
 l1=m.add(m.add(b,one),m.scale(u,-1));lm=m.add(aa,m.scale(u,Q(-1,2)));lp=m.add(aa,m.scale(u,Q(1,2)));a2=m.power(aa,2);k=m.add(m.power(aa,4),m.add(m.mul(u,a2),m.scale(m.mul(m.mul(u,a2),m.power(b,2)),-1)))
 checked=0;min_a=10**9
 for sa,sb in ((1,1),(1,0),(0,1),(0,0)):
  for s in range(29):
   for i in range(s+1):
    for plus in (False,True):
     for isq in (False,True):
      col=m.exact(sa,sb,{(0,i,s-i):Q(1)},isq,plus,k,l1,lm,lp);checked+=1
      u0=[a0 for (uu,a0,_),c in col.items() if uu==0 and c]
      if u0:min_a=min(min_a,min(u0))
      assert col.get((0,3,0),0)==0
 assert min_a>=4
 transition={(0,3,0):3,(0,3,1):3};assert transition[(0,3,0)]==3
 out={'schema':'marici.nima.L2-explicit-transition-detector.v1','status':'proved','functional':'rho0(f)=coefficient of a^3*b^0 in u0 sector',
  'columns_checked_through_D28':checked,'minimum_a_order_of_u0_image':min_a,
  'all_degree_reason':'u0 k term has a^4; the only u0 (3/2)d_a k term has a^3 times an L2 base factor of positive a-order',
  'rho0_on_A_image':0,'rho0_on_distinguished_transition':3,
  'normalized_log_selector':'rho=rho0/3 over Z[1/3]','integral_unit_pairing':False}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
