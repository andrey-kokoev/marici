#!/usr/bin/env python3
"""Compile the strict conductor truncation q on the 50-state omega model."""
import argparse,importlib.util,json
from pathlib import Path

def load(path):
 s=importlib.util.spec_from_file_location('joint',path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def mod_conductor(p):
 # C=A/(X0,...,X5): retain only the constant monomial.
 return p.get((0,0,0,0,0,0),0)

def main():
 a=argparse.ArgumentParser();a.add_argument('--root',default='.');a.add_argument('--output',required=True);z=a.parse_args();r=Path(z.root)
 m=load(r/'research/chatgpt/check_marici_joint_conductor_dual_endpoints.py')
 P=m.node(); pd=m.transpose(P[0],P[1]); top=('P',m.E,m.O)
 # q(p_top^vee)=-1 makes q(kappa)=1 for kappa=-p_top^vee.
 q={b:(-1 if b==top else 0) for b in P[0]}
 defects=[]; checks=0
 for b,col in pd.items():
  val=0
  for target,poly in col.items(): val+=q[target]*mod_conductor(poly)
  if val: defects.append((repr(b),val))
  checks+=1
 assert not defects
 assert q[top]==-1  # H(top)=-e_ALL in the independently certified comparison
 # Every incoming top coefficient is one X_i, hence dies in C.
 incoming=[]
 for b,col in pd.items():
  if top in col:
   incoming.append({'source':repr(b),'coefficient':m.pretty_poly(col[top]),'conductor_value':mod_conductor(col[top])})
 assert len(incoming)==6 and all(x['conductor_value']==0 for x in incoming)
 out={'schema':'marici.strict_conductor_truncation_q.v1','status':'proved',
  'omega_model':'Hom_A(P_B,A Omega_6)[6], P_B ranks (1,9,18,15,6,1)',
  'target':'C Pi^vee[1] (equivalently C Pi^vee[3] after [2])',
  'formula':'q(p_(E,O)^vee)=-1; q=0 on the other 49 dual basis states; coefficients reduced by A -> C',
  'orientation':'kappa=-p_(E,O)^vee, hence q(kappa)=+1',
  'chain_map_defects':defects,'dual_columns_checked':checks,'incoming_top_columns':incoming,
  'consequence':'The strict pullback square-zero block q d_omega-d_C q is zero.',
  'source_provenance':'marici_joint_conductor_dual_endpoints: H(top)=-e_ALL and six conductor-annihilator homotopies'}
 Path(z.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','dual_columns_checked':checks,'incoming_top_columns':len(incoming)}))
if __name__=='__main__':main()
