"""Count possible targets and compare all chart proposals with same-triple alternatives."""
from r37_excel_extension_trial import D,candidates,json,combinations
from collections import Counter
rules=list(map(set,candidates()));cores=json.loads((D/'results/ramsey_37_catalogue_free.json').read_text())['certificates'];tot=Counter()
for idx,rec in enumerate(cores):
 a=rec['core'];o=sorted(range(16),key=lambda i:(a[i].bit_count(),i));blue=lambda q:all(not (a[o[i-1]]>>o[j-1]&1) for i,j in combinations(q,2));cols=range(1,17);five=[q for q in combinations(cols,5) if blue(q)];supported={t for q in five for t in combinations(q,3)};extend={u for q in five for u in combinations(q,4)};events={(t,v):u not in extend for u in combinations(cols,4) if blue(u) for v in u for t in [tuple(x for x in u if x!=v)] if t in supported};row=[]
 for k,L in enumerate(rules):
    hit=events.keys()&L;triples={t for t,v in hit};ctrl=[v for (t,p),v in events.items() if t in triples and (t,p) not in L];row.append((sum(events[x] for x in hit),len(hit),sum(ctrl),len(ctrl)))
 if idx in [6,7,8,23,38]:print(idx,'targets',sum(events.values()),'of',len(events),'in rule / same triple controls',row)
 tot['cores with targets']+=any(events.values());tot['targets']+=sum(events.values())
print(tot)
