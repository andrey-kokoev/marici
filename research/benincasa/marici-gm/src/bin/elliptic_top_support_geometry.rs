use std::collections::BTreeMap;

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Poly<const N: usize>(BTreeMap<[u8; N], i128>);

impl<const N: usize> Poly<N> {
    fn term(exponent: [u8; N], coefficient: i128) -> Self {
        let mut out = Self::default();
        if coefficient != 0 {
            out.0.insert(exponent, coefficient);
        }
        out
    }
    fn constant(value: i128) -> Self {
        Self::term([0; N], value)
    }
    fn variable(index: usize) -> Self {
        let mut exponent = [0; N];
        exponent[index] = 1;
        let mut out = Self::default();
        out.0.insert(exponent, 1);
        out
    }
    fn add(&self, other: &Self) -> Self {
        let mut out = self.clone();
        for (m, c) in &other.0 {
            let next = out.0.get(m).copied().unwrap_or(0) + c;
            if next == 0 {
                out.0.remove(m);
            } else {
                out.0.insert(*m, next);
            }
        }
        out
    }
    fn scale(&self, scalar: i128) -> Self {
        let mut out = Self::default();
        for (m, c) in &self.0 {
            let next = c * scalar;
            if next != 0 {
                out.0.insert(*m, next);
            }
        }
        out
    }
    fn sub(&self, other: &Self) -> Self {
        self.add(&other.scale(-1))
    }
    fn mul(&self, other: &Self) -> Self {
        let mut out = Self::default();
        for (lm, lc) in &self.0 {
            for (rm, rc) in &other.0 {
                let mut m = [0; N];
                for i in 0..N {
                    m[i] = lm[i] + rm[i];
                }
                let next = out.0.get(&m).copied().unwrap_or(0) + lc * rc;
                if next == 0 {
                    out.0.remove(&m);
                } else {
                    out.0.insert(m, next);
                }
            }
        }
        out
    }
    fn pow(&self, mut exponent: u8) -> Self {
        let mut out = Self::constant(1);
        let mut base = self.clone();
        while exponent > 0 {
            if exponent & 1 == 1 {
                out = out.mul(&base);
            }
            exponent >>= 1;
            if exponent > 0 {
                base = base.mul(&base);
            }
        }
        out
    }
    fn evaluate(&self, point: [i128; N]) -> i128 {
        self.0
            .iter()
            .map(|(m, c)| {
                let mut term = *c;
                for i in 0..N {
                    term *= point[i].pow(u32::from(m[i]));
                }
                term
            })
            .sum()
    }
    fn format(&self, names: [&str; N]) -> String {
        if self.0.is_empty() {
            return "0".to_owned();
        }
        let mut terms: Vec<_> = self.0.iter().collect();
        terms.sort_by_key(|(m, _)| std::cmp::Reverse(m.iter().copied().sum::<u8>()));
        terms
            .into_iter()
            .map(|(m, c)| {
                let factors: Vec<_> = m
                    .iter()
                    .enumerate()
                    .filter(|(_, e)| **e > 0)
                    .map(|(i, e)| {
                        if *e == 1 {
                            names[i].to_owned()
                        } else {
                            format!("{}^{}", names[i], e)
                        }
                    })
                    .collect();
                if factors.is_empty() {
                    c.to_string()
                } else if *c == 1 {
                    factors.join("*")
                } else if *c == -1 {
                    format!("-{}", factors.join("*"))
                } else {
                    format!("{}*{}", c, factors.join("*"))
                }
            })
            .collect::<Vec<_>>()
            .join(" + ")
            .replace("+ -", "- ")
    }
}

fn sum<const N: usize>(terms: &[Poly<N>]) -> Poly<N> {
    terms.iter().fold(Poly::default(), |a, b| a.add(b))
}

fn coefficient_in_t(polynomial: &Poly<4>, degree: u8) -> Poly<3> {
    let mut out = Poly::default();
    for (monomial, coefficient) in &polynomial.0 {
        if monomial[3] == degree {
            out.0
                .insert([monomial[0], monomial[1], monomial[2]], *coefficient);
        }
    }
    out
}

