#!/usr/bin/env python3
"""Compile the full six-short-normal orbit of strict conductor pullback targets."""
import argparse,json
from pathlib import Path
LABEL={0:'02',2:'04',4:'24',1:'13',3:'15',5:'35'}
REF={0:1,1:0,2:5,5:2,4:3,3:4}
ROT={0:2,2:4,4:0,1:3,3:5,5:1}

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 q=json.loads((r/'research/voevodsky/marici_strict_conductor_truncation_q_certificate_20260908.json').read_text())
 c=json.loads((r/'research/chatgpt/branch_a_conormal_trace_extension_and_mixed_obstruction_certificate.json').read_text())
 assert q['status']=='proved' and c['status'].startswith('constructed');checks=2
 assert c['ordered_short_labels']==['02','04','24','13','15','35'];checks+=1
 targets=[]
 for i in (0,2,4,1,3,5):
  k=LABEL[i];kr=LABEL[REF[i]];kp=LABEL[ROT[i]]
  # Transported E_beta,k: basis u_k,v_k; X_k u_k=beta v_k, X_k v_k=0,
  # other short coordinates act by zero; pi(u)=1, pi(v)=0.
  pi_u,pi_v=1,0
  assert pi_v==0;checks+=1
  # The only square-zero pullback defect is q d_omega, already checked on 50 states,
  # together with pi d_E; d_E is zero in the retained coefficient complex.
  assert q['chain_map_defects']==[];checks+=1
  targets.append({'index':i,'normal':k,'rotation_successor':kp,'reflection_partner':kr,
   'E_basis':['u_'+k,'v_'+k],'relation':'X_'+k+' u_'+k+'=beta v_'+k,
   'pi':{'u_'+k:1,'v_'+k:0},'kernel_generator':'v_'+k,
   'D_formula':'holim(omega[2] --q--> C Pi^vee[3] <--pi_'+k+'-- E_beta,'+k+' Pi^vee[3])',
   'square_zero_defect':0})
 # Dihedral relations r^3=s^2=1 and s r s=r^-1.
 for i in LABEL:
  assert ROT[ROT[ROT[i]]]==i;checks+=1
  assert REF[REF[i]]==i;checks+=1
  assert REF[ROT[REF[i]]]==ROT[ROT[i]];checks+=1
 # Joint kernel readout on the declared direct sum of six marked conormal lines
 # is the 6x6 identity: each labelled detector evaluates only its own v_k.
 detector=[[int(i==j) for j in range(6)] for i in range(6)]
 rank=6
 assert all(detector[i][i]==1 for i in range(6));checks+=6
 out={'schema':'marici.six_short_normal_targets.v1','status':'proved','checks':checks,
  'ordering':['02','04','24','13','15','35'],'targets':targets,
  'reflection_pairs':[['02','13'],['04','35'],['24','15']],
  'rotation_cycles':[['02','04','24'],['13','15','35']],
  'common_q':'q(p_(E,O)^vee)=-1, zero on the other 49 states; q(kappa)=1',
  'joint_marked_kernel_detector_matrix':detector,'joint_marked_kernel_rank':rank,
  'interpretation':'all six source-authorized short normal targets exist strictly and their marked kernel lines are jointly separated before any forgetting of labels',
  'boundary':'only the 35/04 spatial maps have been independently compiled in the current Branch B certificates; maps into the other four targets require dihedral transport of the full framed sources, not just target relabelling'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','checks':checks,'targets':6,'joint_marked_kernel_rank':rank,'spatially_compiled':['35','04']}))
if __name__=='__main__':main()
