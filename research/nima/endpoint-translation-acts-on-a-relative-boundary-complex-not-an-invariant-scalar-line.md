# Endpoint translation acts on a relative boundary complex, not an invariant scalar line

## Failure of scalar semi-invariance

Let \(S_a\) be forward tail translation,

\[
(S_aG)(q)=G(q+a),
\]

and let \(E_0\) be endpoint evaluation. Then

\[
E_0S_a=E_a.
\]

A scalar zero-sieve factor for translation would require a scalar
\(\lambda_a\) such that

\[
E_a=\lambda_aE_0
\]

on the declared source state space. This fails whenever the two evaluations
\(E_0\) and \(E_a\) are linearly independent.

Equivalently, choose \(G\) with \(G(0)=0\) and \(G(a)\ne0\). Then the present
endpoint zero does not propagate under translation. No scalar multiplier can
repair it.

Thus the moving endpoint is not an invariant line on the full tail state
space. The line semi-invariance criterion from the zero-sieve theorem rejects
the raw endpoint port before completion.

## Relative boundary complex

The exact translation defect is

\[
\delta_aG
=
(E_a-E_0)G.
\]

For a tail equation

\[
(\partial_q+\zeta)G=-f,
\]

one has

\[
\delta_aG
=
-\int_0^a\bigl(\zeta G(q)+f(q)\bigr)\,dq.
\]

Hence the endpoint defect factors through the oriented interval carrier. Define

\[
I_a(G,f)
=
\int_0^a\bigl(\zeta G(q)+f(q)\bigr)\,dq.
\]

Then

\[
E_a-E_0=-I_a.
\]

This is a chain-homotopy identity. Translation does not preserve the endpoint
covector strictly; it preserves it in the relative boundary complex containing
the seam interval.

The minimal categorical object is therefore the two-term packet

\[
\mathcal B_a:
\quad
\mathcal H_{\mathrm{tail}}
\xrightarrow{\ (E_0,E_a,I_a)\ }
\mathcal L_0\oplus\mathcal L_a\oplus\mathcal S_a
\]

subject to the relation

\[
E_a-E_0+I_a=0.
\]

The scalar endpoint is a projection of this packet, not a stable subobject.

## Concatenation coherence

For \(a,b\ge0\), interval incidence satisfies

\[
I_{a+b}
=
I_a+I_bS_a.
\]

Endpoint defects obey the same law:

\[
E_{a+b}-E_0
=
(E_a-E_0)+(E_{a+b}-E_a).
\]

Therefore relative translation composes by oriented concatenation. The
comparison cell for \(a+b\) is the composite of the cells for \(a\) and \(b\).

This is the endpoint analogue of the moving-seam cocycle. It is additive rather
than multiplicative because it is a boundary homotopy.

## Determinant line of the relative packet

A line-valued zero-sieve character can arise only after totalizing the relative
boundary complex. Let

\[
\operatorname{Det}(\mathcal B_a)
\]

be its determinant line when the finite or regularized complex is defined.
Oriented concatenation gives a candidate factorization

\[
\operatorname{Det}(\mathcal B_{a+b})
\cong
\operatorname{Det}(\mathcal B_a)
\otimes
\operatorname{Det}(S_a^*\mathcal B_b).
\]

This is the multiplicative line law needed by the categorical zero sieve. It
does not follow from the scalar equation \(E_a-E_0=-I_a\) alone. It requires:

1. a typed determinant functor for the relative packet;
2. coherent signs and orientations under concatenation;
3. treatment of the primitive and square divergent currents;
4. compatibility with reciprocal sewing;
5. survival through completion.

The endpoint multiplier is therefore a determinant of relative translation,
not a ratio \(E_a/E_0\).

## Prime-power specialization

At the arithmetic scale

\[
a_{p,k}=k\log p,
\]

the weighted relative current is

\[
w_{p,k}(E_{a_{p,k}}-E_0)
=
-\frac1k p^{-k/2}I_{a_{p,k}}.
\]

The connected grades \(k\ge3\) are absolutely summable. The primitive and
square grades are not ordinary completed scalar ports and must remain explicit
low-order boundary data.

Consequently, the determinant totalization must be third-order relative:

- primitive endpoint current;
- square endpoint current;
- connected interval tail;
- seam carrier;
- archimedean countercurrent.

Discarding the first two grades would manufacture a determinant line by
removing the exact obstruction it is supposed to carry.

## Relation to endpoint-line invariance

For a restricted one-dimensional source family, it may happen that

\[
E_a=\lambda_aE_0.
\]

That is the rank-one dual-orbit case. Then the relative complex contracts to an
invariant endpoint line, and \(\lambda_a\) is an honest zero-sieve character.

On the full source state space, the dual orbit of endpoint evaluation generally
has rank greater than one. The relative boundary complex is then irreducible
data. Scalar line invariance must not be inferred from a distinguished source
vector on which both evaluations happen to be proportional.

## Hostile tests

1. A state with \(G(0)=0\) and \(G(a)\ne0\) falsifies scalar endpoint
   semi-invariance.
2. Deleting \(I_a\) makes the translation square fail.
3. Reversing interval orientation changes the boundary identity.
4. Failure of \(I_{a+b}=I_a+I_bS_a\) destroys determinant concatenation.
5. Removing primitive or square currents changes the relative determinant
   packet.
6. A determinant factorization with no completion control can acquire a
   derived-limit anomaly.

## Consequence for categorical RH

The endpoint row in the generator table cannot be filled by a scalar
multiplier on the raw endpoint line. It must be replaced by a relative
determinant character built from endpoint motion and seam incidence.

This sharpens the next constructor: combine the typed third-order endpoint
packet with its archimedean countercurrent and prove determinant
factorization under interval concatenation. Only that totalized line can
participate in the global zero-sieve semi-invariance law.

## Verdict

Arithmetic translation does not preserve the endpoint scalar kernel. It acts
coherently on a relative boundary complex whose homotopy is the oriented seam
interval. The endpoint contribution to categorical RH must therefore be a
third-order relative determinant line, not an invariant raw evaluation line.
