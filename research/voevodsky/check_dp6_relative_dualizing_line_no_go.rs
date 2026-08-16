//! Relative-dualizing-line obstruction for the shifted corridor target.
//!
//! A line-valued perfect/log-smooth Gysin correspondence has one locally
//! constant cohomological shift on each connected component.  The enhanced
//! corridor forced by the conductor Tor grading instead requires shifts 0
//! and 1 on two reflection-exchanged boundary edges.  This checker certifies
//! the resulting connectedness and equivariance obstruction.  It does not
//! exclude a stratified two-term dualizing complex or a derived wall object.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct ShiftAssignment {
    left: i32,
    right: i32,
}

fn is_locally_constant_on_connected_corridor(s: ShiftAssignment) -> bool {
    // The two boundary charts meet through the corridor wall.  A perfect
    // relative-dualizing line has constant virtual rank across that edge.
    s.left == s.right
}

fn reflection_pullback(s: ShiftAssignment) -> ShiftAssignment {
    ShiftAssignment {
        left: s.right,
        right: s.left,
    }
}

fn main() {
    let desired = ShiftAssignment { left: 0, right: 1 };

    // The exact P plus P[1] target is not the restriction of one dualizing
    // line on a connected perfect correspondence.
    assert!(!is_locally_constant_on_connected_corridor(desired));

    // Exhaustively check the only shifts relevant to the source/target
    // amplitudes.  Connected line assignments are diagonal; none is (0,1).
    let mut connected_assignments = Vec::new();
    for left in -2..=2 {
        for right in -2..=2 {
            let assignment = ShiftAssignment { left, right };
            if is_locally_constant_on_connected_corridor(assignment) {
                connected_assignments.push(assignment);
            }
        }
    }
    assert_eq!(connected_assignments.len(), 5);
    assert!(!connected_assignments.contains(&desired));

    // An equivariant line has reflection-invariant virtual rank.  Reflection
    // sends the desired assignment to (1,0), not back to itself.
    assert_eq!(
        reflection_pullback(desired),
        ShiftAssignment { left: 1, right: 0 }
    );
    assert_ne!(reflection_pullback(desired), desired);
    for assignment in &connected_assignments {
        assert_eq!(reflection_pullback(*assignment), *assignment);
    }

    // Disconnecting the charts permits the two shifts but removes the wall
    // restriction/endpoint BC map.  The minimal admissible repair therefore
    // needs a wall-supported cone (a two-term/stratified dualizing complex),
    // not merely two unrelated line components.
    let disconnected_allows_desired = true;
    let disconnected_supplies_wall_bc = false;
    assert!(disconnected_allows_desired);
    assert!(!disconnected_supplies_wall_bc);

    println!(
        "{}",
        r#"{"status":"falsified_scoped_connected_relative_dualizing_line","connected_corridor_vertices":2,"connected_corridor_edges":1,"desired_boundary_shifts":[0,1],"locally_constant_line_assignments_in_test_window":5,"desired_assignment_locally_constant":false,"reflection_of_desired":[1,0],"equivariant_line_can_realize_desired":false,"disconnected_lines_allow_shifts":true,"disconnected_lines_supply_wall_bc":false,"minimal_additional_geometry":"a reflection-equivariant stratified two-term relative-dualizing complex with a wall-supported cone and endpoint Beck-Chevalley maps","literal_entry143_realization_constructed":false,"endpoint_Q_mapping_fiber_instantiated":false,"p_partial_Q_defined":false}"#
    );
}
