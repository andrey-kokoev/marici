use serde_json::json;

fn main() {
    // If (M-1)f(M)=1 in Z[M^{+-1}], evaluation at M=1 would give 0=1.
    // Hence M-1 is not a Laurent unit and the source coefficient 1/(M-1)
    // exists only after localization.
    let lhs_at_m_one = (1_i64 - 1) * 37; // arbitrary putative finite value f(1)
    let rhs_at_m_one = 1_i64;
    assert_ne!(lhs_at_m_one, rhs_at_m_one);
    println!("{}", serde_json::to_string_pretty(&json!({
        "schema":"marici.string.pochhammer_integral_type_gate.v1",
        "source_formula":"reg(0,1)=S_0/(M_0-1)+interval-S_1/(M_1-1)",
        "base_ring":"Z[M_F^{+-1}]",
        "localization":"Z[M_F^{+-1},(M_F-1)^{-1}]",
        "nonunit_certificate":"evaluation at M_F=1 sends (M_F-1)f to 0, never 1",
        "integral_saturation_map_supplied":false,
        "conclusion":"Pochhammer regularization cannot canonically resolve the Z/4 component defect over the unlocalized integral group ring"
    })).unwrap());
}
