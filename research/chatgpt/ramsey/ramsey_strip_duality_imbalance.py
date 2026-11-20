"""Natural antisymmetric matching signal: +1 for links only in M, -1 for links only in its row swap. Test accumulated-signal minimization among row-compatible different tracks; no eigenoperator is assumed."""
from ramsey_strip_unique_restart_memory import states,turn
flags=set.union(*(set(m) for m in states.values()))
v={q:{e:int(e in m)-int(e in turn(m)) for e in flags} for q,m in states.items()}
dot=lambda a,b:sum(a[e]*b[e] for e in flags)
print('Gram matrix for A orientations',[[dot(v[i,0],v[j,0]) for j in (2,3,5)] for i in (2,3,5)])
for history in [[(2,0)],[(2,0),(3,1)],[(5,0)]]:
    acc={e:sum(v[q][e] for q in history) for e in flags};i,b=history[-1];scores={q:sum((acc[e]+u[e])**2 for e in flags) for q,u in v.items() if q[1]!=b and q[0]!=i};print('history',history,'imbalance squared after each next state',scores)
