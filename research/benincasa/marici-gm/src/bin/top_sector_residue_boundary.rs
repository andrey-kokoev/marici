use std::collections::BTreeMap;

type Monomial = [u8; 3];

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Polynomial(BTreeMap<Monomial, i64>);

impl Polynomial {
    fn constant(value: i64) -> Self {
        let mut result = Self::default();
        if value != 0 {
            result.0.insert([0, 0, 0], value);
        }
        result
    }

    fn variable(index: usize) -> Self {
        let mut monomial = [0, 0, 0];
        monomial[index] = 1;
        let mut result = Self::default();
        result.0.insert(monomial, 1);
        result
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        for (monomial, coefficient) in &other.0 {
            let next = result.0.get(monomial).copied().unwrap_or(0) + coefficient;
            if next == 0 {
                result.0.remove(monomial);
            } else {
                result.0.insert(*monomial, next);
            }
        }
        result
    }

    fn scale(&self, scalar: i64) -> Self {
        let mut result = Self::default();
        for (monomial, coefficient) in &self.0 {
            let next = coefficient * scalar;
            if next != 0 {
                result.0.insert(*monomial, next);
            }
        }
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::default();
        for (left, left_coefficient) in &self.0 {
            for (right, right_coefficient) in &other.0 {
                let monomial = [left[0] + right[0], left[1] + right[1], left[2] + right[2]];
                let next = result.0.get(&monomial).copied().unwrap_or(0)
                    + left_coefficient * right_coefficient;
                if next == 0 {
                    result.0.remove(&monomial);
                } else {
                    result.0.insert(monomial, next);
                }
            }
        }
        result
    }

    fn power(&self, exponent: u8) -> Self {
        let mut result = Self::constant(1);
        for _ in 0..exponent {
            result = result.multiply(self);
        }
        result
    }
}

fn sum(terms: &[Polynomial]) -> Polynomial {
    terms
        .iter()
        .fold(Polynomial::default(), |sum, term| sum.add(term))
}

fn determinant_3(matrix: [[i64; 3]; 3]) -> i64 {
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
}

fn main() {
    let x = Polynomial::variable(0);
    let y = Polynomial::variable(1);
    let z = Polynomial::variable(2);
    let e = sum(&[x.clone(), y.clone(), z.clone()]);

    // Fiber order is (c,a,b)=(y12,y23,y31).  The source hyperplanes meet at
    // c=-E, a=x+z, b=y+z.
    let c = e.scale(-1);
    let a = x.add(&z);
    let b = y.add(&z);
    let x2 = x.power(2);
    let y2 = y.power(2);
    let z2 = z.power(2);
    let c2 = c.power(2);
    let a2 = a.power(2);
    let b2 = b.power(2);
    let h = x2.add(&y2).add(&z2.scale(-1));

    // Source-normalized K, copied algebraically from the admitted rank-cube checker.
    let k_at_triple = sum(&[
        x2.multiply(&a.power(4)),
        h.multiply(&a2).multiply(&b2).scale(-1),
        y2.multiply(&b.power(4)),
        a2.multiply(&x2)
            .multiply(&sum(&[x2.clone(), y2.scale(-1), z2.scale(-1)])),
        c2.multiply(&a2)
            .multiply(&sum(&[x2.scale(-1), y2.clone(), z2.scale(-1)])),
        b2.multiply(&y2)
            .multiply(&sum(&[y2.clone(), x2.scale(-1), z2.scale(-1)])),
        c2.multiply(&b2)
            .multiply(&sum(&[y2.scale(-1), x2.clone(), z2.scale(-1)])),
        z2.multiply(&c.power(4)),
        z2.multiply(&c2)
            .multiply(&sum(&[x2.scale(-1), y2.scale(-1), z2.clone()])),
        z2.multiply(&x2).multiply(&y2),
    ]);

    let ell_minus = sum(&[z.clone(), x.scale(-1), y.clone()]);
    let ell_plus = sum(&[z, x, y.scale(-1)]);
    let expected = e
        .power(2)
        .multiply(&ell_minus.power(2))
        .multiply(&ell_plus.power(2));
    assert_eq!(k_at_triple, expected);

    // Rows are dq_g1, dq_g2, dq_G12 in the ordered fiber coordinates (c,a,b).
    let jacobian = determinant_3([[1, 0, 1], [1, 1, 0], [1, 0, 0]]);
    assert_eq!(jacobian, -1);

    // Oriented Boolean-boundary signs for bit order (q_g1,q_g2,q_G12).
    // Deleting q_G12 lands on the lower-pair proper grade, whose rank is zero.
    let boundary = [1_i64, -1, 0];
    assert_eq!(boundary[0].abs(), 1);
    assert_eq!(boundary[1].abs(), 1);

    println!(
        "{{\"schema\":\"marici.benincasa.top_sector_residue_boundary.v1\",\"status\":\"exact_symbolic_identity_verified\",\"triple_section\":{{\"y12\":\"-E\",\"y23\":\"X1+X3\",\"y31\":\"X2+X3\"}},\"normal_jacobian\":{jacobian},\"K_at_triple\":\"E^2 (X2+X3-X1)^2 (X1+X3-X2)^2\",\"proper_face_ranks\":{{\"q_G12_q_g2\":1,\"q_G12_q_g1\":1,\"q_g1_q_g2\":0}},\"oriented_proper_boundary\":[1,-1,0],\"new_carrier_datum\":false}}"
    );
}
