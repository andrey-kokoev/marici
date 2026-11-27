"""Exhaustive chart test at 8→9, with swap axes and the action of the mirror fixed."""
from ramsey_excel_successor_chart_audit import cube,mirror,local,signature,D,json,product,Counter
A=((1,4,7),(1,4,8),(1,5,8),(2,5,8));zero=(0,0,0);bits=list(product(range(2),repeat=3))
def xor(a,b):return tuple(x^y for x,y in zip(a,b))
def reflect(b):return tuple(1-x for x in b[::-1])
def run():
    fresh=[];seen=set()
    for a in A:
        new=cube(a)-seen;seen|=cube(a)
        if len(new)==4:fresh.append((a,new))
    patch=fresh+[(tuple(9-i for i in a[::-1]),set(map(mirror,new))) for a,new in fresh];out=[]
    # Commuting with each named bit flip forces F_a(b)=b XOR F_a(000).
    # Fix the initial chart exactly. Enumerate ALL other chart origins,
    # then filter by the same fixed reflected bit map on every occurrence.
    for rest in product(bits,repeat=3):
        origins=(zero,)+rest
        def lab(i,r):return xor(local(A[i],r),origins[i])
        if any(lab(3-i,mirror(r))!=reflect(lab(i,r)) for i,a in enumerate(A) for r in cube(a)):continue
        faces=[signature({lab(A.index(a),r) for r in new}) for a,new in patch];aligned=[];overlap=[]
        for i in range(3):
            a,b=A[i:i+2];shift=tuple(y-x for x,y in zip(a,b));aligned.append(all(lab(i,r)==lab(i+1,tuple(x+d for x,d in zip(r,shift))) for r in cube(a)));overlap.append(all(lab(i,r)==lab(i+1,r) for r in cube(a)&cube(b)))
        out.append(dict(origins=origins,faces=faces,distinct_faces=len(set(faces)),translation_agrees=aligned,literal_overlap_agrees=overlap))
    assert len(out)==8 and sum(all(q['translation_agrees']) for q in out)==1;print(Counter(q['distinct_faces'] for q in out));print([(q['origins'][1],q['faces']) for q in out]);dest=D.parent/'results/ramsey_excel_chart_axioms.json';text=json.dumps(dict(scope='8→9; fixed old chart, named reversible swaps and fixed reverse-complement mirror on full cube occurrences',cases=out),indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':run()
