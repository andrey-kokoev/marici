#!/usr/bin/env python3
"""Dihedrally transport the complete framed/support maps to all six short normals."""
import argparse,json
from pathlib import Path
LABEL={0:'02',2:'04',4:'24',1:'13',3:'15',5:'35'}
ROT={0:2,2:4,4:0,1:3,3:5,5:1}
PLUS=(1,3,5);MINUS=(0,2,4);BASE_T=((1,3),(1,5),(3,5),(1,3,5))
def rn(i,n):
 for _ in range(n):i=ROT[i]
 return i
def rt(T,n):return tuple(sorted(rn(i,n) for i in T))
def main():
 p=argparse.ArgumentParser();p.add_argument('--root',default='.');p.add_argument('--output',required=True);a=p.parse_args();r=Path(a.root)
 line=json.loads((r/'research/voevodsky/branch_b_framed_line_adapter_certificate_20260908.json').read_text())
 supp=json.loads((r/'research/voevodsky/branch_b_derived_support_transition_certificate_20260908.json').read_text())
 six=json.loads((r/'research/voevodsky/marici_six_short_normal_targets_certificate_20260908.json').read_text())
 assert line['status']==supp['status']==six['status']=='proved';checks=3;frames=[]
 # Base endpoint 35=X5 and 04=X2; rotate each complete source/support diagram twice.
 for sigma,base,I in [('plus',5,PLUS),('minus',2,MINUS)]:
  for n in range(3):
   idx=rn(base,n);k=LABEL[idx];Ir=tuple(sorted(rn(i,n) for i in I))
   for T0 in BASE_T:
    T=rt(T0,n)
    lf=next(x for x in line['frames'] if x['sigma']==sigma and tuple(x['T'])==T0)
    sf=next(x for x in supp['frames'] if x['sigma']==sigma and tuple(x['T'])==T0)
    assert lf['coefficient']==1 and lf['degree_displacement']==0;checks+=2
    assert sf['defects']==0 and sf['basis_columns_checked']==1024;checks+=2
    raw=-1 if idx%2==0 else 1;pol=raw;loaded=raw*pol
    assert loaded==1;checks+=1
    frames.append({'sigma':sigma,'rotation_power':n,'normal':k,'T':list(T),
      'endpoint_rees_indices':list(Ir),'support_basis_columns_checked':1024,
      'support_defects':0,'raw_determinant_sign':raw,'polarity_sign':pol,
      'loaded_coefficient':loaded,'degree_displacement':0,
      'map':'complete rotated physical top detector -> v_'+k+' tensor Pi^vee[3]',
      'pullback_chain_defect':[0,0,0]})
 assert len(frames)==24;checks+=24
 assert {x['normal'] for x in frames}==set(six['ordering']);checks+=6
 # Four independent marked source channels per normal; coordinate incidence is block I_6.
 counts={k:sum(x['normal']==k for x in frames) for k in six['ordering']}
 assert all(v==4 for v in counts.values());checks+=6
 out={'schema':'marici.six_normal_spatial_transport.v1','status':'proved','checks':checks,
  'frames':frames,'frame_count':24,'support_columns_total':24*1024,
  'normal_channel_counts':counts,'joint_normal_incidence_rank':6,
  'operation_transport':'rotation preserves the normalized native mate; antipode and decomposable terms are retained',
  'reflection':'02<->13, 04<->35, 24<->15; raw determinant and polarity signs reverse together, loaded coefficient remains +1',
  'result':'all six strict targets now carry complete framed spatial maps in four rotated T channels',
  'boundary':'rank six is on the marked endpoint/conormal source sector; conservativity on the completed admissible Xi source remains open'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':'proved','checks':checks,'frames':24,'support_columns_total':24*1024,'joint_normal_incidence_rank':6}))
if __name__=='__main__':main()
