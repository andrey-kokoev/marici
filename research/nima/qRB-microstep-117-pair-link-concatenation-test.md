# qRB microstep 117: pair-link concatenation

The pair-response interface must preserve shell concatenation:

$$
\rho_{nm}^{[a,c]}
=
\rho_{nm}^{[a,b]}+\rho_{nm}^{[b,c]}
$$

for `a<b<c`.

It must also intertwine the pair response with the wall Laplace readout:

$$
\mathfrak L_{c_p}
\bigl(\mathcal T_{\rm pair\to link}(\rho_{nm}^{[a,b]}),u_z\bigr)
=
\int_0^\infty e^{-zt}\rho_{nm}^{[a,b]}(t)\,dt,
$$

after the separately typed endpoint-flux term is removed.

Equality on an open parameter set is required; isolated zeros are insufficient. This is the minimal source test distinguishing a genuine pair-to-wall current from a fitted shell coefficient.

Status: concatenation and Laplace-intertwining requirements isolated; the actual map remains open.
