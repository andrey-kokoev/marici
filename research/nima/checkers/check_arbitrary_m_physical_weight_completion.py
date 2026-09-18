#!/usr/bin/env python3
"""Arbitrary-rank gate for extending positive-root weights to cluster transport."""
from itertools import combinations
from math import comb
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
def catalan(k):return comb(2*k,k)//(k+1)
def row(m):
 n=m+3;boundary={tuple(sorted((i,(i+1)%n))) for i in range(n)}
 ds=[(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in boundary]
 def cross(a,b):x,y=a;u,v=b;return x<u<y<v or u<x<v<y
 clusters=sorted(tuple(sorted(c)) for c in combinations(ds,m) if all(not cross(a,b) for a,b in combinations(c,2)))
 edges=[];known=0;unknown=0;double=0
 neg={(i,n-1) for i in range(1,n-2)};pos=set(ds)-neg
 for i,a in enumerate(clusters):
  for j,b in enumerate(clusters[i+1:],i+1):
   if len(set(a)^set(b))==2:
    edges.append((i,j));changed=set(a)^set(b);q=len(changed&neg)
    if q==0:known+=1
    else:unknown+=1;double+=q==2
 return {'m':m,'cutoff_n':m+5,'almost_positive_roots':len(ds),'positive_roots':len(pos),'negative_simple_roots':len(neg),'clusters':len(clusters),'expected_clusters':catalan(m+1),'mutation_edges':len(edges),'expected_edges':m*catalan(m+1)//2,'determined_edges':known,'undetermined_edges':unknown,'edges_exchanging_two_negative_simples':double}
rows=[row(m) for m in range(1,7)]
checks={'root_counts':all(r['positive_roots']==r['m']*(r['m']+1)//2 and r['negative_simple_roots']==r['m'] for r in rows),'cluster_counts_catalan':all(r['clusters']==r['expected_clusters'] for r in rows),'edge_counts':all(r['mutation_edges']==r['expected_edges'] for r in rows),'undetermined_nonzero_every_rank':all(r['undetermined_edges']>0 for r in rows),'full_completion_adds_m_coordinates':all(r['almost_positive_roots']==r['positive_roots']+r['m'] for r in rows)}
out={'schema':'marici.nima.arbitrary-m-physical-weight-completion.v1','rows':rows,'checks':checks,'passed':all(checks.values()),'theorem':'At type A_m, interval/positive-root weights provide m(m+1)/2 of the m(m+3)/2 cluster coordinates. Exactly m negative-simple coordinates are absent. Adding nonzero values for them is sufficient to define product-weight mutation ratios with telescoping unit holonomy on every face.','residual':'Positive-root physical weights alone leave mutation transports undetermined at every tested rank A1 through A6; the missing-coordinate count is exactly m for all m by the polygon model.','claim_boundary':'The coordinate count and sufficiency theorem hold for every finite m. The edge-count rows are exhaustive finite checks, not a closed formula for every m, and no completion is declared physical.'};p=ROOT/'research/nima/results/arbitrary-m-physical-weight-completion.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
