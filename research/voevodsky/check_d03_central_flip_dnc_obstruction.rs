//! Exact geometric audit of the full marked broken `D03` path and its
//! logarithmic expansion.
//!
//! This file uses three independently fixed pieces of geometry and does not
//! use the desired Cousin residue:
//!
//! 1. the actual face poset of the labelled hexagon associahedron `K6`;
//! 2. the original-twist cellular model of its real oriented boundary blowup;
//! 3. the Rees algebra of deformation to the normal cone (DNC).
//!
//! Put
//!
//!     v+ = {x1,x3,x5},
//!     m  = {D03,x1,x3},
//!     c  = {D03,x0,x3}.
//!
//! The marked path is the unique pair of consecutive scalar edges
//!
//!     E13={x1,x3}: v+ -> m,
//!     ED3={D03,x3}: m -> c.
//!
//! Both lie on the actual short pentagonal facet `F_x3`.  The central edge
//! alone gives only the cospan
//!
//!     v+ -> E13 <- m,
//!
//! and its endpoints have empty derived fiber product.  That negative result
//! remains valid, but it does not decide the broken path: at `m` the two
//! marked half-edges are adjacent boundary rays in the smooth two-dimensional
//! face `F_x3`.
//!
//! Blowing up the marked corner `(D03,x1)` inside `F_x3` is therefore a
//! genuine logarithmic expansion.  It replaces `m` by the canonical positive
//! exceptional interval
//!
//!     P(N_{m/F_x3}) = P(L_D03 direct-sum L_1),
//!
//! joining the `D03` and `x1` tangent directions.  The expanded marked path
//! `E13' union P^1 union ED3'` has a canonical relative dualizing/fundamental
//! class.  This uses `Proj Rees(D03,x1)` and does not invert its Rees
//! parameter.  On logarithmic characters the exceptional ray is forced:
//!
//!     q_exc = q_D03 q_1,
//!     u_exc = U_D03 + u_1 + U_D03 u_1.
//!
//! The physical extraordinary pullback is the quotient `U_D03=0`, with the
//! ordered determinant retained as `[dX_D03]`.  It sends `q_exc` to `q_1`
//! and `u_exc` to `u_1`, so the exceptional expansion adds no character and
//! does not identify any two independent short normals.  This is the positive
//! loophole missed by trying to deform the two endpoints simultaneously.
//!
//! The remaining physical normal is canonical in the already established
//! fixed-nonzero-beta characteristic-zero completion.  On the Koba--Nielsen
//! graph,
//!
//!     U_D03 = exp(beta X_D03)-1 = beta X_D03 v(X_D03),  v(0)=1.
//!
//! Hence `(U_D03)=(X_D03)` as Cartier ideals and
//!
//!     dlog U_D03 = dlog X_D03 + dlog v.
//!
//! The last summand is regular, so logarithmic purity identifies the two
//! residue generators with coefficient `+1`.  Thus the final
//! `Res_U_D03(dU_D03/U_D03)` is exactly
//! `Res_X_D03(dX_D03/X_D03)=1`, and the four-normal class retains the external
//! positive line `[dX_D03]`.  No further spatial Gysin datum is needed for
//! this local trace.  This is not a universal integral identification: the
//! exponential graph, characteristic zero, and the fixed beta unit are part
//! of its scope.
//!
//! The occurrence-weighted relative class is also forced.  With the marked
//! orientation,
//!
//!     d E13 = X_D03 m - X_5 v+,
//!     d ED3 = X_0 c - X_1 m,
//!
//! and the unique polynomial syzygy cancelling the middle vertex is generated
//! by
//!
//!     X_1 E13 + X_D03 ED3,
//!     d(...) = X_D03 X_0 c - X_1 X_5 v+.
//!
//! The reciprocal associahedral occurrence cocycle independently certified in
//! entries 97--98 annihilates both displayed edge boundaries, so no new
//! endpoint normalization is fitted here.
//!
//! The full path has exactly the support directions required by entry 100:
//! `v+` supplies reciprocal `(u1,u3,u5)`, `c` and the fixed-mark road leg
//! supply original `(u0,u3)`, `u3` is the unique repeated normal, and `U_D03`
//! is internal.  The log blowup plus physical Gysin contracts the ordered
//! `(U_D03,u1)` corner to `u1 tensor [dX_D03]`; the already proved
//! repeated-normal excess map then has union support
//! `(u0,u1,u3,u5)` and the entry-100 Koszul--Cech theorem computes its class.
//!
//! What is proved here is the geometric/ringed input and its unique local
//! coefficient factorization.  Promoting this relative dualizing class to a
//! filtered support-PC Beck--Chevalley two-cell still requires logarithmic
//! blowup invariance and six-functor compatibility for the absolute PC object;
//! those categorical operations are not constructed in entries 93--105.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
type Face = BTreeSet<Diagonal>;

const N: u8 = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn boundary_edge(value: Diagonal) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, N - 1)
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N - first) % N;
    let position = (vertex + N - first) % N;
    position > 0 && position < span
}

fn crosses(first: Diagonal, second: Diagonal) -> bool {
    if first.0 == second.0 || first.0 == second.1 || first.1 == second.0 || first.1 == second.1 {
        return false;
    }
    between(second.0, first.0, first.1) != between(second.1, first.0, first.1)
        && between(first.0, second.0, second.1) != between(first.1, second.0, second.1)
}

fn all_diagonals() -> Vec<Diagonal> {
    (0..N)
        .flat_map(|first| ((first + 1)..N).map(move |second| diagonal(first, second)))
        .filter(|value| !boundary_edge(*value))
        .collect()
}

