"""Learn one odd-bridge template per normalized turn word; predict named bridges by relabeling the prefix, without constructing its remainder. Check against independently deleting each edge of each target remainder."""
from itertools import permutations
from collections import Counter
from ramsey_strip_prefix_geometry import N,result,labels,rep,r,P,T
from ramsey_strip_prefix_odd_cuts import component

def lift(word):
 p=[0 if word[0]=='A' else 14]
 for name in word.split():p.append(min(y for y in N[p[-1]] if labels.get(rep(y))==name))
 return tuple(p)
def truth(p):
 used=set()
 for i,(x,y) in enumerate(zip(p,p[1:])):used.update((x,y) if i%2==0 else (r[x],r[y]))
 rem=set(range(30))-used;g={x:N[x]&rem for x in rem};return frozenset((x,y) for x in rem for y in g[x] if x<y and (c:=component(x,g,(x,y))) and y not in c and len(c)%2)
def action(p):
 f=lambda d:tuple(sorted(p[i] for i in d));return [P.index(f(d)) for d in P]+[15+T.index(tuple(sorted(map(f,t)))) for t in T]
G=[a for p in permutations(range(6)) if all((a:=action(p))[r[i]]==r[a[i]] for i in range(30))];assert len(G)==16
examples=['A a0 d0 D d1 c1 C','A a0 d0 c0 C c1 d1','A a0 d0 c0 C c1 b1','A a0 d0 c0 b0 B b1'];ref=[lift(w) for w in examples];templates=list(map(truth,ref));tested=Counter();
for (_,_,ok),words in result.items():
 if not ok:continue
 for w in words:
    for flip in (False,True):
        p=tuple(r[x] if flip else x for x in lift(w));s=[labels[rep(x)] for x in p[1:]];first=next(i for i,n in enumerate(s[1:],2) if len(n)==1);typ={4:0,5:1 if s[-1][0]==s[2][0] else 2,6:3}[first];maps=[a for a in G if tuple(a[x] for x in ref[typ])==p];assert len(maps)==1;f=maps[0];pred={(f[x],f[y]) for x,y in templates[typ]};assert pred==truth(p);tested[typ]+=1
print('templates, named bridges, orientation checks');
for i in range(4):print(examples[i],sorted(templates[i]),tested[i]);
