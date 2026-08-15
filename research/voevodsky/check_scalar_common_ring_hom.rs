//! Formal common-ring Hom audit for the scalar Tate--Cartier and mixed blocks.
//!
//! This certificate works only after the coefficientwise base change
//!
//!   R = Z[t1,t3,t5,x1,x3,x5,(1+t1*x1)^-1,
//!         (1+t3*x3)^-1,(1+t5*x5)^-1].
//!
//! It deliberately does not assert that this base change is a spatial
//! extraordinary pull--push.  The source is the tensor totalization of the
//! integral Tate complex with the three-conormal exterior packet.  The target
//! is the full inherited three-Morse-top block.  The genuinely generated
//! invariant image subcomplex R*H_Sigma -> R*z_Sigma is separately
//! contractible because its displayed differential has unit coefficient.
//!
//! The target has an explicit D3-equivariant contraction.  Postcomposition
//! with that contraction contracts the entire coefficientwise Hom complex,
//! including its D3-equivariant subcomplex.  Thus its H^1 is zero, with no
//! torsion or normalized line.  This says nothing about a geometric
//! extraordinary correspondence, because the required common ringed support
//! category has not been constructed.
//!
//! As a separate negative control, directly requiring alpha(N_road)=q_Sigma
//! is incompatible with the cocycle equation.  The full Tate--Cartier
//! boundary of N_road lies in the ideal (3,t1,t3,t5), whereas
//! d(q_Sigma)=x1*b1+x3*b3+x5*b5 does not.  This does not impose that value in
//! the Hom calculation and does not constrain an induced cone-roof carrier
//! comparison rho_alpha.

use std::collections::BTreeMap;

type Int = i64;
const LABELS: usize = 3;
const VARIABLES: usize = 6;

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Poly(BTreeMap<[u8; VARIABLES], Int>);

impl Poly {
    fn scalar(value: Int) -> Self {
        if value == 0 {
            Self::default()
        } else {
            Self(BTreeMap::from([([0; VARIABLES], value)]))
        }
    }

    fn variable(slot: usize) -> Self {
        let mut powers = [0; VARIABLES];
        powers[slot] = 1;
        Self(BTreeMap::from([(powers, 1)]))
    }

    fn t(label: usize) -> Self {
        Self::variable(label)
    }

    fn x(label: usize) -> Self {
        Self::variable(LABELS + label)
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (&powers, &coefficient) in &other.0 {
            *self.0.entry(powers).or_default() += scale * coefficient;
        }
        self.0.retain(|_, coefficient| *coefficient != 0);
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        result.add_scaled(other, 1);
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::default();
        for (&left_powers, &left_coefficient) in &self.0 {
            for (&right_powers, &right_coefficient) in &other.0 {
                let powers = std::array::from_fn(|slot| left_powers[slot] + right_powers[slot]);
                let term = Self(BTreeMap::from([(
                    powers,
                    left_coefficient * right_coefficient,
                )]));
                result.add_scaled(&term, 1);
            }
        }
        result
    }

    fn permute(&self, permutation: [usize; LABELS]) -> Self {
        let mut result = Self::default();
        for (&powers, &coefficient) in &self.0 {
            let mut image = [0; VARIABLES];
            for old in 0..LABELS {
                image[permutation[old]] = powers[old];
                image[LABELS + permutation[old]] = powers[LABELS + old];
            }
            result.add_scaled(&Self(BTreeMap::from([(image, coefficient)])), 1);
        }
        result
    }

    fn in_three_rees_ideal(&self) -> bool {
        self.0.iter().all(|(powers, coefficient)| {
            coefficient.rem_euclid(3) == 0 || powers[..LABELS].iter().any(|power| *power > 0)
        })
    }
}

type Matrix = Vec<Vec<Poly>>;

fn zero(rows: usize, columns: usize) -> Matrix {
    vec![vec![Poly::default(); columns]; rows]
}