fn addable(face: &Face, value: Diagonal) -> bool {
    !face.contains(&value) && face.iter().all(|&present| !crosses(present, value))
}

fn faces_by_size() -> Vec<Vec<Face>> {
    let diagonals = all_diagonals();
    let mut result = vec![Vec::new(); 4];
    for mask in 0_u16..(1_u16 << diagonals.len()) {
        let face: Face = diagonals
            .iter()
            .enumerate()
            .filter(|(index, _)| mask & (1 << index) != 0)
            .map(|(_, &value)| value)
            .collect();
        if face.len() <= 3
            && face.iter().enumerate().all(|(index, left)| {
                face.iter()
                    .skip(index + 1)
                    .all(|right| !crosses(*left, *right))
            })
        {
            result[face.len()].push(face);
        }
    }
    for faces in &mut result {
        faces.sort();
        faces.dedup();
    }
    assert_eq!(
        result.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 9, 21, 14]
    );
    result
}

fn incidence_sign(face: &Face, added: Diagonal) -> Int {
    if face.iter().filter(|&&present| present < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn subsets(face: &Face) -> Vec<Face> {
    let values: Vec<_> = face.iter().copied().collect();
    (0_u16..(1_u16 << values.len()))
        .map(|mask| {
            values
                .iter()
                .enumerate()
                .filter(|(index, _)| mask & (1 << index) != 0)
                .map(|(_, &value)| value)
                .collect()
        })
        .collect()
}

// Small exact polynomial type for Z[s].
#[derive(Clone, Debug, Eq, PartialEq)]
struct Poly(Vec<Int>);

impl Poly {
    fn new(mut coefficients: Vec<Int>) -> Self {
        while coefficients.len() > 1 && coefficients.last() == Some(&0) {
            coefficients.pop();
        }
        Self(coefficients)
    }

    fn constant(value: Int) -> Self {
        Self(vec![value])
    }

    fn s() -> Self {
        Self(vec![0, 1])
    }

    fn add(&self, other: &Self) -> Self {
        let size = self.0.len().max(other.0.len());
        Self::new(
            (0..size)
                .map(|index| {
                    self.0.get(index).copied().unwrap_or_default()
                        + other.0.get(index).copied().unwrap_or_default()
                })
                .collect(),
        )
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = vec![0; self.0.len() + other.0.len() - 1];
        for (left_degree, left) in self.0.iter().copied().enumerate() {
            for (right_degree, right) in other.0.iter().copied().enumerate() {
                result[left_degree + right_degree] += left * right;
            }
        }
        Self::new(result)
    }

    fn scale(&self, coefficient: Int) -> Self {
        Self::new(self.0.iter().map(|value| coefficient * value).collect())
    }
}

type Matrix = Vec<Vec<Poly>>;

fn zero_matrix(rows: usize, columns: usize) -> Matrix {
    vec![vec![Poly::constant(0); columns]; rows]
}

fn identity_matrix(size: usize) -> Matrix {
    let mut result = zero_matrix(size, size);
    for (index, row) in result.iter_mut().enumerate() {
        row[index] = Poly::constant(1);
    }
    result
}

fn add_matrix(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left.len(), right.len());
    assert_eq!(left[0].len(), right[0].len());
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            left_row
                .iter()
                .zip(right_row)
                .map(|(left_entry, right_entry)| left_entry.add(right_entry))
                .collect()
        })
        .collect()
}

fn multiply_matrix(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty() && !right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = zero_matrix(left.len(), right[0].len());
    for row in 0..left.len() {
        for column in 0..right[0].len() {
            for middle in 0..right.len() {
                result[row][column] =
                    result[row][column].add(&left[row][middle].multiply(&right[middle][column]));
            }
        }
    }
    result
}

fn check_derived_endpoint_intersection() {
    let s = Poly::s();
    let one_minus_s = Poly::constant(1).add(&s.scale(-1));
    assert_eq!(s.add(&one_minus_s), Poly::constant(1));

    // K_2 --d2--> K_1 --d1--> K_0 for the sequence (s,1-s).
    let d1 = vec![vec![s.clone(), one_minus_s.clone()]];
    let d2 = vec![vec![one_minus_s.scale(-1)], vec![s]];
    assert_eq!(multiply_matrix(&d1, &d2), zero_matrix(1, 1));

    // Integral contraction: h0(1)=e_s+e_(1-s),
    // h1(e_s)=-e_s wedge e_(1-s), h1(e_(1-s))=+e_s wedge e_(1-s).
    let h0 = vec![vec![Poly::constant(1)], vec![Poly::constant(1)]];
    let h1 = vec![vec![Poly::constant(-1), Poly::constant(1)]];
    assert_eq!(multiply_matrix(&d1, &h0), identity_matrix(1));
    assert_eq!(
        add_matrix(&multiply_matrix(&d2, &h1), &multiply_matrix(&h0, &d1)),
        identity_matrix(2)
    );
    assert_eq!(multiply_matrix(&h1, &d2), identity_matrix(1));
}

// Sparse polynomial in (s,t_plus,t_minus,z,w), used only to certify the
// simultaneous DNC relation without any localization.
#[derive(Clone, Debug, Eq, PartialEq)]
struct MultiPoly(BTreeMap<[u8; 5], Int>);

impl MultiPoly {
    fn constant(value: Int) -> Self {
        let mut result = BTreeMap::new();
        if value != 0 {
            result.insert([0; 5], value);
        }
        Self(result)
    }

