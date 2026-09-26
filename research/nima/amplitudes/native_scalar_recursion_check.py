"""Cross-check general native scalar recursion without using legacy builders."""
from collections import Counter
from dataclasses import asdict, replace
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json
import random
import unittest
import native_scalar_recursion as N
import native_scalar_fibers as Small
import scalar_tree_baseline as Old
import scalar_eight_factorization as Eight

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = []


def higher_fixture(n):
    m = (n-2)//2
    weights = tuple(Q(2**k) for k in range(m))
    energy = sum(weights,Q(0))
    ps = [(energy,Q(0),Q(0),energy),(energy,Q(0),Q(0),-energy)]
    for k,w in enumerate(weights):
        t = Q(k+1,k+3)
        direction = ((1-t*t)/(1+t*t),2*t/(1+t*t),Q(0))
        ps.extend((-w,)+tuple(sign*w*x for x in direction) for sign in (-1,1))
    return tuple(ps)


def count(n):
    v = (n-2)//2
    return factorial(3*v)//(factorial(v)*6**v)


class Tests(unittest.TestCase):
    def compare(self, ps, root):
        rows = N.construct(ps,Old.COUPLING,root)
        evaluated = N.Evaluation(rows)
        self.assertEqual(evaluated.amplitude,Old.recursive(ps,Old.COUPLING,root)[0])
        self.assertEqual(evaluated.diagram_count,count(len(ps)))
        SAMPLES.append({'legs':len(ps),'root':root,'momenta':ps,'coupling':Old.COUPLING,
                        'amplitude':evaluated.amplitude,'diagram_count':evaluated.diagram_count,
                        'row_count':len(rows),'current_count':len(evaluated.groups)})
        return evaluated

    def test_partition_census(self):
        for size in (1,3,5,7,9,11):
            labels = tuple(2*i+1 for i in range(size))
            actual = N.partitions(labels)
            self.assertEqual(set(actual),set(Old.partitions_three(labels)))
            self.assertEqual(len(actual),len(set(actual)))
            for blocks in actual:
                self.assertEqual(tuple(sorted(x for block in blocks for x in block)),labels)
                self.assertTrue(all(len(block)%2==1 for block in blocks))
                self.assertEqual(tuple(block[0] for block in blocks),tuple(sorted(block[0] for block in blocks)))

    def test_four_six(self):
        for ps in (Old.FOUR,Old.SIX):
            for root in range(len(ps)):
                e = self.compare(ps,root)
                self.assertEqual(e.amplitude,Small.amplitude(Small.construct(ps,Old.COUPLING)))
                diagrams = e.diagrams()
                self.assertEqual(len(diagrams),count(len(ps)))
                self.assertEqual(sum((w for _,w in diagrams),Q(0)),e.amplitude)

    def test_eight_independent_topologies_and_weights(self):
        for ps in (Eight.EIGHT,Eight.outgoing_pairs((Q(1),Q(2),Q(3)))):
            direct,terms = Eight.direct_eight(ps,Old.COUPLING)
            expected = {tuple(sorted(t['ends'])):t['contribution'] for t in terms}
            self.assertEqual(len(expected),280)
            for root in range(8):
                e = self.compare(ps,root)
                diagrams = e.diagrams()
                self.assertEqual(Counter(edges for edges,w in diagrams),Counter({edges:1 for edges in expected}))
                self.assertEqual(dict(diagrams),expected)
                self.assertEqual(e.amplitude,direct)

    def test_higher(self):
        for n,roots in ((10,(0,4,9)),(12,(0,))):
            ps = higher_fixture(n)
            values = []
            for root in roots:
                e = self.compare(ps,root)
                values.append(e.amplitude)
                with self.assertRaisesRegex(ValueError,'budget'):
                    e.diagrams(limit=10000)
            self.assertTrue(all(v==values[0] for v in values))

    def test_scaling_permutation_and_zero(self):
        ps = Eight.EIGHT
        base = N.amplitude(N.construct(ps,Old.COUPLING))
        scaled = tuple(tuple(Q(2)*x for x in p) for p in ps)
        self.assertEqual(N.amplitude(N.construct(scaled,Old.COUPLING)),base/Q(2)**4)
        self.assertEqual(N.amplitude(N.construct(ps,2*Old.COUPLING)),base*8)
        self.assertEqual(N.amplitude(N.construct(ps,Q(0))),0)
        rng = random.Random(812)
        for _ in range(10):
            order = list(range(8));rng.shuffle(order)
            self.assertEqual(N.amplitude(N.construct(tuple(ps[i] for i in order),Old.COUPLING)),base)

    def test_row_order_and_fibers(self):
        rows = list(N.construct(Old.FOUR,Q(2),boundary='a')+N.construct(Eight.EIGHT,Old.COUPLING,boundary='b'))
        random.Random(33).shuffle(rows)
        self.assertEqual(N.amplitude(rows,'a'),-2)
        self.assertEqual(N.amplitude(rows,'b'),Eight.direct_eight(Eight.EIGHT,Old.COUPLING)[0])

    def test_structural_guards(self):
        rows = N.construct(Eight.EIGHT,Old.COUPLING)
        branch_i = next(i for i,r in enumerate(rows) if isinstance(r.label,N.Branch))
        branch = rows[branch_i]
        with self.assertRaisesRegex(ValueError,'partition'):
            N.Evaluation(rows[:branch_i]+rows[branch_i+1:])
        with self.assertRaisesRegex(ValueError,'duplicate'):
            N.Evaluation(rows+(branch,))
        bad = replace(branch,label=N.Branch((branch.source,)*3))
        with self.assertRaisesRegex(ValueError,'child attachment'):
            N.Evaluation(rows[:branch_i]+(bad,)+rows[branch_i+1:])
        ci = next(i for i,r in enumerate(rows) if isinstance(r.label,N.Current) and r.label.denominator is not None)
        bad = replace(rows[ci],label=replace(rows[ci].label,denominator=rows[ci].label.denominator+1))
        with self.assertRaisesRegex(ValueError,'current declaration'):
            N.Evaluation(rows[:ci]+(bad,)+rows[ci+1:])
        ri = next(i for i,r in enumerate(rows) if isinstance(r.label,N.Current) and r.label.amputated)
        bad = replace(rows[ri],label=replace(rows[ri].label,denominator=Q(0),amputated=False))
        with self.assertRaisesRegex(ValueError,'current declaration'):
            N.Evaluation(rows[:ri]+(bad,)+rows[ri+1:])
        extra = Small.Row(N.Current((99,),(Q(0),)*4,None,False),N.address('b',(99,)),'declaration')
        with self.assertRaisesRegex(ValueError,'unreachable'):
            N.Evaluation(rows+(extra,))

    def test_domain(self):
        with self.assertRaisesRegex(ValueError,'even multiplicity'):
            N.construct(Old.SIX[:-1],Old.COUPLING)
        with self.assertRaisesRegex(ValueError,'root'):
            N.construct(Old.SIX,Old.COUPLING,6)
        with self.assertRaisesRegex(ValueError,'off shell'):
            N.construct(((Q(2),Q(0),Q(0),Q(1)),)+Old.FOUR[1:],Old.COUPLING)
        poles = Old.SIX[:2]+(Old.momentum(-1,0,0,-1),)*2+(Old.momentum(-1,0,0,1),)*2
        for c in (Q(0),Old.COUPLING):
            with self.assertRaisesRegex(ValueError,'pole'):
                N.construct(poles,c)


