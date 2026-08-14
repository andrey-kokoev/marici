//! Exact integral certificate for the scalar-polarity conductor normal-link fold.
//!
//! This checker deliberately stays on the cellular associated grade.  The two
//! degree-two generators are not literal associahedron faces: they are the dual
//! cellular top classes of the vertex figures (equivalently, of the positive
//! projectivized rank-three conductor normal cones) at the two parity-central
//! triangulation vertices.  Since K_6 is simple, each vertex figure is a
//! canonical Delta^2.  Its three link edges are dual to the three conductor
//! coordinates, and its three link vertices are the unique roads reached by
//! the corresponding flips.  Orient the dual link-edge bases so that
//!
//!   d2(f_+) = e1 + e3 + e5,   d2(f_-) = e0 + e2 + e4.
//!
//! This derives d2 without using K_alt.  In particular, no global barycentric
//! representative and no factor 1/2 is chosen.
//!
//! The remaining source differential is the independently scalar-derived
//! six-point QTDS contact matrix of entries 20 and 66.  The fold lands in the
//! exact augmented triangle
//!
//!   0 -> 1_or -> P_tag -> P_road -> 1 -> 0
//!
//! by (+1,-1), K_alt, Id, Id.  The audit checks chain identities, integral
//! kernels and Smith factors, the canonical H1(kernel) = A2 identification,
//! and all six powers of the one-step cyclic action.
//!
//! This is not a full PC chain lift.  In particular it does not construct the
//! occurrence-loaded coefficient/Gysin trace between the paired source edge
//! local systems.

type Z = i64;
type Matrix = Vec<Vec<Z>>;

const QTDS: [[Z; 6]; 3] = [
    [1, 1, 0, -1, -1, 0],
    [0, -1, -1, 0, 1, 1],
    [-1, 0, 1, 1, 0, -1],
];

const K_ALT: [[Z; 6]; 3] = [
    [0, 0, -1, 0, 0, 1],
    [-1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, -1, 0],
];

const TRIANGLE_BOUNDARY: [[Z; 3]; 3] = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]];

fn matrix<const ROWS: usize, const COLUMNS: usize>(entries: [[Z; COLUMNS]; ROWS]) -> Matrix {
    entries.map(Vec::from).into()
}

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

fn dimensions(value: &Matrix) -> (usize, usize) {
    let columns = value.first().map_or(0, Vec::len);
    assert!(value.iter().all(|row| row.len() == columns));
    (value.len(), columns)
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    let (left_rows, middle) = dimensions(left);
    let (right_rows, right_columns) = dimensions(right);
    assert_eq!(middle, right_rows);
    let mut result = zero(left_rows, right_columns);
    for row in 0..left_rows {
        for column in 0..right_columns {
            result[row][column] = (0..middle)
                .map(|index| left[row][index] * right[index][column])
                .sum();
        }
    }
    result
}

fn horizontal(left: &Matrix, right: &Matrix) -> Matrix {
    let (left_rows, _) = dimensions(left);
    let (right_rows, _) = dimensions(right);
    assert_eq!(left_rows, right_rows);
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            left_row
                .iter()
                .chain(right_row)
                .copied()
                .collect::<Vec<_>>()
        })
        .collect()
}

fn power(value: &Matrix, exponent: usize) -> Matrix {
    let (rows, columns) = dimensions(value);
    assert_eq!(rows, columns);
    let mut result = identity(rows);
    for _ in 0..exponent {
        result = multiply(&result, value);
    }
    result
}

fn gcd(mut left: Z, mut right: Z) -> Z {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

fn determinant(value: &Matrix) -> Z {
    let (size, columns) = dimensions(value);
    assert_eq!(size, columns);
    if size == 0 {
        return 1;
    }
    if size == 1 {
        return value[0][0];
    }

    // Fraction-free Bareiss elimination is exact over Z.
    let mut work = value.clone();
    let mut previous_pivot = 1;
    let mut sign = 1;
    for pivot_index in 0..size - 1 {
        let Some(pivot_row) = (pivot_index..size).find(|&row| work[row][pivot_index] != 0) else {
            return 0;
        };
        if pivot_row != pivot_index {
            work.swap(pivot_row, pivot_index);
            sign = -sign;
        }
        let pivot = work[pivot_index][pivot_index];
        for row in pivot_index + 1..size {
            for column in pivot_index + 1..size {
                let numerator =
                    work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column];
                assert_eq!(numerator % previous_pivot, 0);
                work[row][column] = numerator / previous_pivot;
            }
            work[row][pivot_index] = 0;
        }
        previous_pivot = pivot;
    }
    sign * work[size - 1][size - 1]
}

