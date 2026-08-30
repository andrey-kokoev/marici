"""Numerical diagonal-Loewner scan of Im F(x+iy)/y on the positive axis."""
import json,math
from pathlib import Path
from reduced_source_pick_hostile_scan import reduced_F

xs=[10**(-3+k/8) for k in range(57)] # 1e-3 through 1e4
epsilons=[1e-3,3e-4,1e-4]
rows=[]
for x in xs:
    estimates=[reduced_F(complex(x,e),40).imag/e for e in epsilons]
    rows.append((x,estimates))
minimum=min(rows,key=lambda row:min(row[1]))
assert min(v for _,row in rows for v in row)>0
depth_discrepancy=max(abs(reduced_F(complex(x,1e-4),36).imag/1e-4-row[-1]) for x,row in rows)
step_spread=max(max(row)-min(row) for _,row in rows)
result={'x_range':[xs[0],xs[-1]],'number_of_x_samples':len(xs),'imaginary_steps':epsilons,
        'minimum_normalized_imaginary_slope':min(minimum[1]),'minimum_location_x':minimum[0],
        'maximum_step_spread':step_spread,'maximum_depth_36_40_slope_discrepancy':depth_discrepancy,
        'no_negative_diagonal_loewner_slope_found':True,'interval_certified':False,
        'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'reduced-source-pick-boundary-slope.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
