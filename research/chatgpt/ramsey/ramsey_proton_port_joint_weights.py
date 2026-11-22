"""Exact joint-projector squared weights of single coordinate preparations and of the equally weighted mixture of the three coordinates of each outer-arrow port."""
from ramsey_proton_handoff_mode_contrast import D,json,F

def run():
    src=json.loads((D.parents[1]/'nima/results/twelve-triangle-1836-arrows.json').read_text());diag={}
    for e in src:
        s,a,k=e['source'];_,b,l=e['target'];
        if (a,k)==(b,l):assert F(e['weight_imag_sqrt3'])==0;diag[s,a,k]=F(e['weight_real'])
    ports={}
    for a in sorted({a for _,a,_ in diag}):
        coord={}
        for k in 'xyz':
            l,g,n=(diag[s,a,k] for s in ('raw','local','aligned'));w=(n,l-n,g-n,1-l-g+n);assert g==F(1,12) and n==l*g and min(w)>0;coord[k]=w
        avg=tuple(sum(col)/3 for col in zip(*coord.values()));assert avg==tuple(F(i,36) for i in (1,11,2,22));ports[a]=dict(coordinates={k:list(map(str,v)) for k,v in coord.items()},mean=list(map(str,avg)))
    assert len(ports)==12;return ports
if __name__=='__main__':
    out=run();print(out['AB']);(D/'ramsey_proton_port_joint_weights.json').write_text(json.dumps(out)+'\n')
