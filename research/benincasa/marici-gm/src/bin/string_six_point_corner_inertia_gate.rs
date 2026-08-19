use serde_json::json;

fn main() {
    // Work in Z[m,n].  Coefficient vectors are ordered [1,m,n,mn].
    let diagonal=[-1,0,0,1];              // mn-1
    let iterated=[1,-1,-1,1];             // (m-1)(n-1)
    assert_ne!(diagonal,iterated);

    // Neither polynomial divides the other: both have total degree at most
    // two, so divisibility would force a constant multiple, excluded above.
    let constant_multiple=false;

    // Exact witness on the diagonal-inertia divisor away from either facet.
    // m=2,n=1/2: mn-1=0, while (m-1)(n-1)=-1/2.
    let witness=json!({
        "m":"2",
        "n":"1/2",
        "m_minus_1":"1",
        "n_minus_1":"-1/2",
        "mn_minus_1":"0",
        "iterated_boundary_coefficient":"-1/2"
    });
    let factors=[
        ("Z*A2","12|35",1),
        ("Z*A2*B24","124|35",2),
        ("A3/Z","13|25",1),
        ("A3*B34/Z","134|25",2),
    ];
    let packet=json!({
        "schema":"marici.benincasa.string_six_point_corner_inertia_gate.v1",
        "normal_torus":"G_m^2 with facet monodromies (m,n)",
        "ordinary_iterated_boundary":"(m-1)(n-1)",
        "observed_composite_resonance":"m*n-1",
        "constant_multiple":constant_multiple,
        "same_support":false,
        "generic_diagonal_inertia_witness":witness,
        "composite_factors":factors.iter().map(|(factor,corner,count)|json!({"factor":factor,"corner":corner,"occurrences":count})).collect::<Vec<_>>(),
        "classification":"existing two-normal carrier corner plus diagonal coefficient inertia; not ordinary iterated-boundary support",
        "exceptional_divisor_requires_predeclared_log_blowup":true
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-corner-inertia-gate.json",&text).unwrap();
    print!("{text}");
}
