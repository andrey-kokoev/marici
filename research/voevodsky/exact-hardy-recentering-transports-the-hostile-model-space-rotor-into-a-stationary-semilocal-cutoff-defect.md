# Exact Hardy recentering transports the hostile model-space rotor into a stationary semilocal cutoff defect

## Objective

Transport the exact finite-Blaschke model-space rotor from the stationary Hardy chart back into the semilocal cutoff geometry.

The existing exact Hardy transport is sufficient. When a finite Blaschke factor is inserted multiplicatively into the scattering symbol, its projection defect is carried through cutoff recentering by unitary conjugation. Rank, trace norm, source compression, and dagger symmetry are therefore preserved.

## Baseline transported cutoff pair

On one angular sector, exact transport sends the physical cutoff to a fixed Hardy projection

\[
\mathcal U_\chi
P_\Lambda
\mathcal U_\chi^*
=
\Pi.
\]

Write

\[
L
=
\log\Lambda
\]

and

\[
U_L
=
M_{e^{2iLt}}.
\]

For a baseline scattering phase \(\Gamma_\chi\), the transported moving projection is

\[
Q_{L,\chi}^{base}
=
U_L
M_{\Gamma_\chi}
\Pi
M_{\Gamma_\chi}^*
U_L^*.
\]

The observer is the fixed multiplier

\[
M_{m_{g,\chi}}.
\]

## Insert the hostile divisor factor

Let

\[
B_{b,\gamma}
=
b_{\gamma,b}
b_{-\gamma,b}
\]

be the symmetry-completed degree-two Blaschke product. Define the hostile-augmented scattering phase

\[
\Gamma_\chi^{host}
=
\Gamma_\chi
B_{b,\gamma}.
\]

The corresponding transported projection is

\[
Q_{L,\chi}^{host}
=
U_L
M_{\Gamma_\chi}
M_{B_{b,\gamma}}
\Pi
M_{B_{b,\gamma}}^*
M_{\Gamma_\chi}^*
U_L^*.
\]

Because

\[
M_{B_{b,\gamma}}
\Pi
M_{B_{b,\gamma}}^*
=
\Pi
-
P_{K_{B_{b,\gamma}}},
\]

we obtain the exact relative defect

\[
\boxed{
Q_{L,\chi}^{host}
-
Q_{L,\chi}^{base}
=
-
U_L
M_{\Gamma_\chi}
P_{K_{B_{b,\gamma}}}
M_{\Gamma_\chi}^*
U_L^*.
}
\]

Thus the hostile perturbation is a rank-two projection defect at every cutoff.

## Physical cutoff defect

Transport back to the physical semilocal carrier:

\[
P_{\Lambda,\chi}^{rot}
=
\mathcal U_\chi^*
U_L
M_{\Gamma_\chi}
P_{K_{B_{b,\gamma}}}
M_{\Gamma_\chi}^*
U_L^*
\mathcal U_\chi.
\]

This is an orthogonal projection of rank two. It satisfies

\[
\boxed{
\operatorname{rank}
P_{\Lambda,\chi}^{rot}
=
2,
}
\]

\[
\boxed{
\operatorname{Tr}
P_{\Lambda,\chi}^{rot}
=
\|P_{\Lambda,\chi}^{rot}
\|_1
=
2.
}
\]

These quantities are independent of \(L\) and \(\Lambda\).

Therefore the exact transported rotor has no pro-horn trace divergence.

## Why cutoff translation causes no growth

The cutoff dependence enters only through unitary conjugation by \(U_L\). Hence

\[
P_{L,\chi}^{rot}
=
U_L
P_{0,\chi}^{rot}
U_L^*.
\]

The family need not converge strongly as \(L\to\infty\) in the unrecentered chart, but after exact Hardy recentering it is stationary.

This is the correct boundary-following notion of cutoff compatibility. Requiring an unrecentered rank-two projection to converge as its support translates would impose the wrong topology.

## Observer compression

Observer multipliers commute with both \(U_L\) and \(M_{\Gamma_\chi}\). Therefore

\[
\operatorname{Tr}
\left(
M_{|m|^2}
P_{L,\chi}^{rot}
\right)
=
\operatorname{Tr}
\left(
M_{|m|^2}
P_{K_{B_{b,\gamma}}}
\right).
\]

Using an orthonormal Takenaka basis \(e_{+,b},e_{-,b}\),

\[
\operatorname{Tr}
\left(
M_{|m|^2}
P_{K_B}
\right)
=
\int
|m(t)|^2

d\mu_{b,+\gamma}(t)
+
\int
|m(t)|^2

d\mu_{b,-\gamma}(t).
\]

As \(b\downarrow0\),

\[
\boxed{
\operatorname{Tr}
\left(
M_{|m|^2}
P_{L,\chi}^{rot}
\right)
\longrightarrow
|m(\gamma)|^2
+
|m(-\gamma)|^2.
}
\]

