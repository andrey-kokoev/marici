use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn atom(text:&str)->Atom{Atom::parse(text,"marici",Default::default()).unwrap().expand()}
fn dot(i:usize,j:usize)->Atom{
    let raw=i.max(j)-i.min(j);let difference=raw.min(5-raw);
    match difference{0=>atom("2"),1=>atom("(3+sqrt(5))/4"),2=>atom("(3-sqrt(5))/4"),_=>unreachable!()}
}
fn subset_norm_squared(start:usize,size:usize)->Atom{
    let indices=(0..size).map(|offset|(start+offset)%5).collect::<Vec<_>>();
    let mut result=atom("0");
    for i in &indices{for j in &indices{result+=dot(*i,*j);}}
    result.expand()
}
fn main(){
    let expected=[atom("2"),atom("(11+sqrt(5))/2"),atom("(21+sqrt(5))/2"),atom("17")];
    let mut rows=Vec::new();
    for size in 1..=4{
        let values=(0..5).map(|start|subset_norm_squared(start,size)).collect::<Vec<_>>();
        assert!(values.iter().all(|value|*value==expected[size-1]));
        let m=size as i64;
        let polynomial=(atom(&format!("{}*t^2",m*m))-expected[size-1].clone()).factor();
        rows.push(json!({
            "arc_size":size,
            "cyclic_occurrences":5,
            "P_A_squared":expected[size-1].to_string(),
            "signed_threshold_polynomial":polynomial.to_string()
        }));
    }
    let field_polynomial=atom("t*(t^2-2)*(8*t^2-11-sqrt(5))*(18*t^2-21-sqrt(5))*(16*t^2-17)").factor();
    let rational_norm=atom("t*(t^2-2)*((8*t^2-11)^2-5)*((18*t^2-21)^2-5)*(16*t^2-17)").factor();
    let packet=json!({
        "schema":"marici.benincasa.five_site.cyclic_one_wall_landau.v1",
        "slice":"Entry 1234 conical C5 orbit with X_i=t",
        "landau_geometry":"For q_A=|A|t+y_i+y_j, stationary collinear two-focus configurations have y_i+y_j=±|P_A| after complex continuation.",
        "connected_arc_thresholds":rows,
        "total_and_one_cut_threshold":"t=0 from G=5t and G_minus_e=5t+2y_e at y_e=0",
        "candidate_polynomial_over_Qsqrt5":field_polynomial.to_string(),
        "rational_field_norm":rational_norm.to_string(),
        "physical_sheet_thresholds":"negative roots t=-|P_A|/|A|; positive roots belong to signed analytic continuation",
        "classification":"source-derived one-wall Landau/endpoint support over existing partial-energy and soft carrier",
        "scope":"complete for individual marked walls; simultaneous multi-wall anomalous Landau support remains uncomputed",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-cyclic-one-wall-landau.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
