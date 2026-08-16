use std::{env, fs};

const ORDER: usize = 6;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat {
    num: i128,
    den: i128,
}

impl Rat {
    const ZERO: Self = Self { num: 0, den: 1 };
    const ONE: Self = Self { num: 1, den: 1 };

    fn new(mut num: i128, mut den: i128) -> Self {
        assert_ne!(den, 0);
        if den < 0 {
            num = -num;
            den = -den;
        }
        let divisor = gcd(num.abs(), den);
        Self {
            num: num / divisor,
            den: den / divisor,
        }
    }

    fn add(self, other: Self) -> Self {
        Self::new(
            self.num * other.den + other.num * self.den,
            self.den * other.den,
        )
    }

    fn mul(self, other: Self) -> Self {
        Self::new(self.num * other.num, self.den * other.den)
    }

    fn scale(self, numerator: i128, denominator: i128) -> Self {
        self.mul(Self::new(numerator, denominator))
    }

    fn inv(self) -> Self {
        Self::new(self.den, self.num)
    }
}

fn gcd(mut left: i128, mut right: i128) -> i128 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left.max(1)
}

#[derive(Clone, Copy)]
struct Series([Rat; ORDER]);

impl Series {
    fn constant(value: Rat) -> Self {
        let mut coefficients = [Rat::ZERO; ORDER];
        coefficients[0] = value;
        Self(coefficients)
    }

    fn from_i128(coefficients: [i128; ORDER]) -> Self {
        Self(coefficients.map(|value| Rat::new(value, 1)))
    }

    fn add(self, other: Self) -> Self {
        Self(core::array::from_fn(|index| {
            self.0[index].add(other.0[index])
        }))
    }

    fn scale(self, numerator: i128, denominator: i128) -> Self {
        Self(self.0.map(|value| value.scale(numerator, denominator)))
    }

    fn mul(self, other: Self) -> Self {
        let mut coefficients = [Rat::ZERO; ORDER];
        for left in 0..ORDER {
            for right in 0..ORDER - left {
                coefficients[left + right] =
                    coefficients[left + right].add(self.0[left].mul(other.0[right]));
            }
        }
        Self(coefficients)
    }

    fn inv(self) -> Self {
        let mut result = [Rat::ZERO; ORDER];
        result[0] = self.0[0].inv();
        for degree in 1..ORDER {
            let mut sum = Rat::ZERO;
            for index in 1..=degree {
                sum = sum.add(self.0[index].mul(result[degree - index]));
            }
            result[degree] = sum.mul(result[0]).scale(-1, 1);
        }
        Self(result)
    }
}

fn laurent_residue(terms: &[(i32, Rat)], series: Series) -> Rat {
    let mut residue = Rat::ZERO;
    for (exponent, coefficient) in terms {
        let needed = -1 - exponent;
        if needed >= 0 && (needed as usize) < ORDER {
            residue = residue.add(coefficient.mul(series.0[needed as usize]));
        }
    }
    residue
}

