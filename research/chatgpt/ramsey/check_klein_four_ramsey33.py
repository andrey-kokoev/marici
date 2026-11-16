"""Exhaustive R(3,3) audit of explicitly chosen local V4-square rules.
These rules are candidates, not claimed native Marici operations.
Standard library only. Run this file to regenerate the JSON evidence.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json


def coloring(n, mask):
    adjacency = [[None]*n for _ in range(n)]
    for bit,(u,v) in enumerate(combinations(range(n),2)):
        adjacency[u][v] = adjacency[v][u] = (mask >> bit) & 1
    return adjacency


def triangles(c):
    return [(a,b,d,c[a][b]) for a,b,d in combinations(range(len(c)),3)
            if c[a][b] == c[a][d] == c[b][d]]


def audit(c):
    n = len(c)
    # 1 = red, 0 = blue. A wedge is x--red-->a, x--blue-->b.
    # Completing vertex y has a--blue-->y and b--red-->y.
    # Four distinct vertices give r=(x a)(b y), b=(x b)(a y).
    both = all(any(c[x][a] == 1 for a in range(n) if a != x)
               and any(c[x][b] == 0 for b in range(n) if b != x) for x in range(n))
    wedges = []
    for x in range(n):
        for a in range(n):
            if c[x][a] != 1: continue
            for b in range(n):
                if c[x][b] != 0: continue
                completions = [y for y in range(n) if y not in (x,a,b) and c[a][y] == 0 and c[b][y] == 1]
                wedges.append({'root':x,'red':a,'blue':b,'completions':completions})
    return {'both_colors_at_every_vertex':both,
            'local_existence':both and all(w['completions'] for w in wedges),
            'local_uniqueness':both and all(len(w['completions']) == 1 for w in wedges),
            'wedges':wedges}


def record(c):
    return {'n':len(c),
            'red_edges':[[a,b] for a,b in combinations(range(len(c)),2) if c[a][b] == 1],
            'blue_edges':[[a,b] for a,b in combinations(range(len(c)),2) if c[a][b] == 0],
            'monochromatic_triangles':triangles(c), **audit(c)}


def graph(n, red_edges):
    red = {tuple(sorted(e)) for e in red_edges}
    return [[None if i == j else int(tuple(sorted((i,j))) in red) for j in range(n)] for i in range(n)]


def verify_square_laws(c):
    squares = set()
    for w in audit(c)['wedges']:
        x,a,b = w['root'],w['red'],w['blue']
        for y in w['completions']:
            r = {x:a,a:x,b:y,y:b}
            s = {x:b,b:x,a:y,y:a}
            vertices = (x,a,b,y)
            assert all(r[r[v]] == s[s[v]] == v and r[s[v]] == s[r[v]] for v in vertices)
            assert all(len({v,r[v],s[v],r[s[v]]}) == 4 for v in vertices)
            squares.add(tuple(sorted((tuple(sorted((x,a))),tuple(sorted((b,y)))))) +
                        tuple(sorted((tuple(sorted((x,b))),tuple(sorted((a,y)))))))
    return len(squares)


def main():
    rows = []
    for n in (4,5,6):
        counts = Counter()
        examples = {}
        for mask in range(1 << (n*(n-1)//2)):
            c = coloring(n,mask)
            free = not triangles(c)
            result = audit(c)
            if n == 6 and result['local_uniqueness']:
                red_degrees = [sum(value == 1 for value in row) for row in c]
                assert set(red_degrees) in ({1},{4}), 'Unexpected six-vertex unique-square model'
            counts['total'] += 1
            counts['triangle_free'] += int(free)
            for rule in ('local_existence','local_uniqueness'):
                passes = bool(result[rule])
                counts[rule+'_passes'] += int(passes)
                counts[rule+('_true_positive' if passes and free else '_false_positive' if passes else '_false_negative' if free else '_true_negative')] += 1
                if passes != free:
                    key = rule+('_false_positive' if passes else '_false_negative')
                    if key not in examples: examples[key] = {'mask':mask,**record(c)}
        rows.append({'n':n,'counts':dict(counts),'first_counterexamples':examples})
        print(n,dict(counts))
    assert [r['counts']['triangle_free'] for r in rows] == [18,12,0]
    cycle = graph(5,[(i,(i+1)%5) for i in range(5)])
    matching = graph(6,[(0,1),(2,3),(4,5)])
    assert not triangles(cycle) and audit(cycle)['local_uniqueness']
    assert triangles(matching) and audit(matching)['local_uniqueness']
    assert verify_square_laws(cycle) == 5
    assert verify_square_laws(matching) == 6
    cuts=[]
    for removed in range(5):
        keep=[v for v in range(5) if v!=removed]
        cut=[[cycle[i][j] for j in keep] for i in keep]
        assert not audit(cut)['local_existence']
        repair_masks=[]
        for mask in range(16):
            extension=[row+[int((mask>>i)&1)] for i,row in enumerate(cut)]
            extension.append([int((mask>>i)&1) for i in range(4)]+[None])
            if audit(extension)['local_uniqueness'] and not triangles(extension):repair_masks.append(mask)
        assert repair_masks
        cuts.append({'removed_original_vertex':removed,'remaining_original_vertices':keep,
                     'cut':record(cut),'minimum_added_vertices_for_unique_triangle_free_completion':1,
                     'all_one_vertex_repair_masks':repair_masks})
    extensions=[]
    for mask in range(32):
        extension=[row+[int((mask>>i)&1)] for i,row in enumerate(cycle)]
        extension.append([int((mask>>i)&1) for i in range(5)]+[None])
        checked=audit(extension)
        assert triangles(extension) and not checked['local_uniqueness']
        extensions.append({'new_vertex_red_mask':mask,'monochromatic_triangle_count':len(triangles(extension)),
                           'local_existence':bool(checked['local_existence']),'local_uniqueness':bool(checked['local_uniqueness'])})
    result={'scope':'All 64 + 1024 + 32768 labelled two-colorings; explicitly selected local square rules, not all possible Klein-four carrier models.',
            'color_convention':{'1':'red','0':'blue'},
            'rule':'Both colors at every vertex; each mixed wedge x-R-a and x-B-b must have a distinct y with a-B-y and b-R-y. Uniqueness additionally requires exactly one y.',
            'census':rows,'five_cycle':record(cycle),'six_vertex_matching_counterexample':record(matching),
            'five_cycle_alternating_squares':5,'six_vertex_matching_alternating_squares':6,
            'five_cycle_vertex_cuts':cuts,'all_five_cycle_one_vertex_extensions':extensions,
            'six_vertex_unique_rule_classification':'Exactly the 15 perfect matchings and their 15 color complements.',
            'verdict':'Local commuting-square existence and uniqueness do not characterize triangle avoidance or explain the 5-to-6 Ramsey threshold. Vertex deletion also fails to preserve this local closure.'}
    target=Path(__file__).with_name('klein_four_ramsey33_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Verified and saved',target)

if __name__ == '__main__':main()