The limit is independent of cutoff after recentering.

## Signed orientation

For the inner Blaschke orientation,

\[
Q^{host}
-
Q^{base}
=
-
P^{rot}.
\]

The opposite crossing orientation reverses which projection is subtracted and therefore gives

\[
+
P^{rot}.
\]

Thus the positive physical rotor projection is fixed while the signed relative readout changes sign.

The affine index correction acts on the same transported range:

\[
-
P^{rot}
+
2P^{rot}
=
+
P^{rot}.
\]

Hence the operator clutching is exact on the semilocal cutoff carrier.

## Dagger symmetry

The centered dagger exchanges the two elementary factors at \(\gamma\) and \(-\gamma\). It preserves the full degree-two model space and hence

\[
D
P_{K_B}
D^{-1}
=
P_{K_B}.
\]

If the baseline transport satisfies the established Real compatibility, then

\[
D
P_{\Lambda,\chi}^{rot}
D^{-1}
=
P_{\Lambda,\chi}^{rot}
\]

with the corresponding conjugate angular sector understood.

## Successor naturality

Let an admitted source successor act spectrally by multiplication with \(m_c\). Since it commutes with the cutoff translation and baseline scattering multipliers, its pullback of the rotor form is

\[
P^{rot}
\longmapsto
M_{m_c}^*
P^{rot}
M_{m_c}.
\]

In the crossing limit, its compressed rotor matrix tends to

\[
\begin{pmatrix}
|m_c(\gamma)|^2&0\\
0&|m_c(-\gamma)|^2
\end{pmatrix}.
\]

Thus the exact finite-\(b\) successor law converges to the previously derived discrete rotor law.

If one of these amplitudes vanishes, the corresponding rotor blade is unobservable on the successor image but remains present in the background projection defect.

## Relative trace identity

The localized relative trace of the hostile perturbation is

\[
\operatorname{Tr}
\left(
M_{|m|^2}
(
Q^{host}
-
Q^{base}
)
\right)
=
-
\operatorname{Tr}
\left(
M_{|m|^2}
P_{K_B}
\right).
\]

This equals the logarithmic-derivative current of the Blaschke factor after calibrating the overall Hardy-projection orientation. For the declared upper-Hardy convention above, the inner-factor inclusion gives the negative projection difference; choosing the opposite Hardy projection reverses both signs. Therefore the following descriptions coincide once this single convention is fixed:

1. local argument-principle jump;
2. boundary phase current;
3. Hardy relative projection trace;
4. finite Blaschke model-space defect;
5. transported semilocal cutoff rotor.

No separate scalar counterterm is required.

## Tetrahedral closure for the hostile fixture

The rotor channels now have explicit representatives on all relevant faces:

### Source--spectral face \(H_{123}\)

The positive phase-energy Cauchy packets and their discrete rotor limit.

### Spectral--trace face \(H_{134}\)

The finite-rank model-space projection

\[
P_{K_B}.
\]

### Source--geometry face \(H_{124}\)

Exact Hardy transport

\[
\mathcal U_\chi^*
U_L
M_{\Gamma_\chi}
(
\cdot
)
M_{\Gamma_\chi}^*
U_L^*
\mathcal U_\chi.
\]

### Geometry--trace face \(H_{234}\)

The transported physical projection

\[
P_{\Lambda,\chi}^{rot}.
\]

The four faces agree by unitary conjugation. Thus the local hostile rotor horn is filled in the finite-rank trace-class category.

## Scope boundary

The construction assumes that the hostile Blaschke factor is inserted as a multiplicative factor of the admitted scattering symbol.

It does not assert that the actual Tate or completed-zeta scattering phase contains such an off-axis divisor factor. Nor does it prove positivity of the baseline semilocal Weil form.

What it proves is conditional and exact:

\[
\boxed{
\text{if a finite Blaschke divisor factor is present, its rotor is a stationary finite-rank semilocal cutoff defect.}
}
\]

## Remaining gates

For the hostile fixture itself, the principal physical transport gate is closed.

The remaining questions are:

1. compatibility with simultaneous infinite divisor products;
2. convergence of the sum of transported finite-rank defects;
3. interaction with the fixed completed endpoint graph;
4. whether the baseline physical common bulk has additional negative directions;
5. actual arithmetic provenance of any such divisor factor.

## Disposition

Exact Hardy recentering transports the finite Blaschke model-space rotor into the semilocal cutoff geometry without trace growth:

\[
\boxed{
P_{\Lambda,\chi}^{rot}
=
\mathcal U_\chi^*
U_L
M_{\Gamma_\chi}
P_{K_B}
M_{\Gamma_\chi}^*
U_L^*
\mathcal U_\chi,
\qquad
\operatorname{Tr}P_{\Lambda,\chi}^{rot}
=2.
}
\]

The apparent Paley--Wiener divergence disappears because the physical object is a relative projection defect, not an ambient evaluation operator.
