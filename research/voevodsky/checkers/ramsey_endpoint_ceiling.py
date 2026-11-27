from ramsey_forced_edge_transfer import *

def run():
    data=json.loads(C.read_text());st=Counter();ex={};details=[]
    for idx,f in enumerate(data['families'],129):
        S=grow(f['rows'],1);es=f['eligible'];states=[c for m in range(1<<len(es)) if verdict(graph(9,S,c:=sum(1<<e for j,e in enumerate(es) if m>>j&1)))];obs=None
        for k,p,e,_,new in f['targets']:
            if new:continue
            opp=[(i,j) for i,j in combinations(range(len(states)),2) if (states[i]^states[j])>>e&1];
            if not opp:continue
            if obs is None:obs={(g,h):tuple(verdict(build({g:tuple(i+1 for i in range(5) if h>>i&1)},S,c)) for c in states) for g in (0,9) for h in range(32)}
            full=(1<<len(opp))-1;parts={sum(1<<n for n,(i,j) in enumerate(opp) if b[i]!=b[j]):q for q,b in obs.items()};left=full;probes=[]
            while left:
                m=max(parts,key=lambda v:(v&left).bit_count());
                if not m&left:break
                left &= ~m;probes.append(parts[m])
            kind='ambiguous' if left else 'single' if full in parts else 'joint';st[kind]+=1;row=dict(family=idx,target_gap=k,target_ports=[i+1 for i in range(5) if p>>i&1],edge=[i+1 for i in ports[e]],kind=kind);details.append(row)
            if kind in ex:continue
            x=dict(row,rows=[[v+1 for v in s] for s in f['rows']]);ex[kind]=x
            if left:
                i,j=opp[(left&-left).bit_length()-1];assert all(b[i]==b[j] for b in obs.values());x['indistinguishable_red_port_edges']=[[[i+1 for i in ports[n]] for n in es if states[t]>>n&1] for t in (i,j)]
            else:x['probes']=[(g,[i+1 for i in range(5) if h>>i&1]) for g,h in probes]
            for c in states:
                a=graph(9,S,c);raw={sum(1<<(v-9) for v in q if v>=9) for q in combinations(sorted(set(range(14))-{k-1,k}),6) if all(not a[i]>>j&1 for i,j in combinations(q,2))};assert (p in {s for s in raw if not any(t!=s and t&s==t for t in raw)})== (not(c>>e&1))
    assert sum(st.values())==108;out=dict(protocol_sha=sha256((D.parent/'ramsey_endpoint_ceiling_protocol.md').read_bytes()).hexdigest(),counts=st,examples=ex,details=details);print(st,ex);save(D.parent/'ramsey_endpoint_ceiling.json',out)
if __name__=='__main__':run()
