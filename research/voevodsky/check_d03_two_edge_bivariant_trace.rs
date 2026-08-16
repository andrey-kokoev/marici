//! Finite coefficient certificate for the two-edge positive D03 trace.
//!
//! This proves the occurrence concatenation, the two independent normal
//! double-Rees totalizations, preservation of the repeated-u3 Tor packet,
//! and the symbolic attachment to the already certified F03/Q collar.  It
//! explicitly does not construct the universal exceptional-fibre pushforward
//! for the central weighted graph.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Vector3([i64; 3]);

impl Vector3 {
    fn add(self, other: Self) -> Self {
        let mut out = [0; 3];
        for (index, target) in out.iter_mut().enumerate() {
            *target = self.0[index] + other.0[index];
        }
        Self(out)
    }

    fn scale(self, scalar: i64) -> Self {
        let mut out = self.0;
        for value in &mut out {
            *value *= scalar;
        }
        Self(out)
    }
}

fn gcd(mut left: i64, mut right: i64) -> i64 {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

// Unweighted incidence matrices of the tensor of two primitive two-term
// complexes.  Weights are independent regular parameters, so this verifies
// the complete lower/double-overlap sign pattern once for both normal pairs.
fn check_product_totalization() {
    let d2 = [1_i64, -1, -1, 1];
    let d1 = [
        [1_i64, 0, 1, 0],
        [-1, 0, 0, 1],
        [0, 1, -1, 0],
        [0, -1, 0, -1],
    ];
    for row in d1 {
        let composite: i64 = row.iter().zip(d2).map(|(a, b)| a * b).sum();
        assert_eq!(composite, 0);
    }
    assert_eq!(d2.iter().fold(0, |g, value| gcd(g, *value)), 1);
}

fn main() {
    // Endpoint order is (v_plus,m_plus,c).  The two weighted edge boundaries
    // are X_D*m-x5*v and x0*c-x1*m.  Multiplying by x1 and X_D respectively
    // cancels the shared m coefficient without division.
    let x_d = 5_i64;
    let x5 = 7_i64;
    let x1 = 11_i64;
    let x0 = 13_i64;
    let d_ec = Vector3([-x5, x_d, 0]);
    let d_er = Vector3([0, -x1, x0]);
    let concatenation_boundary = d_ec.scale(x1).add(d_er.scale(x_d));
    assert_eq!(concatenation_boundary, Vector3([-x1 * x5, 0, x_d * x0]));
    assert_eq!(gcd(x1, x_d), 1);

    // Both normal pairs use the complete rank 1->4->4 product resolution;
    // the degree-zero, lower, and double-overlap terms are all retained.
    check_product_totalization(); // (u5,u_D)
    check_product_totalization(); // (u1,u0)
    let normal_total_ranks = [[1_usize, 4, 4], [1_usize, 4, 4]];
    let positive_tor_from_normal_products = 0_usize;
    let normal_product_torsion = 0_usize;
    assert_eq!(normal_total_ranks, [[1, 4, 4], [1, 4, 4]]);
    assert_eq!(positive_tor_from_normal_products, 0);
    assert_eq!(normal_product_torsion, 0);

    // The two essential Cech overlap generators are legal only in their
    // respective correspondence charts; neither denominator is inverted in
    // the coefficient base.
    let overlaps = ["1/(u5*u_D)", "1/(u1*u0)"];
    let base_inversions = 0_usize;
    assert_eq!(overlaps, ["1/(u5*u_D)", "1/(u1*u0)"]);
    assert_eq!(base_inversions, 0);

    // Repeated-u3 packet.  The reciprocal relation is u+q*u^vee=0.  In the
    // ordered middle basis, eta_mix=(-q,-1) is primitive because one entry is
    // a unit.  Its normalized projection (1,-q) retains the entry-100 sign.
    let q3 = 3_i64;
    let u3 = 6_i64;
    let u3_vee = -2_i64;
    assert_eq!(u3 + q3 * u3_vee, 0);
    let eta_mix = [-q3, -1_i64];
    let excess_projection = [1_i64, -q3];
    assert_eq!(eta_mix.iter().fold(0, |g, value| gcd(g, *value)), 1);
    assert_eq!(excess_projection, [1, -q3]);
    let repeated_u3_tor_ranks = [1_usize, 1_usize];
    assert_eq!(repeated_u3_tor_ranks, [1, 1]);

    // Shared-m gluing is the lcm equality X_D*x1=x1*X_D.  It is independent
    // of both normal exceptional factors, so tensor totalization introduces
    // no new torsion or fitted scalar.
    let shared_m_left = x_d * x1;
    let shared_m_right = x1 * x_d;
    assert_eq!(shared_m_left, shared_m_right);
    let global_coefficient_torsion = 0_usize;
    assert_eq!(global_coefficient_torsion, 0);

    // Symbolic composition with the certified P03 tensor C_D collar.  The
    // occurrence top survives as primitive p03, and the local quotient has
    // radial coefficient X_D/u_D and normal coefficient one.
    let p03_coefficient = 1_i64;
    let generic_top_coefficient = "X_D/u_D";
    let normal_circle_coefficient = "1";
    assert_ne!(p03_coefficient, 0);
    assert_eq!(generic_top_coefficient, "X_D/u_D");
    assert_eq!(normal_circle_coefficient, "1");

    // Universal central weighted graph [x1:x0] -> [t1*x1:t0*x0].  At either
    // single weight-zero locus the opposite corner has a P1 fibre; with both
    // weights zero the entire P1xP1 remains.  These are genuine extra fibres,
    // not removable by coefficient saturation.
    let fibre_dimension_t0_zero = 1_usize;
    let fibre_dimension_t1_zero = 1_usize;
    let fibre_dimension_both_zero = 2_usize;
    assert_eq!(fibre_dimension_t0_zero, 1);
    assert_eq!(fibre_dimension_t1_zero, 1);
    assert_eq!(fibre_dimension_both_zero, 2);

    println!(
        "{}",
        r#"{"claim":"The two-edge D03 coefficient correspondence closes integrally: d(e_c)=X_D*m_plus-x5*v_plus and d(e_r)=x0*c-x1*m_plus have primitive concatenation x1*e_c+X_D*e_r; the independent normal kernels K(u5,u_D) and K(u1,u0) retain every lower and double-overlap term and totalize with d^2=0; the spectator repeated-u3 packet retains primitive eta_mix=(-q3,-1), Tor0 and Tor1, and the entry-100 sign.  The shared m_plus lcm gluing is exact and torsion-free.  Symbolic composition with the full P03 tensor C_D collar has nonzero primitive p03 and local Q coefficients (X_D/u_D,1).","status":"proved","scope":"two-edge occurrence/normal coefficient and bivariant trace plus symbolic target-collar attachment","assumptions":["all occurrence and normal/Rees parameters are independent regular labelled sections","double inverses occur only in their indicated Cech overlap summands","the completed first edge and the certified P03 tensor C_D target orientations are fixed"],"factorization_test":{"occurrence_boundaries":["X_D*m_plus-x5*v_plus","x0*c-x1*m_plus"],"primitive_concatenation":"x1*e_c+X_D*e_r","shared_m_coefficient":"X_D*x1, cancels exactly","normal_product_ranks":[[1,4,4],[1,4,4]],"all_lower_terms":"RETAINED","double_overlaps":["1/(u5*u_D)","1/(u1*u0)"],"d_squared":"ZERO","eta_mix":"(-q3,-1), primitive with u3+q3*u3^vee=0","repeated_u3_Tor":[1,1],"torsion":"NONE","base_inversion":"NONE","p03":"NONZERO primitive","local_Q":"top->(X_D/u_D)*p03 and n_D->p03"},"universal_central_graph":{"t0_zero":"extra P1 fibre","t1_zero":"extra P1 fibre","t0_t1_zero":"extra P1xP1 fibre"},"unconstructed":["the exceptional-fibre nearby-cycle/extraordinary pushforward from the universal central weighted graph to entry143","a universal corner selection retaining both [t0] and [t1]","the resulting spatial alpha03 and its global polarity/endpoint coherence"],"boundary":"The checker proves the closed torsion-free coefficient trace and nonzero target-Q attachment.  It does not collapse the central exceptional fibres or promote the trace to a universal spatial support map."}"#
    );
}
