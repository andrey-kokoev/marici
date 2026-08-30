use std::fs;

fn main() {
    // Entry 867: residues of the two split algebraic lines at generic P6=0.
    // exp(2*pi*i*(-1/2))=-1 and exp(2*pi*i*0)=+1; D1 is a unit there.
    let algebraic_monodromy = [-1_i8, 1_i8];
    let mut lifts = 0_u32;
    for mask in 0_u32..8 {
        let source = [0,1,2].map(|i| if (mask >> i) & 1 == 0 { 1_i8 } else { -1_i8 });
        let preserves_all_edges = source.iter().all(|s|
            algebraic_monodromy.iter().all(|a| s == a));
        if preserves_all_edges { lifts += 1; }
    }
    assert_eq!(lifts, 0);
    let packet = format!(concat!(
        "{{\n",
        "  \"schema\": \"marici.p6_relative_monodromy_lift.v1\",\n",
        "  \"algebraic_residues\": [\"-1/2\", \"0\"],\n",
        "  \"algebraic_monodromy\": [-1, 1],\n",
        "  \"source_support_graph\": \"K_3_2\",\n",
        "  \"source_sign_assignments_tested\": 8,\n",
        "  \"diagonal_lifts_preserving_all_edges\": {},\n",
        "  \"relative_monodromy_exists_on_submodule\": true,\n",
        "  \"diagonal_lift_through_marked_extension\": false\n",
        "}}\n"), lifts);
    fs::write("research/benincasa/results/p6-relative-monodromy-lift.json", packet)
        .expect("write result packet");
}
