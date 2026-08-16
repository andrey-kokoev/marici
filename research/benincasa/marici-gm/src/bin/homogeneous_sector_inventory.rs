use std::{env, fs};

fn require_once(source: &str, needle: &str) {
    assert_eq!(
        source.matches(needle).count(),
        1,
        "source marker must occur exactly once: {needle}"
    );
}

fn main() {
    let source_path = env::args().nth(1).expect("primary-source path");
    let source = fs::read_to_string(source_path).expect("read primary source");

    require_once(&source, "the integral family has $15$ master integrals");
    require_once(
        &source,
        "sub-sector without denominators contains $\\nu_3^{\\mbox{\\tiny{(CI)}}}=7$ master integrals",
    );
    require_once(
        &source,
        "sub-sector containing only the denominator $\\q_{\\mathcal{G}_{12}}$, has $9$ master integrals",
    );
    require_once(
        &source,
        "In the generic case of multiple external legs, in which $x_i\\neq P_i$, the basis of this sector increases to $34$",
    );

    let zero_rank = 3_i32.pow(3) - 2_i32.pow(2) * (2 + 3);
    let elliptic_blocks = [1, 2, 2, 4];
    assert_eq!(zero_rank, 7);
    assert_eq!(elliptic_blocks.iter().sum::<i32>(), 9);

    let triangle_start = source
        .find("\\begin{equation}\\label{eq:Triangle}")
        .expect("triangle integrand");
    let triangle_tail = &source[triangle_start..];
    let triangle_end = triangle_tail
        .find("\\end{equation}")
        .expect("triangle integrand end");
    let triangle = &triangle_tail[..triangle_end];
    for denominator in [
        "\\q_{\\mathcal{G}_{12}}",
        "\\q_{\\mathcal{G}_{23}}",
        "\\q_{\\mathcal{G}_{31}}",
        "\\q_{\\mathfrak{g}_{12}}",
        "\\q_{\\mathfrak{g}_{23}}",
        "\\q_{\\mathfrak{g}_{31}}",
    ] {
        assert!(triangle.contains(denominator));
    }

    // The primary source counts the 15-master polylogarithmic family and the
    // q_G12-only 9-master subsector, but gives no rank statement for the
    // q_Gij plus two lower-pole top sectors appearing in eq:Triangle.
    let top_sector_rank_markers = [
        "q_{\\mathcal{G}_{12}} plus two-pole sector has",
        "q_{\\mathcal{G}_{23}} plus two-pole sector has",
        "q_{\\mathcal{G}_{31}} plus two-pole sector has",
    ];
    assert!(top_sector_rank_markers
        .iter()
        .all(|marker| !source.contains(marker)));

    println!(
        r#"{{
  "schema": "marici.homogeneous-sector-inventory.v1",
  "source_homogeneous_polylog_family_rank": 15,
  "source_zero_subsector_rank": 7,
  "source_q_G12_only_subsector_rank": 9,
  "source_q_only_block_ranks": [1, 2, 2, 4],
  "source_generic_multi_external_lower_rank": 34,
  "rank_34_is_homogeneous": false,
  "physical_integrand_cyclic_q_sectors": 3,
  "physical_integrand_terms_per_q_sector": 2,
  "q_plus_two_pole_top_sector_rank_published": false,
  "q_plus_two_pole_top_sector_basis_published": false,
  "cross_family_transition_maps_published": false,
  "naive_15_plus_3_times_9_global_rank_authorized": false,
  "missing_source_data": [
    "master counts and bases for each q_Gij plus two-lower-pole top sector",
    "Gauss-Manin extensions from those top sectors to the q-only and lower subsectors",
    "transition maps among cyclic partial-fraction families"
  ],
  "carrier_falsified": false,
  "global_decomposition_status": "not_yet_defined_from_complete_source_modules"
}}"#
    );
}
