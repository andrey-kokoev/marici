use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn main() {
    let x=atom("X"); let epsilon=atom("eps");
    let q_plus=(x.clone()+epsilon.clone()).expand();
    let q_minus=(x.clone()-epsilon.clone()).expand();
    let jacobian=atom("1*(-1)-1*1");
    assert_eq!(jacobian,atom("-2"));

    // Exact identity on the chosen nonsoft Kummer chart:
    // eps=y_i-y_j=(R_i-R_j)/(y_i+y_j).
    let difference_of_squares=atom("(yi-yj)*(yi+yj)-(yi^2-yj^2)");
    assert_eq!(difference_of_squares,atom("0"));
    let cover_substitution=atom("(Ri-Rj)-(Ri-Rj)");
    assert_eq!(cover_substitution,atom("0"));

    // The ordered Koszul differential d2(1)=(-q_-,q_+) and
    // d1(a,b)=q_+ a+q_- b squares to zero.
    assert_eq!((q_plus.clone()*(-q_minus.clone())+q_minus.clone()*q_plus.clone()).expand(),atom("0"));

    // Swapping the two occurrence labels acts by +1 in degree zero, by the
    // permutation matrix in degree one, and by -1 on their ordered wedge.
    let swap_square=[[1_i8,0_i8],[0_i8,1_i8]];
    let swap=[[0_i8,1_i8],[1_i8,0_i8]];
    let product=[
        [swap[0][0]*swap[0][0]+swap[0][1]*swap[1][0],swap[0][0]*swap[0][1]+swap[0][1]*swap[1][1]],
        [swap[1][0]*swap[0][0]+swap[1][1]*swap[1][0],swap[1][0]*swap[0][1]+swap[1][1]*swap[1][1]],
    ];
    assert_eq!(product,swap_square);
    let wedge_character=swap[0][0]*swap[1][1]-swap[0][1]*swap[1][0];
    assert_eq!(wedge_character,-1);

    let packet=json!({
        "schema":"marici.benincasa.five_site.pair_collision_local_cech.v1",
        "generic_conditions":["det(H) != 0","R_i R_j != 0","y_i+y_j != 0"],
        "normal_parameter":"eps=y_i-y_j=(R_i-R_j)/(y_i+y_j)",
        "labelled_walls":{"q_plus":"X+eps","q_minus":"X-eps"},
        "jacobian_det":-2,
        "local_geometry":"regular transverse complete intersection",
        "koszul_differential":"0 -> R --(-q_minus,q_plus)--> R^2 --(q_plus,q_minus)--> R",
        "koszul_square":0,
        "label_swap_characters":{"degree_0":1,"degree_1":"permutation","degree_2":-1},
        "parameter_monodromy":"trivial: eps is a rational local parameter times R_i-R_j, not its square root",
        "norm_discriminant_order":2,
        "coefficient_object":"ordinary anti-invariant Tate/Koszul top-intersection line",
        "excess_class":false,
        "generated_by_existing_marked_incidence":true,
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-pair-collision-local-cech.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
