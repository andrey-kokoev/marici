"""Prospective 7→8 transfer probe: does a table square survive on ONE labelling?"""
from itertools import combinations
from collections import Counter
import gzip,json,sys
from ramsey38_choose_promotion_trial import graph,setup,prev
P=prev.out/'ramsey38_excel_square_protocol.json';R=prev.out/'ramsey38_excel_square_transfer.json'
protocol=dict(start=310001,records=64,selection='Consecutive catalogue records; least degree-seven root per record, no filtering by supports. Report records without a root separately.',prediction='At each eligible root the 4 rows {1,i,j}, i=4,5 and j=7,8, are jointly realizable on a single injection of the five active table columns to the seven red-neighbor labels, with four distinct outside rows. The unused columns can be assigned arbitrarily to unused anchors including the root. This is necessary incidence, not a graph generator.',primary='On the five active labels each row has exactly its three specified reds. Extra reds on inactive columns allowed.',relaxation='Ignore extra reds even on active labels, still demand four distinct outside rows and a common map.',controls='Maximum number of square corners jointly realized under each criterion, keeping table column 1 fixed across corners. 4 required for success; one or two corners are not a square. Do not count alternate embeddings as additional root predictions.')

def best(labels,rows):
    scores=[0,0];witness=[None,None]
    for a in labels:
        others=sorted(set(labels)-{a})
        for pair in combinations(others,2):
            for tips in combinations(sorted(set(others)-set(pair)),2):
                if pair>tips:continue # the existence score is invariant under swapping the two axes
                active={a,*pair,*tips};corners=[{a,i,j} for i in pair for j in tips];options=[[v for v,s in rows.items() if c<=s] for c in corners];strict=[next((v for v in vs if rows[v]&active==c),None) for c,vs in zip(corners,options)];n=sum(v is not None for v in strict)
                def save(h,n,vs):
                    if n>scores[h]:scores[h]=n;witness[h]=dict(columns=[a,*pair,*tips],rows=vs)
                save(0,n,strict)
                if sum(bool(x) for x in options)>scores[1]:
                    def match(i,used,chosen):
                        if i==4:save(1,len(used),chosen);return
                        for v in options[i]:
                            if v not in used:match(i+1,used|{v},chosen+[v])
                        match(i+1,used,chosen+[None])
                    match(0,set(),[])
                if scores==[4,4]:return scores,witness
    return scores,witness

def run():
    assert json.loads(P.read_text())==protocol;ctrl={10:{1,4,7},11:{1,4,8},12:{1,5,7},13:{1,5,8}};assert best([1,4,5,7,8],ctrl)[0]==[4,4] and best([1,4,5,7,8],{10:set.union(*ctrl.values())})[0]==[0,1];hist=[Counter(),Counter()];entries=[]
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i<protocol['start']:continue
            if i>=protocol['start']+protocol['records']:break
            g=graph(line.strip());u=next((v for v in sorted(g) if len(g[v])==7),None);z=dict(record=i,root=u)
            if u is not None:
                L,r,_=setup(g,u);rows={x:{v for j,v in enumerate(L) if m>>j&1} for x,m in r.items()};s,w=best(L,rows);z.update(scores=s,witnesses=w)
                for h in range(2):
                    hist[h][s[h]]+=1
                    if w[h]:
                        a,b,c,d,e=w[h]['columns'];vs=w[h]['rows'];assert len({v for v in vs if v is not None})==s[h]
                        for want,v in zip(({a,b,d},{a,b,e},{a,c,d},{a,c,e}),vs):
                            if v is not None:assert want<=g[v] and (h or g[v]&{a,b,c,d,e}==want)
            entries.append(z)
    assert len(entries)==protocol['records'];print(hist);prev.save(R,dict(protocol_sha=prev.sha(P.read_bytes()),max_corners=[dict(h) for h in hist],entries=entries))
if __name__=='__main__':{'freeze':lambda:prev.save(P,protocol),'test':run}[sys.argv[1]]()
