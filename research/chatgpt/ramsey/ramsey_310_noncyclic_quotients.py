"""Generate quotient candidates without a cyclic template. Resume labelled SAT enumeration;
WL buckets only index exact isomorphism comparisons. Offset timeouts are not exclusions.
uv run --offline --with python-sat --with networkx python -B <this file> [seconds]
"""
import json,sys
from itertools import combinations
from collections import Counter,defaultdict
from pathlib import Path
from time import monotonic
import networkx as nx
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from ramsey_310_quotient_first import lift,admissible
P=Path(__file__).with_suffix('.json');es=list(combinations(range(13),2));n=len(es);idx={e:i+1 for i,e in enumerate(es)}
def v(i,j):return idx[tuple(sorted((i,j)))]
def graph(m):
    G=nx.empty_graph(13);G.add_edges_from(e for k,e in enumerate(es) if m>>k&1);return G
def block(m):return [-i if m>>(i-1)&1 else i for i in range(1,n+1)]
def run(seconds,min_degree=None,mate_filter=False):
    path=P if min_degree is None else P.with_stem(P.stem+f'_mindeg{min_degree}')
    if mate_filter:path=path.with_stem(path.stem+'_mate')
    if min_degree is not None:assert min_degree in (5,6,7,8,9)
    rec=json.loads(path.read_text()) if path.exists() else {'models':[],'representatives':[]};known=defaultdict(list)
    def key(g):return nx.weisfeiler_lehman_graph_hash(g)
    for r in rec['representatives']:
        g=graph(int(r['mask'],16));known[key(g)].append(g)
    clauses=[];top=n
    for U in combinations(range(13),4):clauses.append([v(i,j) for i,j in combinations(U,2)])
    for i,j in es:
        for U in combinations(set(range(13))-{i,j},3):clauses.append([v(i,j)]+[v(a,u) for a in (i,j) for u in U])
    for i in range(13):
        inc=[v(i,j) for j in range(13) if j!=i]
        for lits,cap in [(inc,8 if mate_filter else 9),([-z for z in inc],12-(min_degree or 5))]:
            enc=CardEnc.atmost(lits,cap,top_id=top,encoding=EncType.seqcounter);top=enc.nv;clauses.extend(enc.clauses)
    # Label vertex zero's neighbors consecutively: every isomorphism class admits this.
    clauses.extend([[-v(0,j+1),v(0,j)] for j in range(1,12)])
    if min_degree is not None:
        # Choose a minimum-degree vertex as zero; its neighbors are a prefix.
        clauses.extend([[v(0,min_degree)],[-v(0,min_degree+1)]])
    with Solver(name='cadical195',bootstrap_with=clauses) as s:
        for z in rec['models']:s.add_clause(block(int(z,16)))
        end=monotonic()+seconds
        while monotonic()<end and s.solve():
            pos=set(s.get_model());m=sum(1<<k for k in range(n) if k+1 in pos);s.add_clause(block(m));rec['models'].append(hex(m));G=graph(m);bucket=known[key(G)]
            if any(nx.is_isomorphic(G,H) for H in bucket):continue
            bucket.append(G);Q=[set(G[i]) for i in G];assert admissible(Q)
            status,rounds=lift(Q,min(3,max(.1,end-monotonic())));rec['representatives'].append({'mask':hex(m),'degrees':sorted(map(len,Q)),'status':status,'refinements':rounds});path.write_text(json.dumps(rec)+'\n')
            if status=='witness':break
    path.write_text(json.dumps(rec)+'\n');print('labelled',len(rec['models']),'classes',len(rec['representatives']),Counter(r['status'] for r in rec['representatives']));print('degree sequences',len({tuple(r['degrees']) for r in rec['representatives']}))
if __name__=='__main__':run(float(sys.argv[1]) if len(sys.argv)>1 else 60,int(sys.argv[2]) if len(sys.argv)>2 else None,'--mate' in sys.argv)
