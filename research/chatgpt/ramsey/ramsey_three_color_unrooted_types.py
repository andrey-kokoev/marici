"""Independent transfer check: classify old fives by how close they are to being a red neighbourhood. (maximum overlap with any neighbourhood, multiplicity). Compare q-only strata, then smallest common selection of these coarse types."""
from ramsey_root_signature_transfer import D,json,graph,bits,inds,combinations,Counter,Solver

def setup(H):
    T=[t for t in inds(H) if t.bit_count()==5];n=len(H);kinds=[];C=[[-(1+3*i+k),-(1+3*j+k)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(3)]+[[-(1+3*i+k),-(1+3*i+h)] for i in range(n) for k,h in combinations(range(3),2)]
    for t in T:
        sizes=[(h&t).bit_count() for h in H];k=(max(sizes),sizes.count(max(sizes)));kinds.append(k)
    K=sorted(set(kinds));labs={k:1+3*n+i for i,k in enumerate(K)}
    for t,k in zip(T,kinds):
        for ps in combinations(range(3),2):C.append([-labs[k]]+[1+3*i+h for i in bits(t) for h in ps])
    return labs,Counter(kinds),Solver(name='g4',bootstrap_with=C)
if __name__=='__main__':
    data=[setup(graph(l)) for l in (D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()];allk=sorted(set.union(*(set(labs) for labs,_,_ in data)));print(allk)
    def win(sel):return [not sat.solve(assumptions=[labs[k] for k in sel if k in labs]) for labs,c,sat in data]
    tiers={str(ps):win([k for k in allk if k[0] in ps]) for size in range(1,4) for ps in combinations((3,4,5),size)};print(tiers);winners=[]
    for size in range(1,len(allk)+1):
        for s in combinations(allk,size):
            if all(win(s)):winners.append(dict(types=s,rows=[sum(c[k] for k in s) for _,c,_ in data]))
        if winners:break
    print(size,len(winners),min(winners,key=lambda r:sum(r['rows'])));(D/'ramsey_three_color_unrooted_types.json').write_text(json.dumps(dict(allk=allk,tiers=tiers,winners=winners))+'\n')
