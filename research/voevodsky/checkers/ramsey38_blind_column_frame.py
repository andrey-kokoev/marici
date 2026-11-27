"""Can visible structure order the seven columns before two rows are revealed?"""
from ramsey38_excel_fold_transport import prev,json,gzip,graph,Counter,combinations,sys,rule
from itertools import permutations,product
from math import factorial,prod
P=prev.out/'ramsey38_blind_column_frame_protocol.json';R=prev.out/'ramsey38_blind_column_frame.json'
protocol=dict(start=310193,records=128,root='least degree-seven; all unordered pairs of outside vertices',mask='Before ranking, erase all 14 incidences from the two marked rows to the seven columns. Root, columns, masked pair, remaining rows are four distinct initial classes. Keep both masked rows interchangeable. Mask location known; neither color revealed.',rule='Refine by (old color, sorted multiset of visible red neighbor colors) until stable. Assign integer colors in lexical signature order at every round. Root first, column classes in ascending color order; all within-class permutations equally admissible. No vertex-ID tie breaks.',questions='Could a marked-graph automorphism cycle five columns? Necessary only: a stable class has >=5. How many column frames remain? For held-out overlap-eligible pairs, check old mirrored Excel word pair in the ordered classes; count possible, forced and expected hits for uniformly tied order vs unconstrained 1/210.')

def frame(g,u,L,hidden):
    colors={v:0 if v==u else 1 if v in L else 2 if v in hidden else 3 for v in g};adj={v:(g[v]-hidden if v in L else g[v]-L if v in hidden else g[v]) for v in g}
    while True:
        sig={v:(colors[v],tuple(sorted(colors[w] for w in adj[v]))) for v in g};ids={s:i for i,s in enumerate(sorted(set(sig.values())))};nxt={v:ids[s] for v,s in sig.items()}
        done=len(set(colors.values()))==len(ids);colors=nxt
        if done:break
    return [tuple(v for v in L if colors[v]==c) for c in sorted({colors[v] for v in L})]

def run():
    assert json.loads(P.read_text())==protocol;cnt=Counter();hist=Counter();expected=0;examples=[]
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i<protocol['start']:continue
            if i>=protocol['start']+protocol['records']:break
            g=graph(line.strip());cnt['records']+=1;u=next((v for v in sorted(g) if len(g[v])==7),None)
            if u is None:continue
            L=g[u];cnt['roots']+=1
            for x,y in combinations(sorted(set(g)-L-{u}),2):
                blocks=frame(g,u,L,{x,y});count=prod(factorial(len(q)) for q in blocks);hist[count]+=1;cnt['not_excluded_C5']+=max(map(len,blocks))>=5
                s,t=g[x]&L,g[y]&L
                if not(len(s)==len(t)==3 and len(s&t)==2):continue
                cnt['eligible']+=1;hits=0
                for ps in product(*(permutations(q) for q in blocks)):
                    cols=(u,)+sum(ps,());words={' '.join('R' if v in row else 'B' for v in cols).replace(' ','') for row in (s,t)};hits+=words==set(rule['words'])
                cnt['possible']+=hits>0;cnt['forced']+=hits==count;expected+=hits/count
                if hits and len(examples)<8:examples.append(dict(record=i,root=u,rows=[x,y],classes=blocks,hits=hits,frames=count))
    print(cnt,hist,expected);prev.save(R,dict(protocol_sha=prev.sha(P.read_bytes()),counts=dict(cnt),frame_histogram=dict(hist),fractional_hits=expected,uniform_expected=cnt['eligible']/210,examples=examples))
if __name__=='__main__':{'freeze':lambda:prev.save(P,protocol),'test':run}[sys.argv[1]]()
