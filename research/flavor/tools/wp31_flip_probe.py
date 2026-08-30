import json, math, sys
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0,'checkers')
from wp25_center_selection import mask_slots, tex_key
from wp7_ensemble import build_texture, observables17, CENTRAL, SIGMA

w27=json.load(open('results/wp27_natural_k.json'))
wp20=json.load(open('results/wp20_valley_audit.json'))
keys=[x if isinstance(x,str) else x.get('key') for x in w27['singular']]

def resid_factory(mu,md,pe):
    def resid(theta):
        Yu,Yd=build_texture(mu,md,pe[0],(int(pe[1]),int(pe[2])),theta)
        with np.errstate(all='ignore'):
            obs=observables17(Yu,Yd)
        obs=np.where(np.isfinite(obs),obs,1.0e6)
        return (obs-CENTRAL)/SIGMA
    return resid

results=[]
for k in keys:
    mu_s,md_s,pe=k.split('_',2)
    mu,md=int(mu_s),int(md_s)
    us,ds=mask_slots(mu),mask_slots(md)
    wsec = 'd' if mu_s in ('267','275','281','282') else 'u'
    slots = ds if wsec=='d' else us
    base = len(us) if wsec=='d' else 0
    i01 = base + slots.index((0,1)); i10 = base + slots.index((1,0))
    resid=resid_factory(mu,md,pe)
    recs=[r for r in wp20['records'] if tex_key(*r['member'],r['phase_edge'])==k]
    for ri,r in enumerate(recs):
        th=r['log_mags'][:]; ph=r['phi_raw']
        sign0='+' if th[i10]>th[i01] else '-'
        # flipped start: swap the transpose-pair values, negate phi
        tf=th[:]; tf[i01],tf[i10]=th[i10],th[i01]
        t0=np.concatenate([tf,[-ph]])
        lb=np.concatenate([np.array(th)-8.0*math.log(10),[-math.pi]])
        ub=np.concatenate([np.array(th)+8.0*math.log(10),[math.pi]])
        try:
            s1=least_squares(lambda t: resid(t)[:6], t0, bounds=(lb,ub), max_nfev=8000)
            s2=least_squares(resid, s1.x, bounds=(lb,ub), method='trf',
                             xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=50000)
            xf=s2.x
            sign1='+' if xf[i10]>xf[i01] else '-'
            Yu,Yd=build_texture(mu,md,pe[0],(int(pe[1]),int(pe[2])),xf)
            obs_new=observables17(Yu,Yd)
            th0=np.concatenate([th,[ph]])
            Yu0,Yd0=build_texture(mu,md,pe[0],(int(pe[1]),int(pe[2])),th0)
            obs0=observables17(Yu0,Yd0)
            dobs=float((np.abs(obs_new-obs0)/SIGMA).max())
            results.append(dict(key=k,min_idx=ri,wsec=wsec,sign0=sign0,
                chi2_orig=r['chi2_stored'],chi2_flip=float(2*s2.cost),
                sign_flip=sign1,phi_flip=float(xf[9]),dobs_sigma=dobs))
            print(k,ri,'start',sign0,'-> flip lands',sign1,
                  'chi2 %.4f -> %.4f'%(r['chi2_stored'],2*s2.cost),
                  'dobs/sigma %.2e'%dobs, flush=True)
        except Exception as e:
            print(k,ri,'FAILED',e, flush=True)
            results.append(dict(key=k,min_idx=ri,wsec=wsec,sign0=sign0,failed=str(e)))
json.dump(results,open('tools/wp31_flip_probe.json','w'),indent=1)
