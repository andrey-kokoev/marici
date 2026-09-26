"""Exact native fiber/legacy amplitude comparisons and hostile controls."""
from dataclasses import asdict, replace
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import hashlib
import json
import random
import re
import unittest
import native_scalar_fibers as N
import scalar_tree_baseline as Old

ROOT = Path(__file__).resolve().parents[1]

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def wire(row):
    payload = {'rows':[wire(r) for r in row.label.rows]} if isinstance(row.label, N.Channel) else asdict(row.label)
    return {'label':{'kind':type(row.label).__name__, **payload}, 'from':row.source, 'to':row.target}

class FiberTests(unittest.TestCase):
    def compare(self, ps, coupling):
        rows = N.construct(ps, coupling)
        value = N.amplitude(rows)
        expected = -coupling if len(ps) == 4 else Old.direct_six(ps, coupling)[0]
        self.assertEqual(value, expected)
        for root in range(len(ps)):
            self.assertEqual(value, Old.recursive(ps, coupling, root)[0])
            self.assertEqual(N.contributions(N.construct(ps, coupling, anchor=root)), N.contributions(rows))
        if len(ps) == 6:
            expected_terms = {tuple(sorted(t['split'])):t['contribution'] for t in Old.direct_six(ps, coupling)[1]}
            self.assertEqual(dict(N.contributions(rows)), expected_terms)
            self.assertEqual(len(expected_terms), 10)
        return rows

    def test_fixtures_and_parameters(self):
        for ps in (Old.FOUR, Old.SIX):
            for c in (Q(0), Q(3,5), Q(-2,3), Q(7,4)):
                self.compare(ps, c)
        self.assertEqual(N.amplitude(N.construct(Old.FOUR, Old.COUPLING)), Q(-3,5))
        self.assertEqual(N.amplitude(N.construct(Old.SIX, Old.COUPLING)), Q(6,25))

    def test_all_permutations(self):
        for order in permutations(range(6)):
            ps = tuple(Old.SIX[i] for i in order)
            rows = N.construct(ps, Old.COUPLING)
            self.assertEqual(dict(N.contributions(rows)),
                             {tuple(sorted(t['split'])):t['contribution'] for t in Old.direct_six(ps, Old.COUPLING)[1]})
            self.assertEqual(N.amplitude(rows), Old.recursive(ps, Old.COUPLING)[0])

    def test_nonuniform_and_scaling(self):
        u = (Q(3,5), Q(4,5), Q(0))
        v = (Q(0), Q(5,13), Q(12,13))
        for a,b in ((Q(1),Q(2)), (Q(2,3),Q(5,4)), (Q(7,3),Q(3,2))):
            e = a+b
            ps = ((e,Q(0),Q(0),e), (e,Q(0),Q(0),-e)) + tuple(
                (-w,) + tuple(sign*w*x for x in d) for w,d in ((a,u),(b,v)) for sign in (-1,1))
            self.compare(ps, Old.COUPLING)
        for s in (Q(1,3), Q(2), Q(5,2)):
            scaled = tuple(tuple(s*x for x in p) for p in Old.SIX)
            self.compare(scaled, Old.COUPLING)
            self.assertEqual(N.amplitude(N.construct(scaled, Old.COUPLING)), Q(6,25)/s**2)

    def test_fibers_and_order(self):
        a = N.construct(Old.FOUR, Q(2), 'a')
        b = N.construct(Old.SIX, Q(3,5), 'b')
        rows = list(a+b)
        random.Random(42).shuffle(rows)
        rows = tuple(replace(r, label=N.Channel(tuple(reversed(r.label.rows))))
                     if isinstance(r.label, N.Channel) else r for r in rows)
        self.assertEqual(N.amplitude(rows, 'a'), Q(-2))
        self.assertEqual(N.amplitude(rows, 'b'), Q(6,25))
        with self.assertRaisesRegex(ValueError, 'declaration'):
            N.amplitude(rows, 'absent')

    def test_missing_duplicate_and_corrupt_rows(self):
        rows = N.construct(Old.SIX, Old.COUPLING)
        with self.assertRaisesRegex(ValueError, 'missing/extra'):
            N.amplitude(rows[:-1])
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            N.amplitude(rows+(rows[-1],))
        channel = rows[-1]
        edge = channel.label.rows[-1]
        wrong_edge = replace(edge, label=replace(edge.label, denominator=edge.label.denominator+1))
        bad = replace(channel, label=N.Channel(channel.label.rows[:-1]+(wrong_edge,)))
        with self.assertRaisesRegex(ValueError, 'propagator'):
            N.amplitude(rows[:-1]+(bad,))
        vertex = channel.label.rows[0]
        wrong_vertex = replace(vertex, label=N.Vertex(Q(999)))
        bad = replace(channel, label=N.Channel((wrong_vertex,)+channel.label.rows[1:]))
        with self.assertRaisesRegex(ValueError, 'vertex weight'):
            N.amplitude(rows[:-1]+(bad,))

    def test_wrong_sum_and_weights(self):
        terms = N.contributions(N.construct(Old.SIX, Old.COUPLING))
        good = sum((w for _,w in terms), Q(0))
        self.assertNotEqual(good, -good)
        self.assertNotEqual(good, good/6)  # spurious permutation divisor
        self.assertNotEqual(good, Q(len(terms)))  # unweighted fiber count
        self.assertNotEqual(good, good-terms[0][1])
        self.assertNotEqual(good, sum((abs(w) for _,w in terms), Q(0)))

    def test_invalid_and_poles(self):
        with self.assertRaisesRegex(ValueError, 'off shell'):
            N.construct((Old.momentum(2,0,0,1),)+Old.FOUR[1:], Old.COUPLING)
        with self.assertRaisesRegex(ValueError, 'conservation'):
            N.construct(Old.FOUR[:3]+(Old.FOUR[2],), Old.COUPLING)
        poles = Old.SIX[:2]+(Old.momentum(-1,0,0,-1),)*2+(Old.momentum(-1,0,0,1),)*2
        with self.assertRaisesRegex(ValueError, 'pole'):
            N.construct(poles, Old.COUPLING)
        with self.assertRaisesRegex(ValueError, 'four/six'):
            N.construct(Old.FOUR*2, Old.COUPLING)


