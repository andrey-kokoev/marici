"""Aggregate certified leading minors for the degree-nine Hausdorff jet."""
import json
from decimal import Decimal
from pathlib import Path
root=Path(__file__).parents[1]/'results'
names=['quarter-point-end-to-end-interval.json','quarter-point-order-two-interval.json','quarter-point-order-three-interval.json','quarter-point-order-four-interval.json']
data=[json.loads((root/n).read_text()) for n in names];A=[tuple(map(Decimal,x)) for x in data[0]['moment_intervals']]
lower=[A[1][0],Decimal(data[0]['lower_localizer_determinant_interval'][0])]
upper=[4*A[0][0]-A[1][1],Decimal(data[0]['upper_localizer_determinant_interval'][0])]
for d,key in zip(data[1:],['order_two_determinant_intervals','order_three_determinant_intervals','order_four_determinant_intervals']):
    lower.append(Decimal(d[key][1][0]));upper.append(Decimal(d[key][2][0]))
assert all(x>0 for x in lower+upper)
result={'truncation_degree':9,'lower_localizer_leading_minor_lower_bounds':[str(x) for x in lower],'upper_localizer_leading_minor_lower_bounds':[str(x) for x in upper],'both_localizer_matrices_positive_definite':True,'truncated_positive_measure_on_0_4_exists':True,'representing_measure_unique':False,'full_hierarchy_proved':False,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'quarter-point-truncated-measure-certificate.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
