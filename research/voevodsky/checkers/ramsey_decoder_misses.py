from ramsey_paired_decoder_transfer import terms,P,graph,grow,build,verdict,ports,sha256,D,json,Counter,combinations

def run():
    stats=Counter();categories=Counter();examples={};C=json.loads(P.read_text())['families']
    for f in C:
        S=grow(f['rows'],1);es=f['eligible'];old={(k,p,e) for k,p,e,_ in f['pred']};states=[c for v in range(1<<len(es)) if verdict(graph(9,S,c:=sum(1<<e for i,e in enumerate(es) if v>>i&1)))];obs=None
        for k in range(1,9):
            for p in terms(S,k):
                inside=[e for e in es if all(p>>i&1 for i in ports[e])];
                if len(inside)!=1:continue
                e,=inside;stats['demands']+=1
                if not states:stats['no_parent']+=1;continue
                labels=[(c>>e)&1 for c in states];
                if len(set(labels))==1:stats['fixed_red' if labels[0] else 'fixed_blue']+=1;continue
                if (k,p,e) in old:stats['predicted_nonconstant']+=1;continue
                stats['missed_nonconstant']+=1
                if obs is None:obs={(g,m):[verdict(build({g:tuple(i+1 for i in range(5) if m>>i&1)},S,c)) for c in states] for g in range(10) for m in range(32)}
                opp=[(i,j) for i,j in combinations(range(len(states)),2) if labels[i]!=labels[j]];full=(1<<len(opp))-1;sol=[]
                for domain in [(0,9),tuple(g for g in range(10) if g!=k)]:
                    parts={sum(1<<h for h,(i,j) in enumerate(opp) if col[i]!=col[j]):u for u,col in obs.items() if u[0] in domain};covered=0;probes=[]
                    while covered!=full:
                        mask=max(parts,key=lambda t:(t&~covered).bit_count());
                        if not(mask&~covered):break
                        covered|=mask;probes.append(parts[mask])
                    kind='single' if full in parts else 'joint' if covered==full else 'ambiguous';sol.append((kind,probes,None if covered==full else [states[i] for i in opp[next(h for h in range(len(opp)) if not covered>>h&1)]]))
                tag=sol[0][0]+'/'+sol[1][0];categories[tag]+=1;examples.setdefault(tag,dict(rows=f['rows'],gap=k,port_mask=p,edge_index=e,endpoint=sol[0],other=sol[1],states=states))
    print(stats,categories);print(examples);r=D.parent/'ramsey_decoder_misses.json';s=json.dumps(dict(protocol_sha=sha256((D.parent/'ramsey_decoder_miss_protocol.md').read_bytes()).hexdigest(),counts=stats,miss_types=categories,examples=examples),indent=2)+'\n';assert not r.exists() or r.read_text()==s;r.write_text(s)
if __name__=='__main__':run()
