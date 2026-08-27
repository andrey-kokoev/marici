import cmath


def check_exponential(alpha: float, z: complex) -> None:
    # g(u)=exp(-alpha*u), c=1, and Lg=(alpha^2-1/4)g.
    integral = z / (alpha * alpha - z * z)
    green_integral = (alpha * alpha - 0.25) * integral
    lhs = green_integral
    rhs = z + (z * z - 0.25) * integral
    assert abs(lhs - rhs) < 1e-12

    bulk_plus_polar = 2 * integral + 2 * z / (z * z - 0.25)
    transported = 2 * green_integral / (z * z - 0.25)
    assert abs(bulk_plus_polar - transported) < 1e-12


for alpha in (1.0, 2.0, 5.0):
    for z in (0.1 + 0.7j, 0.4 + 3.2j, -0.2 + 1.1j):
        check_exponential(alpha, z)

print("green_operator=d2_minus_one_quarter")
print("polar_port=Dirichlet_boundary_completion")
print("next_gate=theta_source_curvature_transport")

