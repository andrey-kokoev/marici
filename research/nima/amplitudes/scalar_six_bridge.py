"""Export the LIVE scalar-six fixture to a candidate Agda calculation.
Python is an untrusted exporter; Agda recomputes every denominator and the
integer cross-multiplication. No claim that Python code itself is verified.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import json
import unittest
from pathlib import Path
import scalar_tree_baseline as source

ROOT = Path(__file__).resolve().parents[3]
AGDA = ROOT/'research/nima/agda'


def independent(ps,coupling):
    # Bitmask census, separate from source's combination/current algorithms.
    records = []
    for mask in range(64):
        if not mask & 1 or mask.bit_count()!=3:
            continue
        labels = tuple(i for i in range(6) if mask & (1<<i))
        q = tuple(sum((ps[i][j] for i in labels),Q(0)) for j in range(4))
        d = q[0]*q[0]-q[1]*q[1]-q[2]*q[2]-q[3]*q[3]
        if d==0:
            raise ValueError('Pole')
        records.append((labels,d,-coupling*coupling/d))
    return sum((r[2] for r in records),Q(0)),records


def integer(q):
    q = Q(q)
    if q.denominator!=1:
        raise ValueError('This fixed-fixture bridge requires integer momenta')
    return f'(pos {q.numerator})' if q>=0 else f'(negsuc {-q.numerator-1})'


def generated():
    value,records = independent(source.SIX,source.COUPLING)
    direct,_ = source.direct_six(source.SIX,source.COUPLING)
    if value!=direct or any(source.recursive(source.SIX,source.COUPLING,r)[0]!=value for r in range(6)):
        raise AssertionError('Independent/live evaluator mismatch')
    if len(records)!=10 or value!=Q(6,25):
        raise AssertionError('Frozen sample changed: review the certificate, do not refit it')
    text = ['{-# OPTIONS --safe --cubical --guardedness #-}', 'module ScalarSixFixture where',
            'open import ScalarSixKernel',
            'open import Cubical.Data.Int.Base using (ℤ; pos; negsuc)',
            '', 'momenta : Label → Momentum']
    text += [f'momenta l{i} = p '+ ' '.join(integer(x) for x in p) for i,p in enumerate(source.SIX)]
    text += ['', 'couplingNumerator couplingDenominator exportedNumerator exportedDenominator : ℤ',
             'couplingNumerator = '+integer(source.COUPLING.numerator),
             'couplingDenominator = '+integer(source.COUPLING.denominator),
             'exportedNumerator = '+integer(value.numerator),
             'exportedDenominator = '+integer(value.denominator)]
    return '\n'.join(text)+'\n',records


class BridgeTests(unittest.TestCase):
    def test_independent_census(self):
        value,records = independent(source.SIX,source.COUPLING)
        self.assertEqual(value,Q(6,25))
        self.assertEqual(len({r[0] for r in records}),10)
        for root in range(6):
            self.assertEqual(source.recursive(source.SIX,source.COUPLING,root)[0],value)

    def test_distinct_scaled_sample(self):
        ps = tuple(tuple(2*x for x in p) for p in source.SIX)
        value,_ = independent(ps,Q(9,10))
        self.assertEqual(value,Q(27,200))
        self.assertEqual(source.recursive(ps,Q(9,10))[0],value)

    def test_missing_duplicate_and_sign_hostiles(self):
        value,records = independent(source.SIX,source.COUPLING)
        self.assertNotEqual(sum((r[2] for r in records[1:]),Q(0)),value)
        self.assertNotEqual(2*value,value)
        self.assertNotEqual(-value,value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-fixture',action='store_true')
    args = parser.parse_args()
    text,records = generated()
    path = AGDA/'ScalarSixFixture.agda'
    if args.write_fixture:
        path.write_text(text,encoding='utf-8')
    elif not path.exists() or path.read_text(encoding='utf-8')!=text:
        raise SystemExit('Fixture drift: explicit review/export required')
    receipt = {'status':'export-consistency-passed-not-a-compiler-receipt',
        'value':'6/25','independent_algorithm':'bitmask channel census',
        'shared_dependency':'Python Fraction; independent arithmetic additionally checked in Agda',
        'channels':records,'fixture_sha256':hashlib.sha256(text.encode()).hexdigest(),
        'agda_source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in AGDA.glob('ScalarSix*.agda')},
        'compiler_status':'Requires separate fresh successful compiler receipt',
        'source_sha256':hashlib.sha256(Path(source.__file__).read_bytes()).hexdigest(),
        'boundary':'Only this fixed live fixture, not arbitrary kinematics or Python semantic verification'}
    out = ROOT/'research/nima/results/scalar-six-bridge.json'
    out.write_text(json.dumps(receipt,default=str,indent=2)+'\n',encoding='utf-8')
    print('Live fixture and independent census agree: 10 channels, M6=6/25')


if __name__=='__main__':
    main()
