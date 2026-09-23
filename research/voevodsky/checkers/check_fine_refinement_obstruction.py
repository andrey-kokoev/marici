"""Capability obstruction, exact-section control, and archive identity boundary."""
from pathlib import Path
from fractions import Fraction as Q
from copy import deepcopy
import json,sys
from verify_fine_refinement_obstruction import verify
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima/results';OUT=ROOT/'research/voevodsky/results'
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from verify_scalar_envelope_band import envelopes,value,check

def source(p,q,h):
 d=Q(1,128**4);r=[Q(1,128**j) for j in range(4)];center=(50,51,52,53)
 a=50+d*h;b=Q(51);u=206+d*p-a-b
 v=sum(x*y for x,y in zip(center,r))+d*q-a-r[1]*b
 t2=(v-r[3]*u)/(r[2]-r[3]);return (a,b,t2,u-t2)
def main():
 expected={'family':'owning-m4-moment-curve-two-history-v1','n':18,
 'continuation':'append-fine-upper-then-exact-point-admission','h_upper':'1/2'}
 lower,_=envelopes(18);point=(Q(1),Q(1));plane=max(lower,key=lambda a:value(a,point));assert value(plane,point)==1
 packet={'expected':deepcopy(expected),'public_point':['1','1'],
 'A_lower_plane':list(map(str,plane)),'A_farkas_weights':['1','1'],'A_combined_upper':'-1/2',
 'B_source_witness':list(map(str,source(*point,Q(0))))}
 result=verify(expected,packet)
 rejected=[]
 for mode in ('wrong-operation','false-emptiness','bad-positive-witness','non-source-plane','wrong-family'):
  bad=deepcopy(packet)
  if mode=='wrong-operation':bad['expected']['h_upper']='1'
  elif mode=='false-emptiness':bad['A_combined_upper']='0'
  elif mode=='bad-positive-witness':bad['B_source_witness'][0]='-1'
  elif mode=='non-source-plane':bad['A_lower_plane']=['0','0','2']
  else:bad['expected']['n']=6
  try:verify(expected,bad)
  except (AssertionError,ValueError):rejected.append(mode)
  else:raise AssertionError('invalid obstruction accepted')
 # Tightening eta is NOT an impossibility of shared lifting: eta=0 has a
 # whole-domain common section, independently checked here.
 packets=json.loads((N/'scalar-envelope-band-packets.json').read_text())
 exact=next(p for p in packets if p['request']=={'n':18,'eta':'0'})
 exact_metrics=check({'n':18,'eta':'0'},exact)
 # Logical archive accounting, not an authenticated archive implementation:
 # a family archive supplies both answers; selecting the actual one needs a bit.
 alternatives={name:result[name+'_admits_point'] for name in ('A','B')}
 assert set(alternatives.values())=={False,True}
 report={'passed':True,'obstruction_packet':packet,'verified_conclusion':result,
 'zero_tolerance_common_section':exact_metrics,
 'archive_boundary':{'family_archive_answers':alternatives,'history_selector_bits_required_for_two_branches':1,
 'identity_free_resolution':'Return ambiguity or refuse; cannot reconstruct the actual history from a common section.'},
 'rejections':rejected,
 'scope':'Exact semantic obstruction for a newly requested fine continuation. Not a failed-selector claim, implemented split protocol, archive authentication or total-storage theorem.'}
 (OUT/'fine-refinement-obstruction.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'conclusion':result,'zero_tolerance_section_cells':exact_metrics['cells'],'rejections':len(rejected)},indent=2))
if __name__=='__main__':main()
