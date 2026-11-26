"""Blind two-copy incidence constructor. Pair core vertices and label involution (no stored endpoint). Draw 11 pairs of size-2 masks and 2 pairs of size-3 masks. Equal label marginals by shuffled stubs; repeated masks allowed. Search all involution-invariant red completions with the prescribed degrees. A blue clique in core must have >= as many labels in its union and size <=7. Add violating cliques lazily; finite budgets are not exclusions. Local neighbor-label matchings are necessary by Hall."""
import json,collections,random,sys,itertools
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from ramsey_retention_slice import D,check
P=D.parent;F=(1<<26)-1;rng=random.Random(351326);swap=lambda s:((s&85)<<1)|((s&170)>>1)
def draw():
 while True:
  st=[i for i in range(4) for _ in range(7)];rng.shuffle(st);m=[];p=0
  for d in [3]*2+[2]*11:
   g=st[p:p+d];p+=d
   s=0
   for j in g:
    i=2*j+rng.randrange(2);i=i^1 if s>>i&1 else i;s|=1<<i
   if s.bit_count()!=d:break
   m.extend([s,swap(s)])
  else:return m
def solve(m,symmetric=True,local_only=False,small_max=5,matching=True):
 def orbit(i,j):return min(tuple(sorted((i,j))),tuple(sorted((i^1,j^1))))
 E={};V={};cs=[];n=0
 for i in range(26):
  for j in range(i):
   if m[i]&m[j]:continue
   k=orbit(i,j) if symmetric else (i,j)
   if k not in E:n+=1;E[k]=n
   V[i,j]=V[j,i]=E[k]
 def card(xs,k,eq):
  nonlocal n
  if k>len(xs):
   if eq:cs.append([])
   return
  f=(CardEnc.equals if eq else CardEnc.atmost)(xs,k,top_id=n,encoding=EncType.seqcounter);n=max(n,f.nv);cs.extend(f.clauses)
 for i in range(0,26,2 if symmetric else 1):card([e for (u,v),e in V.items() if u==i],8-m[i].bit_count(),True)
 for i,j,k in itertools.combinations(range(26),3):
  if (i,j) in V and (j,k) in V and (k,i) in V:cs.append(list(set([-V[i,j],-V[j,k],-V[k,i]])))
 for i in (range(0,26,2 if symmetric else 1) if matching else ()):
  ass=collections.defaultdict(list)
  for l in range(8):
   if m[i]>>l&1:continue
   opts=[]
   for j in range(26):
    if (i,j) in V and m[j]>>l&1:n+=1;opts.append(n);ass[j].append(n);cs.append([-n,V[i,j]])
   cs.append(opts)
  for xs in ass.values():card(xs,1,False)
 def clause(q):return sorted({V[i,j] for i,j in itertools.combinations(q,2) if (i,j) in V})
 # Blue obstructions on small label subsets, including unconditionally blue ones.
 small=set()
 for t in range(1,small_max+1):
  for labs in itertools.combinations(range(8),t):
   L=sum(1<<l for l in labs);eligible=[i for i,s in enumerate(m) if not s&~L];
   for q in itertools.combinations(eligible,t+1):small.add(tuple(clause(q)))
 if () in small:return dict(status='forced_blue')
 cs.extend(map(list,small));rows=[sum(1<<i for i,s in enumerate(m) if s>>l&1) for l in range(8)];assert all(s.bit_count()==7 for s in rows)
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  for it in range(60):
   sl.conf_budget(3000);ok=sl.solve_limited();
   if ok!=True:return dict(status='unsat' if ok==False else 'unknown',models=it)
   if local_only:return dict(status='sat_local')
   model=set(sl.get_model());a=[sum(1<<j for j in range(26) if V.get((i,j)) in model) for i in range(26)];I=[(0,0)]
   for i,v in enumerate(a):I.extend([(q|1<<i,u|m[i]) for q,u in I if not q&v]);
   bad=[q for q,u in I if q.bit_count()>min(7,u.bit_count())];
   if not bad:
    g=a[:]+[0]*9
    for j,s in enumerate(rows,26):
     g[j]=s|1<<34;g[34]|=1<<j
     for i in range(26):g[i]|=(s>>i&1)<<j
    assert check(g,(1<<35)-1,3,9);return dict(status='witness',models=it+1,core=a,rows=rows)
   for q in bad:sl.add_clause(clause([i for i in range(26) if q>>i&1]))
  return dict(status='unknown',models=60)
if __name__=='__main__':
 path=P/'ramsey_incidence_first35.json';out=json.loads(path.read_text()) if path.exists() else [];start=len(out)
 for ix in range(int(sys.argv[1])):
  m=draw()
  if ix<start:assert out[ix]['masks']==m;continue
  z=solve(m);out.append(dict(masks=m,**z));path.write_text(json.dumps(out)+'\n');
 print(collections.Counter(z['status'] for z in out),collections.Counter((z['status'],z.get('models',0)>0) for z in out))
