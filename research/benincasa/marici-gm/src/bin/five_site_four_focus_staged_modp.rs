use serde_json::{json,Value};
use std::{fs,sync::Arc};
use symbolica::prelude::*;

fn sqrt_mod(value:u32,p:u32)->Vec<u32>{(0..p).filter(|x|((*x as u64)*(*x as u64)%p as u64) as u32==value%p).collect()}
fn resultant_var(mut left:MultivariatePolynomial<Zp,u16>,mut right:MultivariatePolynomial<Zp,u16>,var:Symbol)->MultivariatePolynomial<Zp,u16>{
    left.unify_variables(&mut right);
    let index=left.get_vars_ref().iter().position(|x|*x==PolyVariable::Symbol(var)).unwrap();
    left.to_univariate(index).resultant_prs(&right.to_univariate(index))
}
fn main(){
    let prime=std::env::var("MARICI_PRIME").ok().and_then(|x|x.parse().ok()).unwrap_or(1009u32);
    let index=std::env::var("MARICI_REP_INDEX").ok().and_then(|x|x.parse().ok()).unwrap_or(0usize);
    let roots=sqrt_mod(5,prime); assert_eq!(roots.len(),2);
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-site-connected-pair-four-focus-system.json").unwrap()).unwrap();
    let record=&source["records"].as_array().unwrap()[index];
    let mut root_packets=Vec::new();
    for z_value in roots {
        let field=Zp::new(prime);
        let order=Arc::new(vec![PolyVariable::Symbol(symbol!("b")),PolyVariable::Symbol(symbol!("c")),PolyVariable::Symbol(symbol!("t"))]);
        let parse_poly=|text:&str|->MultivariatePolynomial<Zp,u16>{
            let specialized=text.replace("z",&z_value.to_string());
            Atom::parse(&specialized,"marici",Default::default()).unwrap().expand().to_polynomial(&field,Some(order.clone()))
        };
        let existence=parse_poly(record["realization_equation"].as_str().unwrap());
        let minors=record["collinearity_minors"].as_array().unwrap().iter().map(|x|parse_poly(x.as_str().unwrap())).collect::<Vec<_>>();
        let first=minors.iter().map(|minor|resultant_var(existence.clone(),minor.clone(),symbol!("b"))).collect::<Vec<_>>();
        let mut second=Vec::new();
        for (i,j) in [(0usize,1usize),(0,2),(1,2)] {
            let candidate=resultant_var(first[i].clone(),first[j].clone(),symbol!("c"));
            second.push(json!({"pair":[i,j],"candidate":candidate.to_string(),"factorization":candidate.factor().into_iter().map(|(f,e)|json!({"factor":f.to_string(),"power":e})).collect::<Vec<_>>() }));
        }
        root_packets.push(json!({"z_value":z_value,"first_resultants":first.iter().map(ToString::to_string).collect::<Vec<_>>(),"second_resultants":second}));
    }
    let packet=json!({"schema":"marici.benincasa.five_site.four_focus_staged_modp.v1","prime":prime,"representative_index":index,"representative":record["representative"],"root_packets":root_packets,"scope":"candidate superset from staged pairwise elimination; full-ideal certification remains"});
    fs::write("../results/five-site-four-focus-staged-modp.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("wrote five-site-four-focus-staged-modp.json");
}
