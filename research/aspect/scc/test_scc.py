#!/usr/bin/env python3
"""Fast structural tests for the SCC coordinator."""
from __future__ import annotations
import importlib.util
from pathlib import Path
import unittest

PATH=Path(__file__).with_name("scc.py")
SPEC=importlib.util.spec_from_file_location("marici_scc",PATH)
SCC=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(SCC)

class SCCTests(unittest.TestCase):
    def test_real_registry_is_valid(self):
        models,errors=SCC.discover()
        self.assertFalse(errors)
        self.assertIn("bivariant-network-v15",models)

    def test_missing_fields_are_named(self):
        errors=SCC.validate_model({"id":"x"})
        self.assertIn("missing required field: owner",errors)
        self.assertIn("missing required field: checks",errors)

    def test_dependency_layers_are_topological(self):
        models={"a":{"depends_on":[]},"b":{"depends_on":["a"]},"c":{"depends_on":["a"]},"d":{"depends_on":["b","c"]}}
        layers,blocked=SCC.execution_layers(models)
        self.assertEqual(layers,[["a"],["b","c"],["d"]])
        self.assertEqual(blocked,[])

    def test_cycle_is_blocked(self):
        models={"a":{"depends_on":["b"]},"b":{"depends_on":["a"]}}
        layers,blocked=SCC.execution_layers(models)
        self.assertEqual(layers,[])
        self.assertEqual(blocked,["a","b"])

    def test_workspace_escape_is_rejected(self):
        with self.assertRaises(ValueError):SCC.workspace_path("../outside")

    def test_constructor_synthesis_is_bounded_and_attaches_hostile(self):
        model={"id":"x","missing_constructors":["source-derived relative normalization between target lines"],"next_falsifier":"test simultaneous frame rescaling"}
        report=SCC.synthesize(model)
        self.assertEqual(report["status"],"candidate_menu_not_truth_certificate")
        self.assertEqual(report["candidates"][0]["rule"],"relative-normalization")
        self.assertIn("discriminating_hostile",report["candidates"][0])

    def test_higher_cocycle_gets_next_degree_constructor(self):
        report=SCC.synthesize({"id":"x","missing_constructors":["first source-derived degree above the frozen cocycle profile"]})
        self.assertEqual(report["candidates"][0]["rule"],"higher-coherence-extension")
        self.assertIn("proper face",report["candidates"][0]["discriminating_hostile"])

    def test_constructor_synthesis_refuses_vocabulary_free_guess(self):
        report=SCC.synthesize({"id":"x","missing_constructors":["unknown thing"]})
        self.assertEqual(report["status"],"no_rule_match")
        self.assertEqual(report["candidates"],[])

    def test_sibling_check_is_not_a_python_requirement(self):
        model={"id":"x","owner":"marici.Aspect","classification":"candidate","stratum":"point","inputs":[],"checks":[{"id":"first","path":"first.py","requires":[]},{"id":"second","path":"second.py","requires":["first"]}]}
        errors=SCC.validate_model(model)
        self.assertTrue(any("requires names sibling check first" in error for error in errors))

if __name__=="__main__":unittest.main()