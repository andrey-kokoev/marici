"""Exact matrix model and admission gate for source-chart pyramid transport."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv2(a):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0];return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def eq(a,b):return a==b
S={'A':[[F(1),F(0)],[F(0),F(1)]],'B':[[F(2),F(0)],[F(0),F(1)]],'C':[[F(1),F(1)],[F(0),F(1)]],'D':[[F(1),F(0)],[F(1),F(2)]]};R={k:inv2(v) for k,v in S.items()};C={(i,j):mm(S[j],R[i]) for i in S for j in S};tri=[]
for i,j,k in (('A','B','C'),('A','B','D'),('A','C','D'),('B','C','D')):tri.append({'face':i+j+k,'strict':eq(mm(C[(j,k)],C[(i,j)]),C[(i,k)])})
tetra=eq(mm(C[('C','D')],mm(C[('B','C')],C[('A','B')])),mm(mm(C[('C','D')],C[('B','C')]),C[('A','B')])) and eq(mm(C[('C','D')],mm(C[('B','C')],C[('A','B')])),C[('A','D')])
def admit(cert):
 req=['common_source_domain','all_charts_bounded','all_ranges_closed','all_charts_bounded_below_on_declared_source_quotient','bounded_image_inverses','source_and_endpoint_provenance','independent_physical_edges_agree_with_transport']
 for x in req:
  if cert.get(x) is not True:return False,x
 return True,'admitted'
valid={x:True for x in ['common_source_domain','all_charts_bounded','all_ranges_closed','all_charts_bounded_below_on_declared_source_quotient','bounded_image_inverses','source_and_endpoint_provenance','independent_physical_edges_agree_with_transport']}
response=dict(valid);response['independent_physical_edges_agree_with_transport']=False
hilbert=dict(valid);hilbert['all_charts_bounded_below_on_declared_source_quotient']=False
checks={'all_triangles_strict':all(x['strict'] for x in tri),'tetrahedron_strict':tetra,'valid_fixture_admitted':admit(valid)==(True,'admitted'),'response_presentation_has_internal_chart_but_external_comparison_open':admit(response)==(False,'independent_physical_edges_agree_with_transport'),'source_forgetting_hilbert_record_refused_at_lower_bound':admit(hilbert)==(False,'all_charts_bounded_below_on_declared_source_quotient')}
out={'schema':'marici.voevodsky.four-chart-transport-analytical-realization-check.v2','triangle_rows':tri,'checks':checks,'passed':all(checks.values()),'current_admission':{'complete_response_internal_chart':True,'external_physical_admitted':admit(response)[0],'external_first_missing_gate':admit(response)[1],'source_forgetting_hilbert_admitted':admit(hilbert)[0],'hilbert_first_missing_gate':admit(hilbert)[1]},'meaning':'Complete response gives an internal fourth chart and strict fillers. External physical identification remains separate, while the source-forgetting Hilbert record fails the lower-bound gate.'}
if __name__=='__main__':
 p=ROOT/'results'/'four-chart-transport-analytical-realization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
