"""Finite word closure, exact conditional phase lift, and resource boundaries."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_hinge_phase_continuation as phase


class HingePhaseTests(unittest.TestCase):
    def test_actual_source_group_is_closed(self):
        group,mul,spin=phase.source_group()
        self.assertEqual(len(group),24)
        self.assertTrue(all(mul(a,b) in group for a in group for b in group))
        self.assertTrue(all(sum(x*x for x in q)==1 for q in group))
        self.assertEqual(spin((Q(2),Q(-1),Q(-1),Q())),(((Q(2),Q(-1)),(Q(-1),Q())),((Q(1),Q()),(Q(2),Q(1)))))

    def test_spin_convention_and_geometric_hinge(self):
        F=phase.F;_,_,spin=phase.source_group()
        U=phase.scale(F(1)/phase.SQ6,phase.from_spin(spin,(Q(2),Q(-1),Q(-1),Q())))
        self.assertEqual(phase.mm(phase.adj(U),U),phase.eye(2))
        R=phase.spatial(U)
        self.assertEqual(sum(R[i][i] for i in range(3)),F(Q(5,3)))
        self.assertEqual(phase.mm(R,[[F()],[F(1)],[F(1)]]),[[F()],[F(1)],[F(1)]])

    def test_full_fixture_controller_and_retained_records(self):
        before={p:p.read_bytes() for p in (phase.STORE,phase.OWNER)}
        r=phase.build()
        self.assertTrue(r['finite_protocol_word_hinge_excluded'])
        self.assertTrue(r['moving_frame_intertwining_verified'])
        self.assertTrue(r['moving_frame_changes_native_projector'])
        self.assertEqual(r['conditional_herald_probabilities'],['3/8','3/8','1/4'])
        self.assertEqual(r['face_mixer_capture_counterexamples'],{'0':'0','1/2':'16/25','1':'1'})
        self.assertTrue(r['all_failure_records_retained'])
        self.assertEqual(r['actual_stored_stage_entries_verified'],144)
        self.assertEqual(r['full_raw_controller_unitary_dimension'],24)
        self.assertTrue(r['raw_logical_controller_intertwining_verified'])
        self.assertFalse(r['capture_release_law_derived'])
        self.assertTrue(all(p.read_bytes()==data for p,data in before.items()))

    def test_scope_guards(self):
        c=json.loads(phase.CONTRACT.read_text(encoding='utf-8'))
        for key in ('all_source_implementations_excluded','continuous_generator_native_licensed',
                    'controller_preparation_native_licensed','controlled_selector_native_licensed',
                    'moving_face_adapter_native_licensed','herald_probability_is_annihilation_probability',
                    'capture_release_law_derived','outgoing_photon_factorization_constructed',
                    'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError):phase.validate_contract(bad)


if __name__=='__main__':unittest.main()
