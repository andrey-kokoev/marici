"""Scout finite verified-zero dominance over any unverified zero tail."""
import json,math
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.special import logsumexp
mp.mp.dps=40
ZEROS=np.array([float(mp.im(mp.zetazero(k))) for k in range(1,101)])
H=math.floor(ZEROS[-1]); TS=np.geomspace(.7,3,80);XS=np.linspace(0,110,1101)
# Deliberately crude unit-bin multiplicity bound: number in [k,k+1] <= (k+1)log(k+1).
KS=np.arange(H,501,dtype=float);LOGCOUNT=np.log((KS+1)*np.log(KS+1));worst=None;rows=[]
for t in TS:
 gm=ZEROS[:,None];xx=XS[None,:]
 low_terms=np.concatenate((-t*(gm-xx)**2,-t*(gm+xx)**2),axis=0)-math.log(2)
 log_lower=logsumexp(low_terms,axis=0)
 # Any zero has |beta-1/2|<=1/2. Overcount every unit bin by N(k+1).
 tail_terms=[]
 for x in XS:
  lp=LOGCOUNT+t/4-t*np.minimum((KS-x)**2,(KS+x)**2)
  # Factor 2 covers both signs/shifts and another factor 2 is retained as slack.
  tail_terms.append(logsumexp(lp)+math.log(4))
 log_tail=np.array(tail_terms);gap=log_lower-log_tail;i=int(np.argmin(gap));row={'t':float(t),'minimum_log_dominance':float(gap[i]),'minimizer_xi':float(XS[i]),'all_dominated':bool(np.all(gap>0))};rows.append(row)
 if worst is None or row['minimum_log_dominance']<worst['minimum_log_dominance']:worst=row
out={'schema':'marici.verified-zero-dominance-expanded-scout.v1','certified':False,'verified_zero_count_candidate':len(ZEROS),'last_ordinate':float(ZEROS[-1]),'tail_bins_start':H,'grid':{'t':[float(TS[0]),float(TS[-1]),len(TS)],'xi':[0,25,len(XS)]},'worst':worst,'all_grid_dominated':all(r['all_dominated'] for r in rows),'rows':rows,'limitations':['mpmath zeros are not rigorous zero verification certificates','unit-bin zero-count inequality must be replaced by a cited explicit bound','grid is not a continuum proof']};(Path(__file__).parents[1]/'results'/'verified-zero-dominance-expanded-scout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'last_zero':ZEROS[-1],'worst':worst,'all':out['all_grid_dominated']},indent=2))