def main():
    output = ROOT/'results/native-scalar-recursion.json'
    output.unlink(missing_ok=True)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    source = Path(N.__file__).read_text(encoding='utf-8')
    assert 'import scalar_tree_baseline' not in source and 'Old.' not in source
    inputs = (Path(N.__file__),Path(Small.__file__),Path(Old.__file__),Path(Eight.__file__),Path(__file__))
    packet = {'status':'arbitrary-even-n-native-scalar-recursion-implemented',
              'tests_run':result.testsRun,'samples':SAMPLES,
              'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
              'algorithm_domain':'Even n>=4, massless phi4 trees, rational conserved non-pole external momenta, supplied coupling and Feynman conventions.',
              'implementation':'Native three-column DAG; every odd partition and child attachment retained; memoized readout; no legacy evaluator call.',
              'checked':'4/6 all roots; two 8-point fixtures all roots, all 280 individual topology weights; 10 points roots 0/4/9; 12 points root 0; structural, scaling, permutation, pole and expansion-budget controls.',
              'formal_status':'Computational general-n implementation and finite checks; not an arbitrary-n Agda correctness proof or a full NativeTableResolution instantiation.',
              'complexity':'Exponential in multiplicity; diagram expansion separately budgeted; no claim of tractable arbitrarily large inputs.',
              'novel_physical_prediction':False}
    output.write_text(json.dumps(packet,indent=2,default=str)+'\n',encoding='utf-8')
    print('PASS: native arbitrary-even-n recursion; checked through 12 legs / 1,401,400 retained diagram choices.')

if __name__=='__main__':
    main()
