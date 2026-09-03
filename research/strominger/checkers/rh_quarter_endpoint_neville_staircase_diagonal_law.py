import json
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/'results'/'rh_quarter_endpoint_neville_minor_ratio_formula.json').read_text())
def groups(rs):
 d={}
 for x in rs:d.setdefault(2*x['column']-x['row'],set()).add(x['elimination'])
 return {str(k):sorted(v) for k,v in sorted(d.items())}
a,b=groups(src['A_records']),groups(src['B_records']);checks={'A_singletons':all(len(v)==1 for v in a.values()),'B_singletons':all(len(v)==1 for v in b.values()),'distinct':a!=b};r={'schema':'marici.strominger.rh_quarter_endpoint_neville_staircase_diagonal_law.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'Neville weights depend only on h=2*column-row in the bounded endpoint matrices.','A_by_distance':a,'B_by_distance':b,'checks':checks};(base/'results'/'rh_quarter_endpoint_neville_staircase_diagonal_law.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
