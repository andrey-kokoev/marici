"""Apply the source nonbacktracking rule at its own scale (successive Hall vertices). Do not treat a complete transit d->29->e as a primitive egress edge."""
from ramsey_join_flag_phase import lift,final,move,R,D,json
from ramsey_exit_triad_axis_lift import run

def extend(a,b,d):
    adj={}
    for x,y in a^b:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
    w=[29,d]
    while len(w)<3 or w[-2]!=29:
        z,=adj[w[-1]]-{w[-2]};w.append(z)
    assert len(w)==12 and all(x!=z for x,z in zip(w,w[2:]));return w

def check():
    M,=final;N=move(M,R);at=lambda m:next(d for d,j in m if j==29);out=[]
    for r,(a,b) in zip(run(),((M,N),(N,M))):
        h=lift(r['column_map'])
        for _ in range(3):
            prior,d=at(a),at(b);na,nb=move(a,h),move(b,h);fresh=at(nb);assert at(na)==d and len({prior,d,fresh})==3
            old=extend(a,b,d);back=extend(b,a,d);new=extend(na,nb,d);assert old==back and old[-3:]==[prior,29,d] and new[-3:]==[fresh,29,d];first=next(i for i in range(len(old)) if old[i]!=new[i]);out.append(dict(previous=[prior,29,d],onward_direct_splice=[prior,29,d,29,fresh],stay_or_reflect=old,onward_no_flag_reversal=new,first_distinct_visit=[old[first],new[first]]));a,b=na,nb
    return out
if __name__=='__main__':
    out=check();print(out[0]);(D/'ramsey_join_nonreturn_scale.json').write_text(json.dumps(out)+'\n')
