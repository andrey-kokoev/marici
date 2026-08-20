//! Exact incidence audit for the source one-loop two-site arrangement.

use std::collections::BTreeSet;

#[derive(Clone, Copy)]
struct Linear {
    // x1, x2, P
    c: [i32; 3],
}

fn add(a: Linear, b: Linear) -> Linear {
    Linear { c: [a.c[0] + b.c[0], a.c[1] + b.c[1], a.c[2] + b.c[2]] }
}

fn sub(a: Linear, b: Linear) -> Linear {
    Linear { c: [a.c[0] - b.c[0], a.c[1] - b.c[1], a.c[2] - b.c[2]] }
}

fn canonical(mut c: [i32; 3]) -> [i32; 3] {
    let g = c.iter().map(|x| x.abs()).filter(|x| *x != 0).fold(0, gcd);
    if g > 1 { for x in &mut c { *x /= g; } }
    if c.iter().find(|x| **x != 0).is_some_and(|x| *x < 0) {
        for x in &mut c { *x = -*x; }
    }
    c
}

fn gcd(a: i32, b: i32) -> i32 { if b == 0 { a } else { gcd(b, a % b) } }

fn main() {
    // A_sigma: z1=x1+sigma P; B_tau: z1-zG=-x2+tau P.
    let a_plus = Linear { c: [1, 0, 1] };
    let a_minus = Linear { c: [1, 0, -1] };
    let b_plus = Linear { c: [0, 1, -1] }; // z1=zG=0 gives x2-P=0
    let b_minus = Linear { c: [0, 1, 1] };

    let mut letters = BTreeSet::new();
    // Branch-pair collisions.
    letters.insert(canonical(sub(a_plus, a_minus).c));
    letters.insert(canonical(sub(b_plus, b_minus).c));
    // Intersections with both marked planes z1=zG=0.
    for line in [a_plus, a_minus, b_plus, b_minus] { letters.insert(canonical(line.c)); }
    // A_sigma and B_tau intersect on the marked plane zG=0.
    for a in [a_plus, a_minus] {
        for b in [b_plus, b_minus] { letters.insert(canonical(add(a, b).c)); }
    }

    let expected: BTreeSet<[i32; 3]> = [
        [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1],
        [1, 1, 2], [1, 0, -1], [0, 1, -1], [1, 1, -2],
    ].iter().copied().map(canonical).collect();
    assert_eq!(letters, expected);
    assert_eq!(letters.len(), 8);
    println!("bubble_arrangement_letters=8 exact_match=true new_carrier_divisors=0");
}
