# Mellin half-density coordinates give a canonical minimal closure of the derivative square

## Scope

The finite Laguerre chain map

\[
P_+\mathsf D=\mathsf DQ_-
\]

needs a completed joint graph domain. Mellin half-density coordinates turn the operators into constant-coefficient derivatives plus one explicit exponential weight. This yields a canonical minimal closed chain map without claiming equality with every maximal distributional domain.

## Unitary logarithmic chart

On the positive ray, define

\[
(\mathcal Uf)(q)=e^{q/2}f(e^q),
\qquad q\in\mathbb R.
\]

Then

\[
\mathcal U:L^2(\mathbb R_+,dx)\to L^2(\mathbb R,dq)
\]

is unitary.

For the dilation generator \(A=x\partial_x\),

\[
\mathcal U\left(A+\frac12\right)\mathcal U^{-1}
=
\partial_q.
\]

Thus the centered dilation operator is exactly translation differentiation in the half-density chart.

## Three transformed operators

Write \(\partial=\partial_q\). The direct odd completion becomes

\[
\widehat P_+
=
\partial^2-\frac14.
\]

The shifted even-potential completion becomes

\[
\widehat Q_-
=
\left(\partial-\frac32\right)
\left(\partial-\frac12\right).
\]

The ordinary derivative bridge becomes

\[
\widehat{\mathsf D}
=
e^{-q}\left(\partial-\frac12\right).
\]

The exponential multiplier is the complete difference between additive differentiation and multiplicative translation in this chart.

## Exact core identity

On \(C_c^\infty(\mathbb R)\),

\[
\left(\partial^2-\frac14\right)
e^{-q}\left(\partial-\frac12\right)
=
e^{-q}\left(\partial-\frac12\right)
\left(\partial-\frac32\right)
\left(\partial-\frac12\right).
\]

Hence

\[
\widehat P_+\widehat{\mathsf D}
=
\widehat{\mathsf D}\widehat Q_-
\]

on the compactly supported smooth core.

This verifies the commuting square independently of either Laguerre matrix.

## Joint graph completion

Define the core norm

\[
\|g\|_{\mathrm{chain}}^2
=
\|g\|_2^2
+
\|\widehat Q_-g\|_2^2
+
\|\widehat{\mathsf D}g\|_2^2
+
\|\widehat P_+\widehat{\mathsf D}g\|_2^2.
\]

Let

\[
\mathcal X_{\min}
=
\overline{C_c^\infty(\mathbb R)}^{\|\cdot\|_{\mathrm{chain}}}.
\]

By construction, the four graph coordinates extend continuously from the core. If \(g_n\to g\) in this norm, then

\[
\widehat P_+\widehat{\mathsf D}g_n
-
\widehat{\mathsf D}\widehat Q_-g_n
=0
\]

for every \(n\), and both terms converge in \(L^2\). Therefore

\[
\widehat P_+\widehat{\mathsf D}g
=
\widehat{\mathsf D}\widehat Q_-g
\]

for every \(g\in\mathcal X_{\min}\).

This closes the chain identity on a canonical source-generated minimal domain.

## What is and is not proved

Proved:

- the half-density chart is unitary;
- the transformed operators are explicit;
- the compact core is invariant;
- the chain identity survives completion in the declared joint graph norm.

Not yet proved:

- \(\mathcal X_{\min}\) equals the intersection of all maximal distributional domains;
- finite Laguerre sequences are a core for this weighted joint graph;
- endpoint/sewing maps are continuous on \(\mathcal X_{\min}\);
- prime-wise constants are uniform after adding scale and cutoff labels.

The possible minimal-versus-maximal gap is a genuine boundary condition at the logarithmic ends \(q\to\pm\infty\), especially because \(e^{-q}\) grows at the additive endpoint \(q\to-\infty\).

## Source interpretation

The joint graph is not an invented higher-order energy. Every term is forced by one of the arrows in the commuting square:

- \(g\): state mass;
- \(\widehat Q_-g\): even-potential completion;
- \(\widehat{\mathsf D}g\): derivative incidence;
- \(\widehat P_+\widehat{\mathsf D}g\): completed odd output.

Thus the domain is constructor-derived. It records exactly the data required to close the square and no unrelated Sobolev term.

## Result

The first completed derivative comparison can be defined rigorously as the minimal chain graph

\[
\mathcal X_{\min}
=
\overline{C_c^\infty}^{\|\cdot\|_{\mathrm{chain}}}.
\]

On this domain the typed identity holds exactly:

\[
\widehat P_+\widehat{\mathsf D}
=
\widehat{\mathsf D}\widehat Q_-.
\]

The next gate is a trace and cutoff theorem on \(\mathcal X_{\min}\), together with a decision whether the source requires the minimal domain or a larger maximal realization.
