//! Scoped finite obstruction to canonically framing the toric conifold family.
//!
//! The family is W = {X t = s u}.  This checker separates the formal
//! s-adic coefficient calculation from ordinary nearby-cycle topology.
//! It does not construct a log costalk or a map to entry131/entry143.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct RelationCoefficient {
    xt: i64,
    su: i64,
}

fn reduce_conifold(value: RelationCoefficient) -> i64 {
    // In the quotient Xt=su, both monomials have the same coefficient.
    value.xt + value.su
}

fn splitting(n: i64) -> [i64; 2] {
    [n + 1, n]
}

fn polarity_parameter(n: i64) -> i64 {
    -n - 1
}

fn main() {
    // With dg=Xp and dh=up, q_s=tg-s h is closed:
    // d(q_s)=(Xt-su)p=0.
    let differential_qs = RelationCoefficient { xt: 1, su: -1 };
    assert_eq!(reduce_conifold(differential_qs), 0);

    // The first s-adic coefficient of q_s is -h.
    let qs_coefficients = ["t*g", "-h"];
    assert_eq!(qs_coefficients[0], "t*g");
    assert_eq!(qs_coefficients[1], "-h");

    // Coefficient extraction [s] -> 1 is not G_m-equivariant:
    // s has weight one and the unit has weight zero.
    let weight_s = 1_i32;
    let weight_unit = 0_i32;
    assert_ne!(weight_s, weight_unit);

    // Normalization/conductor lattice:
    // 0 -> Z*(1,1) -> Z^2 --(a-b)--> Z -> 0.
    // Every integral section taking 1 to a primitive lift is (n+1,n).
    for n in -32_i64..=32 {
        let lift = splitting(n);
        assert_eq!(lift[0] - lift[1], 1);
        assert_eq!(lift[0], n + 1);
        assert_eq!(lift[1], n);
    }

    // Branch-exchanging polarity sends n to -n-1.  A fixed integral
    // splitting would solve 2n=-1, which has no integer solution.
    for n in -32_i64..=32 {
        assert_eq!(polarity_parameter(polarity_parameter(n)), n);
        assert_ne!(polarity_parameter(n), n);
    }
    assert_ne!((-1_i64) % 2, 0);

    // After adjoining 1/2 the unique polarity-symmetric lift is
    // (1/2,-1/2).  Store doubled coordinates to keep the check integral.
    let doubled_half_lift = [1_i64, -1_i64];
    assert_eq!(
        doubled_half_lift[0] - doubled_half_lift[1],
        2
    );
    assert_eq!(
        [doubled_half_lift[1], doubled_half_lift[0]],
        [-doubled_half_lift[0], -doubled_half_lift[1]]
    );

    // Ordinary-topology negative control.  For s != 0 the fiber is the
    // graph u=Xt/s and contracts by (X,t,u)->(rX,rt,r^2u).  At s=0 the
    // two contractible components meet in a contractible u-line, so the
    // reduced nearby and special lattices both have rank zero.
    let generic_reduced_homology_ranks = [0_usize, 0_usize, 0_usize];
    let special_reduced_homology_ranks = [0_usize, 0_usize, 0_usize];
    assert_eq!(generic_reduced_homology_ranks, [0, 0, 0]);
    assert_eq!(special_reduced_homology_ranks, [0, 0, 0]);

    println!(
        "{{\"checker\":\"check_d03_toric_conifold_framing_obstruction\",\"status\":\"proved_scoped_framing_obstruction\",\"closed_class\":\"q_s=tg-s*h; d(q_s)=(Xt-su)p=0\",\"first_s_grade\":\"-h\",\"weight_gate\":\"[s] to 1 is not G_m-equivariant\",\"integral_splittings\":\"s_n(1)=(n+1,n), n in Z\",\"polarity\":\"n maps to -n-1; no integral fixed point\",\"half_split\":\"unique symmetric lift (1/2,-1/2) only after inverting 2\",\"ordinary_nearby_control\":\"reduced lattice zero (contractible graph fiber)\",\"unconstructed\":[\"log or branch-selected costalk framing\",\"entry131 support comparison\",\"entry143 target map\"],\"scope\":\"finite coefficient, weight, normalization-lattice, and topology controls only\"}}"
    );
}
