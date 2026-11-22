"""Exact reconfiguration graph of all legal fourth supports. Reconstruct from minimal elements by upward closure inside independent sets. Cross-check component partition via independent unions of minima."""
from itertools import combinations
from collections import Counter
from ramsey_fork_audit_uniform import D,json,inds,grow,verify

def comps(vertices,neighbors):
    left=set(vertices);out=[]
    while left:
        q=[min(left)];left.remove(q[0]);
        for s in q:
            nxt=left.intersection(neighbors(s));left-=nxt;q.extend(sorted(nxt))
        out.append(sorted(q))
    return out

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);I=set(inds(H));src=json.loads((D/'ramsey_compulsory_kernel_test.json').read_text());out=[];best=None
    for r in src['triples']:
        ms=r['minima'];
        if not ms:continue
        legal=[s for s in I if any(s&m==m for m in ms)];cs=comps(legal,lambda s:(s^(1<<v) for v in range(len(H))));cm=comps(ms,lambda s:(t for t in ms if s|t in I));assert {tuple(sorted(set(c)&set(ms))) for c in cs}==set(map(tuple,cm));out.append(dict(fixed=r['triple'],components=list(map(len,cs)),minimal_components=cm));
        if len(cs)>1 and (best is None or len(legal)<best['count']):
            for c in cs:verify(grow(H,r['triple']+[c[0]]),10)
            best=dict(fixed=r['triple'],count=len(legal),legal_components=cs,minimal_components=cm)
    return dict(hist=Counter(len(r['components']) for r in out),smallest=best,rows=out)
if __name__=='__main__':
    out=run();print(out['hist'],out['smallest']);(D/'ramsey_connected_fourth_repairs.json').write_text(json.dumps(out)+'\n')
