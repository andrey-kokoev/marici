"""Arb cover of |t|=1 for the normalized boundary-margin remainder."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[2] / 'benincasa' / '.tmp_flint'))
from flint import acb, acb_series, arb, ctx
ctx.dps=60
N=2048
R=arb('0.5')
pi=arb.pi()
max_upper=arb(0); failures=[]
for j in range(N):
    mid=2*3.141592653589793*(j+0.5)/N
    rad=3.141592653589793/N
    theta=arb(mid,rad)
    z=R.sqrt()*(acb(0,theta)).exp()
    # Q depends on t=z^2 and is even in z. Reflect to Re(z) >= 0 so
    # the completed-zeta product stays away from its cancellation-prone side.
    if __import__('math').cos(mid) < 0:
        z = -z
    s=acb_series([acb(arb('.5'))+z,1],3)
    xi=acb('.5')*s*(s-1)*((-s/2)*acb(pi).log()).exp()*(s/2).gamma()*s.zeta()
    X,X1,X2=xi[0],xi[1],2*xi[2]
    if abs(X).lower() <= 0:
        failures.append({'arc':j,'reason':'Xi ball contains zero','Xi':str(X)})
        continue
    m=X1/X; m1=X2/X-m*m
    L=m/(2*z); Lt=(z*m1-m)/(4*z**3)
    Q=4*(4*L-(1-4*z*z)*Lt)
    upper=abs(Q).upper()
    if upper>max_upper:max_upper=upper
T=arb('0.007225')
margin=arb('0.36981997796728245512935065376058')
threshold=margin*(1-T/R)/((T/R)**5)
remainder_upper=max_upper*((T/R)**5)/(1-T/R)
central_poly_lower=arb('0.3698199776056205986744622113741447417522141245456141')
final_lower=central_poly_lower-remainder_upper
certified=(not failures and final_lower.lower() > 0)
out={'precision_decimal_digits':ctx.dps,'arc_count':N,'circle_radius_t':str(R),'xi_nonzero_on_cover':not failures,'failure_count':len(failures),'max_abs_Q_upper':str(max_upper),'cauchy_acceptance_threshold_lower':str(threshold.lower()),'degree_four_remainder_upper':str(remainder_upper),'normalized_margin_final_lower':str(final_lower.lower()),'central_remainder_accepted':certified,'central_interval_x_upper':'0.085','interval_certified':certified,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'arb-normalized-margin-cauchy-circle.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
