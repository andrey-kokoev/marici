//! Integral coefficient skeleton for the unsplit scalar endpoint object.
//!
//! This checker combines, without splitting either one, the two-sheet
//! normalization--conductor quotient and the orientation-twisted augmented
//! road triangle.  The correct operation is a homotopy pullback over the
//! common endpoint-orientation line, not the Yoneda splice of the conductor
//! one-extension with the whole triangle two-extension.
//!
//! The resulting complex is
//!
//!   Z -> Z + P_tag^or -> P_sh + P_road^or -> Z_or.
//!
//! It has one primitive torsion-free homology line, carrying Z_or before the
//! once-relative polarity factor and the trivial character afterward.  A
//! strict equivariant representative of that line would require both 1/2
//! and 1/3; the complex itself needs neither.
//!
//! This is only the integral D3 coefficient/carrier skeleton.  It does not
//! construct the support-PC endpoint quotient, d_sp,sc, or G_03^Cousin.

type Z = i64;
type Matrix = Vec<Vec<Z>>;

fn zero(rows: usize, columns: usize) -> Matrix {
    vec![vec![0; columns]; rows]
}

fn identity(size: usize) -> Matrix {
    let mut result = zero(size, size);
    for (index, row) in result.iter_mut().enumerate() {
        row[index] = 1;
    }
    result
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty());
    assert!(!right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = zero(left.len(), right[0].len());
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                result[row][column] += left[row][middle] * right[middle][column];
            }
        }
    }
    result
}

fn scale(value: &Matrix, scalar: Z) -> Matrix {
    value
        .iter()
        .map(|row| row.iter().map(|entry| scalar * entry).collect())
        .collect()
}

fn block_diagonal(left: &Matrix, right: &Matrix) -> Matrix {
    let mut result = zero(left.len() + right.len(), left[0].len() + right[0].len());
    for row in 0..left.len() {
        for column in 0..left[0].len() {
            result[row][column] = left[row][column];
        }
    }
    for row in 0..right.len() {
        for column in 0..right[0].len() {
            result[left.len() + row][left[0].len() + column] = right[row][column];
        }
    }
    result
}

fn power(value: &Matrix, exponent: usize) -> Matrix {
    let mut result = identity(value.len());
    for _ in 0..exponent {
        result = multiply(&result, value);
    }
    result
}

fn rank_mod_prime(value: &Matrix, prime: Z) -> usize {
    let mut rows: Matrix = value
        .iter()
        .map(|row| row.iter().map(|entry| entry.rem_euclid(prime)).collect())
        .collect();
    let mut rank = 0;
    let columns = rows.first().map_or(0, Vec::len);
    for column in 0..columns {
        let Some(pivot) = (rank..rows.len()).find(|row| rows[*row][column] != 0) else {
            continue;
        };
        rows.swap(rank, pivot);
        let pivot_value = rows[rank][column];
        let inverse = (1..prime)
            .find(|candidate| (candidate * pivot_value).rem_euclid(prime) == 1)
            .expect("prime-field inverse");
        for entry in &mut rows[rank] {
            *entry = (*entry * inverse).rem_euclid(prime);
        }
        let pivot_row = rows[rank].clone();
        for row in 0..rows.len() {
            if row == rank {
                continue;
            }
            let factor = rows[row][column];
            for entry in column..columns {
                rows[row][entry] = (rows[row][entry] - factor * pivot_row[entry]).rem_euclid(prime);
            }
        }
        rank += 1;
    }
    rank
}

fn apply(matrix: &Matrix, vector: &[Z]) -> Vec<Z> {
    matrix
        .iter()
        .map(|row| {
            row.iter()
                .zip(vector)
                .map(|(left, right)| left * right)
                .sum()
        })
        .collect()
}

