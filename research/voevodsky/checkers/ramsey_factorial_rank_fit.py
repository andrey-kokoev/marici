"""Same data and split as band-position fit; fixed versus fitted factorial effects."""
import json,math,numpy as np
from ramsey_band_position_fit import x,y,train,band,D
base=x[:,:3];d=x[:,4];s=x[:,5];lf=np.array([math.lgamma(v+1) for v in d]);w=s/np.maximum(d,1);out={}
for name,z,coef in [('base',lf,0),('multiply_d!',lf,1),('divide_d!',lf,-1),('power_of_d!',lf,None),('ramp_log_factorial',w*lf,None),('ds',d*s,None)]:
    X=base if coef is not None else np.column_stack([base,z]);offset=z*(coef or 0);b=np.linalg.lstsq(X[train],(y-offset)[train],rcond=None)[0];e=X@b+offset-y;out[name]=dict(exponent=float(coef if coef is not None else b[-1]),stats={});
    for group,mask in [('train',train),('test',~train),('rank4or5',~train&(d>=4)),('test_band',~train&band)]:out[name]['stats'][group]=dict(n=int(mask.sum()),rms=float(np.mean(e[mask]**2)**.5),typical_factor=float(np.exp(np.median(abs(e[mask])))))
    print(name,out[name]['exponent'],[round(v['rms'],5) for v in out[name]['stats'].values()])
(D/'ramsey_factorial_rank_fit.json').write_text(json.dumps(out,indent=2)+'\n')
