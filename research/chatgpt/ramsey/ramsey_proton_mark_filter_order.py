"""Endpoint mask on the archived outer-arrow port labels. Compare filtering before vs after alignment; the mask is a proposed interface, not one of the native L/G/N stages."""
from ramsey_proton_handoff_mode_contrast import D,json,F,apply

def weight(z):return sum(a*a+3*b*b for a,b in z.values())
def run():
    ops={}
    for e in json.loads((D.parents[1]/'nima/results/twelve-triangle-1836-arrows.json').read_text()):
        a,b=e['source'],e['target'];ops.setdefault(a[0],[]).append((tuple(a[1:]),tuple(b[1:]),(F(e['weight_real']),F(e['weight_imag_sqrt3']))))
    L,G,N=[ops[k] for k in ('raw','local','aligned')];v=apply(N,{('AB','x'):(1,0)});modes={e:{k:z for k,z in v.items() if k[0]==e} for e,_ in v};out=[]
    for binding in json.loads((D/'ramsey_live_matching_receipt.json').read_text()):
        mark=binding['binding'][0];rows=[]
        for row in binding['rows']:
            values=[]
            for e,side in zip(row['receipt'][:2],(1,0)):
                mask=lambda z:{k:c for k,c in z.items() if k[0][side]==mark};u=apply(L,modes[e]);base=apply(N,apply(G,u));early=apply(N,apply(G,mask(u)));late=mask(base);ratios=[weight(early)/weight(base),weight(late)/weight(base)];assert ratios==[row['bit'],F(1,4)];values.append(list(map(str,ratios)))
            rows.append(dict(row=row['row'],bit=row['bit'],early_late_by_leg=values))
        out.append(dict(binding=binding['binding'],mark=mark,rows=rows))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_proton_mark_filter_order.json').write_text(json.dumps(out)+'\n')
