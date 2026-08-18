//! Finite dual-number audit for the Cartier-filtration receiving complex.
//!
//! Work over R = Q[z]/(z^2).  A normalized exact block has differential
//! d_E(s) = z A s.  Ambient reduction cannot map it to
//! [R --z^2--> R], but it maps canonically to
//! [R/(z) --z--> R].

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct Dual {
    c: i64,
    z: i64,
}

impl Dual {
    fn mul_z(self) -> Self {
        Self { c: 0, z: self.c }
    }
}

fn standard_target_compatible(a: i64) -> bool {
    // In R, z^2=0. Compatibility with degree-zero identity would require
    // z A = z^2 h = 0 for some h.
    Dual { c: a, z: 0 }.mul_z() == Dual { c: 0, z: 0 }
}

fn cartier_target_compatible(a: i64, source: Dual) -> bool {
    // f_{-1} is A mod z, delta is multiplication by z, and f_0=id_R.
    let left = Dual { c: a * source.c, z: 0 }.mul_z();
    let right = Dual { c: a * source.c, z: a * source.z }.mul_z();
    left == right
}

fn main() {
    let samples = [
        Dual { c: 1, z: 0 },
        Dual { c: 0, z: 1 },
        Dual { c: 3, z: -2 },
    ];

    let even_ok = samples.iter().copied().all(|s| cartier_target_compatible(0, s));
    let odd_ok = samples.iter().copied().all(|s| cartier_target_compatible(1, s));

    assert!(standard_target_compatible(0));
    assert!(!standard_target_compatible(1));
    assert!(even_ok && odd_ok);

    println!(
        "{{\"ring\":\"Q[z]/(z^2)\",\"standard_doubled_resolution_receives_odd_map\":false,\"cartier_filtration_complex\":\"[R/(z) --z--> R]\",\"receives_even_map\":{},\"receives_odd_map\":{},\"source_degree_map\":\"A mod z\",\"even_A\":0,\"odd_A\":1,\"homotopy_fiber_cohomology\":\"NOT_YET_COMPUTED\"}}",
        even_ok, odd_ok
    );
}
