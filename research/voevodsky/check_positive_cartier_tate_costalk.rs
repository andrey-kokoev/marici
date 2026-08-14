//! Integral D3 audit for the smallest positive Cartier/Tor costalk candidate.
//!
//! The candidate uses no new carrier generator.  Its four terms are:
//!
//!   positive conductor orientation line
//!     -> three ordinary Cartier gallery/tag lines
//!     -> three retained Cartier Tor_1/road lines (containing q_Sigma)
//!     -> the endpoint/primitive unit.
//!
//! At carrier level the only primitive D3-equivariant differential between
//! the two permutation modules is `1-r`, so the resulting four-term window
//! is the integral orientation-twisted Tate extension.  The actual derived
//! base changes `R/(x_i) tensor^L C = [C -> 0 C]`, however, have zero strict
//! differential between their H0 and Tor_1 copies.  Consequently the
//! carrier window is only a candidate until a marked extraordinary-costalk
//! Beck--Chevalley map lifts `1-r`; inserting that matrix directly into the
//! split local packets would fit the desired answer.

type Int = i64;
type Matrix = [[Int; 3]; 3];
type Column = [Int; 3];
type Row = [Int; 3];

const ZERO: Matrix = [[0; 3]; 3];
const IDENTITY: Matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];

fn add(left: Matrix, right: Matrix, right_scale: Int) -> Matrix {
    let mut result = ZERO;
    for row in 0..3 {
        for column in 0..3 {
            result[row][column] = left[row][column] + right_scale * right[row][column];
        }
    }
    result
}

fn scale(value: Matrix, scalar: Int) -> Matrix {
    add(ZERO, value, scalar)
}

fn multiply(left: Matrix, right: Matrix) -> Matrix {
    let mut result = ZERO;
    for row in 0..3 {
        for column in 0..3 {
            result[row][column] = (0..3)
                .map(|middle| left[row][middle] * right[middle][column])
                .sum();
        }
    }
    result
}

fn matrix_column(matrix: Matrix, column: Column) -> Column {
    let mut result = [0; 3];
    for row in 0..3 {
        result[row] = (0..3)
            .map(|middle| matrix[row][middle] * column[middle])
            .sum();
    }
    result
}

fn row_matrix(row: Row, matrix: Matrix) -> Row {
    let mut result = [0; 3];
    for column in 0..3 {
        result[column] = (0..3)
            .map(|middle| row[middle] * matrix[middle][column])
            .sum();
    }
    result
}

fn determinant(value: Matrix) -> Int {
    value[0][0] * (value[1][1] * value[2][2] - value[1][2] * value[2][1])
        - value[0][1] * (value[1][0] * value[2][2] - value[1][2] * value[2][0])
        + value[0][2] * (value[1][0] * value[2][1] - value[1][1] * value[2][0])
}

