"""Role reversal = swap ends of transition relation, keep the same place-pair observation on each gap. Compare coarsest observation-preserving stable partitions in R and its converse (existential relational matching, not predecessor multiplicities). Common rooted frame control: named involutions are self-converse."""
from four_role_predictive_quotients import G,Ys,gap,matching,actions,obs,D,json
from itertools import combinations
def partition(obs,rels):
 def labels(values):
  tab={};return [tab.setdefault(x,len(tab)) for x in values]
 p=labels(obs);curve=[len(set(p))]
 while True:
  q=labels([(p[i],tuple(tuple(sorted({p[j] for j in row[i]})) for row in rels)) for i in range(len(p))]);
  if q==p:return p,curve
  p=q;curve.append(len(set(p)))
def transpose(r):return [[i for i,row in enumerate(r) if j in row] for j in range(len(r))]
r=[[G.index(gap(y))] for y in Ys];rev=transpose(r);o=list(map(matching,Ys));f,cf=partition(o,[r]);b,cb=partition(o,[rev]);both,cc=partition(o,[r,rev]);
def wit(p,q):
 for i,j in combinations(range(len(G)),2):
  if p[i]==p[j] and q[i]!=q[j]:return [G[i],G[j]]
rr=[[[j] for j in g] for g in actions];assert all(transpose(g)==g for g in rr);ram,rc=partition(obs,rr);out=dict(domain='55 decimal gap pairs; observation = unordered set of place matchings of K(gap)',forward=cf,converse=cb,both_directions=cc,intersection_size=len(set(zip(f,b))),forward_equal_converse_distinct=wit(f,b),converse_equal_forward_distinct=wit(b,f),ramsey_named_self_converse=True,ramsey_forward_and_converse=rc);print(out);(D/'results/four_role_reverse_quotient.json').write_text(json.dumps(out,indent=2)+'\n')
