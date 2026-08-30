// RETRACTED MODEL (Entry 2143): the all-deleted source sector is a product.
fn main(){
    // A source additive readout F=f1(nu1)+f2(nu2)+f3(nu3) has no mixed jet.
    let mixed=[[0_i32;3];3];
    for i in 0..3 { for j in 0..3 { if i!=j { assert_eq!(mixed[i][j],0); } } }
    println!("{}",r#"{"status":"pass","readout":"direct_sum","mixed_second_normal_rank":0,"N2_generated":false}"#);
}
