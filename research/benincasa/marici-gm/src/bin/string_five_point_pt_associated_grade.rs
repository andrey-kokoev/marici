#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat(i128, i128);

fn gcd(mut a: i128, mut b: i128) -> i128 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a.abs()
}

impl Rat {
    fn new(mut n: i128, mut d: i128) -> Self {
        assert_ne!(d, 0);
        if d < 0 { n = -n; d = -d; }
        let g = gcd(n, d);
        Self(n / g, d / g)
    }
    fn add(self, r: Self) -> Self { Self::new(self.0*r.1+r.0*self.1, self.1*r.1) }
    fn mul(self, r: Self) -> Self { Self::new(self.0*r.0, self.1*r.1) }
}

fn mat_mul(a: [[Rat; 2]; 2], b: [[Rat; 2]; 2]) -> [[Rat; 2]; 2] {
    let z = Rat::new(0, 1);
    let mut out = [[z; 2]; 2];
    for i in 0..2 { for j in 0..2 {
        out[i][j] = a[i][0].mul(b[0][j]).add(a[i][1].mul(b[1][j]));
    }}
    out
}

fn main() {
    let (s12, s23, s24, s35, s45) = (2_i128, 3, 9, -14, 11);
    let z = Rat::new(0, 1);

    // Leading periods of the source cycles against the two frozen
    // Parke--Taylor cocycles.  The support is diagonal by Entry 883.
    let p_source = [
        [Rat::new(1, s23*s45), z],
        [z, Rat::new(1, s24*s35)],
    ];

    // Field-theory associated grade of Entry 888's circuit.
    let circuit = [
        [Rat::new(-(s12+s23), s12), Rat::new(-s24, s12)],
        [Rat::new(-s23, s12), Rat::new(-(s12+s24), s12)],
    ];

    let transported = mat_mul(circuit, p_source);
    let p_target = [
        [Rat::new(-1, s12*s45).add(Rat::new(-1, s23*s45)), Rat::new(-1, s12*s35)],
        [Rat::new(-1, s12*s45), Rat::new(-1, s12*s35).add(Rat::new(-1, s24*s35))],
    ];
    assert_eq!(transported, p_target);

    println!("five_point_pt_associated_grade: ok");
    println!("transported_period_matrix: {transported:?}");
    println!("scope: alpha_prime_leading_associated_grade_only");
}
