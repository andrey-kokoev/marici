use std::{env, fs};

const ORDER: usize = 4;

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

    fn from(coefficients: [Rat; ORDER]) -> Self {
        Self(coefficients)
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

fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut exact_points = 0usize;
    let mut generic_nonzero = 0usize;

    for x in 1i128..=7 {
        for y in 1i128..=7 {
            for n in -6i128..=6 {
                let sum = x + y;
                let t = n * n * x * y;
                let k00 = 4 * x * y * (t - 2 * sum);
                if k00 == 0 {
                    continue;
                }

                // r-series of k0, k1, k2 and l2.
                let k0 = Series::from([
                    Rat::new(k00, 1),
                    Rat::ZERO,
                    Rat::new(8 * x * y * sum, 1),
                    Rat::ZERO,
                ]);
                let k_next = Series::from([
                    Rat::new(-4 * n * x * y * sum, 1),
                    Rat::new(-8 * n * x * y * sum, 1),
                    Rat::new(4 * n * x * y * sum, 1),
                    Rat::ZERO,
                ]);
                let k_second = Series::from([
                    Rat::new(5 * x * x + 14 * x * y + 5 * y * y, 1),
                    Rat::new(-8 * n * n * x * y * y - 4 * x * x + 4 * y * y, 1),
                    Rat::new(-2 * x * x - 8 * x * y - 2 * y * y, 1),
                    Rat::new(4 * x * x - 4 * y * y, 1),
                ]);
                let l0 = 16 * x * y * sum;
                let l1 = 8 * n * x * y * sum;
                let l_second = Series::from([
                    Rat::new(-12 * x * x - 32 * x * y - 12 * y * y, 1),
                    Rat::new(8 * x * x - 8 * y * y, 1),
                    Rat::new(4 * sum * sum, 1),
                    Rat::ZERO,
                ]);

                let inv_k0 = k0.inv();
                let normalized_k0_neg_three_halves = Series::from([
                    Rat::ONE,
                    Rat::ZERO,
                    Rat::new(-12 * x * y * sum, k00),
                    Rat::ZERO,
                ]);
                let k1_over_k0 = k_next.mul(inv_k0);
                let k2_over_k0 = k_second.mul(inv_k0);
                let a1 = Series::constant(Rat::new(l1, l0)).add(k1_over_k0.scale(-3, 2));
                let a2 = l_second
                    .scale(1, l0)
                    .add(k2_over_k0.scale(-3, 2))
                    .add(k1_over_k0.mul(k1_over_k0).scale(15, 8))
                    .add(k1_over_k0.scale(-3 * l1, 2 * l0));
                let m0 = normalized_k0_neg_three_halves.scale(-l0, 2);
                let m1 = m0.mul(a1);
                let m2 = m0.mul(a2);

                let d0 = [(-2, Rat::new(-n, 4 * x * y))];
                let d1 = [
                    (-3, Rat::new(-n * n, 4 * x * y)),
                    (-2, Rat::new(n * n, 4 * x * y)),
                ];
                let common = 8 * x * x * y * y;
                let d2 = [
                    (-4, Rat::new(-2 * n * n * n * x * y, common)),
                    (-3, Rat::new(2 * n * n * n * x * y, common)),
                    (-2, Rat::new(-n * (2 * n * n * x * y + x + y), common)),
                    (-1, Rat::new(-n * (-x + y), common)),
                ];

                let residue = laurent_residue(&d2, m0)
                    .add(laurent_residue(&d1, m1))
                    .add(laurent_residue(&d0, m2));
                let numerator = -12 * n * (x - y) * sum * (t - sum);
                let expected = Rat::new(numerator, k00);
                assert_eq!(residue, expected);

                if numerator != 0 {
                    generic_nonzero += 1;
                }
                assert_eq!(-12 * n * (x * x - y * y) * (t - sum), numerator);
                exact_points += 1;
            }
        }
    }
    assert!(generic_nonzero > 0);

    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.complete_unsplit_first_wall_class.v1\",\n",
            "  \"exact_laurent_reductions\": {},\n",
            "  \"generic_nonzero_cases\": {},\n",
            "  \"normalized_residue\": \"-12*n*(x-y)*(x+y)*(n^2*x*y-x-y)/k00\",\n",
            "  \"k00\": \"4*x*y*(n^2*x*y-2*x-2*y)\",\n",
            "  \"physical_branch_residue\": \"-3*n*(x-y)*(x+y)*(n^2*x*y-x-y)/(8*x^(5/2)*y^(5/2)*(n^2*x*y-2*x-2*y)^(5/2))\",\n",
            "  \"first_nonzero_grade\": -1,\n",
            "  \"residue_parity_in_n\": \"odd\",\n",
            "  \"symmetric_source_wall_pairing\": 0,\n",
            "  \"vanishing_subloci\": [\"n=0\",\"x=y\",\"n^2*x*y=x+y\"],\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        exact_points, generic_nonzero
    );
    fs::write(output, json).expect("write certificate");
}
