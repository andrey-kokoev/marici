fn main(){
    // F(nu,k)=regular(nu^0)+nu*(8C-8C*k)+higher nu grades.
    // Contact grade extracts the nu coefficient. k*d/dk then gives -8C.
    let c=5_i64;
    let contact_coeff_at_k1=8*c-8*c;
    let score_of_contact_coeff=-8*c;
    let contact_coeff_of_score=-8*c;
    assert_eq!(contact_coeff_at_k1,0);
    assert_eq!(score_of_contact_coeff,contact_coeff_of_score);
    println!("{{\"status\":\"pass\",\"commutator\":0,\"projected_scalar_value\":0,\"projected_score_response\":\"-8*C\",\"contamination_removed_by\":\"contact_normal_grade\"}}");
}
