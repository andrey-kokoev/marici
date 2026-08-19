use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn laurent_sine(x: Atom) -> Atom {
    x.clone() - a("1") / x
}
fn laurent_cosine_twice(x: Atom) -> Atom {
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
        result *= laurent_sine(mon);
    }
    clean(result)
}
fn substitute(x: Atom, name: &str, value: &str) -> Atom {
    x.replace(a(name).to_pattern())
        .with(a(value).to_pattern())
        .together()
        .cancel()
        .factor()
}

fn main() {
    let x = a("X");
    let z = a("Z");
    let q = a("Q");
    let y = clean(q / (x.clone() * z.clone()));
    let sx = laurent_sine(x.clone());
    let sy = laurent_sine(y.clone());
    let sz = laurent_sine(z.clone());
    let cx = laurent_cosine_twice(x);
    let cy = laurent_cosine_twice(y);
    let cz = laurent_cosine_twice(z);
    // Common invertible csc(s14) and global powers of 2i are omitted.
    let e = [
        [
            clean(a("2") / sx.clone()),
            clean(-(cx.clone() / sx.clone() + cz / sz)),
        ],
        [clean(-(cx / sx.clone() + cy / sy)), clean(a("2") / sx)],
    ];
    let basis = permutations();
    let right_words = [basis[4], basis[5]];
    let kd: Vec<Vec<Atom>> = right_words
        .iter()
        .map(|beta| {
            basis
                .iter()
                .map(|alpha| dense_entry(*alpha, *beta))
                .collect()
        })
        .collect();
    let mut product = vec![vec![a("0"); 6]; 2];
    for i in 0..2 {
        for j in 0..6 {
            product[i][j] =
                clean(e[i][0].clone() * kd[0][j].clone() + e[i][1].clone() * kd[1][j].clone());
        }
    }
    let mut route_qx = Vec::new();
    let mut route_xq = Vec::new();
    for row in &product {
        for entry in row {
            route_qx.push(substitute(substitute(entry.clone(), "Q", "1"), "X", "1"));
            route_xq.push(substitute(substitute(entry.clone(), "X", "1"), "Q", "1"));
        }
    }
    for i in 0..12 {
        assert_eq!(route_qx[i], route_xq[i], "entry {i} has an order defect");
        let text = route_qx[i].to_string();
        assert!(!text.contains("marici::X") && !text.contains("marici::Q"));
    }
    for i in 0..6 {
        assert_eq!(clean(route_qx[i].clone() + route_qx[i + 6].clone()), a("0"));
    }
    let nonzero = route_qx.iter().filter(|x| **x != a("0")).count();
    println!("{{\"schema\":\"marici.benincasa.string_six_point_mixed_corner_exact.v1\",\"entries\":12,\"nonzero_entries\":{},\"ordered_maps_equal\":true,\"normal_variables_absent\":true,\"exceptional_rank\":1,\"row_relation\":\"row_2=-row_1\",\"representatives\":[{}]}}",nonzero,route_qx.iter().map(|x|format!("\"{}\"",x.to_string().replace('"',"\\\""))).collect::<Vec<_>>().join(","));
}
