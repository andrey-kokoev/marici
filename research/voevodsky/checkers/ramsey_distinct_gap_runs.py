from itertools import combinations
from collections import Counter
from ramsey_contact_path_parity import D, json, save, sha256, path_capacity
from ramsey_relative_sign_joint_context import graph,grow,verdict


def run():
    gaps=list(combinations(range(9),2)); table={}; mask_counts=Counter()
    for u in range(256):
        blocked={k for k in range(8) if u>>k&1};base=path_capacity(8,u)
        def run_at(f):
            left=max((k for k in blocked if k<f),default=-1);right=min((k for k in blocked if k>=f),default=8)
            return left,right-left-1
        for f,g in gaps:
            a,n=run_at(f);b,m=run_at(g);naive=base+int(n%2==0)+int(m%2==0);pred=base+1 if a==b else naive
            shifted=sum(1<<(k+(k>=f)+(k>=g)) for k in blocked);assert pred==path_capacity(10,shifted)
            table[u,f,g]=(pred,naive);mask_counts[pred-naive]+=1
    old=json.loads((D.parent/'ramsey_double_flank_contact.json').read_text());families={tuple(map(tuple,c['rows'])) for z in old['charts'] for c in z['cases'] if c['gap'] in (z['first'],z['first']+1)};assert len(families)==40
    tally=Counter();examples={};pairs=list(combinations(range(5),2))
    for ss in sorted(families):
        rows=[tuple(k-1 for k in s) for s in ss];edges=[e for e in pairs if set(rows[e[0]]).isdisjoint(rows[e[1]])];assert len(edges)==2
        for red in ([],edges[:1],edges[1:],edges):
            color=sum(1<<pairs.index(e) for e in red);options=[]
            for p in range(32):
                if any(p>>i&1 and p>>j&1 for i,j in red):continue
                u=sum(1<<k for k in set().union(*(rows[i] for i in range(5) if p>>i&1)));options.append((p.bit_count(),u))
            for f,g in gaps:
                values=[(k+x,k+y) for k,u in options for x,y in [table[u,f,g]]];actual,naive=map(max,zip(*values));assert (actual<7)==verdict(graph(10,grow(grow(rows,g),f),color))
                status='false_accept' if actual>=7>naive else 'false_reject' if naive>=7>actual else 'agree';tally[status]+=1
                if status!='agree' and status not in examples:examples[status]=dict(rows=ss,red=[(i+1,j+1) for i,j in red],gaps=(f,g),actual=actual,naive=naive)
    out=dict(mask_delta=dict(mask_counts),decisions=dict(tally),examples=examples,protocol_sha=sha256((D.parent/'ramsey_distinct_gap_runs_protocol.md').read_bytes()).hexdigest());print(out);save(D.parent/'ramsey_distinct_gap_runs.json',out)

if __name__=='__main__':run()
