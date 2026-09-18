# Many-many pair-to-wall source equation

The existing scalar wall port has the form

$$
\mathfrak L_{c_p}(f,g)
=ic_p\left(\overline{\gamma_0f}\,\eta(g)-\overline{\eta(f)}\,\gamma_0g\right).
$$

For a pair response, the source-derived comparison must determine maps

$$
\gamma_0\rho_{nm}=\rho_{nm}(0),
\qquad
\eta\rho_{nm}=\mathcal E_{nm}(R_{nm},\partial_zR_{nm}),
$$

such that

$$
\mathfrak L_{c_p}(\rho_{nm},u_z)
=\mathcal L_z(\rho_{nm})
$$

after the declared endpoint-flux subtraction.

The function `E_nm` is the missing source datum. The pair equation determines the combination

$$
 zR_{nm}-\rho_{nm}(0)-\kappa_{nm}\partial_zR_{nm},
$$

but does not by itself select its decomposition into the two scalar wall coordinates.

Status: source derivation reduced to determining one boundary-coordinate functional `E_nm`; no candidate decomposition is promoted to a theorem.
