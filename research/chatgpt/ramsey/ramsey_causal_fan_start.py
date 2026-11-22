"""Start on the next outgoing incidence from a fan centered at the literal R column. Inspect vertices as encountered; no overlap or cycle index in the trigger. Test arbitrary incoming phase and reversed traversal."""
from ramsey_flag_online_first_hit import cycle,m,r,X,P,D,json,tours,permutations,apex

def stream(w,col,p,E):
    v=None;trace=[]
    for i in range(2*len(w)):
        a,b=w[i%len(w)],w[(i+1)%len(w)];d=min(a,b)
        if v is None:
            if a>=15 or apex(a)!=col:continue
            start=i;v=p[col-1]
        options=[e for e in E if e[0]==v and any(set(e)=={p[q-1] for q in X[k]} for k in P[d])];assert len(options)<=1
        if options:
            e,=options;trace.append(e);v=e[1]
            if v in {'C','D'}-{p[col-1]}:return start,i+1,trace
    return None

def run():
    c=cycle(m);E=set(tours()[0]['word']);out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        for row,t in zip(('BRNN','BNRN'),(c,[r[i] for i in c])):
            col=row.index('R')+1;assert [d for d in t[::2] if apex(d)==col]==[t[-2]];rec={}
            for name,w in [('forward',t),('reversed',t[:1]+t[:0:-1])]:
                trials=[stream(w[k:]+w[:k],col,p,E) for k in range(len(w))];assert all(trials);assert len({tuple(x[2]) for x in trials})==1;rec[name]=dict(prefix=trials[0][2],from_entry=trials[0][:2],worst_flags=max(x[1] for x in trials));
            assert rec['forward']['from_entry'][0]==8 and len(rec['forward']['prefix'])==2;out.append(dict(binding=''.join(p),row=row,start_fan=t[-2],test=rec))
    return out
if __name__=='__main__':
    out=run();print(out[:2]);(D/'ramsey_causal_fan_start.json').write_text(json.dumps(out)+'\n')
