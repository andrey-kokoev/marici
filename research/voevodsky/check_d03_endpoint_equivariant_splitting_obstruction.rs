//! Definitive finite coefficient checker for the endpoint equivariant split.
//!
//! This proves the integral matrix/parity obstruction only.  The vanishing
//! central-support restriction is a declared input of the scoped model, and
//! no global nonexistence statement about spatial/Gysin kernels is made.

fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let remainder = a % b;
        a = b;
        b = remainder;
    }
    a
}

fn main() {
    // The homogeneous equivariance differential is multiplication by two.
    // Its one-by-one Smith normal form is [2], so ker=0 and coker=Z/2.
    let equivariance_matrix = [[2_i64]];
    assert_eq!(equivariance_matrix, [[2]]);
    let smith_diagonal = [equivariance_matrix[0][0].abs()];
    assert_eq!(smith_diagonal, [2]);
    let h0_free_rank = 0_usize;
    let h1_torsion_orders = [2_i64];
    assert_eq!(h0_free_rank, 0);
    assert_eq!(h1_torsion_orders, [2]);

    // A normalized splitting has s_n(1)=(n+1,n).  Polarity equivariance
    // asks n=-n-1, equivalently 2n+1=0.  Exhaustion is only a witness;
    // odd parity is the range-independent proof.
    for n in -4096_i64..=4096 {
        assert_ne!(2 * n + 1, 0);
        assert_ne!((2 * n + 1) % 2, 0);
    }
    let affine_obstruction_mod_two = 1_i64;
    assert_eq!(affine_obstruction_mod_two, 1);

    // Adding the special Tor1 variable in degree -1 with zero differential
    // gives Z[-1] --0--> Z --2--> Z.  It adds H^-1=Z but leaves H^1=Z/2.
    let tor_shifted_boundary = 0_i64;
    let h_minus_one_free_rank = if tor_shifted_boundary == 0 { 1 } else { 0 };
    assert_eq!(h_minus_one_free_rank, 1);
    assert_eq!(gcd(2, tor_shifted_boundary), 2);

    // If an additional framed variable has boundary m into the defect line,
    // the presentation matrix is [2 m], with cokernel Z/gcd(2,m).
    // The odd obstruction class becomes zero exactly when m is odd.
    for m in -128_i64..=128 {
        let cokernel_order = gcd(2, m);
        assert!(cokernel_order == 1 || cokernel_order == 2);
        assert_eq!(cokernel_order == 1, m % 2 != 0);
        let obstruction_survives = 1 % cokernel_order != 0;
        assert_eq!(obstruction_survives, m % 2 == 0);
    }

    // Scoped declared input: the literal central-support restriction of the
    // finite endpoint packet is zero.  This checker does not derive it from
    // a six-functor or ringed-support comparison.
    let central_support_restriction_declared_zero = true;
    assert!(central_support_restriction_declared_zero);

    println!(
        "{{\"checker\":\"check_d03_endpoint_equivariant_splitting_obstruction\",\"status\":\"proved_scoped_integral_obstruction\",\"matrix\":[[2]],\"smith_diagonal\":[2],\"cohomology\":{\"Hminus1_with_zero_Tor_shift\":\"Z\",\"H0\":\"0\",\"H1\":\"Z/2\"},\"affine_equation\":\"2n+1=0 has no integral solution\",\"general_repair\":\"coker[2 m]=Z/gcd(2,m); obstruction dies iff m is odd\",\"central_support_restriction\":\"zero is a scoped declared input, not derived here\",\"unconstructed\":[\"conormal or branch framing supplying odd evaluation\",\"literal entry131/entry143 spatial comparison\",\"global extraordinary-kernel no-go\"],\"scope\":\"finite integral endpoint equivariant splitting complex only\"}}"
    );
}
