"""Exact greedy imbalance dynamics. Detect recurrence of (current oriented track, accumulated signed vector), not merely recurrence of track."""
from ramsey_strip_duality_imbalance import v,flags,dot
keys=sorted(flags)
def run(start,exclude_current=True):
    current=(start,0);a=dict(v[current]);seq=[current];norms=[dot(a,a)];seen={ (current,tuple(a[e] for e in keys)):0 };log=[]
    for _ in range(100):
        choices={q:sum((a[e]+u[e])**2 for e in keys) for q,u in v.items() if q[1]!=current[1] and (not exclude_current or q[0]!=current[0])};best=[q for q,k in choices.items() if k==min(choices.values())];log.append(choices)
        if len(best)!=1:return seq,norms,('tie',best),log
        current,=best;a={e:a[e]+v[current][e] for e in keys};seq.append(current);norms.append(dot(a,a));state=current,tuple(a[e] for e in keys)
        if state in seen:return seq,norms,('cycle starts',seen[state],'period',len(seq)-1-seen[state]),log
        seen[state]=len(seq)-1
    raise AssertionError('no recurrence within bound')
for excluded in (True,False):
    for start in (2,3,5):
        seq,norms,result,log=run(start,excluded);print('exclude same track',excluded,'start',start,'sequence',seq,'norms',norms,'result',result)
