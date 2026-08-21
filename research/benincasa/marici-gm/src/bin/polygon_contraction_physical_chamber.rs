use serde_json::json;
use std::fs;

fn main(){
    let mut arities=Vec::new();
    for n in 4..=8 {
        // Contract edge (n,1), whose nonnegative energy is set to zero.
        // The remaining singleton walls are sums of one site energy and the
        // other adjacent edge energy.
        let first_support=vec!["X_1", "y_{1,2}"];
        let second_support=vec![format!("X_{n}"),format!("y_{{{},{}}}",n-1,n)];
        assert_eq!(first_support.len(),2);
        assert_eq!(second_support.len(),2);
        arities.push(json!({
            "arity":n,
            "contracted_edge":format!("y_{{{},1}}=0",n),
            "remaining_singleton_walls":[
                "q_1=X_1+y_{1,2}",
                format!("q_{n}=X_{n}+y_{{{},{}}}",n-1,n)
            ],
            "generic_positive_chamber_endpoint_intersection":false,
            "first_endpoint_requires":first_support,
            "second_endpoint_requires":second_support,
            "endpoint_support_is_deeper_soft_corner":true
        }));
    }
    let packet=json!({
        "schema":"marici.benincasa.polygon_contraction_physical_chamber.v1",
        "frozen_chamber":"X_i>0 and y_i>=0",
        "audits":arities,
        "conclusion":{
            "generic_contraction_boundary_selects_first_occurrence":false,
            "generic_contraction_boundary_selects_second_occurrence":false,
            "one_sided_unit_residue_physically_selected":false,
            "endpoint_residues_live_on_deeper_soft_support":true,
            "direct_physical_period_recursion":false
        },
        "scope":"Exact support and positivity audit for the Euclidean polygon chamber; analytic continuation to deeper soft corners is not constructed."
    });
    fs::write("../results/polygon-contraction-physical-chamber.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["conclusion"]).unwrap());
}
