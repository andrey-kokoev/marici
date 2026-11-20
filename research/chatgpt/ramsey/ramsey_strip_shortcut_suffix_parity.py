"""Canonical shortcut: retain every off-strip match and match the four released lifted positions in the two middle links of the detour. Check relative cycle lengths from suffix distance only, including the 6->4 case where other short completions exist."""
from ramsey_strip_shortcut_boundary_read import words,E,fill,edges,r,Counter
H=Counter()
for w,p in words.items():
 for i in range(len(w)-3):
    if tuple(sorted((w[i],w[i+3]))) not in E:continue
    v=w[:i+1]+w[i+3:];q=words[v];c=p+tuple(r[x] for x in p[-2:0:-1]);d=q+tuple(r[x] for x in q[-2:0:-1]);rel={edges(p[i+2],p[i+3]),edges(r[p[i+2]],r[p[i+3]])};assert set(c)-set(d)=={x for e in rel for x in e}
    for extra in fill(set(range(30))-set(c)):
     for alt in (0,1):
        def mat(c,off):return dict(off|{edges(c[j],c[(j+1)%len(c)]) for j in range(alt,len(c),2)})
        a,b=mat(c,extra),mat(d,extra|rel);assert len(a)==len(b)==len(set(b.values()))==15;inv={y:x for x,y in b.items()};todo=set(a);cycles=[]
        while todo:
            x=min(todo);n=0
            while x in todo:todo.remove(x);n+=1;x=inv[a[x]]
            if n>1:cycles.append(n)
        suffix=len(w)-i-4;assert cycles==[suffix+3];H[len(w),i,alt,tuple(cycles)]+=1
print('canonical relative cycles:',sorted(H.items()))
