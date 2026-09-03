import json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_order_four_interpolated_hurwitz_minors.py')));Q,D,mu,ad,hm=g['Q'],g['D'],g['mu'],g['ad'],g['hurwitz_minor'];records=[]
for n in range(2,7):
 X=mu(mu(Q(n+1),D(n+1,0)),D(n+1,2));Y=mu(mu(Q(0),D(n+1,1)),D(n+1,1));L=max(len(X),len(Y));X += [0]*(L-len(X));Y += [0]*(L-len(Y));G=ad(X,Y,-1);records.append({'source_size':n,'X_degree':len(X)-1,'G_degree':len(G)-1,'X_first8':all(hm(X,r)>0 for r in range(1,9)),'G_first8':all(hm(G,r)>0 for r in range(1,9))})
checks={'five_sizes':len(records)==5,'all_positive':all(x['X_first8'] and x['G_first8'] for x in records)};r={'schema':'marici.strominger.rh_quarter_endpoint_hurwitz_size_ladder.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'Finite endpoint Hurwitz ladder regenerated as bounded evidence only.','records':records,'checks':checks};(base/'results'/'rh_quarter_endpoint_hurwitz_size_ladder.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
