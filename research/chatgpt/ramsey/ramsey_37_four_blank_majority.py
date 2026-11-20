"""Search all 1,1,2-disagreement witnesses up to relabeling of a singleton repair."""
from itertools import combinations
from pathlib import Path
from ramsey_37_one_defect_repairs import neighbours
from ramsey_37_joint_pin_audit import E, ALL, cliques

def flip(N,e):
    i,j=e;N[i]^=1<<j;N[j]^=1<<i

def valid(N):return not next(cliques(N,3),0) and not next(cliques([ALL^v^(1<<i) for i,v in enumerate(N)],7),0)

def search():
    for idx,line in enumerate(Path(__file__).with_name('pauli-realization-catalogues').joinpath('r37_22.g6').read_bytes().splitlines(),1):
        bits=''.join(f'{b-63:06b}' for b in line[1:]);N=[0]*22
        for i,j in E:
            if bits[j*(j-1)//2+i]=='1':flip(N,(i,j))
        for e,red,rep in neighbours(line):
            if len(rep)!=2:continue
            flip(N,e);bad=N if red else [ALL^v^(1<<i) for i,v in enumerate(N)]; defects=list(cliques(bad,3 if red else 7));
            def inside(edge,s):return all(s>>v&1 for v in edge)
            for x in E:
                if x in rep or not inside(x,defects[0]):continue
                flip(N,x)
                # In the intermediate illegal matrix, a second flip must hit every defect, with correct color.
                d1=list(cliques(N,3));d2=list(cliques([ALL^v^(1<<i) for i,v in enumerate(N)],7));assert d1 or d2
                if not(d1 and d2):
                    inter=ALL
                    for s in d1+d2:inter&=s
                    for y in combinations([v for v in range(22) if inter>>v&1],2):
                        if y==x or y in rep:continue
                        flip(N,y);ok=valid(N);flip(N,y)
                        if ok:
                            flip(N,x);F=rep+[x,y];g=[]
                            for m in range(16):
                                for j,f in enumerate(F):
                                    if m>>j&1:flip(N,f)
                                if valid(N):g.append(m)
                                for j,f in enumerate(F):
                                    if m>>j&1:flip(N,f)
                            print('record',idx,'flip',e,'red?',red,'blanks',F,'legal difference masks',g,'defects',[[i for i in range(22) if s>>i&1] for s in defects]);return
                flip(N,x)
            flip(N,e)
    print('no four-blank witness')
if __name__=='__main__':search()
