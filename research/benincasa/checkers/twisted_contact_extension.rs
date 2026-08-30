// Minimal-character repair of the contact logarithmic local system.

fn rank_2x2(m: [[i32; 2]; 2]) -> usize {
    let det = m[0][0] * m[1][1] - m[0][1] * m[1][0];
    if det != 0 {
        2
    } else if m.iter().flatten().any(|x| *x != 0) {
        1
    } else {
        0
    }
}

fn main() {
    let t_log = [[1, 1], [0, 1]];
    let t_kummer = -1;

    // A rank-one twist chi can align an eigencharacter with -1 only for chi=-1.
    let admissible_twists: Vec<i32> = [-1, 1]
        .iter()
        .copied()
        .filter(|chi| chi * t_log[0][0] == t_kummer)
        .collect();
    assert_eq!(admissible_twists, vec![-1]);

    let t_twisted = [[-1, -1], [0, -1]];
    let nilpotent_part = [
        [t_twisted[0][0] + 1, t_twisted[0][1]],
        [t_twisted[1][0], t_twisted[1][1] + 1],
    ]; // T_twisted-(-I)
    assert_eq!(rank_2x2(nilpotent_part), 1);

    // Intertwiners K_- -> twisted logarithmic block form ker(T_twisted+I),
    // the unique invariant line spanned by e_1.
    let intertwiner_equation = [[0, -1], [0, 0]];
    assert_eq!(rank_2x2(intertwiner_equation), 1);

    println!(
        "{{\"status\":\"pass\",\"unique_character_twist\":-1,\"twisted_nilpotent_rank\":1,\"kummer_subline_dimension\":1,\"isomorphism\":false}}"
    );
}
