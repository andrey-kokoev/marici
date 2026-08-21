"""Interval certificate for all Hausdorff finite differences through degree nine."""
import json,math
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING
from pathlib import Path
root=Path(__file__).parents[1]/'results';data=json.loads((root/'quarter-point-order-four-interval.json').read_text())
down=Context(prec=70,rounding=ROUND_FLOOR);up=Context(prec=70,rounding=ROUND_CEILING)
A=[(Decimal(x[0]),Decimal(x[1])) for x in data['moments_A0_through_A9']]
m=[(down.divide(x[0],Decimal(4)**k),up.divide(x[1],Decimal(4)**k)) for k,x in enumerate(A)]
def difference(k,j):
    lo=Decimal(0);hi=Decimal(0)
    for r in range(j+1):
        c=Decimal(math.comb(j,r))
        if r%2==0:
            lo=down.add(lo,down.multiply(c,m[k+r][0]));hi=up.add(hi,up.multiply(c,m[k+r][1]))
        else:
            lo=down.subtract(lo,up.multiply(c,m[k+r][1]));hi=up.subtract(hi,down.multiply(c,m[k+r][0]))
    return lo,hi
boxes={(k,j):difference(k,j) for k in range(10) for j in range(10-k)}
assert all(x[0]>0 for x in boxes.values())
smallest=min(boxes,key=lambda x:boxes[x][0])
result={'maximum_available_degree':9,'number_of_complete_monotonicity_boxes':len(boxes),
        'all_lower_bounds_strictly_positive':True,'smallest_box_index_k_j':list(smallest),
        'smallest_box':[str(x) for x in boxes[smallest]],
        'boxes':{f'{k},{j}':[str(x[0]),str(x[1])] for (k,j),x in boxes.items()},
        'infinite_complete_monotonicity_proved':False,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-complete-monotonicity.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():
        if key!='boxes':print(f'{key}={value}')
