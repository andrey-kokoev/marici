#!/usr/bin/env python3
"""Show nonunit paired-Pfaffian correspondence has empty and multiple fibers."""

import json
from pathlib import Path

def solutions(mod,rho,rhs):return [x for x in range(mod) if rho*x%mod==rhs%mod]
def main():
 multiple=solutions(6,2,2);empty=solutions(6,2,1)
 assert multiple==[1,4] and empty==[]
 # Geometric coordinates from one common rest parameter always satisfy.
 geometric=[]
 for rest in range(6):
  old=rest*2%6;new=rest*1%6
  assert 2*new%6==old
  geometric.append({'rest':rest,'old_torsion':old,'new_torsion':new})
 result={'schema':'marici.coherence.nonunit-pfaffian-correspondence-fibers.v1','ring':'Z/6','multiple_fiber':{'equation':'2 tau_new = 2','solutions':multiple},'empty_fiber':{'equation':'2 tau_new = 1','solutions':empty},'geometric_common-rest_pairs':geometric,'conclusion':'without localizing rho, the refinement relation is neither a function nor a surjective correspondence over arbitrary line coordinates'}
 Path(__file__).with_name('nonunit-pfaffian-correspondence-fibers.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
