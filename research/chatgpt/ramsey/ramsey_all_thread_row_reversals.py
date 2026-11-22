"""Generalize the exit reversal to any selected flag (d,t): fix both letters of d, exchange partners of each other block of t. Does one row acting independently at the five threads pick flags of a SINGLE intermediate matching?"""
from ramsey_unused_flag_threads import run as threads,m,mate,D,json
from ramsey_row_quotient_constructor import P,T,action

def run():
    rows=[]
    for row in (m,mate):
        inv={j:i for i,j in row};out=[]
        for path in threads()['paths']:
            j,mid,k,i=path if path[0]>=15 else path[::-1];d=inv[j];p=list(range(6))
            for block in T[j-15]:
                if block!=P[d]:a,b=block;p[a],p[b]=b,a
            g=action(p);out.append(dict(source=[d,j],input=[i,k],output=[g[i],g[k]]))
        rows.append(out)
    from ramsey_intrinsic_complement_matching import run as complement
    c=complement();forced=set(map(tuple,c['forced_common']));alt=set(map(tuple,c['alternating']));images=[]
    for row in rows:
        s=set(tuple(r['output']) for r in row);assert len(s)==5 and s<=alt and len({x for x,y in s|forced})==len({y for x,y in s|forced})==15;images.append(s)
    assert images[0]|images[1]==alt;return rows
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_all_thread_row_reversals.json').write_text(json.dumps(out)+'\n')
