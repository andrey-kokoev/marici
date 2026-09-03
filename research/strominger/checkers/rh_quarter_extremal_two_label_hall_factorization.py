import json,runpy,math
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms=g['source_terms']
T=(1,2,3,5,6);i,j=7,0;R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));expected=(-1)**(i-j)*(-1)**(sum(x>i for x in T)+sum(x>j for x in T))
def leq(K,L):return all(a<=b for a,b in zip(K,L))
def comp(K,L):return leq(K,L) or leq(L,K)
terms=[(K,expected*v) for K,v in source_terms(R,S)];D=((0,2,3,4,5,7),(0,2,3,5,6,7));neg={K:-v for K,v in terms if v<0};neighborhood=[(K,v) for K,v in terms if v>0 and any(comp(K,L) for L in D)];demand=sum(neg[L] for L in D);supply=sum(v for _,v in neighborhood);slack=supply-demand;masses=[v for _,v in neighborhood]+[neg[L] for L in D];scale=0
for v in masses:scale=math.gcd(scale,int(v))
normalized_supply=[{'label':K,'coefficient':str(v//scale)} for K,v in neighborhood];normalized_demand=[{'label':L,'coefficient':str(neg[L]//scale)} for L in D]
result={'schema':'marici.strominger.rh_quarter_extremal_two_label_hall_factorization.v1','status':'passed' if slack>0 and scale>0 and slack%scale==0 else 'failed','base':T,'i':i,'j':j,'negative_labels':D,'comparable_positive_neighborhood':normalized_supply,'normalized_demands':normalized_demand,'common_integer_scale':str(scale),'normalized_slack':str(slack//scale),'exact_slack':str(slack),'identity':'sum(normalized neighborhood coefficients) - sum(normalized demand coefficients) = normalized_slack','counts':{'positive_neighbors':len(neighborhood),'negative_demands':2},'checks':{'both_demands_negative':all(L in neg for L in D),'strict_slack':slack>0,'factorization_exact':scale*(sum(int(x['coefficient']) for x in normalized_supply)-sum(int(x['coefficient']) for x in normalized_demand))==slack}}
(base/'results'/'rh_quarter_extremal_two_label_hall_factorization.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
