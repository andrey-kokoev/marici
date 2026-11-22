"""Intervene on certification, exit inputs and cross-return retention separately. Keep one direct binding and unchanged typed executor for both rows."""
from ramsey_live_matching_receipt import m,mate,P,X,D,json,apex,execute,validate,registry
from ramsey_flag_selector_ablation import match,rho
p='ACDB'
def supports(d):return {e for e in registry if any(set(e)=={p[i-1] for i in X[h]} for h in P[d])}
def visits(M,N,count):
    f=dict(M);b={j:d for d,j in N};x=0
    for k in range(count):
        y=f[x] if k%2==0 else b[x];yield x,y,min(x,y);x=y

def live(M,N,col,reset):
    v=None;prefix=();log=[]
    for i,(x,y,d) in enumerate(visits(M,N,30),1):
        if x<15 and v is None and apex(x)==col:v=p[col-1]
        opts=[e for e in supports(d) if e[0]==v];assert len(opts)<=1
        if opts:
            e,=opts;ev=execute((e,))[0];prefix=validate(prefix+(ev,));v=e[1];log.append((i,e,ev[2]))
            if len(prefix)==2:return dict(complete=True,events=log)
        if y==0 and reset:v=None;prefix=()
    return dict(complete=False,events=log)

def run():
    old=dict(m);bad=next(M for M in match() if list(visits(M.items(),[(rho[d],rho[j]) for d,j in M.items()],4))[-1][:2]==(19,1));out=[]
    for col,M,N in [(2,m,mate),(3,mate,m)]:
        tail=p[col-1];head,={'C','D'}-{tail};word,=[(a,b) for a in registry for b in registry if a[0]==tail and a[1]==b[0] and b[1]==head];cert=[]
        for mm in (old,bad):
            nn={rho[d]:rho[j] for d,j in mm.items()};f,g=(mm,nn) if col==2 else (nn,mm);ds=[d for x,y,d in visits(f.items(),g.items(),4)];cert.append([(i+1,j+1) for i,j in [(0,3),(3,2)] if word[0] in supports(ds[i]) and word[1] in supports(ds[j])]);
        assert cert[0] and not cert[1];exit_runs={}
        for absent in (None,4,7,9):
            available=set().union(*(supports(d) for d in (4,7) if d!=absent));fits=[(a,b) for a in available for b in available if a[0]==tail and a[1]==b[0] and b[1]==head];issued=[validate(execute(w)) for w in fits];assert bool(issued)==(absent not in (4,7));exit_runs[str(absent)]=[[e[2] for e in q] for q in issued]
        keep=live(M,N,col,False);reset=live(M,N,col,True);assert keep['complete'] and not reset['complete'] and len(reset['events'])==3;out.append(dict(tail=tail,candidate=word,certificates=cert,exit_event_ids=exit_runs,keep=keep,reset=reset))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_three_selector_interventions.json').write_text(json.dumps(out)+'\n')
