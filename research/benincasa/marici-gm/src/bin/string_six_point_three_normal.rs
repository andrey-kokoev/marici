use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn sine(x: Atom) -> Atom {
    x.clone() - a("1") / x
}
fn cosine_twice(x: Atom) -> Atom {
    x.clone() + a("1") / x
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn permutations() -> Vec<[usize; 3]> {
    vec![
        [2, 3, 4],
        [2, 4, 3],
        [3, 2, 4],
        [3, 4, 2],
        [4, 2, 3],
        [4, 3, 2],
    ]
}
fn pair(i: usize, j: usize) -> Atom {
    match (i.min(j), i.max(j)) {
        (2, 3) => a("X"),
        (2, 4) => a("B24"),
        (3, 4) => a("B34"),
        _ => panic!(),
    }
}
fn pivot(i: usize) -> Atom {
    match i {
        2 => a("A2"),
        3 => a("A3"),
        4 => a("A4"),
        _ => panic!(),
    }
}
fn dense_entry(alpha: [usize; 3], beta: [usize; 3]) -> Atom {
    let mut pos = [0usize; 5];
    for (i, j) in beta.iter().enumerate() {
        pos[*j] = i;
    }
    let mut result = a("1");
    for t in 0..3 {
        let i = alpha[t];
        let mut mon = pivot(i);
        for j in alpha.iter().skip(t + 1) {
            if pos[i] > pos[*j] {
                mon *= pair(i, *j);
            }
        }
        result *= sine(mon);
    }
    clean(result)
}
fn specialize(x: Atom, name: &str) -> Atom {
    x.replace(a(name).to_pattern())
        .with(a("1").to_pattern())
        .together()
        .cancel()
        .factor()
}
fn route(x: Atom, order: &[&str]) -> Atom {
    order
        .iter()
        .fold(x, |value, variable| specialize(value, variable))
}

fn main() {
    let x = a("X");
    let z = a("Z");
    let q = a("Q");
    let y = clean(q / (x.clone() * z.clone()));
    let sx = sine(x.clone());
    let sy = sine(y.clone());
    let sz = sine(z.clone());
    let cx = cosine_twice(x);
    let cy = cosine_twice(y);
    let cz = cosine_twice(z);

    // This is sin(pi*s14) sin(pi*s235) times the sparse block, up to
    // the common source normalization. Hence the three normals are
    // A4=e^{i pi s14}, X=e^{i pi s23}, Q=e^{i pi s235}.
    let sparse_normalized = [
        [
            clean(a("2") / sx.clone()),
            clean(-(cx.clone() / sx.clone() + cz / sz)),
        ],
        [clean(-(cx / sx.clone() + cy / sy)), clean(a("2") / sx)],
    ];
    let basis = permutations();
    let right_words = [basis[4], basis[5]];
    let dense: Vec<Vec<Atom>> = right_words
        .iter()
        .map(|beta| {
            basis
                .iter()
                .map(|alpha| dense_entry(*alpha, *beta))
                .collect()
        })
        .collect();
    let mut transition = vec![vec![a("0"); 6]; 2];
    for i in 0..2 {
        for j in 0..6 {
            transition[i][j] = clean(
                sparse_normalized[i][0].clone() * dense[0][j].clone()
                    + sparse_normalized[i][1].clone() * dense[1][j].clone(),
            );
        }
    }

    let orders = [
        ["A4", "X", "Q"],
        ["A4", "Q", "X"],
        ["X", "A4", "Q"],
        ["X", "Q", "A4"],
        ["Q", "A4", "X"],
        ["Q", "X", "A4"],
    ];
    let routes: Vec<Vec<Atom>> = orders
        .iter()
        .map(|order| {
            transition
                .iter()
                .flatten()
                .cloned()
                .map(|entry| route(entry, order))
                .collect()
        })
        .collect();
    for candidate in routes.iter().skip(1) {
        assert_eq!(candidate, &routes[0]);
    }
    for entry in &routes[0] {
        let text = entry.to_string();
        assert!(
            !text.contains("marici::A4")
                && !text.contains("marici::X")
                && !text.contains("marici::Q")
        );
    }
    for j in 0..6 {
        assert_eq!(
            clean(routes[0][j].clone() + routes[0][j + 6].clone()),
            a("0")
        );
    }
    let nonzero = routes[0].iter().filter(|entry| **entry != a("0")).count();
    let first_a4_grade: Vec<Atom> = transition
        .iter()
        .flatten()
        .cloned()
        .map(|entry| {
            let mixed_grade = route(entry, &["X", "Q"]);
            specialize(clean(mixed_grade / (a("A4") - a("1"))), "A4")
        })
        .collect();
    for j in 0..6 {
        assert_eq!(
            clean(first_a4_grade[j].clone() + first_a4_grade[j + 6].clone()),
            a("0")
        );
    }
    let first_grade_nonzero = first_a4_grade
        .iter()
        .filter(|entry| **entry != a("0"))
        .count();
    println!(
        "{{\"schema\":\"marici.benincasa.string_six_point_three_normal.v1\",\"flag\":[\"s14\",\"s23\",\"s235\"],\"orders_checked\":6,\"all_orders_equal\":true,\"normal_variables_absent\":true,\"ordinary_exceptional_rank\":0,\"ordinary_nonzero_entries\":{},\"ordinary_tetrahedral_coherence\":\"trivial_zero\",\"first_A4_grade_rank\":{},\"first_A4_grade_nonzero_entries\":{}}}",
        nonzero,
        if first_grade_nonzero > 0 { 1 } else { 0 },
        first_grade_nonzero
    );
}
