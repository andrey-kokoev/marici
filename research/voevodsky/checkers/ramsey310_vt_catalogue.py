"""Read graph6 members from McKay's vertex-transitive archive, Zenodo 4010122.
Usage: python ramsey310_vt_catalogue.py archive-or-prefix.tar 40 (or 26).
Only the tar prefix through degree 9 is needed at order 40; use exact member names.
"""
import tarfile,gzip,sys,hashlib,json
from ramsey310_six_set_parent_test import independent

def run(path,n,k,target):
    name=f'alltrans{n}_k={k:02}.gz'
    with tarfile.open(path) as f:
        for m in f:
            if m.name==name: compressed=f.extractfile(m).read();break
        else:raise ValueError(name)
    rows=gzip.decompress(compressed).splitlines();tf=miss=0;example=None;U=(1<<n)-1
    for line in rows:
        assert line[0]==63+n and len(line)==1+(n*(n-1)//2+5)//6
        a=[0]*n;bit=0;triangle=False
        for j in range(n):
            for i in range(j):
                c=line[1+bit//6]-63;hit=c>>(5-bit%6)&1;bit+=1
                if hit:
                    if a[i]&a[j]:triangle=True;break
                    a[i]|=1<<j;a[j]|=1<<i
            if triangle:break
        if triangle:continue
        tf+=1;assert all(x.bit_count()==k for x in a)
        if not independent(a,U,target):miss+=1;example=line.decode()
    print(json.dumps(dict(member=name,sha256=hashlib.sha256(compressed).hexdigest(),graphs=len(rows),triangle_free=tf,no_independent_target=miss,target=target,example=example)),flush=True)
if __name__=='__main__':
    n=int(sys.argv[2]);
    for k in ([5,6,7,8,9] if n==40 else [6]):run(sys.argv[1],n,k,10 if n==40 else 8)
