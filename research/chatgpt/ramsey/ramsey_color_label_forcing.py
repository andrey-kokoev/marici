"""No privileged color: peel impossible color classes before choosing any triple. Partners of C must individually hit its missed rows. A forced common vertex of the partner family would need both other colors. A stronger test forbids intersecting partner pairs without consulting their row compatibility."""
from ramsey_inverse_five_motifs import D,json,graph,inds,bits,Counter

def audit(H):
    n=len(H);T=[s for s in inds(H) if s.bit_count()==5 and max((s&h).bit_count() for h in H)==4];I=sorted(inds(H));miss=[sum(1<<j for j,t in enumerate(T) if not t&s) for s in I];dis=[sum(1<<j for j,t in enumerate(I) if not s&t) for s in I];adj=[sum(1<<j for j in bits(dis[i]) if not m&miss[j]) for i,m in enumerate(miss)];out={};
    for mode in ('forced_vertex','disjoint','one_row','pair_rows'):
        live=(1<<len(I))-1;rounds=[];ex={}
        while live:
            ban=0;h=Counter();round_example={}
            for i in bits(live):
                p=adj[i]&live;why=None
                if not p:why='no partner'
                else:
                    # Intersection of all possible partners: family must be hit twice disjointly.
                    common=I[next(bits(p))]
                    for j in bits(p):
                        common&=I[j]
                        if not common:break
                    if common:why='forced twice'
                    elif mode!='forced_vertex' and not any(p&dis[j] for j in bits(p)):why='pairwise intersecting'
                    elif mode=='one_row':
                        commonrow=(1<<len(T))-1
                        for j in bits(p):
                            for k in bits(p&dis[j]&~((1<<j)-1)):commonrow&=miss[j]&miss[k]
                            if not commonrow:break
                        if commonrow:why='one common missed row'
                    elif mode=='pair_rows' and not any(p&adj[j] for j in bits(p)):why='remaining row clash'
                if why:
                    ban|=1<<i;h[why]+=1;round_example.setdefault(why,dict(round=len(rounds)+1,support=I[i],partner_count=p.bit_count(),common=common if p else None,missed=T[next(bits(commonrow))] if why=='one common missed row' else None));ex.setdefault(why,round_example[why])
            if not ban:break
            rounds.append(dict(counts=dict(h),examples=round_example));live^=ban
        out[mode]=dict(rounds=rounds,survivors=[I[i] for i in bits(live)],examples=ex)
    return out
if __name__=='__main__':
    z=[audit(graph(l)) for l in (D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()];print([[len(r[k]['survivors']) for k in r] for r in z]);print(z[5]['forced_vertex']['rounds'],z[5]['disjoint']['rounds'],z[5]['pair_rows']['rounds']);(D/'ramsey_color_label_forcing.json').write_text(json.dumps(z)+'\n')