def main():
    receipt_path = ROOT/'results/native-scalar-fiber-amplitude.json'
    receipt_path.unlink(missing_ok=True)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(FiberTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    formal_path = ROOT/'results/agda-NativeScalarFiberFixture.json'
    formal = json.loads(formal_path.read_text(encoding='utf-8-sig'))
    assert formal['passed'] and formal['ignore_interfaces']
    formal_modules = ('NativeScalarFiberFixture', 'FiniteFiberAmplitude', 'TableFibrationCycle',
                      'ScalarSixKernel', 'ScalarSixFixture', 'ScalarSixCertificate')
    for module in formal_modules:
        assert formal['owner_source_inventory_sha256'][module+'.agda'] == sha(ROOT/f'agda/{module}.agda')
    # Bind the integer Agda fixture to these very Python inputs, not just a
    # same-valued amplitude obtained from different source data.
    fixture = (ROOT/'agda/ScalarSixFixture.agda').read_text(encoding='utf-8')
    def integer(kind, n):
        return Q(int(n) if kind == 'pos' else -int(n)-1)
    for i in range(6):
        line = re.search(rf'^momenta l{i} = (.+)$', fixture, re.M).group(1)
        assert tuple(integer(k,n) for k,n in re.findall(r'\((pos|negsuc) (\d+)\)',line)) == Old.SIX[i]
    scalars = {}
    for name in ('couplingNumerator','couplingDenominator','exportedNumerator','exportedDenominator'):
        match = re.search(rf'^{name} = \((pos|negsuc) (\d+)\)', fixture, re.M)
        scalars[name] = integer(*match.groups())
    assert scalars['couplingNumerator']/scalars['couplingDenominator'] == Old.COUPLING
    assert scalars['exportedNumerator']/scalars['exportedDenominator'] == N.amplitude(N.construct(Old.SIX, Old.COUPLING))
    rows = N.construct(Old.SIX, Old.COUPLING)
    native_source = Path(N.__file__).read_text(encoding='utf-8')
    assert 'import scalar_tree_baseline' not in native_source and 'Old.' not in native_source
    inputs = [Path(N.__file__), Path(Old.__file__), Path(__file__)]+[ROOT/f'agda/{m}.agda' for m in formal_modules]
    receipt = {
        'status':'exact-weighted-native-fiber-benchmark-passed', 'tests_run':result.testsRun,
        'permutation_cases':720, 'four_point':'-3/5', 'six_point':'6/25',
        'six_channels':[{'split':s, 'weight':str(w)} for s,w in N.contributions(rows)],
        'native_tables':{'four':[wire(r) for r in N.construct(Old.FOUR, Old.COUPLING)], 'six':[wire(r) for r in rows]},
        'source_sha256':{str(p.relative_to(ROOT)):sha(p) for p in inputs},
        'formal_receipt_sha256':sha(formal_path),
        'formula':'M(b) = sum_{h in H_b} -lambda^V(h) / product_e q_e^2',
        'comparison':'Per-channel equality with direct_six; totals with recursive at every root on declared fixtures; 720 permutations compared at root 0.',
        'formal_scope':'Generic finite weighted-fiber compatibility; actual ScalarSix fixture channel census, propagators, reciprocal checks and native weighted sum 144/600=6/25 checked by Agda.',
        'computational_scope':'Independent native four/six-point rational table construction and evaluation; not an Agda certification of Python execution or QFT rules.',
        'physics_inputs':'massless real phi4; metric +---; all incoming; vertex -i lambda; propagator i/q^2; delta-stripped i M; non-pole rational kinematics',
        'not_claimed':['weights derived from bare fibration','loops or continuum measure','arbitrary multiplicity scattering theorem','native full-Resolve amplitude instantiation'],
        'novel_physical_prediction':False
    }
    receipt_path.write_text(json.dumps(receipt, indent=2, default=str)+'\n', encoding='utf-8')
    print('PASS: native fiber sum M4=-3/5, M6=6/25; ten channel weights match the existing evaluator.')

if __name__ == '__main__':
    main()
