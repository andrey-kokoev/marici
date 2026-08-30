# Balanced-word interferometry detects the kernel of abelianization

## Question

Which pairs of constructor words admit a relative interference phase that is invariant under independent phase choices for the primitive operations?

Let \(g_1,\ldots,g_r\) be reversible projective constructors. A word \(w\) may contain \(g_i\) and \(g_i^{-1}\). Define its signed occurrence vector

\[
d(w)=(d_1(w),\ldots,d_r(w))\in\mathbf Z^r,
\]

where \(d_i\) counts \(g_i\) minus \(g_i^{-1}\).

## Claim boundary

Under independent representative changes

\[
g_i\mapsto e^{i\phi_i}g_i,
\]

a word transforms as

\[
w\mapsto e^{i\langle d(w),\phi\rangle}w.
\]

A coherent comparison of branches \(w_0\) and \(w_1\) therefore acquires relative gauge factor

\[
e^{i\langle d(w_0)-d(w_1),\phi\rangle}.
\]

For independent \(U(1)^r\) phase freedom, the relative phase is gauge-invariant for every \(\phi\) if and only if

\[
d(w_0)=d(w_1).
\]

This is the balanced-word criterion.

Let \(F_r\) be the free group on the primitive constructors. Its abelianization map is

\[
\operatorname{ab}:F_r\longrightarrow\mathbf Z^r,
\qquad
\operatorname{ab}(w)=d(w).
\]

Hence

\[
d(w_0)=d(w_1)
\quad\Longleftrightarrow\quad
w_1^{-1}w_0\in[F_r,F_r].
\]

Gauge-invariant word interferometry detects relations in the kernel of abelianization. Additive scalar occurrence data sees only \(\mathbf Z^r\) and necessarily erases this residue.

Examples:

- \(UV\) versus \(VU\) is balanced: both have degree \((1,1)\). Their relative word is a commutator.
- \(UVU^{-1}V^{-1}\) versus \(I\) is balanced: both have degree zero.
- \(U\) versus \(I\) is unbalanced and requires an external phase lift.
- \(U^2V\) versus \(UVU\) is balanced and can expose a higher order-sensitive relation.

For toric logical loops, \(ZX\) versus \(XZ\) is the smallest balanced pair exposing odd intersection. The scalar lens records identical constructor multiplicities, while the ordered lens produces a relative sign.

If source relations constrain the allowed phase gauges to a subgroup \(G\subseteq U(1)^r\), equality of degree vectors can be weakened to the condition that \(d(w_0)-d(w_1)\) annihilates \(G\). That weaker result requires the gauge subgroup to be independently source-derived.

Balanced words remove representative-phase ambiguity. They do not construct coherent branch control, prevent environmental which-word records, or calibrate path-specific phases unrelated to primitive constructor gauges.

## Disposition

Balanced-word interferometry is the exact interface between scalar occurrence data and ordered constructor residue:

\[
\text{word}
\longrightarrow
\text{abelianized occurrence vector}
\quad+\quad
\text{commutator residue}.
\]

The first component determines phase-gauge covariance. The second contains the order information accessible to a balanced coherent comparison.

The first falsifier is one of:

1. the signed occurrence vectors differ;
2. inverse operations do not carry inverse phase;
3. primitive phase gauges are correlated but treated as independent, or conversely;
4. branch-specific path phases are conflated with constructor rephasing;
5. equality in abelianization is used to claim equality of ordered words;
6. a balanced algebraic pair is claimed physically comparable without a coherent higher-order constructor.

The next finite audit for any proposed interference protocol is mechanical: record both word occurrence vectors, their difference, the resulting commutator-subgroup word, and the physical constructor that makes the two branches coherent.
