#!/usr/bin/env python3
"""Fast structural tests for the SCC coordinator."""
from __future__ import annotations
import contextlib
import importlib.util
import io
from pathlib import Path
import unittest

PATH=Path(__file__).with_name("scc.py")
SPEC=importlib.util.spec_from_file_location("marici_scc",PATH)
SCC=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(SCC)

def apparatus_certificate(**overrides):
    cert={
        "authority_locator":"wp970:authority",
        "substrate_state_type":"flavor-source-state",
        "apparatus_state_type":"fdm2-state",
        "observational_rank_certificate":{"locator":"wp970:rank","rank":2,"kernel_pair_promoted_to_state_identity":False},
        "natural_transport_certificate":{"locator":"wp970:naturality","source_authorized":True,"naturality_square_closed":True,"chart_transition_class":"common_gain_on_complete_packet","derivative_transport_included":True,"independent_channel_gains_are_hostile":True},
        "bounded_port_accessibility_certificate":{"locator":"wp970:access","claim":"not_claimed"},
        "conjugate_readout_certificate":{"locator":"grothendieck:4003","carrier_readout":"f","generator_weighted_mate":"Qf","joint_response_matrix":"diag(2f(L),2Lf(L))","same_prepared_carrier":True,"source_authorized":True,"joint_rank":2,"determinant_nonzero_on_admitted_domain":True,"certified_inference":"transversality_only","locates_zero":False,"controlled_successor_test":{"locator":"aspect:successor","perturbation_generator":"calibrated spectral shear","predicted_joint_first_jet":"source first jet","uncertainty_threshold_locator":"aspect:threshold","source_derived_prediction":True,"threshold_preregistered":True,"observer_fitted":False,"null_models":["independent_detector_channels","common_mode_drift"],"outcome":"not_run"}},
        "one_use_joint_map":{"locator":"wp970:one-use","source_authorized":True},
        "labelled_composition_or_tensor_law":{"locator":"wp970:tensor-law"},
        "reset_or_catalytic_return_map":{"locator":"wp970:reset","apparatus_reset_independent":True},
        "repeated_joint_law":{
            "coupling_semantics":"fresh","marginal_signature":"uniform-sign",
            "joint_signature":"fresh-product","two_use_variance":0.5,"covariance":0,
            "preparation_label_side_channel":False,
            "controlled_intervention_admissible":True,
            "triple_composition_closed":True,"mixed_coherence_closed":True,
        },
        "degradation_and_uncertainty_bounds":{"locator":"wp970:bounds"},
        "quotient_descent_certificate":{"locator":"wp970:descent","valid":True},
        "feature_calibration":{"full_authorized_packet":True,"observer_fitted":False,"covariance_observer_fitted":False},
        "admitted_domain":"WP970 FDM-2 uniform-sign kernel","support_assumptions":["calibrated physical packet"],
        "physical_instrument":"wp970:fdm2","candidate_synthesis_status":"candidate_requires_source_derivation",
        "source_derivation_status":"source_derived",
    }
    cert.update(overrides);return cert

