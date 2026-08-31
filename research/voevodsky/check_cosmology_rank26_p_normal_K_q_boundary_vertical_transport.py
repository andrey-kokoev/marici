"""Test boundary transition A -> A+2 by vertical exponent translation (i,j)->(i,j+2)."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_rank26_p_normal_K_q_boundary_vertical_transport.json'
def main():
 packets={a:json.loads((RES/f'cosmology_rank26_p_normal_K_q_boundary_signatures_a{a}.json').read_text()) for a in (12,14,16)}; comparisons={}; failures=[]
 for a,b in ((12,14),(14,16)):
  source={(r['k_pole'],*r['exponent']):r for r in packets[a]['records']};target={(r['k_pole'],*r['exponent']):r for r in packets[b]['records']};passed=0
  for (kp,i,j),r in source.items():
   t=target[(kp,i,j+2)];ok=r['signature_sha256']==t['signature_sha256'] and r['relative_total_degree']==t['relative_total_degree']
   if ok:passed+=1
   else:failures.append({'from':a,'to':b,'k_pole':kp,'source':[i,j],'target':[i,j+2]})
  comparisons[f'A{a}_to_A{b}']={'source_boundary_rows':len(source),'signature_matches':passed,'failures':len(source)-passed}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-boundary-vertical-transport.v1','status':'vertical_boundary_transition_verified' if not failures else 'vertical_boundary_transition_falsified','map':'J_A(k,i,j)=(k,i,j+2) from ambient A boundary to ambient A+2 boundary','comparisons':comparisons,'failures':failures,'decision':'Vertical multiplication by v^2 transports every normalized boundary q-lift signature across both tested ambient inclusions.' if not failures else 'Vertical translation is not a compatible boundary operator.','limitations':['single prime','pivot-selected signatures','degrees 12,14,16 only','signature compatibility is not yet a chain-homotopy proof'],'passed':not failures}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
