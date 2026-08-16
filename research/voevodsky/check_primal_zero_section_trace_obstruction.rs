//! Exact ablation for the naive normalization zero-section trace.
//!
//! This tests ordinary conductor restriction only. It does not test the
//! sought extraordinary principal-dual-line Gysin correspondence.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Polynomial {
    constant: i64,
    x: i64,
}

impl Polynomial {
    const fn constant(value: i64) -> Self {
        Self {
            constant: value,
            x: 0,
        }
    }

    const fn multiple_of_x(coefficient: i64) -> Self {
        Self {
            constant: 0,
            x: coefficient,
        }
    }

    const fn conductor_value(self) -> i64 {
        self.constant
    }
}

fn main() {
    // The chain equation is x*T(b,n)=epsilon*T(q,p). Primitive Q framing
    // fixes T(q,p)=+/-1, but the left side belongs to the proper ideal (x).
    for orientation in [-1_i64, 1_i64] {
        let primitive_q_value = Polynomial::constant(orientation);
        for candidate_coefficient in -8_i64..=8_i64 {
            let zero_section_side = Polynomial::multiple_of_x(candidate_coefficient);
            assert_ne!(zero_section_side, primitive_q_value);
            assert_eq!(zero_section_side.conductor_value(), 0);
            assert_eq!(primitive_q_value.conductor_value(), orientation);
        }
    }

    // The obstruction is sectorwise, so D3 summation cannot cancel it.
    for orientation in [-1_i64, 1_i64] {
        assert_ne!([0_i64; 3], [orientation; 3]);
    }

    println!(
        "{}",
        r#"{"claim":"Ordinary normalization zero-section gluing cannot support a primitive primal endpoint/Q trace: the chain equation is x_i*T(b_i,n_D)=epsilon_D*T(q_i,p_D), while primitive Q framing makes the right side a unit and the left side lies in (x_i), becoming 0=+/-1 on the conductor. This is a scoped no-go for zero-section assembly, not for an extraordinary principal-dual-line Gysin correspondence.","status":"falsified","assumptions":["The occurrence ring is unlocalized and x_i is not a unit.","The mixed differential has d(q_i)=x_i*b_i.","The target differential has d(n_D)=epsilon_D*p_D.","Primitive Q framing evaluates T(q_i,p_D) to a signed unit."],"factorization_test":{"sectorwise_chain_equation":"failed","conductor_specialization":"0=+/-1","D3_sum_cancellation":"impossible sectorwise","numeric_denominators":"none","principal_dual_line_repair":"not tested and not falsified"},"counterevidence":["Inverting x_i destroys conductor support.","A principal-dual-line evaluation changes ordinary restriction into the missing extraordinary correspondence."],"next_experiment":"Construct a marked occurrence-Gysin/nearby-cycle correspondence carrying (x_i)^vee, both Tor grades, the nonzero Q leg, and both endpoint cells; then compute the endpoint-fixed mapping fibre and reflection parity."}"#
    );
}
