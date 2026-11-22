"""Stream the active flags starting at the first overlap fan. No path search, owner filter, or future flag in the emission decision. Test whether extending the scan could source the complete receipt."""
from ramsey_handoff_flag_owners import cycle,m,r,X,P,D,json,tours,permutations
from ramsey_first_fan_rim_probe import apex

def run():
    c=cycle(m);ts=tours();E=set(ts[0]['word']);outer={e for e in E if e[::-1] not in E};apexes={v for v in 'ABCD' if sum(e[0]==v for e in E)==1};out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        pair=[]
        for t in (c,[r[i] for i in c]):
            w=t[-2:]+t[:-2];flags=[tuple(sorted(z)) for z in zip(w,w[1:]+w[:1])];v=p[apex(w[0])-1];assert v in apexes;start=v;emitted=[];log=[];visible=set()
            for i,(d,j) in enumerate(flags):
                support={frozenset(p[col-1] for col in X[k]) for k in P[d]};allowed={e for e in E if frozenset(e) in support};visible.update(allowed)
                if v!=start and v in apexes:continue
                choices=[e for e in allowed if e[0]==v];assert len(choices)<=1;log.append(choices)
                if choices:e,=choices;v=e[1];emitted.append(e)
            assert visible==outer and len(emitted)==2 and v in apexes-{start} and len(log)<=4;fit,=[tr for tr in ts if tuple(emitted) in zip(tr['word'],tr['word'][1:]+tr['word'][:1])];pair.append(dict(start=start,head=v,reads=log,seam=fit['seam'],never_visible=sorted(E-visible)))
        assert pair[0]['seam']!=pair[1]['seam'];out.append(dict(binding=''.join(p),rows=pair))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_flag_online_first_hit.json').write_text(json.dumps(out)+'\n')
