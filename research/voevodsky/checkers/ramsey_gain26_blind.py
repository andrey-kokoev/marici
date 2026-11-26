"""Select from a fixed predecessor-only 26-vertex family by a necessary test: does some set of eight whole supports miss each blue seven at most once? Never read the 35-vertex witness to select or score a candidate. Separately audit representativeness by single-vertex extension and red-edge deletion at all roots of the stored endpoint."""
import itertools,json,sys,subprocess
from ramsey_retention_slice import D,decode,check
P=D.parent;graphs=[decode(s) for s in (P/'ramsey38_26_e73_hog.g6').read_text().splitlines()];assert all(sum(v.bit_count() for v in a)==146 and check(a,(1<<26)-1,3,8) for a in graphs)
def screen(gs,d):return list(map(int,subprocess.check_output([sys.argv[1],'7',str(d)],input='\n'.join(' '.join(map(str,a)) for a in gs)+'\n',text=True).splitlines()))
rows=[0]*len(graphs)
for d in range(4,9):
 ids=[i for i,c in enumerate(rows) if d==4 or c==d-1];
 if ids:
  vals=screen([graphs[i] for i in ids],d);assert len(vals)==len(ids)
  for i,b in zip(ids,vals):
   if b:rows[i]=d
print('blind counts',[(d,rows.count(d)) for d in sorted(set(rows))],flush=True)
a=decode(next(r['graph6'] for r in json.loads(D.read_text()) if r['l']==3 and r['k']==9));audit=[];w=[]
for root,v in enumerate(a):
 vs=[i for i in range(35) if i!=root and not v>>i&1];pr=lambda s:sum(1<<j for j,i in enumerate(vs) if s>>i&1);b=[pr(a[i]) for i in vs];I=[0]
 for i,x in enumerate(b):I.extend([s|1<<i for s in I if not s&x]);
 Q=[s for s in I if s.bit_count()==7];S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(b))];sixes=[s for s in I if s.bit_count()==6];E=[(i,j) for i in range(26) for j in range(i) if b[i]>>j&1];can_extend=sum(all(s&q for q in Q) for s in S);can_delete=sum(not any(not t&(b[i]|b[j]) for t in sixes) for i,j in E);audit.append(dict(root=root,edges=len(E),maximal_supports=len(S),sevens=len(Q),extendable_supports=can_extend,removable_edges=can_delete));w.append(b)
control=screen(w,8);assert all(control);print('control profiles',set(tuple(r.values())[1:] for r in audit));(P/'ramsey_gain26_blind.json').write_text(json.dumps(dict(capped_packing=rows,endpoint_control=audit,endpoint_screen=control))+'\n')
