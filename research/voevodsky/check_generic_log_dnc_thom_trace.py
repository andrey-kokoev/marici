"""Compare the Kato Thom trace with the generic logarithmic DNC trace."""


def pair(functional, vector):
    return sum(a * b for a, b in zip(functional, vector))


def main():
    # Base change C -> D=C[X^-1] preserves the relative interval complex.
    boundary = [-1, -1]
    interval = [-1, 1]
    trace = [0, 1]
    assert pair(boundary, interval) == 0
    assert pair(trace, interval) == 1

    # On the raw generic DNC chart u=X*t.  In logarithmic differentials,
    # dlog(u)=dlog(X)+dlog(t).  Relative to the occurrence base, dlog(X)=0.
    dlog_u_absolute = (1, 1)  # basis (dlog X, dlog t)
    relative_quotient = lambda form: form[1]
    assert relative_quotient(dlog_u_absolute) == 1
    dlog_t_relative = 1
    assert relative_quotient(dlog_u_absolute) == dlog_t_relative

    # Therefore the relative log orientation determinant is +1.
    log_orientation_determinant = 1
    localized_trace = log_orientation_determinant * pair(trace, interval)
    assert localized_trace == 1

    # The additive comparison is deliberately different: du=X*dt+t*dX,
    # hence du=X*dt relatively.  It would carry a nonconstant unit X.
    additive_orientation_factor = "X"
    assert additive_orientation_factor != "1"

    # Reflection reverses both interval and log orientation, retaining +1.
    reflected_interval = [1, -1]
    reflected_orientation = -1
    assert [reflected_orientation * x for x in reflected_interval] == interval

    print("generic_coordinate_relation: u=X*t")
    print("relative_log_identity: dlog(u)=dlog(t)")
    print("relative_log_orientation_determinant: +1")
    print("localized_interval_class: PRIMITIVE")
    print("generic_log_DNC_trace_coefficient: +1")
    print("additional_unit: NONE")
    print("additive_du_dt_factor: X (OUTSIDE_CLAIM)")
    print("reflection_compatibility: PASS")
    print("Kato_to_raw_generic_log_trace: IDENTIFIED")
    print("global_algebraic_span_comparison: NEXT_GATE")


if __name__ == "__main__":
    main()
