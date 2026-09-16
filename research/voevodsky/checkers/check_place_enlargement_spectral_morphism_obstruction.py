"""Exact scalar hostiles for threshold transport under place enlargement."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def update(e,a,k,w):return (e*a+w)/(e+k)
# Reinforcement creates positive new spectrum from the old radical.
reinforce={'e':F(1),'a':F(0),'k':F(1),'w':F(1)};reinforce['a_new']=update(**reinforce)
# Cancellation sends positive old spectrum into the new radical.
cancel={'e':F(2),'a':F(1,2),'k':F(1),'w':F(-1)};cancel['a_new']=update(**cancel)
checks={'reinforcement_old_radical':reinforce['a']==0,'reinforcement_new_positive':reinforce['a_new']>0,'cancellation_old_positive':cancel['a']>0,'cancellation_new_radical':cancel['a_new']==0,'energy_weights_positive':reinforce['e']+reinforce['k']>0 and cancel['e']+cancel['k']>0}
out={'schema':'marici.voevodsky.place-enlargement-spectral-morphism-obstruction.v1','update':'a_new=(e*a+w)/(e+kappa)','reinforcement_fixture':{k:str(v) for k,v in reinforce.items()},'cancellation_fixture':{k:str(v) for k,v in cancel.items()},'checks':checks,'all_exact':all(checks.values()),'conclusion':'No positive threshold-control function can make every place enlargement a morphism between the scalar |a_S| spectral towers.','replacement':'Use the strict orthogonal local-energy row inclusion as a correspondence, then apply the stage-dependent scalar boundary readout.'}
if __name__=='__main__':
 p=ROOT/'results'/'place-enlargement-spectral-morphism-obstruction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
