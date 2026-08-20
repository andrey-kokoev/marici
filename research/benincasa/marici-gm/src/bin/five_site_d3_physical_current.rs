use serde_json::json;
use std::fs;

fn main() {
    // For a labelled external basis matrix Q (columns q_i), H=Q^T Q.
    // u=Q^T ell, hence det(du/dell)^2=det(Q)^2=det(H).
    let packet=json!({
        "schema":"marici.benincasa.five_site.d3_physical_current.v1",
        "source_measure":"d^3 ell on physical loop momentum space",
        "labelled_coordinates":"u_i=ell dot q_i, i=1,2,3",
        "external_gram":"H=Q^T Q",
        "jacobian":"det(du/dell)=det(Q), with det(Q)^2=det(H)",
        "physical_current":"du1 wedge du2 wedge du3 / sqrt(det(H))",
        "coefficient_character":"rank-one external-Gram Kummer character det(H)^(-1/2)",
        "singular_support":"det(H)=0 only, plus separately retained source denominator/soft supports",
        "internal_radial_discriminant":"not a divisor of the constrained d=3 current; the full CM determinant vanishes on rank<=3 support",
        "entry_1212_endpoint_kummer":"belongs to the unrestricted d=5 coefficient continuation and has no ordinary d=3 pullback as a local system",
        "physical_activation_of_d5_endpoint_line":"not applicable rather than zero",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-d3-physical-current.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
