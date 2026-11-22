"""Intersect two index-free witness tests: one common ordered pair of distinct matching owners across rows, and at most one flag of reverse access. No specified exit, polarity or permitted slot pair used by the filter."""
from ast import literal_eval
from ramsey_flag_timing_relaxation import run as census,D,json
from ramsey_flag_selector_ablation import match,rho
from collections import Counter

def run():
    weights=Counter()
    for m in match():
        back={rho[j]:rho[d] for d,j in m.items()};u=back[m[0]];weights[u,m[u],back[m[u]]]+=1
    records=[]
    for bind in census():
        controls={}
        for local in (False,True):
            for common in (False,True):
                good={}
                for q,pair in bind['witnesses'].items():
                    opts=[]
                    for owners,sz in zip(('mnmn','nmnm'),pair):
                        opts.append({owners[i-1]+owners[j-1] for i,j in sz if not local or i<=j+1})
                    orders=(opts[0]&opts[1])&{'mn','nm'}
                    if all(opts) and (not common or orders):good[q]=sorted(orders)
                controls[str((local,common))]=dict(prefixes=good,count=sum(weights[literal_eval(q)] for q in good))
        both=controls[str((True,True))];assert list(both['prefixes'])==['(13, 19, 7)'] and both['count']==13;records.append(dict(binding=bind['binding'],controls=controls))
    return records
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_owner_locality_control.json').write_text(json.dumps(out)+'\n')
