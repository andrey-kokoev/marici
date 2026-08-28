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

    def test_sibling_check_is_not_a_python_requirement(self):
        model={"id":"x","owner":"marici.Aspect","classification":"candidate","stratum":"point","inputs":[],"checks":[{"id":"first","path":"first.py","requires":[]},{"id":"second","path":"second.py","requires":["first"]}]}
        errors=SCC.validate_model(model)
        self.assertTrue(any("requires names sibling check first" in error for error in errors))

if __name__=="__main__":unittest.main()
