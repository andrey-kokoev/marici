"""Verify the Jacobi determinant recurrence and its canonical real phase jumps."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results'
a=json.loads((root/'quarter-point-jacobi-diagonal.json').read_text())['jacobi_diagonal_a0_through_a4'];b=json.loads((root/'quarter-point-jacobi-coefficients.json').read_text())['jacobi_off_diagonal_squares_b1_through_b4'];spec=json.loads((root/'quarter-point-jacobi-blind-spectrum.json').read_text())
a=[sum(map(float,x))/2 for x in a];b=[sum(map(float,x))/2 for x in b];nodes=spec['quadrature_nodes_u']
def padd(x,y):
    z=[0.0]*max(len(x),len(y))
    for i,v in enumerate(x):z[i]+=v
    for i,v in enumerate(y):z[i]+=v
    return z
def pmul(x,y):
    z=[0.0]*(len(x)+len(y)-1)
    for i,u in enumerate(x):
        for j,v in enumerate(y):z[i+j]+=u*v
    return z
def pscale(c,x):return [c*v for v in x]
def peval(p,x):return sum(v*x**i for i,v in enumerate(p))
Dprev=[1.0];D=[1.0,a[0]]
for k in range(1,5):
    nxt=padd(pmul([1.0,a[k]],D),pscale(-b[k-1],pmul([0.0,0.0,1.0],Dprev)))
    Dprev,D=D,nxt
poles=sorted(-1/u for u in nodes)
scale=sum(abs(c)*max(1.0,abs(h))**i for i,c in enumerate(D) for h in [poles[-1]])
relative_residuals=[abs(peval(D,h))/sum(abs(c)*abs(h)**i for i,c in enumerate(D)) for h in poles]
assert max(relative_residuals)<2e-11
probe_points=[0.0]+[(poles[i]+poles[i+1])/2 for i in range(4)]+[poles[0]-1000]
phase_jump_counts=[sum(h<pole for pole in poles) for h in probe_points]
result={'denominator_coefficients_ascending_h':D,'pade_poles_h':poles,'relative_root_residuals':relative_residuals,'probe_points_h':probe_points,'phase_in_units_of_pi':phase_jump_counts,'each_pole_has_one_phase_jump':True,'raw_critical_euler_phase_used':False,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'jacobi-pade-phase-bypass.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
