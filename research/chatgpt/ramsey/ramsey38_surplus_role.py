"""Read roles from rooted red adjacency, not stored label numbers; decompose the five-neighbour gain by structural profiles across all inputs."""
from ramsey38_relative_query import families,data,C,J,D,ls,comb,json,Counter
rows=[]
for i,(h,_,_) in enumerate(data):
 N=h[0];profile={v:(N&h[v]) for v in range(27) if v and not N>>v&1};Q,={a for a in profile.values() if a.bit_count()==4};pairs={a for a in profile.values() if a.bit_count()==2};missing={1<<x|1<<y for x,y in comb(ls(N),2)}-pairs;z,=[v for v in ls(N) if not any(a>>v&1 for a in missing)];pred={tuple(sorted((z,v))) for v in ls(N&~Q&~(1<<z))};counts=[]
 for j in [C[i],J[i]]:
  counts.append(Counter(((x,y),s.bit_count()) for x,y,F in families(j) for s in F if not any(h[v]&s for v in ls(s))))
 l,b=sorted(counts,key=lambda c:sum(c.values()));delta={k:b[k]-l[k] for k in l.keys()|b.keys() if b[k]!=l[k]};assert delta=={(d,5):2 for d in pred};rows.append(dict(input=i,singleton=z,four_address=ls(Q),predicted_pairs=sorted(pred),five_counts=[[l[d,5],b[d,5]] for d in sorted(pred)]))
o=dict(inputs=rows,all_other_pair_size_deltas_zero=True);print(rows[0],len(rows));(D/'ramsey38_surplus_role.json').write_text(json.dumps(o,indent=2)+'\n')
