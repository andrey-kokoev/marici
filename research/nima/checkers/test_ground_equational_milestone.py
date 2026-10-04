"""Hostile implementation tests; toy axioms are not evidence for the candidate."""
import unittest
from unittest.mock import patch
import check_double_negation as audit
from ground_equational_milestone import Closure, search, trees
from check_fresh_equations import infer, verify


class GroundMilestoneTests(unittest.TestCase):
    def test_complete_one_parameter_pool(self):
        self.assertEqual([len(trees(k)) for k in range(6)],[1,1,2,5,14,42])
        self.assertEqual(len(set(t for k in range(6) for t in trees(k))),65)

    def test_idempotence_positive_control(self):
        axiom=(('x0','x0'),'x0')
        result=search(axiom,seconds=5,pool_cost=1,instances=10)
        self.assertEqual(result['status'],'goal-derived')
        replay=verify(result['certificate'],axiom)
        self.assertEqual(replay['goals_checked'],['involution'])
        self.assertFalse(replay['basis_complete'])
        self.assertFalse(result['adequacy_constructed'])

    def test_commutativity_does_not_prove_involution(self):
        result=search((('x0','x1'),('x1','x0')),seconds=5,pool_cost=2,instances=100)
        self.assertEqual(result['status'],'unresolved')
        self.assertEqual(result['statistics']['stop'],'instance-pool-exhausted')
        self.assertEqual(result['certificate']['derived'],{})

    def test_instance_limit_is_unresolved(self):
        result=search((('x0','x0'),'x0'),seconds=5,pool_cost=1,instances=0)
        self.assertEqual(result['status'],'unresolved')
        self.assertEqual(result['statistics']['stop'],'instances')

    def test_node_and_clock_limits_are_unresolved(self):
        for limits,stop in [({'nodes':1},'nodes'),({'seconds':0},'seconds'),({'unions':0},'unions')]:
            result=search((('x0','x0'),'x0'),pool_cost=1,**limits)
            self.assertEqual(result['status'],'unresolved')
            self.assertEqual(result['statistics']['stop'],stop)

    def test_every_union_has_prior_sound_justification(self):
        axiom=(('x0','x0'),'x0')
        c=Closure(axiom,seconds=5)
        for k in range(4):
            for t in trees(k): c.add(t)
        for t in trees(2):
            node=c.add(t); lhs=c.add((t,t))
            c.union(lhs,node,('call',0,{'x0':t}),'axiom'); c.rebuild()
        x=c.add('x0'); xx=c.add(('x0','x0'))
        c.union(xx,x,('call',0,{'x0':'x0'}),'axiom'); c.rebuild()
        known=[axiom]
        for r in c.records[1:]:
            self.assertEqual(infer(r['proof'],known),r['equation'])
            known.append(r['equation'])
        for n in range(len(c.terms)):
            self.assertEqual(c.find(n),c.find(x))
            self.assertEqual(infer(c.explain(n,x),known),(c.terms[n],'x0'))
        self.assertGreater(c.congruence_unions,0)

    def test_no_explanation_for_distinct_classes(self):
        c=Closure((('x0','x1'),('x1','x0')))
        a=c.add('x0'); b=c.add(('x0','x0')); c.rebuild()
        with self.assertRaises(ValueError): c.explain(a,b)

    def test_mutated_target_is_rejected(self):
        packet=search((('x0','x0'),'x0'),pool_cost=1)['certificate']
        packet['derived']['involution']=['refl','x0']
        with self.assertRaises(ValueError): verify(packet)

    def test_external_input_is_bound(self):
        packet=search((('x0','x0'),'x0'),pool_cost=1)['certificate']
        with self.assertRaises(ValueError): verify(packet,(('x0','x1'),('x1','x0')))

    def test_unresolved_search_cannot_emit_goal(self):
        with patch.object(audit,'audit',return_value=({'status':'unresolved'},{})):
            with patch('sys.argv',['check_double_negation.py','--emit']):
                with self.assertRaisesRegex(RuntimeError,'no goal theorem'):
                    audit.main()

    def test_forged_basis_status_is_rejected(self):
        packet=search((('x0','x0'),'x0'),pool_cost=1)['certificate']
        packet['status']='basis-derived'
        with self.assertRaises(ValueError): verify(packet)


if __name__=='__main__': unittest.main()
