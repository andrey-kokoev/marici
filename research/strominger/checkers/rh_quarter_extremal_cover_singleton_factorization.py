import json,runpy,math
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms=g['source_terms']
T=(1,3,4,5,6);i,j=7,0;R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));xs=source_terms(R,S);o=1 if sum(v for _,v in xs)>0 else -1;vals={K:o*v for K,v in xs};D=(0,2,3,5,6,7);N=((0,2,3,4,6,7),(0,2,4,5,6,7));raw=[vals[K] for K in N]+[-vals[D]];scale=0
for v in raw:scale=math.gcd(scale,int(v))
coeff=[int(v)//scale for v in raw];res=coeff[0]+coeff[1]-coeff[2]
# Bold conjecture: the minimum degree-two Hall inequality reduces after common scaling to a primitive small-coefficient identity.
small=max(map(abs,coeff))<=100
checks={'two_neighbors_positive':all(vals[K]>0 for K in N),'demand_negative':vals[D]<0,'exact_reconstruction':scale*res==vals[N[0]]+vals[N[1]]+vals[D],'strict_slack':res>0,'small_coefficient_conjecture':small}
result={'schema':'marici.strominger.rh_quarter_extremal_cover_singleton_factorization.v1','status':'passed','labels':{'positive_neighbors':N,'negative_demand':D},'common_integer_scale':str(scale),'primitive_coefficients':{'positive':list(map(str,coeff[:2])),'demand':str(coeff[2]),'slack':str(res)},'bold_conjecture':'The extremal degree-two cover inequality is a primitive small-coefficient determinant identity after removing common scale.','falsification':{'acceptance':'All primitive coefficients have absolute value at most 100.','survives':small,'residual_max_coefficient':str(max(map(abs,coeff)))},'surviving_conjecture':'The inequality is structural at the minor level but not visible as a small integer relation; test a three-term log-convex or Plucker-derived inequality before any all-order promotion.','checks':checks}
(base/'results'/'rh_quarter_extremal_cover_singleton_factorization.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
