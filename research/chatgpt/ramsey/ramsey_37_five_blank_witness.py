"""Look for three disjoint repairs of total size <=5 at a radius-one defect."""
from ramsey_37_four_blank_majority import *
def main():
 for idx,line in enumerate(Path(__file__).with_name('pauli-realization-catalogues').joinpath('r37_22.g6').read_bytes().splitlines(),1):
    bits=''.join(f'{b-63:06b}' for b in line[1:]);N=[0]*22
    for i,j in E:
        if bits[j*(j-1)//2+i]=='1':flip(N,(i,j))
    for e,red,rep in neighbours(line):
        flip(N,e); ban=set(rep);repairs=[{f} for f in rep];
        def walk(path,cap):
            d=next(cliques(N,3),0) or next(cliques([ALL^v^(1<<i) for i,v in enumerate(N)],7),0)
            if not d:
                if path not in repairs:repairs.append(path)
                return
            if len(path)==cap:return
            for f in combinations([k for k in range(22) if d>>k&1],2):
                if f in ban or f in path:continue
                flip(N,f);walk(path|{f},cap);flip(N,f)
        walk(set(),3 if len(rep)==2 else 2)
        for a,b,c in combinations(repairs,3):
            if not(a&b or b&c or a&c) and len(a|b|c)<=5:
                print(idx,e,red,a,b,c);return
        flip(N,e)
 print('no five-blank witness')
if __name__=='__main__':main()
