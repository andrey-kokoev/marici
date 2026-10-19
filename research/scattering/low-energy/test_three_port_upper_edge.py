"""Regression controls for the upper-edge auxiliary certificate."""
import unittest
import check_three_port_upper_edge as edge


class UpperEdgeTests(unittest.TestCase):
    def test_inverse_with_zero_first_pivot(self):
        A=[[edge.F(0),edge.F(2)],[edge.F(3),edge.F(4)]]
        edge.verify_inverse(A,edge.inverse(A))

    def test_singular_matrix_refused(self):
        A=[[edge.F(1),edge.F(2)],[edge.F(2),edge.F(4)]]
        with self.assertRaisesRegex(AssertionError,'singular upper-threshold block'):
            edge.inverse(A)

    def test_actual_fixture_and_convention_boundary(self):
        report=edge.build()
        self.assertEqual(report['upper_block_rank'],11)
        self.assertEqual(report['coefficient_limit'],'I3')
        self.assertEqual(report['endpoint_amplitude_limit'],'-I3')
        A=report['certified_inverse_norm_upper_bound']
        self.assertTrue((edge.F(A*A)-edge.F(*report['squared_whitened_frobenius_norm'])).positive())
        self.assertEqual(report['certified_packet_probability_constant']*edge.Q(report['certified_energy_window_width']),1)
        self.assertFalse(report['finite_flux_assigned_at_threshold'])
        self.assertFalse(report['new_live_proposition_admitted'])
        self.assertFalse(report['C12_protocol_renewed'])


if __name__=='__main__':unittest.main()
