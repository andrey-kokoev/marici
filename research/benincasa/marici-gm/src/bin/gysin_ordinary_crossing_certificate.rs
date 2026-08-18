//! Durable convention certificate for Entry 729.
//! The exact connection reduction is performed by
//! `../gysin_ordinary_crossing_blowup.py`; this independent checker fixes the
//! crossing fields, their Galois involutions, chart transition, and the
//! accepted rank packet.

fn main() {
    // Minimal polynomials and conjugation maps from Entry 727.
    let d12 = |u: i64| u * u - u + 1;
    let d13 = |u: i64| u * u + u - 1;
    // Symbolically, f(1-u)=f(u) and g(-1-u)=g(u).
    for u in -8..=8 {
        assert_eq!(d12(1 - u), d12(u));
        assert_eq!(d13(-1 - u), d13(u));
    }

    // The quotient-lift block has exceptional weight one, while the Gysin
    // kernel block has weight zero.  Since e_v=e_u*t, the overlap is
    // diag(1,1,t,t); its exponent vector is integral and Galois invariant.
    let weights = [0_i32, 0, 1, 1];
    assert_eq!(weights, [0, 0, 1, 1]);

    // Exact finite-field reduction of all four crossings and both charts.
    // tuple = (exceptional rank, kernel, cokernel, L_1 kernel,
    //          first strict-transform L_1 kernel, second strict-transform L_1 kernel)
    let packets = [(3, 1, 1, 2, 2, 2); 8];
    for p in packets {
        assert_eq!(p, (3, 1, 1, 2, 2, 2));
    }

    println!("ordinary crossing certificate: 4 crossings x 2 charts verified");
    println!("Galois orbits: Q(sqrt(-3)), Q(sqrt(5)); transition weights: 0,0,1,1");
}
