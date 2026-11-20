"""Recover marks as a minimum rim-symmetric separator. Hold the exit out; isolate the entry and require that the remaining two connected components be exchanged by rim interchange. Do not consult routes, closure or profile data until the final cross-check."""
from itertools import combinations
from ramsey_strip_prism_proof import labels,E
V=set(labels.values());N={v:{b if a==v else a for a,b in E if v in (a,b)} for v in V};flip=lambda v:v if len(v)==1 else v[0]+str(1-int(v[1]))
def readers(entry,exit):
    U=V-{entry,exit}
    for k in range(len(U)+1):
        hits=[]
        for sel in combinations(sorted(U),k):
            S=set(sel)
            if {flip(v) for v in S}!=S or not N[entry]<=S:continue
            todo=U-S;cc=[]
            while todo:
                q=[todo.pop()];
                for x in q:
                    new=N[x]&todo;todo-=new;q.extend(new)
                cc.append(set(q))
            if len(cc)==2 and {flip(v) for v in cc[0]}==cc[1]:hits.append(S)
        if hits:return hits
m=[readers('A','D'),readers('D','A')];assert m==[[{'a0','a1','B','C'}],[{'d0','d1','B','C'}]]
from ramsey_strip_mixed_mod_holdout import rules,dist
for (S,),rule in zip(m,rules):assert S=={name for v,name in labels.items() if tuple(dist[v][i] for i in (0,15,9,29)) in rule}
print('unique minimum readers:',m)
