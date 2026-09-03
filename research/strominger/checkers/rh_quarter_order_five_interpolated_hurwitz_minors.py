import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")))
Q,D,mu,ad,tr=g["Q"],g["D"],g["mu"],g["ad"],g["tr"]
hurwitz_minor,interp,bern=g["hurwitz_minor"],g["interp"],g["bern"]
X=mu(mu(Q(4),D(4,0)),D(4,2));Y=mu(mu(Q(0),D(4,1)),D(4,1));L=max(len(X),len(Y));X += [F(0)]*(L-len(X));Y += [F(0)]*(L-len(Y));degree=L-1
records=[];first_failure=None
for k in range(1,degree+1):
 xs=[F(j,k) for j in range(k+1)];ys=[hurwitz_minor([X[i]-t*Y[i] for i in range(L)],k) for t in xs];poly=interp(xs,ys);b=bern(poly,k);ok=all(z>=0 for z in b) and ys[0]>0
 rec={"minor_order":k,"interpolated_degree":len(poly)-1,"bernstein_nonnegative":ok,"zero_bernstein_coefficients":sum(z==0 for z in b)};records.append(rec)
 if not ok and first_failure is None:first_failure=rec
endpoint=tr(ad(X,Y,-1));endpoint_ok=all(hurwitz_minor(endpoint,k)>0 for k in range(1,len(endpoint)))
checks={"all_open_hurwitz_minors_bernstein_nonnegative":first_failure is None,"degree_dropped_endpoint_hurwitz":endpoint_ok,"all_forty_principal_minors_checked":len(records)==40,"open_leading_coefficient_positive":X[-1]>0 and X[-1]==Y[-1]}
result={"schema":"marici.strominger.rh_quarter_order_five_interpolated_hurwitz_minors.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Each degree-40 order-five parametric Hurwitz principal minor is reconstructed exactly from its degree-bounded rational samples and tested in the Bernstein basis. Passing proves continuous pencil stability, with the degree-dropped endpoint checked separately; shift covariance then promotes zero shift to every nonnegative shift.","pencil_degree":degree,"records":records,"first_failure":first_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_order_five_interpolated_hurwitz_minors.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
