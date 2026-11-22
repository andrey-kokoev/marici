"""Act by each row's simultaneous B/R and N/N endpoint reversal on the entire incidence neighbourhood of the third division."""
from ramsey_join_flag_phase import lift,P,T,X,D,json

def run():
    near=[j for j,t in enumerate(T,15) if P[9] in t];assert near==[15,26,29];out={}
    for d in (7,4,9):
        p={}
        for e in P[d]:
            a,b=X[e];p[a],p[b]=b,a
        g=lift(tuple(p[i] for i in range(1,5)));out[d]=dict(columns=p,duads={i:g[i] for i in (0,14,8,3,4,7,9)},partitions={j:g[j] for j in near});assert g[9]==9
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_row_duality_square.json').write_text(json.dumps(out)+'\n')
