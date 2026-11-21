"""Two successive certified gluing steps, reading only a (3,6;17) seed catalogue."""
from ramsey_port_deletion_chain import D,json,search

def read_seed(line):
    n=line[0]-63;A=[0]*n;t=0
    for j in range(n):
        for i in range(j):
            if ((line[1+t//6]-63)>>(5-t%6))&1:A[i]|=1<<j;A[j]|=1<<i
            t+=1
    return A
if __name__=='__main__':
    for index,line in enumerate((D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines(),1):
        first=search(read_seed(line),7,4)
        if 'graph' not in first:continue
        second=search(first['graph'],8,4)
        if 'graph' in second:
            (D/'ramsey_port_chain_from_17.json').write_text(json.dumps({'source':index,'first':first,'second':second})+'\n');print(index,first['supports'],second['supports']);break
    else:raise AssertionError('no chain found')
