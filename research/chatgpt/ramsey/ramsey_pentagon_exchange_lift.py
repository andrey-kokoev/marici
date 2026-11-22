"""Lift both core exchanges at the exit connection to the bipartite Hall carrier. Compare their square with the independently defined literal row swap, not just with an unlabelled reflection."""
from ramsey_polarity_receipt_quotient import check,m,mate,D,json
from ramsey_antipode_extension import run as polarity
from ramsey_row_quotient_constructor import R,P,T,move

def run():
    pol,=polarity();f=pol['map'];q=check();a=q['petersen_outer'];b=q['petersen_inner'];mid={x:y for x,y,_ in q['neither_receipt_both']};flags={(P.index(d),j) for j,t in enumerate(T,15) for d in t};out=[]
    for k in (2,-2):
        g={}
        for i in range(5):
            j=k*i%5;g[a[i]]=b[j];g[b[i]]=a[j];g[mid[a[i]]]=mid[a[j]]
        g.update({f[x]:f[y] for x,y in list(g.items())});assert move(flags,g)==flags
        for flip in (False,True):
            h={x:f[y] if flip else y for x,y in g.items()};sq=[h[h[i]] for i in range(30)];u,v=move(m,h),move(mate,h);out.append(dict(slope=k,dual=flip,literal_square=sq==R,exit_image=h[29],image_of_selected_exit=sorted((h[7],h[29])),common_with_m=len(u&m),common_with_mate=len(u&mate),square_exchanges_rows=move(m,sq)==mate,square_fixed=[i for i,y in enumerate(sq) if i==y]));assert sq==R and flags-(m|mate|u|v)==set(pol['absolute_flags']) and not (m|mate)&(u|v)
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_pentagon_exchange_lift.json').write_text(json.dumps(out)+'\n')
