"""Directed rank-three Loewner minors on the 0.001 central grid."""
import itertools,json
from decimal import Decimal as D
from pathlib import Path

import central_separated_rank_three_loewner as T

points=[D(i)/D(1000) for i in range(11)]
rows=[]
for triple in itertools.combinations(points,3):
    matrix=[[T.kernel(x,y) for y in triple] for x in triple]
    determinant=T.determinant3(matrix)
    vandermonde_squared=((triple[1]-triple[0])*(triple[2]-triple[0])*(triple[2]-triple[1]))**2
    normalized=(T.I.down.divide(determinant[0],vandermonde_squared),
                T.I.up.divide(determinant[1],vandermonde_squared))
    rows.append((determinant,normalized,triple))
weakest=min(rows,key=lambda row:row[0][0])
normalized_min=min(rows,key=lambda row:row[1][0])
normalized_max=max(rows,key=lambda row:row[1][1])
assert all(determinant[0]>0 for determinant,_,_ in rows)
result={
    'grid_points':[str(x) for x in points],
    'triple_count':len(rows),
    'all_rank_three_Loewner_minors_strictly_positive':True,
    'weakest_triple':[str(x) for x in weakest[2]],
    'weakest_determinant_interval':[str(x) for x in weakest[0]],
    'minimum_normalized_determinant_interval':[str(x) for x in normalized_min[1]],
    'minimum_normalized_determinant_triple':[str(x) for x in normalized_min[2]],
    'maximum_normalized_determinant_interval':[str(x) for x in normalized_max[1]],
    'maximum_normalized_determinant_triple':[str(x) for x in normalized_max[2]],
    'directed_decimal_rounding':True,
    'interval_certified':True,
    'zero_locations_used':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-three-loewner-grid.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
