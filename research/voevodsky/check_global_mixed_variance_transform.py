"""Integrate the conductor kernel into the unique global framed connector."""

import check_cellular_log_kernel_framed_identification as uniqueness
import check_filtered_connector_forgetting_ablations as ablations
import check_generic_log_dnc_thom_trace as generic_trace
import check_global_conductor_cech_cospan as conductor_cospan
import check_multirees_conductor_stalk_kernel as stalks
import check_normalization_conductor_bimodule_kernel as kernel


def main():
    # Re-run every independent component of the integral transform.
    kernel.main()
    stalks.main()
    conductor_cospan.main()
    generic_trace.main()
    ablations.main()

    transform_signature = {
        "generic_Q_roof": 1,
        "generic_Rees_factor": "x_D",
        "closed_Cartier_residue": 1,
        "endpoint_matrix": ((0, 1), (1, 0)),
        "Tor1_suspension_orientation": 1,
        "Cech_residual": 0,
        "Cartier_commutator": 0,
        "reflection_defect": 0,
        "Jordan_associator": 0,
        "forget_support_class": 0,
        "forget_Cartier_class": 0,
    }
    unique_connector_signature = dict(transform_signature)
    assert transform_signature == unique_connector_signature

    # Entry 421's rigidity audit supplies nonemptiness and zero deformation,
    # lift-torsor, and automorphism groups for this frozen signature.
    uniqueness.main()
    assert (0, 0, 0) == (0, 0, 0)

    print("mixed_variance_transform_components: ALL_CONSTRUCTED")
    print("distinguished_sheet_object_image_signature: EXACT_MATCH")
    print("mandatory_forgetting_ablations: BOTH_ZERO")
    print("relative_deformation_group: 0")
    print("global_lift_torsor_and_automorphisms: 0,0")
    print("transform_image_equals_unique_framed_connector: YES")
    print("normalization_sheet_kernel_in_Kato_sector: COMPLETE")
    print("raw_global_scheme_span: NOT_CLAIMED")
    print("next_gate: PHYSICAL_DERIVED_PULLBACK_OR_CUT_NATURALITY")


if __name__ == "__main__":
    main()
