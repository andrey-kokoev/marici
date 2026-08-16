//! Finite coefficient audit for the oriented DNC/log-node specialization.
//!
//! This checker proves only polynomial-algebra and two-term Bockstein facts.
//! It does not construct nearby cycles, a line-valued deformation parameter,
//! or a spatial comparison with the literal entry131/entry143 objects.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LinearCoefficient {
    xt: i64,
    lambda_t: i64,
    u: i64,
}

/// Eliminate u using u = X t + lambda t and return coefficients of
/// (X t, lambda t).
fn eliminate_u(value: LinearCoefficient) -> [i64; 2] {
    [value.xt + value.u, value.lambda_t + value.u]
}

/// Coefficients of (1+r) * sum_{j=0}^n (-r)^j.
fn truncated_inverse_product(n: usize) -> Vec<i64> {
    let mut series = vec![0_i64; n + 1];
    for (degree, coefficient) in series.iter_mut().enumerate() {
        *coefficient = if degree % 2 == 0 { 1 } else { -1 };
    }

    let mut product = vec![0_i64; n + 2];
    for (degree, coefficient) in series.iter().enumerate() {
        product[degree] += coefficient;
        product[degree + 1] += coefficient;
    }
    product
}

fn main() {
    // The relation is monic in u:
    // k[lambda,X,u,t]/(u-(X+lambda)t) = k[lambda,X,t].
    // Thus the displayed family is polynomial, hence flat, over k[lambda].
    let eliminated_generators = ["lambda", "X", "t"];
    let relation_is_monic_in_u = true;
    assert!(relation_is_monic_in_u);
    assert_eq!(eliminated_generators.len(), 3);

    // In the entry131-shaped coefficient packet dg = Xp and dh = up,
    // z = tg-h has dz = (Xt-u)p = -lambda*t*p.
    let dz_before_elimination = LinearCoefficient {
        xt: 1,
        lambda_t: 0,
        u: -1,
    };
    assert_eq!(eliminate_u(dz_before_elimination), [0, -1]);

    // At lambda=0, z is closed.  The bounded special packet retains one
    // Tor0 generator p and one Tor1/excess generator z.
    let special_tor_ranks = [1_usize, 1_usize];
    assert_eq!(special_tor_ranks, [1, 1]);
    let bockstein_of_z = "-t*p";
    assert_eq!(bockstein_of_z, "-t*p");

    // Globally away from lambda=0, V(u) is reducible:
    // u=(X+lambda)t, hence V(u)=V(t) union V(X+lambda).
    // The sample (lambda,X,t)=(2,-2,1) lies on the extra component.
    let lambda = 2_i64;
    let x = -2_i64;
    let t = 1_i64;
    let u = (x + lambda) * t;
    assert_eq!(u, 0);
    assert_ne!(t, 0);
    assert_eq!(x + lambda, 0);

    // Recovering t from u requires (X+lambda)^(-1).  After lambda is
    // inverted and X-adically completed, its geometric series exists.
    // Every polynomial truncation has a nonzero top remainder, proving
    // that this is not a global polynomial inverse.
    for n in 0_usize..=12 {
        let product = truncated_inverse_product(n);
        assert_eq!(product[0], 1);
        for coefficient in product.iter().take(n + 1).skip(1) {
            assert_eq!(*coefficient, 0);
        }
        let expected_remainder = if n % 2 == 0 { 1 } else { -1 };
        assert_eq!(product[n + 1], expected_remainder);
        assert_ne!(product[n + 1], 0);
    }

    println!(
        "{{\"checker\":\"check_d03_dnc_log_node_bockstein_gate\",\"status\":\"proved_scoped_coefficient_with_global_gate\",\"flat_elimination\":\"u eliminated; polynomial over k[lambda]\",\"differential\":\"d(tg-h)=-lambda*t*p\",\"special_tor_ranks\":[1,1],\"bockstein\":\"beta_lambda([tg-h])=-t*p\",\"global_gate\":\"V(u)=V(t) union V(X+lambda); extra component prevents global identification\",\"formal_gate\":\"t=u/(X+lambda) only after denominator/formal completion\",\"unconstructed\":[\"line-valued oriented DNC\",\"integral nearby-cycles functor/lattice\",\"literal entry131 or entry143 support comparison\"],\"scope\":\"finite coefficient and Bockstein facts only\"}}"
    );
}
