"""Cross-read source executor and flag geometry, without graph colors."""
from ramsey_folded_entry_handoff import run as replay,D,json
from ramsey_flag_triangle_probe import roles,flags
from collections import defaultdict
seed=json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text());fs=seed['retained_face_cycles'];F=lambda t:'F_'+''.join(sorted(set(t)));other=lambda v:F(set('ABCD')-{v});seam=set(fs[0])&set(fs[1]);u,v,=fs[0][:2];assert {u,v}==seam and fs[1][:2]==[v,u];native=(u,F(fs[1]),v,F(fs[0]));rows=[];groups=defaultdict(lambda:defaultdict(set))
for model in replay():
    p=model['binding']
    for i,row in enumerate(model['rows']):
        b,q,r,m=[p[j] for j in roles(flags[i])];c=(b,F((b,q,r)),q,F((b,q,m)));same=any(c[k:]+c[:k]==native for k in range(4));first=row['receipt'][0];assert first[1] in (b,q) and same==(first[1]!=b);d=tuple(sorted([b,other(b)]));pred=b if same else other(b);rows.append(dict(binding=p,row=i,prefix=row['prefix'],first=first,receipt=row['receipt'],diag=d,native_order=same,mark=pred,flag_rim=c));
        for name,key in [('prefix_receipt',(i,tuple(row['receipt']))),('prefix_diagonal',(i,d)),('first_diagonal',(first,d)),('diagonal_only',d)]:groups[name][key].add(same)
out=dict(rows=rows,ambiguities={k:[sum(len(s)>1 for s in g.values()),len(g)] for k,g in groups.items()});print(out['ambiguities'],[(r['binding'],r['row'],r['first'],r['mark']) for r in rows]);(D/'ramsey_execution_rim_bit.json').write_text(json.dumps(out,indent=2)+'\n')
