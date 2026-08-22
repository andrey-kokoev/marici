"""All nondecreasing rank-five Newton-LDL grid anchors."""
import itertools,json
from decimal import Decimal as D
from pathlib import Path

import central_rank_five_loewner_grid as G

points=[D(i)/D(1000) for i in range(11)]
rows=[]
for nodes in itertools.combinations_with_replacement(points,5):
    diagonal=G.pivots(G.matrix(nodes))
    rows.append((diagonal,nodes))
assert all(len(diagonal)==5 and all(pivot[0]>0 for pivot in diagonal) for diagonal,_ in rows)
weakest=min(rows,key=lambda row:row[0][-1][0])
weakest_by_pivot=[min(rows,key=lambda row,k=k:row[0][k][0]) for k in range(5)]
result={
    'grid_points':[str(x) for x in points],
    'nondecreasing_anchor_count':len(rows),
    'all_confluent_and_separated_rank_five_Newton_LDL_pivots_positive':True,
    'weakest_anchor':[str(x) for x in weakest[1]],
    'weakest_final_pivot_interval':[str(x) for x in weakest[0][-1]],
    'weakest_anchor_all_pivots':[[str(a),str(b)] for a,b in weakest[0]],
    'coordinatewise_weakest_pivots':[
        {'pivot_index':k+1,
         'anchor':[str(x) for x in row[1]],
         'interval':[str(a) for a in row[0][k]]}
        for k,row in enumerate(weakest_by_pivot)],
    'degree_twenty_nine_tail_included':True,
    'directed_decimal_rounding':True,
    'interval_certified':True,
    'zero_locations_used':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-five-confluent-anchors.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
