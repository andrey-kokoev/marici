# Value Control and Seam Jets Have No Common Relative-Sup Topology

## The two readouts

On positive-chamber analytic packets, the primitive profile supplies the
relative value seminorm

\[
\lVert h\rVert_{\mathrm{rel}}
=
\sup_{u\geq0}\frac{|h(u)|}{\phi_1(u)}.
\]

The seam supplies derivative readouts

\[
j_{2r+1}(h)=h^{(2r+1)}(0).
\]

Both are source-relevant, but they do not extend continuously to one completion
defined only by the relative value seminorm.

## Exact hostile sequence

For positive integers \(N\), define

\[
h_N(u)
=
N^{-1/2}\phi_1(u)\sin(Nu).
\]

Every \(h_N\) is analytic wherever \(\phi_1\) is analytic, and

\[
\lVert h_N\rVert_{\mathrm{rel}}
\leq
N^{-1/2}
\longrightarrow0.
\]

At the seam,

\[
h_N'(0)=N^{1/2}\phi_1(0),
\]

so

\[
|h_N'(0)|\longrightarrow\infty.
\]

Hence first-derivative evaluation is unbounded in the relative value topology.
Higher seam jets fail for the same reason, with successively larger powers of
\(N\).

The witness remains inside the positive cone after adding it to the primitive:

\[
\phi_1(u)+h_N(u)
=
\phi_1(u)\left(1+N^{-1/2}\sin(Nu)\right)>0
\]

for \(N>1\) and \(u\geq0\).

## Common-domain residual

This is the smallest theta common-domain incompatibility:

- pointwise positive-chamber dominance is continuous in the relative value
  topology;
- seam-current extraction is not;
- analyticity and positivity do not repair the mismatch.

Therefore no completion based only on relative value control can carry both the
bulk perturbation readout and the modular boundary-current readout.

The residual is not consumption of a shared physical resource. It is failure
of joint continuity:

\[
\mathcal R_{\mathrm{common}}(h_N)
=
\bigl(\lVert h_N\rVert_{\mathrm{rel}},h_N'(0)\bigr)
\longrightarrow
(0,\infty).
\]

## Required topology

A faithful completed graph must retain at least two independent coordinates:

\[
\lVert h\rVert_{\mathrm{graph},1}
=
\lVert h\rVert_{\mathrm{rel}}
+
\frac{|h'(0)|}{\phi_1(0)}.
\]

For all-frequency integration by parts, the finite graph norm is still
insufficient. The natural object is the projective analytic graph topology
carrying the entire odd seam germ together with positive-chamber value control.

This gives a directed-system interpretation of finite repair:

- adjoining \(j_1\) repairs the first observed discontinuity;
- adjoining \(j_3\) exposes the next;
- the projective limit of all odd jets is the even-germ condition;
- in the analytic category, that limit is global reciprocal reflection.

## Scope boundary

The graph topology records both readouts but does not prove positivity of an
oscillatory transform. It prevents a value-small packet from becoming
coherence-invisible.

## Falsifier

Any claimed one-norm completion must bound derivative evaluation:

\[
|h'(0)|\leq C\lVert h\rVert_{\mathrm{rel}}.
\]

The sequence \(h_N\) disproves every such bound.
