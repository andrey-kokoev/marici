import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research/scattering/high-energy'))
import high_energy_scattering_net as scattering


class HighEnergyScatteringTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads(scattering.CONTRACT.read_text())
        self.pins = json.loads(scattering.PINS.read_text())

    def validate(self):
        return scattering.validate(self.contract, self.pins, verify_sources=False)

    def test_shared_metric_graph_is_wired(self):
        contract, pins, graph = self.validate()
        self.assertEqual(len(graph.actions), 11)
        self.assertEqual(graph.metrics()['active_action_count'], 10)
        self.assertEqual(graph.metrics()['frontier_width'], 1)
        self.assertEqual(contract['objective']['outcome'], None)

    def test_unknown_dependency_rejected(self):
        self.contract['conjectures'][0]['depends_on'] = ['absent-source-claim']
        with self.assertRaisesRegex(ValueError, 'unknown dependency'):
            self.validate()

    def test_cycle_rejected(self):
        self.contract['conjectures'][0]['depends_on'] = [self.contract['conjectures'][-1]['id']]
        with self.assertRaisesRegex(ValueError, 'dependency cycle'):
            self.validate()

    def test_duplicate_claim_rejected(self):
        self.contract['conjectures'].append(copy.deepcopy(self.contract['conjectures'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            self.validate()

    def test_historical_receipt_not_proof(self):
        self.contract['conjectures'][0]['outcome'] = '++'
        with self.assertRaisesRegex(ValueError, 'silently admitted'):
            self.validate()

    def test_prepared_columns_not_full_S(self):
        self.contract['boundary']['prepared_columns_are_full_S'] = True
        with self.assertRaisesRegex(ValueError, 'scientific promotion'):
            self.validate()

    def test_kernel_replay_not_fresh_solve(self):
        self.contract['actions'][0]['fresh_stationary_solve'] = True
        with self.assertRaisesRegex(ValueError, 'strength promotion'):
            self.validate()

    def test_replay_argv_is_fixed(self):
        self.contract['actions'][0]['arguments'][1] = '../../unrelated-input.npz'
        with self.assertRaisesRegex(ValueError, 'argv changed'):
            self.validate()

    def test_missing_member_pin_rejected(self):
        del self.pins['archive_members'][scattering.ARCHIVE]['packet_comparison.json']
        with self.assertRaisesRegex(ValueError, 'evidence incomplete'):
            self.validate()

    def test_source_path_escape_rejected(self):
        for name in ('../outside', '/outside', 'C:/outside', 'research/scattering/high-energy/../../outside'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                scattering.source_path(name)

    def test_missing_sources_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, 'stale source'):
                scattering.validate(self.contract, self.pins, root=Path(directory))

    def test_archive_member_drift_rejected_before_execution(self):
        pins = copy.deepcopy(self.pins)
        pins['archive_members'][scattering.ARCHIVE][scattering.MEMBERS[0]]['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'member drift'):
            scattering.prepare(ROOT / '.ai/tmp/high-energy-scattering-hostile', pins)

    def test_workspace_escape_rejected(self):
        with self.assertRaisesRegex(ValueError, 'workspace must be'):
            scattering.prepare(ROOT / 'research/scattering/high-energy', self.pins)

    def test_replay_numerical_discrepancy_rejected(self):
        from zipfile import ZipFile
        with ZipFile(ROOT / scattering.ARCHIVE) as archive:
            saved = json.loads(archive.read('packet_comparison.json'))
        current = copy.deepcopy(saved)
        self.assertEqual(scattering.compare_replay(current, saved), 0)
        current['rows'][0]['response128']['peak_transport'] += 1e-4
        with self.assertRaisesRegex(ValueError, 'replay discrepancy'):
            scattering.compare_replay(current, saved)

    def test_physical_map_excluded_from_frontier(self):
        _, _, graph = self.validate()
        physical = next(a for a in graph.actions if a.name == 'physical-calibration-and-species')
        self.assertEqual(physical.status, 'pruned')
        self.assertIsNone(self.contract['objective']['outcome'])

    def test_live_programme_attachment_preserves_other_branches(self):
        scattering.validate_programme()

    def test_registry_and_collection_wiring(self):
        registry = json.loads((ROOT / 'research/conjecture_net/registry.json').read_text())
        entry = next(e for e in registry['nets'] if e['id'] == 'scattering.high-energy.v1')
        self.assertEqual(entry['classification'], 'conjecture-net contract')
        self.assertEqual(entry['status'], 'not evaluated by collection')
        inventory = json.loads((ROOT / 'research/conjecture_net/inventory.json').read_text())
        for path in (scattering.CONTRACT, scattering.PINS, Path(scattering.__file__)):
            item = next(e for e in inventory['files'] if e['source'] == path.relative_to(ROOT).as_posix())
            self.assertEqual(item['sha256'], scattering.digest(path))
            self.assertEqual((ROOT / 'research/conjecture_net' / item['collected']).read_bytes(), path.read_bytes())


if __name__ == '__main__':
    unittest.main()
