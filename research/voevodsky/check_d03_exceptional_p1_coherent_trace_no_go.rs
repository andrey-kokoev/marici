//! Scoped coherent no-go and constructible relative positive control on P1.
//!
//! The exceptional conductor ideal J_E=O(-1) has zero coherent pushforward.
//! This checker does not identify the relative cellular class with entry143.

fn h0_rank(degree: i32) -> usize {
    (degree + 1).max(0) as usize
}

fn h1_rank(degree: i32) -> usize {
    (-degree - 1).max(0) as usize
}

fn main() {
    // Standard cohomology of O(n) on P1.
    for degree in -8..=8 {
        let expected_h0 = if degree >= 0 {
            (degree + 1) as usize
        } else {
            0
        };
        let expected_h1 = if degree <= -2 {
            (-degree - 1) as usize
        } else {
            0
        };
        assert_eq!(h0_rank(degree), expected_h0);
        assert_eq!(h1_rank(degree), expected_h1);
    }

    // Bare conductor ideal J=O(-1): Rp_*J=0.
    assert_eq!((h0_rank(-1), h1_rank(-1)), (0, 0));

    // RHom(O(-1), O(-2)[1]) = O(-1)[1], also with zero pushforward.
    let internal_hom_degree = -2 - (-1);
    assert_eq!(internal_hom_degree, -1);
    assert_eq!(
        (h0_rank(internal_hom_degree), h1_rank(internal_hom_degree)),
        (0, 0)
    );

    // The tensor variant O(-1) tensor O(-2)[1]=O(-3)[1] has R1 rank two,
    // so it cannot be a primitive scalar trace.
    assert_eq!((h0_rank(-3), h1_rank(-3)), (0, 2));

    // The actual relative dualizing complex O(-2)[1] has R1 rank one and
    // therefore the primitive Grothendieck-duality trace.
    assert_eq!((h0_rank(-2), h1_rank(-2)), (0, 1));

    // An unshifted coherent map O(-1)->O(-2) would be a section of O(-1).
    assert_eq!(h0_rank(-2 - (-1)), 0);

    // Constructible positive control.  Give P1 its one 0-cell and one 2-cell,
    // and take the marked point as the full 0-cell subcomplex.  The relative
    // chain complex has C2=Z, C1=C0=0, so its oriented top/BM class is Z.
    let relative_chain_ranks = [0_usize, 0_usize, 1_usize];
    let relative_d2_rank = 0_usize;
    let relative_h2_rank = relative_chain_ranks[2] - relative_d2_rank;
    assert_eq!(relative_chain_ranks, [0, 0, 1]);
    assert_eq!(relative_h2_rank, 1);

    let bare_coherent_unit_trace_exists = false;
    let relative_constructible_top_is_primitive = relative_h2_rank == 1;
    let literal_entry143_map_constructed = false;
    assert!(!bare_coherent_unit_trace_exists);
    assert!(relative_constructible_top_is_primitive);
    assert!(!literal_entry143_map_constructed);

    println!(
        "{}",
        r#"{"claim":"For p:P1->point and the exceptional conductor ideal J_E=O(-1), Rp_*J_E=0. Its dual variant RHom(O(-1),O(-2)[1])=O(-1)[1] also pushes to zero; the tensor variant O(-3)[1] has rank-two R1 and is not a primitive scalar trace. The actual dualizing complex O(-2)[1] has primitive rank-one R1, while Hom(O(-1),O(-2))=H0(O(-1))=0. In contrast, the relative cellular pair (P1,point) has a primitive rank-one oriented top/Borel-Moore class.","status":"falsified","scope":"bare coherent exceptional-component ideal J_E=O(-C) used as a proper unit-trace kernel","factorization_test":{"P1_line_cohomology":"H0(O(n))=max(n+1,0), H1(O(n))=max(-n-1,0)","Rp_*O(-1)":[0,0],"RHom_dual_O(-1)[1]":[0,0],"tensor_O(-3)[1]_R1_rank":2,"dualizing_O(-2)[1]_R1_rank":1,"Hom_O(-1)_to_O(-2)":0,"relative_pair_H2_rank":1},"positive_control":"constructible/log relative pair retains a primitive oriented BM top class","unconstructed":["constructible/log-BM endpoint kernel","proper comparison to literal entry143 endpoint star","endpoint butterfly connector"],"boundary":"This no-go applies only to bare coherent J_E. It does not obstruct the relative dualizing or constructible/log pair, whose spatial entry143 realization remains unconstructed."}"#
    );
}
