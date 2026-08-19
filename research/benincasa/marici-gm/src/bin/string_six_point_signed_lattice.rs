use serde_json::json;

fn det2(a: [[i64; 2]; 2]) -> i64 {
    a[0][0] * a[1][1] - a[0][1] * a[1][0]
}

fn main() {
    // Columns are the source-derived diagonal and off-diagonal target
    // directions in the fixed labelled target basis.
    let x_plus = [[1, 0], [-1, 1]];
    let x_minus = [[1, 0], [1, 1]];
    assert_eq!(det2(x_plus), 1);
    assert_eq!(det2(x_minus), 1);

    // B_minus = B_plus * shear.  This is an integral, unimodular sheet
    // transition; no denominator clearing enters its construction.
    let sheet_shear = [[1, 0], [2, 1]];
    assert_eq!(det2(sheet_shear), 1);
    for i in 0..2 {
        for j in 0..2 {
            let value = x_plus[i][0] * sheet_shear[0][j]
                + x_plus[i][1] * sheet_shear[1][j];
            assert_eq!(value, x_minus[i][j]);
        }
    }

    let packet = json!({
        "schema": "marici.benincasa.string_six_point_signed_lattice.v1",
        "fixed_target_basis": ["e_1", "e_2"],
        "x_plus_branch_columns": [[1,0],[-1,1]],
        "x_minus_branch_columns": [[1,0],[1,1]],
        "x_plus_determinant": det2(x_plus),
        "x_minus_determinant": det2(x_minus),
        "sheet_transition": [[1,0],[2,1]],
        "sheet_transition_determinant": det2(sheet_shear),
        "target_lattice_status": "source-derived unimodular saturation",
        "source_lattice_status": "not yet saturated over the Laurent coefficient ring",
        "betti_integral_lattice_status": "not established",
        "prohibited_inference": "rational rank twelve does not by itself prove an integral Betti lattice"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-signed-lattice.json", &text).unwrap();
    print!("{text}");
}
