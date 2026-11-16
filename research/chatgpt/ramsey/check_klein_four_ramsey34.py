"""R(3,4) transfer audit. No tuned diagonal rule; exhaustive labelled extension.
A red graph represents a coloring: nonedges are blue.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
from check_klein_four_ramsey33 import audit, graph
from check_klein_four_diagonal_balance import balanced


def independent_masks(adjacency, size):
    result=[]
    for subset in combinations(range(len(adjacency)),size):
        mask=sum(1<<v for v in subset)
        if all(not(adjacency[v]&mask) for v in subset):result.append(mask)
    return result


def valid_extensions(adjacency):
    n=len(adjacency);full=(1<<n)-1
    blue_triangles=independent_masks(adjacency,3)
    # The new red neighborhood must be independent; its blue neighborhood
    # cannot contain a blue triangle. These are exactly the newly born obstructions.
    for red in range(1<<n):
        blue=full^red
        if any((blue&t)==t for t in blue_triangles):continue
        remaining=red;ok=True
        while remaining:
            bit=remaining&-remaining;remaining-=bit
            if adjacency[bit.bit_length()-1]&red:ok=False;break
        if ok:yield tuple(adjacency[v]|(((red>>v)&1)<<n) for v in range(n))+(red,)


def matrix(adjacency):
    return [[None if a==b else (adjacency[a]>>b)&1 for b in range(len(adjacency))] for a in range(len(adjacency))]


def square_profile(c):
    # Enumerate each matching pair on a four-set once, rather than rooted wedges.
    counts=Counter()
    for a,b,d,e in combinations(range(len(c)),4):
        matchings=[((a,b),(d,e)),((a,d),(b,e)),((a,e),(b,d))]
        for i,red in enumerate(matchings):
            if not all(c[u][v]==1 for u,v in red):continue
            for j,blue in enumerate(matchings):
                if i==j or not all(c[u][v]==0 for u,v in blue):continue
                diagonal=matchings[3-i-j]
                colors=sorted(c[u][v] for u,v in diagonal)
                counts[{(0,0):'BB',(0,1):'RB',(1,1):'RR'}[tuple(colors)]]+=1
    return dict(counts)


def direct_check(adjacency):
    n=len(adjacency)
    assert not any(all((adjacency[a]>>b)&1 for a,b in combinations(t,2)) for t in combinations(range(n),3))
    assert not independent_masks(adjacency,4)


def main():
    parents=[()];levels=[];representatives={};profile_counts=Counter();degree_patterns=Counter();local_counts=Counter()
    blue_link_types=Counter();degree_two_links=0;completion_multiplicities=Counter()
    for n in range(1,10):
        children=[child for parent in parents for child in valid_extensions(parent)]
        levels.append({'vertices':n,'labelled_admissible_colorings':len(children)})
        print('n =',n,'admissible =',len(children),flush=True)
        if n==8:
            for adjacency in children:
                direct_check(adjacency)
                degrees=tuple(sorted(m.bit_count() for m in adjacency));degree_patterns[str(degrees)]+=1
                assert all(d in (2,3) for d in degrees)
                edge_count=sum(degrees)//2
                c=matrix(adjacency);base=audit(c);balance,_=balanced(c,base)
                multiplicities=Counter(len(w['completions']) for w in base['wedges'])
                assert set(multiplicities) <= {1,2}
                completion_multiplicities.update(multiplicities)
                local_counts['square_existence']+=int(bool(base['local_existence']))
                local_counts['square_uniqueness']+=int(bool(base['local_uniqueness']))
                local_counts['diagonal_balance']+=int(balance)
                local_counts['frozen_balanced_closure']+=int(bool(base['local_existence']) and balance)
                profile=square_profile(c)
                profile_counts[str(tuple(sorted(profile.items())))]+=1
                for root in range(8):
                    ids=[v for v in range(8) if v!=root and c[root][v]==0]
                    link=[[c[a][b] for b in ids] for a in ids]
                    link_degrees=tuple(sorted(sum(value==1 for value in row) for row in link))
                    blue_link_types[str((len(ids),link_degrees))]+=1
                    if len(ids)==5:
                        degree_two_links+=1
                        assert audit(link)['local_uniqueness'] and balanced(link)[0]
                if edge_count not in representatives:
                    representatives[edge_count]={
                        'red_edges':[[a,b] for a,b in combinations(range(8),2) if c[a][b]],
                        'degrees':degrees,'square_diagonals':profile,'completion_multiplicities':dict(multiplicities),
                        'local_square_existence':bool(base['local_existence']),
                        'local_square_uniqueness':bool(base['local_uniqueness']),
                        'diagonal_balance':balance,
                    }
        parents=children
    assert levels[-1]['labelled_admissible_colorings']==0
    assert levels[-2]['labelled_admissible_colorings']>0
    # Explicit lower-bound witness independent of the enumerator's first examples.
    wagner=graph(8,[(i,(i+1)%8) for i in range(8)]+[(i,i+4) for i in range(4)])
    wagner_adj=tuple(sum((1<<j) for j in range(8) if wagner[i][j]==1) for i in range(8))
    direct_check(wagner_adj)
    assert independent_masks(wagner_adj,3)
    assert not list(valid_extensions(wagner_adj))
    wagner_profile=square_profile(wagner)
    assert all(wagner_profile.get(k,0)>0 for k in ('RR','RB','BB'))
    # The derived upper bound is necessary but not sufficient: even arbitrarily
    # large perfect matchings have unique local completions and large blue cliques.
    matching=graph(10,[(i,i+1) for i in range(0,10,2)])
    assert audit(matching)['local_uniqueness']
    assert all(matching[a][b]==0 for a,b in combinations([0,2,4,6],2))
    output={
        'scope':'Every labelled red-triangle-free graph with independence number at most 3, grown by all possible new-vertex neighborhoods through n=9; arbitrary invalid colorings are pruned, not sampled.',
        'extension_rule':'New red neighbors are independent in red; new blue neighbors contain no blue triangle.',
        'levels':levels,'eight_vertex_degree_patterns':dict(degree_patterns),
        'eight_vertex_local_rule_counts':dict(local_counts),'eight_vertex_completion_multiplicities':dict(completion_multiplicities),'eight_vertex_square_profile_counts':dict(profile_counts),
        'blue_neighborhood_types':dict(blue_link_types),'five_vertex_blue_links_with_frozen_closure':degree_two_links,
        'representatives_by_red_edge_count':representatives,
        'wagner_witness':{'red_edges':[[a,b] for a,b in combinations(range(8),2) if wagner[a][b]],
                          'square_diagonals':wagner_profile,'red_independence_number':3},
        'capacity_only_counterexample':{'n':10,'red_edges':[[i,i+1] for i in range(0,10,2)],'blue_K4':[0,2,4,6],
                                       'all_mixed_wedges_have_exactly_one_completion':True},
        'verdict':'The frozen rule rejects every 8-vertex critical coloring. Even one critical witness uses RR, RB and BB square diagonals, so a necessary pointwise diagonal-color rule must allow all three. The 8-to-9 obstruction follows from asymmetric neighborhood bounds and degree parity, not a demonstrated global V4 carrier law.'
    }
    path=Path(__file__).with_name('klein_four_ramsey34_results.json')
    path.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print('Local rules:',dict(local_counts));print('Wagner:',wagner_profile);print('Saved',path)

if __name__=='__main__':main()
