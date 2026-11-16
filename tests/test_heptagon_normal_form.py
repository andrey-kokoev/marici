import importlib.util
from hashlib import sha256
from itertools import combinations, permutations
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE=Path(__file__).resolve().parents[1]/'research/chatgpt/ramsey'
sys.path.insert(0,str(HERE))
from heptagon_profile import PAIRS, PROFILE, profile_orbit
from heptagon_completion_classification import classify, canonical_order, switch_certificate
from pauli_realization_audit import decode_graph6, triangle_free, independent_witness
from pauli_low_cost_structure import span, parity_closed_heptagons
CHECKER=HERE/('drat-checker/target/release/ramsey-drat-checker'+('.exe'if os.name=='nt'else''))

class NormalFormTests(unittest.TestCase):
    def test_profile_and_compression_certificates(self):
        self.assertEqual(len(profile_orbit()),7);self.assertEqual(sum(PROFILE),14)
        self.assertEqual([sum(c for pair,c in zip(PAIRS,PROFILE)if i in pair)for i in range(7)],[4]*7)
        data=json.loads((HERE/'heptagon-profile-completions.json').read_text())
        self.assertEqual(data['completion_count'],4)
        self.assertEqual(len({r['graph6']for r in data['records']}),4)
        for record in data['records']:
            rows=decode_graph6(record['graph6']);self.assertTrue(triangle_free(rows))
            self.assertIsNone(independent_witness(rows,7));self.assertEqual([r.bit_count()for r in rows],[6]*22)
            cycles,_=parity_closed_heptagons(rows);self.assertEqual(len(cycles),4)
            cert=record['compression_certificate'];masks=[]
            for relation in cert['independent_relations']:
                mask=sum(1<<(i-1)for i in relation['vertices_1based']);masks.append(mask)
                self.assertTrue(all((r&mask).bit_count()%2==0 for r in rows))
            self.assertEqual(len(masks),6);self.assertEqual(len(set(span(masks))),64)
            indices=[i-1 for i in cert['nonsingular_principal_vertices_1based']]
            minor=[sum(((rows[i]>>j)&1)<<k for k,j in enumerate(indices))for i in indices]
            self.assertEqual(len(indices),16);self.assertEqual(len(set(span(minor))),65536)
            strings=cert['pauli_realization']['paulis'];self.assertEqual(len(strings),22)
            self.assertTrue(all(len(s)==8 for s in strings))
            for i,j in combinations(range(22),2):
                parity=sum((a in 'XW'and b in 'ZW')+(a in 'ZW'and b in 'XW')for a,b in zip(strings[i],strings[j]))%2
                self.assertEqual(parity,(rows[i]>>j)&1)

    def test_isomorphism_classification(self):
        data=json.loads((HERE/'heptagon-profile-completions.json').read_text());groups=classify(data['records'])
        self.assertEqual(sorted(len(g['members'])for g in groups),[2,2])
        for group in groups:
            source=decode_graph6(data['records'][group['representative_record_0based']]['graph6'])
            for member in group['members']:
                target=decode_graph6(data['records'][member['record_0based']]['graph6']);mapping=member['representative_to_member_0based']
                self.assertEqual(sorted(mapping),list(range(22)))
                self.assertTrue(all(((source[i]>>j)&1)==((target[mapping[i]]>>mapping[j])&1)for i,j in combinations(range(22),2)))

    def test_square_switch_and_shared_relations(self):
        data=json.loads((HERE/'heptagon-profile-completions.json').read_text())
        cert=switch_certificate(data['records'],classify(data['records']))
        source=decode_graph6(data['records'][cert['source_record_0based']]['graph6'])
        target=decode_graph6(data['records'][cert['target_record_0based']]['graph6'])
        changed=source[:]
        for i,j in cert['removed_edges_0based']:
            self.assertTrue(changed[i]>>j&1);changed[i]^=1<<j;changed[j]^=1<<i
        for i,j in cert['added_edges_0based']:
            self.assertFalse(changed[i]>>j&1);changed[i]|=1<<j;changed[j]|=1<<i
        self.assertEqual(changed,target)
        common=[sum(1<<i for i in s)for s in cert['shared_relation_supports_0based']]
        self.assertEqual(len(set(span(common))),32)
        for rows,field in [(source,'source_extra_relation_0based'),(target,'target_extra_relation_0based')]:
            extra=sum(1<<i for i in cert[field]);self.assertEqual(len(set(span(common+[extra]))),64)
            self.assertTrue(all((row&mask).bit_count()%2==0 for row in rows for mask in common+[extra]))
        supports=[set(parity_closed_heptagons(decode_graph6(r['graph6']))[0])for r in data['records']]
        self.assertTrue(all(s==supports[0]for s in supports))

    def test_lex_leader_orientation(self):
        # Exhaustive small graph check of the transposition-comparator argument.
        pairs=list(combinations(range(4),2))
        for bits in range(1<<len(pairs)):
            rows=[0]*4
            for k,(i,j)in enumerate(pairs):
                if bits>>k&1:rows[i]|=1<<j;rows[j]|=1<<i
            order=min(permutations(range(4)),key=lambda p:tuple((rows[p[i]]>>p[j])&1 for i,j in pairs))
            for i in range(3):
                j=i+1;others=[k for k in range(4)if k not in(i,j)]
                self.assertLessEqual(tuple((rows[order[i]]>>order[k])&1 for k in others),tuple((rows[order[j]]>>order[k])&1 for k in others))

    @unittest.skipUnless(importlib.util.find_spec('pysat'),'optional python-sat dependency')
    def test_core_proof_input_digests(self):
        from heptagon_forcing_probe import build_formula
        for filename,mode in [('heptagon-other-profile-lex-cadical-probe.json','other-profile'),('heptagon-profile-completions.json','fixed-profile')]:
            receipt=json.loads((HERE/filename).read_text());clauses,nvars,edges,_=build_formula(mode,lex=True)
            self.assertFalse(receipt['strengthened'])
            if mode=='fixed-profile':
                for record in receipt['records']:
                    rows=decode_graph6(record['graph6'])
                    clauses.append([-v if rows[i]>>j&1 else v for(i,j),v in edges.items()])
            text=f'p cnf {nvars} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n'for c in clauses)
            self.assertEqual(sha256(text.encode()).hexdigest(),receipt['cnf_sha256'])
            self.assertTrue(receipt['proof_independently_checked'])
            self.assertEqual(receipt['independent_check']['cnf_sha256'],receipt['cnf_sha256'])
            self.assertEqual(receipt['independent_check']['proof_sha256'],receipt['proof_sha256'])

    @unittest.skipUnless(importlib.util.find_spec('pysat'),'optional python-sat dependency')
    def test_strengthened_and_lex_encodings_accept_known_model(self):
        from heptagon_forcing_probe import build_formula
        from pysat.solvers import Solver
        line=(HERE/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines()[186]
        rows=decode_graph6(line);cycles,_=parity_closed_heptagons(rows)
        order=canonical_order(rows,next(iter(cycles.values())))
        for strengthened in(False,True):
            for mode,expected in [('baseline',True),('fixed-profile',True),('other-profile',False),('two-zero',False),('sparse',False)]:
                clauses,_,edges,_=build_formula(mode,strengthen=strengthened,lex=True)
                assumptions=[v if rows[order[i]]>>order[j]&1 else -v for(i,j),v in edges.items()]
                with Solver(name='cadical195',bootstrap_with=clauses)as solver:self.assertEqual(solver.solve(assumptions=assumptions),expected)

    @unittest.skipUnless(CHECKER.exists(),'build the independent Rust checker first')
    def test_checker_accepts_and_rejects_fixtures(self):
        fixtures=[('p cnf 1 2\n1 0\n-1 0\n','0\n',True),
                  ('p cnf 1 1\n1 0\n','0\n',False),
                  ('p cnf 1 1\n1 0\n','1 0\n',False),
                  ('p cnf 1 1\n1 0\n','-1 0\n0\n',False)]
        with tempfile.TemporaryDirectory()as directory:
            for formula,proof,expected in fixtures:
                cnf=Path(directory)/'input.cnf';drat=Path(directory)/'input.drat'
                cnf.write_text(formula);drat.write_text(proof)
                run=subprocess.run([str(CHECKER),str(cnf),str(drat)],capture_output=True,text=True)
                self.assertEqual(run.returncode==0,expected)

if __name__=='__main__':unittest.main()