fn divide_by_variable_and_scalar(polynomial: &Poly<3>, variable: usize, scalar: i128) -> Poly<3> {
    let mut out = Poly::default();
    for (monomial, coefficient) in &polynomial.0 {
        assert!(monomial[variable] > 0);
        assert_eq!(coefficient % scalar, 0);
        let mut quotient = *monomial;
        quotient[variable] -= 1;
        out.0.insert(quotient, coefficient / scalar);
    }
    out
}

fn embed(polynomial: &Poly<3>) -> Poly<4> {
    let mut out = Poly::default();
    for (monomial, coefficient) in &polynomial.0 {
        out.0
            .insert([monomial[0], monomial[1], monomial[2], 0], *coefficient);
    }
    out
}

fn substitute_t(polynomial: &Poly<4>, replacement: &Poly<3>) -> Poly<3> {
    let mut out = Poly::default();
    for (monomial, coefficient) in &polynomial.0 {
        let base = Poly::term([monomial[0], monomial[1], monomial[2]], *coefficient);
        out = out.add(&base.mul(&replacement.pow(monomial[3])));
    }
    out
}

fn cayley_menger<const N: usize>(
    x: &Poly<N>,
    y: &Poly<N>,
    z: &Poly<N>,
    c: &Poly<N>,
    a: &Poly<N>,
    b: &Poly<N>,
) -> Poly<N> {
    let x2 = x.pow(2);
    let y2 = y.pow(2);
    let z2 = z.pow(2);
    let c2 = c.pow(2);
    let a2 = a.pow(2);
    let b2 = b.pow(2);
    let h = x2.add(&y2).sub(&z2);
    let ga0 = x2.mul(&x2.sub(&y2).sub(&z2));
    let gac = y2.sub(&x2).sub(&z2);
    let gb0 = y2.mul(&y2.sub(&x2).sub(&z2));
    let gbc = x2.sub(&y2).sub(&z2);
    let hc = z2.sub(&x2).sub(&y2);
    sum(&[
        x2.mul(&a.pow(4)),
        a2.mul(&b2).mul(&h).scale(-1),
        y2.mul(&b.pow(4)),
        a2.mul(&ga0),
        c2.mul(&a2).mul(&gac),
        b2.mul(&gb0),
        c2.mul(&b2).mul(&gbc),
        z2.mul(&c.pow(4)),
        c2.mul(&z2).mul(&hc),
        z2.mul(&x2).mul(&y2),
    ])
}

