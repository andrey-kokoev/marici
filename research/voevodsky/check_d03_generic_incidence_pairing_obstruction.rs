//! Exact finite falsifier for a primitive D03 generic-incidence pairing.
//!
//! The occurrence variable `x3` remains polynomial and noninvertible.  The
//! normal parameter `u_D` may have negative exponent only in the indicated
//! target Cech summand.  Matching source and target incidence signs therefore
//! do not, by themselves, produce a primitive chain pairing.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Monomial {
    coefficient: i8,
    x3: i8,
    x_d: i8,
    u_d: i8,
}

impl Monomial {
    const fn new(coefficient: i8, x3: i8, x_d: i8, u_d: i8) -> Self {
        Self {
            coefficient,
            x3,
            x_d,
            u_d,
        }
    }

    const fn legal_source(self) -> bool {
        self.x3 >= 0 && self.x_d >= 0 && self.u_d >= 0
    }

    const fn legal_target_cech(self) -> bool {
        self.x3 >= 0 && self.x_d >= 0
    }

    const fn multiply_x3(self) -> Self {
        Self::new(self.coefficient, self.x3 + 1, self.x_d, self.u_d)
    }

    const fn multiply_target_incidence(self, incidence_sign: i8) -> Self {
        Self::new(
            self.coefficient * incidence_sign,
            self.x3,
            self.x_d + 1,
            self.u_d - 1,
        )
    }

    const fn negate(self) -> Self {
        Self::new(-self.coefficient, self.x3, self.x_d, self.u_d)
    }

    const fn conductor_zero(self) -> bool {
        self.x3 > 0
    }
}

fn chain_equation_holds(a: Monomial, k: Monomial, incidence_sign: i8) -> bool {
    a.multiply_x3() == k.multiply_target_incidence(incidence_sign).negate()
}

fn main() {
    let target_incidence = Monomial::new(1, 0, 1, -1);
    assert!(target_incidence.legal_target_cech());
    assert!(!target_incidence.legal_source());

    // Both source [top<D03] and target top->D03 incidences have sign +1.
    // For k=+/-1, the target term has x3 exponent zero, whereas x3*a has
    // positive x3 exponent for every legal polynomial a.
    for primitive_sign in [-1_i8, 1_i8] {
        let primitive_k = Monomial::new(primitive_sign, 0, 0, 0);
        assert!(primitive_k.legal_source());
        for coefficient in -4_i8..=4 {
            for x_d in 0_i8..=3 {
                for u_d in -3_i8..=1 {
                    let candidate_a = Monomial::new(coefficient, 0, x_d, u_d);
                    assert!(candidate_a.legal_target_cech());
                    assert!(!chain_equation_holds(candidate_a, primitive_k, 1));
                }
            }
        }
        assert!(!primitive_k.conductor_zero());
        assert!(primitive_k.multiply_target_incidence(1).legal_target_cech());
    }

    // The smallest monomial solution is k=x3 and
    // a=-(X_D/u_D) for the matching positive incidence convention.
    let smallest_k = Monomial::new(1, 1, 0, 0);
    let smallest_a = Monomial::new(-1, 0, 1, -1);
    assert!(smallest_k.legal_source());
    assert!(smallest_a.legal_target_cech());
    assert!(chain_equation_holds(smallest_a, smallest_k, 1));
    assert!(smallest_k.conductor_zero());

    // Reversing the target incidence reverses a, but never removes x3 from k.
    assert!(chain_equation_holds(smallest_a.negate(), smallest_k, -1));

    println!(
        "{}",
        r#"{"claim":"Matching +1 source [top<D03] and target top-to-D03 Q incidences fix only the associated-grade orientation sign. Over the legal unlocalized occurrence/target-Cech coefficients, the chain equation x3*a + (X_D/u_D)*k=0 has no primitive unit solution k=+/-1; its smallest monomial solution is k=x3 and a=-X_D/u_D (with both signs reversed together under orientation reversal). Principal-ideal-dual evaluation can send x3 to 1 only after changing to an extraordinary shifted variance and is not a global incidence pairing.","status":"falsified","scope":"incidence-only derivation of a primitive D03 generic pairing; no falsification of a separately constructed graph-DNC primal correspondence or extraordinary Cartier/Gysin trace","source_packet":{"generator":"q_J","differential":"d(q_J)=x3*d(xi_tilde)","matched_incidence":"coefficient of [top<D03] is +1"},"target_packet":{"generators":["n_D03","p_D03"],"differential":"d(n_D03)=+(X_D03/u_D03)*p_D03","cech_rule":"u_D03^-1 occurs only targetwise; x3 is never inverted"},"factorization_test":{"primitive_k_plus_or_minus_one":"FAIL by x3=0 specialization and exponent divisibility","smallest_monomial_solution":"PASS: k=x3, a=-X_D03/u_D03","orientation_reversal":"PASS: reverses a but retains the x3 factor in k","matching_incidence_signs":"PASS: fixes sign only","principal_ideal_dual":"OUTSIDE SCOPE: changes variance and degree; not a global chain/support map"},"evidence_refs":["ledger entry 143","ledger entry 156","ledger entry 157","ledger entry 159","proposed ledger entry 160","research/voevodsky/check_d03_pabs_morse_pullback.rs","research/voevodsky/check_global_k6_koszul_cech_promotion.rs","research/voevodsky/check_primal_zero_section_trace_obstruction.rs","research/voevodsky/check_d03_generic_incidence_pairing_obstruction.rs"],"counterevidence":["Inverting x3 would solve the scalar equation but erase conductor support.","Evaluating (x3)^vee tensor x3 to 1 is an extraordinary Cartier/Gysin operation, not a consequence of matching cellular incidences."],"next_experiment":"Construct the one-road pre-quotient graph multi-DNC primal correspondence and test its localization triangle while retaining the nonzero Q leg and entry-131 shifted costalk."}"#
    );
}
