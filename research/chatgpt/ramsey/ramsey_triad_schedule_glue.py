"""Compare genuine alternating successor with iterating the proposed triad frame change. Check overlap at the intermediate matching, not merely at its exit flag."""
from ramsey_exit_triad_axis_lift import run,P,T,X,D,json
from ramsey_row_quotient_constructor import final,move,R,frame_records

def check():
    M,=final;N=move(M,R);rows=[];ms=next(ms for _,_,ms in frame_records if M in ms)
    for rec,(a,b) in zip(run(),((M,N),(N,M))):
        p=rec['column_map'];ex=[X.index(tuple(sorted(p[i-1] for i in edge))) for edge in X];pair=lambda d:tuple(sorted(ex[i] for i in d));h=[P.index(pair(d)) for d in P]+[15+T.index(tuple(sorted(map(pair,t)))) for t in T];orig=(a,b);out=[];exit=lambda m:next(i for i,j in m if j==29)
        for _ in range(3):
            na,nb=move(a,h),move(b,h);assert exit(b)==exit(na);out.append(dict(edge=[exit(a),exit(b)],overlap_exit_seam=len(b&na),same_selected_frame=na in ms and nb in ms,shared=sorted(b&na)));a,b=na,nb
        assert (a,b)==orig and all(v['overlap_exit_seam']<15 for v in out);rows.append(out)
    return rows
if __name__=='__main__':
    out=check();print(out);(D/'ramsey_triad_schedule_glue.json').write_text(json.dumps(out)+'\n')
