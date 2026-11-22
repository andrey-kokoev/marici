"""Exact minimum incidence loss for fixed other ports: for each minimal legal exceptional kernel K keep all old vertices not adjacent to K. Cross-check against all independent supports containing some kernel."""
from collections import Counter
from ramsey_fork_audit_uniform import grow,inds,D,json,verify
from ramsey_final_miss_levels import bits

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);I=inds(H);joint=1<<10|1<<26;ks=json.loads((D/'ramsey_exceptional_forced_kernel.json').read_text())['rows'];lookup={}
    for r in ks:
        mins=r['minima'];legal=[s for s in I if s&joint==joint and any(s&m==m for m in mins)];lookup[tuple(r['fixed'])]=(mins,legal)
    out=[];hist=Counter()
    for r in json.loads((D/'ramsey_two_port_repair_depth.json').read_text())['repairs']:
        q=tuple(r['kept']);s=r['failed'][r['reused_slot']];mins,legal=lookup[q];best=None
        for m in mins:
            ban=0
            for i in bits(m):ban|=H[i]
            t=(s&~ban)|m;key=((s&~t).bit_count(),(t&~s).bit_count(),t,m)
            if best is None or key<best:best=key
        loss,add,t,m=best;assert (loss,add)==min(((s&~x).bit_count(),(x&~s).bit_count()) for x in legal);assert t&joint==joint;verify(grow(H,[*q,t]),10);hist[loss]+=1;out.append(dict(fixed=q,old=s,new=t,dropped=list(bits(s&~t)),added=list(bits(t&~s)),legal_count=len(legal),kernel_blockers=[dict(kernel=k,blocked=[v for v in bits(s) if H[v]&k]) for k in mins]))
    return dict(hist=hist,rows=out)
if __name__=='__main__':
    out=run();print(out['hist']);print(max(out['rows'],key=lambda r:len(r['dropped'])));(D/'ramsey_exceptional_port_drop.json').write_text(json.dumps(out)+'\n')
