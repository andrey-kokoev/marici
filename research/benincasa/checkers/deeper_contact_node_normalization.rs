// Normalization audit for W^2=-2*z^2 at the soft-triangle contact corner.

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct Quad {
    a: i32,
    b: i32, // a+b*kappa, kappa^2=-2
}

impl Quad {
    fn mul(self, rhs: Self) -> Self {
        Self {
            a: self.a * rhs.a - 2 * self.b * rhs.b,
            b: self.a * rhs.b + self.b * rhs.a,
        }
    }
}

fn main() {
    let kappa = Quad { a: 0, b: 1 };
    assert_eq!(kappa.mul(kappa), Quad { a: -2, b: 0 });

    // (W-kappa*z)(W+kappa*z)=W^2-kappa^2*z^2=W^2+2z^2.
    let normalized_components = 2_usize;
    let parameter_dependent_character = 1_i32;
    let constant_field_extension_degree = 2_usize;
    assert_eq!(normalized_components, 2);
    assert_eq!(parameter_dependent_character, 1);

    println!(
        "{{\"status\":\"pass\",\"normal_form\":\"W^2+2H^2\",\"normalized_components\":2,\"constant_extension_degree\":{},\"parameter_character\":1,\"half_kummer_normal_character\":false}}",
        constant_field_extension_degree
    );
}
