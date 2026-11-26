"""Split d by band position or into balanced halves, before seeing holdout. Test normalized factorial sum (neutral at d=0 and d=1)."""
from ramsey_band_position_fit import x,y,train,band,D
import numpy as np, math, json
base=x[:,:3];d=x[:,4].astype(int);s=x[:,5].astype(int);out={}
for split,j in [('position',s),('balanced',d//2)]:
 z=np.array([math.log((math.factorial(int(u))+math.factorial(int(v-u)))/2) for u,v in zip(j,d)])
 for typ,c in [('multiply',1),('divide',-1),('fit',None)]:
    X=base if c is not None else np.column_stack((base,z));offset=(c or 0)*z;b=np.linalg.lstsq(X[train],(y-offset)[train],rcond=None)[0];e=X@b+offset-y;key=split+'_'+typ;out[key]=dict(exponent=c if c is not None else float(b[-1]),stats={});
    for group,mask in [('train',train),('test',~train),('test_band',~train&band),('new_depth',~train&(d>=4))]:out[key]['stats'][group]=dict(n=int(mask.sum()),rms=float(np.sqrt(np.mean(e[mask]**2))),median_factor=float(np.exp(np.median(abs(e[mask])))))
    print(key,out[key]['exponent'],[(g,round(v['rms'],4)) for g,v in out[key]['stats'].items()])
(D/'ramsey_split_factorial_fit.json').write_text(json.dumps(out,indent=2)+'\n')
