"""Lift the same vertex permutation as the proton rim test. Search single-qubit Clifford rotations, with or without K. Verify all four stored local projectors and all return blocks exactly; measure the fourth spinor power."""
from ramsey_electron_face_joint_weights import D,json,F,A,ZERO,ONE,read_operator,product
from ramsey_crossing_axis_scramble import pts
from assemble_metric_coefficient_protocol import decode,sharp,tr

def run():
    root=D.parents[1];load=lambda p:json.loads((root/p).read_text());norm=load('voevodsky/results/electron_tetrahedral_spinor_store.json')['normals'];missing=[next(v for v,x in pts.items() if all(F(b)==F(-h,3) for h,(a,b) in zip(x,w))) for w in norm];d=load('strominger/results/common-three-carrier-protocol/electron.json');L,N=[read_operator(d['operators'][k],8) for k in ('L','N')];block=lambda M,i,j:{(a%2,b%2):z for (a,b),z in M.items() if a//2==i and b//2==j};P=[block(L,i,i) for i in range(4)];I={(0,0):ONE,(1,1):ONE};K=lambda M:{k:z.flip(8) for k,z in M.items()};h=decode({'1':'1/2'});H={(0,0):h,(1,0):h,(0,1):h,(1,1):-h};S={(0,0):ONE,(1,1):decode({'8':'1'})};adj=lambda U:sharp(U,[ONE,ONE]);con=lambda U,M:product(product(U,M),adj(U));queue=[('',I)];rot={}
    for word,U in queue:
        sig=tuple(tuple(sorted((k,tuple(z.c)) for k,z in con(U,M).items())) for M in P[:2]);
        if sig in rot:continue
        rot[sig]=(word,U);queue.extend([(word+'H',product(H,U)),(word+'S',product(S,U))]);
    assert len(rot)==24;out=[];cache={}
    for rec in load('chatgpt/ramsey/ramsey_proton_anti_quarterturn.json'):
        p=rec['binding'];g={p[int(i)-1]:p[j-1] for i,j in rec['rim'].items()};f=tuple(missing.index(g[x]) for x in missing)
        if f not in cache:
            hits=[(w,U,k) for w,U in rot.values() for k in (False,True) if all(con(U,K(M) if k else M)==P[f[i]] for i,M in enumerate(P))];(w,U,k),=hits;assert k;assert all(con(U,K(block(N,i,j)))==block(N,f[i],f[j]) for i in range(4) for j in range(4));sq=product(U,K(U));assert product(sq,sq)=={a:-b for a,b in I.items()};cache[f]=w
        out.append(dict(binding=p,face_permutation=f,apply_before_K='K first, then gates left to right: '+cache[f],fourth_power='-I'))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_electron_anti_quarterturn.json').write_text(json.dumps(out)+'\n')
