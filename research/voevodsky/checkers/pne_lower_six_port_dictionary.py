"""Generate lower graph from contact addresses only; apply the upper proof's independent-five disjointness test at each pole. Compare actual ports with all six-cliques (not completion certificates)."""
import json,itertools,collections
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';rows=json.loads((D/'pne_four_cover_realizations.json').read_text());out=[]
for index,r in {x['index']:x for x in rows}.items():
 C=r['contacts'];N=[set() for i in range(22)]
 def link(i,j):N[i].add(j);N[j].add(i)
 link(20,21)
 for i in range(5):link(20,i);link(21,i+5);link(i,i+5)
 for j,p in enumerate(C):
  for k in (0,1):
   for a in p[k]:link(5*k+int(a),10+j)
  for t in range(j):
   if all(set(p[k]).isdisjoint(C[t][k]) for k in (0,1)):link(10+j,10+t)
 for root in (20,21):
  S=N[root];H=set(range(22))-S-{root};F=[frozenset(t) for t in itertools.combinations(sorted(H),5) if all(b not in N[a] for a,b in itertools.combinations(t,2))];ds=[{j for j,b in enumerate(F) if a.isdisjoint(b)} for a in F];g=[{j for j,v in enumerate(ds) if i!=j and u.isdisjoint(v)} for i,u in enumerate(ds)];ports=[F.index(N[s]&H) for s in sorted(S)];hist=collections.Counter(sum(i in ds[t] for t in ports) for i in range(len(F)));assert max(hist)<=1
  def choices(c,k):
   if not k:yield ();return
   for i in c:
    tail={j for j in c if j>i and j in g[i]}
    if not ds[i]:tail.add(i)
    for rest in choices(tail,k-1):yield (i,)+rest
  pool=list(choices(set(range(len(F))),6));distinct=[q for q in pool if len(set(q))==6];need={w:6-len(N[w]&H) for w in H};passed=[q for q in pool if all(sum(w in F[t] for t in q)==need[w] for w in H)];assert tuple(sorted(ports)) in passed
  # Full independent-seven test: if J is the portion in H, every port avoiding J can join it; with root present alpha(H)<=5 suffices.
  Js=[set(j) for k in range(6) for j in itertools.combinations(H,k) if all(b not in N[a] for a,b in itertools.combinations(j,2))];good=[q for q in passed if all(len(j)+sum(j.isdisjoint(F[t]) for t in q)<=6 for j in Js)]
  out.append(dict(index=index,root=root,fives=len(F),actual=[sorted(F[t]) for t in ports],misses=dict(hist),sixCliques=len(distinct),repeatable=sum(not x for x in ds),multisets=len(pool),requiredCounts=sorted(set(need.values())),degreePassed=len(passed),degreePassedDistinct=sum(len(set(q))==6 for q in passed),sevenFree=len(good),actualSevenFree=tuple(sorted(ports)) in good,alternativeAttachments=[[sorted(F[t]) for t in q] for q in passed if q!=tuple(sorted(ports))]))
print(out[0]);print({(x['fives'],x['sixCliques'],x['repeatable']) for x in out});(D/'pne_lower_six_port_dictionary.json').write_text(json.dumps(out,indent=2)+'\n')
