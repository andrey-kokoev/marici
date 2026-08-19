import json

R.<u,v> = PolynomialRing(QQ)

Q = -u^4 + 4*u^3*v - 4*u^3 - 4*u^2*v + 4*u^2 - 8*u*v - 4*v^2 + 16*u + 16*v - 16
D = 4*u^4 - 4*u^3*v + 4*u^3 + 4*u^2*v - 7*u^2 + 2*u*v - 4*u + v^2 - 4*v + 4
P = u*(u-2)*(v-2)

with open("research/benincasa/bivariate_soft_gram_connection.json", "r") as handle:
    connection = json.load(handle)

au = R.fraction_field()(sage_eval(connection["connection_u"][5][5], locals={"u":u, "v":v}))
av = R.fraction_field()(sage_eval(connection["connection_v"][5][5], locals={"u":u, "v":v}))

assert au == -D.derivative(u)/(2*D)
assert av == -D.derivative(v)/(2*D)

norm_D = factor(Q.resultant(D, v))
expected_norm = -9*u^6*(4*u^2-13*u+8)*(4*u^2+5*u-8)
assert norm_D == factor(expected_norm)

# A square in QQ(Q) has square norm in QQ(u).  The two distinct quadratic
# factors occur to odd order, so D is not a square on the quartic curve.
assert gcd(4*u^2-13*u+8, 4*u^2+5*u-8) == 1

result = {
    "schema": "marici.q-marked-top-kummer-obstruction.v1",
    "top_connection": "-dlog(u*(u-2)*(v-2))",
    "e6_connection": "-1/2*dlog(D)",
    "D": str(D),
    "norm_D_on_Q": str(norm_D),
    "D_square_in_QQ_Q": False,
    "rational_embedding_into_e6": False,
    "rational_match_to_algebraic_quotient": "g=1/(P*D)",
}

with open("research/nima/q-marked-top-kummer-obstruction.json", "w") as handle:
    json.dump(result, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(json.dumps(result, indent=2, sort_keys=True))
