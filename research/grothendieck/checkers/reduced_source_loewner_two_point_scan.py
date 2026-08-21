"""Coupled two-point Loewner scan with a finite-Jacobi conditioning control."""
import json
from pathlib import Path
from reduced_source_pick_hostile_scan import reduced_F

xs=[10**(-3+k/4) for k in range(29)]
def derivative(x,e=1e-3):
    d1=reduced_F(complex(x,e),44).imag/e;d2=reduced_F(complex(x,e/2),44).imag/(e/2)
    return (4*d2-d1)/3
F=[reduced_F(complex(x,0),44).real for x in xs];d=[derivative(x) for x in xs]
rows=[]
for i,x in enumerate(xs):
    for j in range(i+1,len(xs)):
        y=xs[j];K=(F[j]-F[i])/(y-x);rows.append((d[i]*d[j]-K*K,x,y))
minimum=min(rows);wide=[row for row in rows if row[2]/row[1]>=100];minimum_wide=min(wide)
assert minimum_wide[0]>0
# Positive five-node control predicts the scale of the closest hostile pair.
root=Path(__file__).parents[1]/'results';quad=json.loads((root/'quarter-point-pade-gaussian-identity.json').read_text())
us,ws=quad['quadrature_nodes_u'],quad['quadrature_weights']
def K5(x,y):return sum(4*w/u**2/((x+1/u-.25)*(y+1/u-.25)) for u,w in zip(us,ws))
x,y=minimum[1],minimum[2];control=K5(x,x)*K5(y,y)-K5(x,y)**2
assert control>0
result={'x_sample_count':len(xs),'pair_count':len(rows),'raw_minimum_determinant':minimum[0],
        'raw_minimum_pair':[x,y],'minimum_widely_separated_determinant':minimum_wide[0],
        'minimum_wide_pair':[minimum_wide[1],minimum_wide[2]],
        'positive_five_node_control_at_raw_minimum_pair':control,
        'near_diagonal_source_scan_resolved':False,'robust_negative_counterexample_found':False,
        'interval_certified':False,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'reduced-source-loewner-two-point-scan.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
