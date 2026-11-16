"""Second audit: add opposite-colored diagonals to every local V4 square.
Preserves the first checker and its evidence. No external dependencies.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from check_klein_four_ramsey33 import coloring, triangles, audit, graph, record


def balanced(c, baseline=None):
    baseline = baseline or audit(c)
    failures = []
    for wedge in baseline['wedges']:
        x,a,b = wedge['root'],wedge['red'],wedge['blue']
        for y in wedge['completions']:
            if c[x][y] == c[a][b]:
                failures.append({'square':[x,a,y,b], 'diagonals':[[x,y],[a,b]], 'shared_diagonal_color':c[x][y]})
    return not failures, failures


def is_induced_c5(c):
    return len(c) == 5 and not triangles(c) and all(sum(v == 1 for v in row) == 2 for row in c)


def forbidden_four_sets(c):
    # Equal diagonals in an alternating square are exactly an induced red C4
    # or induced red 2K2 (with the complementary pattern in blue).
    found = []
    for subset in combinations(range(len(c)),4):
        degrees = sorted(sum(c[a][b] == 1 for b in subset if b != a) for a in subset)
        if degrees in ([1,1,1,1],[2,2,2,2]):
            found.append(subset)
    return found


def main():
    census = []
    for n in (3,4,5,6):
        counts = Counter()
        for mask in range(1 << (n*(n-1)//2)):
            c = coloring(n,mask)
            base = audit(c)
            diagonal_balance,_ = balanced(c,base)
            assert diagonal_balance == (not forbidden_four_sets(c))
            free = not triangles(c)
            rules = {
                'baseline_unique':bool(base['local_uniqueness']),
                'balanced_existence':bool(base['local_existence'] and diagonal_balance),
                'balanced_unique':bool(base['local_uniqueness'] and diagonal_balance),
            }
            counts['total'] += 1
            counts['triangle_free'] += int(free)
            for rule,passes in rules.items():
                counts[rule+'_passes'] += int(passes)
                counts[rule+('_true_positive' if passes and free else '_false_positive' if passes else '_false_negative' if free else '_true_negative')] += 1
            assert rules['balanced_existence'] == is_induced_c5(c)
            assert rules['balanced_unique'] == is_induced_c5(c)
        census.append({'n':n,'counts':dict(counts)})
        print(n,dict(counts))
    cycle = graph(5,[(i,(i+1)%5) for i in range(5)])
    matching = graph(6,[(0,1),(2,3),(4,5)])
    assert balanced(cycle)[0] and not balanced(matching)[0]
    # Key lemma: a vertex outside an induced C5 in a diagonally balanced graph
    # must be all-red or all-blue to the cycle. Exhaust every attachment.
    extension_masks = []
    extensions = []
    for mask in range(32):
        c = [row+[(mask>>i)&1] for i,row in enumerate(cycle)]
        c.append([(mask>>i)&1 for i in range(5)]+[None])
        base = audit(c)
        balance,_ = balanced(c,base)
        if balance:extension_masks.append(mask)
        assert not (base['local_existence'] and balance)
        extensions.append({'attachment_red_mask':mask,'diagonal_balance':balance,
                           'local_existence':bool(base['local_existence']),
                           'monochromatic_triangle_count':len(triangles(c))})
    assert extension_masks == [0,31]
    # A triangle-free four-node path witnesses that the added rule is too strong
    # to characterize Ramsey avoidance for all n.
    path = graph(4,[(0,1),(1,2),(2,3)])
    assert not triangles(path) and balanced(path)[0] and not audit(path)['local_existence']
    output = {
        'rule':'Both colors at every vertex; every mixed wedge completes to an alternating square; every such square has opposite-colored diagonals.',
        'extra_axiom_warning':'Diagonal balance is an additional coloring axiom, not a consequence of the Klein-four group laws.',
        'census':census,
        'six_vertex_matching_rejection':{'coloring':record(matching),'failures':balanced(matching)[1]},
        'all_five_cycle_extensions':extensions,
        'diagonally_balanced_extension_masks':extension_masks,
        'triangle_free_four_vertex_rejected_example':record(path),
        'finite_result':'The augmented rule accepts exactly the 12 labeled C5 colorings for n=3..6.',
        'general_theorem':'For finite complete two-colored graphs with both colors at every vertex, balanced square existence holds if and only if the red graph is a five-cycle (and the blue graph its complement). See the accompanying proof note.',
        'verdict':'Repairs the 5-to-6 test, but rigidly selects C5 rather than explaining general Ramsey-number growth.',
    }
    target = Path(__file__).with_name('klein_four_diagonal_balance_results.json')
    target.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print('Verified and saved',target)

if __name__ == '__main__':main()
