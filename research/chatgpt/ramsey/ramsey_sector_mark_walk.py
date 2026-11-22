"""Frozen mark-relative walks. Import prior experiment's geometry; its output is deterministic."""
from ramsey_sector_walk_color import V,T,p,coord,dist,step,sides,P,truth,D,json
from collections import defaultdict,Counter
from functools import lru_cache
@lru_cache(None)
def paths(i,j):
    if i==j:return [(i,)]
    return [(i,)+s for k in step[i] if dist[k][j]<dist[i][j] for s in paths(k,j)]
def table(rows):
    t=defaultdict(Counter)
    for k,col in rows:t[k][col]+=1
    return t
def err(t):return sum(min(v[0],v[1]) for v in t.values())
allrows=defaultdict(list);reports={};coll={}
for c in V:
    mark={e for e,(f,a,b) in T.items() if c in (p[a],p[b],coord(f))};h={e:min(dist[e][f] for f in mark) for e in T};rows=[];bad=Counter();valleys={}
    for ab in P:
        words=[[],[],[]];vs=[]
        for a,b in (ab,ab[::-1]):
            dirs=[[],[],[]];val=False
            for path in paths(sides[a][1],sides[b][0]):
                signs=''.join('+' if h[y]>h[x] else '-' if h[y]<h[x] else '=' for x,y in zip(path,path[1:]));val|=('-' in signs and '+' in signs[signs.index('-')+1:]);types=''.join('F' if step[x][0]==y else 'S' for x,y in zip(path,path[1:]));
                for dst,k in zip(dirs,[signs,(h[path[0]],signs),(h[path[0]],signs,types)]):dst.append(k)
            for w,d in zip(words,dirs):w.append(tuple(sorted(d)))
            vs.append(val)
        col=c in truth[ab];bad[int(all(vs)),int(col)]+=1;valleys[ab]=list(vs);rows.append(([tuple(sorted(w)) for w in words],col,ab))
    reports[c]=dict(incident=len(mark),valley_confusion={str(k):v for k,v in bad.items()},best_errors=[]);allrows[c]=rows
    for i in range(3):reports[c]['best_errors'].append(err(table([(ks[i],v) for ks,v,_ in rows])))
    if c=='000':
        for ks,v,ab in rows:
            other=next((b for k,u,b in rows if k[2]==ks[2] and u!=v),None)
            if other:coll=dict(pair=ab,other=other,color=v,signature=ks[2]);break
transfer=[]
for i in range(3):
    t=table([(k[i],v) for k,v,_ in allrows['000']]);stats=Counter()
    for c in V[1:]:
        for k,v,_ in allrows[c]:
            votes=t.get(k[i]);key='unseen' if not votes else 'ambiguous' if len(votes)>1 else 'right' if v in votes else 'wrong';stats[key]+=1
    transfer.append(dict(stats))
two=table([(k[0],v) for c in ('000','001') for k,v,_ in allrows[c]]);held=[(k[0],v) for c in V if c not in ('000','001') for k,v,_ in allrows[c]];r=dict(states=reports,transfer=transfer,rich_collision=coll,two_seed=dict(classes=len(two),ambiguous=sum(len(v)>1 for v in two.values()),held=len(held),correct=sum(k in two and set(two[k])=={v} for k,v in held)));print(r);(D/'ramsey_sector_mark_walk.json').write_text(json.dumps(r,indent=2)+'\n')