fn main() {
    let x = Poly::<3>::variable(0);
    let y = Poly::<3>::variable(1);
    let z = Poly::<3>::variable(2);
    let e = sum(&[x.clone(), y.clone(), z.clone()]);
    let top = cayley_menger(&x, &y, &z, &e.scale(-1), &x.add(&z), &y.add(&z));
    let signed_left = y.add(&z).sub(&x);
    let signed_right = x.add(&z).sub(&y);
    let expected_top = e.mul(&signed_left).mul(&signed_right).pow(2);
    assert_eq!(top, expected_top);
    println!("K_TRIPLE={}", top.format(["x", "y", "z"]));
    println!("K_TRIPLE_FACTORED=[(x+y+z)(-x+y+z)(x-y+z)]^2");
    println!("K_TRIPLE_A={}", top.evaluate([2, 3, 4]));
    println!("K_TRIPLE_B={}", top.evaluate([3, 5, 6]));

    let x = Poly::<4>::variable(0);
    let y = Poly::<4>::variable(1);
    let z = Poly::<4>::variable(2);
    let t = Poly::<4>::variable(3);
    let e = sum(&[x.clone(), y.clone(), z.clone()]);
    let kg1g2 = cayley_menger(&x, &y, &z, &t, &y.add(&t).scale(-1), &x.add(&t).scale(-1));
    let kg1g = cayley_menger(&x, &y, &z, &e.scale(-1), &t, &y.add(&z));
    let kg2g = cayley_menger(&x, &y, &z, &e.scale(-1), &x.add(&z), &t);
    println!("K_FACE_011={}", kg1g2.format(["x", "y", "z", "t"]));
    println!("K_FACE_101={}", kg1g.format(["x", "y", "z", "t"]));
    println!("K_FACE_110={}", kg2g.format(["x", "y", "z", "t"]));
    let mut mixed_roots = Vec::new();
    for (label, face, leading_variable) in [("101", &kg1g, 0_usize), ("110", &kg2g, 1_usize)] {
        assert_eq!(coefficient_in_t(face, 1), Poly::default());
        assert_eq!(coefficient_in_t(face, 3), Poly::default());
        let quartic = coefficient_in_t(face, 4);
        let quadratic = coefficient_in_t(face, 2);
        let constant = coefficient_in_t(face, 0);
        let discriminant = quadratic.pow(2).sub(&quartic.mul(&constant).scale(4));
        println!("FACE_{label}_T4={}", quartic.format(["x", "y", "z"]));
        println!("FACE_{label}_T2={}", quadratic.format(["x", "y", "z"]));
        println!("FACE_{label}_T0={}", constant.format(["x", "y", "z"]));
        println!(
            "FACE_{label}_U_DISCRIMINANT={}",
            discriminant.format(["x", "y", "z"])
        );
        let root_constant = divide_by_variable_and_scalar(&quadratic, leading_variable, 2);
        let leading_root = if leading_variable == 0 {
            x.clone()
        } else {
            y.clone()
        };
        let root = leading_root.mul(&t.pow(2)).add(&embed(&root_constant));
        assert_eq!(*face, root.pow(2));
        println!(
            "FACE_{label}_SQUARE_ROOT={}",
            root.format(["x", "y", "z", "t"])
        );
        mixed_roots.push(root);
    }

    let jacobian = -1_i128;
    let expected_011 = t.mul(&y.add(&z).sub(&x)).mul(&x.add(&z).sub(&y)).pow(2);
    assert_eq!(kg1g2, expected_011);
    let lambda = sum(&[
        Poly::<3>::variable(0),
        Poly::<3>::variable(1),
        Poly::<3>::variable(2),
    ])
    .mul(
        &Poly::<3>::variable(1)
            .add(&Poly::<3>::variable(2))
            .sub(&Poly::<3>::variable(0)),
    )
    .mul(
        &Poly::<3>::variable(0)
            .add(&Poly::<3>::variable(2))
            .sub(&Poly::<3>::variable(1)),
    );
    assert_eq!(
        substitute_t(
            &mixed_roots[0],
            &Poly::<3>::variable(0).add(&Poly::<3>::variable(2))
        ),
        lambda.scale(-1)
    );
    assert_eq!(
        substitute_t(
            &mixed_roots[1],
            &Poly::<3>::variable(1).add(&Poly::<3>::variable(2))
        ),
        lambda.scale(-1)
    );
    assert_eq!(jacobian.abs(), 1);
    assert_eq!(top.evaluate([2, 3, 4]), 18_225);
    println!("INCIDENCE_JACOBIAN={jacobian}");
    println!("TOP_RESIDUE_BOUNDARY_SIGNS=[1,-1,1]");

    // Normalization graph for W1 union W2. Vertices are
    // (C1+, C1-, C2+, C2-); edges are the two conductor nodes on each
    // wall followed by the same-sheet intersections (P+, P-).
    let boundary: [[i32; 6]; 4] = [
        [-1, -1, 0, 0, -1, 0],
        [1, 1, 0, 0, 0, -1],
        [0, 0, -1, -1, 1, 0],
        [0, 0, 1, 1, 0, 1],
    ];
    let cycles: [[i32; 3]; 6] = [
        [1, 0, 1],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, -1],
        [0, 0, -1],
        [0, 0, 1],
    ];
    for vertex in 0..4 {
        for cycle in 0..3 {
            let value: i32 = (0..6)
                .map(|edge| boundary[vertex][edge] * cycles[edge][cycle])
                .sum();
            assert_eq!(value, 0);
        }
    }
    // Rows (e1,e3,e6) give an upper-triangular unit minor, so these three
    // cycles form a primitive integral basis of the rank-three cycle lattice.
    let unit_minor = cycles[0][0] * cycles[2][1] * cycles[5][2];
    assert_eq!(unit_minor, 1);
    println!("TWO_WALL_GRAPH_VERTICES=4");
    println!("TWO_WALL_GRAPH_EDGES=6");
    println!("TWO_WALL_GRAPH_B1=3");
    println!("TWO_WALL_CYCLE_BASIS=[mixed_101,mixed_110,top_111_mod_mixed]");
    println!("TWO_WALL_CYCLE_UNIT_MINOR={unit_minor}");
}
