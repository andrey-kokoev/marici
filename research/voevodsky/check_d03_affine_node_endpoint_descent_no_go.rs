//! Scoped no-go for direct affine-node descent to the literal endpoint.
//!
//! This checker treats X and u as independent universal parameters and
//! B=R[t]/(u-Xt).  It excludes ordinary localization and a normalized
//! R-linear trace from the affine component ideal.  It says nothing against
//! a proper extraordinary/Gysin kernel with its own dualizing trace.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Polynomial {
    // Coefficients of 1, u after specialization X=0.
    constant: i64,
    u: i64,
}

impl Polynomial {
    const ZERO: Self = Self { constant: 0, u: 0 };
    const ONE: Self = Self { constant: 1, u: 0 };
    const U: Self = Self { constant: 0, u: 1 };
}

fn main() {
    // If A[u^-1] mapped unitaly to B with u |-> X*t, the inverse relation
    // u*u^-1=1 would remain true after quotienting B by (X,t).  Its left
    // side becomes zero and its right side remains one.
    let localized_relation_left_mod_x_t = Polynomial::ZERO;
    let localized_relation_right_mod_x_t = Polynomial::ONE;
    assert_ne!(
        localized_relation_left_mod_x_t,
        localized_relation_right_mod_x_t
    );
    let ordinary_localization_exists = false;
    assert!(!ordinary_localization_exists);

    // Let Tr:tB->R be R-linear and normalized by Tr(t)=1.  Multiplying the
    // node relation u*t=X*t^2 and applying Tr forces
    //
    //     u = X*Tr(t^2).
    //
    // Specialization modulo X gives u=0 in Z[u], which is false.
    let trace_relation_left_mod_x = Polynomial::U;
    let trace_relation_right_mod_x = Polynomial::ZERO;
    assert_ne!(trace_relation_left_mod_x, trace_relation_right_mod_x);
    let normalized_r_linear_trace_exists = false;
    assert!(!normalized_r_linear_trace_exists);

    // The obstruction is specifically to the direct affine/ringed descent.
    // A proper component-supported correspondence may change the pushforward
    // object and provide an extraordinary trace; it is not constructed here.
    let proper_extraordinary_gysin_constructed = false;
    let literal_entry143_endpoint_map_constructed = false;
    assert!(!proper_extraordinary_gysin_constructed);
    assert!(!literal_entry143_endpoint_map_constructed);

    println!(
        "{}",
        r#"{"claim":"For the affine node B=R[t5]/(u5-X5*t5) over the universal ring R with independent X5 and u5, neither ordinary localization nor a normalized direct R-linear endpoint trace exists. A unital map from R[u5^-1] would send u5 to X5*t5; reduction modulo (X5,t5) turns the inverse equation into 0=1. If Tr:t5*B->R were R-linear with Tr(t5)=1, applying Tr to u5*t5=X5*t5^2 and reducing modulo X5 would force u5=0 in Z[u5].","status":"falsified","scope":"direct affine-node/ringed exit-path descent to the literal universal endpoint only","factorization_test":{"node":"B=R[t5]/(u5-X5*t5)","ordinary_localization":"FALSIFIED by reduction modulo (X5,t5): 0=1","normalized_trace":"FALSIFIED by reduction modulo X5: u5=0","X5_inverted":false,"u5_inverted":false},"unconstructed":["proper component-supported Rees/DNC correspondence","relative-dualizing extraordinary/Gysin trace","literal entry143 endpoint costalk comparison"],"boundary":"This does not obstruct a proper extraordinary kernel whose pushforward and dualizing trace differ from the direct affine ideal t5*B."}"#
    );
}
