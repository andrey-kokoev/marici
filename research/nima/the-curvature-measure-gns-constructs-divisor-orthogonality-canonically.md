# The curvature-measure GNS constructs divisor orthogonality canonically

Event 10285 required an orthogonal divisor-label space to represent the
Poincaré–Lelong energy as a trace. That space need not be postulated by
enumerating zeros.

Define the positive curvature measure

\[
\mu_\Xi
=
\frac1{2\pi}
\Delta\log|\Xi(s)|.
\]

Because \(\log|\Xi|\) is subharmonic, \(\mu_\Xi\) is a positive Radon measure.
Poincaré–Lelong later identifies it with the divisor measure, but positivity
and the measure GNS can be formed directly from the analytic field.

Construct

\[
\mathcal H_\Xi
=
L^2(\mathbb C,\mu_\Xi).
\]

Let

\[
(N_\perp f)(\sigma,t)
=
\left(\sigma-\frac12\right)f(\sigma,t)
\]

and

\[
(W_{\eta,\chi}f)(\sigma,t)
=
\chi(\sigma)e^{-\eta t^2}f(\sigma,t).
\]

Then

\[
E_{\eta,\chi}
=
\left\|
N_\perp W_{\eta,\chi}^{1/2}\mathbf 1
\right\|_{\mathcal H_\Xi}^2.
\]

This weighted-vector norm is canonical. A literal operator trace is
equivalent only after the source supplies a multiplicity fiber of dimension
\(m_\rho\) at each atom. Ordinary scalar \(L^2(\mu_\Xi)\) records
multiplicity as measure weight, not as Hilbert-space dimension, so its
unweighted operator trace must not be substituted for the displayed norm.

## Why cross terms disappear

Orthogonality of distinct divisor atoms is not an extra spectral axiom.
Disjoint atoms are orthogonal in \(L^2(\mu_\Xi)\) by measure theory. A zero of
multiplicity \(m\) appears as measure mass \(m\), so its energy contribution
is linear in \(m\), exactly as required.

Thus the granularity theorem is:

\[
\text{positive curvature current}
\to
\text{measure GNS}
\to
\text{canonical atomic orthogonality}.
\]

One must not reverse this arrow by inventing zero eigenvectors and then
declaring them orthogonal.

## Remaining authority gap

The analytic GNS does not yet explain RH from arithmetic constructors.
Its measure is built from \(\Xi\), and the statement

\[
N_\perp=0
\quad\mu_\Xi\text{-almost everywhere}
\]

is exactly RH.

The missing source theorem is now a representation comparison:

\[
\mathcal H_{\mathrm{prime/Green}}
\longrightarrow
L^2(\mu_\Xi)
\]

that intertwines:

- the arithmetic normal-incidence operator;
- multiplication by \(\sigma-1/2\);
- the heat weight;
- and the complete Green trace.

If that map is unitary or uniformly faithful, arithmetic coercivity can be
transported to the curvature GNS without first enumerating zeros.

## Minimality

The measure GNS is canonical up to unitary equivalence for the positive
functional

\[
f\longmapsto\int f\,d\mu_\Xi.
\]

Therefore it is the minimal analytic coefficient space required by the
Poincaré–Lelong witness. Any larger zero-state Hilbert space must descend to
this GNS or explain its additional invisible directions.

This replaces the ad hoc “orthogonal zero labels” obligation from event
10285 with a source-derived positive-current GNS theorem. The hard frontier
is no longer orthogonality; it is faithful arithmetic realization of the
curvature measure.
