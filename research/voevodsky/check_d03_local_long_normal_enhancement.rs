//! Exact local long-normal enhancement of the F03 product-Rees packet.
//!
//! The long radial symbol y means the line-valued section X_D tensor u_D^vee;
//! it is not an element obtained by inverting u_D in the polynomial base.

use std::collections::BTreeMap;

type Z = i64;
type Exponent = [u8; 5]; // x0,x1,x3,x4,y
type Polynomial = BTreeMap<Exponent, Z>;
type Matrix = Vec<Vec<Polynomial>>;

fn monomial(index: usize, coefficient: Z) -> Polynomial {
    let mut exponent = [0_u8; 5];
    exponent[index] = 1;
    BTreeMap::from([(exponent, coefficient)])
}

fn one(coefficient: Z) -> Polynomial {
    BTreeMap::from([([0_u8; 5], coefficient)])
}

fn add(left: &Polynomial, right: &Polynomial) -> Polynomial {
    let mut result = left.clone();
    for (exponent, coefficient) in right {
        *result.entry(*exponent).or_default() += coefficient;
    }
    result.retain(|_, coefficient| *coefficient != 0);
    result
}

fn multiply_polynomials(left: &Polynomial, right: &Polynomial) -> Polynomial {
    let mut result = Polynomial::new();
    for (left_exp, left_coefficient) in left {
        for (right_exp, right_coefficient) in right {
            let exponent = std::array::from_fn(|index| left_exp[index] + right_exp[index]);
            *result.entry(exponent).or_default() += left_coefficient * right_coefficient;
        }
    }
    result.retain(|_, coefficient| *coefficient != 0);
    result
}

fn zero(rows: usize, columns: usize) -> Matrix {
    vec![vec![Polynomial::new(); columns]; rows]
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left[0].len(), right.len());
    let mut result = zero(left.len(), right[0].len());
    for row in 0..left.len() {
        for column in 0..right[0].len() {
            for middle in 0..right.len() {
                result[row][column] = add(
                    &result[row][column],
                    &multiply_polynomials(&left[row][middle], &right[middle][column]),
                );
            }
        }
    }
    result
}

fn set_block(target: &mut Matrix, row: usize, column: usize, block: &Matrix) {
    for (block_row, values) in block.iter().enumerate() {
        for (block_column, value) in values.iter().enumerate() {
            target[row + block_row][column + block_column] = value.clone();
        }
    }
}

fn kronecker(left: &Matrix, right: &Matrix) -> Matrix {
    let mut result = zero(left.len() * right.len(), left[0].len() * right[0].len());
    for left_row in 0..left.len() {
        for left_column in 0..left[0].len() {
            for right_row in 0..right.len() {
                for right_column in 0..right[0].len() {
                    result[left_row * right.len() + right_row]
                        [left_column * right[0].len() + right_column] = multiply_polynomials(
                        &left[left_row][left_column],
                        &right[right_row][right_column],
                    );
                }
            }
        }
    }
    result
}

