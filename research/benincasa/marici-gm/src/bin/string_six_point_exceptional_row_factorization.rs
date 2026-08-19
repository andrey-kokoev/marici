use serde_json::json;
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
fn at(x: Atom, name: &str, value: &str) -> Atom {
    clean(x.replace(a(name).to_pattern()).with(a(value).to_pattern()))
}
fn permutations() -> Vec<[usize; 3]> {
    vec![[2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2]]
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

fn main() {
    let x = a("X");
    let z = a("Z");
    let sx = sine(x.clone());
    let sz = sine(z.clone());
    let cx = cosine_twice(x);
    let cz = cosine_twice(z);
    let sparse = [
        clean(a("2") / sx.clone()),
        clean(-(cx / sx + cz / sz)),
    ];
    let basis = permutations();
    let right = [basis[4], basis[5]];
    let dense: Vec<Vec<Atom>> = right
        .iter()
        .map(|beta| basis.iter().map(|alpha| dense_entry(*alpha, *beta)).collect())
        .collect();
    let transition: Vec<Atom> = (0..6)
        .map(|j| clean(sparse[0].clone() * dense[0][j].clone() + sparse[1].clone() * dense[1][j].clone()))
        .collect();
    let plus: Vec<Atom> = transition
        .into_iter()
        .map(|entry| {
            let entry = at(at(entry, "X", "1"), "Q", "1");
            at(clean(entry / (a("A4") - a("1"))), "A4", "1")
        })
        .collect();

    let p = [4usize, 1, 0, 5, 3, 2];
    let factor_index = [0usize, 1, 1, 2, 3, 3];
    let factors = [
        a("(Z*A2)^2-1"),
        a("(Z*A2*B24)^2-1"),
        a("(A3/Z)^2-1"),
        a("(A3*B34/Z)^2-1"),
    ];
    let branches = [
        ["1/A2", "-1/A2"],
        ["1/(A2*B24)", "-1/(A2*B24)"],
        ["A3", "-A3"],
        ["A3*B34", "-A3*B34"],
    ];

    let mut records = Vec::new();
    for i in 0..6 {
        let j = p[i];
        let k = factor_index[i];
        let quotient = clean(plus[j].clone() / factors[k].clone());
        assert_eq!(clean(factors[k].clone() * quotient.clone() - plus[j].clone()), a("0"));
        let restrictions: Vec<_> = branches[k]
            .iter()
            .map(|value| at(quotient.clone(), "Z", value))
            .collect();
        assert!(restrictions.iter().all(|r| *r != a("0")));
        records.push(json!({
            "occurrence":i,
            "dense_component":j,
            "factor":factors[k].to_string(),
            "quotient":quotient.to_string(),
            "branch_restrictions":restrictions.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "generic_local_unit":true
        }));
    }
    let packet = json!({
        "schema":"marici.benincasa.string_six_point_exceptional_row_factorization.v1",
        "permutation":p,
        "factorizations":records,
        "exact_factorization_count":6,
        "generic_local_unit_count":6,
        "classification":"after the source-labelled permutation, every exact exceptional-row component is its assigned source wall times a generically invertible local coefficient",
        "scope":"rank-one exceptional row on each generic localized wall; full rational six-by-six transition remains unproved"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-exceptional-row-factorization.json", &text).unwrap();
    print!("{text}");
}