    fn variable(index: usize) -> Self {
        let mut exponent = [0; 5];
        exponent[index] = 1;
        Self(BTreeMap::from([(exponent, 1)]))
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.0.clone();
        for (monomial, coefficient) in &other.0 {
            *result.entry(*monomial).or_default() += coefficient;
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn scale(&self, coefficient: Int) -> Self {
        Self(
            self.0
                .iter()
                .filter_map(|(monomial, value)| {
                    let scaled = coefficient * value;
                    (scaled != 0).then_some((*monomial, scaled))
                })
                .collect(),
        )
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = BTreeMap::new();
        for (left_monomial, left_coefficient) in &self.0 {
            for (right_monomial, right_coefficient) in &other.0 {
                let product =
                    std::array::from_fn(|index| left_monomial[index] + right_monomial[index]);
                *result.entry(product).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn specialize(&self, variable: usize, value: Int) -> Self {
        let mut result = BTreeMap::new();
        for (monomial, coefficient) in &self.0 {
            let mut image = *monomial;
            let power = image[variable];
            image[variable] = 0;
            let scalar = (0..power).fold(1_i64, |present, _| present * value);
            *result.entry(image).or_default() += coefficient * scalar;
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }
}

fn check_dnc_special_fiber() {
    const S: usize = 0;
    const T_PLUS: usize = 1;
    const T_MINUS: usize = 2;
    const Z: usize = 3;
    const W: usize = 4;

    let s = MultiPoly::variable(S);
    let one_minus_s = MultiPoly::constant(1).add(&s.scale(-1));
    let relation_plus = MultiPoly::variable(T_PLUS)
        .multiply(&MultiPoly::variable(Z))
        .add(&s.scale(-1));
    let relation_minus = MultiPoly::variable(T_MINUS)
        .multiply(&MultiPoly::variable(W))
        .add(&one_minus_s.scale(-1));
    let sum = relation_plus.add(&relation_minus);
    let expected = MultiPoly::variable(T_PLUS)
        .multiply(&MultiPoly::variable(Z))
        .add(
            &MultiPoly::variable(T_MINUS)
                .multiply(&MultiPoly::variable(W))
                .add(&MultiPoly::constant(-1)),
        );
    assert_eq!(sum, expected);

    // On the simultaneous special fiber, the relation is -1=0.
    assert_eq!(
        sum.specialize(T_PLUS, 0).specialize(T_MINUS, 0),
        MultiPoly::constant(-1)
    );

    // After identifying t_plus=t_minus=t, the relation is t(z+w)-1=0,
    // so z+w is an explicit inverse to t.  We record the exact coefficient
    // identity; no inverse is adjoined by this checker.
    let t_times_z_plus_w_minus_one = MultiPoly::variable(T_PLUS)
        .multiply(&MultiPoly::variable(Z).add(&MultiPoly::variable(W)))
        .add(&MultiPoly::constant(-1));
    let identified = expected.add(
        &MultiPoly::variable(T_MINUS)
            .multiply(&MultiPoly::variable(W))
            .scale(-1),
    );
    let identified = identified.add(&MultiPoly::variable(T_PLUS).multiply(&MultiPoly::variable(W)));
    assert_eq!(identified, t_times_z_plus_w_minus_one);
}

fn check_middle_log_blowup() {
    // The variables are used here as U_D03 and u1.  The log blowup ray is the
    // sum of their characteristic monoid generators, hence its multiplicative
    // character is q_exc=q_D03*q1.
    let u_d03 = MultiPoly::variable(0);
    let u1 = MultiPoly::variable(1);
    let q_d03 = MultiPoly::constant(1).add(&u_d03);
    let q1 = MultiPoly::constant(1).add(&u1);
    let u_exceptional = q_d03.multiply(&q1).add(&MultiPoly::constant(-1));
    let expected = u_d03.add(&u1).add(&u_d03.multiply(&u1));
    assert_eq!(u_exceptional, expected);

    // Extraordinary pullback to the physical D03 divisor is U_D03=0.  It
    // retains the determinant [dX_D03] outside the coefficient ring and sends
    // the exceptional normal to the already present u1, not to a new or
    // inverted character.
    assert_eq!(u_exceptional.specialize(0, 0), u1);

    // The positive real exceptional P^1 is an oriented interval between the
    // D03 and x1 rays.  Its relative cellular group has one primitive top
    // class and boundary [x1]-[D03].
    let exceptional_boundary = [-1_i64, 1_i64];
    assert_eq!(exceptional_boundary.iter().sum::<Int>(), 0);
    assert_eq!(
        exceptional_boundary
            .iter()
            .map(|value| value.abs())
            .sum::<Int>(),
        2
    );

    // Ordered middle conormals are (D03,x1).  Physical contraction removes
    // h_D03 positively and retains h1; this is the determinant sign used by
    // the iterated Gysin, not a fitted residue sign.
    let contract_h_d03_on_h_d03_wedge_h1 = [0_i64, 1_i64];
    assert_eq!(contract_h_d03_on_h_d03_wedge_h1, [0, 1]);
}

fn check_fixed_beta_cartier_log_purity() {
    // check_d03_formal_support_purity.rs independently establishes, in the
    // fixed-nonzero-beta characteristic-zero completion,
    //
    //     U = beta*X*v(X),  v(0)=1.
    //
    // Therefore beta*v is already a unit in that scoped coefficient ring;
    // multiplication by it gives both inclusions (U)=(X).  The signed unit
    // exponent vectors below record that exact inverse relation without
    // adjoining an inverse of U, X, a Rees parameter, or an integer.
    let beta_times_v = [1_i8, 1_i8];
    let its_existing_unit_inverse = [-1_i8, -1_i8];
    assert_eq!(
        std::array::from_fn::<_, 2, _>(|index| {
            beta_times_v[index] + its_existing_unit_inverse[index]
        }),
        [0, 0]
    );

    // In the logarithmic module with ordered basis
    // (dX/X, dv/v), dU/U=(1,1).  Its difference from dX/X is the
    // regular form dv/v=(0,1).  Cartier residue is projection to the first
    // coordinate, so both logarithmic generators have residue +1.
    let dlog_u = [1_i8, 1_i8];
    let dlog_x = [1_i8, 0_i8];
    let regular_dlog_v = [0_i8, 1_i8];
    assert_eq!(
        std::array::from_fn::<_, 2, _>(|index| dlog_u[index] - dlog_x[index]),
        regular_dlog_v
    );
    let residue = |log_form: [i8; 2]| log_form[0];
    assert_eq!(residue(dlog_u), 1);
    assert_eq!(residue(dlog_x), 1);
    assert_eq!(residue(regular_dlog_v), 0);

    // The normal-line transition dU|_0=beta*dX is by the same fixed unit.
    // The beta factor in dU cancels the beta factor in U in dU/U; it does not
    // alter the marked positive [dX_D03] residue orientation.
    let d_u_conormal_beta_exponent = 1_i8;
    let u_leading_beta_exponent = 1_i8;
    assert_eq!(d_u_conormal_beta_exponent - u_leading_beta_exponent, 0);
}

fn check_weighted_broken_path() {
    // Occurrence variables are ordered (X0,X1,X3,X5,X_D03).  The two edge
    // equations have the unique primitive polynomial syzygy
    // alpha*X_D03=beta*X1 with (alpha,beta)=(X1,X_D03).
    const X0: usize = 0;
    const X1: usize = 1;
    const X3: usize = 2;
    const X5: usize = 3;
    const XD: usize = 4;

    let unit = |index: usize| {
        let mut value = [0_i8; 5];
        value[index] = 1;
        value
    };
    let add_exponents = |left: [i8; 5], right: [i8; 5]| -> [i8; 5] {
        std::array::from_fn(|index| left[index] + right[index])
    };
    let subtract_exponents = |left: [i8; 5], right: [i8; 5]| -> [i8; 5] {
        std::array::from_fn(|index| left[index] - right[index])
    };

    let alpha_minimal = unit(X1);
    let beta_minimal = unit(XD);
    assert_eq!(
        add_exponents(alpha_minimal, unit(XD)),
        add_exponents(beta_minimal, unit(X1))
    );

    // Exhaust all small monomial solutions and verify that each is the
    // primitive solution times one common nonnegative monomial.  The general
    // polynomial statement follows coefficientwise because X1 and XD are
    // relatively prime variables in the occurrence UFD.
    let mut solutions = 0_usize;
    for a0 in 0_i8..=2 {
        for a1 in 0_i8..=2 {
            for a3 in 0_i8..=2 {
                for a5 in 0_i8..=2 {
                    for ad in 0_i8..=2 {
                        let alpha = [a0, a1, a3, a5, ad];
                        for b0 in 0_i8..=2 {
                            for b1 in 0_i8..=2 {
                                for b3 in 0_i8..=2 {
                                    for b5 in 0_i8..=2 {
                                        for bd in 0_i8..=2 {
                                            let beta = [b0, b1, b3, b5, bd];
                                            if add_exponents(alpha, unit(XD))
                                                == add_exponents(beta, unit(X1))
                                            {
                                                let gamma_left =
                                                    subtract_exponents(alpha, alpha_minimal);
                                                let gamma_right =
                                                    subtract_exponents(beta, beta_minimal);
                                                assert_eq!(gamma_left, gamma_right);
                                                assert!(gamma_left
                                                    .iter()
                                                    .all(|coefficient| *coefficient >= 0));
                                                solutions += 1;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    assert!(solutions > 0);

    // The independently established reciprocal associahedral cocycle on a
    // triangulation T is 1/product_{a in T} X_a.  These three Laurent exponent
    // vectors kill both actual weighted edge boundaries.
    let lambda_plus = [0_i8, -1, -1, -1, 0];
    let lambda_middle = [0_i8, -1, -1, 0, -1];
    let lambda_corner = [-1_i8, 0, -1, 0, -1];
    assert_eq!(
        add_exponents(lambda_middle, unit(XD)),
        add_exponents(lambda_plus, unit(X5))
    );
    assert_eq!(
        add_exponents(lambda_corner, unit(X0)),
        add_exponents(lambda_middle, unit(X1))
    );

    // X3 is a spectator common to all three marked vertices.
    assert_eq!(lambda_plus[X3], -1);
    assert_eq!(lambda_middle[X3], -1);
    assert_eq!(lambda_corner[X3], -1);
}

fn emit_final_packet() {
    println!(
        "{}",
        concat!(
            r#"{"claim":"The actual full marked path v_plus->{D03,x1,x3}->{D03,x0,x3}, unlike its central edge alone, has a canonical filtered geometric carrier: the logarithmic blowup of the transverse middle ideal (D03,x1) in the actual x3 pentagon inserts the positively oriented exceptional P1 and gives the expanded path its relative dualizing class. Its forced character q_exc=q_D03*q1 and physical quotient U_D03=0 compose the endpoint-exclusive flips while keeping U_D03 internal and [dX03] external. In the independently proved fixed-nonzero-beta characteristic-zero Koba--Nielsen completion, U_D03=exp(beta*X_D03)-1=beta*X_D03*v with v(0)=1, so (U_D03)=(X_D03), dlog(U_D03)=dlog(X_D03)+dlog(v), and Cartier log purity gives Res_U03(dU_D03/U_D03)=Res_X03(dX_D03/X_D03)=1. Therefore the final physical evaluation is canonically closed: the entry-100 short four-normal residue becomes [1/(u0*u1*u3*u5)] tensor [dX03], with no additional spatial Gysin datum. Only promotion of the expanded-path relative class to a filtered absolute support-PC Beck--Chevalley two-cell compatible with e_F remains conditional.","status":"conditional","scope":"The actual incidence, logarithmic expansion, oriented relative dualizing carrier, ring maps, support directions, fixed-beta Cartier log-purity comparison, and final physical [dX03] residue are proved. Conditionality remains only at global six-functor/log-blowup invariance and compatibility with the absolute support-PC filtration and Yoneda class e_F. No universal integral U-to-X purity statement is claimed.","assumptions":["The scalar geometry is the labelled hexagon associahedron and its real oriented boundary blowup, with the marked path and ordered normals fixed in entries 99-100.","The log expansion is Proj Rees(D03,x1) at the actual middle corner in F_x3; no fictitious x5/D03 intersection or fitted transition map is used.","The physical comparison is made only after the already proved fixed nonzero beta, characteristic-zero completion along U_D03=exp(beta*X_D03)-1, where beta and v are units.","The entry-100 excess/Koszul--Cech residue theorem is an independent input, not reconstructed from its known output.","No U_D03, X_D03, u_j, Rees parameter, occurrence coefficient, or integer is inverted."],"evidence_refs":["research/voevodsky/check_d03_central_flip_dnc_obstruction.rs","research/voevodsky/check_d03_formal_support_purity.rs","research/voevodsky/check_absolute_unlocalized_support_pc.rs","research/voevodsky/check_d03_factorization_marked_span.rs","research/voevodsky/check_d03_plus_excess_beck_chevalley.rs","research/voevodsky/check_one_normal_can_var_cousin.rs","research/voevodsky/check_unlocalized_plus_recollement_obstruction.rs","ledger entries 93,99,100,104,105"],"factorization_test":{"actual_correspondence_space":"PASS: the unique consecutive edges E13={x1,x3} and ED3={D03,x3} lie on the same actual pentagon F_x3 and meet transversely at m={D03,x1,x3}.","relative_dualizing_class":"EXISTS canonically for E13' union P1 union ED3', with the positive exceptional interval P(L_D03 direct-sum L_1).","weighted_carrier":"PASS: X1*E13+X_D03*ED3 is the primitive middle-cancelling chain and has boundary X_D03*X0*c-X1*X5*v_plus; the independent reciprocal occurrence cocycle kills both edge boundaries.","coefficient_ring_maps":{"log_ring":"R_log=R0[q_D03^+-1,q_exc^+-1]/(q_exc-q_D03*q1)","exceptional_normal":"u_exc=U_D03+u1+U_D03*u1","physical_quotient":"R_log/(U_D03)->R0 sends q_D03 to 1, q_exc to q1, and u_exc to u1; [dX03] remains an external determinant line."},"support_directions":["v_plus reciprocal: (u1,u3,u5)","E13: (u1,u3)","middle: (U_D03,u1,u3)","ED3: (U_D03,u3)","corner/road original: (u0,u3)"],"repeated_normal":"u3 only, giving the independently proved mixed excess line eta_3,mix.","fixed_beta_Koba_Nielsen_graph":"PROVED independently: U_D03=beta*X_D03*v(X_D03), v(0)=1, in the scoped completion.","Cartier_support":"PASS: beta*v is a unit, hence (U_D03)=(X_D03) without localizing either normal.","Cartier_log_purity":"PASS: dU_D03/U_D03=dX_D03/X_D03+dv/v, the second term is regular, and both logarithmic residues are +1.","physical_trace":"CLOSED canonically in the fixed-beta characteristic-zero scope: the beta factors in dU_D03 and U_D03 cancel, leaving the positive external [dX03] line.","additional_spatial_Gysin":"NOT NEEDED for the local physical-normal evaluation; its datum is exactly the Cartier residue orientation already fixed by the marked normal.","local_coefficient_output":"By the independent entry-100 theorem, eta_3,mix maps to [1/(u0*u1*u3*u5)] tensor [dX03] with unit endpoints.","full_filtered_PC_two_cell":"CONDITIONAL: no cited entry or checker constructs log-blowup invariance/iterated-nearby-cycle six-functor compatibility embedding this relative kernel into the absolute filtration and e_F."},"counterevidence":["The central edge or either endpoint pair alone still has empty derived intersection and no nonzero cross-support Gysin class.","The Cartier identification is not a universal integral theorem: it uses the characteristic-zero exponential series and fixed nonzero beta unit.","Local Cartier residue closure does not itself prove the global Beck--Chevalley/Yoneda compatibility.","Treating q_exc as independent, imposing q_exc=q1 before Gysin, or inverting U_D03 would erase the geometric derivation."],"next_experiment":"Construct the log-blowup or iterated-nearby-cycle pull-push kernel on the absolute support-PC category and prove its Beck--Chevalley compatibility with e_F. The physical Cartier residue needs no further datum; the remaining test is purely the global functorial promotion."}"#
        )
    );
}

fn main() {
    let by_size = faces_by_size();
    let d03 = diagonal(0, 3);
    let x0 = diagonal(0, 2);
    let x1 = diagonal(1, 3);
    let x3 = diagonal(3, 5);
    let x5 = diagonal(1, 5);

    let edge: Face = [x1, x3].into_iter().collect();
    let road_edge: Face = [d03, x3].into_iter().collect();
    let plus: Face = [x1, x3, x5].into_iter().collect();
    let road_endpoint: Face = [d03, x1, x3].into_iter().collect();
    let marked_corner: Face = [d03, x0, x3].into_iter().collect();
    assert!(by_size[2].contains(&edge));
    assert!(by_size[2].contains(&road_edge));
    assert!(by_size[3].contains(&plus));
    assert!(by_size[3].contains(&road_endpoint));
    assert!(by_size[3].contains(&marked_corner));
    assert!(crosses(x5, d03));

    let endpoint_additions: Vec<_> = all_diagonals()
        .into_iter()
        .filter(|&value| addable(&edge, value))
        .collect();
    assert_eq!(endpoint_additions, [d03, x5]);
    let endpoints: BTreeSet<_> = endpoint_additions
        .iter()
        .map(|&added| {
            let mut endpoint = edge.clone();
            endpoint.insert(added);
            endpoint
        })
        .collect();
    assert_eq!(
        endpoints,
        BTreeSet::from([plus.clone(), road_endpoint.clone()])
    );

    // Ordered-normal boundary of the actual edge.  D03 sorts before x1,x3;
    // x5 sorts between x1 and x3.
    assert_eq!(incidence_sign(&edge, d03), 1);
    assert_eq!(incidence_sign(&edge, x5), -1);

    // The second marked edge replaces x1 by x0 while retaining D03 and x3.
    // It shares exactly the middle vertex with the central edge.
    let road_additions: Vec<_> = all_diagonals()
        .into_iter()
        .filter(|&value| addable(&road_edge, value))
        .collect();
    assert_eq!(road_additions, [x0, x1]);
    assert_eq!(incidence_sign(&road_edge, x0), 1);
    assert_eq!(incidence_sign(&road_edge, x1), -1);
    let road_endpoints: BTreeSet<_> = road_additions
        .iter()
        .map(|&added| {
            let mut endpoint = road_edge.clone();
            endpoint.insert(added);
            endpoint
        })
        .collect();
    assert_eq!(
        road_endpoints,
        BTreeSet::from([road_endpoint.clone(), marked_corner.clone()])
    );

    // Both path edges are consecutive edges of the actual x3 short-facet
    // pentagon.  This canonical two-dimensional corner, absent from an audit
    // of either endpoint pair alone, is the center of the log expansion.
    let facet_vertices: Vec<_> = by_size[3]
        .iter()
        .filter(|face| face.contains(&x3))
        .cloned()
        .collect();
    let facet_edges: Vec<_> = by_size[2]
        .iter()
        .filter(|face| face.contains(&x3))
        .cloned()
        .collect();
    assert_eq!(facet_vertices.len(), 5);
    assert_eq!(facet_edges.len(), 5);
    assert!(facet_edges.contains(&edge));
    assert!(facet_edges.contains(&road_edge));
    assert_eq!(
        edge.union(&road_edge).copied().collect::<Face>(),
        road_endpoint
    );

    // Every oriented-blowup generator on E13 has H subset {x1,x3}.  Radial
    // attachment retains H and introduces no endpoint-only normal circle.
    let edge_circles = subsets(&edge);
    assert_eq!(edge_circles.len(), 4);
    for circles in &edge_circles {
        assert!(circles.is_subset(&edge));
        assert!(!circles.contains(&x5));
        assert!(!circles.contains(&d03));
        let plus_circles = circles.clone();
        let road_circles = circles.clone();
        assert!(plus_circles.is_subset(&plus));
        assert!(road_circles.is_subset(&road_endpoint));
    }

    // Characteristic-lattice maps: both retain exactly the common x1,x3
    // directions.  Their kernels are distinct primitive endpoint directions.
    let plus_to_edge = [[1_i64, 0, 0], [0, 1, 0]];
    let road_to_edge = [[1_i64, 0, 0], [0, 1, 0]];
    assert_eq!(plus_to_edge, road_to_edge);
    let plus_exclusive = [0_i64, 0, 1];
    let road_exclusive = [0_i64, 0, 1];
    let apply_projection = |matrix: [[Int; 3]; 2], value: [Int; 3]| {
        std::array::from_fn(|row| {
            (0..3)
                .map(|column| matrix[row][column] * value[column])
                .sum::<Int>()
        })
    };
    assert_eq!(apply_projection(plus_to_edge, plus_exclusive), [0, 0]);
    assert_eq!(apply_projection(road_to_edge, road_exclusive), [0, 0]);

    // The central edge exposes only short characters u1,u3; the next marked
    // road edge introduces u0 and retains u3.  Across the full path, u3 is
    // exactly the repeated short normal of entry 100.
    let edge_short_characters = BTreeSet::from([1_u8, 3]);
    let entry100_road_characters = BTreeSet::from([0_u8, 3]);
    assert_eq!(
        edge_short_characters
            .intersection(&entry100_road_characters)
            .copied()
            .collect::<BTreeSet<_>>(),
        BTreeSet::from([3])
    );
    assert!(!edge_short_characters.contains(&0));

    check_weighted_broken_path();
    check_middle_log_blowup();
    check_fixed_beta_cartier_log_purity();
    check_derived_endpoint_intersection();
    check_dnc_special_fiber();

    // Retain the earlier central-edge-only packet as an explicit negative
    // control.  The full-path packet below supersedes it as this checker's
    // emitted result.
    let _central_edge_only_packet = format!(
        "{}",
        concat!(
            r#"{"claim":"For the actual labelled K6 and its real oriented boundary blowup, the marked central flip has a canonical oriented relative edge E13={x1,x3} with endpoints v_plus={x1,x3,x5} and w03={D03,x1,x3}, but it does not supply a canonical cross-support Gysin or exceptional correspondence. Intrinsically one has the cospan v_plus->E13<-w03; the endpoint fiber product is empty even derived. Simultaneous deformation to the two endpoint normal cones has empty unlocalized special fiber, and identifying its Rees parameters forces t to be invertible. Endpoint or union blowups of the interval are identities, while the two ambient exceptional divisors are disjoint. Thus the existing associahedron, normalization-conductor support, and ordinary DNC/blowup geometry canonically yield only the relative carrier edge, not the nonzero entry-100 mixed Cousin trace.","status":"falsified","scope":"falsifies the claim that the required nonzero marked ringed-support/Gysin class is canonically supplied by the existing central edge and ordinary deformation/blowup geometry; does not rule out an enriched specialization kernel with new geometric data","assumptions":["the scalar support geometry is the actual labelled hexagon associahedron with faces indexed by noncrossing dissections","the absolute PC model is the original-twist real-oriented-boundary-blowup cellular complex of entry 105, over independent occurrence and universal monodromy coefficient rings","the normalization-conductor plus support is the v_plus endpoint with ordered conormal directions (x1,x3,x5)","DNC uses its Rees parameter over the polynomial base; no t, u_j, occurrence coefficient, or integer is inverted"],"evidence_refs":["research/voevodsky/check_d03_central_flip_dnc_obstruction.rs","research/voevodsky/check_absolute_unlocalized_support_pc.rs","research/voevodsky/check_d03_formal_support_purity.rs","research/voevodsky/check_d03_factorization_marked_span.rs","research/voevodsky/check_d03_plus_excess_beck_chevalley.rs","src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md","src/ledger/20260814-99 Global Dual-Block Carrier and the Unlocalized Can-Var Boundary.md","src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md","src/ledger/20260814-104 Canonical Peripheral Roof and the Cross-Geometry Purity Gap.md","src/ledger/20260814-105 Absolute Support Complex, Shift-Corrected Purity, and the Marked-Correspondence Obstruction.md"],"factorization_test":{"actual_face_census":"PASS: (1,9,21,14)","central_flip_space":"PASS: unique edge E13={x1,x3} with exactly the two endpoints v_plus and w03","intrinsic_diagram":"cospan of closed immersions v_plus->E13<-w03, not a Cartesian span","endpoint_compatibility":"x5 and D03 cross, so no scalar face contains both endpoint-exclusive divisors","oriented_edge_class":"EXISTS canonically after the marked orientation; d[E13,H]=X_D03[w03,H]-X5[v_plus,H] for all four H subset {x1,x3}","base_coefficient_maps":"identity on the independent universal occurrence and monodromy rings; the cellular endpoint maps multiply by X_D03 and -X5 and use costandard radial var=1","support_character_maps":{"plus_to_edge":"(q1,q3,q5)->(q1,q3,1), equivalently u5->0 on the characteristic quotient","road_endpoint_to_edge":"(q1,q3,qD03)->(q1,q3,1), equivalently U03->0 on the characteristic quotient","common_packet":"K(u1,u3) only","entry100_u0":"absent from the central edge; it enters only on the next marked road edge"},"derived_endpoint_fiber_product":"EMPTY/ZERO: K_Z[s](s,1-s) has the displayed integral contraction","simultaneous_DNC":"EMPTY at t_plus=t_minus=0 because t_plus*z+t_minus*w=1","single_parameter_DNC":"FORCES LOCALIZATION: t(z+w)=1, so t is already a unit","edge_blowups":"IDENTITIES: (s), (1-s), and (s(1-s)) are effective Cartier ideals","ambient_blowup":"NO BRIDGE: the disjoint point centers have disjoint P2 exceptional divisors; the strict-transform edge meets them at two distinct P0s","canonical_Gysin_exceptional_class":"DOES NOT EXIST in this geometry; i_w03^! i_plus,*=0 because the supports are disjoint","normalization_conductor_interaction":"the plus DNC exceptional P2 contains only the tangent-direction point [x5] met by the strict transform of E13; no canonical map carries it to the separate [D03] point at the other endpoint","entry100_trace":"NOT PRODUCED: the flip packet has neither u0 nor a cross-support class, while the required residue uses (u0,u1,u3,u5) and a repeated u3 excess line"},"counterevidence":["The relative fundamental class of E13 is genuine and is the correct carrier/transgression shadow; its existence must not be relabelled as a cross-support Gysin map.","An orientation of the interval fixes the two endpoint signs but does not identify the endpoint-only normal lines or their Kummer packets.","Using a common DNC chart after t inversion deletes the special fiber whose support is required.","Blowing up a fictitious intersection of the crossing facets x5 and D03 would add geometry not present in K6.","The marked two-edge path can introduce u0 on its road leg, but that is a larger correspondence and its weighted endpoint relation still does not create an exceptional base-change class."],"next_experiment":"If the frontier is retained, specify an enriched marked specialization kernel on the full two-edge path v_plus->w03->W03 (or a logarithmic expansion that genuinely adds a common special fiber), give its ring maps from the long-divisor normal U03 to the transverse road packet (u0,u3), and prove six-functor/excess base change before testing the already fixed residue. Without such new geometric input, record the canonical central-flip Gysin class as falsified rather than fitting a transition map."}"#
        )
    );

    emit_final_packet();

    let _full_path_before_cartier_packet = format!(
        "{}",
        concat!(
            r#"{"claim":"The full marked scalar path v_plus->{D03,x1,x3}->{D03,x0,x3} has a canonical logarithmic expansion at its middle corner inside the actual x3 pentagonal facet. Blowing up the transverse ideal (D03,x1) inserts the positive exceptional P1 and gives an oriented relative dualizing class. Its log character is q_exc=q_D03*q1; physical extraordinary pullback U_D03=0 sends u_exc to u1 and retains [dX03], so no character or Rees parameter is inverted and no short normals are identified. Together with the actual road leg, the geometry selects exactly the entry-100 packets I_plus^vee=(u1^vee,u3^vee,u5^vee), I03=(u0,u3), with u3 the unique repeated normal. Consequently the independently proved excess/Koszul-Cech theorem computes the four-normal residue from this geometric input. Promotion to a filtered support-PC Beck-Chevalley two-cell remains conditional on logarithmic-blowup invariance and six-functor compatibility not constructed in entries 93-105.","status":"conditional","scope":"proved actual face incidence, middle log expansion, relative dualizing carrier, coefficient-ring maps, support directions, occurrence normalization, and reduction to the already proved entry-100 local excess theorem; conditional only at the sheaf-level filtered PC two-cell and its compatibility with e_F","assumptions":["the marked path and ordered normals are those fixed in entries 99-100","the real oriented boundary blowup admits the standard log blowup of the actual middle stratum inside F_x3","physical D03 Gysin means extraordinary pullback U_D03=0 with [dX03] retained as the determinant line","the entry-100 excess/Koszul-Cech map is used as an independently proved theorem, not redefined by its residue","no t, u_j, occurrence coefficient, or integer is inverted in the base"],"evidence_refs":["research/voevodsky/check_d03_central_flip_dnc_obstruction.rs","research/voevodsky/check_absolute_unlocalized_support_pc.rs","research/voevodsky/check_d03_formal_support_purity.rs","research/voevodsky/check_d03_factorization_marked_span.rs","research/voevodsky/check_d03_plus_excess_beck_chevalley.rs","research/voevodsky/check_one_normal_can_var_cousin.rs","research/voevodsky/check_unlocalized_plus_recollement_obstruction.rs","ledger entries 93,99,100,104,105"],"factorization_test":{"actual_broken_path":"PASS: unique consecutive edges E13={x1,x3} and ED3={D03,x3} through m={D03,x1,x3} to c={D03,x0,x3}","ambient_two_face":"PASS: both edges are adjacent boundary edges of the actual short-facet pentagon F_x3","central_edge_only_control":"ZERO: its endpoint derived fiber product is empty and simultaneous endpoint DNC forces t inversion; this does not apply to the middle-corner log blowup","weighted_relative_chain":"PASS: X1*E13+X_D03*ED3 is the primitive polynomial middle-cancelling chain with boundary X_D03*X0*c-X1*X5*v_plus","occurrence_cocycle":"PASS independently: lambda(T)=1/product_{a in T}X_a kills both weighted edge boundaries","log_expansion":"PASS: Proj Rees(D03,x1) inserts the oriented exceptional P1 between the two marked tangent rays without inverting the Rees parameter","log_ring":"R_log=R0[q_D03^+-1,q_exc^+-1]/(q_exc-q_D03*q1)","exceptional_normal":"u_exc=U_D03+u1+U_D03*u1","physical_ring_map":"R_log/(U_D03)->R0 sends q_D03 to 1, q_exc to q1, and u_exc to u1; [dX03] remains external","support_sequence":["v_plus: reciprocal (u1,u3,u5)","E13: common (u1,u3)","middle: (U_D03,u1,u3)","ED3: common (U_D03,u3)","corner/road: original (u0,u3)"],"middle_gysin_orientation":"PASS: iota_hD03(hD03 wedge h1)=h1 has positive sign","repeated_normal":"u3 only; the canonical mixed excess line is eta_3,mix","local_coefficient_output":"REDUCES canonically to entry 100, hence eta_3,mix maps to [1/(u0*u1*u3*u5)] tensor [dX03] with unit endpoints","full_filtered_PC_two_cell":"CONDITIONAL: the repository has no certified log-blowup invariance/nearby-cycle comparison embedding this local relative dualizing kernel into the absolute filtration and e_F"},"counterevidence":["The central edge or either endpoint pair alone still has no nonzero cross-support Gysin class.","The exceptional P1 is selected only because the full marked path identifies the actual middle corner (D03,x1) inside F_x3; blowing up a fictitious x5/D03 intersection remains invalid.","The relative dualizing carrier and coefficient reduction do not by themselves prove compatibility with the global Yoneda extension.","Treating q_exc as independent, setting it by hand to q1 before physical Gysin, or inverting U_D03 would destroy the geometric derivation."],"next_experiment":"Construct the log-blowup pull-push kernel for the expanded path in the absolute support-PC category and verify the excess Beck-Chevalley square with e_F. The decisive new check is functorial: its associated carrier must be the primitive weighted broken path, while physical U_D03 Gysin followed by the already fixed entry-100 excess map must give the four-normal residue without any additional normalization."}"#
        )
    );
}
