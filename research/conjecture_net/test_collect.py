import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import collect


class CollectionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.home = self.root / 'research/conjecture_net'
        self.home.mkdir(parents=True)
        for key, value in [('ROOT', self.root), ('HOME', self.home)]:
            context = patch.object(collect, key, value)
            context.start()
            self.addCleanup(context.stop)
        self.source = self.root / 'research/owner/contracts/example-conjecture-net.json'
        self.source.parent.mkdir(parents=True)
        self.source.write_text(json.dumps({'id': 'example', 'conjectures': [], 'proof': 'research/owner/proof.agda'}))
        (self.root / 'research/owner/proof.agda').write_text('module proof where\n')

    def test_collects_referenced_evidence_and_registry(self):
        self.assertEqual(collect.build(True)['status'], 'pass')
        self.assertEqual(collect.build()['status'], 'pass')
        self.assertTrue((self.home / 'collection/research/owner/proof.agda').exists())
        registry = json.loads((self.home / 'registry.json').read_text())
        self.assertEqual(registry['nets'][0]['id'], 'example')
        self.assertEqual(registry['nets'][0]['status'], 'not evaluated by collection')

    def test_other_net_families_and_snapshot_are_classified(self):
        state = self.source.parent / 'theta-interaction-net-state.v1.json'
        state.write_text(json.dumps({'schema': 'marici.scc.rh-interaction-net-state-contract.v1'}))
        snapshot = self.root / 'research/owner/replay.json'
        snapshot.write_text(json.dumps({'after_snapshot': {'actions': []}}))
        pointer = self.source.parent / 'pointer.json'
        pointer.write_text(json.dumps({'schema': 'marici.conjecture-net.outcome-pointer.v1'}))
        entries = collect.registry({p.relative_to(self.root).as_posix(): ''
                                    for p in (state, snapshot, pointer)})['nets']
        self.assertEqual(len(entries), 2)
        self.assertTrue(any(e['classification'] == 'versioned interaction-net state contract' for e in entries))
        self.assertTrue(any('replay action-net snapshot' in e['classification'] for e in entries))

    def test_local_hodge_net_and_typed_attachment_survive_registry_regeneration(self):
        contracts = self.home / 'contracts'
        contracts.mkdir()
        net = contracts / 'hodge-conjecture-net.v1.json'
        net.write_text(json.dumps({'schema': 'marici.hodge-conjecture-net.v1',
                                   'id': 'hodge-test', 'conjectures': []}))
        attachment = contracts / 'hodge-foundational-attachments.v1.json'
        attachment.write_text(json.dumps({'schema': 'marici.hodge-foundational-attachments.v1',
                                          'connections': [], 'work_net': str(net)}))
        entries = collect.registry({})['nets']
        self.assertEqual(len(entries), 2)
        self.assertEqual({entry['classification'] for entry in entries},
                         {'conjecture-net contract', 'typed foundational attachment index (not an independent conjecture net)'})
        self.assertTrue(all(entry['collected_contract'] is None for entry in entries))
        self.assertTrue(all(entry['status'] == 'not evaluated by collection' for entry in entries))

    def test_operational_programme_without_legacy_phase_does_not_break_registry(self):
        contracts = self.home / 'contracts'
        contracts.mkdir()
        (contracts / 'programme-hierarchy.v18.json').write_text(json.dumps({
            'schema': 'marici.physics-programme.research-net.v18', 'id': 'programme-v18',
            'root': {'id': 'physical-root'}, 'conjectures': []}))
        programmes = collect.registry({})['programme_hierarchies']
        self.assertEqual(len(programmes), 1)
        self.assertIsNone(programmes[0]['phase'])
        self.assertEqual(programmes[0]['root'], 'physical-root')

    def test_source_drift_requires_refresh(self):
        collect.build(True)
        self.source.write_text('{}')
        self.assertEqual(collect.build()['status'], 'fail')

    def test_copy_drift_detected_without_changing_original(self):
        original = self.source.read_bytes()
        collect.build(True)
        target = self.home / 'collection' / self.source.relative_to(self.root)
        target.write_text('tampered')
        self.assertEqual(collect.build()['status'], 'fail')
        self.assertEqual(self.source.read_bytes(), original)

    def test_no_recursive_collection(self):
        collect.build(True)
        first = collect.discover()
        collect.build(True)
        self.assertEqual(first, collect.discover())
        self.assertFalse(any('/collection/' in path for path in first))

    def test_unindexed_files_fail_closed(self):
        collect.build(True)
        (self.home / 'collection/extra.json').write_text('{}')
        self.assertEqual(collect.build()['status'], 'fail')


if __name__ == '__main__':
    unittest.main()
