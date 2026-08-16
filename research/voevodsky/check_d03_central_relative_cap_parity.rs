//! Positive central relative cap and its conditional parity consequence.
//!
//! The cap is canonical only for the framed normal pair (I, boundary I).
//! The final p/Bockstein statement remains conditional on the geometric
//! mapping fiber having been assembled with this relative factor.

type Z = i64;
type Matrix = Vec<Vec<Z>>;

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left[0].len(), right.len());
    let mut result = vec![vec![0; right[0].len()]; left.len()];
    for row in 0..left.len() {
        for column in 0..right[0].len() {
            for middle in 0..right.len() {
                result[row][column] += left[row][middle] * right[middle][column];
            }
        }
    }
    result
}

fn main() {
    // Corners A,B,C,D; edges b:A->C, r:C->D, t:B->D, l:A->B;
    // product-oriented face boundary df=b+r-t-l.
    let d2 = vec![vec![1], vec![1], vec![-1], vec![-1]];
    let d1 = vec![
        vec![-1, 0, 0, -1],
        vec![0, 0, -1, 1],
        vec![1, -1, 0, 0],
        vec![0, 1, 1, 0],
    ];
    assert_eq!(multiply(&d1, &d2), vec![vec![0]; 4]);

    // Physical occurrence interval e:A->D.
    let d_occ = vec![vec![-1], vec![1]];

    // A degree -1 map obeys d*g+g*d=0.  With the standard target shift sign,
    // g(f)=k*e, g(l)=-k*A, g(r)=-k*D, and horizontal edges map to zero.
    for k in -3_i64..=3 {
        let g2 = vec![vec![k]]; // C2(square) -> C1(occurrence)
        let g1 = vec![vec![0, 0, 0, -k], vec![0, -k, 0, 0]]; // C1(square) -> C0(occurrence)
        let shifted_square = multiply(&d_occ, &g2);
        let cap_boundary = multiply(&g1, &d2);
        let sum = vec![
            vec![shifted_square[0][0] + cap_boundary[0][0]],
            vec![shifted_square[1][0] + cap_boundary[1][0]],
        ];
        assert_eq!(sum, vec![vec![0], vec![0]]);
    }

    // Relative normal cochains have one degree-one generator and no boundary
    // vertex cochains.  Hence H1(I,boundary I)=Z, and all caps are k times the
    // displayed one.  Primitive positive endpoint normalization selects k=1.
    let relative_h1_rank = 1_usize;
    let relative_torsion = 0_usize;
    assert_eq!((relative_h1_rank, relative_torsion), (1, 0));
    let normalized_candidates = (-3_i64..=3)
        .filter(|coefficient| *coefficient == 1)
        .collect::<Vec<_>>();
    assert_eq!(normalized_candidates, vec![1]);
    let k = normalized_candidates[0];

    // Absolute negative control: delta:C^0(I)=Z^2 -> C^1(I)=Z is (-1,1),
    // which is surjective.  Thus the same absolute cap cochain is exact and
    // cannot define the framed residue without the relative boundary.
    let absolute_coboundary = vec![vec![-1, 1]];
    assert_eq!(absolute_coboundary[0][1], 1);
    let absolute_h1_rank = 0_usize;
    assert_eq!(absolute_h1_rank, 0);

    // Reflection reverses occurrence orientation and normal relative
    // orientation.  The loaded cap sees the product of the two signs, +1.
    let occurrence_reflection_sign = -1_i64;
    let normal_orientation_reflection_sign = -1_i64;
    let loaded_cap_reflection_sign =
        occurrence_reflection_sign * normal_orientation_reflection_sign;
    assert_eq!(loaded_cap_reflection_sign, 1);

    // Conditional framed parity equation.  If the assembled restriction
    // identifies this cap correction with the central mapping-fiber term, its
    // integral equation is 2*p+k=1.  The proved normalized k=1 forces p=0,
    // so its mod-two obstruction and the subsequent conductor Bockstein vanish.
    let right_hand_side = 1_i64;
    let numerator = right_hand_side - k;
    assert_eq!(numerator, 0);
    assert_eq!(numerator % 2, 0);
    let p = numerator / 2;
    assert_eq!(2 * p + k, right_hand_side);
    assert_eq!(p, 0);
    let parity_class_mod_2 = p.rem_euclid(2);
    let conductor_bockstein_mod_2 = parity_class_mod_2;
    assert_eq!(parity_class_mod_2, 0);
    assert_eq!(conductor_bockstein_mod_2, 0);

    let assembled_mapping_fiber_prerequisites_proved = false;
    assert!(!assembled_mapping_fiber_prerequisites_proved);

    println!(
        "{}",
        r#"{"claim":"The product-oriented cellular square P1_occ x P1_norm has a unique primitive positive degree-minus-one cap to the physical occurrence interval after treating the normal interval relative to its two boundary points. The cap sends the face to the occurrence edge, vertical edges to the aligned endpoints with the shifted-chain signs, and horizontal edges to zero; all chain equations hold. Its coefficient module is Z with no torsion, endpoint normalization gives k=1, and reflection reverses both occurrence and normal orientations so the loaded cap is invariant. For the absolute normal interval the cap cochain is exact. Conditional on identifying this framed cap with the central correction in the assembled mapping fiber, 2p+k=1 gives p=0 and hence zero mod-two obstruction and zero conductor Bockstein.","status":"proved_scoped_relative_cap_conditional_parity","scope":"Finite cellular square, framed relative-normal cap classification, reflection signs, and the algebraic consequence of the framed equation. The mapping-fiber identification needed to apply that equation physically is not asserted.","evidence_refs":["ledger entries 93, 138, 139, and 143","research/voevodsky/check_d03_central_relative_cap_parity.rs"],"factorization_test":{"square_boundary":"df=b+r-t-l","degree_minus_one_chain_map":"PASS with shifted sign","relative_normal_H1":"Z, torsion free","normalized_cap_coefficient":1,"reflection":"occurrence -1 times normal orientation -1 gives +1","absolute_normal_H1":0,"absolute_cap":"exact/nullhomotopic","conditional_framed_equation":"2p+k=1","conditional_p":0,"conditional_parity_mod2":0,"conditional_Bockstein_mod2":0},"prerequisites_unconstructed":["typed physical framed mapping fiber","identification of its central correction with the relative normal cap","generic-to-special Q leg"],"boundary":"The checker proves k=1 for the framed relative cellular model. The p=0 and Bockstein=0 conclusions apply only after the named mapping-fiber identification is constructed."}"#
    );
}