fn identity(size: usize) -> Matrix {
    let mut result = zero(size, size);
    for (index, row) in result.iter_mut().enumerate() {
        row[index] = Poly::scalar(1);
    }
    result
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty() && !right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = zero(left.len(), right[0].len());
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                let term = left[row][middle].multiply(&right[middle][column]);
                result[row][column].add_scaled(&term, 1);
            }
        }
    }
    result
}

fn add(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left.len(), right.len());
    let mut result = left.clone();
    for row in 0..result.len() {
        assert_eq!(result[row].len(), right[row].len());
        for column in 0..result[row].len() {
            result[row][column].add_scaled(&right[row][column], 1);
        }
    }
    result
}

fn apply(matrix: &Matrix, vector: &[Poly]) -> Vec<Poly> {
    assert_eq!(matrix.first().map_or(0, Vec::len), vector.len());
    matrix
        .iter()
        .map(|row| {
            row.iter()
                .zip(vector)
                .fold(Poly::default(), |sum, (entry, value)| {
                    sum.add(&entry.multiply(value))
                })
        })
        .collect()
}

fn stage_dimension(stage: usize) -> usize {
    [1, 3, 3, 1][stage]
}

fn tate_differential(stage: usize) -> Vec<Vec<Int>> {
    match stage {
        0 => vec![vec![1], vec![1], vec![1]],
        1 => vec![vec![1, 0, -1], vec![-1, 1, 0], vec![0, -1, 1]],
        2 => vec![vec![1, 1, 1]],
        _ => unreachable!(),
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct CBasis {
    stage: usize,
    component: usize,
    exterior_mask: u8,
}

fn exterior_degree(mask: u8) -> usize {
    mask.count_ones() as usize
}

fn c_basis(degree: usize) -> Vec<CBasis> {
    let mut result = Vec::new();
    for stage in 0..=3 {
        for mask in 0_u8..8 {
            if stage + exterior_degree(mask) != degree {
                continue;
            }
            for component in 0..stage_dimension(stage) {
                result.push(CBasis {
                    stage,
                    component,
                    exterior_mask: mask,
                });
            }
        }
    }
    result
}

fn wedge_sign(label: usize, mask: u8) -> Int {
    let preceding = (0..label).filter(|slot| mask & (1 << slot) != 0).count();
    if preceding % 2 == 0 {
        1
    } else {
        -1
    }
}

fn c_differentials() -> (Vec<Vec<CBasis>>, Vec<Matrix>) {
    let bases: Vec<_> = (0..=6).map(c_basis).collect();
    assert_eq!(
        bases.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 6, 15, 20, 15, 6, 1]
    );
    let indices: Vec<BTreeMap<_, _>> = bases
        .iter()
        .map(|basis| {
            basis
                .iter()
                .copied()
                .enumerate()
                .map(|(index, value)| (value, index))
                .collect()
        })
        .collect();
    let mut differentials = Vec::new();
    for degree in 0..6 {
        let mut differential = zero(bases[degree + 1].len(), bases[degree].len());
        for (column, source) in bases[degree].iter().copied().enumerate() {
            if source.stage < 3 {
                let tate = tate_differential(source.stage);
                for (target_component, row_values) in tate.iter().enumerate() {
                    let coefficient = row_values[source.component];
                    if coefficient == 0 {
                        continue;
                    }
                    let target = CBasis {
                        stage: source.stage + 1,
                        component: target_component,
                        exterior_mask: source.exterior_mask,
                    };
                    differential[indices[degree + 1][&target]][column]
                        .add_scaled(&Poly::scalar(coefficient), 1);
                }
            }
            for label in 0..LABELS {
                if source.exterior_mask & (1 << label) != 0 {
                    continue;
                }
                let totalization_sign = if source.stage % 2 == 0 { 1 } else { -1 };
                let target = CBasis {
                    exterior_mask: source.exterior_mask | (1 << label),
                    ..source
                };
                differential[indices[degree + 1][&target]][column].add_scaled(
                    &Poly::t(label),
                    totalization_sign * wedge_sign(label, source.exterior_mask),
                );
            }
        }
        differentials.push(differential);
    }
    (bases, differentials)
}

fn mixed_differentials_and_contraction() -> (Vec<usize>, Vec<Matrix>, Vec<Matrix>) {
    // Cohomological degrees are M^0=<m_i>, M^1=<q_i,xi_i>, M^2=<b_i>.
    let ranks = vec![3, 6, 3];
    let mut d_zero = zero(6, 3);
    let mut d_one = zero(3, 6);
    for label in 0..LABELS {
        d_zero[label][label] = Poly::scalar(1);
        d_zero[LABELS + label][label].add_scaled(&Poly::x(label), -1);
        d_one[label][label] = Poly::x(label);
        d_one[label][LABELS + label] = Poly::scalar(1);
    }

    // h^1(q_i)=m_i, h^1(xi_i)=0, and h^2(b_i)=xi_i.
    let mut h_one = zero(3, 6);
    let mut h_two = zero(6, 3);
    for label in 0..LABELS {
        h_one[label][label] = Poly::scalar(1);
        h_two[LABELS + label][label] = Poly::scalar(1);
    }
    (ranks, vec![d_zero, d_one], vec![Vec::new(), h_one, h_two])
}

fn act_mixed(degree: usize, value: &[Poly], permutation: [usize; LABELS]) -> Vec<Poly> {
    let mut result = vec![Poly::default(); value.len()];
    match degree {
        0 | 2 => {
            for old in 0..LABELS {
                result[permutation[old]] = value[old].permute(permutation);
            }
        }
        1 => {
            for old in 0..LABELS {
                result[permutation[old]] = value[old].permute(permutation);
                result[LABELS + permutation[old]] = value[LABELS + old].permute(permutation);
            }
        }
        _ => unreachable!(),
    }
    result
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct HomKey {
    source_degree: usize,
    source_index: usize,
    target_degree: usize,
    target_index: usize,
}

type HomCochain = BTreeMap<HomKey, Poly>;

fn add_hom(value: &mut HomCochain, key: HomKey, coefficient: &Poly, scale: Int) {
    value.entry(key).or_default().add_scaled(coefficient, scale);
    value.retain(|_, entry| *entry != Poly::default());
}

fn hom_delta(
    value: &HomCochain,
    degree: isize,
    c_differentials: &[Matrix],
    m_differentials: &[Matrix],
) -> HomCochain {
    let mut result = HomCochain::new();
    for (key, coefficient) in value {
        if key.target_degree < m_differentials.len() {
            for target in 0..m_differentials[key.target_degree].len() {
                let term = m_differentials[key.target_degree][target][key.target_index]
                    .multiply(coefficient);
                add_hom(
                    &mut result,
                    HomKey {
                        target_degree: key.target_degree + 1,
                        target_index: target,
                        ..*key
                    },
                    &term,
                    1,
                );
            }
        }
        if key.source_degree > 0 {
            let source_differential = &c_differentials[key.source_degree - 1];
            let hom_sign = if degree.rem_euclid(2) == 0 { -1 } else { 1 };
            for source in 0..source_differential[0].len() {
                let term = coefficient.multiply(&source_differential[key.source_index][source]);
                add_hom(
                    &mut result,
                    HomKey {
                        source_degree: key.source_degree - 1,
                        source_index: source,
                        ..*key
                    },
                    &term,
                    hom_sign,
                );
            }
        }
    }
    result
}

fn hom_contraction(value: &HomCochain, contraction: &[Matrix]) -> HomCochain {
    let mut result = HomCochain::new();
    for (key, coefficient) in value {
        if key.target_degree == 0 {
            continue;
        }
        for target in 0..contraction[key.target_degree].len() {
            let term =
                contraction[key.target_degree][target][key.target_index].multiply(coefficient);
            add_hom(
                &mut result,
                HomKey {
                    target_degree: key.target_degree - 1,
                    target_index: target,
                    ..*key
                },
                &term,
                1,
            );
        }
    }
    result
}

fn add_hom_cochains(left: &HomCochain, right: &HomCochain) -> HomCochain {
    let mut result = left.clone();
    for (key, coefficient) in right {
        add_hom(&mut result, *key, coefficient, 1);
    }
    result
}

fn check_formal_hom_contraction(
    c_bases: &[Vec<CBasis>],
    c_differentials: &[Matrix],
    m_ranks: &[usize],
    m_differentials: &[Matrix],
    contraction: &[Matrix],
) {
    for (source_degree, source_basis) in c_bases.iter().enumerate() {
        for source_index in 0..source_basis.len() {
            for (target_degree, target_rank) in m_ranks.iter().copied().enumerate() {
                for target_index in 0..target_rank {
                    let key = HomKey {
                        source_degree,
                        source_index,
                        target_degree,
                        target_index,
                    };
                    let basis = HomCochain::from([(key, Poly::scalar(1))]);
                    let degree = target_degree as isize - source_degree as isize;
                    let delta_after_h = hom_delta(
                        &hom_contraction(&basis, contraction),
                        degree - 1,
                        c_differentials,
                        m_differentials,
                    );
                    let h_after_delta = hom_contraction(
                        &hom_delta(&basis, degree, c_differentials, m_differentials),
                        contraction,
                    );
                    assert_eq!(add_hom_cochains(&delta_after_h, &h_after_delta), basis);
                }
            }
        }
    }
}

fn check_direct_norm_value_obstruction(
    c_bases: &[Vec<CBasis>],
    c_differentials: &[Matrix],
    m_differentials: &[Matrix],
) {
    // N_road is the sum of the three stage-2 road generators in exterior
    // degree zero.  Its full total differential contains epsilon(N)=3 and
    // all nine t_i-labelled exterior terms.
    let mut n_road = vec![Poly::default(); c_bases[2].len()];
    for component in 0..LABELS {
        let generator = CBasis {
            stage: 2,
            component,
            exterior_mask: 0,
        };
        let index = c_bases[2]
            .iter()
            .position(|value| *value == generator)
            .unwrap();
        n_road[index] = Poly::scalar(1);
    }
    let d_n_road = apply(&c_differentials[2], &n_road);
    assert!(d_n_road.iter().all(Poly::in_three_rees_ideal));
    assert!(d_n_road
        .iter()
        .any(|coefficient| coefficient == &Poly::scalar(3)));

    // q_Sigma is q1+q3+q5.  Its differential is the primitive endpoint
    // vector (x1,x3,x5), nonzero modulo (3,t1,t3,t5).
    let mut q_sigma = vec![Poly::default(); 6];
    for label in 0..LABELS {
        q_sigma[label] = Poly::scalar(1);
    }
    let d_q_sigma = apply(&m_differentials[1], &q_sigma);
    assert_eq!(d_q_sigma, (0..LABELS).map(Poly::x).collect::<Vec<_>>());
    assert!(d_q_sigma
        .iter()
        .all(|coefficient| !coefficient.in_three_rees_ideal()));

    // Localizing by 1+t_i*x_i does not change this quotient: each such unit
    // becomes 1 modulo (3,t1,t3,t5).
    for label in 0..LABELS {
        let graph_unit = Poly::scalar(1).add(&Poly::t(label).multiply(&Poly::x(label)));
        assert!(!graph_unit.in_three_rees_ideal());
    }
}

fn main() {
    let (c_bases, c_differentials) = c_differentials();
    for degree in 0..5 {
        assert_eq!(
            multiply(&c_differentials[degree + 1], &c_differentials[degree]),
            zero(c_bases[degree + 2].len(), c_bases[degree].len())
        );
    }

    let (m_ranks, m_differentials, contraction) = mixed_differentials_and_contraction();
    assert_eq!(
        multiply(&m_differentials[1], &m_differentials[0]),
        zero(3, 3)
    );
    assert_eq!(multiply(&contraction[1], &m_differentials[0]), identity(3));
    assert_eq!(
        add(
            &multiply(&m_differentials[0], &contraction[1]),
            &multiply(&contraction[2], &m_differentials[1]),
        ),
        identity(6)
    );
    assert_eq!(multiply(&m_differentials[1], &contraction[2]), identity(3));

    // The same contraction commutes with rotation and reflection, so it
    // preserves the strict D3-equivariant Hom subcomplex.
    let rotation = [1, 2, 0];
    let reflection = [0, 2, 1];
    for permutation in [rotation, reflection] {
        for degree in 0..=2 {
            for basis_index in 0..m_ranks[degree] {
                let mut basis = vec![Poly::default(); m_ranks[degree]];
                basis[basis_index] = Poly::scalar(1);
                if degree < 2 {
                    assert_eq!(
                        apply(
                            &m_differentials[degree],
                            &act_mixed(degree, &basis, permutation)
                        ),
                        act_mixed(
                            degree + 1,
                            &apply(&m_differentials[degree], &basis),
                            permutation,
                        )
                    );
                }
                if degree > 0 {
                    assert_eq!(
                        apply(
                            &contraction[degree],
                            &act_mixed(degree, &basis, permutation)
                        ),
                        act_mixed(
                            degree - 1,
                            &apply(&contraction[degree], &basis),
                            permutation,
                        )
                    );
                }
            }
        }
    }

    check_formal_hom_contraction(
        &c_bases,
        &c_differentials,
        &m_ranks,
        &m_differentials,
        &contraction,
    );
    check_direct_norm_value_obstruction(&c_bases, &c_differentials, &m_differentials);

    println!(
        "{}",
        r#"{"claim":"After the explicit coefficientwise base change to the common three-normal multi-Rees ring, the full inherited mixed block M_i=(R<m_i> -> R<q_i,xi_i> -> R<b_i>) has the D3-equivariant contraction h(b_i)=xi_i, h(q_i)=m_i, h(xi_i)=0. Postcomposition by h contracts Hom_R(C_nc^mR,M_F), and because h is D3-equivariant it also contracts the strict D3-equivariant Hom subcomplex. Hence formal H^1 is zero in every relative shift, with no free line and no torsion. No inclusion-, quotient-, or cap-derived coefficient cocycle survives as a Hom-cohomology class. Separately, a direct strict value alpha(N_road)=q_Sigma is impossible: d_C(N_road) lies in (3,t1,t3,t5)C while d_M(q_Sigma)=(x1,x3,x5) does not lie in (3,t1,t3,t5)M, even with every exterior multi-Rees term retained. This coefficient theorem is not a geometric RHom or extraordinary correspondence.","status":"proved","assumptions":["The computed target is the full three-top mixed block certified by check_positive_mixed_rees_top.rs; the genuine two-term subcomplex R*H_Sigma -> R*z_Sigma generated by H_Sigma is also contractible by its unit differential.","The formal common ring is Z[t_i,x_i,(1+t_i*x_i)^-1] for i=1,3,5, with D3 permuting the labelled pairs.","Only strict coefficientwise semilinear D3 maps are computed; no support pullback, nearby-cycle branch selection, BM/ordinary variance conversion, or spatial extraordinary functor is inferred."],"factorization_test":{"C_total_ranks":[1,6,15,20,15,6,1],"M_ranks":[3,6,3],"M_d_squared":"zero","M_equivariant_contraction":"passed for rotation and reflection","Hom_contraction":"passed on every elementary common-ring Hom generator","formal_H1":"zero","integer_torsion":"none","direct_alpha_N_equals_qSigma":"falsified modulo (3,t1,t3,t5)","geometric_RHom":"untyped"},"counterevidence":["The genuine H_Sigma-generated image subcomplex R*H_Sigma -> R*z_Sigma is contractible; only the artificial truncation that retains all six lower generators while deleting two Morse tops is noncontractible, and that truncation is not the frozen M_F.","The PL cap 1-r is internal to C_nc^mR and does not define a map to M_F.","The common coefficient base change does not choose the positive spatial support component among the eight multi-Rees components."],"next_experiment":"Define an explicit D3-equivariant ringed support/nearby-cycle functor selecting V(x1,x3,x5), together with the variance-correct extraordinary pull-push into the absolute mixed block. Only then form geometric RHom and test whether its class maps to the coefficientwise nullhomotopic shadow without prescribing q_Sigma or any residue."}"#
    );
}
