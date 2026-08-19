use serde_json::json;

fn main() {
    let edges = [
        ("123456--124356", "B34", true),
        ("123456--132456", "X", false),
        ("124356--142356", "B24", true),
        ("132456--134256", "B24", true),
        ("134256--143256", "B34", true),
        ("142356--143256", "X", false),
    ];
    // Entry 964's three unimodular pairs, indexed in the edge list above.
    let saturating_pairs = [[0usize, 1usize], [0, 3], [1, 3]];
    let active_pairs: Vec<_> = saturating_pairs
        .iter()
        .filter(|pair| edges[pair[0]].2 && edges[pair[1]].2)
        .copied()
        .collect();
    assert_eq!(active_pairs, vec![[0, 3]]);

    let source_fitting_monomials = [
        "A2", "A3", "A2*B24", "A3*B34", "Z*A2", "Z*A2*B24", "A3/Z", "A3*B34/Z",
    ];
    assert!(!source_fitting_monomials.contains(&"B24"));
    assert!(!source_fitting_monomials.contains(&"B34"));

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_loaded_transition_gate.v1",
        "branch_specialization":"X=1, equivalently s23=0",
        "edge_loadings":edges.iter().map(|(edge,u,active)|json!({
            "edge":edge,
            "half_monodromy":u,
            "loaded_boundary_factor":format!("{u}^2-1"),
            "generic_on_branch":active
        })).collect::<Vec<_>>(),
        "entry_964_saturating_pairs":saturating_pairs.iter().map(|p|[edges[p[0]].0,edges[p[1]].0]).collect::<Vec<_>>(),
        "unique_branch_active_saturating_pair":[edges[0].0,edges[3].0],
        "naive_augmented_determinant_factor":"(B34^2-1)*(B24^2-1)",
        "source_fitting_monomials":source_fitting_monomials,
        "B24_is_source_fitting_monomial":false,
        "B34_is_source_fitting_monomial":false,
        "classification":"branch specialization selects a unique carrier pair, but standalone loaded edge columns introduce unsupported B24 and B34 resonance divisors"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-loaded-transition-gate.json", &text).unwrap();
    print!("{text}");
}
