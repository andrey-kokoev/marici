"""From K2 by port additions ONLY: a common nested stem through 26, then 8 ports ->35 or 7 ->34 and 4 ->39. No graph catalogue, saved attachment schedule or deletion operation in the delivered branches."""
import subprocess,sys
from collections import Counter
from itertools import combinations
from ramsey_reciprocal_port_layer import reciprocal,attach,verify,independent,D,json,nxgraph,nx
from ramsey_port_lookahead import completions
from ramsey_hall_anchor_ports import anchor_lift
from ramsey_ports_saturated_core import four

def layer(paths,k,d):
    buckets={};out=[];tested=0
    for H,hist in paths:
        for S,G in completions(H,k,d):
            tested+=1;key=tuple(sorted(map(int.bit_count,G)));group=buckets.setdefault(key,[]);g=nxgraph(G)
            if any(nx.is_isomorphic(g,j) for j in group):continue
            group.append(g);verify(G,k);out.append((G,hist+[list(S)]))
    print(k,'assignments',tested,'distinct cores',len(out),flush=True);return out

def fork(H,S):
    # Each proposed 34 extends the SAME unmodified 26: omit one port,
    # and shrink one other support before constructing the new graph.
    tries=0
    for skip in range(8):
        T=S[:skip]+S[skip+1:];A=attach(H,T);F=(1<<34)-1
        for i,m in enumerate(T):
            for j in range(26):
                if not m>>j&1:continue
                v=26+i
                if independent(A,F&~(A[v]|A[j]),7):continue
                U=T[:];U[i]^=1<<j;B=attach(H,U);verify(B,9);tries+=1;z=four(B)
                if z['supports']:
                    G=attach(B,z['supports']);verify(G,10);return {'to34':U,'to39':z['supports'],'graphs':[B,G],'valid34s_tried':tries,'omitted_port':skip,'thinned_port_index_among_retained':i,'removed_incidence':j}

def run(exe):
    paths=[([2,1],[])];stats=Counter()
    for k,d in ((3,2),(4,2),(5,4),(6,2)):paths=layer(paths,k,d)
    for H,hist in paths:
        stats['16s']+=1
        for s,K in reciprocal(H):
            stats['21s']+=1;p=subprocess.run([exe,*map(str,K)],capture_output=True,text=True,check=True)
            for line in p.stdout.splitlines():
                t=list(map(int,line.split()));B=attach(K,t);stats['26s']+=1;res=anchor_lift(B,9)
                if not res or not res.get('graph'):continue
                f=fork(B,res['supports']);stats['35s']+=1
                if f:
                    sched=hist+[list(s),t];A=[2,1];stem=[A];verify(A,2)
                    for k,U in enumerate(sched,3):A=attach(A,U);verify(A,k);stem.append(A)
                    assert A==B;verify(res['graph'],9);return {'stem_supports':sched,'stem_graphs':stem,'to35':res['supports'],'graph35':res['graph'],'alternate':f,'stats':dict(stats)}
    raise AssertionError('no fork found')
def short():
    from ramsey_port_deletion_chain import search
    paths=[([2,1],[])]
    for k,d in ((3,2),(4,2),(5,3),(6,4)):paths=layer(paths,k,d)
    for H,h in paths:
        a=search(H,7,4)
        if 'graph' not in a:continue
        b=search(a['graph'],8,4)
        if 'graph' in b:return h+[a['supports'],b['supports']]
    raise AssertionError('no short branch')

if __name__=='__main__':
    (D/'ramsey_pure_short_fork.json').write_text(json.dumps(short())+'\n')
    ans=run(sys.argv[1]);(D/'ramsey_pure_port_fork.json').write_text(json.dumps(ans)+'\n');print('stem',list(map(len,ans['stem_graphs'])),'fork',len(ans['graph35']),list(map(len,ans['alternate']['graphs'])),'search',ans['stats'],'fork trial',ans['alternate']['valid34s_tried'])
