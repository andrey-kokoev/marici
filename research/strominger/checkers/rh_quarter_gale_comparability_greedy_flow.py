import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def leq(K,L):return all(a<=b for a,b in zip(K,L))
def comp(K,L):return leq(K,L) or leq(L,K)
def greedy(pos,neg,mode):
 supply={K:v for K,v in pos};degree=lambda L:sum(comp(K,L) for K,_ in pos)
 if mode=='lex':ns=sorted(neg)
 elif mode=='largest_demand':ns=sorted(neg,key=lambda x:(x[1],x[0]))
 else:ns=sorted(neg,key=lambda x:(degree(x[0]),x[0]))
 for L,v in ns:
  need=-v;cands=[K for K,a in supply.items() if a>0 and comp(K,L)]
  cands=sorted(cands,key=(lambda K:K) if mode=='lex' else (lambda K:(-supply[K],K)))
  for K in cands:
   z=min(need,supply[K]);supply[K]-=z;need-=z
   if need==0:break
  if need:return need,L
 return 0,None
modes=('lex','largest_demand','most_constrained');stats={m:{'failed_cases':0,'first':None} for m in modes};cases=0
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));et=(-1)**(j-i+1) if i<j else (-1)**(i-j);expected=et*(-1)**(sum(x>i for x in T)+sum(x>j for x in T));terms=[(K,expected*v) for K,v in source_terms(R,S)];pos=[x for x in terms if x[1]>0];neg=[x for x in terms if x[1]<0];cases+=1
   for m in modes:
    deficit,L=greedy(pos,neg,m)
    if deficit:
     stats[m]['failed_cases']+=1
     if stats[m]['first'] is None:stats[m]['first']={'base':T,'i':i,'j':j,'negative_label':L,'deficit':str(deficit)}
success=[m for m,s in stats.items() if s['failed_cases']==0]
result={'schema':'marici.strominger.rh_quarter_gale_comparability_greedy_flow.v1','status':'passed' if success else 'failed','terminal_case_count':cases,'successful_rules':success,'statistics':stats,'verdict':'A deterministic greedy rule is a bounded canonical candidate only if it covers every negative demand without residual.','checks':{'all_cases':cases==3584,'greedy_rule_found':bool(success)}}
(base/'results'/'rh_quarter_gale_comparability_greedy_flow.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
