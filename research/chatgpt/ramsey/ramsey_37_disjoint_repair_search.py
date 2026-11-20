"""Bounded third-repair search at the first two-repair center, record 1."""
from ramsey_37_four_blank_majority import *

def main():
    line=Path(__file__).with_name('pauli-realization-catalogues').joinpath('r37_22.g6').read_bytes().splitlines()[0]; bits=''.join(f'{b-63:06b}' for b in line[1:]);N=[0]*22
    for i,j in E:
        if bits[j*(j-1)//2+i]=='1':flip(N,(i,j))
    e,_,rep=next(z for z in neighbours(line) if len(z[2])==2);flip(N,e)
    def dfs(path,limit):
        forbidden=set(rep)|set(path); b=next(cliques(N,3),0) or next(cliques([ALL^v^(1<<i) for i,v in enumerate(N)],7),0)
        if not b:return path
        if len(path)==limit:return None
        for f in combinations([i for i in range(22) if b>>i&1],2):
            if f in forbidden:continue
            flip(N,f);out=dfs(path+[f],limit);flip(N,f)
            if out:return out
    for limit in range(3,9):
        ans=dfs([],limit)
        if ans:print('record 1 defect flip',e,'single repairs',rep,'third repair',ans,flush=True);return
if __name__=='__main__':main()
