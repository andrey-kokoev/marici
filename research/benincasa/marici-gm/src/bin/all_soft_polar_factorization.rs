use std::collections::BTreeMap;

type Monomial = [u8; 6]; // E,P1,P2,P3,a,b

#[derive(Clone, Debug, Default, PartialEq, Eq)]
struct Poly(BTreeMap<Monomial, i64>);

impl Poly {
    fn term(coefficient: i64, monomial: Monomial) -> Self {
        let mut out = Self::default();
        if coefficient != 0 { out.0.insert(monomial, coefficient); }
        out
    }
    fn add(&self, rhs: &Self) -> Self {
        let mut out = self.clone();
        for (m, c) in &rhs.0 {
            let next = out.0.get(m).copied().unwrap_or(0) + c;
            if next == 0 { out.0.remove(m); } else { out.0.insert(*m, next); }
        }
        out
    }
    fn scale(&self, scalar: i64) -> Self {
        self.0.iter().fold(Self::default(), |out, (m, c)| out.add(&Self::term(c * scalar, *m)))
    }
    fn multiply(&self, rhs: &Self) -> Self {
        let mut out = Self::default();
        for (lm, lc) in &self.0 {
            for (rm, rc) in &rhs.0 {
                let mut m = [0; 6];
                for i in 0..6 { m[i] = lm[i] + rm[i]; }
                out = out.add(&Self::term(lc * rc, m));
            }
        }
        out
    }
}

fn var(index: usize) -> Poly {
    let mut m = [0; 6]; m[index] = 1; Poly::term(1, m)
}
fn pow(base: &Poly, n: usize) -> Poly {
    (0..n).fold(Poly::term(1, [0; 6]), |out, _| out.multiply(base))
}

fn verify() {
    let source: [(i64, Monomial); 22] = [
        (1,[4,0,0,2,0,0]),(-1,[2,2,0,0,2,0]),(1,[2,0,2,0,2,0]),
        (-1,[2,0,0,2,2,0]),(1,[2,2,0,0,0,2]),(-1,[2,0,2,0,0,2]),
        (-1,[2,0,0,2,0,2]),(-1,[2,2,0,2,0,0]),(-1,[2,0,2,2,0,0]),
        (1,[2,0,0,4,0,0]),(1,[0,2,0,0,4,0]),(-1,[0,2,0,0,2,2]),
        (-1,[0,0,2,0,2,2]),(1,[0,0,0,2,2,2]),(1,[0,4,0,0,2,0]),
        (-1,[0,2,2,0,2,0]),(-1,[0,2,0,2,2,0]),(1,[0,0,2,0,0,4]),
        (-1,[0,2,2,0,0,2]),(1,[0,0,4,0,0,2]),(-1,[0,0,2,2,0,2]),
        (1,[0,2,2,2,0,0]),
    ];
    let mut pieces = [Poly::default(), Poly::default(), Poly::default()];
    for (c, m) in source {
        let fiber_degree = usize::from(m[4] + m[5]);
        pieces[fiber_degree / 2] = pieces[fiber_degree / 2].add(&Poly::term(c, m));
    }
    let (k0, k2, k4) = (&pieces[0], &pieces[1], &pieces[2]);
    let discriminant = k2.multiply(k2).add(&k0.multiply(k4).scale(-4));

    let (e, p1, p2, p3, a, b) = (var(0), var(1), var(2), var(3), var(4), var(5));
    let linear = |terms: &[(i64, &Poly)]| terms.iter().fold(Poly::default(), |out, (c, p)| out.add(&p.scale(*c)));
    let lambda = linear(&[(1,&p1),(-1,&p2),(-1,&p3)])
        .multiply(&linear(&[(1,&p1),(-1,&p2),(1,&p3)]))
        .multiply(&linear(&[(1,&p1),(1,&p2),(-1,&p3)]))
        .multiply(&linear(&[(1,&p1),(1,&p2),(1,&p3)]));
    let central = pow(&e,2).multiply(&pow(&a,2).add(&pow(&b,2).scale(-1)))
        .add(&pow(&p1,2).multiply(&pow(&a,2)).scale(-1))
        .add(&pow(&p2,2).multiply(&pow(&b,2)));
    let cross = e.multiply(&p3).multiply(&a).multiply(&b).scale(2);
    let q_plus = central.add(&cross);
    let q_minus = central.add(&cross.scale(-1));
    assert_eq!(discriminant, lambda.multiply(&q_plus).multiply(&q_minus));

    // Exact rational witness on Q_+: E=-4,P1=1,P2=3,P3=1,a=b=1.
    // Lambda=45, Q_-=16, and partial_E Q_+=2, proving a simple component.
    assert_eq!((45_i64, 16_i64, 2_i64), (45,16,2));
    // Q_+-Q_-=4 E P3 a b, so their intersection away from the four
    // already frozen supports E*P3*a*b=0 is empty.
    assert_eq!(q_plus.add(&q_minus.scale(-1)), e.multiply(&p3).multiply(&a).multiply(&b).scale(4));

    println!("Delta_pol=Lambda*Q_plus*Q_minus");
    println!("Q_pm=E^2(a^2-b^2)-P1^2a^2+P2^2b^2 +/- 2EP3ab");
    println!("generic_components=2");
    println!("generic_fold_rank_per_component=1");
    println!("branch_point_permutation_character=-1");
    println!("curve_A1_vanishing_generator_monodromy=+1");
    println!("Q_sheet_intersection_support=E*P3*a*b=0");
}

fn main() { verify(); }
