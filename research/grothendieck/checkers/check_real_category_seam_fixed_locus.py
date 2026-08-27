points = (0j, 3j, -7j, 2 + 3j, -4 + 1j)


def real_involution(z):
    return -z.conjugate()


for z in points:
    assert real_involution(real_involution(z)) == z
    assert (real_involution(z) == z) == (z.real == 0)

# The seam coordinate Re(z) violates the Cauchy--Riemann equations:
# u(x,y)=x, v(x,y)=0, so u_x=1 while v_y=0.
u_x = 1
u_y = 0
v_x = 0
v_y = 0
assert not (u_x == v_y and u_y == -v_x)

print("parameter_involution=R(z)=-conjugate(z)")
print("fixed_locus=Re(z)=0")
print("seam_complex_analytic=false")
print("required_category=Real_equivariant_boundary_category")
