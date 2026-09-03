import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py')));A,B,det,k=g['A'],g['B'],g['det'],g['k'];st=json.loads((base/'results'/'rh_quarter_endpoint_neville_staircase_diagonal_law.json').read_text())
def recips(M):
 d=[F(1)]+[det([r[:n] for r in M[:n]]) for n in range(1,k+1)];p=[d[n]/d[n-1] for n in range(1,k+1)];return [str(p[n]/p[n+1]) for n in range(len(p)-1)]
def vals(x):return [v[0] for _,v in sorted((int(h),v) for h,v in st[x+'_by_distance'].items())]
a,b=vals('A'),vals('B');ra,rb=recips(A),recips(B);checks={'A_tail_alignment':a[1:]==ra[:len(a)-1],'B_alignment':b==rb[:len(b)],'A_boundary_positive':F(a[0])>0};r={'schema':'marici.strominger.rh_quarter_endpoint_neville_vs_routh_pivots.v2','status':'passed' if all(checks.values()) else 'failed','verdict':'Interior staircase weights align with reciprocal consecutive Routh-pivot ratios; A has one positive boundary chip.','A_weights':a,'B_weights':b,'checks':checks};(base/'results'/'rh_quarter_endpoint_neville_vs_routh_pivots.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
