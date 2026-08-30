use serde_json::json;
use std::fs;

fn main(){
    let roots:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/five-site-cyclic-triple-region-real-roots.json").unwrap()).unwrap();
    let residue:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/five-site-cyclic-triple-d4-source-residue.json").unwrap()).unwrap();
    let record=roots["records"].as_array().unwrap().iter().find(|record|record["representative"]=="g_12|g_34|g_5").unwrap();
    let root=record["refined_branch_and_square_signs"].as_array().unwrap().iter().find(|root|
        root["common_nonzero_wall_multiplier_sign"]==true&&root["positive_linear_loop_sheet_exists"]==true).unwrap();
    assert_eq!(root["projective_wall_multiplier_signs"],json!([-1,-1,-1]));
    assert_eq!(root["required_t_sign_for_positive_fixed_y"],-1);
    assert_eq!(residue["termwise_cancellation_possible"],false);
    assert_eq!(residue["common_local_residue_sign"],-1);

    // After the harmless common projective rescaling beta -> -beta, write
    // alpha_12, alpha_34, alpha_5 > 0.  Under Xi -> Xi-i epsilon_i,
    // Im(q_12,q_34,q_5)=(-(e1+e2),-(e3+e4),-e5).
    // Their pairing is strictly negative on the complete positive regulator cone.
    let packet=json!({
        "schema":"marici.five_site_cyclic_triple_d4_iepsilon_pairing.v1",
        "active_walls":["g_12","g_34","g_5"],
        "positive_multiplier_frame":["alpha_12>0","alpha_34>0","alpha_5>0"],
        "source_regulator_map":{
            "prescription":"X_i -> X_i-i*epsilon_i, epsilon_i>0",
            "imaginary_active_walls":["-(epsilon_1+epsilon_2)","-(epsilon_3+epsilon_4)","-epsilon_5"]
        },
        "normal_pairing":"-alpha_12*(epsilon_1+epsilon_2)-alpha_34*(epsilon_3+epsilon_4)-alpha_5*epsilon_5",
        "strict_sign_on_positive_regulator_cone":-1,
        "local_model":"interior ordinary A1 pinch with nonzero source residue",
        "picard_lefschetz_intersection_absolute_value":1,
        "orientation_sign":"depends on the retained ordered residue and thimble orientation",
        "scope":"local physical-sheet activation; no claim about the global analytic function away from the fold"
    });
    fs::write("../results/five-site-cyclic-triple-d4-iepsilon-pairing.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",json!({"strict_regulator_pairing_sign":-1,"local_intersection_absolute_value":1}));
}
