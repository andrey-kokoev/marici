# A typed Beurling rigging joins arithmetic constructors to Fourier-Bohr observation

> Status: abstract Banach prototype. The source-native refinement is the projective exponential rigging in `theta-selects-a-projective-exponential-fock-rigging.md`; it replaces the choice of one polynomial weight by the full source-derived seminorm family.

## Objective

The source needs three capabilities that cannot live as bounded operations on one Hilbert space:

- exact typed arithmetic composition;
- completion-stable coefficient observation;
- seam and endpoint evaluation.

A rigged typed convolution object supplies the smallest common architecture.

## Typed valuation carrier

Let \(\mathcal M\) be the finite-support valuation monoid. An element

\[
\nu=(\nu_p)_p,\qquad \nu_p\in\mathbb N,
\]

represents the uniquely factored integer

\[
n(\nu)=\prod_p p^{\nu_p}
\]

and carries additive Mellin scale

\[
\ell(\nu)=\sum_p \nu_p\log p=\log n(\nu).
\]

Attach a finite-dimensional type fiber \(T_\nu\) recording channel distinctions that scalar frequency cannot retain: primitive, square, connected, seam-related, and any later boundary incidence types. Equal Mellin frequency does not identify different vectors in \(T_\nu\).

## Source test algebra

For \(s\ge0\), use the polynomial scale weight

\[
w_s(\nu)=(1+\ell(\nu))^s.
\]

It is submultiplicative:

\[
w_s(\nu+\mu)\le w_s(\nu)w_s(\mu).
\]

Define the typed Beurling test algebra

\[
\mathcal A_s=\ell^1_{w_s}(\mathcal M;T).
\]

Typed convolution is bounded on \(\mathcal A_s\). This is the rung on which constructor multiplication and finite Fock operations act.

Adams transport sends \(\nu\) to \(r\nu\). Because

\[
w_s(r\nu)\le r^s w_s(\nu),
\]

each fixed Adams operation \(\psi^r\) is bounded on \(\mathcal A_s\), provided its declared map between type fibers is bounded and respects multiplication.

## Observation Hilbert module

Let

\[
\mathcal H=\ell^2(\mathcal M;T).
\]

Since \(w_s\ge1\), the test algebra embeds continuously into \(\mathcal H\). Fourier-Bohr synthesis maps a finite typed packet to

\[
(\mathcal Mc)(t)=\sum_{\nu,\alpha}
c_{\nu,\alpha}e^{it\ell(\nu)}e_{\nu,\alpha},
\]

where \(\alpha\) indexes the type fiber. With the invariant mean, distinct typed basis states are orthogonal and

\[
\lVert\mathcal Mc\rVert_{\mathrm B^2}^2
=
\sum_{\nu,\alpha}|c_{\nu,\alpha}|^2.
\]

This is the completion-stable coefficient-observation rung.

The fiber label is essential. A scalar-valued Fourier-Bohr signal would collapse two distinct channel types occupying the same \(\nu\).

## Boundary dual

The continuous dual of \(\mathcal A_s\) contains weighted bounded coefficient families:

\[
\mathcal A_s'
\supseteq
\ell^\infty_{1/w_s}(\mathcal M;T^*).
\]

The aggregate evaluation

\[
c\longmapsto\sum_{\nu,\alpha} b_{\nu,\alpha}c_{\nu,\alpha}
\]

is continuous on \(\mathcal A_s\) whenever

\[
\sup_{\nu,\alpha}\frac{|b_{\nu,\alpha}|}{w_s(\nu)}<\infty.
\]

Thus the constant seam row and polynomially growing endpoint rows can live in the rigged dual even though they are unbounded on \(\mathcal H\). This types the three rungs as

\[
\mathcal A_s
\longrightarrow
\mathcal H
\longrightarrow
\mathcal A_s'.
\]

The last arrow denotes dual pairing, not a bounded Hilbert-space operator.

## Universal-property reading

This is not a direct sum of unrelated topologies. It is a rigging with three typed roles:

- \(\mathcal A_s\): constructor algebra;
- \(\mathcal H\): observable coefficient completion;
- \(\mathcal A_s'\): boundary readout domain.

A proposed current or coherence map is admitted only if it declares which rung it acts on and proves the corresponding continuity law. Transport between rungs does not promote a distributional boundary row to a bounded Hilbert observer.

## Hostile gates

The architecture fails if any of the following occurs:

1. The weight is not submultiplicative, so convolution leaves the test algebra.
2. An Adams map violates \(w_s(r\nu)\le C_rw_s(\nu)\).
3. Scalar Fourier-Bohr synthesis erases a nontrivial type fiber.
4. A boundary coefficient grows faster than the chosen weight.
5. A claimed Hilbert boundary port has cutoff norm diverging with support size.
6. A common operation is asserted without compatible actions on the test algebra, Hilbert module, and dual pairing.

## Remaining source-specific gate

This construction proves that a coherent carrier class exists. It does not select \(s\), the type fibers, or the endpoint and archimedean coefficient families. Those must be derived from theta/Tate incidence.

The next finite calculation is:

1. list the actual primitive, square, connected, seam, endpoint, and archimedean coefficient growth;
2. find the least polynomial weight exponent controlling all of them;
3. verify typed convolution and every required Adams map;
4. test whether the doubled Green pairing extends continuously between the declared rungs.

A failure of polynomial growth forces a stronger source rigging. A failure of fiberwise Adams coherence closes this candidate.