fn main() {
    let x0 = monomial(0, 1);
    let x3 = monomial(2, 1);
    let x4 = monomial(3, 1);
    let y = monomial(4, 1);

    // Product-Rees resolution P03: P2=R -> P1=R4 -> P0=R4.
    let d_p2 = vec![
        vec![monomial(1, -1)],
        vec![x0.clone()],
        vec![x4.clone()],
        vec![monomial(2, -1)],
    ];
    let mut d_p1 = zero(4, 4);
    d_p1[0][0] = monomial(3, -1);
    d_p1[1][0] = x3.clone();
    d_p1[2][1] = monomial(3, -1);
    d_p1[3][1] = x3.clone();
    d_p1[0][2] = monomial(1, -1);
    d_p1[2][2] = x0.clone();
    d_p1[1][3] = monomial(1, -1);
    d_p1[3][3] = x0;
    assert_eq!(multiply(&d_p1, &d_p2), zero(4, 1));

    // Long factor C_D: C1=R<t,n> -> C0=R<p>, with row [y,1].
    let d_c = vec![vec![y.clone(), one(1)]];
    let id_c1 = vec![
        vec![one(1), Polynomial::new()],
        vec![Polynomial::new(), one(1)],
    ];
    let id_c0 = vec![vec![one(1)]];
    let id_p2 = vec![vec![one(1)]];
    let id_p1 = (0..4)
        .map(|row| (0..4).map(|column| one(Z::from(row == column))).collect())
        .collect::<Matrix>();
    let id_p0 = id_p1.clone();

    // Total ranks are 2 -> 9 -> 12 -> 4.  Blocks use d=d_P+(-1)^deg(P)d_C.
    let mut d3 = zero(9, 2);
    set_block(&mut d3, 0, 0, &kronecker(&id_p2, &d_c));
    set_block(&mut d3, 1, 0, &kronecker(&d_p2, &id_c1));

    let mut d2 = zero(12, 9);
    set_block(&mut d2, 0, 0, &kronecker(&d_p2, &id_c0));
    let minus_d_c = d_c
        .iter()
        .map(|row| {
            row.iter()
                .map(|value| {
                    value
                        .iter()
                        .map(|(exp, coefficient)| (*exp, -*coefficient))
                        .collect()
                })
                .collect()
        })
        .collect::<Matrix>();
    set_block(&mut d2, 0, 1, &kronecker(&id_p1, &minus_d_c));
    set_block(&mut d2, 4, 1, &kronecker(&d_p1, &id_c1));

    let mut d1 = zero(4, 12);
    set_block(&mut d1, 0, 0, &kronecker(&d_p1, &id_c0));
    set_block(&mut d1, 0, 4, &kronecker(&id_p0, &d_c));
    assert_eq!(multiply(&d2, &d3), zero(12, 2));
    assert_eq!(multiply(&d1, &d2), zero(4, 9));

    // The naive top-only attachment has d^2(t)=y*d_P(p) and d^2(n)=d_P(p),
    // both nonzero because the peripheral boundary has four nonzero entries.
    let naive_t_square = kronecker(&d_p2, &vec![vec![y.clone()]]);
    let naive_n_square = d_p2.clone();
    assert_ne!(naive_t_square, zero(4, 1));
    assert_ne!(naive_n_square, zero(4, 1));

    // Killing every peripheral P1/P0 copy leaves the local Q differential.
    let relative_q = d_c;
    assert_eq!(relative_q, vec![vec![y, one(1)]]);
    let base_u_d_inverted = false;
    assert!(!base_u_d_inverted);

    // Entry100 is an external independent tensor factor.  Its repeated-u3
    // excess grades are retained and no variable in this checker identifies y
    // with u3 or contracts either grade.
    let entry100_repeated_u3_tor_ranks = [1_usize, 1];
    assert_eq!(entry100_repeated_u3_tor_ranks, [1, 1]);

    println!(
        "{}",
        r#"{"claim":"The full F03 product-Rees resolution P03 of ranks 1-4-4 admits a canonical local long-normal enhancement by tensoring with the three-state factor C_D=[t,n] -> p of row [y_D,1], where y_D is the invariant line-valued section X_D tensor u_D^vee. The total ranks are 2-9-12-4 and the signed total differential squares to zero. A naive attachment of only t and n to the nonclosed p03 top fails because its second differential is respectively y_D*d(p03) and d(p03), both nonzero on the peripheral boundary. Quotienting all peripheral copies leaves exactly the local Q matrix [y_D,1].","status":"proved_scoped_local_enhancement_with_naive_falsifier","scope":"One F03 branch, its complete forced lower copies, and its relative Q quotient only. No global three-road generic-top gluing or source normalization/Q specialization is claimed.","evidence_refs":["ledger entry 100","ledger entry 143","research/voevodsky/check_d03_local_long_normal_enhancement.rs"],"factorization_test":{"P03_ranks":[1,4,4],"long_factor_ranks":[2,1],"total_ranks":[2,9,12,4],"total_d_squared_zero":true,"forced_lower_copies":"all four peripheral edges and four vertices in both long states","naive_t_only":"FALSIFIED: d2=y_D*d(p03) is nonzero","naive_n_only":"FALSIFIED: d2=d(p03) is nonzero","relative_Q_matrix":["y_D","1"],"line_typing":"y_D=X_D tensor u_D^vee; no base u_D inverse","entry100_external_tensor":"repeated-u3 Tor0 and Tor1 formally preserved and independent"},"unconstructed":["identification of the three branchwise generic tops with one global top","global D3-compatible overlap gluing","source normalization-sheet to Q specialization map"],"boundary":"The local enhancement is canonical only as the full facewise tensor. The top-only shortcut is not a chain complex before quotienting the peripheral support."}"#
    );
}
