"""Seedless cyclic (3,10) search; independently replay each witness and try every next border."""
def search(n):
    full=(1<<n)-1
    def has(m,k,adj):
        if not k:return True
        while m.bit_count()>=k:
            b=m&-m;m^=b
            if has(m&adj[b.bit_length()-1],k-1,adj):return True
        return False
    def visit(i,d):
        if i>n//2:
            blue=[full^((d<<j|d>>(n-j))&full)^1<<j for j in range(n)]
            return None if has(blue[0],9,blue) else d
        e=d|1<<i|1<<(n-i)
        if not any(e&(e<<j|e>>(n-j)) for j in range(1,n) if e>>j&1):
            z=visit(i+1,e)
            if z is not None:return z
        return visit(i+1,d)
    return visit(1,0)
def verify(n,d):
    sets=[0]
    for j in range(n):
        red=sum(1<<i for i in range(j) if d>>(j-i)&1)
        assert red in sets and all(red&s for s in sets if s.bit_count()==9)
        sets += [s|1<<j for s in sets if not s&red]
    nine=[s for s in sets if s.bit_count()==9]; borders=sum(all(s&t for t in nine) for s in sets)
    return max(s.bit_count() for s in sets),len(nine),borders
if __name__=='__main__':
    for n in range(35,44):
        d=search(n);print(n,('no cyclic witness' if d is None else ([i for i in range(1,n//2+1) if d>>i&1],verify(n,d))),flush=True)
