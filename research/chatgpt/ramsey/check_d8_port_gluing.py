"""Glue local D8 flag/arrow charts over alternating squares.
Tests agreed incidence axioms separately from an optional closed-surface target.
"""
from itertools import combinations, product
from collections import Counter, defaultdict, deque
from pathlib import Path
import json
from check_klein_four_ramsey33 import graph, audit
from check_state_transport_d8 import ELEMENTS, VERTICES, multiply, inverse, act_vertex, to_arrow


def square_charts(c):
    squares = {}
    for wedge in audit(c)['wedges']:
        x,a,b = wedge['root'],wedge['red'],wedge['blue']
        for y in wedge['completions']:
            red = tuple(sorted((tuple(sorted((x,a))),tuple(sorted((b,y))))))
            blue = tuple(sorted((tuple(sorted((x,b))),tuple(sorted((a,y))))))
            key = red+blue
            squares[key] = (red,blue)
    charts=[]
    for number,(_, (red,blue)) in enumerate(sorted(squares.items())):
        vertices=sorted({v for edge in red for v in edge})
        x=vertices[0]
        a=next(v for edge in red if x in edge for v in edge if v!=x)
        b=next(v for edge in blue if x in edge for v in edge if v!=x)
        y=next(v for v in vertices if v not in (x,a,b))
        position={(0,0):x,(1,0):a,(0,1):b,(1,1):y}
        flags={}
        for state in ELEMENTS:
            tail,head=to_arrow(state)
            flags[state]=(position[tail],position[head])
        assert len(set(position.values()))==4 and len(set(flags.values()))==8
        assert all(c[u][v]==(1 if state[2]==0 else 0) for state,(u,v) in flags.items())
        charts.append({'id':number,'positions':position,'flags':flags,'cycle':[x,a,y,b]})
    return charts


def gf2_rank(rows):
    pivots={}
    for row in rows:
        while row:
            bit=row.bit_length()-1
            if bit in pivots:row^=pivots[bit]
            else:pivots[bit]=row;break
    return len(pivots)


