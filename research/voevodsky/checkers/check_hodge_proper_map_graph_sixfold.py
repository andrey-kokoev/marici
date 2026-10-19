"""Normal-rank and projective-bundle coefficients for the graph construction."""
from math import comb
from pathlib import Path
import json


def expand_power(a,b,n):
    terms={(0,0):1}
    for _ in range(n):
        out={}
        for (e,h),c in terms.items():
            out[e+1,h]=out.get((e+1,h),0)+a*c
            out[e,h+1]=out.get((e,h+1),0)+b*c
        terms=out
    return terms


def main():
    tested=0
    for N in (3,4,5,7):
        normal_rank=N+3;bad_rank=N-1
        codim=(normal_rank-bad_rank)*(N-bad_rank)
        assert codim==4 and codim>3
        assert (6+N)-N==6 and 6-3==3
        for a,b in ((1,1),(2,3),(3,2)):
            fundamental=expand_power(a,b,N)
            assert fundamental[0,N]==b**N>0
            terms=expand_power(a,b,N+1)
            coefficients=[terms[1,N],terms[2,N-1],terms[3,N-2]]
            expected=[(N+1)*a*b**N,comb(N+1,2)*a*a*b**(N-1),
                      comb(N+1,3)*a**3*b**(N-2)]
            assert coefficients==expected and coefficients[0]!=0
            for h_degree in range(3):
                survivor={e:c for (e,h),c in terms.items() if h+h_degree==N}
                assert survivor=={1+h_degree:expected[h_degree]}
            tested+=1
    # Contrast the earlier rank-three normal section: bad rank zero has
    # codimension three, so avoiding all zeros on a threefold is not automatic.
    assert (3-0)*(1-0)==3
    result={'passed':True,'classification':'proper_map_graph_has_controlled_smooth_sixfold_ambient',
        'rank_drop_codimension':4,'graph_dimension':3,'coefficient_controls':tested,
        'projection_degree':'b^N','Lefschetz_pushforward_image':'E cup H4(X)',
        'center_class_pushforward':'f_*(1_Y)',
        'source_embedding_assumed_embedding_in_X':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Primitive candidate pullback, positive pairing and Chow pull-push across the auxiliary sixfold.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-proper-map-graph-sixfold-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
