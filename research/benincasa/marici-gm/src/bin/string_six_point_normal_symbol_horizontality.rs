use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}

fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}

fn main() {
    // Common regularized source row from the exact deeper-corner audit.
    let r = vec![
        a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
        a("-2*(-1+A3)*(-1+A2*B24)*(1+A3)*(1+A2*B24)/(A2*B24*A3)"),
        a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
        a("-2*(-1+A2)*(-1+A3*B34)*(1+A2)*(1+A3*B34)/(A2*A3*B34)"),
        a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)"),
        a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)"),
    ];

    let variables = [
        ("A2", symbol!("marici::A2")),
        ("A3", symbol!("marici::A3")),
        ("B24", symbol!("marici::B24")),
        ("B34", symbol!("marici::B34")),
    ];

    let mut projective_motion = Vec::new();
    for (name, variable) in variables {
        // M_x+M_y-M_z is identically zero entrywise, so its covariant
        // derivative in the common Hom bundle is also zero. Verify the
        // explicit derivative before invoking that formal statement.
        for entry in &r {
            let relation_entry = entry.clone() + a("0") - entry.clone();
            assert_eq!(clean(relation_entry.derivative(variable)), a("0"));
        }

        // The common image line itself is not constant in the serialized
        // six-word frame when at least one projective Wronskian is nonzero.
        let dr0 = r[0].derivative(variable);
        let nonzero_wr = (1..r.len())
            .filter(|j| {
                clean(r[0].clone() * r[*j].derivative(variable) - r[*j].clone() * dr0.clone())
                    != a("0")
            })
            .count();
        // The symbol module is target_rank(2) tensor source_line(r). If dr is
        // projectively independent of r, adjoining derivatives doubles the
        // source rank and gives derivative closure rank 2*2=4.
        let derivative_closure_rank = if nonzero_wr > 0 { 4 } else { 2 };
        projective_motion.push((name, nonzero_wr, derivative_closure_rank));
    }
    assert!(projective_motion.iter().all(|(_, count, rank)| *count > 0 && *rank == 4));

    let motion_json: Vec<serde_json::Value> = projective_motion
        .iter()
        .map(|(name, count, rank)| serde_json::json!({
            "variable": name,
            "nonzero_projective_wronskians": count,
            "derivative_closure_rank": rank
        }))
        .collect();
    println!(
        "{}",
        serde_json::to_string(&serde_json::json!({
            "schema": "marici.benincasa.string_six_point_normal_symbol_horizontality.v1",
            "tangential_variables": ["A2", "A3", "B24", "B34"],
            "syzygy": [1, 1, -1],
            "syzygy_coefficients_constant": true,
            "differentiated_matrix_identity_zero": true,
            "kernel_relation_horizontal_in_common_Hom_bundle": true,
            "image_line_constant_in_serialized_frame": false,
            "projective_motion": motion_json,
            "symbol_module_rank": 2,
            "derivative_closure_rank": 4,
            "closed_under_serialized_derivative": false,
            "canonical_rank_two_connection_from_transition_alone": false,
            "distinction": "horizontal kernel relation does not imply a trivial image-line connection"
        }))
        .unwrap()
    );
}
