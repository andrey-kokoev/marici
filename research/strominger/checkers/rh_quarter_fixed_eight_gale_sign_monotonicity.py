import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')))
source_terms,k=g['source_terms'],g['k']
def leq(K,L):return all(a<=b for a,b in zip(K,L))
stats={'positive_upset':{'bad_cases':0,'first':None},'positive_downset':{'bad_cases':0,'first':None}};cases=0
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));et=(-1)**(j-i+1) if i<j else (-1)**(i-j);expected=et*(-1)**(sum(x>i for x in T)+sum(x>j for x in T));terms=[(K,expected*v) for K,v in source_terms(R,S)];cases+=1
   for a,(K,v) in enumerate(terms):
    for L,w in terms[a+1:]:
     pairs=[]
     if leq(K,L):pairs.append((K,v,L,w))
     if leq(L,K):pairs.append((L,w,K,v))
     for low,lv,high,hv in pairs:
      if lv>0 and hv<0:
       s=stats['positive_downset'];s['bad_cases']+=1
       if s['first'] is None:s['first']={'base':T,'i':i,'j':j,'low':low,'low_value':str(lv),'high':high,'high_value':str(hv)}
       break
     else:continue
     break
    else:continue
    break
   for a,(K,v) in enumerate(terms):
    found=False
    for L,w in terms[a+1:]:
     pairs=[]
     if leq(K,L):pairs.append((K,v,L,w))
     if leq(L,K):pairs.append((L,w,K,v))
     if any(lv<0 and hv>0 for _,lv,_,hv in pairs):found=True;bad=next(p for p in pairs if p[1]<0 and p[3]>0);break
    if found:
     s=stats['positive_upset'];s['bad_cases']+=1
     if s['first'] is None:s['first']={'base':T,'i':i,'j':j,'low':bad[0],'low_value':str(bad[1]),'high':bad[2],'high_value':str(bad[3])}
     break
successful=[n for n,s in stats.items() if s['bad_cases']==0]
result={'schema':'marici.strominger.rh_quarter_fixed_eight_gale_sign_monotonicity.v1','status':'passed' if successful else 'failed','verdict':'Oriented positive labels must form a Gale upset or downset before Gale-order monotone transport can be source-driven without sign sorting.','terminal_case_count':cases,'successful_orientations':successful,'statistics':stats,'checks':{'all_cases':cases==3584,'gale_sign_monotonicity_found':bool(successful)}}
(base/'results'/'rh_quarter_fixed_eight_gale_sign_monotonicity.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
