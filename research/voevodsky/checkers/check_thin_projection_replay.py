"""Thin reachability projection cannot invert fine rotation replay."""
from functools import lru_cache
from pathlib import Path
import json
@lru_cache(None)
def trees(s):
 if len(s)==1:return (s[0],)
 return tuple((a,b) for i in range(1,len(s)) for a in trees(s[:i]) for b in trees(s[i:]))
def rot(t):
 if isinstance(t,str):return set()
 x,y=t;out=set()
 if isinstance(x,tuple):out.add((x[0],(x[1],y)))
 out|={(z,y) for z in rot(x)}|{(x,z) for z in rot(y)}
 return out
v=set(trees(tuple('abcde')))
@lru_cache(None)
def paths(a,b):
 if a==b:return ((a,),)
 return tuple((a,)+tail for mid in rot(a) for tail in paths(mid,b))
start=(((('a','b'),'c'),'d'),'e');end=('a',('b',('c',('d','e'))))
all_paths=paths(start,end);assert len(all_paths)==9 and len(set(all_paths))==9
roots=tuple('abcde')
def project(path,source_roots):
 if tuple(source_roots)!=roots:raise PermissionError('MISSING_LEAF_ROOT')
 assert path and all(y in rot(x) for x,y in zip(path,path[1:]))
 return (path[0],path[-1])
images={project(p,roots) for p in all_paths};assert images=={(start,end)}
def choose_section(arrow):
 candidates=paths(*arrow)
 return min(candidates,key=repr) if candidates else None
chosen=choose_section((start,end));assert chosen in all_paths
assert sum(choose_section(project(p,roots))==p for p in all_paths)==1
assert project(chosen,roots)==(start,end)
try:project(chosen,roots[:-1])
except PermissionError:missing_refused=True
else:raise AssertionError('missing primitive root admitted')
report={'passed':True,'fine_paths_at_extreme_pair':len(all_paths),'thin_arrows_at_extreme_pair':len(images),'any_set_section_cannot_recover_all_nine':True,'chosen_section_recovers_exactly_one':True,'missing_root_refused':missing_refused,'control_law':'public_reachability factors through projection; exact_rotation_replay does not','scope':'Finite five-leaf free path graph to thin Tamari reachability. Set-theoretic section is not claimed functorial or historical reconstruction; no analytic role map.'}
out=Path(__file__).resolve().parents[1]/'results/thin-projection-replay.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
