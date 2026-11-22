"""Exact Z/6 phase arithmetic, exponent of exp(i*pi/3); omega=exp(2*pi*i/3). Source eigenlines independently checked against K using omega^2+omega+1=0."""
from itertools import permutations
from pathlib import Path
import json
D=Path(__file__).parent;load=lambda p:json.loads(p.read_text());seed=load(D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json');E=[''.join(e) for e in seed['arrows']];phase=dict(AB=0,BC=3,CA=1,BA=3,AD=0,DB=4);assert set(E)==set(phase);roots=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def step(v):return {e:sum(v[t] for t in E if t[1]==e[0]) for e in E}
def delta(e):return {t:int(e==t) for t in E}
seam=[e for e in E if e[::-1] in E];ends=set(''.join(seam));entry=[e for e in E if e[1] in ends and e[0] not in ends];assert sorted(entry)==['CA','DB'];controls={}
for e in seam:
    v=step(step(delta(e)));controls[e]={t:n for t,n in v.items() if n};assert [t for t in entry if v[t]]==[next(t for t in entry if t[1]==e[0])]
syms=[]
for p in permutations('ABCD'):
    op=lambda e:''.join(p['ABCD'.index(i)] for i in e)
    if set(map(op,E))!=set(E):continue
    offs={(phase[op(e)]-phase[e])%6 for e in E};assert len(offs)==1 and all((a[1]==b[0])==(op(a)[1]==op(b)[0]) for a in E for b in E);syms.append(dict(vertices=''.join(p),phase_offset=offs.pop(),entry_image=list(map(op,entry))))
assert len(syms)==2
for sign in (1,-1):
    for e in E:
        incoming=[roots[(sign*phase[t])%6] for t in E if t[1]==e[0]];assert tuple(map(sum,zip(*incoming)))==roots[(sign*(phase[e]+2))%6]
obs=load(D/'ramsey_execution_rim_bit.json')['rows'];checks=[]
for row in obs:
    s=row['binding'][0];ref,=[e for e in seam if e[0]==s];t=row['first'];diff=(phase[t]-phase[ref])%6;sig=1 if diff in (0,1,5) else -1;arr=t[1]==s;assert (sig==1)==arr;checks.append(dict(row=row['row'],binding=row['binding'],reference=ref,first=t,ratio_real_sign=sig,stationary_arrival=arr))
r=dict(symmetries=syms,two_steps=controls,both_seam_inputs={t:sum(controls[e].get(t,0) for e in seam) for t in entry},phase_checks=checks);print(r);(D/'ramsey_seam_launch_mode.json').write_text(json.dumps(r,indent=2)+'\n')
