# 1869 — The First Triple-Wall Pilot Produces a New Nonsoft Quartic Candidate

## Representative

Take the first nonzero triple-wall representative from Entry 1868:

\[
G_{\setminus e_{12}}\mid g_{1345}\mid g_{145}.
\]

Its three wall equations solve

\[
y_1=-\frac52t,
\qquad
y_2=-\frac32t,
\qquad
y_3=-\frac12t.
\]

Set \(z=t^2\) and \(v=y_4^2\). Differences of the five Kummer equations
then solve \(u_1,u_2,u_3\), leaving one exact quadratic

\[
P(v,z)=0
\]

over \(\mathbb Q(\sqrt5)\).

## Critical discriminant

The repeated-root condition in \(v\) has discriminant

\[
\frac5{64}
\left[
-200+515z+24\sqrt5-114\sqrt5z
+96\sqrt5z^2-320z^2
\right].
\]

Its rational field norm, up to the nonzero source-fixed unit, is

\[
\boxed{
D_3(z)
=
7424-35728z+61041z^2-44032z^3+11264z^4.
}
\]

## Exact exclusion tests

At the good prime \(2147483647\):

- \(D_3\) is square-free;
- \(D_3\) is coprime to all eight factor blocks in Entry 1866;
- \(D_3\) is coprime to the \(y_4=0\) condition;
- \(D_3\) is coprime to the \(y_5=0\) condition.

The last test uses the exact repeated-root specialization

\[
y_5^2=0
\quad\Longleftrightarrow\quad
780-375z-140\sqrt5+173\sqrt5z=0,
\]

up to an invertible quadratic-field constant. Therefore the quartic is not a
soft or previously compiled one-/two-wall factor.

## Remaining saturation gate

The discriminant detects criticality of the triple-wall pullback. It does not
yet prove that all three wall multipliers are nonzero. A generic root could
still belong to an uncompiled lower-wall critical component with one vanished
multiplier.

Hence the established statement is

\[
\boxed{
D_3(z)\text{ is a new nonsoft triple-wall candidate, not yet certified
period singular support.}
}
\]

## Next falsifier

Compute the source-ordered null vector of the full fiber Jacobian on
\(P=\partial_vP=0\). Saturate by each of its three wall-multiplier
coordinates. If all three are units on the generic quartic locus, adjoin
\(D_3\) to the Picard--Fuchs candidate denominator. Otherwise classify the
surviving lower-wall factor and do not enlarge the bound.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_triple_landau_pilot.rs`
- `research/benincasa/results/five-site-cyclic-triple-landau-pilot.json`
- Entries 1866--1868
- allocator claim: `seqclaim-e6b6290cf809258efcfd1a01`
