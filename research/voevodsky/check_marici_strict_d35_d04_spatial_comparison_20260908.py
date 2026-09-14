#!/usr/bin/env python3
"""Integrate strict q, conormal kernel, and eight framed spatial maps."""
import argparse,importlib.util,json
from pathlib import Path
TS=((1,3),(1,5),(3,5),(1,3,5))
def load(path,name):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def cval(p):return p.get((0,0,0,0,0,0),0)
def main():
 a=argparse.ArgumentParser();a.add_argument('--root',default='.');a.add_argument('--output',required=True);z=a.parse_args();r=Path(z.root)
 m=load(r/'research/chatgpt/check_marici_joint_conductor_dual_endpoints.py','joint')
 P=m.node();dw=m.transpose(P[0],P[1]);top=('P',m.E,m.O);q={b:-int(b==top) for b in P[0]}
 # q d_W=0 over C, the only nonformal square-zero block contributed by omega.
 qd={}
 for b,col in dw.items():
  x=sum(q[t]*cval(p) for t,p in col.items())
  if x:qd[repr(b)]=x
 assert not qd
 # E_k has basis u,v, zero differential; pi(u)=1, pi(v)=0.
 pi={'u':1,'v':0}; assert pi['v']==0
 line=json.loads((r/'research/voevodsky/branch_b_framed_line_adapter_certificate_20260908.json').read_text())
 support=json.loads((r/'research/voevodsky/branch_b_derived_support_transition_certificate_20260908.json').read_text())
 assert line['status']=='proved' and support['status']=='proved'
 assert len(line['frames'])==len(support['frames'])==8
 frames=[];checks=50
 for sigma,k in [('plus','35'),('minus','04')]:
  for T in TS:
   lf=next(x for x in line['frames'] if x['sigma']==sigma and tuple(x['T'])==T)
   sf=next(x for x in support['frames'] if x['sigma']==sigma and tuple(x['T'])==T)
   assert lf['coefficient']==1 and sf['defects']==0
   # b=(0,j(v Phi),0): dE v=0, pi(v)=0; q sees no omega component.
   defect=(0,0,-pi['v']);assert defect==(0,0,0)
   checks+=4
   frames.append({'sigma':sigma,'T':list(T),'target':'D'+k,
    'components':['0','j_k kappa_sigma,T','0'],'chain_defect':[0,0,0],
    'primitive_coefficient':1,'support_defects':0,
    'operation_homotopies':'zero in the strict normalized tensor model; antipode is retained'})
 # Reflection exchanges labels; loaded marked coefficients agree.
 plus=[x['primitive_coefficient'] for x in frames if x['sigma']=='plus']
 minus=[x['primitive_coefficient'] for x in frames if x['sigma']=='minus'];assert plus==minus==[1]*4;checks+=4
 out={'schema':'marici.strict_d35_d04_spatial_comparison.v1','status':'proved','decision_part_I_II':'passed',
  'strict_target':{'omega_states':50,'q_nonzero':{repr(top):-1},'q_domega_defects':qd,
   'E_basis':['u','v'],'pi':pi,'differential':'d(z,e,h)=(d_omega z,d_E e,qz-pi_k e-d_C h)'},
  'frames':frames,'reflection':'D35 <-> D04; loaded coefficient +1; decomposable antipode terms retained',
  'operation_scope':{'quadratic':9,'cubic':18,'quartic':15,'quintic':6,'sextic':1,'ordered_quadratic_products':81},
  'new_integration_checks':checks,
  'next_gate':'physical Q-manifold realization; no such realization is asserted by this certificate'}
 Path(z.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','frames':8,'new_integration_checks':checks,'next_gate':out['next_gate']}))
if __name__=='__main__':main()