def analyze(c):
    n=len(c);charts=square_charts(c)
    arrows=sorted({arrow for chart in charts for arrow in chart['flags'].values()})
    edges=sorted({tuple(sorted(arrow)) for arrow in arrows})
    # Quotient: physical vertex labels identify positions; flags are identified
    # exactly when their directed endpoints agree. Source equality alone is insufficient.
    flag_occurrences=defaultdict(list)
    for chart in charts:
        for state,arrow in chart['flags'].items():flag_occurrences[arrow].append((chart['id'],state))
    assert len(arrows)==len(flag_occurrences)
    assert all((v,u) in flag_occurrences for u,v in arrows)
    assert len(edges)==n*(n-1)//2  # holds for these selected examples, not assumed generally
    pair_records=[];rigid_failures=[];transition_checks=0
    for left,right in combinations(charts,2):
        a={edge:state for state,edge in left['flags'].items()}
        b={edge:state for state,edge in right['flags'].items()}
        shared=sorted(a.keys()&b.keys())
        transitions={}
        for arrow in shared:
            g=multiply(b[arrow],inverse(a[arrow]));transitions[arrow]=g
            assert multiply(g,a[arrow])==b[arrow]
            assert g[2]==0  # global red/blue labels are fixed in this audit
            assert multiply(g,a[arrow[::-1]])==b[arrow[::-1]]
            la=to_arrow(a[arrow]);rb=to_arrow(b[arrow])
            assert tuple(act_vertex(g,p) for p in la)==rb
            transition_checks+=1
        pair_records.append({'charts':[left['id'],right['id']],
                             'shared_arrows':shared,
                             'transitions':[{'arrow':arrow,'D8':g} for arrow,g in transitions.items()]})
        # Diagnostic ONLY: a single rigid D8 map over all shared bare positions
        # is stronger than port gluing, and may fail even on a good quotient.
        p={v:coord for coord,v in left['positions'].items()}
        q={v:coord for coord,v in right['positions'].items()}
        candidates=[g for g in ELEMENTS if all(act_vertex(g,p[v])==q[v] for v in p.keys()&q.keys())
                    and all(multiply(g,a[edge])==b[edge] for edge in shared)]
        if not candidates:rigid_failures.append([left['id'],right['id']])
    triple_checks=0
    for occurrences in flag_occurrences.values():
        for (_,a),(_,b),(_,d) in combinations(occurrences,3):
            g_ba=multiply(b,inverse(a));g_db=multiply(d,inverse(b));g_da=multiply(d,inverse(a))
            assert multiply(g_db,g_ba)==g_da
            triple_checks+=1
    # Commuting squares attach as four-edge 2-cells. Test endpoint closure.
    incidence=defaultdict(list);link_edges=defaultdict(list)
    for chart in charts:
        cycle=chart['cycle']
        assert len(set(cycle))==4
        assert [c[cycle[i]][cycle[(i+1)%4]] for i in range(4)]==[1,0,1,0]
        for i,u in enumerate(cycle):
            v=cycle[(i+1)%4];edge=tuple(sorted((u,v)))
            incidence[edge].append((chart['id'],1 if u<v else -1))
            link_edges[u].append((cycle[(i-1)%4],v))
    vertex_links=[]
    for vertex in range(n):
        degree=Counter();adjacency=defaultdict(set)
        for a,b in link_edges[vertex]:
            degree[a]+=1;degree[b]+=1;adjacency[a].add(b);adjacency[b].add(a)
        reached=set();todo=[next(iter(degree))] if degree else []
        while todo:
            v=todo.pop()
            if v not in reached:reached.add(v);todo.extend(adjacency[v]-reached)
        vertex_links.append({'vertex':vertex,'link_degrees':dict(degree),
                             'is_connected_cycle':bool(degree) and len(reached)==len(degree) and set(degree.values())=={2}})
    edge_hist=Counter(len(fs) for fs in incidence.values())
    closed_surface=all(len(fs)==2 for fs in incidence.values()) and all(l['is_connected_cycle'] for l in vertex_links)
    color_degrees=[{'vertex':v,'red':sum(c[v][w]==1 for w in range(n)),
                    'blue':sum(c[v][w]==0 for w in range(n))} for v in range(n)]
    if closed_surface:assert all(d['red']==d['blue'] for d in color_degrees)
    orientable=None
    if closed_surface:
        neighbors=defaultdict(list)
        for entries in incidence.values():
            (a,sa),(b,sb)=entries
            neighbors[a].append((b,-sa*sb));neighbors[b].append((a,-sa*sb))
        signs={};orientable=True
        for start in range(len(charts)):
            if start in signs:continue
            signs[start]=1;todo=deque([start])
            while todo:
                a=todo.popleft()
                for b,relative in neighbors[a]:
                    expected=signs[a]*relative
                    if b in signs:orientable &= signs[b]==expected
                    else:signs[b]=expected;todo.append(b)
    indices={e:i for i,e in enumerate(edges)}
    boundaries=[]
    for chart in charts:
        cycle=chart['cycle'];row=0
        for i in range(4):row^=1<<indices[tuple(sorted((cycle[i],cycle[(i+1)%4])))]
        boundaries.append(row)
    rank=gf2_rank(boundaries)
    # The covered one-skeleton is complete and connected in the examples.
    betti=[1,len(edges)-n+1-rank,len(charts)-rank]
    # Every pair of physical labels lies together in a chart. Any further vertex
    # identification would therefore collapse a chart, violating injectivity.
    conflicts={tuple(sorted((a,b))) for chart in charts for a,b in combinations(chart['positions'].values(),2)}
    assert conflicts==set(combinations(range(n),2))
    return {'nodes':n,'charts':len(charts),'framed_ports':len(flag_occurrences),'directed_elementary_arrows':len(arrows),
            'ports_per_node':dict(Counter(a for a,b in arrows)),'color_degrees':color_degrees,
            'local_vertex_occurrences':4*len(charts),'local_flag_occurrences':8*len(charts),
            'basic_port_gluing_passes':True,'patch_embeddings_injective':True,'global_color_consistency':True,
            'pairwise_port_transition_checks':transition_checks,'triple_overlap_port_cocycle_checks':triple_checks,
            'rigid_whole_intersection_transition_failures':rigid_failures,
            'square_face_count_per_edge_histogram':dict(edge_hist),'vertex_links':vertex_links,
            'optional_closed_surface_passes':closed_surface,'closed_surface_orientable':orientable,
            'euler_characteristic':n-len(edges)+len(charts),'betti_numbers_over_F2':betti,
            'minimum_nodes_with_these_prescribed_seams_and_injective_charts':n,
            'minimum_warning':'This minimum is conditional on the prescribed seams; it does not optimize over arbitrary alternative patch gluings.',
            'chart_data':[{'id':p['id'],'cycle':p['cycle'],'positions':[{'local':coord,'global':v} for coord,v in p['positions'].items()]} for p in charts],
            'pairwise_port_transitions':pair_records}


def main():
    cycle=graph(5,[(i,(i+1)%5) for i in range(5)])
    matching=graph(6,[(0,1),(2,3),(4,5)])
    c5=analyze(cycle);m6=analyze(matching)
    assert (c5['charts'],c5['framed_ports'],c5['optional_closed_surface_passes'])==(5,20,True)
    assert (m6['charts'],m6['framed_ports'],m6['optional_closed_surface_passes'])==(6,30,False)
    assert c5['closed_surface_orientable'] and c5['betti_numbers_over_F2']==[1,2,1]
    assert c5['square_face_count_per_edge_histogram']=={2:10}
    assert m6['square_face_count_per_edge_histogram']=={1:12,4:3}
    result={'scope':'Local D8 charts on every alternating square of two fixed complete colored graphs; explicit prescribed endpoint seams.',
            'five_cycle':c5,'six_node_matching':m6,
            'verdict':'Basic equivariant port gluing accepts both. A separately stated closed-square-surface requirement separates them. This geometric requirement is not implied by the D8 algebra and is not yet a universal Ramsey criterion.'}
    path=Path(__file__).with_name('d8_port_gluing_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for label,r in [('C5',c5),('Matching6',m6)]:
        print(label,json.dumps({k:r[k] for k in ['nodes','charts','framed_ports','basic_port_gluing_passes','square_face_count_per_edge_histogram','optional_closed_surface_passes','closed_surface_orientable','euler_characteristic','betti_numbers_over_F2','triple_overlap_port_cocycle_checks']}))
    print('Verified and saved',path)

if __name__=='__main__':main()
