#!/usr/bin/env python3
"""Resumable high-precision scalar gamma-tail moments at R=250."""
import json,sys
from pathlib import Path
try: import mpmath as mp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp
start=int(sys.argv[1]);stop=int(sys.argv[2]);mp.mp.dps=70;R=mp.mpf(250);omega=mp.mpf('1.1');root=Path(__file__).parents[1]/'results';d=json.loads((root/'digamma_real_asymptotic_coefficients.json').read_text());corr={int(k):mp.mpf(v) for k,v in d['coefficients'].items()}
def E(q):return (-1j*omega)**(q-1)*mp.gammainc(1-q,-1j*omega*R,mp.inf)
def plainpow(k):return R**(1-k)/(k-1)
def logplain(k):return R**(1-k)*(mp.log(R/(2*mp.pi))/(k-1)+1/(k-1)**2)
def logosc(k):return -mp.diff(E,k)-mp.log(2*mp.pi)*E(k)
out={}
for k in range(start,stop):
 z=logosc(k)+sum(c*E(k+j) for j,c in corr.items())
 out[str(k)]={'plain':mp.nstr(logplain(k)+sum(c*plainpow(k+j) for j,c in corr.items()),80),'cos':mp.nstr(mp.re(z),80),'sin':mp.nstr(mp.im(z),80)}
p=root/f'gamma_tail_moments_250_{start}_{stop-1}.json';p.write_text(json.dumps({'schema':'marici.voevodsky.gamma-tail-moment-chunk.v1','R':250,'precision_digits':70,'start':start,'stop_exclusive':stop,'moments':out,'passed':True},indent=2)+'\n');print(json.dumps({'start':start,'stop':stop,'count':len(out),'path':str(p)},indent=2))
