# Common boundary-Weyl filler for the two prime-cell defects

Let `D_min` be the symmetric minimal realization of the four-component Clifford bulk operator and let

$$
(\mathcal E,\Gamma_0,\Gamma_1)
$$

be a boundary triple for `D_min^*`, so Green's identity is

$$
\langle D_{\min}^*f,g\rangle-
\langle f,D_{\min}^*g\rangle
=
\langle\Gamma_1f,\Gamma_0g\rangle_{\mathcal E}
-
\langle\Gamma_0f,\Gamma_1g\rangle_{\mathcal E}.
$$

Let `gamma(z)` be the Poisson operator and

$$
M(z)=\Gamma_1\gamma(z)
$$

its matrix Weyl function. For a self-adjoint boundary parameter `Theta`, the extension `D_Theta` satisfies Krein's formula

$$
(D_\Theta-z)^{-1}
=(D_0-z)^{-1}
+\gamma(z)(\Theta-M(z))^{-1}\gamma(\bar z)^*.
$$

The boundary characteristic is

$$
\det(\Theta-M(z)).
$$

After the odd-coordinate rescaling and complex Hadamard transform, the two local metric defects become chiral coefficients

$$
\delta_+=a-2b,
\qquad
\delta_-=a+2b.
$$

The required filler must realize these as the two diagonal boundary channels of `Theta-M(z)`. Equivalently, before chiral diagonalization its matrix coefficients must recover:

1. the common even-wall defect `a`;
2. the oriented Stokes/Wronskian defect `b`.

Source admission requires:

- the `Gamma_12` boundary variation equals the local Weil/gamma-prime current;
- the `Gamma_13` residues at the endpoint poles reproduce the transported endpoint swap/Wronskian form;
- reciprocal and cutoff maps intertwine `Gamma_0`, `Gamma_1`, and `M(z)`;
- the determinant/cofactor section maps the pointed Xi lift to the pair-to-Euler joint graph without changing multiplicity.

If both source coefficients vanish, then `a=b=0` and the four prime-cell matrix-unit identities follow. The boundary-triple construction is the higher coherence cell; it does not identify endpoint and bulk operators directly.

Status: abstract common filler and acceptance equations fixed; source construction of the boundary triple and its matrix Weyl function remains open.
