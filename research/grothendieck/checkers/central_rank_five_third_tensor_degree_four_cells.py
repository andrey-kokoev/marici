"""Degree-four third-tensor variation at the two extreme rank-five cells."""
import itertools, json
from decimal import Decimal as D
from pathlib import Path

import central_rank_five_third_tensor_interval_anchor as T

T.P.ORDER = 4
T.P.multiindices = [key for key in itertools.product(range(5), repeat=5) if sum(key) <= 4]
results = [T.evaluate(['0']*5), T.evaluate(['.01']*5)]
result = {'extreme_cells':results,
          'maximum_retained_third_tensor_variation':str(max(
              D(row['third_tensor_variation_from_retained_higher_degrees']) for row in results)),
          'degree_five_and_higher_remainder_included':False,
          'interval_certified_for_degree_four_jet':True,
          'rh_proved':False}

if __name__ == '__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-five-third-tensor-degree-four-cells.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