fn combinations(size: usize, chosen: usize) -> Vec<Vec<usize>> {
    fn extend(
        size: usize,
        chosen: usize,
        start: usize,
        current: &mut Vec<usize>,
        result: &mut Vec<Vec<usize>>,
    ) {
        if current.len() == chosen {
            result.push(current.clone());
            return;
        }
        let needed = chosen - current.len();
        for index in start..=size - needed {
            current.push(index);
            extend(size, chosen, index + 1, current, result);
            current.pop();
        }
    }

    if chosen > size {
        return Vec::new();
    }
    let mut result = Vec::new();
    extend(size, chosen, 0, &mut Vec::new(), &mut result);
    result
}

fn determinantal_divisor(value: &Matrix, size: usize) -> Z {
    if size == 0 {
        return 1;
    }
    let (rows, columns) = dimensions(value);
    let mut divisor = 0;
    for selected_rows in combinations(rows, size) {
        for selected_columns in combinations(columns, size) {
            let minor: Matrix = selected_rows
                .iter()
                .map(|&row| {
                    selected_columns
                        .iter()
                        .map(|&column| value[row][column])
                        .collect()
                })
                .collect();
            divisor = gcd(divisor, determinant(&minor));
        }
    }
    divisor
}

fn smith_nonzero_factors(value: &Matrix) -> Vec<Z> {
    let (rows, columns) = dimensions(value);
    let mut previous_divisor = 1;
    let mut result = Vec::new();
    for size in 1..=rows.min(columns) {
        let divisor = determinantal_divisor(value, size);
        if divisor == 0 {
            break;
        }
        assert_eq!(divisor % previous_divisor, 0);
        result.push(divisor / previous_divisor);
        previous_divisor = divisor;
    }
    for pair in result.windows(2) {
        assert_eq!(pair[1] % pair[0], 0);
    }
    result
}

fn geometric_normal_link_d2() -> Matrix {
    // These are the coordinate facets of the two positive projectivized
    // normal cones.  No occurrence coefficient and no K_alt entry is read in
    // constructing this matrix.
    let facets = [[1_usize, 3, 5], [0_usize, 2, 4]];
    let mut result = zero(6, 2);
    for (top_class, directions) in facets.iter().enumerate() {
        for &direction in directions {
            result[direction][top_class] = 1;
        }
    }
    result
}

fn shift(size: usize, coefficient: Z) -> Matrix {
    let mut result = zero(size, size);
    for source in 0..size {
        result[(source + 1) % size][source] = coefficient;
    }
    result
}

fn assert_kernel_and_surjection(map: &Matrix, kernel_basis: &Matrix, right_inverse: &Matrix) {
    let (target_rank, source_rank) = dimensions(map);
    let (kernel_rows, kernel_rank) = dimensions(kernel_basis);
    let (inverse_rows, inverse_columns) = dimensions(right_inverse);
    assert_eq!(kernel_rows, source_rank);
    assert_eq!((inverse_rows, inverse_columns), (source_rank, target_rank));
    assert_eq!(multiply(map, kernel_basis), zero(target_rank, kernel_rank));
    assert_eq!(multiply(map, right_inverse), identity(target_rank));

    // A unimodular completion proves that the displayed vectors are the full
    // integral kernel, not merely a rational kernel of the correct rank.
    let completion = horizontal(kernel_basis, right_inverse);
    assert_eq!(dimensions(&completion), (source_rank, source_rank));
    assert_eq!(determinant(&completion).abs(), 1);
}

