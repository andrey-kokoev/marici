# Chain-compatible Krein sewing is rigid up to one phase

## Scope

The wall boundary module carries two independent structures:

\[
J=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}
\]

from the Green concomitant, and the derivative incidence

\[
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\]

representing

\[
w_1\mapsto w_0\mapsto0.
\]

This note classifies all invertible sewing maps preserving both structures.

## Orientation-preserving sewing

Let

\[
S=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
\]

Requiring the derivative chain to commute,

\[
SN=NS,
\]

gives

\[
c=0,
\qquad
d=a.
\]

Hence

\[
S=
\begin{pmatrix}
a&b\\
0&a
\end{pmatrix}.
\]

Now impose Green-form preservation,

\[
S^*JS=J.
\]

The matrix entries give

\[
|a|=1,
\qquad
\overline a b=0.
\]

Since \(a\neq0\),

\[
b=0.
\]

Therefore every orientation-preserving chain-compatible sewing is

\[
S=e^{i\theta}I.
\]

The apparent upper-triangular shear allowed by the nilpotent chain is eliminated by the Krein metric.

## Orientation-reversing sewing

If reciprocal reflection reverses the derivative incidence, the intertwining law is

\[
SN=-NS.
\]

This gives

\[
c=0,
\qquad
d=-a,
\]

so

\[
S=
\begin{pmatrix}
a&b\\
0&-a
\end{pmatrix}.
\]

Again imposing

\[
S^*JS=J
\]

forces

\[
|a|=1,
\qquad
b=0.
\]

Thus every orientation-reversing sewing is

\[
S=e^{i\theta}
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

## Consequence

Once the source specifies whether reflection preserves or reverses the derivative arrow, the entire sewing matrix is fixed up to one unit-modulus scalar.

There is no remaining:

- hyperbolic \(U(1,1)\) boost;
- triangular splitting shear;
- independent rescaling of wall and partner;
- or mixed wall-partner rotation.

Those freedoms preserve less structure but fail the joint chain-plus-Green audit.

## Phase authority

The surviving phase \(e^{i\theta}\) is invisible to the Hermitian boundary metric. It must be fixed, if needed, by an ordered source port:

- causal versus anti-causal history;
- reciprocal Euler character;
- Wronskian orientation;
- or a declared determinant-line convention.

If all observables are phase-insensitive, the phase may remain a legitimate gauge. It must not be fitted from a desired scalar sign.

## Completion stability

Because every admissible sewing is unitary in the ordinary coefficient norm as well as \(J\)-unitary,

\[
\|S\|=\|S^{-1}\|=1.
\]

Therefore this finite boundary sewing introduces no composite norm amplification and no cutoff-dependent shear.

Completion instability can only enter through:

- the extraction of asymptotic boundary coefficients;
- a cutoff-dependent phase frame;
- or coupling of the boundary module to the bulk.

It cannot arise from the intrinsic two-dimensional sewing matrix once both structures are enforced.

## Result

The joint centralizer is rigid:

\[
SN=NS,\quad S^*JS=J
\Longrightarrow
S=e^{i\theta}I,
\]

while the reversing normalizer is

\[
SN=-NS,\quad S^*JS=J
\Longrightarrow
S=e^{i\theta}\operatorname{diag}(1,-1).
\]

The next source question is reduced to one bit and one possible phase: does reciprocal reflection preserve or reverse the chain arrow, and which ordered source convention fixes \(e^{i\theta}\)?
