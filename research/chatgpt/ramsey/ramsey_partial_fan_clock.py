"""Audit partial synchronization: inclusion-minimal sets of shared internal visit times forcing opposite seams, with all fan pins retained."""
from itertools import combinations,product
from ramsey_stuttering_fan_clock import admissible_pairs,D,json

def run():
    out=[]
    for p,rows in admissible_pairs():
        pairs=list(product(*rows));controls={};force=[]
        for k in range(5):
            for js in combinations(range(1,5),k):
                fits=[(x,y) for x,y in pairs if all(x[0][j]==y[0][j] for j in js)];diff=sum(x[1]!=y[1] for x,y in fits);controls[str(js)]=[len(fits)-diff,diff]
                if fits and diff==len(fits) and not any(set(s)<=set(js) for s in force):force.append(js)
        best=[(x,y) for x,y in pairs if x[0][2:]==y[0][2:] and x[2]==y[2]==1];assert force==[(2,)] and best;assert all(x[0][2]==4 for x,y in pairs if x[0][2]==y[0][2]);out.append(dict(binding=''.join(p),minimal=force,counts_same_opposite=controls,witness=best[0]))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_partial_fan_clock.json').write_text(json.dumps(out)+'\n')
