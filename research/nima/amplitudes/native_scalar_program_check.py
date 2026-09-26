"""Native DAG -> marked sum/product grammar -> amplitude and diagram tests."""
from collections import Counter
from dataclasses import replace
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import unittest
import native_scalar_program as P
import native_scalar_recursion as N
import native_scalar_fibers as Small
import native_scalar_recursion_check as Fixtures
import scalar_tree_baseline as Old
import scalar_eight_factorization as Eight
ROOT = Path(__file__).resolve().parents[1]
SAMPLES=[]

class Tests(unittest.TestCase):
    def test_programs(self):
        for ps in (Old.FOUR,Old.SIX,Eight.EIGHT,Fixtures.higher_fixture(10),Fixtures.higher_fixture(12)):
            rows = N.construct(ps,Old.COUPLING)
            tree = N.Evaluation(rows)
            program = P.compile_table(rows)
            self.assertEqual(program.value,tree.amplitude)
            self.assertEqual(program.value,Old.recursive(ps,Old.COUPLING)[0])
            self.assertEqual(program.diagram_count,tree.diagram_count)
            self.assertEqual(len(program.factors),sum(len(s)>1 for s in tree.groups))
            # Weights are local coefficients, not one precomputed amplitude.
            for s,w in program.factors:
                d=tree.groups[s]['declaration']
                self.assertEqual(w,-Old.COUPLING if d.amputated else Old.COUPLING/d.denominator)
            if len(ps)<=8:
                words=program.diagrams()
                weights=dict(program.factors)
                self.assertEqual(sum((N.multiply(weights[a] for a in word) for word in words),Q(0)),program.value)
                def edges(word):
                    return tuple(sorted(min(s,tuple(i for i in range(len(ps)) if i not in s),key=lambda a:(len(a),a))
                                        for s in word if s!=tree.remaining))
                self.assertEqual(Counter(edges(w) for w in words),Counter(e for e,_ in tree.diagrams()))
                if len(ps)==8:
                    expected={tuple(sorted(t['ends'])):t['contribution'] for t in Eight.direct_eight(ps,Old.COUPLING)[1]}
                    self.assertEqual({edges(w):N.multiply(weights[a] for a in w) for w in words},expected)
            else:
                with self.assertRaisesRegex(ValueError,'budget'):program.diagrams()
            SAMPLES.append({'legs':len(ps),'instructions':len(program.instructions),'marked_factors':len(program.factors),
                            'diagram_count':program.diagram_count,'value':str(program.value)})

    def test_structural_controls(self):
        program=P.compile_table(N.construct(Old.SIX,Old.COUPLING))
        last=len(program.instructions)-1
        bad=replace(program,instructions=program.instructions[:-1]+(P.Instruction('product',(last,0)),))
        with self.assertRaisesRegex(ValueError,'non-topological'):bad.validate()
        k=next(i for i,s in enumerate(program.instructions) if s.kind=='factor')
        bad=replace(program,instructions=program.instructions[:k]+(P.Instruction('factor',factor=(99,)),)+program.instructions[k+1:])
        with self.assertRaisesRegex(ValueError,'undeclared factor'):bad.validate()
        bad=replace(program,instructions=program.instructions+(P.Instruction('sum',(0,1)),),root=len(program.instructions))
        with self.assertRaisesRegex(ValueError,'unreachable'):bad.validate()
        # A well-typed expression can describe the wrong amplitude. Compare
        # semantics as well as grammar; do not call shape validation physics.
        k=next(i for i,s in enumerate(program.instructions) if s.kind=='sum')
        wrong=replace(program,instructions=program.instructions[:k]+(replace(program.instructions[k],kind='product'),)+program.instructions[k+1:])
        self.assertNotEqual(wrong.value,program.value)
        self.assertNotEqual(wrong.diagram_count,program.diagram_count)


def main():
    out=ROOT/'results/native-scalar-program.json'
    out.unlink(missing_ok=True)
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
    if not result.wasSuccessful():raise SystemExit(1)
    formal_path=ROOT/'results/agda-ScalarAmplitudeResolveFixture.json'
    formal=json.loads(formal_path.read_text(encoding='utf-8-sig'))
    assert formal['passed'] and formal['ignore_interfaces']
    modules=('NativeAmplitudeResolution','AmplitudeDiagramExpansion','ScalarAmplitudeResolveFixture',
             'NativeScalarFiberFixture','ScalarSixKernel','ScalarSixFixture','ScalarSixCertificate',
             'NativeTableResolution','NativeTableRules','IndexedConstructorTables','IndexedResolutionTransport','WholePackageResolution','WholePackageSigmaPi',
             'FiniteFiberAmplitude','TableFibrationCycle','ProofRelevantCoherenceClosure')
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    for m in modules:assert formal['owner_source_inventory_sha256'][m+'.agda']==sha(ROOT/f'agda/{m}.agda')
    audit_path=ROOT/'results/native-amplitude-resolution-formal-audit.json'
    audit=json.loads(audit_path.read_text(encoding='utf-8-sig'))
    assert audit['positive_receipt_sha256'].lower()==sha(formal_path)
    assert audit['checker_sha256'].lower()==sha(ROOT/'checkers/check_native_amplitude_resolution.ps1')
    assert len(audit['controls'])==2
    for c in audit['controls']:
        assert c['correctly_rejected'] and c['exit_code']!=0
        assert c['source_sha256'].lower()==sha(ROOT/f"agda/negative/{c['module']}.agda")
    native=Path(P.__file__).read_text(encoding='utf-8')
    assert '.amplitude' not in native and '.value' not in native.split('def compile_table',1)[1]
    paths=[Path(P.__file__),Path(N.__file__),Path(Small.__file__),Path(Old.__file__),Path(Eight.__file__),Path(Fixtures.__file__),Path(__file__)]+[ROOT/f'agda/{m}.agda' for m in modules]
    packet={'status':'finite-expression-native-Resolve-amplitude-bridge-checked','samples':SAMPLES,
            'source_sha256':{str(p.relative_to(ROOT)):sha(p) for p in paths},'formal_receipt_sha256':sha(formal_path),'formal_audit_sha256':sha(audit_path),
            'formal_scope':'All finite marked sum/product expressions have direct native and actual old Resolve runs, independent readouts and commuting translated readout. Semiring expansion preserves diagram multiplicity. Actual six-point fixture gives 144/600=6/25.',
            'computational_scope':'Native DAG compiled to shared expression grammar and compared through twelve legs; individual diagram weights checked through eight.',
            'remaining':'No proof of Python execution, general partition enumerator correctness, DAG compiler correctness or completeness of physical phi4 diagrams for arbitrary n is asserted.',
            'weights':'Supplied local coefficients and algebra; no arbitrary precomputed-result literal in the compiler.'}
    out.write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    print('PASS: finite-expression Resolve bridge and diagram expansion; compiled native programs checked through n=12.')
if __name__=='__main__':main()
