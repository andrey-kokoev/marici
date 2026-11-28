"""External diagnostic, not a second chance to select a candidate on core 6."""
from r37_excel_extension_trial import D,candidates,json,combinations
from collections import Counter,defaultdict
cores=json.loads((D/'results/ramsey_37_catalogue_free.json').read_text())['certificates'];L=candidates();stat=Counter();first={};width=[]
for rule in L:
 groups=defaultdict(set)
 for t,v in rule:groups[t].add(v)
 width.append(max(map(len,groups.values())))
for idx,c in enumerate(cores):
 a=c['core'];order=sorted(range(16),key=lambda i:(a[i].bit_count(),i));blue=lambda t:all(not(a[i]>>j&1) for i,j in combinations(t,2));fives=[s for s in combinations(range(16),5) if blue(s)];tri={t for s in fives for t in combinations(s,3)};quad={t for s in fives for t in combinations(s,4)}
 if not any(blue(q) and q not in quad and any(t in tri for t in combinations(q,3)) for q in combinations(range(16),4)):continue
 for k,rule in enumerate(L):
  for control in (0,1):
   bind=lambda i:order[(i-1)^control];usable=[]
   for t,v in rule:
    s=tuple(sorted(map(bind,t)));u=bind(v);q=tuple(sorted((*s,u)))
    if blue(q):usable.append((s,u,s in tri and q not in quad))
   prefix=(k,control);stat[prefix,'cases']+=1;stat[prefix,'nonempty']+=bool(usable);stat[prefix,'first success']+=bool(usable and usable[0][2]);stat[prefix,'any true']+=any(x[2] for x in usable);stat[prefix,'hits']+=sum(x[2] for x in usable);stat[prefix,'attempts']+=len(usable)
   for s,u,ok in usable:
    if ok:first.setdefault(prefix,(idx,s,u))
print('max distinct nominated sites per triple',width)
for p in [(k,c) for k in range(3) for c in (0,1)]:print(p,[stat[p,m] for m in ('cases','nonempty','first success','any true','hits','attempts')],first.get(p))
