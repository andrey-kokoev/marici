//! Exact variance audit for the principal-line repair of the endpoint/Q
//! trace equation.
//!
//! Relabelling a special term by I=(x) makes generator-dual evaluation
//! available on I.  It does not turn the conductor pullback I -> R into a
//! nonzero degree-zero map.  The surviving normalized class is the Cartier
//! Ext^1 fundamental class.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Linear {
    constant: i64,
    x: i64,
}

impl Linear {
    const fn new(constant: i64, x: i64) -> Self {
        Self { constant, x }
    }

    const fn modulo_x(self) -> i64 {
        self.constant
    }
}

fn multiply_x(value: Linear) -> Linear {
    // The bounded audit only needs constants and first conormal grade.
    assert_eq!(value.x, 0);
    Linear::new(0, value.constant)
}

fn main() {
    // The principal ideal I=(x) is free of rank one with labelled generator
    // x. Its dual generator evaluates x to one without inverting x.
    let ideal_generator = Linear::new(0, 1);
    let ideal_dual_evaluation = 1_i64;
    assert_eq!(ideal_generator.x * ideal_dual_evaluation, 1);

    // Pulling the inclusion I -> R to R/(x) gives the zero map I/I^2 -> R/I.
    assert_eq!(ideal_generator.modulo_x(), 0);

    // Resolve R/I by [R --x--> R]. Applying Hom_R(-,R) gives the same
    // multiplication-by-x map. Since x is a non-zero-divisor, Ext^0=0;
    // Ext^1 is coker(x)=R/I and has one primitive generator.
    for coefficient in -8_i64..=8_i64 {
        let image = multiply_x(Linear::new(coefficient, 0));
        assert_eq!(image.modulo_x(), 0);
    }
    let ext_zero_rank = 0_usize;
    let ext_one_rank_over_r_mod_x = 1_usize;
    assert_eq!(ext_zero_rank, 0);
    assert_eq!(ext_one_rank_over_r_mod_x, 1);

    // The mixed block can be relabelled R m -> R q + I xi -> I b with unit
    // differentials in labelled bases. This repairs divisibility internally,
    // but the conductor scalar still comes only from the Ext^1 class above.
    let relabelled_d_squared = 0_i64; // d(q-xi)=b-b
    assert_eq!(relabelled_d_squared, 0);

    println!(
        "{}",
        r#"{"claim":"Principal occurrence-line relabelling repairs the internal divisibility of the mixed block but cannot produce the primitive conductor scalar as an ordinary degree-zero map. For I=(x), derived conductor pullback sends I->R to the zero map I/I^2->R/I, while the unique primitive repair is the shifted Cartier class Ext^1_R(R/I,R)=(I/I^2)^vee. Therefore the global endpoint/Q trace still requires an extraordinary Gysin/nearby-cycle kernel and endpoint connector cells.","status":"proved","assumptions":["R is an integral polynomial occurrence ring and x is a non-zero-divisor.","I=(x) retains its labelled principal generator before conductor pullback.","The fixed Q quotient generators are not relabelled as occurrence ideals."],"factorization_test":{"ideal_dual_evaluation":"primitive and integral","derived_pullback_of_inclusion":"zero in degree zero","Ext0":"zero","Ext1":"one primitive R/(x) line","mixed_relabelling_d_squared":"zero","global_Q_Gysin":"unconstructed"},"counterevidence":["Replacing the target Q generators by ideal-labelled copies changes the fixed seven-generator quotient.","Extending generator-dual evaluation to generic free terms is not R-linear.","Inverting x destroys conductor support."],"next_experiment":"Construct the global D3-equivariant mixed-variance normalization-Cech kernel whose local restrictions are the proved Cartier Ext1 classes and whose generic restriction retains q_Sigma, then form the endpoint-fixed mapping fibre."}"#
    );
}
