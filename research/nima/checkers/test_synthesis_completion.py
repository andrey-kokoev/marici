import ast
import copy
import json
from pathlib import Path
import unittest
from algebra_formula_search import patterns, shapes
from emit_minimum_kernel import tree_prefixes
from build_minimality_cover import leaf_count
from fresh_equational_search import complete, unify, match, GOALS
from check_fresh_equations import verify, infer

BASE=Path(__file__).resolve().parents[1]

class FreshProofTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packet=json.loads(json.dumps(complete((('x0','x1'),('x1','x0')),seconds=1,max_facts=5)))

    def test_direct_axiom_goal(self):
        self.assertIn('commutativity',self.packet['derived'])
        result=verify(self.packet, (('x0','x1'),('x1','x0')))
        self.assertFalse(result['basis_complete'])
        self.assertTrue(result['external_input_bound'])

    def test_occurs_and_nonlinear_match(self):
        self.assertIsNone(unify('x0',('x0','x1')))
        self.assertIsNone(match(('x0','x0'),('x0','x1')))

    def test_unbound_input_rejected(self):
        with self.assertRaises(ValueError): verify(self.packet,('x0','x1'))

    def test_goal_wash_rejected(self):
        p=copy.deepcopy(self.packet); p['goals']={}; p['derived']={}
        with self.assertRaises(ValueError): verify(p)

    def test_status_promotion_rejected(self):
        p=copy.deepcopy(self.packet); p['status']='basis-derived'
        with self.assertRaises(ValueError): verify(p)

    def test_missing_axiom_rejected(self):
        p=copy.deepcopy(self.packet); p['records']=[]
        with self.assertRaises(ValueError): verify(p)

    def test_nonprior_reference_rejected(self):
        with self.assertRaises(ValueError): infer(['call',0,{}],[])

    def test_transitivity_boundary_rejected(self):
        with self.assertRaises(ValueError): infer(['trans',['refl','x0'],['refl','x1']],[])

    def test_congruence_boundary_rejected(self):
        with self.assertRaises(ValueError): infer(['cong',['x0','x1'],[0],['refl','x1']],[])

    def test_derivation_mutation_rejected(self):
        p=copy.deepcopy(self.packet); p['derived']['commutativity']=['refl','x0']
        with self.assertRaises(ValueError): verify(p)

    def test_wolfram_attempts_replayed_without_cached_proof(self):
        for filename in ['fresh-equational-search.json','fresh-equational-search-aged.json','fresh-equational-search-final.json']:
            p=json.loads((BASE/'results'/filename).read_text())
            result=verify(p)
            self.assertGreater(result['facts_checked'],1)
            self.assertFalse(result['basis_complete'])

    def test_no_cached_proof_import_in_fresh_components(self):
        permitted={'collections','itertools','pathlib','argparse','heapq','hashlib','json','time','check_fresh_equations'}
        for name in ['fresh_equational_search.py','check_fresh_equations.py','emit_fresh_equations.py']:
            tree=ast.parse((BASE/'checkers'/name).read_text())
            for node in ast.walk(tree):
                if isinstance(node,ast.ImportFrom): self.assertIn(node.module,permitted)
                if isinstance(node,ast.Import):
                    for entry in node.names: self.assertIn(entry.name,permitted)
        agda=(BASE/'agda/FreshEquationalConsequences.agda').read_text(encoding='utf-8')
        self.assertEqual([line for line in agda.splitlines() if 'import ' in line],
                         ['open import Cubical.Foundations.Prelude'])

class MinimumCoverTests(unittest.TestCase):
    def test_large_tree_frontier_is_prefix_exhaustive(self):
        fronts=[t for t,_,stopped in tree_prefixes(7) if stopped]
        self.assertEqual(len(fronts),429)
        def matches(tree,prefix):
            if prefix=='hole': return True
            if prefix is None: return tree is None
            return tree is not None and matches(tree[0],prefix[0]) and matches(tree[1],prefix[1])
        for cost in range(1,9):
            for tree in shapes(cost):
                self.assertEqual(sum(matches(tree,p) for p in fronts),int(cost>=7))

    def test_all_canonical_words_have_exactly_one_template(self):
        cover=json.loads((BASE/'results/minimality-prefix-cover.json').read_text())
        count=0
        for record in cover['records']:
            # Prefix sets also check non-overlap, not just successful lookup.
            prefixes=[tuple(r['prefix']) for r in record['leaves'] if r['kind']!='noncanonical']
            self.assertEqual(len(prefixes),len(set(prefixes)))
            prefixset=set(prefixes)
            for names in patterns(leaf_count(record['shape'])):
                self.assertEqual(sum(names[:k] in prefixset for k in range(len(names)+1)),1)
                count+=1
        self.assertEqual(count,125105)

    def test_omitted_branch_is_real_negative_mutation(self):
        positive=(BASE/'agda/GeneratedMinimumCoverage.agda').read_text(encoding='utf-8')
        negative=(BASE/'agda/negative/SynthesisMinimumMissingCase.agda').read_text(encoding='utf-8')
        self.assertIn('shape0 0 0 ',positive)
        self.assertNotIn('shape0 0 0 ',negative)
        for line in positive.split('  module W0 =',1)[1].split('  module W1 =',1)[0].splitlines()[1:]:
            if line and not line.startswith('  shape0 0 0 '): self.assertIn(line,negative)

if __name__=='__main__': unittest.main()
