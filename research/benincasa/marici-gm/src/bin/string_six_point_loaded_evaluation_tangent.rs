use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s:&str)->Atom { Atom::parse(s,"marici",Default::default()).unwrap() }
fn clean(x:Atom)->Atom { x.together().cancel().factor() }
fn read(path:&str)->Value { serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap() }
fn deriv(x:&Atom)->Atom { clean(x.derivative(symbol!("marici::B34"))) }

fn main(){
    let cp=read("../string-six-point-loaded-corner-comparison.json");
    let lp=read("../string-six-point-circuit-exceptional-cochain.json");
    let c:Vec<Vec<Atom>>=cp["matrix"].as_array().unwrap().iter().map(|row|
        row.as_array().unwrap().iter().map(|x|a(x.as_str().unwrap())).collect()).collect();
    let lambda:Vec<Atom>=lp["cochain"].as_array().unwrap().iter().map(|x|a(x.as_str().unwrap())).collect();
    let mut r=vec![a("0");6];
    for j in 0..6 { for i in 0..6 { r[j]+=lambda[i].clone()*c[i][j].clone(); } r[j]=clean(r[j].clone()); }
    let dl:Vec<Atom>=lambda.iter().map(deriv).collect();
    let dc:Vec<Vec<Atom>>=c.iter().map(|row|row.iter().map(deriv).collect()).collect();
    let dr:Vec<Atom>=r.iter().map(deriv).collect();
    let mut rhs=vec![a("0");6];
    for j in 0..6 { for i in 0..6 { rhs[j]+=dl[i].clone()*c[i][j].clone()+lambda[i].clone()*dc[i][j].clone(); } rhs[j]=clean(rhs[j].clone()); }
    assert_eq!(rhs,dr);
    let derivative_support:Vec<Vec<usize>>=(0..6).map(|j|(0..6).filter(|&i|dc[i][j]!=a("0")).collect()).collect();
    let original_support:Vec<Vec<usize>>=(0..6).map(|j|(0..6).filter(|&i|c[i][j]!=a("0")).collect()).collect();
    for j in 0..6 { assert!(derivative_support[j].iter().all(|i|original_support[j].contains(i))); }
    let nonzero_derivative_columns:Vec<usize>=(0..6).filter(|&j|!derivative_support[j].is_empty()).collect();
    assert_eq!(nonzero_derivative_columns,vec![4,5]);
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_loaded_evaluation_tangent.v1",
      "direction":"B34*d/dB34 (overall Euler factor omitted from support identity)",
      "identity":"lambda*C=r",
      "tangent_identity":"lambda'*C+lambda*C'=r'",
      "exact_product_rule_verified":true,
      "original_column_support":original_support,
      "derivative_column_support":derivative_support,
      "nonzero_derivative_columns":nonzero_derivative_columns,
      "support_preserved":true,
      "new_incidence":false,
      "physical_log_insertion_reduced":false,
      "conclusion":"The formal B34 tangent of the exact loaded evaluation closes through the existing circuit incidence and creates no new support. This is an algebraic control, not the physical logarithmic-insertion Gauss-Manin reduction."
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-loaded-evaluation-tangent.json",&text).unwrap();
    print!("{text}");
}
