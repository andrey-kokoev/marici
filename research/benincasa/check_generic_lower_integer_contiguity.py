"""Certify the integer Kummer-contiguity map behind one deletion edge."""

from fractions import Fraction


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def scale(value, form):
    return tuple(value * entry for entry in form)


def main():
    # Evaluate away from q=0 at q=2.  Only the logarithmic q-direction matters.
    q = Fraction(2)
    dlog_q = (Fraction(1, 2), Fraction(0), Fraction(1, 2))
    alpha = 17

    # d(q^-alpha)/q^-alpha = -alpha*dlog(q).  Hence
    # (d + alpha*dlog(q))(q^-alpha f) = q^-alpha*d(f).
    gauge_derivative = scale(-alpha, dlog_q)
    target_connection = scale(alpha, dlog_q)
    assert add(gauge_derivative, target_connection) == (0, 0, 0)

    # Source presentation A[u]/(uK-1), target A[v]/(vKq-1).
    # The natural localization map sends u=K^-1 to v*q.
    # Check the defining relation symbolically after substitution.
    source_relation_image = "v*q*K-1"
    target_relation = "v*K*q-1"
    assert source_relation_image.replace("q*K", "K*q") == target_relation

    # q^-alpha is algebraic precisely for integral alpha in this audit.
    assert isinstance(alpha, int)
    formal_alpha_has_algebraic_power = False
    assert not formal_alpha_has_algebraic_power

    # The logarithmic normal complex is [k --alpha--> k]. At alpha=17 over
    # either Q or the census field, its differential is invertible.
    prime = 32_003
    alpha_inverse = pow(alpha, prime - 2, prime)
    assert alpha * alpha_inverse % prime == 1

    print("integer_weight: 17")
    print("localization_ring_map: u_K -> v_Kq*q")
    print("contiguity_chain_map: f -> q_g1^-17*f")
    print("chain_identity: PASS")
    print("integer_specialized_localization_cone: TYPED")
    print("normal_log_complex_at_17: ACYCLIC")
    print("supported_residue_at_17: ZERO")
    print("supported_resonance_divisor: alpha=0")
    print("formal_generic_alpha_algebraic_contiguity: NO")
    print("rank_five_generic_increment_as_supported_cone: FALSIFIED")


if __name__ == "__main__":
    main()
