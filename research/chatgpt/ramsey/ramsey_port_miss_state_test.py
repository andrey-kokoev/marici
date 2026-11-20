"""Exact continuation coordinates for mutually blue root ports; find failure of top-layer-only truncation. No solver needed."""
from pathlib import Path
from itertools import combinations_with_replacement
from ramsey_clique_power_blowup import layers

def main():
    data=Path(__file__).with_name('pauli-realization-catalogues')/'r36_17.g6'
    for number,line in enumerate(data.read_bytes().splitlines(),1):
        n=line[0]-63;bits=''.join(f'{b-63:06b}' for b in line[1:]);A=[sum(1<<j for j in range(n) if j!=i and bits[max(i,j)*(max(i,j)-1)//2+min(i,j)]=='1') for i in range(n)]
        F=layers(A);assert max(map(int.bit_count,F))==5;five=[s for s in F if s.bit_count()==5];four=[s for s in F if s.bit_count()==4]
        def avoided(s):return sum(1<<j for j,t in enumerate(F) if not s&t)
        M={s:avoided(s) for s in four+five};full=(1<<len(F))-1
        def block(I):
            z=0
            for s in I:z|=M[s]
            return z
        pairs=0;bad=0;example=None;distinct=set();legal_triples=0
        for i,j in combinations_with_replacement(range(len(F)),2):
            a,b=F[i],F[j];single=[s for s in five if not s&a or not s&b]
            if any(not(s&a or s&b) for s in single):continue
            pairs+=1;top=full^block(single);sat4=[s for s in four if not s&(a|b)];exact=top&~block(sat4);distinct.add(exact);legal_triples+=exact.bit_count();bad+=(top^exact).bit_count()
            if example is None and top!=exact:
                diff=top^exact;c=F[(diff&-diff).bit_length()-1];s=next(s for s in sat4 if not s&c);example=(a,b,c,s)
        print(number,'legal unordered pairs',pairs,'distinct next menus',len(distinct),'valid next choices summed',legal_triples,'false top-only choices',bad,flush=True)
        if example:
            a,b,c,s=example
            # Directly check the proposed three attachments as a graph, including root.
            B=A.copy()+[0]*4
            for j,t in enumerate((a,b,c),n):
                for i in range(n):
                    if t>>i&1:B[i]|=1<<j;B[j]|=1<<i
                B[-1]|=1<<j;B[j]|=1<<(n+3)
            fs=layers(B);assert all(r in fs for r in B) and s|(7<<n) in fs and s.bit_count()==4
            print('example attachment masks and missed four:',*[hex(x) for x in example],flush=True)
if __name__=='__main__':main()
