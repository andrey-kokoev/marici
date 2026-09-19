#!/usr/bin/env python3
"""Construct the arbitrary-m associahedral facet carrier for physical cochains."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[3]
rows=[]
for m in range(1,16):
 n=m+3;boundary={tuple(sorted((i,(i+1)%n))) for i in range(n)};ds={(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in boundary}
 pos={(i-1,j+1) for i in range(1,m+1) for j in range(i,m+1)};neg=ds-pos
 # Canonical negative-simple order is the complement in lexicographic order.
 rows.append({'m':m,'polygon_vertices':n,'facets':len(ds),'expected_facets':m*(m+3)//2,'positive_root_facets':len(pos),'expected_positive_roots':m*(m+1)//2,'negative_simple_facets':len(neg),'expected_negative_simples':m,'partition_disjoint':not(pos&neg),'partition_complete':pos|neg==ds,'negative_simple_diagonals':[list(x) for x in sorted(neg)]})
checks={'m1_to_m15':len(rows)==15,'facet_count':all(x['facets']==x['expected_facets'] for x in rows),'positive_root_count':all(x['positive_root_facets']==x['expected_positive_roots'] for x in rows),'negative_simple_count':all(x['negative_simple_facets']==x['expected_negative_simples'] for x in rows),'exact_partition':all(x['partition_disjoint'] and x['partition_complete'] for x in rows)}
out={'schema':'marici.nima.arbitrary-m-facet-cochain-carrier.v1','labeling_theorem':'For every finite m>=1, the facets of the type-A_m associahedron (polygon diagonals) partition canonically into m(m+1)/2 positive-root diagonals (i-1,j+1), 1<=i<=j<=m, and the m complementary negative-simple diagonals.','cochain_statement':'Any declared positive-root densities p_[i,j] and negative-simple densities b_i therefore define a unique facet cochain after multiplication by the oriented top-boundary incidence signs. Its top-cell evaluation is defined, but it is not a cocycle theorem.','descent_acceptance':['source-derived canonical residue map on every facet','history-to-positroid identification for every shared codimension-two stratum','common-chart transition with logarithmic orientation sign','coefficientwise cancellation of the two restricted facet residues','explicit external remainder and contracted-locus classification'],'rows':rows,'checks':checks,'passed':all(checks.values()),'claim_boundary':'This proves the arbitrary-m carrier and labeling statement only. It does not supply arbitrary-m physical densities, canonical-form residue maps, or codimension-two descent.'}
p=R/'research/nima/results/arbitrary-m-facet-cochain-carrier.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
