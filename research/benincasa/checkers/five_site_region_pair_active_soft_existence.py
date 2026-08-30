import json
from pathlib import Path

base=json.loads(Path('research/benincasa/results/five-site-region-pair-active-soft-blowup.json').read_text())
assert base['representative']==['g_123','g_125']

# Active wall equations are q1=3t+y3+y5 and q2=3t+y2+y4.
cases=[
 {'soft':'y2=0','equality':'y4=y3+y5','segment':'C2 lies on the geodesic segment joining C3 and C5'},
 {'soft':'y3=0','equality':'y5=y2+y4','segment':'C3 lies on the geodesic segment joining C2 and C4'},
 {'soft':'y4=0','equality':'y2=y3+y5','segment':'C4 lies on the geodesic segment joining C3 and C5'},
 {'soft':'y5=0','equality':'y3=y2+y4','segment':'C5 lies on the geodesic segment joining C2 and C4'},
]
assert len(cases)==base['active_soft_occurrence_count']==4

packet={
 'schema':'marici.five_site_region_pair_active_soft_existence.v1',
 'active_walls':['q_1=3*t+y3+y5','q_2=3*t+y2+y4'],
 'cases':cases,
 'necessary_and_sufficient_metric_condition':'at the soft center, equality of the two active wall distance sums; equivalently one labelled triangle inequality is saturated',
 'carrier_support':'existing edge-soft divisor intersect existing three-center Gram/triangle-equality divisor with segment chamber',
 'generic_edge_soft_existence':False,
 'source_coefficient_status':'still uncomputed on the supported endpoint locus',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-active-soft-existence.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('generic_edge_soft_existence','necessary_and_sufficient_metric_condition','carrier_support','source_coefficient_status','new_carrier_datum')},sort_keys=True))
