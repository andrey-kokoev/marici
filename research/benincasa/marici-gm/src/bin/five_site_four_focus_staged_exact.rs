use serde_json::{json,Value};
use std::{fs,sync::Arc};
use symbolica::prelude::*;

fn resultant_var(mut left:MultivariatePolynomial<Q,u16>,mut right:MultivariatePolynomial<Q,u16>,var:Symbol)->MultivariatePolynomial<Q,u16>{
    left.unify_variables(&mut right);
    let index=left.get_vars_ref().iter().position(|x|*x==PolyVariable::Symbol(var)).unwrap();
    left.to_univariate(index).resultant_prs(&right.to_univariate(index))
}
fn main(){
    let index=std::env::var("MARICI_REP_INDEX").ok().and_then(|x|x.parse().ok()).unwrap_or(0usize);
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-site-connected-pair-four-focus-system.json").unwrap()).unwrap();
    let record=&source["records"].as_array().unwrap()[index];
    let order=Arc::new(vec![PolyVariable::Symbol(symbol!("b")),PolyVariable::Symbol(symbol!("c")),PolyVariable::Symbol(symbol!("z")),PolyVariable::Symbol(symbol!("t"))]);
    let parse_poly=|text:&str|->MultivariatePolynomial<Q,u16>{Atom::parse(text,"marici",Default::default()).unwrap().expand().to_polynomial(&Q,Some(order.clone()))};
    let existence=parse_poly(record["realization_equation"].as_str().unwrap());
    let minors=record["collinearity_minors"].as_array().unwrap().iter().map(|x|parse_poly(x.as_str().unwrap())).collect::<Vec<_>>();
    let first=minors.iter().map(|minor|resultant_var(existence.clone(),minor.clone(),symbol!("b"))).collect::<Vec<_>>();
    let second=[(0usize,1usize),(0,2),(1,2)].into_iter().map(|(i,j)|{
        let candidate=resultant_var(first[i].clone(),first[j].clone(),symbol!("c"));
        json!({"pair":[i,j],"candidate":candidate.to_string()})
    }).collect::<Vec<_>>();
    let packet=json!({"schema":"marici.benincasa.five_site.four_focus_staged_exact.v1","representative_index":index,"representative":record["representative"],"first_resultants":first.iter().map(ToString::to_string).collect::<Vec<_>>(),"second_resultants":second,"scope":"exact staged necessary-condition elimination over Q(z,t)"});
    fs::write("../results/five-site-four-focus-staged-exact.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("wrote five-site-four-focus-staged-exact.json");
}
