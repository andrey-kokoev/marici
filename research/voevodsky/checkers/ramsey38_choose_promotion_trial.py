"""Choose one legal red addition from competing promotions on the SAME visible base graph."""
from ramsey38_named_gain_trial import prev,graph,gzip,templates,face,screen,find,json,combinations
from ramsey38_polygon_endpoint_rule import compatible
import sys
P=prev.out/'ramsey38_choose_promotion_predictions.json';R=prev.out/'ramsey38_choose_promotion_comparison.json'
protocol='First four distinct records after 411, first root in label order with seven columns, supports <=4, at least two legal single red additions growing a size-three support, and an edge target. Request every size-two row separately. Goal: sole release of target with promoted triangle buried. Rank shell/move by number of compatible tips, then lexical (changed row,column,boundary,tip). Verify graph and selected shell/tip independently; exhaust alternatives and test whether release existed before addition.'
def setup(g,u):
    L=sorted(g[u]);rs={x:sum(1<<i for i,v in enumerate(L) if v in g[x]) for x in set(g)-set(L)-{u}};moves=sorted((x,v) for x,s in rs.items() if s.bit_count()==3 for i,v in enumerate(L) if not s>>i&1 and not g[x]&g[v]);return L,rs,moves

def shells(rs,j,S):
    for bd,cl in templates():
        if S is not None and S in cl:continue
        if rs[j] not in cl and all(k==j or s.bit_count()==4 or s in cl for k,s in rs.items()):yield bd

def options(L,rs,moves,j,verify=False):
    if verify:from ramsey38_release_census import first_ball
    out=[];dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1)
    for x,v in moves:
        S=rs[x];red={**rs,x:S|1<<L.index(v)}
        for bd in shells(red,j,S):
            ps=[];cert={}
            for i,w in enumerate(L):
                if red[x]>>i&1:continue
                req=set(red.values())|{S|1<<i}
                if verify:
                    o=first_ball(bd,req)
                    if o:ps.append(w);cert[w]=[sorted(L[t] for t in c) for c in o]
                else:
                    rf=set(map(face,req));fs=set(map(face,bd));
                    if screen(frozenset(range(7)),rf,fs)=='pass' and not find(rf|fs,fs) and compatible(set(map(dec,bd)),set(map(dec,req))):ps.append(w)
            if ps:out.append(dict(edge=[x,v],bd=sorted(bd),tips=ps,**(dict(certificates=cert) if verify else {})))
    return sorted(out,key=lambda d:(-len(d['tips']),d['edge'],d['bd']))

def freeze():
    es=[]
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i<=411:continue
            word=line.strip();g=graph(word)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,moves=setup(g,u);targets=sorted(j for j,s in rs.items() if s.bit_count()==2)
                if len(moves)<2 or not targets or max(map(int.bit_count,rs.values()))>4:continue
                preds=[]
                for j in targets:
                    opts=options(L,rs,moves,j);preds.append(dict(row=j,choice=opts[0] if opts else None))
                es.append(dict(record=i,word=word,u=u,moves=moves,requests=preds));break
            if len(es)==4:break
    assert len(es)==4;prev.save(P,dict(protocol=protocol,cases=es));print([(e['record'],e['u'],len(e['requests'])) for e in es])
def legal(g):
    def indep(p,k):
        if k==0:return True
        while len(p)>=k:
            a=min(p);p=p-{a}
            if indep(p-g[a],k-1):return True
        return False
    return all(not(g[a]&g[b]) for a in g for b in g[a]) and not indep(set(g),8)
def compare():
    from ramsey38_release_census import first_ball
    out=[]
    for e in json.loads(P.read_text())['cases']:
        g=graph(e['word']);L,rs,moves=setup(g,e['u']);assert list(map(list,moves))==e['moves']
        for x,v in moves:
            h={w:set(s) for w,s in g.items()};h[x].add(v);h[v].add(x);assert legal(h)
        for d in e['requests']:
            j=d['row'];opts=options(L,rs,moves,j,True);base=any(first_ball(bd,set(rs.values())) for bd in shells(rs,j,None));ch=d['choice'];hit=bool(ch and any(z['edge']==ch['edge'] and z['bd']==ch['bd'] and ch['tips'][0] in z['tips'] for z in opts));wins=sorted({tuple(z['edge']) for z in opts});print(e['record'],j,ch and ch['edge'],hit,wins,'base',base);out.append(dict(record=e['record'],root=e['u'],row=j,legal_moves=moves,successful_moves=wins,first_fills=hit,base_release=base,options=opts))
    prev.save(R,dict(prediction_sha=prev.sha(P.read_bytes()),results=out))
if __name__=='__main__':{'freeze':freeze,'compare':compare}[sys.argv[1]]()
