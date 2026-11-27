from ramsey_flank_unfiltered import *
from ramsey_five_port_multi import sevens

def run():
    rows=[s for s in combinations(range(8),3) if min(s[1]-s[0],s[2]-s[1])>=2];out=[];types=Counter();pairs=Counter()
    for ss in combinations(rows,5):
        es=[n for n,(i,j) in enumerate(ports) if not set(ss[i])&set(ss[j])];
        if len(es)!=2:continue
        S=grow(ss,1);bits=[1<<e for e in es];full=sum(bits);cols=[0,*bits,full];parents=[verdict(graph(9,S,c)) for c in cols];
        if not all(parents[1:]):continue
        for gap in range(1,9):
            children=[build({gap:()},S,c) for c in cols];ok=[verdict(g) for g in children];
            if ok!=[False,False,False,True]:continue
            witnesses=[];tags=[]
            for g in children[1:3]:
                d=Counter();examples={}
                for q in sevens(g):
                    mode='X' if gap in q else 'E';assert mode=='X' or (gap-1 in q and gap+1 in q);d[mode]+=1;examples.setdefault(mode,dict(child_sites=[v+1 for v in q if v<10],ports=[v-9 for v in q if v>=10]))
                tags.append(''.join(sorted(d)));witnesses.append(dict(counts=d,examples=examples))
            if not any('E' in t for t in tags):continue
            # With only the other edge red, an E survivor is a singleton target clause:
            # the same seven is killed by setting both edges red.
            for j in range(2):
                if 'E' in tags[j]:types[(tags[j],tags[1-j])]+=1
            pairs[tuple(sorted(tags))]+=1;out.append(dict(rows=[[x+1 for x in s] for s in ss],gap=gap,edges=[[i+1 for i in ports[e]] for e in es],legal_parents=parents,legal_children=ok,only_first_then_only_second=witnesses))
    assert sum(types.values())==12
    r=dict(protocol_sha=sha256((D.parent/'ramsey_conditional_probe_types_protocol.md').read_bytes()).hexdigest(),families=len({tuple(map(tuple,z['rows'])) for z in out}),seam_counts={'/'.join(k):v for k,v in pairs.items()},target_counts={'/'.join(k):v for k,v in types.items()},cases=out);print({k:v for k,v in r.items() if k!='cases'});print(out[0]);save(D.parent/'ramsey_conditional_probe_types.json',r)
if __name__=='__main__':run()
