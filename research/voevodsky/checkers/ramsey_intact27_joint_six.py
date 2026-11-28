"""Test the complete order-27 catalogue for six same-root ports. All labels zero-based."""
import gzip,json,subprocess,tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from itertools import combinations
from ramsey_retention_slice import CAT,D,decode,check


def full(a):
    I=[0]
    for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v]);
    S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];M={}
    for k in range(3,8):
        qs=[q for q in I if q.bit_count()==k];M[k]=[sum(1<<j for j,q in enumerate(qs) if q&s==0) for s in S]
    assert all(M[7]);N=[{j for j in range(i+1,len(S)) if not M[7][i]&M[7][j]} for i in range(len(S))]
    def choose(p,opts):
        if len(p)==6:return [S[i] for i in p]
        for i in sorted(opts):
            n=len(p)+1
            if any(allmiss(sub+(i,),M[k]) for k in range(3,7) if 9-k<=n for sub in combinations(p,8-k)):continue
            rem=opts&N[i]
            if len(rem)>=6-n:
                w=choose(p+(i,),rem)
                if w:return w
    def allmiss(sub,col):
        m=col[sub[0]]
        for j in sub[1:]:m&=col[j]
        return m!=0
    rows=choose((),set(range(len(S))))
    if rows:
        g=a[:]+[0]*7
        for i,s in enumerate(rows,27):
            g[i]=s|(1<<33);g[-1]|=1<<i
            for j in range(27):g[j]|=int(bool(s>>j&1))<<i
        assert check(g,(1<<34)-1,3,9)
    return rows


def audit():
    lines=gzip.open(CAT/'r38_27.g6.gz','rb').read().splitlines();n=len(lines);assert n==477142
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'pack.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_intact27_seven_pack.rs')),'-o',str(exe)],check=True)
        def scan(span):
            lo,hi=span;data=b'\n'.join(str(i).encode()+b' '+lines[i] for i in range(lo,hi));p=subprocess.run([str(exe),'6'],input=data,capture_output=True,check=True);assert int(p.stderr)==hi-lo;return list(map(int,p.stdout.split()))
        spans=[(i,min(i+5000,n)) for i in range(0,n,5000)];ids=[]
        with ThreadPoolExecutor(8) as ex:
            for batch in ex.map(scan,spans):ids.extend(batch)
    tested={}
    for i in sorted(ids):
        tested[i]=full(decode(lines[i].decode()))
        if tested[i]:break
    out=dict(total=n,six_compatible_on_sevens=sorted(ids),full_results=tested);print(out);(D.parent/'ramsey_intact27_joint_six.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
