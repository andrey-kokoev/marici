"""All fixed-point-free involutions of each strict 16-site catalogue host. Relabel in 8 pairs. No deduplication by conjugacy."""
import gzip,json
from pathlib import Path
H=Path(__file__).parent;out=[]
for idx,line in enumerate(gzip.open(H/'r36_16.g6.gz','rt'),1):
    assert line[0]=='O';bits=''.join(f'{ord(c)-63:06b}' for c in line.strip()[1:]);N=[set() for _ in range(16)]
    for j in range(16):
        for i in range(j):
            if bits[j*(j-1)//2+i]=='1':N[i].add(j);N[j].add(i)
    sig=[len(s) for s in N]
    for _ in range(16):
        v=[(sig[i],tuple(sorted(sig[j] for j in N[i]))) for i in range(16)];s=[v.index(x) for x in v];
        if len(set(s))==len(set(sig)):break
        sig=s
    def gen(left,p):
        if not left:
            order=[x for i in range(16) if i<p[i] for x in (i,p[i])];out.append(dict(record=idx,order=order,N=[sum(1<<j for j in range(16) if order[j] in N[i]) for i in order]));return
        opts=[([j for j in left if i!=j and sig[i]==sig[j] and all((a in N[i])==(b in N[j]) for a,b in p.items())],i) for i in left];vs,i=min(opts,key=lambda z:len(z[0]));
        for j in vs:gen(left-{i,j},p|{i:j,j:i})
    gen(set(range(16)),{})
assert idx==2576;print(len(out),len({r['record'] for r in out}));(H/'ramsey_strict_aligned_hosts.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
