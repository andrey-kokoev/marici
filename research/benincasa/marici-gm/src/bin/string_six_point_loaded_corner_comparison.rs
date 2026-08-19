use serde_json::json;
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.expand().together().cancel().factor()
}
fn permutations(xs: &mut [usize], start: usize, out: &mut Vec<Vec<usize>>) {
    if start == xs.len() {
        out.push(xs.to_vec());
        return;
    }
    for i in start..xs.len() {
        xs.swap(start, i);
        permutations(xs, start + 1, out);
        xs.swap(start, i);
    }
}
fn parity(p: &[usize]) -> i64 {
    let mut n = 0;
    for i in 0..p.len() {
        for j in i + 1..p.len() {
            if p[i] > p[j] {
                n += 1;
            }
        }
    }
    if n % 2 == 0 {
        1
    } else {
        -1
    }
}
fn determinant(m: &[Vec<Atom>]) -> Atom {
    let mut ps = Vec::new();
    permutations(&mut [0, 1, 2, 3, 4, 5], 0, &mut ps);
    let mut sum = a("0");
    for p in ps {
        let mut term = a(&parity(&p).to_string());
        for row in 0..6 {
            term *= m[row][p[row]].clone();
        }
        sum += term;
    }
    clean(sum)
}

fn main() {
    let f1 = a("(Z*A2)^2-1");
    let f2 = a("(Z*A2*B24)^2-1");
    let f3 = a("(A3/Z)^2-1");
    let f4 = a("(A3*B34/Z)^2-1");
    // Rows: 123456,124356,132456,134256,142356,143256.
    // Columns retain the six occurrence order of Entries 962-963.
    let mut m = vec![vec![a("0"); 6]; 6];
    m[1][0] = f1.clone(); // ZA2 at host 124356
    m[2][1] = -f2.clone(); // B24 circuit: 132456 -> 134256
    m[3][1] = f2.clone();
    m[4][2] = f2.clone(); // second ZA2B24 occurrence
    m[3][3] = f3.clone(); // A3/Z at host 134256
    m[0][4] = -f4.clone(); // B34 circuit: 123456 -> 124356
    m[1][4] = f4.clone();
    m[5][5] = f4.clone(); // second A3B34/Z occurrence
    let det = determinant(&m);
    let expected = clean(f1.clone() * f2.clone().pow(2) * f3.clone() * f4.clone().pow(2));
    assert_eq!(clean(det.clone() + expected.clone()), a("0"));

    // The loaded-path identities use the occurrence-derived pivots.
    let left_identity = clean(
        ((a("Z*A2").pow(2) - a("1")) + a("Z*A2").pow(2) * (a("B24").pow(2) - a("1"))) - f2.clone(),
    );
    let right_identity = clean(
        ((a("A3/Z").pow(2) - a("1")) + a("A3/Z").pow(2) * (a("B34").pow(2) - a("1"))) - f4.clone(),
    );
    assert_eq!(left_identity, a("0"));
    assert_eq!(right_identity, a("0"));

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_loaded_corner_comparison.v1",
        "target_basis":["123456","124356","132456","134256","142356","143256"],
        "source_occurrence_basis":["ZA2@124356","ZA2B24@124356","ZA2B24@142356","A3/Z@134256","A3B34/Z@134256","A3B34/Z@143256"],
        "matrix":m.iter().map(|row|row.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),
        "determinant":det.to_string(),
        "determinant_up_to_unit":expected.to_string(),
        "fitting_valuations":{"ZA2":1,"ZA2B24":2,"A3/Z":1,"A3B34/Z":2},
        "pivot_transition_identities_verified":true,
        "generic_rank":6,
        "additional_irreducible_factors":[],
        "classification":"occurrence-labelled host and pivot-transition columns reproduce the complete composite Fitting divisor up to a unit"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-loaded-corner-comparison.json", &text).unwrap();
    print!("{text}");
}
