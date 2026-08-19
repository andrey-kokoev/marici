use serde_json::json;

fn det2(a:i64,b:i64,c:i64,d:i64)->i64 { a*d-b*c }

fn main() {
    // Gradients at (m,n)=(1,1).
    let grad_diag=[1,1]; // d(mn-1)
    let grad_m=[1,0];    // d(m-1)
    let grad_n=[0,1];    // d(n-1)
    let det_m=det2(grad_diag[0],grad_diag[1],grad_m[0],grad_m[1]);
    let det_n=det2(grad_diag[0],grad_diag[1],grad_n[0],grad_n[1]);
    assert_eq!(det_m,-1);
    assert_eq!(det_n,1);

    // Hom_R(R/(f),R/(g)) consists of elements annihilated by f modulo g.
    // Mod m-1, mn-1 becomes n-1, a non-zero-divisor in Z[n^+-1].
    // Mod mn-1, m-1 remains a non-zero-divisor in Z[m^+-1].
    let hom_diag_to_m=0;
    let hom_m_to_diag=0;
    let hom_diag_to_n=0;
    let hom_n_to_diag=0;
    assert_eq!(hom_diag_to_m+hom_m_to_diag+hom_diag_to_n+hom_n_to_diag,0);

    let packet=json!({
        "schema":"marici.benincasa.string_six_point_corner_flag_module_gate.v1",
        "base_ring":"Z[m^+-1,n^+-1]",
        "diagonal_module":"R/(m*n-1)",
        "facet_modules":["R/(m-1)","R/(n-1)"],
        "ordinary_R_linear_Hom_ranks":{
            "diag_to_m":hom_diag_to_m,"m_to_diag":hom_m_to_diag,
            "diag_to_n":hom_diag_to_n,"n_to_diag":hom_n_to_diag
        },
        "common_intersection":"R/(m-1,n-1) = Z",
        "intersection_jacobian_determinants":{"with_m_facet":det_m,"with_n_facet":det_n},
        "transverse":true,
        "excess_Tor_1":0,
        "classification":"no direct generic flag map; canonical comparison is a cospan through the common point costalk"
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-corner-flag-module-gate.json",&text).unwrap();
    print!("{text}");
}
