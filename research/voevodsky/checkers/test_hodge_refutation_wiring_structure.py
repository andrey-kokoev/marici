"""Fast structural regression only: historical math receipts are deliberately mocked.

This does NOT replace fresh --check mathematical evidence validation.
"""
import inspect
import json
from pathlib import Path
import sys
import unittest
from contextlib import ExitStack
from unittest.mock import patch
import check_hodge_conjecture_net as net


class RefutationWiringStructureTests(unittest.TestCase):
    def validate_structure(self):
        with ExitStack() as stack:
            for name,fn in list(vars(net).items()):
                if name.endswith('_report') and inspect.isfunction(fn):
                    module=sys.modules[fn.__module__]
                    stored=json.loads(Path(module.OUT).read_text(encoding='utf-8'))
                    stack.enter_context(patch.object(net,name,lambda stored=stored:stored))
            return net.validate(*net.load_bundle())

    def test_summary_uses_direction_policy_not_port_loop_variable(self):
        r=self.validate_structure()
        self.assertEqual(r['active_refutation_count'],4)
        self.assertEqual(r['dismissed_construction_count'],52)
        self.assertIsNone(r['actual_next_off_reflection_control'])

    def test_refutation_frontier_and_ports(self):
        r=self.validate_structure()
        self.assertEqual((r['node_count'],r['input_port_count']),(70,143))
        self.assertEqual(r['frontier'],['all-algebraic-cycles-annihilation','fixed-candidate-nonalgebraicity','higher-coherence-counterexample-existence'])


if __name__=='__main__':unittest.main()
