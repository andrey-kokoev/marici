use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn atom(text:&str)->Atom{Atom::parse(text,"marici",Default::default()).unwrap().expand()}

fn determinant(matrix:&[Vec<Atom>])->Atom{
    if matrix.len()==1{return matrix[0][0].clone();}
    let mut total=atom("0");
    for column in 0..matrix.len(){
        let minor=(1..matrix.len()).map(|row|(0..matrix.len()).filter(|c|*c!=column).map(|c|matrix[row][c].clone()).collect()).collect::<Vec<Vec<Atom>>>();
        let sign=if column%2==0{atom("1")}else{atom("-1")};
        total+=sign*matrix[0][column].clone()*determinant(&minor);
    }
    total.expand()
}

fn dot(i:usize,j:usize)->Atom{
    let difference=(i.max(j)-i.min(j)).min(5-(i.max(j)-i.min(j)));
    match difference{
        0=>atom("2"),
        1=>atom("(3+sqrt(5))/4"),
        2=>atom("(3-sqrt(5))/4"),
        _=>unreachable!()
    }
}

fn main(){
    let point_gram=(0..5).map(|i|(0..5).map(|j|dot(i,j)).collect()).collect::<Vec<Vec<Atom>>>();
    let det5=determinant(&point_gram).expand();
    assert_eq!(det5,atom("0"));
    let mut total_resultant_squared=atom("0");
    for row in &point_gram{for entry in row{total_resultant_squared+=entry.clone();}}
    total_resultant_squared=total_resultant_squared.expand();
    assert_eq!(total_resultant_squared,atom("25"));

    // q1=P1, q2=P1+P2, q3=P1+P2+P3.
    let routing=[vec![1_i32],vec![1,2],vec![1,2,3]];
    let h=(0..3).map(|i|(0..3).map(|j|{
        let mut value=atom("0");
        for left in &routing[i]{for right in &routing[j]{value+=dot(*left as usize,*right as usize);}}
        value.expand()
    }).collect()).collect::<Vec<Vec<Atom>>>();
    let det_h=determinant(&h).factor();
    assert_ne!(det_h,atom("0"));

    let packet=json!({
        "schema":"marici.benincasa.five_site.cyclic_slice_correction.v2",
        "spatial_resultants":"P_k=(cos(2*pi*k/5),sin(2*pi*k/5),1), k=0,...,4",
        "point_dot_products":{"same":"2","cyclic_distance_1":"(3+sqrt(5))/4","cyclic_distance_2":"(3-sqrt(5))/4"},
        "point_gram_rank":3,
        "five_by_five_gram_determinant":det5.to_string(),
        "total_resultant_squared":total_resultant_squared.to_string(),
        "momentum_conservation":"fails: sum_i P_i=(0,0,5), with squared norm 25",
        "routing_basis":["q1=P1","q2=P1+P2","q3=P1+P2+P3"],
        "routing_gram":h.iter().map(|row|row.iter().map(|entry|entry.to_string()).collect::<Vec<_>>()).collect::<Vec<_>>(),
        "routing_gram_determinant":det_h.to_string(),
        "site_energies":"X_1=...=X_5=t",
        "physical_real_domain":"none: global momentum conservation fails",
        "complex_parameter":"t",
        "total_energy":"E_T=5t",
        "soft_support":"excluded at generic t and nonzero P_k",
        "cyclic_symmetry":"exact C5 only as an algebraic Gram family",
        "classification":"nonphysical algebraic slice; downstream Landau calculations require this retyping",
        "no_go":"in real d=3 an exact C5 orbit is 1+2 dimensional; conservation kills the invariant line, so a conserved orbit has Gram rank at most 2",
        "frozen_before_period_evaluation":true
    });
    fs::write("../results/five-site-cyclic-physical-slice.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
