use serde_json::json;

fn main() {
    // Exponents of (B34,B24,X) in the diagonal frames D_i.
    let d0 = [[0,0,0],[-2,0,0],[-2,-2,0],[-2,-2,-2],[0,-2,-2],[0,0,-2]];
    let d1 = [[-2,0,0],[-2,-2,0],[-2,-2,-2],[0,-2,-2],[0,0,-2],[0,0,0]];
    let d2 = [[0,0,0]];
    let relative = |frame: &[[i32;3]]| -> Vec<[i32;3]> {
        frame.iter().map(|e| [-e[0],-e[1],-e[2]]).collect()
    };
    let r0=relative(&d0); let r1=relative(&d1); let r2=relative(&d2);
    for residue in r0.iter().chain(&r1).chain(&r2) {
        assert!(residue.iter().all(|x| x % 2 == 0));
    }
    let packet=json!({
        "schema":"marici.benincasa.string_six_point_dual_relative_connection.v1",
        "convention":"dD + A_dual D - D A_primal = 0",
        "relative_connection":"A_dual-D*A_primal*D^-1 = -dD*D^-1",
        "logarithmic_coordinates":["dlog(B34)","dlog(B24)","dlog(X)"],
        "degree_zero_residues":r0,
        "degree_one_residues":r1,
        "degree_two_residues":r2,
        "curvature_zero":true,
        "all_residues_even_integral":true,
        "local_monodromy_identity":true,
        "new_support":false,
        "absolute_gauss_manin_connection_constructed":false,
        "conclusion":"The dual cellular frame change contributes only a flat diagonal logarithmic gauge with trivial monodromy; it cannot itself generate a connection-level extension class."
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-dual-relative-connection.json",&text).unwrap();
    print!("{text}");
}
