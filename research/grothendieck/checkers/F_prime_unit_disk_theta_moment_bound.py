"""Real-boundary theta-moment reduction for a unit-disk bound on F'."""
import json,math
from pathlib import Path
from reduced_source_pick_hostile_scan import eta_pair,digamma

def eta_triple(s,depth=100):
    row=[]
    for n in range(1,depth+2):
        l=math.log(n);v=n**(-s);row.append([v,-l*v,l*l*v])
    sums=[0.,0.,0.];two=2.
    for _ in range(depth):
        for j in range(3):sums[j]+=row[0][j]/two
        row=[[row[i][j]-row[i+1][j] for j in range(3)] for i in range(len(row)-1)];two*=2
    return sums
def trigamma(z):
    total=0.
    while z<30:total+=1/z**2;z+=1
    return total+1/z+1/(2*z*z)+1/(6*z**3)-1/(30*z**5)+1/(42*z**7)-1/(30*z**9)
def xi_data(s):
    eta,e1,e2=eta_triple(s);L=math.log(2);r=2**(1-s);zeta=eta/(1-r)
    zlog=e1/eta-L*r/(1-r)
    zlog1=e2/eta-(e1/eta)**2+L*L*r/(1-r)**2
    xi=.5*s*(s-1)*math.pi**(-s/2)*math.gamma(s/2)*zeta
    l1=1/s+1/(s-1)-.5*math.log(math.pi)+.5*digamma(s/2).real+zlog
    l2=-1/s**2-1/(s-1)**2+.25*trigamma(s/2)+zlog1
    return xi,xi*l1,xi*(l2+l1*l1)
center=xi_data(.5)[0];edge,x1,x2=xi_data(1.5);lower=2*center-edge
A=x1/2;B=(x2-x1)/4
ell1=A/lower;ell2=B/lower+(A/lower)**2
Fprime_bound=4*ell1+5*ell2
result={'Xi_half':center,'Xi_three_halves':edge,'unit_disk_Xi_modulus_lower_majorant':lower,
        'Y_prime_one':A,'Y_double_prime_one':B,'log_Y_prime_bound':ell1,
        'log_Y_double_prime_bound':ell2,'resulting_F_prime_unit_disk_bound':Fprime_bound,
        'target_bound_20_passes_numerically':Fprime_bound<20,
        'theta_coefficient_argument':'positive coefficients make derivative suprema occur at t=1',
        'interval_certified':False,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'F-prime-unit-disk-theta-moment-bound.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
