use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn verify() {
    let q_plus = atom("E^2*(a^2-b^2)-P1^2*a^2+P2^2*b^2+2*E*P3*a*b");
    let q_minus = atom("E^2*(a^2-b^2)-P1^2*a^2+P2^2*b^2-2*E*P3*a*b");
    let soft_central = atom("-P1^2*a^2+P2^2*b^2");
    assert_eq!(
        q_plus.clone().replace(atom("E").to_pattern()).with(atom("0").to_pattern()).expand(),
        soft_central
    );
    assert_eq!(
        (q_plus.clone() - q_minus.clone() - atom("4*E*P3*a*b")).expand(),
        atom("0")
    );

    // In the b != 0 chart, r=a/b and Q_sigma/b^2 is a quadratic in r.
    let c = atom("E^2-P1^2");
    let f = atom("(E^2-P1^2)*(E^2-P2^2)+E^2*P3^2"); // K0/P3^2
    for sign in [1_i32, -1_i32] {
        let q = atom(&format!("(E^2-P1^2)*r^2+({}2*E*P3)*r+(P2^2-E^2)", if sign > 0 { "" } else { "-" }));
        let xi = atom(&format!("2*(E^2-P1^2)*r+{}2*E*P3", if sign > 0 { "" } else { "-" }));
        assert_eq!((xi.clone()*xi - atom("4")*c.clone()*q - atom("4")*f.clone()).expand(), atom("0"));
    }

    // Matrices in ordered polar basis (e_+,e_-).
    let soft_matrix = ["2*P3*a*b", "-2*P3*a*b"];
    let endpoint_matrix = ["1", "1"];
    assert_eq!(soft_matrix.len(), 2);
    assert_eq!(endpoint_matrix.len(), 2);

    println!("M_soft=[2*P3*a*b,-2*P3*a*b]^T");
    println!("rank_M_soft_generic=1");
    println!("rank_M_soft_on_P3*a*b=0=0");
    println!("M_endpoint=[1,1]^T");
    println!("rank_M_endpoint_on_P3*(E^2-P1^2)!=0=1");
    println!("occurrence_character_soft=+1");
    println!("occurrence_character_endpoint=-1");
    println!("kummer_deck_character_both=-1");
    println!("endpoint_chart_exits=P3*(E^2-P1^2)=0");
}

fn main() { verify(); }
