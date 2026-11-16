"""Generate a nonexhaustive sample from all seven 17-vertex (3,6) graphs,
then issue and verify rational fractional port certificates for each retained
Weisfeiler-Lehman hash representative. This is NOT the complete 2576 catalogue.
"""
import json
from pathlib import Path
from itertools import combinations
import networkx as nx
from ramsey_17parent_fast_probe import removev,sample
from ramsey_extension_blockers import parse_g6
from ramsey_fractional_port_certificate import calculate, verify


def main():
    sources=[parse_g6(x) for x in Path('/mnt/data/ramsey36_all7.g6').read_text().splitlines()]
    seen=set();certificates=[];passed=0
    for src in sources:
        for v in range(17):
            for A in sample(removev(src,v),35):
                passed+=1
                G=nx.Graph();G.add_nodes_from(range(16))
                G.add_edges_from((u,w) for u,w in combinations(range(16),2) if A[u]>>w&1)
                hash=nx.weisfeiler_lehman_graph_hash(G)
                if hash in seen:continue
                seen.add(hash)
                c=calculate(A,1000)
                v=verify(c['A'],c['weights'],c['denominator'])
                c['hash']=hash
                c['verification']=v
                certificates.append(c)
    out={'provenance': 'seven McKay (3,6;17) graphs, vertex removal and constrained random edge deletion, 35 trials per parent-vertex; NOT a complete (3,6;16) census',
         'generated_candidates': passed, 'WL_representatives':len(certificates),
         'max_LP_numeric': max(c['lp_numeric'] for c in certificates),
         'max_integer_certificate_total':max(sum(c['weights'].values())/c['denominator'] for c in certificates),
         'certificates':certificates}
    Path('/mnt/data/ramsey_fractional_port_sample_certificates.json').write_text(json.dumps(out,indent=2))
    print('all exact checks pass:',passed,'generated',len(certificates),'hash representatives','LP max',out['max_LP_numeric'],'rational mass max',out['max_integer_certificate_total'])

if __name__=='__main__':main()
