"""Narrow majority slices from a vertex swap and two individually legal completions."""
from ramsey_37_four_blank_majority import *

def main():
 best=30
 for idx,line in enumerate(Path(__file__).with_name('pauli-realization-catalogues').joinpath('r37_22.g6').read_bytes().splitlines(),1):
    bits=''.join(f'{b-63:06b}' for b in line[1:]);N=[0]*22
    for i,j in E:
        if bits[j*(j-1)//2+i]=='1':flip(N,(i,j))
    for e,red,rep in neighbours(line):
        if len(rep)!=2:continue
        f=next(t for t in rep if t!=e)
        # Need permuted G to have opposite sign on e from G and unchanged sign on f from G.
        for x in e:
            for y in range(22):
                if y in e:continue
                d=(N[x]^N[y])&~((1<<x)|(1<<y));width=2*d.bit_count()+1
                if width>=best:continue
                edits={tuple(sorted((a,b))) for a in [x,y] for b in range(22) if d>>b&1}
                if e not in edits or f in edits:continue
                best=width;print('width',best,'record',idx,'center flip',e,'other repair',f,'swap',x,y,'third repair',sorted(edits-{e}),flush=True)
if __name__=='__main__':main()
