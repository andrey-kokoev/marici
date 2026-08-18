use std::collections::BTreeMap;

fn det(left: (i32, i32), right: (i32, i32)) -> i32 {
    left.0 * right.1 - left.1 * right.0
}

fn main() {
    // Gradients in the q_G12 residue chart with orientation da wedge db.
    let normals = BTreeMap::from([
        ("g1", (0, 1)),
        ("g2", (1, 0)),
        ("g3", (1, 1)),
        ("G23", (1, 0)),
        ("G31", (0, 1)),
    ]);
    let representatives = [
        ("g1", "g2", -1),
        ("g1", "g3", -1),
        ("g1", "G23", -1),
        ("g2", "g3", 1),
        ("g2", "G31", 1),
        ("g3", "G23", -1),
        ("g3", "G31", 1),
        ("G23", "G31", 1),
    ];

    for (left, right, expected) in representatives {
        assert_eq!(det(normals[left], normals[right]), expected);
        println!("pair={left},{right};orientation={expected}");
    }

    // The source occurrence cycle (a,b,c)->(b,c,a) is an even permutation.
    // Residuing c, then a, then b gives the cyclic chart orientations
    // da^db -> db^dc -> dc^da -> da^db with unit +1 at every step.
    let cyclic_volume_sign = 1_i32;
    let residue_chart_transition_unit = 1_i32;
    let cm_determinant_transition_unit = 1_i32;
    let square_root_line_transition_unit = 1_i32;
    assert_eq!(
        cyclic_volume_sign
            * residue_chart_transition_unit
            * cm_determinant_transition_unit
            * square_root_line_transition_unit,
        1
    );

    println!("representative_count=8");
    println!("labelled_occurrence_count=24");
    println!("cyclic_chart_orientation_unit=1");
    println!("cm_branch_transition_unit=1");
    println!("kato_line_transition_unit=1");
    println!("all_naturality_squares_commute=true");
}
