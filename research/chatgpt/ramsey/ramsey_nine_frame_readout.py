"""Read the 8 transported k=9 wirings (not a census of other completions). Find all rooted 3-probe coordinates; test geometry of the induced group."""
from ramsey_eight_label_probe_transport import group,E,W,ref,Counter,json,D,combinations
from itertools import permutations

def run():
    G=group();lookup={e:i for i,e in enumerate(E)};edge_maps=[[lookup[tuple(sorted((g[u],g[v])))] for u,v in E] for g in G];base=sum(1<<i for i,e in enumerate(E) if ref[e]);
    def act(g,w):return sum(1<<j for i,j in enumerate(g) if w>>i&1)
    orbit=sorted({act(g,base) for g in edge_maps});assert len(orbit)==8
    coord=lambda w,t:sum((w>>j&1)<<i for i,j in enumerate(t));roots={};good=[]
    for v in W:
        star=[i for i,e in enumerate(E) if v in e];trip=[t for t in combinations(star,3) if len({coord(w,t) for w in orbit})==8];roots[v]=len(trip);good+=trip
    print('root counts',roots,'total',len(good));
    if not good:good=[next(t for t in combinations(range(len(E)),3) if len({coord(w,t) for w in orbit})==8)]
    t=good[0];O=sorted(orbit,key=lambda w:coord(w,t));actions={tuple(coord(act(g,w),t) for w in O) for g in edge_maps};dist=Counter((u^v).bit_count() for u,v in combinations(O,2));order_dist=Counter();
    for a in actions:
        p=tuple(range(8));k=0
        while True:
            k+=1;p=tuple(a[i] for i in p)
            if p==tuple(range(8)):break
        order_dist[k]+=1
    translations=[a[0] for a in actions if all(a[i]==a[0]^i for i in range(8))];affine=sum(all(a[i]^a[j]^a[0]==a[i^j] for i,j in combinations(range(8),2)) for a in actions);iso=sum(all((i^j).bit_count()==(a[i]^a[j]).bit_count() for i,j in combinations(range(8),2)) for a in actions)
    columns=Counter(sum(((w>>i)&1)<<k for k,w in enumerate(O)) for i in range(len(E)));print('probe', [E[j] for j in t],'distinct actions',len(actions),'affine',affine,'cube isometries',iso,'xor',translations,'orders',order_dist,'distances',dist,'link distributions',Counter({n:sum(c for x,c in columns.items() if x.bit_count()==n) for n in range(9)}),flush=True)
    shapes=Counter()
    for mask,count in columns.items():
        vs=[i for i in range(8) if mask>>i&1];ds=sorted((i^j).bit_count() for i,j in combinations(vs,2));shape={0:'empty',8:'whole'}.get(len(vs))
        if len(vs)==2:shape={1:'edge',3:'body_diagonal'}[ds[0]]
        if len(vs)==4:assert ds==[1,1,1,1,2,2];shape='face'
        assert shape;shapes[shape]+=count
    assert iso==24 and all((a[0].bit_count()+sum((a[1<<i]^a[0])>(a[1<<j]^a[0]) for i,j in combinations(range(3),2)))%2==0 for a in actions)
    from ramsey_eight_label_probe_transport import sig
    root_types=Counter((sig[v].bit_count(),n) for v,n in roots.items());print('shapes',shapes,'root types',root_types)
    return dict(shapes=dict(shapes),root_types={str(k):v for k,v in root_types.items()},root_counts=roots,readout=[E[i] for i in t],coordinate_ordered_wirings=O,actions=sorted(actions),affine=affine,isometries=iso,xor_translations=sorted(translations),distances=dict(dist),orders=dict(order_dist),link_truth_tables=columns)
if __name__=='__main__':(D/'ramsey_nine_frame_readout.json').write_text(json.dumps(run())+'\n')
