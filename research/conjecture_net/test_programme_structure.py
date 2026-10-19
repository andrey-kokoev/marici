import copy
import json
import unittest
from check_programme_structure import HOME, validate


class ProgrammeTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v1.json').read_text())
        self.terms = json.loads((HOME / 'contracts/programme-terms.v1.json').read_text())

    def test_structure_checkpoint(self):
        result = validate(self.hierarchy, self.terms)
        self.assertEqual(result['nodes'], 6)
        self.assertEqual(result['unresolved_terms'], 9)
        self.assertIsNone(result['root_outcome'])

    def test_premature_outcome_rejected(self):
        self.hierarchy['root']['outcome'] = '++'
        with self.assertRaisesRegex(ValueError, 'cannot admit'):
            validate(self.hierarchy, self.terms)

    def test_proof_edge_rejected(self):
        self.hierarchy['structural_edges'][0]['proof_bearing'] = True
        with self.assertRaisesRegex(ValueError, 'cannot imply proof'):
            validate(self.hierarchy, self.terms)

    def test_unknown_term_rejected(self):
        self.hierarchy['root']['scope_terms'].append('undefined')
        with self.assertRaisesRegex(ValueError, 'unknown term'):
            validate(self.hierarchy, self.terms)

    def test_unreviewed_net_link_rejected(self):
        self.hierarchy['existing_net_links'].append({'source_net': 'sector'})
        with self.assertRaisesRegex(ValueError, 'await repository review'):
            validate(self.hierarchy, self.terms)

    def test_cyclic_structure_rejected(self):
        edge = copy.deepcopy(self.hierarchy['structural_edges'][0])
        edge['from'], edge['to'] = edge['to'], edge['from']
        self.hierarchy['structural_edges'].append(edge)
        with self.assertRaisesRegex(ValueError, 'cyclic hierarchy'):
            validate(self.hierarchy, self.terms)

    def test_automatic_aggregation_rejected(self):
        self.hierarchy['promotion_policy']['automatic_child_outcome_aggregation'] = True
        with self.assertRaisesRegex(ValueError, 'unsafe promotion'):
            validate(self.hierarchy, self.terms)


if __name__ == '__main__':
    unittest.main()
