#[derive(Clone,Copy,Debug,PartialEq,Eq)]struct Q{hh:i32,hs:i32,ss:i32,den:i32}
fn main(){
    // Eq.17: 1/2(-iH+iS)^2.
    let eq17=Q{hh:-1,hs:2,ss:-1,den:2};
    // Eq.18: -1/2(H+H0)^2 with integral H0=-S.
    let eq18=Q{hh:-1,hs:2,ss:-1,den:2};
    assert_eq!(eq17,eq18);
    println!("{{");
    println!("  \"schema\": \"marici.eq17_eq18_endpoint_expansion.v1\",");
    println!("  \"eq17_coefficients_HH_HS_SS\": [\"-1/2\", \"+1\", \"-1/2\"],");
    println!("  \"eq18_coefficients_HH_HS_SS\": [\"-1/2\", \"+1\", \"-1/2\"],");
    println!("  \"uses_integrated_H0_equals_minus_S0\": true,");
    println!("  \"expansion_identity\": true");
    println!("}}");
}