class SCCTests(unittest.TestCase):
    def test_help_is_a_successful_discovery_surface(self):
        output=io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(SCC.main(["--help"]),0)
        self.assertIn("Stratified Coherence Compiler",output.getvalue())
        self.assertIn("observer-set",output.getvalue())

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

    def test_lower_theory_requires_complete_operation_vocabulary(self):
        model={"id":"x","owner":"marici.Aspect","classification":"candidate","stratum":"point","inputs":[],"checks":["mapping-cone-admission"],"lower_theory":{"freeze_id":"L1","fingerprint":"abc","operations":["composition"],"tester_ids":["t"],"context_language_completeness":"incomplete","hostile_language_completeness":"incomplete"}}
        errors=SCC.validate_model(model)
        self.assertTrue(any("must include composition" in error for error in errors))

    def test_irreducibility_witness_requires_unequal_records(self):
        model={"lower_theory":{"context_language_completeness":"incomplete","hostile_language_completeness":"incomplete"}}
        packet={"contextual_irreducibility":{"disposition":"irreducible_witnessed","witness":{"lower_equivalent":True,"Cx_record":"same","Cy_record":"same"},"ancillas":[]}}
        errors=SCC.validate_irreducibility_result(packet,model)
        self.assertTrue(any("unequal contextual records" in error for error in errors))

    def test_answer_encoding_ancilla_is_rejected(self):
        model={"lower_theory":{"context_language_completeness":"incomplete","hostile_language_completeness":"incomplete"}}
        packet={"contextual_irreducibility":{"disposition":"irreducible_witnessed","witness":{"lower_equivalent":True,"Cx_record":0,"Cy_record":1},"ancillas":[{"authority":True,"hostile_independent":False,"uniformly_available":True}]}}
        errors=SCC.validate_irreducibility_result(packet,model)
        self.assertTrue(any("answer-encoding ancilla" in error for error in errors))

    def test_complete_languages_forbid_inconclusive(self):
        model={"lower_theory":{"context_language_completeness":"complete","hostile_language_completeness":"complete"}}
        packet={"contextual_irreducibility":{"disposition":"inconclusive_language_incomplete","ancillas":[]}}
        errors=SCC.validate_irreducibility_result(packet,model)
        self.assertTrue(any("inconclusive disposition forbidden" in error for error in errors))

    def test_apparatus_certificate_passes_without_claiming_existence(self):
        result=SCC.validate_apparatus_certificate(apparatus_certificate())
        self.assertEqual(result["status"],"pass")
        self.assertFalse(result["certifies_apparatus_existence"])

    def test_apparatus_certificate_rejects_missing_authority(self):
        cert=apparatus_certificate();cert["authority_locator"]=""
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","authority"))

    def test_apparatus_certificate_distinguishes_shared_coupling(self):
        cert=apparatus_certificate()
        cert["repeated_joint_law"].update({"coupling_semantics":"shared","joint_signature":"shared-bit","two_use_variance":1,"covariance":0.5})
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual(result["status"],"pass")
        self.assertEqual(cert["repeated_joint_law"]["two_use_variance"],1)

    def test_apparatus_certificate_rejects_observer_fitted_covariance(self):
        cert=apparatus_certificate();cert["feature_calibration"]["covariance_observer_fitted"]=True
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","observer_fitting"))

    def test_apparatus_certificate_requires_triple_coherence(self):
        cert=apparatus_certificate();cert["repeated_joint_law"]["triple_composition_closed"]=False
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","higher_coherence"))

    def test_apparatus_candidate_is_inconclusive(self):
        cert=apparatus_certificate(source_derivation_status="candidate_requires_source_derivation")
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("inconclusive","source_derivation"))

    def test_equal_readout_cannot_become_state_identity(self):
        cert=apparatus_certificate();cert["observational_rank_certificate"]["kernel_pair_promoted_to_state_identity"]=True
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","kernel_pair"))

    def test_equal_chartwise_rank_does_not_replace_naturality(self):
        cert=apparatus_certificate();cert["natural_transport_certificate"]["naturality_square_closed"]=False
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","natural_transport"))

    def test_naturality_requires_derivative_transport(self):
        cert=apparatus_certificate();cert["natural_transport_certificate"]["derivative_transport_included"]=False
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","natural_transport_first_jet"))

    def test_fixed_port_requires_noncorrectable_backward_support(self):
        cert=apparatus_certificate();cert["bounded_port_accessibility_certificate"].update({"claim":"fixed_radius","uniform_depth_range_bound":True,"backward_support_correctable":True})
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","bounded_port_accessibility"))

    def test_conjugate_readout_detects_transversality(self):
        result=SCC.validate_apparatus_certificate(apparatus_certificate())
        self.assertEqual(result["status"],"pass")

    def test_conjugate_readout_cannot_claim_zero_location(self):
        cert=apparatus_certificate();cert["conjugate_readout_certificate"]["locates_zero"]=True
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","inference_scope"))

    def test_two_readouts_on_different_carriers_do_not_form_joint_rank(self):
        cert=apparatus_certificate();cert["conjugate_readout_certificate"]["same_prepared_carrier"]=False
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","conjugate_readout"))

    def test_successor_prediction_must_precede_observation(self):
        cert=apparatus_certificate();cert["conjugate_readout_certificate"]["controlled_successor_test"]["observer_fitted"]=True
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","observer_fitting"))

    def test_successor_pass_requires_both_nulls_rejected(self):
        cert=apparatus_certificate();cert["conjugate_readout_certificate"]["controlled_successor_test"].update({"outcome":"pass","all_preregistered_nulls_rejected":False})
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("fail","successor_nulls"))

    def test_pending_successor_derivation_is_inconclusive(self):
        cert=apparatus_certificate(source_derivation_status="candidate_requires_source_derivation");cert["conjugate_readout_certificate"]["controlled_successor_test"]["source_derived_prediction"]=False
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("inconclusive","successor_source_derivation"))

    def test_unregistered_threshold_is_inconclusive_for_candidate(self):
        cert=apparatus_certificate(source_derivation_status="candidate_requires_source_derivation");cert["conjugate_readout_certificate"]["controlled_successor_test"]["threshold_preregistered"]=False
        result=SCC.validate_apparatus_certificate(cert)
        self.assertEqual((result["status"],result["first_failed_gate"]),("inconclusive","successor_threshold"))

if __name__=="__main__":unittest.main()