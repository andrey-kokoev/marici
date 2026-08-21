"""Zero-free numerical hostile scan of the reduced gamma-prime Pick target."""
import cmath,json,math
from pathlib import Path

bernoulli=[1/6,-1/30,1/42,-1/30,5/66,-691/2730]
def digamma(z):
    correction=0j
    while abs(z)<15:correction-=1/z;z+=1
    value=cmath.log(z)-1/(2*z)
    for k,B in enumerate(bernoulli,1):value-=B/(2*k*z**(2*k))
    return value+correction
def eta_pair(s,depth=40):
    row=[[n**(-s),-math.log(n)*n**(-s)] for n in range(1,depth+2)]
    eta=derivative=0j;two=2
    for _ in range(depth):
        eta+=row[0][0]/two;derivative+=row[0][1]/two
        row=[[row[i][j]-row[i+1][j] for j in range(2)] for i in range(len(row)-1)];two*=2
    return eta,derivative
def reduced_F(t,depth=40):
    s=.5+cmath.sqrt(t);eta,etap=eta_pair(s,depth);L=math.log(2);r=cmath.exp((1-s)*L)
    zeta_log_derivative=etap/eta-L*r/(1-r)
    return 4+4*s*(s-1)/(2*s-1)*(-.5*math.log(math.pi)+.5*digamma(s/2)+zeta_log_derivative)
xs=[-100,-30,-10,-3,-1,-.3,0,.3,1,3,10,30,100]
ys=[.01,.03,.1,.3,1,3,10,30,100]
samples=[(x,y,reduced_F(complex(x,y))) for x in xs for y in ys]
minimum=min(samples,key=lambda row:row[2].imag)
assert minimum[2].imag>0
depth_discrepancy=max(abs(reduced_F(complex(x,y),36)-reduced_F(complex(x,y),40)) for x,y,_ in samples)
# Synthetic negative-residue pole violates the Pick sign.
bad_t=complex(.4,.3);bad=1/(bad_t-.5)
assert bad.imag<0
result={'grid_size':len(samples),'x_grid':xs,'y_grid':ys,
        'minimum_imaginary_part':minimum[2].imag,'minimum_location':[minimum[0],minimum[1]],
        'maximum_depth_36_40_discrepancy':depth_discrepancy,
        'no_negative_pick_value_found':True,'synthetic_negative_residue_imaginary_part':bad.imag,
        'scan_interval_certified':False,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'reduced-source-pick-hostile-scan.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
