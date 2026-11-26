"""Audit staged coverage: all labeled pair graphs accounted for, every generated branch present exactly once in the next layer, status totals and degrees of the last candidates."""
from ramsey_unsaturated_ten import P,json,graphs,ig,collections
from ramsey_eleven_coverage import count
src=[json.loads((P/f'ramsey_unsaturated_ten_{k}.json').read_text()) for k in range(5)];gs=graphs(10);n=count(0,10,(0,)*8);assert n==sum(40320//ig.Graph(8,e).count_automorphisms() for e in gs);want={(i,()) for i in range(len(gs))};rows=[]
for rs in src:
 keys={(r['i'],tuple(r['pr'])) for r in rs};assert want==keys and len(keys)==len(rs);want={(r['i'],tuple(r['pr']+[s])) for r in rs for s in r.get('children',[])};rows.append(dict(branches=len(rs),unknown=sum(r.get('unknown',0) for r in rs)))
z=src[-1];hist=sum((collections.Counter(r['hist']) for r in z),collections.Counter());assert not any(r['win'] for r in z) and set(hist)<={'unsat4','forced4'};data=dict(labeled=n,layers=rows,marked_quartets_with_completion=sum(bool(r['complete']) for r in z),marked_full=sum(r['complete'] for r in z),full_status=hist,last_graphs={i:sorted(ig.Graph(8,gs[i]).degree()) for i in sorted({r['i'] for r in z if r['complete']})});print(data);(P/'ramsey_ten_coverage.json').write_text(json.dumps(data)+'\n')
