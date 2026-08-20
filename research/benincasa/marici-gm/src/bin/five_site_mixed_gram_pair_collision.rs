use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn atom(text:&str)->Atom{Atom::parse(text,"marici",Default::default()).unwrap().expand()}

fn main(){
    let lambda=atom("lam"); let x=atom("X"); let epsilon=atom("eps");
    let q_plus=(lambda.clone()*x.clone()+epsilon.clone()).expand();
    let q_minus=(lambda.clone()*x.clone()-epsilon.clone()).expand();

    assert_eq!((q_plus.clone()-q_minus.clone()).expand(),atom("2*eps"));
    assert_eq!((q_plus.clone()+q_minus.clone()).expand(),atom("2*lam*X"));
    let jacobian=(x.clone()*atom("-1")-x.clone()*atom("1")).expand();
    assert_eq!(jacobian,atom("-2*X"));
    assert_eq!((q_plus.clone()*(-q_minus.clone())+q_minus.clone()*q_plus.clone()).expand(),atom("0"));

    // Gram deck: lam -> -lam and every Y_k=lam*y_k -> -Y_k, hence
    // eps=Y_i-Y_j -> -eps. Each strict transform changes by the unit -1.
    let deck_q_plus=(-lambda.clone()*x.clone()-epsilon.clone()).expand();
    let deck_q_minus=(-lambda.clone()*x.clone()+epsilon.clone()).expand();
    assert_eq!(deck_q_plus,(-q_plus.clone()).expand());
    assert_eq!(deck_q_minus,(-q_minus.clone()).expand());

    let packet=json!({
        "schema":"marici.benincasa.five_site.mixed_gram_pair_collision.v1",
        "weighted_base_change":"det(H)=lam^2, Y_k=lam*y_k, so Y_k^2=F_k",
        "generic_pair_collision":"F_i=F_j with Y_i+Y_j a unit",
        "normal_parameter":"eps=Y_i-Y_j=(F_i-F_j)/(Y_i+Y_j)",
        "strict_transform_walls":{"q_plus":"lam*X+eps","q_minus":"lam*X-eps"},
        "generated_ideal":"(eps,lam*X)",
        "jacobian_det_in_lam_eps":"-2X",
        "generic_X_nonzero":"transverse labelled complete intersection",
        "X_zero_restriction":"the first separation symbol lam*X vanishes; derived restriction has the canonical rank-one conormal/Koszul Tor",
        "koszul_square":0,
        "gram_deck_action":"(lam,Y_i,Y_j)->(-lam,-Y_i,-Y_j); each q_plus/q_minus changes by the unit -1",
        "divisor_inertia":"trivial on dlog(q_plus),dlog(q_minus); external Gram Kummer character remains separate",
        "classification":"weighted Gram nearby cycle plus existing marked incidence and signed-energy conormal support",
        "coefficient_excess":false,
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-mixed-gram-pair-collision.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
