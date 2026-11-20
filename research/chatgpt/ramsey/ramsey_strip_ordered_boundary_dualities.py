"""Compare same-row and other-row endpoint identifications by the orders of their extending cage dualities. No closure data used to select a duality. Mark the first entry as in the row-exit test. Test all source/target row ports simultaneously."""
from collections import Counter
from ramsey_strip_complete_stitch_duality import solutions,s,t,r
from ramsey_strip_shortcut_row_exit import rows,X,P,T,edge,pair,paths,phase
B=rows[0].index('B');Q,=[i for i,ab in enumerate(zip(*rows)) if ab==('N','N')];entry=[];exit=[]
for w in rows:
    U=w.index('R');match=pair(edge(B,Q),edge(U,Q));j,=[j for j,m in enumerate(T,15) if P[s] in m and match in m];entry.append(j);exit.append(P.index(pair(edge(B,U),edge(*[i for i,x in enumerate(w) if x=='N']))))
assert entry[1]==r[entry[0]] and exit[1]==r[exit[0]];H=Counter()
for f in solutions:
    a=exit.index(f[entry[0]]);b=entry.index(f[exit[0]]);square=[f[f[i]] for i in range(30)];order=2 if square==list(range(30)) else 4;assert square==(list(range(30)) if a==b else r);H[a,b,order]+=1
    changed=0
    for z in paths.values():
        p=z['path'];h=[f[i] for i in reversed(p)];changed+=phase(p,rows)!=phase(h,rows)
    assert changed==(0 if a==b else len(paths));print('entry->exit shift',a,'exit->entry shift',b,'order',order,'row phase changed',changed)
assert H==Counter({(0,0,2):1,(1,1,2):1,(0,1,4):1,(1,0,4):1});print('literal ports',entry,exit)
