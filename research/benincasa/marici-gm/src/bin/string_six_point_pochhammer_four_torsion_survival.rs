use serde_json::json;

fn mul(x: u8, y: u8) -> u8 {
    let mut p = 0u8;
    for i in 0..2 { if (y >> i) & 1 == 1 { p ^= x << i; } }
    if p & 8 != 0 { p ^= 0b1110; }
    if p & 4 != 0 { p ^= 0b0111; }
    p & 3
}

fn main() {
    let alpha = 0b10;
    let alpha_plus_one = 0b11;
    assert_eq!(mul(alpha, alpha_plus_one), 1);
    println!("{}", serde_json::to_string_pretty(&json!({
        "schema":"marici.string.pochhammer_four_torsion_survival.v1",
        "certificate_field":"F_4=F_2[alpha]/(alpha^2+alpha+1)",
        "specialization":"M -> alpha",
        "M_inverse":"alpha+1",
        "(M-1)_inverse":"alpha",
        "consequence":"F_2[M^{+-1},(M-1)^{-1}] is nonzero",
        "four_torsion_automatically_killed":false
    })).unwrap());
}
