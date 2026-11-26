"""Global singleton graph lemma: five blue singleton cells with labels T would be the ONLY core cells wholly supported in T (any extra such cell violates the label-union condition with the singletons in its mask). Hence the 21 remaining cells each use exactly one of the 21 available incidences on the three outside labels. Seven cells on any outside label are blue to the other two labels, giving a blue nine. No assumptions on other singleton count, unsaturation, or exceptional-mask sizes. If all eight labels have singletons, their induced red graph H is (3,5), and contains F the graph of two-label masks. Enumerate possible H on fixed F by SAT. Conditional on quartets, their supports must contain a red edge of H too. Track the high-degree exception-first tests separately."""
from ramsey_exception_first import *
from ramsey_incidence_first35 import Solver
from ramsey_unsaturated_pair_graphs import graphs
from concurrent.futures import ProcessPoolExecutor
pairs=itertools.combinations

def possible(es,q=()):
 E={p:i+1 for i,p in enumerate(pairs(V,2))};cs=[[E[e]] for e in es]+[[-E[p] for p in pairs(t,2)] for t in pairs(V,3)]+[[E[p] for p in pairs(t,2)] for t in pairs(V,5)]+[[E[p] for p in pairs([i for i in V if s>>i&1],2)] for s in q]
 with Solver(name='cadical195',bootstrap_with=cs) as sl:return sl.solve()
if __name__=='__main__':
 out=[]
 for d in (6,7,8):
  gs=graphs(d);high=[i for i,e in enumerate(gs) if max(ig.Graph(8,e).degree())>=5];bad=[i for i,e in enumerate(gs) if not possible(e)];r=json.loads((P/f'ramsey_five_leaf_rows_{d}.json').read_text());assert not any(v.get('win') for v in r);print(d,len(gs),len(high),len(bad),sorted(set(bad)-set(high)));out.append(dict(pairs=d,types=len(gs),degree_at_least_five=high,no_singleton_extension=bad,exceptional_high_degree_checks=len(r),unknown=sum(z.get('unknown',0) for z in r)))
 (P/'ramsey_singleton_five_gate.json').write_text(json.dumps(out)+'\n')
