# Mixed Adams-seam curvature is the smallest ordered metric obstruction

## Infinitesimal reduction

Let \(s\) vary continuously along a seam chart, and let
\[
T_{s\to s+\varepsilon}
=
I+\varepsilon A_s+o(\varepsilon)
\]
be the authorized moving-seam transport.

Metric compatibility
\[
T_{s\to t}^*G_tT_{s\to t}=G_s
\]
differentiates to
\[
\partial_sG+A_s^*G+GA_s=0.
\]

This Lyapunov equation is the local seam-direction test. It determines whether the connection generator is compatible with the positive metric field.

## Discrete Adams direction

Let
\[
D_s:H_s\to H_{\psi(s)}
\]
be one typed weighted Adams operation. The seam and Adams directions form a plaquette:
\[
P_{s,\varepsilon}
=
T_{\psi(s)\to\psi(s+\varepsilon)}
D_s
-
D_{s+\varepsilon}
T_{s\to s+\varepsilon}.
\]

Strict naturality gives \(P_{s,\varepsilon}=0\). More generally, the two paths may differ by an authorized mixed holonomy
\[
K_{s,\varepsilon}
=
\big(D_{s+\varepsilon}T_{s\to s+\varepsilon}\big)^{-1}
T_{\psi(s)\to\psi(s+\varepsilon)}D_s.
\]

Nontrivial \(K\) is permitted only when source-authorized and unitary in the transported metric.

## Mixed curvature

Assume
\[
K_{s,\varepsilon}
=
I+\varepsilon F_s+o(\varepsilon).
\]
Then metric-compatible mixed holonomy requires
\[
F_s^*G_s+G_sF_s=0.
\]

The exact formula for \(F_s\) depends on the typing of \(\psi\), the derivative of \(D_s\), and the target seam generator. In a common trivialization, it has the schematic covariant form
\[
F_s
=
A_{\psi(s)}D_s-D_sA_s-\partial_sD_s,
\]
followed by the appropriate normalization by \(D_s^{-1}\).

This formula must not be used until source and target fibers have been identified by authorized trivializations.

## Three lenses on curvature

Define the \(G\)-adjoint
\[
F^{\dagger_G}=G^{-1}F^*G
\]
and decompose
\[
F
=
F_{\mathrm{skew}}
+
F_{\mathrm{herm}},
\]
where
\[
F_{\mathrm{skew}}
=
\tfrac12(F-F^{\dagger_G}),
\qquad
F_{\mathrm{herm}}
=
\tfrac12(F+F^{\dagger_G}).
\]

### Additive modular lens

The scalar trace
\[
\operatorname{Re}\operatorname{tr}F
\]
records infinitesimal volume expansion. It is the local derivative of the determinant modular character when ordinary finite-rank determinants are authorized.

### Determinant lens

The integrated scalar trace controls the determinant of small plaquette holonomy:
\[
\log|\det K_{s,\varepsilon}|
=
\varepsilon\operatorname{Re}\operatorname{tr}F_s
+o(\varepsilon).
\]

### Ordered metric lens

The traceless Hermitian part
\[
F_{\mathrm{herm}}^0
=
F_{\mathrm{herm}}
-\frac{\operatorname{tr}F_{\mathrm{herm}}}{d}I
\]
detects anisotropic distortion invisible to the determinant.

The \(G\)-skew part is legitimate infinitesimal unitary holonomy.

## Minimal hostile

Take \(G=I\) and
\[
F=
\begin{pmatrix}
a&0\\
0&-a
\end{pmatrix},
\qquad a\neq0.
\]
Then
\[
\operatorname{tr}F=0,
\]
so the infinitesimal determinant obstruction vanishes. The small holonomy has determinant one to first order, and in the exact model
\[
K_\varepsilon
=
\begin{pmatrix}
e^{\varepsilon a}&0\\
0&e^{-\varepsilon a}
\end{pmatrix}
\]
has determinant exactly one.

But
\[
F^*+F=2F\neq0.
\]
The plaquette expands one direction and contracts the other. It passes additive and determinant lenses while failing ordered metric compatibility.

## Gauge covariance

Under an authorized change of frame \(S_s\), the connection and Adams cell transform, and the curvature transforms by conjugation:
\[
F_s\mapsto S_sF_sS_s^{-1}.
\]
The condition
\[
F_s^*G_s+G_sF_s=0
\]
is frame invariant when
\[
G_s\mapsto(S_s^{-1})^*G_sS_s^{-1}.
\]

Therefore the checker should report gauge-invariant spectral data of the Hermitian part, not raw matrix entries.

## Relation to finite holonomy

Vanishing Hermitian curvature on every elementary source plaquette is necessary for local metric-compatible holonomy. It does not replace global cycle tests:

- flat local curvature can coexist with nontrivial global unitary holonomy;
- local source charts may not generate every cycle;
- singular seam or endpoint cells may contribute discrete holonomy.

The finite programme becomes:

1. local seam Lyapunov equation;
2. elementary Adams-seam curvature;
3. discrete endpoint/archimedean plaquettes;
4. global simultaneous holonomy unitarization;
5. uniform completion bounds.

## Source-native plaquette certificate

For one prime-power grade and one seam displacement, record:

- source and target fibers;
- \(G_s\) and \(\partial_sG_s\);
- seam generators \(A_s,A_{\psi(s)}\);
- Adams arrow \(D_s\) and covariant derivative;
- exact plaquette holonomy \(K_{s,\varepsilon}\);
- infinitesimal curvature \(F_s\);
- scalar trace;
- traceless \(G\)-Hermitian part;
- \(G\)-skew part;
- authority for any nontrivial unitary residual.

This is the smallest calculation that sees ordered Adams-seam incompatibility.

## Completion control

On each compact off-seam region, require
\[
\sup_{X,s}
\|F_{\mathrm{herm},X}(s)\|=0
\]
for exact metric compatibility, or a source-authorized controlled defect theorem if the construction is approximate.

For discrete finite steps, infinitesimal vanishing is insufficient without integration control. Bounds on the connection and curvature must ensure that small plaquette estimates integrate uniformly to finite transport.

## Next exact calculation

Start with the constructed moving-seam unitary generator, so
\[
A_s^*G+GA_s+\partial_sG=0
\]
is already expected in the geometric sector. Insert the weighted grade-\(k\) Adams arrow
\[
D_{p^k,s}
\]
and compute its covariant derivative.

If \(D_{p^k,s}=a_{p^k}(s)U_{p^k,s}\), separate:

- the scalar derivative \(\partial_s\log a_{p^k}\);
- the unitary commutator curvature of \(U_{p^k,s}\);
- the traceless Hermitian residual.

A nonzero scalar derivative is the local modular obstruction. A zero scalar trace with nonzero traceless Hermitian residual is the first genuinely ordered obstruction.