fn main() {
    let source_d2 = geometric_normal_link_d2();
    let source_d1 = matrix(QTDS);
    let source_d0 = matrix([[1, 1, 1]]);

    let target_delta = matrix([[1], [1], [1]]);
    let target_partial = matrix(TRIANGLE_BOUNDARY);
    let target_epsilon = matrix([[1, 1, 1]]);

    let fold_g2 = matrix([[1, -1]]);
    let fold_g1 = matrix(K_ALT);
    let fold_g0 = identity(3);
    let fold_g_minus_1 = identity(1);

    // The two link triangles have disjoint three-facet support and unit
    // incidence.  This is the independently geometric top boundary.
    assert_eq!(
        source_d2,
        matrix([[0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0]])
    );
    for row in &source_d2 {
        assert_eq!(row.iter().sum::<Z>(), 1);
    }
    for column in 0..2 {
        assert_eq!(source_d2.iter().map(|row| row[column]).sum::<Z>(), 3);
    }

    // Both augmented sequences are chain complexes.
    assert_eq!(multiply(&source_d1, &source_d2), zero(3, 2));
    assert_eq!(multiply(&source_d0, &source_d1), zero(1, 6));
    assert_eq!(multiply(&target_partial, &target_delta), zero(3, 1));
    assert_eq!(multiply(&target_epsilon, &target_partial), zero(1, 3));

    // Every fold square commutes.  The middle equality also rechecks the
    // independently scalar-derived factorization partial_triangle K_alt = QTDS.
    assert_eq!(
        multiply(&fold_g1, &source_d2),
        multiply(&target_delta, &fold_g2)
    );
    assert_eq!(
        multiply(&fold_g0, &source_d1),
        multiply(&target_partial, &fold_g1)
    );
    assert_eq!(
        multiply(&fold_g_minus_1, &source_d0),
        multiply(&target_epsilon, &fold_g0)
    );

    // Explicit, saturated kernels and integral right inverses in every degree.
    let kernel_2 = matrix([[1], [1]]);
    let right_inverse_2 = matrix([[1], [0]]);
    assert_kernel_and_surjection(&fold_g2, &kernel_2, &right_inverse_2);

    let kernel_1 = matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]);
    let right_inverse_1 = matrix([
        [0, 0, 0],
        [0, 0, 1],
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
        [1, 0, 0],
    ]);
    assert_kernel_and_surjection(&fold_g1, &kernel_1, &right_inverse_1);

    let kernel_0 = zero(3, 0);
    assert_kernel_and_surjection(&fold_g0, &kernel_0, &identity(3));
    let kernel_minus_1 = zero(1, 0);
    assert_kernel_and_surjection(&fold_g_minus_1, &kernel_minus_1, &identity(1));

    // On these kernel bases the only nonzero differential is the diagonal:
    // f_+ + f_- maps to k0 + k1 + k2.
    let kernel_delta = matrix([[1], [1], [1]]);
    assert_eq!(
        multiply(&source_d2, &kernel_2),
        multiply(&kernel_1, &kernel_delta)
    );
    assert_eq!(multiply(&source_d1, &kernel_1), zero(3, 3));
    assert_eq!(smith_nonzero_factors(&kernel_delta), vec![1]);

    // The triangle boundary descends canonically from
    // Z<k0,k1,k2>/Z(k0+k1+k2) to A2=ker(epsilon).  Its kernel is exactly the
    // diagonal and its saturated image is all A2, so this is an integral
    // isomorphism H1(kernel) -> A2.
    assert_eq!(multiply(&target_partial, &kernel_delta), zero(3, 1));
    assert_eq!(smith_nonzero_factors(&target_partial), vec![1, 1]);
    assert_eq!(smith_nonzero_factors(&target_epsilon), vec![1]);

    // An explicit saturated basis of ker(source_d1).  The final vector is the
    // odd-sheet top boundary; adjoining e0,e1 gives a unimodular Z^6 basis.
    let source_z1 = matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 1],
    ]);
    let cycle_complement = matrix([[1, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0]]);
    assert_eq!(multiply(&source_d1, &source_z1), zero(3, 4));
    assert_eq!(
        determinant(&horizontal(&source_z1, &cycle_complement)).abs(),
        1
    );
    assert_eq!(smith_nonzero_factors(&source_d1), vec![1, 1]);

    // Coordinates of im(d2) in the displayed cycle basis.  Their Smith form
    // is (1,1), hence H1(source)=Z^2 with no torsion.
    let d2_in_cycles = matrix([[0, 1], [0, 1], [0, 1], [1, -1]]);
    assert_eq!(multiply(&source_z1, &d2_in_cycles), source_d2);
    assert_eq!(smith_nonzero_factors(&d2_in_cycles), vec![1, 1]);

    // The first two QTDS columns form an integral basis of A2.  Thus H0 of
    // the source vanishes, as do all target homology groups.
    let a2_basis = matrix([[1, 1], [0, -1], [-1, 0]]);
    let augmentation_section = matrix([[0], [0], [1]]);
    assert_eq!(multiply(&source_d0, &a2_basis), zero(1, 2));
    assert_eq!(
        determinant(&horizontal(&a2_basis, &augmentation_section)).abs(),
        1
    );
    assert_eq!(
        matrix([
            [QTDS[0][0], QTDS[0][1]],
            [QTDS[1][0], QTDS[1][1]],
            [QTDS[2][0], QTDS[2][1]],
        ]),
        a2_basis
    );

    assert_eq!(smith_nonzero_factors(&source_d2), vec![1, 1]);
    assert_eq!(smith_nonzero_factors(&source_d0), vec![1]);
    assert_eq!(smith_nonzero_factors(&target_delta), vec![1]);

    // One boundary-label step is x_j -> x_{j+1}.  Physical tags and roads
    // rotate d_i,q_i -> d_{i+1},q_{i+1}.  Matrix equivariance then forces the
    // polarity-loaded edge action e_j -> -e_{j+1}; the geometric d2 in turn
    // forces the signed sheet swap f_+ -> -f_-, f_- -> -f_+.  Thus the two
    // signs cancel on f_+ - f_-, and the target relation generator is fixed.
    let source_action_2 = matrix([[0, -1], [-1, 0]]);
    let source_action_1 = shift(6, -1);
    let source_action_0 = shift(3, 1);
    let source_action_minus_1 = matrix([[1]]);

    let target_action_2 = matrix([[1]]);
    let target_action_1 = shift(3, 1);
    let target_action_0 = shift(3, 1);
    let target_action_minus_1 = matrix([[1]]);

    // K_alt is surjective, so this computation proves that the positive tag
    // rotation is forced rather than fitted.  It also records the sharp sign
    // correction: assigning -1 to the top target would break equivariance.
    assert_eq!(
        multiply(&fold_g1, &multiply(&source_action_1, &right_inverse_1)),
        target_action_1
    );
    assert_eq!(target_action_2, matrix([[1]]));

    let source_actions = [
        &source_action_2,
        &source_action_1,
        &source_action_0,
        &source_action_minus_1,
    ];
    let target_actions = [
        &target_action_2,
        &target_action_1,
        &target_action_0,
        &target_action_minus_1,
    ];
    for action in source_actions.into_iter().chain(target_actions) {
        assert_eq!(power(action, 6), identity(dimensions(action).0));
    }

    for exponent in 0..6 {
        let s2 = power(&source_action_2, exponent);
        let s1 = power(&source_action_1, exponent);
        let s0 = power(&source_action_0, exponent);
        let sm1 = power(&source_action_minus_1, exponent);
        let t2 = power(&target_action_2, exponent);
        let t1 = power(&target_action_1, exponent);
        let t0 = power(&target_action_0, exponent);
        let tm1 = power(&target_action_minus_1, exponent);

        assert_eq!(multiply(&s1, &source_d2), multiply(&source_d2, &s2));
        assert_eq!(multiply(&s0, &source_d1), multiply(&source_d1, &s1));
        assert_eq!(multiply(&sm1, &source_d0), multiply(&source_d0, &s0));

        assert_eq!(multiply(&t1, &target_delta), multiply(&target_delta, &t2));
        assert_eq!(
            multiply(&t0, &target_partial),
            multiply(&target_partial, &t1)
        );
        assert_eq!(
            multiply(&tm1, &target_epsilon),
            multiply(&target_epsilon, &t0)
        );

        assert_eq!(multiply(&t2, &fold_g2), multiply(&fold_g2, &s2));
        assert_eq!(multiply(&t1, &fold_g1), multiply(&fold_g1, &s1));
        assert_eq!(multiply(&t0, &fold_g0), multiply(&fold_g0, &s0));
        assert_eq!(
            multiply(&tm1, &fold_g_minus_1),
            multiply(&fold_g_minus_1, &sm1)
        );
    }

    // Static canonical JSON: its key order is the requested result-packet
    // schema.  The executable SHA is reported externally because embedding a
    // file hash in the file itself would be circular.
    println!(
        "{}",
        concat!(
            r#"{"claim":"exact integral fold from the scalar-polarity conductor normal-link complex to the augmented triangle","status":"proved","assumptions":["d1 is the independently scalar-derived entry-20/66 QTDS matrix","each parity-central vertex has the simple rank-three positive conductor normal cone with the declared dual cellular orientations"],"evidence_refs":["research/voevodsky/check_conductor_normal_link_fold.rs","research/nima/check_qtds_descent.py","research/nima/check_three_gluon_qtds_transgression.rs","research/voevodsky/check_d03_loaded_cousin_gysin_boundary.rs"],"factorization_test":{"associated_grade":"PASS","geometric_d2":["e1+e3+e5","e0+e2+e4"],"d_squared_zero":true,"fold_chain_map":true,"degreewise_surjective":true,"kernel_bases":{"degree2":["f_++f_-"],"degree1":["e0+e3","e1+e4","e2+e5"],"degree0":[],"degree-1":[]},"kernel_differential":"Delta=(1,1,1)","smith_normal_forms":{"source_d2":[1,1],"source_d1":[1,1],"source_d0":[1],"target_delta":[1],"target_partial":[1,1],"target_epsilon":[1],"kernel_delta":[1],"source_h1_relations":[1,1]},"source_homology":"H1=Z^2; all other augmented groups zero; no torsion","target_homology":"all augmented groups zero","kernel_h1_to_a2":"canonical integral isomorphism via partial_triangle","cyclic_powers_checked":6,"rotation_sign":"physical tags and roads rotate positively; polarity-loaded edges and sheets carry the compensating minus; top target is invariant"},"counterevidence":["A top-target sign -1 is incompatible with Delta and G2 in the physical positive-rotation convention.","This does not construct a full PC chain lift or the occurrence-loaded coefficient/Gysin trace between paired source edge local systems."],"next_experiment":"construct the occurrence-loaded PC coefficient/Gysin map on paired edge local systems and test its differential and factorization squares"}"#
        )
    );
}
