"""Transport canonical chain coordinates through four frames. Reversing a chain's stored direction complements its endpoint bit only for even chain length."""
from ramsey_strip_chain_parity_kernel import chains,solutions,edge
from ramsey_strip_rotating_boundary import f,image
canon=lambda p:tuple(p if p[0]<p[-1] else p[::-1])
frames=[sorted(map(canon,chains))];maps=[]
for k in range(4):
    old=frames[-1];new=sorted(canon([f[v] for v in p]) for p in old);mapping=[]
    for p in old:
        q=tuple(f[v] for v in p);dest=new.index(canon(q));flip=int(q[0]>q[-1] and (len(q)-1)%2==0);mapping.append((dest,flip))
    maps.append(mapping);frames.append(new);print('turn',k+1,'coordinate flips',sum(b for _,b in mapping))
assert frames[0]==frames[4]
for i in range(18):
    j=i;b=0
    for mapping in maps:j,flip=mapping[j];b^=flip
    assert (j,b)==(i,0)
for m in solutions:
    start=m
    for old,new,mapping in zip(frames,frames[1:],maps):
        bits=[int(edge(p[0],p[1]) in m) for p in old];m=image(m,f);actual=[int(edge(p[0],p[1]) in m) for p in new]
        assert all(actual[j]==bits[i]^flip for i,(j,flip) in enumerate(mapping))
    assert m==start
print('all 18 chain coordinates return unchanged; all',len(solutions),'assignments survive four turns')
