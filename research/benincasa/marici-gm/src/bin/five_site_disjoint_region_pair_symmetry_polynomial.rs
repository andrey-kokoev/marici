use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn atom(s:&str)->Atom{Atom::parse(s,"marici",Default::default()).unwrap().expand()}
fn pdot(i:usize,j:usize)->Atom{
    let d=(i.max(j)-i.min(j)).min(5-(i.max(j)-i.min(j)));
    match d{0=>atom("2"),1=>atom("(3+sqrt(5))/4"),2=>atom("(3-sqrt(5))/4"),_=>unreachable!()}
}
fn dot(a:&[Atom;4],b:&[Atom;4])->Atom{
    let mut z=atom("0");for i in 0..4{for j in 0..4{z+=a[i].clone()*b[j].clone()*pdot(i,j);}}z.expand()
}
fn v(c:[&str;4])->[Atom;4]{c.map(atom)}

fn main(){
    // Fixed-axis parameter L(q)=M_14+q(M_23-M_14) for the labelled pair
    // (g_123,g_125), with cut pairs {2,4} and {1,3} in zero-based notation.
    let d=v(["0","1/2","0","-1/2"]);
    let a=v(["0","-1/2","1/2","1/2"]); // M_14-C_2
    let b=v(["0","-1/2","-1/2","-1/2"]); // M_14-C_4
    let q=atom("q");
    let d2=dot(&d,&d);let ad=dot(&a,&d);let bd=dot(&b,&d);let a2=dot(&a,&a);let b2=dot(&b,&b);
    let aa=(a2.clone()+atom("2")*q.clone()*ad.clone()+q.clone()*q.clone()*d2.clone()).expand();
    let bb=(b2.clone()+atom("2")*q.clone()*bd.clone()+q.clone()*q.clone()*d2.clone()).expand();
    let x=(ad.clone()+q.clone()*d2.clone()).expand();let y=(bd.clone()+q.clone()*d2.clone()).expand();
    let polynomial=(x.clone()*x.clone()*bb.clone()-y.clone()*y.clone()*aa.clone()).expand();
    let packet=json!({
        "schema":"marici.five_site_disjoint_region_pair_symmetry_polynomial.v1",
        "representative":["g_123","g_125"],
        "line":"L(q)=M_14+q(M_23-M_14)",
        "d2":d2.to_string(),"a_dot_d":ad.to_string(),"b_dot_d":bd.to_string(),
        "a2":a2.to_string(),"b2":b2.to_string(),"distance_a_squared":aa.to_string(),"distance_b_squared":bb.to_string(),
        "squared_stationarity_polynomial":polynomial.to_string(),
        "unsquared_sign_gate":"(a.d+q*d2)*(b.d+q*d2)<0",
        "status":"exact source-field polynomial; roots still require isolation and unsquared-sign certification"
    });
    fs::write("../results/five-site-disjoint-region-pair-symmetry-polynomial.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
