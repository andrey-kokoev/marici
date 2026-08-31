# The rapid twisted core is dense with fixed endpoint traces

## Closed relative graph

For a positive weight \(w\) with

\[
w^{-1}\in L^1(\mathbb R),
\]

represent a relative history by its incoming trace \(a=f(-\infty)\) and derivative \(g=f'\in L^2(w\,du)\). The outgoing trace is constrained by

\[
f(+\infty)
=
a+\int_{\mathbb R}g(u)\,du.
\]

The integral functional is continuous on \(L^2(w\,du)\):

\[
\left|\int g\right|
\le
\|w^{-1/2}\|_2
\|w^{1/2}g\|_2.
\]

Thus both endpoint traces are bounded in the closed graph norm.

## Density with preserved integral

Let \(g\in L^2(w\,du)\). Choose smooth compactly supported approximants \(h_n\to g\) in the weighted norm.

Their integrals need not equal \(\int g\). Fix one smooth compactly supported function \(\psi\) with

\[
\int\psi=1.
\]

Set

\[
g_n
=
h_n
+
\left(
\int g-\int h_n
\right)\psi.
\]

Continuity of the integral functional gives

\[
\int h_n\to\int g,
\]

so

\[
g_n\to g
\]

in \(L^2(w\,du)\), while

\[
\int g_n=\int g
\]

exactly.

Define

\[
f_n(u)
=
a+\int_{-\infty}^{u}g_n(v)\,dv.
\]

Then \(f_n\) is a smooth core history with exactly the same two endpoint traces as \(f\), and

\[
f_n\to f
\]

in the relative graph norm.

Hence the rapid core is dense even after freezing both endpoint traces.

## Twisted channels

Apply the exponential conjugators \(U_-\) and \(U_+\). Pullback preserves density, and the same correction argument applies to the conjugated derivatives. Therefore the common twisted core is dense in both closed half-density history spaces.

## Unique extension of the boundary form

On the core,

\[
B_0(f,g)
=
\langle T_Qf,\Omega T_Pg\rangle.
\]

The trace maps are bounded and \(\Omega\) is finite-dimensional, so the right side is continuous in the closed graph norms. The bulk Green form is also continuous by definition of those graph norms.

Since the core is dense, both sides have unique continuous extensions and remain equal:

\[
B
=
T_Q^{*}\Omega T_P.
\]

In particular,

\[
B(f,g)=0
\]

whenever either argument lies in the corresponding closed trace kernel. Two closed extensions agreeing on the core but differing on the trace kernel are impossible because continuous extension from a dense core is unique.

## Hostile resolution

The three hostiles from event 10154 are excluded:

- trace closability: endpoint traces are bounded;
- core density: proved with integral-preserving correction;
- hidden trace-kernel extension: excluded by uniqueness.

## Consequence

The form-core closure theorem is now complete for every off-seam Laplace weight, and transports labelwise under Mellin translation. This upgrades the boundary factorization used in event 10153 from an outline to a closed-domain proof.
