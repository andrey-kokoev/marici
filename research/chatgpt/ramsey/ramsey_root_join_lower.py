"""Join each largest (3,6) core to an independent set of ports and their common root. No (3,7) catalogue input. uv run --with python-sat python <file>."""
from itertools import combinations
from pathlib import Path
from pysat.solvers import Solver
from ramsey_clique_power_blowup import layers

def cores():
    for line in Path(__file__).with_name('pauli-realization-catalogues').joinpath('r36_17.g6').read_bytes().splitlines():
        n=line[0]-63;bits=''.join(f'{b-63:06b}' for b in line[1:]);A=[0]*n
        for j in range(n):
            for i in range(j):
                if bits[j*(j-1)//2+i]=='1':A[i]|=1<<j;A[j]|=1<<i
        yield A

def join(A,p):
    n=len(A);faces=layers(A);assert max(map(int.bit_count,faces))==5 and all(r in faces for r in A)
    V=lambda s,i:1+s*n+i
    with Solver(name='cadical195') as sol:
        for s in range(p):
            for i,j in combinations(range(n),2):
                if A[i]>>j&1:sol.add_clause([-V(s,i),-V(s,j)])
        for f in faces:
            for Q in combinations(range(p),7-f.bit_count()):sol.add_clause([V(s,i) for s in Q for i in range(n) if f>>i&1])
        if not sol.solve():return
        m=set(sol.get_model());B=A.copy()+[0]*(p+1)
        for s in range(p):
            for i in [i for i in range(n) if V(s,i) in m]+[n+p]:B[n+s]|=1<<i;B[i]|=1<<(n+s)
        fs=layers(B);assert all(r in fs for r in B) and max(map(int.bit_count,fs))<=6
        return [hex(r) for r in B]
if __name__=='__main__':
    for p in range(7):
        for idx,A in enumerate(cores(),1):
            witness=join(A,p)
            if witness:print('ports',p,'core',idx,'order',len(witness),witness,flush=True);break
        else:print('first impossible port count',p,flush=True);break
