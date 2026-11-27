"""Observation ceiling using non-target gaps. No rejection reasons in the signature."""
from ramsey_forced_edge_transfer import *
from collections import defaultdict

def run():
    families=json.loads(C.read_text())['families'];previous=json.loads((D.parent/'ramsey_endpoint_ceiling.json').read_text());by=defaultdict(list)
    for r in previous['details']:by[r['family']].append(r)
    stats=Counter();examples={};details=[]
    for idx,targets in by.items():
        f=families[idx-129];S=grow(f['rows'],1);es=f['eligible'];states=[c for m in range(1<<len(es)) if verdict(graph(9,S,c:=sum(1<<e for j,e in enumerate(es) if m>>j&1)))];obs={(g,h):[verdict(build({g:tuple(i+1 for i in range(5) if h>>i&1)},S,c)) for c in states] for g in range(10) for h in range(32)}
        for t in targets:
            k=t['target_gap'];e=ports.index(tuple(i-1 for i in t['edge']));opp=[(i,j) for i,j in combinations(range(len(states)),2) if (states[i]^states[j])>>e&1];full=(1<<len(opp))-1;parts={u:sum(1<<n for n,(i,j) in enumerate(opp) if b[i]!=b[j]) for u,b in obs.items() if u[0]!=k};left=full;probes=[]
            while left:
                u=max(parts,key=lambda u:(parts[u]&left).bit_count());
                if not(parts[u]&left):break
                left&=~parts[u];probes.append(u)
            gaps={}
            for (g,h),v in parts.items():gaps[g]=gaps.get(g,0)|v
            kind='ambiguous' if left else 'single_probe' if full in parts.values() else 'joint_one_gap' if full in gaps.values() else 'joint_multigap';stats[kind]+=1;d=dict(family=idx,target=k,edge=t['edge'],kind=kind);details.append(d)
            if kind in examples:continue
            w=dict(d,rows=[[x+1 for x in s] for s in f['rows']],target_ports=t['target_ports']);examples[kind]=w
            if left:
                i,j=opp[(left&-left).bit_length()-1];assert all(b[i]==b[j] for u,b in obs.items() if u[0]!=k);w['parent_red_edges']=[[[v+1 for v in ports[n]] for n in es if c>>n&1] for c in (states[i],states[j])];
                for c in [states[i],states[j]]:
                    a=graph(9,S,c);qs={frozenset(i-8 for i in q if i>=9) for q in combinations(sorted(set(range(14))-{k-1,k}),6) if all(not a[i]>>j&1 for i,j in combinations(q,2))};p=frozenset(t['target_ports']);assert (p in qs and not any(q<p for q in qs))==(not(c>>e&1))
            else:
                if kind=='joint_one_gap':
                    g=next(g for g in gaps if gaps[g]==full);left=full;probes=[]
                    while left:
                        u=max((u for u in parts if u[0]==g),key=lambda u:(parts[u]&left).bit_count());left&=~parts[u];probes.append(u)
                w['probes']=[(g,[j+1 for j in range(5) if h>>j&1]) for g,h in probes];w['decoder']={''.join(str(int(obs[u][i])) for u in probes):int(not (c>>e&1)) for i,c in enumerate(states)}
    assert sum(stats.values())==108;out=dict(protocol_sha=sha256((D.parent/'ramsey_interior_ceiling_protocol.md').read_bytes()).hexdigest(),counts=stats,examples=examples,details=details);print(stats,examples);save(D.parent/'ramsey_interior_ceiling.json',out)
if __name__=='__main__':run()
