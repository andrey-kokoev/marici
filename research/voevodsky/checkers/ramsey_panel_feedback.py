"""Core 7: freeze score, panel budget, split, and feedback budget. Exact evaluation uses an independent solver. Only train-query countermodels with zero sampled ambiguity enter training."""
import itertools,collections,math,random
from pysat.solvers import Solver

def run(E,V,cs,spec,ranked,local,mask):
 pairs=list(itertools.combinations(E,2));random.Random(710).shuffle(pairs);train=pairs[:23];hold=pairs[23:];out=[]
 with Solver(name='g4',bootstrap_with=cs) as oracle:
  for step in range(11):
   states=sorted(local);groups=collections.defaultdict(int)
   for i,s in enumerate(states):groups[mask(s)]|=1<<i
   bits={};
   for t,(side,i,h,k) in spec.items():bits[t]=sum(1<<u for u,s in enumerate(states) if ((s[i]&s[h]).bit_count() if side=='C' else sum(v>>i&v>>h&1 for v in s))==k)
   def ambiguity(q,left):return sum((groups[p]&left).bit_count()/groups[p].bit_count() for p in [(q[0],),(q[1],),tuple(sorted(q))] if p in groups)
   left=(1<<len(states))-1;panel=[]
   for j in range(5):
    opts=[t for t in ranked if t not in panel and (j!=1 or spec[t][0]!=spec[panel[0]][0])];t=min(opts,key=lambda t:sum(math.log2(1+ambiguity(q,left&bits[t])) for q in itertools.combinations(E,2)));panel.append(t);left&=bits[t]
   def alt(sl,q):
    for red in ((q[0],),(q[1],),q):
     if sl.solve(assumptions=panel+[V[f] if f in red else -V[f] for f in E]):
      pos=set(sl.get_model());return tuple(sum(1<<j for j in range(6) if V[i,j] in pos) for i in range(16))
   with Solver(name='g4',bootstrap_with=cs) as audit:
    scores=[sum(alt(audit,q) is None for q in batch) for batch in [train,hold]]
   rec=dict(step=step,panel=[spec[t] for t in panel],train=scores[0],hold=scores[1],states=len(states));out.append(rec);print(step,scores,flush=True)
   if step==10:break
   for q in train:
    if ambiguity(q,left):continue
    s=alt(oracle,q)
    if s is not None:assert s not in local;local.add(s);rec.update(query=q,added_state=s);break
   else:break
 return dict(seed=710,train=train,hold=hold,steps=out)