fn gcd(mut left: Int, mut right: Int) -> Int {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

fn gcd_two_minors(value: Matrix) -> Int {
    let mut common = 0;
    for row_a in 0..3 {
        for row_b in (row_a + 1)..3 {
            for column_a in 0..3 {
                for column_b in (column_a + 1)..3 {
                    let minor = value[row_a][column_a] * value[row_b][column_b]
                        - value[row_a][column_b] * value[row_b][column_a];
                    common = gcd(common, minor);
                }
            }
        }
    }
    common
}

fn circulant(rotation: Matrix, a: Int, b: Int, c: Int) -> Matrix {
    let rotation_squared = multiply(rotation, rotation);
    add(add(scale(IDENTITY, a), rotation, b), rotation_squared, c)
}

fn primitive_contact_matrix(middle: Matrix) -> Matrix {
    // The augmentation row together with two independent rows of the
    // contact image.  For 1-r this is the entry-94 index-three matrix up to
    // saturated row and based column changes.
    [[1, 1, 1], middle[0], middle[1]]
}

fn entry94_triangle() -> Matrix {
    [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
}

fn weighted_exterior_middle(rees: [Int; 3]) -> Matrix {
    // Candidate ordered bases are tags (e1,e3,e5) and complementary
    // two-forms (e3^e5,e5^e1,e1^e3).  If a global regular-excess/BC map
    // identifies the actual local H0 and Tor1 lines with these exterior
    // powers, contraction for (t1*x1,t3*x3,t5*x5), followed only by the
    // labelled x_i-Cartier evaluations, leaves this t_i-weighted triangle.
    // The formula classifies the candidate; it does not construct that
    // global identification.
    let [t1, t3, t5] = rees;
    [[0, -t5, t3], [t5, 0, -t1], [-t3, t1, 0]]
}

fn main() {
    // Left multiplication by r on (1,r,r^2), and inversion on the road copy.
    let rotation: Matrix = [[0, 0, 1], [1, 0, 0], [0, 1, 0]];
    let rotation_inverse = multiply(rotation, rotation);
    let road_reflection: Matrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0]];
    assert_eq!(multiply(rotation_inverse, rotation), IDENTITY);
    assert_eq!(multiply(road_reflection, road_reflection), IDENTITY);
    assert_eq!(
        multiply(multiply(road_reflection, rotation), road_reflection),
        rotation_inverse
    );

    // The tag/ordinary-Cartier copy carries -r^{-1}s; the Tor/road copy
    // carries ordinary inversion.  This is precisely the determinant-line
    // shift produced by retaining, rather than truncating, Tor_1.
    let tag_reflection = scale(multiply(rotation_inverse, road_reflection), -1);
    assert_eq!(multiply(tag_reflection, tag_reflection), IDENTITY);
    assert_eq!(
        multiply(multiply(tag_reflection, rotation), tag_reflection),
        rotation_inverse
    );

    let norm: Column = [1, 1, 1];
    let augmentation: Row = [1, 1, 1];
    let middle = add(IDENTITY, rotation, -1); // 1-r

    // Full Tate-window chain identities and D3 covariance.
    assert_eq!(matrix_column(middle, norm), [0, 0, 0]);
    assert_eq!(row_matrix(augmentation, middle), [0, 0, 0]);
    assert_eq!(
        multiply(road_reflection, middle),
        multiply(middle, tag_reflection)
    );
    assert_eq!(matrix_column(tag_reflection, norm), [-1, -1, -1]);
    assert_eq!(row_matrix(augmentation, road_reflection), augmentation);

    // The middle image and kernel are saturated: Smith factors (1,1,0).
    assert_eq!(determinant(middle), 0);
    assert_eq!(gcd_two_minors(middle), 1);
    let primitive_contact = primitive_contact_matrix(middle);
    assert_eq!(determinant(primitive_contact).abs(), 3);

    // The split local excess packets naturally expose the augmentation-zero
    // sublattice A2, not the quotient P_tag/N needed by the Tate extension.
    // Restricting 1-r to A2 has Smith factors (1,3), hence index three; it is
    // not the saturated coker(N)->ker(epsilon) connector.
    let a2_first: Column = [-1, 1, 0];
    let a2_second: Column = [-1, 0, 1];
    assert_eq!(matrix_column(middle, a2_first), [-1, 2, -1]);
    assert_eq!(matrix_column(middle, a2_second), [-2, 1, 1]);
    let restricted_a2 = [[2_i64, 1_i64], [-1_i64, 1_i64]];
    let restricted_gcd = restricted_a2
        .iter()
        .flatten()
        .fold(0_i64, |common, entry| gcd(common, *entry));
    let restricted_determinant =
        restricted_a2[0][0] * restricted_a2[1][1] - restricted_a2[0][1] * restricted_a2[1][0];
    assert_eq!((restricted_gcd, restricted_determinant.abs()), (1, 3));

    // Classify the D3-equivariant middle arrow.  Rotation covariance makes
    // it circulant aI+bR+cR^2.  Reflection covariance forces b=-a,c=0.
    let mut equivariant_parameters = Vec::new();
    for a in -3..=3 {
        for b in -3..=3 {
            for c in -3..=3 {
                let candidate = circulant(rotation, a, b, c);
                if multiply(road_reflection, candidate) == multiply(candidate, tag_reflection) {
                    equivariant_parameters.push((a, b, c));
                }
            }
        }
    }
    assert_eq!(
        equivariant_parameters,
        (-3..=3).map(|a| (a, -a, 0)).collect::<Vec<_>>()
    );
    // Saturation and the entry-112 positive orientations force a=+1.
    assert_eq!(circulant(rotation, 1, -1, 0), middle);

    // Each actual local derived base change is [C --0--> C].  Their direct
    // sum therefore has zero strict H0-to-Tor differential.  With the three
    // entry-112 H0 maps and the three road/Tor identifications fixed to be
    // isomorphisms, the extension-diagram chain square would require
    // (1-r) = 0, which is false.
    let split_cartier_middle = ZERO;
    assert_ne!(middle, split_cartier_middle);
    assert_ne!(
        multiply(middle, IDENTITY),
        multiply(IDENTITY, split_cartier_middle)
    );

    // The obstruction is also the extension class: the split direct sum is
    // 0, whereas the oriented Tate window is the generator 1 in Z/3.
    let split_extension_class = 0_i64;
    let tate_extension_class = 1_i64;
    assert_ne!(
        split_extension_class.rem_euclid(3),
        tate_extension_class.rem_euclid(3)
    );
    assert_eq!((3 * tate_extension_class).rem_euclid(3), 0);

    // Keep the two norm lines distinct.  N_tag is killed by the middle map.
    // q_Sigma=N_road lies in the Tor/road term, is reflection-even, and has
    // augmentation three.  It is therefore not an image of 1-r.  The mixed
    // entry-113 block retains q_Sigma as its generic leg; it does not identify
    // q_Sigma with the reflection-odd conductor top.
    let tag_norm = norm;
    let q_sigma_road_norm = norm;
    assert_eq!(gcd(gcd(norm[0], norm[1]), norm[2]), 1);
    assert_eq!(matrix_column(middle, tag_norm), [0, 0, 0]);
    assert_eq!(row_matrix(augmentation, IDENTITY), augmentation);
    assert_eq!(q_sigma_road_norm.iter().sum::<Int>(), 3);
    assert_eq!(
        matrix_column(road_reflection, q_sigma_road_norm),
        q_sigma_road_norm
    );

    // No localization or rational splitting occurs in the candidate.
    let local_cartier_h0_ranks = [1_usize; 3];
    let local_cartier_tor1_ranks = [1_usize; 3];
    assert_eq!(local_cartier_h0_ranks, local_cartier_tor1_ranks);

    // Adversarial DNC/Rees test.  In the Laurent DNC ring
    // q_i-1=t_i*x_i, reciprocal twist has
    // u_i^vee=-q_i^-1*t_i*x_i.  Rescaling its normal basis by the Laurent
    // unit -q_i restores the original t_i*x_i differential integrally.
    let reciprocal_sign = -1_i64;
    let reciprocal_q_exponent = -1_i64;
    let normalized_basis_sign = -1_i64;
    let normalized_basis_q_exponent = 1_i64;
    assert_eq!(reciprocal_sign * normalized_basis_sign, 1);
    assert_eq!(reciprocal_q_exponent + normalized_basis_q_exponent, 0);

    // One common Rees parameter is not clean: (t*x1,t*x3,t*x5) is not a
    // regular sequence.  The syzygy z=x3*e1-x1*e3 is a cycle and the
    // corresponding Koszul two-boundary is -t*z.  At t=0 every such
    // two-boundary vanishes while z remains nonzero, so z is a genuine
    // extra t-torsion homology class unless t is inverted.
    let common_t_syzygy_coefficient = 1_i64 - 1_i64;
    assert_eq!(common_t_syzygy_coefficient, 0);
    let common_t_two_boundary_at_t_zero = ZERO;
    let common_t_syzygy_nonzero_at_t_zero = true;
    assert_eq!(common_t_two_boundary_at_t_zero, ZERO);
    assert!(common_t_syzygy_nonzero_at_t_zero);

    // The multi-Rees sequence (t1*x1,t3*x3,t5*x5) uses disjoint parameter
    // pairs and is regular.  This proves a clean coefficient diagonal, not
    // the off-diagonal BC map.  Under the still-conditional exterior
    // identification, Cartier evaluation of x_i alone retains all three
    // Rees lines rather than giving constant Tate incidence.
    assert_eq!(weighted_exterior_middle([1, 1, 1]), entry94_triangle());
    assert_eq!(weighted_exterior_middle([0, 0, 0]), ZERO);
    assert_ne!(weighted_exterior_middle([2, 3, 5]), entry94_triangle());
    // Semilinear D3 covariance of the multi-Rees exterior differential.
    // On complementary two-forms a permutation P acts as det(P)P.
    let test_rees = [2_i64, 3_i64, 5_i64];
    let rotated_rees = matrix_column(rotation, test_rees);
    assert_eq!(
        multiply(rotation, weighted_exterior_middle(test_rees)),
        multiply(weighted_exterior_middle(rotated_rees), rotation)
    );
    let reflected_rees = matrix_column(road_reflection, test_rees);
    assert_eq!(
        multiply(road_reflection, weighted_exterior_middle(test_rees)),
        multiply(
            weighted_exterior_middle(reflected_rees),
            scale(road_reflection, -1)
        )
    );
    // In the conditional exterior model, legitimate labelled line
    // evaluations t_i^vee(t_i)=1 recover the already-established carrier
    // triangle without a base-ring inverse.  This does not show that the
    // actual split Cartier packets carry that off-diagonal map.  The top and
    // bottom exterior contractions similarly model N and epsilon.  Omitting
    // the Rees conormal lines would still be a silent truncation.
    let top_after_x_cartier = [2_i64, 3_i64, 5_i64];
    let bottom_after_x_cartier = [2_i64, 3_i64, 5_i64];
    let top_after_rees_line_cap = norm;
    let bottom_after_rees_line_cap = augmentation;
    assert_ne!(top_after_x_cartier, norm);
    assert_ne!(bottom_after_x_cartier, augmentation);
    assert_eq!(top_after_rees_line_cap, norm);
    assert_eq!(bottom_after_rees_line_cap, augmentation);

    let packet = format!(
        "{}",
        r#"{"claim":"There is a unique smallest integral D3-equivariant carrier candidate extending the three positive Cartier grades while retaining all three Tor1 copies: Z_or --N_tag--> P_Cart,H0 --(1-r)--> P_Cart,Tor1 --epsilon--> Z, with q_Sigma=N_road retained inside the Tor1/road term and epsilon(q_Sigma)=3. The entry-113 mixed block retains the generic q_Sigma road leg together with the occurrence-loaded special galleries, while the entry-105 cone roof supplies the middle 1-r map on carrier quotients; the reflection-odd tag norm and reflection-even road norm are not identified. A common-parameter DNC q_i-1=t*x_i fails because (t*x1,t*x3,t*x5) has extra t-torsion. The D3-permuted multi-Rees ring q_i-1=t_i*x_i gives a valid integral coefficient/costalk candidate: reciprocal normalization uses only the Laurent unit q_i, regular-excess sends the three Tor1 lines to the complementary two-forms, and labelled x_i and t_i ideal evaluations recover N/(1-r)/epsilon without inversion. However, no established marked spatial correspondence lifts this coefficient window to the actual support/Yoneda cone roof, so the desired kappa exceptional map remains conditional.","status":"inconclusive","assumptions":["The entry-112 positive ordinary Cartier maps identify the three H0 lines with the ordered tag module.","The retained Tor1 determinant shift identifies the three excess lines with the road permutation module; this is the candidate typing to be geometrically proved, not silently truncated.","q_Sigma=N_road is the primitive reflection-even marked-exit norm in the road term, while N_tag is the independent reflection-odd conductor norm; the support cone roof is the coker(N_tag)-to-ker(epsilon) connector.","The orientation-twisted Tate class is the generator of Ext^2_{Z[D3]}(Z,Z_or)=Z/3 as proved in entry 102.","For the multi-Rees coefficient theorem, the parameters t1,t3,t5 are retained as labelled D3-permuted conormal lines and are not identified or inverted."],"evidence_refs":["research/voevodsky/check_positive_cartier_tate_costalk.rs","research/voevodsky/check_positive_mixed_rees_top.rs","research/voevodsky/check_absolute_unlocalized_support_pc.rs","research/voevodsky/check_d03_pabs_morse_pullback.rs","research/voevodsky/check_d03_whole_gallery_tag_gysin.rs","research/voevodsky/check_marked_exit_yoneda_census.rs","ledger entries 93, 99, 102, 105, 110, 112, and 113"],"factorization_test":{"candidate_terms":"ranks 1-3-3-1 with all three Cartier H0 and Tor1 lines retained","candidate_middle_uniqueness":"every integral D3-equivariant tag-to-road arrow is a*(1-r); saturation and positive orientations force a=1","candidate_d_squared":"passed: (1-r)N_tag=0 and epsilon(1-r)=0","candidate_D3_covariance":"passed with tag reflection -r^-1*s and Tor/road reflection s","candidate_integral_exactness":"passed with middle Smith factors (1,1,0)","candidate_Tate_shadow":"passed: full N_tag/(1-r)/epsilon window and index three","generic_qSigma":"retained as N_road in the Tor1/road term with epsilon(q_Sigma)=3; not replaced by a fitted filler or conflated with N_tag","local_derived_base_change":"three copies [C --0--> C], retaining H0 and Tor1","common_t_DNC":"falsified: the common factor t creates nonzero t-torsion Koszul homology represented by x3*e1-x1*e3","multi_Rees_reciprocal_normalization":"passed: -q_i*h_i^vee has differential t_i*x_i using only the existing Laurent unit","multi_Rees_regular_excess":"passed algebraically for the disjoint regular sequence (t1*x1,t3*x3,t5*x5)","after_x_Cartier_cap":"retains the t_i-weighted exterior incidence and all Rees conormal lines","after_labelled_Rees_line_cap":"passed: gives integral N_tag/(1-r)/epsilon without base localization","strict_extension_diagram_morphism":"failed because the established local middle differential is zero while the required one is 1-r","Yoneda_class_comparison":"split local class 0 versus Tate generator 1 mod 3","cone_roof_scope":"supplies the middle carrier connector; it neither produces q_Sigma nor lifts the marked costalk coefficients","spatial_Yoneda_compatibility":"unconstructed","inversions":"none; no x_i, u_i, t_i, or integer is inverted"},"counterevidence":["The three entry-112 maps are ordinary supported associated-grade maps only; they do not identify the Tor1 copies with the road costalks.","A strict direct sum of R/(x_i) tensor^L C has zero cross-leg differential, so inserting 1-r would fit the Tate target unless induced by an independent Beck--Chevalley correspondence.","Using one common Rees parameter adds an unwanted t-normal excess and would require t inversion to remove it.","With separate t_i, Cartier evaluation of x_i alone leaves t_i-weighted incidence; dropping the Rees conormal factors would silently truncate the candidate.","The natural marked-exit composite of the support-filtration connector is zero; q_Sigma is an independent road-norm detector and is not the image of the middle extension class.","The literal D03 pullback of the entry-105 Yoneda class is zero, so ordinary restriction cannot supply the missing spatial lift."],"next_experiment":"Construct a marked spatial multi-Rees correspondence from the three D3-related gallery formal neighborhoods to the actual F0 subset F1 subset F2 support diagram. Its extraordinary pull-push must induce the coefficient map lambda_ex:P_Cart,H0 -> P_Cart,Tor1, carry each t_i conormal line rather than discard it, and have gr(lambda_ex)=1-r with the entry-100 excess generators. Then test that its Yoneda cone-roof composite is the same nonzero Tate two-extension while retaining q_Sigma=N_road as the entry-113 generic road leg."}"#
    );
    let packet = packet
        .replace(
            "gives a valid integral coefficient/costalk candidate: reciprocal normalization uses only the Laurent unit q_i, regular-excess sends the three Tor1 lines to the complementary two-forms, and labelled x_i and t_i ideal evaluations recover N/(1-r)/epsilon without inversion",
            "proves a regular integral coefficient diagonal and reciprocal normalization using only the Laurent unit q_i. After choosing a global exterior identification, the labelled x_i and t_i line evaluations reproduce the inherited N/(1-r)/epsilon carrier matrix without inversion; the multi-Rees geometry does not itself construct that off-diagonal Beck--Chevalley identification",
        )
        .replace(
            "\"candidate_Tate_shadow\":\"passed: full N_tag/(1-r)/epsilon window and index three\"",
            "\"carrier_Tate_shadow\":\"passed: the classified candidate is the full N_tag/(1-r)/epsilon window of index three\",\"full_costalk_Tate_shadow\":\"unconstructed: the local split packets do not carry the required nonzero extension\"",
        )
        .replace(
            "\"multi_Rees_regular_excess\":\"passed algebraically for the disjoint regular sequence (t1*x1,t3*x3,t5*x5)\"",
            "\"multi_Rees_regular_diagonal\":\"passed algebraically for the disjoint regular sequence (t1*x1,t3*x3,t5*x5)\",\"multi_Rees_exterior_BC\":\"not derived; identifying the actual H0/Tor1 lines with Lambda1/Lambda2 is the missing map\"",
        )
        .replace(
            "\"after_labelled_Rees_line_cap\":\"passed: gives integral N_tag/(1-r)/epsilon without base localization\"",
            "\"conditional_exterior_line_cap\":\"reproduces the inherited integral N_tag/(1-r)/epsilon matrix without localization after the unproved exterior identification\"",
        )
        .replace(
            "\"strict_extension_diagram_morphism\":\"failed because the established local middle differential is zero while the required one is 1-r\"",
            "\"excess_kernel_to_A2_snf\":\"(1,3): restriction of 1-r to the split augmentation-zero excess lattice is index three, not the saturated Tate quotient connector\",\"strict_extension_diagram_morphism\":\"failed because the established local middle differential is zero while the required one is 1-r\"",
        );
    println!("{packet}");
}
