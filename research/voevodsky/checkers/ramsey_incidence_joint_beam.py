"""Search neighboring incidence types, re-solving all core edges. Hard constraints: exact degrees, triangle-free, <=4 label regions. Optimize joint five-region score on each hard-feasible type, not individual flags. Releasing a pair reallocates ALL its labels; later exchanges can involve other vertices. Beam by exact score (only unbudgeted UNSAT trusted)."""
import sys,json,itertools,collections,heapq,subprocess,igraph as ig
from ramsey_incidence_mismatch import base,P
from pysat.solvers import Solver
from pysat.card import CardEnc,ITotalizer

def key(m):
 g=ig.Graph(34,[(i,26+j) for i,s in enumerate(m) for j in range(8) if s>>j&1]);p=g.canonical_permutation(color=[1]*26+[2]*8);return tuple(sorted(tuple(sorted(e)) for e in g.permute_vertices(p).get_edgelist()))
def opt(m):
 E,cs=base(m);top=max(E.values())
 for i,s in enumerate(m):
  xs=[v for e,v in E.items() if i in e];d=8-s.bit_count()
  if d>len(xs):return None
  f=CardEnc.equals(xs,d,top_id=top);top=max(top,f.nv);cs+=f.clauses
 act=[]
 for t in range(256):
  if t.bit_count()!=5:continue
  top+=1;act.append(top);vs=[i for i,s in enumerate(m) if not s&~t];cs.extend([[-top]+[E[e] for e in itertools.combinations(q,2) if e in E] for q in itertools.combinations(vs,6)])
 with Solver(name='cadical195',bootstrap_with=cs) as sl,ITotalizer(lits=[-v for v in act],ubound=55,top_id=top) as it:
  if not sl.solve():return None
  model=set(sl.get_model());sl.append_formula(it.cnf.clauses);lo=-1;hi=56
  while hi-lo>1:
   md=(hi+lo)//2
   if sl.solve(assumptions=[-it.rhs[md]]):hi=md;model=set(sl.get_model())
   else:lo=md
  es=[e for e,v in E.items() if v in model];assert len(es)==76;return dict(score=56-hi,m=m,edges=es)

def run():
 start=json.loads((P/'ramsey_incidence_five_frontier.json').read_text());m=start['m'];seen={key(m)};nodes=[dict(m=m,score=40,edges=start['edges'])];front=[(-40,0)];exp=[];nst=0;cap=int(sys.argv[2]);path=P/'ramsey_incidence_joint_beam.json'
 while front and len(exp)<cap:
  _,par=heapq.heappop(front);m=nodes[par]['m'];exp.append(par);rs=[]
  for i,j in itertools.combinations(range(26),2):
   both=m[i]&m[j];v=m[i]^m[j];s=v
   while True:
    a=both|s;b=both|(s^v)
    if 0<a<=b and a.bit_count()<8 and b.bit_count()<8 and {a,b}!={m[i],m[j]}:
     n=m[:];n[i]=a;n[j]=b;k=key(n)
     if k not in seen:seen.add(k);rs.append((n,[i,j,a,b]))
    if s==0:break
    s=(s-1)&v
  states=subprocess.check_output([sys.argv[1],'4'],input=''.join(' '.join(map(str,n))+'\n' for n,t in rs),text=True).splitlines()
  for (n,t),st in zip(rs,states,strict=True):
   if int(st.split()[0]):continue
   nst+=1;z=opt(n)
   if z:z.update(parent=par,trade=t);heapq.heappush(front,(-z['score'],len(nodes)));nodes.append(z)
  path.write_text(json.dumps(dict(expanded=exp,tested=len(seen),sat_probes=nst,nodes=nodes))+'\n');print(len(exp),len(seen),len(nodes),max(z['score'] for z in nodes),flush=True)
if __name__=='__main__':run()
