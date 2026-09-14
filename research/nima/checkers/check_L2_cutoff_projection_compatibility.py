"""Audit natural projection compatibility of labelled L2 cutoff matrices."""
import argparse,importlib.util,json
from pathlib import Path

def load(path):
 import importlib.util
 s=importlib.util.spec_from_file_location('f',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def build(m,D):
 Q=m.Q;one={(0,0,0):Q(1)};u={(1,0,0):Q(1)};aa={(0,1,0):Q(1)};b={(0,0,1):Q(1)}
 l1=m.add(m.add(b,one),m.scale(u,-1));lm=m.add(aa,m.scale(u,Q(-1,2)));lp=m.add(aa,m.scale(u,Q(1,2)));a2=m.power(aa,2);k=m.add(m.power(aa,4),m.add(m.mul(u,a2),m.scale(m.mul(m.mul(u,a2),m.power(b,2)),-1)))
 out={}
 for sa,sb in ((1,1),(1,0),(0,1),(0,0)):
  for s in range(D+1):
   for i in range(s+1):
    f={(0,i,s-i):Q(1)}
    for plus in (False,True):
     for isq in (False,True):
      out[(sa,sb,s,i,plus,isq)]=m.exact(sa,sb,f,isq,plus,k,l1,lm,lp)
 return out
def proj(col,D):return {x:c for x,c in col.items() if x[1]+x[2]<=D}
def main():
 p=argparse.ArgumentParser();p.add_argument('--formula',required=True);p.add_argument('--output',required=True);a=p.parse_args();m=load(a.formula);rows=[]
 for D in (12,16,20,24):
  lo=build(m,D);hi=build(m,D+4);mismatch=[];new_low=[]
  for k,v in lo.items():
   if proj(v,D)!=proj(hi[k],D):mismatch.append(str(k))
  for k,v in hi.items():
   if k not in lo and proj(v,D):new_low.append(str(k))
  assert not mismatch and not new_low
  rows.append({'from_D':D+4,'to_D':D,'shared_columns_project_identically':len(lo),'new_columns_with_low_output':0})
 out={'schema':'marici.nima.L2-cutoff-projection-compatibility.v1','status':'passed','rows':rows,
  'conclusion':'labelled exact matrices form a strict degree-projection system through D28; new source columns have no old-degree output',
  'scope':'chain-matrix compatibility, not yet compatible Smith bases or derived-cell maps'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
