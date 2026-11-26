"""Log-gain fit on the inner 13 square, fixed coefficients on outer 26 shell. Canonical orientation l<=k. Equal branches have all band features zero."""
import csv,math,statistics,json
from pathlib import Path
import numpy as np
D=Path(__file__).resolve().parents[1]/'results';r={(int(z['l']),int(z['k'])):z['first_difference'] for z in csv.DictReader((D/'ramsey_path_power_tensor_grid_26.csv').open())};rows=[]
for z in csv.DictReader((D/'ramsey_mixed_field_26.csv').open()):
 a,b=int(z['l']),int(z['k']);
 if not 3<=a<=b:continue
 depth=r[a,b];d=int(depth) if depth!='=' else 0;s=b-(d*(a-1)+1+int(d==a)) if d else 0;assert 0<=s<=d
 rows.append((a,b,d,s,math.log(int(z['D_v1'])),[1,math.log(math.comb(a+b-4,a-2)),a-2,int(d>0),d,s,d*s,d*(d-1)/2]))
x=np.array([t[-1] for t in rows]);y=np.array([t[4] for t in rows]);train=np.array([b<=13 for _,b,*_ in rows]);band=x[:,3]>0;results={}
for name,ix in {'base':[0,1,2],'indicator':[0,1,2,3],'rank':[0,1,2,3,4],'rank_squared':[0,1,2,3,4,7],'interaction_only':[0,1,2,6],'rank_position':[0,1,2,3,4,5],'rank_position_interaction':[0,1,2,3,4,5,6]}.items():
 X=x[:,ix];beta=np.linalg.lstsq(X[train],y[train],rcond=None)[0];err=X@beta-y;stats={}
 for key,m in [('train',train),('test',~train),('test_numbered',~train&band),('test_equal',~train&~band)]:
    e=err[m];stats[key]=dict(n=len(e),rms=float(np.sqrt(np.mean(e*e))),typical_factor=math.exp(float(np.median(abs(e)))))
 results[name]=dict(coefficients=beta.tolist(),stats=stats);print(name,*(round(v['rms'],5) for v in stats.values()),'factor',round(stats['test']['typical_factor'],4),'coef',beta[-1])
(D/'ramsey_band_position_fit.json').write_text(json.dumps(results,indent=2)+'\n')