fn residue_at(x: i128, y: i128, n: i128) -> Option<Rat> {
    let sum = x + y;
    let t = n * n * x * y;
    let k00 = 4 * x * y * (t - 2 * sum);
    if k00 == 0 {
        return None;
    }

    let k0 = Series::from_i128([k00, 0, 8 * x * y * sum, 0, 0, 0]);
    let k1 = Series::from_i128([
        -4 * n * x * y * sum,
        -8 * n * x * y * sum,
        4 * n * x * y * sum,
        0,
        0,
        0,
    ]);
    let k2 = Series::from_i128([
        5 * x * x + 14 * x * y + 5 * y * y,
        -8 * n * n * x * y * y - 4 * x * x + 4 * y * y,
        -2 * x * x - 8 * x * y - 2 * y * y,
        4 * x * x - 4 * y * y,
        sum * sum,
        0,
    ]);
    let k3 = Series::from_i128([
        4 * n * (n * n * x * y * y + x * x + x * y),
        4 * n * (2 * x * y + y * y),
        -4 * n * (x * x - x * y - 2 * y * y),
        -4 * n * (x * y + y * y),
        0,
        0,
    ]);
    let l0 = Series::constant(Rat::new(16 * x * y * sum, 1));
    let l1 = Series::constant(Rat::new(8 * n * x * y * sum, 1));
    let l2 = Series::from_i128([
        -12 * x * x - 32 * x * y - 12 * y * y,
        8 * x * x - 8 * y * y,
        4 * sum * sum,
        0,
        0,
        0,
    ]);
    let l3 = Series::from_i128([-8 * n * sum * x, -8 * n * sum * y, 0, 0, 0, 0]);

    let inv_k0 = k0.inv();
    let u1 = k1.mul(inv_k0);
    let u2 = k2.mul(inv_k0);
    let u3 = k3.mul(inv_k0);
    let b1 = u1.scale(-3, 2);
    let b2 = u2.scale(-3, 2).add(u1.mul(u1).scale(15, 8));
    let b3 = u3
        .scale(-3, 2)
        .add(u1.mul(u2).scale(15, 4))
        .add(u1.mul(u1).mul(u1).scale(-35, 16));

    let c_over_k00 = Rat::new(8 * x * y * sum, k00);
    let mut norm_coefficients = [Rat::ZERO; ORDER];
    norm_coefficients[0] = Rat::ONE;
    norm_coefficients[2] = c_over_k00.scale(-3, 2);
    norm_coefficients[4] = c_over_k00.mul(c_over_k00).scale(15, 8);
    let norm = Series(norm_coefficients);

    let m0 = norm.mul(l0).scale(-1, 2);
    let m1 = norm.mul(l1.add(l0.mul(b1))).scale(-1, 2);
    let m2 = norm.mul(l2.add(l1.mul(b1)).add(l0.mul(b2))).scale(-1, 2);
    let m3 = norm
        .mul(l3.add(l2.mul(b1)).add(l1.mul(b2)).add(l0.mul(b3)))
        .scale(-1, 2);

    let d0 = [(-2, Rat::new(-n, 4 * x * y))];
    let d1 = [
        (-3, Rat::new(-n * n, 4 * x * y)),
        (-2, Rat::new(n * n, 4 * x * y)),
    ];
    let common2 = 8 * x * x * y * y;
    let d2 = [
        (-4, Rat::new(-2 * n * n * n * x * y, common2)),
        (-3, Rat::new(2 * n * n * n * x * y, common2)),
        (-2, Rat::new(-n * (2 * n * n * x * y + x + y), common2)),
        (-1, Rat::new(n * (x - y), common2)),
    ];
    let d3 = [
        (-5, Rat::new(-2 * n.pow(4) * x * y, common2)),
        (-4, Rat::new(2 * n.pow(4) * x * y, common2)),
        (
            -3,
            Rat::new(-2 * n.pow(4) * x * y - n * n * (x + y), common2),
        ),
        (
            -2,
            Rat::new(2 * n.pow(4) * x * y + n * n * (2 * x + y), common2),
        ),
        (-1, Rat::new(n * n * (-x + y), common2)),
    ];

    Some(
        laurent_residue(&d3, m0)
            .add(laurent_residue(&d2, m1))
            .add(laurent_residue(&d1, m2))
            .add(laurent_residue(&d0, m3)),
    )
}
fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut exact_points = 0_u64;
    let mut nonzero_points = 0_u64;
    let mut formula_matches = 0_u64;
    let mut decomposition_matches = 0_u64;
    let mut even_pairs = 0_u64;
    let mut odd_pairs = 0_u64;
    let mut neither_pairs = 0_u64;

    for x in 1_i128..=9 {
        for y in 1_i128..=9 {
            let a = x * y;
            let sum = x + y;
            for n in -8_i128..=8 {
                let u = n * n;
                let v = a * u - 2 * sum;
                let bracket = a * a * u * u - 7 * a * sum * u + 5 * sum * sum;

                // Polynomial certificate for
                // core = (1/a) dn/w + d(n*P(u)/w^5),
                // where 6*a*P=-4*a^2*u^2+23*a*sum*u-24*sum^2.
                let p_scaled = -4 * a * a * u * u + 23 * a * sum * u - 24 * sum * sum;
                let p_scaled_plus_2u_derivative =
                    -20 * a * a * u * u + 69 * a * sum * u - 24 * sum * sum;
                let derivative_numerator = p_scaled_plus_2u_derivative * v - 5 * a * u * p_scaled;
                let adjusted_core_numerator = 6 * a * u * bracket - 6 * v * v * v;
                assert_eq!(derivative_numerator, adjusted_core_numerator);
                decomposition_matches += 1;

                let Some(value) = residue_at(x, y, n) else {
                    continue;
                };
                let expected = Rat::new(3 * u * (x - y) * sum * bracket, 2 * a * v * v);
                assert_eq!(value, expected);
                formula_matches += 1;
                if value != Rat::ZERO {
                    nonzero_points += 1;
                }
                exact_points += 1;
            }
            for n in 1_i128..=8 {
                let (Some(plus), Some(minus)) = (residue_at(x, y, n), residue_at(x, y, -n)) else {
                    continue;
                };
                if plus == minus {
                    even_pairs += 1;
                } else if plus == minus.scale(-1, 1) {
                    odd_pairs += 1;
                } else {
                    neither_pairs += 1;
                }
            }
        }
    }

    assert_eq!(formula_matches, exact_points);
    assert_eq!(odd_pairs, 0);
    assert_eq!(neither_pairs, 0);
    assert!(nonzero_points > 0);

    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.complete-unsplit-weight-zero.v1\",\n",
            "  \"exact_laurent_reductions\": {},\n",
            "  \"formula_matches\": {},\n",
            "  \"decomposition_matches\": {},\n",
            "  \"nonzero_points\": {},\n",
            "  \"even_n_pairs\": {},\n",
            "  \"odd_n_pairs\": {},\n",
            "  \"neither_parity_pairs\": {},\n",
            "  \"normalized_residue\": \"3*n^2*(x-y)*(x+y)*(n^4*x^2*y^2-7*n^2*x*y*(x+y)+5*(x+y)^2)/(2*x*y*(n^2*x*y-2*x-2*y)^2)\",\n",
            "  \"normalization\": \"k00^(3/2) times physical residue\",\n",
            "  \"wall_cover\": \"w^2=x*y*n^2-2*(x+y)\",\n",
            "  \"core_decomposition\": \"u*(a^2*u^2-7*a*s*u+5*s^2)*dn/w^7=(1/a)*dn/w+d(n*P(u)/w^5)\",\n",
            "  \"primitive_polynomial\": \"P(u)=(-4*a^2*u^2+23*a*s*u-24*s^2)/(6*a)\",\n",
            "  \"surviving_wall_class\": \"3*(x-y)*(x+y)/(16*(x*y)^(7/2))*[dn/w]\",\n",
            "  \"infinity_residues_nonzero_generic\": true,\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        exact_points,
        formula_matches,
        decomposition_matches,
        nonzero_points,
        even_pairs,
        odd_pairs,
        neither_pairs
    );
    fs::write(output, json).expect("write certificate");
}
