"""Generate, do not fit, frame switches: install the incoming exit-duad partner of column 1 as the new image of the original stationary N corner (4). Only tested within the three rooted even frames."""
from itertools import permutations,combinations
from ramsey_join_flag_phase import lift,final,move,R,D,json
from ramsey_fork_missing_corner import partner

def run():
    m,=final;n=move(m,R);rows=[]
    for orig in [(m,n),(n,m)]:
        tables={}
        for p in permutations(range(1,5)):
            if p[0]!=1 or sum(a>b for a,b in combinations(p,2))%2:continue
            a,b=[move(s,lift(p)) for s in orig];tables[p[3]]=(dict(a),{j:d for d,j in b})
        for update in (False,True):
            x,q=0,4;seen={};path=[];exits=[]
            while (x,q) not in seen:
                seen[x,q]=len(path);path.append(x);f,g=tables[q];y=f[x] if x<15 else g[x]
                if y==29:
                    prev=q;q=partner(x) if update else q;exits.append(dict(incoming=x,old_Q=prev,new_Q=q,outgoing=tables[q][1][29]))
                x=y
            assert seen[x,q]==0 and len(path)==(30 if update else 10);assert all(path[i-1]!=path[(i+1)%len(path)] for i in range(len(path)));rows.append(dict(update=update,visits=path,exits=exits))
    return rows
if __name__=='__main__':
    out=run();print([r['exits'] for r in out]);(D/'ramsey_online_exit_reanchor.json').write_text(json.dumps(out)+'\n')
