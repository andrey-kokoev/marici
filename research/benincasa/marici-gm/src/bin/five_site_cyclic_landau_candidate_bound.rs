use serde_json::{json, Value};
use std::fs;
use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn degree(mut polynomial: Atom, variable: Symbol) -> usize {
    let mut value = 0usize;
    loop {
        let derivative = polynomial.derivative(variable).expand();
        if derivative == atom("0") {
            return value;
        }
        polynomial = derivative;
        value += 1;
    }
}

fn quadratic_norm(text: &str) -> Atom {
    let rewritten = text
        .replace("5^(1/2)", "s")
        .replace('x', "z");
    let original = atom(&rewritten);
    let conjugate = original
        .clone()
        .replace(atom("s").to_pattern())
        .with(atom("-s").to_pattern())
        .expand();
    let norm = (original * conjugate)
        .expand()
        .replace(atom("s^2").to_pattern())
        .with(atom("5").to_pattern())
        .expand()
        .factor();
    assert_eq!(
        norm.clone()
            .replace(atom("s").to_pattern())
            .with(atom("0").to_pattern())
            .expand(),
        norm.clone().expand()
    );
    norm
}

const PRIME: i128 = 2_147_483_647;

fn mod_inverse(mut value: i128) -> i128 {
    value = value.rem_euclid(PRIME);
    let (mut old_r, mut r) = (value, PRIME);
    let (mut old_s, mut s) = (1i128, 0i128);
    while r != 0 {
        let quotient = old_r / r;
        (old_r, r) = (r, old_r - quotient * r);
        (old_s, s) = (s, old_s - quotient * s);
    }
    assert_eq!(old_r, 1);
    old_s.rem_euclid(PRIME)
}

fn trim(poly: &mut Vec<i128>) {
    while poly.last() == Some(&0) && poly.len() > 1 {
        poly.pop();
    }
}

fn remainder(mut left: Vec<i128>, right: &[i128]) -> Vec<i128> {
    let inverse = mod_inverse(*right.last().unwrap());
    while left.len() >= right.len() && !(left.len() == 1 && left[0] == 0) {
        let shift = left.len() - right.len();
        let coefficient = (left[left.len() - 1] * inverse).rem_euclid(PRIME);
        for (index, value) in right.iter().enumerate() {
            left[index + shift] = (left[index + shift] - coefficient * value).rem_euclid(PRIME);
        }
        trim(&mut left);
    }
    left
}

fn gcd_degree(mut left: Vec<i128>, mut right: Vec<i128>) -> usize {
    trim(&mut left);
    trim(&mut right);
    while !(right.len() == 1 && right[0] == 0) {
        let next = remainder(left, &right);
        left = right;
        right = next;
    }
    left.len() - 1
}

fn modular_coefficients(polynomial: Atom, variable: Symbol) -> Vec<i128> {
    let degree = degree(polynomial.clone(), variable);
    let mut derivative = polynomial.expand();
    let mut factorial = 1i128;
    let mut coefficients = Vec::new();
    for order in 0..=degree {
        let at_zero = derivative
            .clone()
            .replace(atom("z").to_pattern())
            .with(atom("0").to_pattern())
            .expand();
        let integer: i128 = at_zero.to_string().parse().unwrap();
        coefficients.push((integer.rem_euclid(PRIME) * mod_inverse(factorial.rem_euclid(PRIME))).rem_euclid(PRIME));
        derivative = derivative.derivative(variable).expand();
        factorial = (factorial * (order as i128 + 1)).rem_euclid(PRIME);
    }
    trim(&mut coefficients);
    coefficients
}

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-disjoint-mixed-pair-landau.json").unwrap(),
    )
    .unwrap();
    let z = symbol!("marici::z");

    let one_wall = atom(
        "z*(z-2)*(16*z-17)*(29-44*z+16*z^2)*(109-189*z+81*z^2)",
    )
    .factor();
    let region_pair = atom("1121-18540*z+94932*z^2-174960*z^3+104976*z^4").factor();

    let mut mixed_rows = Vec::new();
    let mut factors = vec![one_wall.clone(), region_pair.clone()];
    let mut mixed_total_degree = 0usize;
    for case in source["cases"].as_array().unwrap() {
        let norm = quadratic_norm(case["saturated_resultant"].as_str().unwrap());
        let norm_degree = degree(norm.clone(), z);
        assert_eq!(norm_degree, 12);
        mixed_total_degree += norm_degree;
        factors.push(norm.clone());
        mixed_rows.push(json!({
            "label": case["label"],
            "norm_degree_in_z": norm_degree,
            "rational_quadratic_field_norm": norm.to_string(),
            "status": "saturated elimination factor; singular-support sufficiency not asserted"
        }));
    }

    let total_degree = degree(one_wall.clone(), z)
        + degree(region_pair.clone(), z)
        + mixed_total_degree;
    assert_eq!(degree(one_wall.clone(), z), 7);
    assert_eq!(degree(region_pair.clone(), z), 4);
    assert_eq!(mixed_total_degree, 72);
    assert_eq!(total_degree, 83);

    let modular = factors
        .iter()
        .cloned()
        .map(|factor| modular_coefficients(factor, z))
        .collect::<Vec<_>>();
    let mut pairwise_checks = 0usize;
    for left in 0..modular.len() {
        let derivative = (1..modular[left].len())
            .map(|power| (modular[left][power] * power as i128).rem_euclid(PRIME))
            .collect::<Vec<_>>();
        assert_eq!(gcd_degree(modular[left].clone(), derivative), 0);
        for right in left + 1..modular.len() {
            assert_eq!(gcd_degree(modular[left].clone(), modular[right].clone()), 0);
            pairwise_checks += 1;
        }
    }
    assert_eq!(pairwise_checks, 28);

    let packet = json!({
        "schema": "marici.five_site_cyclic_landau_candidate_bound.v1",
        "slice": "Entry 1234 cyclic physical slice; z=t^2",
        "one_wall_factor": one_wall.to_string(),
        "one_wall_degree_in_z": 7,
        "region_pair_factor": region_pair.to_string(),
        "region_pair_degree_in_z": 4,
        "disjoint_mixed_pair_norms": mixed_rows,
        "disjoint_mixed_pair_total_degree_in_z": mixed_total_degree,
        "raw_product_degree_in_z": total_degree,
        "squarefree_modular_certificate": {
            "prime": PRIME,
            "individual_squarefree_checks": factors.len(),
            "pairwise_coprimality_checks": pairwise_checks,
            "all_passed": true,
            "logic": "a nonconstant gcd over Q would remain nonconstant modulo every good prime; this good-prime degree-zero certificate proves Q-coprimality"
        },
        "interpretation": "finite source-derived eliminant bound from presently certified one- and two-wall families",
        "not_proved": [
            "absence of higher compatible-subset factors",
            "that every eliminant factor is actual period singular support",
            "a Picard-Fuchs order or operator"
        ],
        "new_carrier_datum": false
    });
    fs::write(
        "../results/five-site-cyclic-landau-candidate-bound.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", json!({
        "one_wall_degree": 7,
        "region_pair_degree": 4,
        "mixed_pair_degree": mixed_total_degree,
        "raw_total_degree": total_degree
    }));
}
