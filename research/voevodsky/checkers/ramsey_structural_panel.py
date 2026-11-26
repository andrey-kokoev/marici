"""Deterministic heuristic, no alternative assignment or SAT verdict in selection. Rank pair readings by hypergeometric surprise given their two margins. Reserve one reading on each side then fill by score. Test two erasures on existing marks."""
import itertools,math,json,collections
from fractions import Fraction
from pysat.solvers import Solver

def run(idx,E,V,cs,spec,P,z):
 old=list(map(set,z['red_supports']));score={}
 for t,(side,i,j,k) in spec.items():
  N=6 if side=='C' else 16;l,r=(len(old[i]),len(old[j])) if side=='C' else (sum(i in s for s in old),sum(j in s for s in old));score[t]=Fraction(math.comb(l,k)*math.comb(N-l,r-k),math.comb(N,r))
 ranked=sorted(spec,key=lambda t:(score[t],spec[t][:3]));first=[next(t for t in ranked if spec[t][0]==side) for side in ('C','J')];ranked=first+[t for t in ranked if t not in first];out={}
 # Complementarity score: cover local color ambiguities not already separated. Only use 2x2 degree-preserving switches; no SAT or recovery verdict in selection.
 a=json.loads((P/'ramsey_37_catalogue_free.json').read_text())['certificates'][idx]['core'];ref=[sum(1<<j for j in s) for s in old];C=range(16);J=range(6);marked=set(E)
 def switches(state):
  for i,h in itertools.combinations(C,2):
   for j in J:
    if not (state[i]&~state[h])>>j&1:continue
    for k in J:
     if not (state[h]&~state[i])>>k&1:continue
     if any((a[i]>>u&1 and state[u]>>k&1) or (a[h]>>u&1 and state[u]>>j&1) for u in C if u!=i and u!=h):continue
     b=state.copy();b[i]^=(1<<j)|(1<<k);b[h]^=(1<<j)|(1<<k);yield b
 def mask(b):return tuple(sorted((i,j) for i,j in E if b[i]>>j&1))
 import sys
 local=set();parents=[ref]+[s for s in switches(ref) if not mask(s)]
 if '--expand' in sys.argv:
  # Exhaust all reachable neutral prefixes, using the same final switch and the same scoring rule.
  seen={tuple(s) for s in parents};cursor=1
  while cursor<len(parents):
   for s in switches(parents[cursor]):
    t=tuple(s)
    if t not in seen and not mask(s):seen.add(t);parents.append(s)
   cursor+=1
 for st in parents:
  for s in switches(st):
   if 1<=len(mask(s))<=2:local.add(tuple(s))
 if '--feedback' in sys.argv:
  from ramsey_panel_feedback import run as feedback
  return feedback(E,V,cs,spec,ranked,local,mask)
 # Give each observed marked pattern equal total weight, not each labeled repair.
 freq=collections.Counter(mask(s) for s in local);states=list(sorted(local));weights=[1/freq[mask(s)] for s in states];reject={}
 for t,(side,i,h,k) in spec.items():reject[t]={u for u,s in enumerate(states) if ((s[i]&s[h]).bit_count() if side=='C' else sum(v>>i&v>>h&1 for v in s))!=k}
 # Same sampled states. A hidden pair is recoverable only if no surviving alternative changes exclusively edges of that pair.
 if '--pair-score' in sys.argv or '--log-audit' in sys.argv:
  groups={pat:0 for pat in freq}
  for u,s in enumerate(states):groups[mask(s)]|=1<<u
  threats=[groups.get(tuple(sorted((e,f))),0)|groups.get((e,),0)|groups.get((f,),0) for e,f in itertools.combinations(E,2)];blocks={t:sum(1<<u for u in vs) for t,vs in reject.items()};livebits=(1<<len(states))-1
 if '--log-audit' in sys.argv:
  prev=json.loads((P/'ramsey_pair_score_panel.json').read_text());opt=json.loads((P/'ramsey_minimum_two_panel.json').read_text());sources={'old_greedy':next(r for r in prev if r['core']==idx)['tests']['joint5']['panel'],'exact_optimal':next(r for r in opt if r['core']==idx)['panel']};res={};start=(1<<len(states))-1
  for mode in ('assignment','pattern'):
   def loss(left):
    vals={pat:(left&bits).bit_count()/(freq[pat] if mode=='pattern' else 1) for pat,bits in groups.items()};return sum(math.log2(1+vals.get((i,),0)+vals.get((j,),0)+vals.get(tuple(sorted((i,j))),0)) for i,j in itertools.combinations(E,2))/45
   panel=[];left=start
   for j in range(5):
    opts=[t for t in ranked if t not in panel and (j!=1 or spec[t][0]!=spec[panel[0]][0])];t=min(opts,key=lambda t:loss(left&~blocks[t]));panel.append(t);left &= ~blocks[t]
   res[mode]={}
   for name,raw in dict(sources,log_greedy=[spec[t] for t in panel]).items():
    gs=[t for t in spec if spec[t] in raw];left=start
    for t in gs:left &= ~blocks[t]
    with Solver(name='g4',bootstrap_with=cs) as sl:
     bad=[]
     for j in (1,2):
      for q in itertools.combinations(E,j):
       if not any(set(x)<=set(q) for x in bad) and sl.solve(assumptions=gs+[V[f] if f in q else -V[f] for f in E]):bad.append(q)
    res[mode][name]=dict(loss_bits=loss(left),sample_recovered=sum(not(left&p) for p in threats),exact_recovered=sum(not any(set(x)<=set(q) for x in bad) for q in itertools.combinations(E,2)),panel=raw)
  return dict(core=idx,states=len(states),patterns=len(freq),results=res)
 chosen=[];alive=set(range(len(states)))
 for step in range(5):
  opts=[t for t in ranked if t not in chosen and (step!=1 or spec[t][0]!=spec[chosen[0]][0])]
  def merit(t):
   secondary=sum(weights[u] for u in sorted(alive&reject[t]))
   if '--pair-score' not in sys.argv:return secondary
   left=livebits&~blocks[t];return (sum(not(left&p) for p in threats),secondary)
  t=max(opts,key=merit);chosen.append(t);alive-=reject[t]
  if '--pair-score' in sys.argv:livebits &= ~blocks[t]
 with Solver(name='g4',bootstrap_with=cs) as sl:
  for name,g in [('base',[]),('3',ranked[:3]),('5',ranked[:5]),('joint3',chosen[:3]),('joint5',chosen)]:
   # Record all nonempty marked supports of size <=2; each invalidates queried pairs that contain it.
   bad=[]
   for n in (1,2):
    for Q in itertools.combinations(E,n):
     if any(set(b)<=set(Q) for b in bad):continue
     if sl.solve(assumptions=g+[V[f] if f in Q else -V[f] for f in E]):bad.append(Q)
   out[name]=dict(recovered=sum(not any(set(b)<=set(Q) for b in bad) for Q in itertools.combinations(E,2)),panel=[spec[t] for t in g]);
 return dict(core=idx,neutral_states=len(parents),local_states=len(states),local_patterns=len(freq),tests=out)
