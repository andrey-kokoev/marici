#!/usr/bin/env python3
"""Two endpoint channels as the complete homogeneous solution of the history wave operator."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
rows=[]
for m in range(2,11):
 events=[(i,j) for i in range(1,m+1) for j in range(i,m+1)];pos={e:k for k,e in enumerate(events)};plaquettes=[(i,j) for i in range(2,m+1) for j in range(i,m)];D=s.zeros(len(plaquettes),len(events))
 for r,(i,j) in enumerate(plaquettes):
  for e,c in (((i,j),1),((i-1,j),-1),((i,j+1),-1),((i-1,j+1),1)):D[r,pos[e]]=c
 # Endpoint-only columns a_i and b_j; remove b_1 to quotient common-constant redundancy.
 cols=[]
 for a in range(1,m+1):cols.append(s.Matrix([1 if i==a else 0 for i,j in events]))
 for b in range(2,m+1):cols.append(s.Matrix([1 if j==b else 0 for i,j in events]))
 H=s.Matrix.hstack(*cols);rows.append({'m':m,'field_dimension':len(events),'wave_constraints':D.rank(),'homogeneous_dimension':len(events)-D.rank(),'expected_two_channel_dimension':2*m-1,'endpoint_sum_span_rank':H.rank(),'endpoint_sum_annihilated':D*H==s.zeros(D.rows,H.cols),'endpoint_sum_exhausts_kernel':D*H==s.zeros(D.rows,H.cols) and H.rank()==len(events)-D.rank()})
checks={'homogeneous_dimension_is_two_m_minus_one':all(x['homogeneous_dimension']==x['expected_two_channel_dimension'] for x in rows),'all_endpoint_sums_are_source_free':all(x['endpoint_sum_annihilated'] for x in rows),'two_endpoint_channels_exhaust_all_source_free_fields':all(x['endpoint_sum_exhausts_kernel'] for x in rows),'tested_m2_through_m10':len(rows)==9}
out={'schema':'marici.nima.nnmhv-two-channel-null-solution-bridge.v1','wave_equation':'Delta_u Delta_v f=0','general_solution':'f(i,j)=A(i)+B(j), with gauge A->A+c and B->B-c','channels':{'lower_endpoint':'A(i)','upper_endpoint':'B(j)'},'rows':rows,'checks':checks,'passed':all(checks.values()),'meaning':'The two-channel split is the complete null-space decomposition of the discrete history d’Alembertian. Two endpoint currents are not an imposed compression: they are the left- and right-moving homogeneous modes, modulo one shared constant.','bridges':['left/right movers of the massless wave equation','endpoint insertion/reflow channels','Hodge decomposition into source and homogeneous sectors','two-channel boundary data','constant gauge redundancy']};p=ROOT/'research/nima/results/nnmhv-two-channel-null-solution-bridge.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'wave_equation':out['wave_equation'],'general_solution':out['general_solution'],'checks':checks,'meaning':out['meaning'],'bridges':out['bridges'],'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