fn determinant(value: &Matrix) -> Z {
    assert!(value.iter().all(|row| row.len() == value.len()));
    if value.is_empty() {
        return 1;
    }
    if value.len() == 1 {
        return value[0][0];
    }
    let mut result = 0;
    for column in 0..value.len() {
        let minor = value[1..]
            .iter()
            .map(|row| {
                row.iter()
                    .enumerate()
                    .filter_map(|(index, entry)| (index != column).then_some(*entry))
                    .collect()
            })
            .collect();
        let sign = if column % 2 == 0 { 1 } else { -1 };
        result += sign * value[0][column] * determinant(&minor);
    }
    result
}

fn check_group_action(rotation: &Matrix, reflection: &Matrix) {
    assert_eq!(power(rotation, 3), identity(rotation.len()));
    assert_eq!(power(reflection, 2), identity(reflection.len()));
    assert_eq!(
        multiply(reflection, &multiply(rotation, reflection)),
        power(rotation, 2)
    );
}

fn main() {
    // Road basis (1,r,r^2).  The physical reflection fixes the first road
    // and exchanges the other two.  Which long channel is listed first is a
    // harmless cyclic relabelling.
    let rotation = vec![vec![0, 0, 1], vec![1, 0, 0], vec![0, 1, 0]];
    let rotation_inverse = power(&rotation, 2);
    let road_reflection = vec![vec![1, 0, 0], vec![0, 0, 1], vec![0, 1, 0]];
    let middle = vec![vec![1, 0, -1], vec![-1, 1, 0], vec![0, -1, 1]]; // 1-r
    let norm = vec![vec![1], vec![1], vec![1]];
    let augmentation = vec![vec![1, 1, 1]];

    // Before twisting, tags carry -r^{-1}s and roads carry s.  Tensoring
    // the full triangle by the road-orientation line makes its top trivial,
    // its bottom Z_or, and changes both middle reflections by -1.
    let tag_reflection = scale(&multiply(&rotation_inverse, &road_reflection), -1);
    let tag_twisted_reflection = scale(&tag_reflection, -1);
    let road_twisted_reflection = scale(&road_reflection, -1);
    check_group_action(&rotation, &tag_twisted_reflection);
    check_group_action(&rotation, &road_twisted_reflection);
    assert_eq!(multiply(&middle, &norm), zero(3, 1));
    assert_eq!(multiply(&augmentation, &middle), zero(1, 3));
    assert_eq!(
        multiply(&road_twisted_reflection, &middle),
        multiply(&middle, &tag_twisted_reflection)
    );
    assert_eq!(multiply(&tag_twisted_reflection, &norm), norm);
    assert_eq!(
        multiply(&scale(&augmentation, -1), &road_twisted_reflection),
        augmentation
    );

    // C3=Z_top -> C2=Z_diag + P_tag^or.
    let d3 = vec![vec![0], vec![1], vec![1], vec![1]];

    // C2 -> C1=P_sh + P_road^or is Delta_sh plus (1-r).
    let mut d2 = zero(5, 4);
    d2[0][0] = 1;
    d2[1][0] = 1;
    for row in 0..3 {
        for column in 0..3 {
            d2[2 + row][1 + column] = middle[row][column];
        }
    }

    // C1 -> C0=Z_or is conductor difference minus road augmentation.
    let d1 = vec![vec![1, -1, -1, -1, -1]];
    assert_eq!(multiply(&d2, &d3), zero(5, 1));
    assert_eq!(multiply(&d1, &d2), zero(1, 4));

    // D3 actions in every degree.
    let rotation_c3 = identity(1);
    let reflection_c3 = identity(1);
    let rotation_c2 = block_diagonal(&identity(1), &rotation);
    let reflection_c2 = block_diagonal(&identity(1), &tag_twisted_reflection);
    let rotation_c1 = block_diagonal(&identity(2), &rotation);
    let reflection_sheets = vec![vec![0, 1], vec![1, 0]];
    let reflection_c1 = block_diagonal(&reflection_sheets, &road_twisted_reflection);
    let rotation_c0 = identity(1);
    let reflection_c0 = vec![vec![-1]];
    for (r, s) in [
        (&rotation_c3, &reflection_c3),
        (&rotation_c2, &reflection_c2),
        (&rotation_c1, &reflection_c1),
        (&rotation_c0, &reflection_c0),
    ] {
        check_group_action(r, s);
    }
    assert_eq!(multiply(&rotation_c2, &d3), multiply(&d3, &rotation_c3));
    assert_eq!(multiply(&reflection_c2, &d3), multiply(&d3, &reflection_c3));
    assert_eq!(multiply(&rotation_c1, &d2), multiply(&d2, &rotation_c2));
    assert_eq!(multiply(&reflection_c1, &d2), multiply(&d2, &reflection_c2));
    assert_eq!(multiply(&rotation_c0, &d1), multiply(&d1, &rotation_c1));
    assert_eq!(multiply(&reflection_c0, &d1), multiply(&d1, &reflection_c1));

    // Exact ranks leave one homology line in degree one.
    assert_eq!(rank_mod_prime(&d3, 101), 1);
    assert_eq!(rank_mod_prime(&d2, 101), 3);
    assert_eq!(rank_mod_prime(&d1, 101), 1);
    assert_eq!(
        [1_usize, 4, 5, 1],
        [d3[0].len(), d2[0].len(), d1[0].len(), d1.len()]
    );
    assert_eq!(5 - 3 - 1, 1);

    // Integral saturation is not inferred from a field rank.  The following
    // C2 basis has columns (diag, norm, tag_0, tag_1), determinant +1, and
    // d2 sends it to (sheet diagonal, 0, road m_0, road m_1).
    let c2_basis = vec![
        vec![1, 0, 0, 0],
        vec![0, 1, 1, 0],
        vec![0, 1, 0, 1],
        vec![0, 1, 0, 0],
    ];
    assert_eq!(determinant(&c2_basis), 1);
    assert_eq!(
        multiply(&d2, &c2_basis),
        vec![
            vec![1, 0, 0, 0],
            vec![1, 0, 0, 0],
            vec![0, 0, 1, 0],
            vec![0, 0, -1, 1],
            vec![0, 0, 0, -1],
        ]
    );

    // The C1 columns (sheet diagonal, m_0, m_1, z, a quotient lift) are
    // likewise a determinant-one basis.  The first three columns are the
    // saturated image of d2, the first four are exactly ker(d1), and the last
    // maps to the primitive generator of C0.  Hence H1=Z<z> integrally and
    // every other homology group vanishes, with no hidden torsion.
    let c1_basis = vec![
        vec![1, 0, 0, 1, 1],
        vec![1, 0, 0, 0, 0],
        vec![0, 1, 0, 1, 0],
        vec![0, -1, 1, 0, 0],
        vec![0, 0, -1, 0, 0],
    ];
    assert_eq!(determinant(&c1_basis), 1);
    assert_eq!(multiply(&d1, &c1_basis), vec![vec![0, 0, 0, 0, 1]]);

    // The primitive cycle z has common endpoint value one.
    let z = vec![1, 0, 1, 0, 0];
    assert_eq!(apply(&d1, &z), vec![0]);
    let phi = |value: &[Z]| value[2] + value[3] + value[4];
    assert_eq!(phi(&z), 1);

    // The surviving line is reflection-odd before polarity and trivial
    // after tensoring the once-relative polarity sign.
    assert_eq!(phi(&apply(&rotation_c1, &z)), 1);
    assert_eq!(phi(&apply(&reflection_c1, &z)), -1);
    let road_character = -1;
    let polarity_character = -1;
    assert_eq!(road_character * polarity_character, 1);

    // No strict D3-equivariant cycle representative of phi=1 exists.  Encode
    // the cycle, normalization, rotation-invariance, and reflection-odd
    // equations as one integral linear system.  Its reductions modulo both
    // 3 and 2 are inconsistent.  Equivalently, rotation gives 3c=1, while
    // reflection plus the cycle equation gives sheet values (1/2,-1/2).
    let mut section_equations = vec![d1[0].clone(), vec![0, 0, 1, 1, 1]];
    let mut section_rhs = vec![0, 1];
    let rotation_difference = {
        let mut value = rotation_c1.clone();
        for (index, row) in value.iter_mut().enumerate() {
            row[index] -= 1;
        }
        value
    };
    let reflection_sum = {
        let mut value = reflection_c1.clone();
        for (index, row) in value.iter_mut().enumerate() {
            row[index] += 1;
        }
        value
    };
    for row in rotation_difference.into_iter().chain(reflection_sum) {
        section_equations.push(row);
        section_rhs.push(0);
    }
    let section_augmented: Matrix = section_equations
        .iter()
        .zip(&section_rhs)
        .map(|(row, rhs)| {
            let mut augmented = row.clone();
            augmented.push(*rhs);
            augmented
        })
        .collect();
    assert_eq!(rank_mod_prime(&section_equations, 3), 4);
    assert_eq!(rank_mod_prime(&section_augmented, 3), 5);
    assert_eq!(rank_mod_prime(&section_equations, 2), 4);
    assert_eq!(rank_mod_prime(&section_augmented, 2), 5);

    // Degree audit for the tempting but incorrect five-term Yoneda splice.
    // e_pol o beta_triangle lies in Ext^3, while the loaded obstruction is
    // e_pol o p_endpoint and lies in Ext^2.
    let conductor_extension_degree = 1;
    let triangle_extension_degree = 2;
    let endpoint_defect_degree = 1;
    assert_eq!(conductor_extension_degree + triangle_extension_degree, 3);
    assert_eq!(conductor_extension_degree + endpoint_defect_degree, 2);

    println!(
        "{}",
        concat!(
            r#"{"claim":"The two-sheet conductor quotient and the orientation-twisted road augmentation have a canonical integral D3-equivariant homotopy-pullback skeleton C3=Z -> C2=Z+P_tag^or -> C1=P_sh+P_road^or -> C0=Z_or. Its differential squares to zero, and its only homology is one primitive torsion-free degree-one line carrying the road-orientation character; tensoring the once-relative polarity line makes that primitive line trivial. The skeleton retains the full three-road extension and requires neither a transition function nor division by 2 or 3.","status":"proved","assumptions":["The conductor sequence is 0->Z->P_sh->Z_or->0 with physical reflection exchanging the two sheets.","The augmented triangle is tensor-twisted by the road-orientation line before its road augmentation is compared with the conductor difference.","This is a coefficient/carrier homotopy pullback, not an asserted support-PC realization."],"factorization_test":{"ranks_C3_C2_C1_C0":[1,4,5,1],"differential_ranks":[1,3,1],"d_squared":"PASS","D3_covariance":"PASS in all degrees","homology":"H1=Z_or, all other groups zero, no torsion","once_polarity_loaded_homology":"Z_triv","strict_integral_section":"ABSENT: rotation would require 3c=1 and reflection would require a sheet half-difference","numeric_inversion":"NONE","naive_full_triangle_splice":"WRONG DEGREE: Ext1 o Ext2 is Ext3, not the desired Ext2"},"counterevidence":["The module complex does not construct the geometric endpoint/Q quotient or its extraordinary support variance.","It does not determine p_partial_Q; that class measures an attempted strictification/pointing of the unsplit object.","No occurrence, multi-Rees, reciprocal/BM, PC/Cousin, or physical-cut map is inferred from coefficient exactness."],"sharp_blocker":"Lift the common quotient maps diff:P_sh->Z_or and epsilon:P_road^or->Z_or, and their homotopy pullback, to the actual two-sheet normalization galleries and the based nonzero-Q road object in one filtered support-PC category. Only then can this skeleton be promoted to S_F^sp and mapped by G_03^Cousin.","next_experiment":"Construct the geometric common endpoint-orientation quotient first, rather than choosing a parity or a road-line section; then tensor the resulting homotopy pullback with the established occurrence/multi-Rees packets and test the entry-131 D03 purity boundary."}"#
        )
    );
}
