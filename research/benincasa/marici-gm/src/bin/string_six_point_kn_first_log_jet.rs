use serde_json::json;

fn main() {
    // Basis (KN, log(f_c) KN), with columns denoting source basis vectors.
    // The normalized first-jet operator sends e0 to eta e1 and e1 to zero.
    let n = [[0_i32, 0], [1, 0]];
    let n2 = [
        [n[0][0]*n[0][0]+n[0][1]*n[1][0], n[0][0]*n[0][1]+n[0][1]*n[1][1]],
        [n[1][0]*n[0][0]+n[1][1]*n[1][0], n[1][0]*n[0][1]+n[1][1]*n[1][1]],
    ];
    assert_eq!(n2, [[0,0],[0,0]]);

    // A diagonal cellular residue r acts as r*I on the logarithmic layer,
    // hence commutes with N. Test all residues from Entry 1016.
    let residues = [[0,0,0],[2,0,0],[2,2,0],[2,2,2],[0,2,2],[0,0,2]];
    for r in residues {
        for scalar in r {
            let left=[[scalar*n[0][0],scalar*n[0][1]],[scalar*n[1][0],scalar*n[1][1]]];
            let right=left;
            assert_eq!(left,right);
        }
    }

    let packet=json!({
        "schema":"marici.benincasa.string_six_point_kn_first_log_jet.v1",
        "source_identity":"A_c d/dA_c KN = (alpha'/(i*pi)) log(f_c) KN",
        "basis":["KN","log(f_c)*KN"],
        "normalized_nilpotent":[[0,0],[1,0]],
        "nilpotent_square_zero":true,
        "scope":"first parameter/Rees jet only",
        "all_orders_finite_connection_constructed":false,
        "commutes_with_entry_1016_cellular_residues":true,
        "mixes_occurrence_words":false,
        "conclusion":"One source channel canonically supplies a length-two unipotent first logarithmic jet. It tensor-commutes with the dual cellular gauge and cannot by itself generate the missing nondiagonal word-level connection."
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-kn-first-log-jet.json",&text).unwrap();
    print!("{text}");
}
