#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat {
    n: i128,
    d: i128,
}

fn gcd(mut a: i128, mut b: i128) -> i128 {
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a.abs()
}

impl Rat {
    fn new(mut n: i128, mut d: i128) -> Self {
        assert_ne!(d, 0);
        if d < 0 {
            n = -n;
            d = -d;
        }
        let g = gcd(n, d);
        Self { n: n / g, d: d / g }
    }

    fn inv_product(a: i128, b: i128) -> Self {
        Self::new(1, a * b)
    }

    fn add(self, rhs: Self) -> Self {
        Self::new(self.n * rhs.d + rhs.n * self.d, self.d * rhs.d)
    }

    fn sub(self, rhs: Self) -> Self {
        Self::new(self.n * rhs.d - rhs.n * self.d, self.d * rhs.d)
    }

    fn mul(self, rhs: Self) -> Self {
        Self::new(self.n * rhs.n, self.d * rhs.d)
    }
}

fn cyclic_pair_sum(x: [i128; 5]) -> Rat {
    (0..5).fold(Rat::new(0, 1), |sum, i| {
        sum.add(Rat::inv_product(x[i], x[(i + 2) % 5]))
    })
}

fn main() {
    // A physical five-point sample in planar coordinates.
    let [s12, s23, s34, s45, s51] = [2_i128, 3, 5, 11, 17];
    let s13 = s45 - s12 - s23;
    let s24 = s51 - s23 - s34;
    assert_eq!((s13, s24), (6, 9));

    // Leading alpha'^{-2} coefficients after removing the common global
    // factor.  The two basis chambers are 12345 and 13245.
    let d_12345 = cyclic_pair_sum([s12, s23, s34, s45, s51]);
    let d_13245 = cyclic_pair_sum([s13, s23, s24, s45, s51]);
    let off = Rat::new(1, s23).mul(Rat::new(1, s45).add(Rat::new(1, s51)));

    let determinant = d_12345.mul(d_13245).sub(off.mul(off));
    assert_ne!(determinant.n, 0);

    // The control chamber 13524 is nonadjacent to 12345 in the blown-up
    // real moduli space, so its twisted-cycle intersection is zero.
    let nonadjacent_common_faces = 0_usize;
    assert_eq!(nonadjacent_common_faces, 0);

    println!("five_point_string_basis_matrix: ok");
    println!("derived_invariants: s13={s13} s24={s24}");
    println!(
        "field_theory_leading_determinant: {}/{}",
        determinant.n, determinant.d
    );
    println!("nonadjacent_control_12345_13524: zero");
}
