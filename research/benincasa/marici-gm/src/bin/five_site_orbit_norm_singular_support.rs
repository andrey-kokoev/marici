use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn atom(text:&str)->Atom{Atom::parse(text,"marici",Default::default()).unwrap().expand()}

fn main(){
    let n1=atom("X^2-4*R");
    let n1_dx=n1.derivative(atom("X").get_symbol().unwrap()).expand();
    let n1_dr=n1.derivative(atom("R").get_symbol().unwrap()).expand();
    assert_eq!(n1_dx,atom("2*X"));
    assert_eq!(n1_dr,atom("-4"));

    let n2=atom("X^4-2*(R+S)*X^2+(R-S)^2");
    let dx=n2.derivative(atom("X").get_symbol().unwrap()).expand();
    let dr=n2.derivative(atom("R").get_symbol().unwrap()).expand();
    let ds=n2.derivative(atom("S").get_symbol().unwrap()).expand();
    assert_eq!(dx,atom("4*X*(X^2-R-S)"));
    assert_eq!((dr.clone()+ds.clone()).expand(),atom("-4*X^2"));
    assert_eq!((dr.clone()-ds.clone()).expand(),atom("4*(R-S)"));
    assert_eq!(n2.replace(atom("X")).with(atom("0")).replace(atom("R")).with(atom("S")).expand(),atom("0"));

    let packet=json!({
        "schema":"marici.benincasa.five_site.orbit_norm_singular_support.v1",
        "one_cut_norm":"X^2-4R",
        "one_cut_total_divisor":"smooth because partial_R N=-4",
        "two_cut_norm":"X^4-2(R+S)X^2+(R-S)^2",
        "two_cut_derivatives":{"partial_X":dx.to_string(),"partial_R":dr.to_string(),"partial_S":ds.to_string()},
        "jacobian_generators":{"partial_R_plus_partial_S":"-4X^2","partial_R_minus_partial_S":"4(R-S)"},
        "reduced_singular_locus":"X=0 and R=S",
        "physical_reduced_singular_locus":"X_A=0 and F_i=F_j, away from det(H)=0",
        "projection_discriminant":"R_i R_j (R_i-R_j)=0 describes ramified/nonreduced fibers of the orbit polynomial, not by itself singular support of its total divisor",
        "typing_correction":"Higher Cech overlaps require the corresponding signed-energy walls X_A=0 in addition to root-equality conditions.",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-orbit-norm-singular-support.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
