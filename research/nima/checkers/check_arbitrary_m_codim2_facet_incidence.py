#!/usr/bin/env python3
"""Enumerate the arbitrary-m codimension-two incidence skeleton of type-A facets."""
from itertools import combinations
from pathlib import Path
from math import comb
import json
R=Path(__file__).resolve().parents[3]
def cross(a,b):x,y=a;u,v=b;return x<u<y<v or u<x<v<y
rows=[];a3=None
for m in range(2,21):
 n=m+3;boundary={tuple(sorted((i,(i+1)%n))) for i in range(n)};facets=sorted((i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in boundary);pos={(i-1,j+1) for i in range(1,m+1) for j in range(i,m+1)}
 strata=[]
 for a,b in combinations(facets,2):
  if cross(a,b):continue
  lane=('P' if a in pos else 'N')+('P' if b in pos else 'N');lane='PN' if lane in ('PN','NP') else lane
  strata.append({'facets':[list(a),list(b)],'root_lane':lane})
 lane_counts={k:sum(z['root_lane']==k for z in strata) for k in ['PP','PN','NN']}
 formulas={'PP':2*comb(m+2,4),'PN':m*(m-1)*(m+1)//3,'NN':comb(m,2)}
 row={'m':m,'facet_count':len(facets),'codim2_strata':len(strata),'root_lane_counts':lane_counts,'closed_form_lane_counts':formulas,'closed_forms_match':lane_counts==formulas,'every_stratum_two_facets':all(len(z['facets'])==2 for z in strata),'all_pairs_noncrossing':all(not cross(*[tuple(q) for q in z['facets']]) for z in strata)};rows.append(row)
 if m==3:
  # Number of clusters containing a diagonal distinguishes square (4) and pentagon (5) A3 facets.
  clusters=[c for c in combinations(facets,3) if all(not cross(x,y) for x,y in combinations(c,2))]
  ftype={d:('square' if sum(d in c for c in clusters)==4 else 'pentagon') for d in facets}
  type_counts={}
  for z in strata:
   ts=tuple(sorted(ftype[tuple(q)] for q in z['facets']));key='+'.join(ts);type_counts[key]=type_counts.get(key,0)+1
  a3={'strata':strata,'parent_facet_type_counts':type_counts,'facet_types':{str(k):v for k,v in ftype.items()}}
checks={'m2_to_m20':len(rows)==19,'a3_has_21_codim2_strata':next(x for x in rows if x['m']==3)['codim2_strata']==21,'all_typed_by_two_facets':all(x['every_stratum_two_facets'] for x in rows),'all_are_compatible_pairs':all(x['all_pairs_noncrossing'] for x in rows),'lane_partition_complete':all(sum(x['root_lane_counts'].values())==x['codim2_strata'] for x in rows),'closed_form_counts_match':all(x['closed_forms_match'] for x in rows),'a3_three_squares_six_pentagons':list(a3['facet_types'].values()).count('square')==3 and list(a3['facet_types'].values()).count('pentagon')==6}
out={'schema':'marici.nima.arbitrary-m-codim2-facet-incidence.v2','theorem':'Codimension-two intersections of type-A_m associahedron facets are exactly unordered compatible (noncrossing) pairs of polygon diagonals. Under the positive/negative-simple partition their counts are PP=2*C(m+2,4), PN=m(m-1)(m+1)/3, and NN=C(m,2). The history-to-facet compiler therefore gives a complete combinatorial index for every shared facet-residue test.','rows':rows,'a3':a3,'checks':checks,'passed':all(checks.values()),'residue_contract_per_stratum':['two parent facet identifiers','source history or boundary-completion preimages','oriented canonical residue from each parent','common positroid representative or proof of no shared physical stratum','exact chart transition and logarithmic Jacobian sign','coefficientwise sum and external/contracted disposition'],'claim_boundary':'This enumerates the complete combinatorial codimension-two test set. It does not supply canonical residues or prove cancellation.'}
p=R/'research/nima/results/arbitrary-m-codim2-facet-incidence.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='a3'},indent=2));print('A3 parent types:',a3['parent_facet_type_counts']);raise SystemExit(0 if out['passed'] else 1)
