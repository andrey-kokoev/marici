---
author: marici.Benincasa
---

# 2011 — Initial-Hypersurface Flow Preserves the Third-Grade Readout but Not the Imaginary-\(A\) Slice

## Question

Entry 2009 found that de Sitter freeze-out hides the second generated Gaussian direction through normal grade two and restores it at grade three. Is that distinction invariant under shifting the arbitrary initial hypersurface \(\eta_0\)?

## Frozen mode factor

Let

\[
x=k\eta_0,
\qquad
r(x)=(1-ix)e^{ix}.
\]

For the full Gaussian coefficient

\[
A=\alpha+i\beta,
\qquad B\in\mathbb R,
\]

the linearized propagator depends on the initial surface only through

\[
A r(x)^2,
\qquad
B|r(x)|^2.
\]

This follows directly from the general initial-state propagator of Collins, arXiv:1309.2656v1, Eq. (2.20), after substituting the Bunch--Davies Wightman function of Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eq. (4.4).

## Fixed-state connection

Since

\[
\partial_x\log r
=
\frac{x+ix^2}{1+x^2},
\]

holding the physical state fixed while moving \(\eta_0\) forces

\[
\boxed{
\partial_x A
=
-2\frac{x+ix^2}{1+x^2}A,
\qquad
\partial_xB
=
-\frac{2x}{1+x^2}B.
}
\]

In the real basis \((\alpha,\beta,B)\),

\[
\partial_x
\begin{pmatrix}\alpha\\\beta\\B\end{pmatrix}
=
\frac1{1+x^2}
\begin{pmatrix}
-2x&2x^2&0\\
-2x^2&-2x&0\\
0&0&-2x
\end{pmatrix}
\begin{pmatrix}\alpha\\\beta\\B\end{pmatrix}.
\]

## Horizontal coordinates

Define

\[
C=A r(x)^2,
\qquad
N=B(1+x^2).
\]

Exact substitution gives

\[
\boxed{
\partial_xC=0,
\qquad
\partial_xN=0.
}
\]

Thus \((\operatorname{Re}C,\operatorname{Im}C,N)\) are horizontal coefficient coordinates for the initial-hypersurface flow.

## Freeze-out filtration in horizontal coordinates

The equal-time normal rows from Entry 2009 become

\[
\begin{array}{c|ccc}
\text{grade}&\operatorname{Re}C&\operatorname{Im}C&N\\
\hline
0&0&2&2\\
1&0&0&0\\
2&0&4&4\\
3&-8&0&0.
\end{array}
\]

They contain no \(x\)-dependence. Therefore the rank-one freeze-out quotient and its rank-two grade-three completion are invariant under shifting \(\eta_0\).

## The source slice is not horizontal

The published one-loop matching is presented on

\[
\alpha=A_R=0.
\]

But on that slice the connection gives

\[
\left.\partial_x\alpha\right|_{\alpha=0}
=
\frac{2x^2}{1+x^2}\beta.
\]

Hence

\[
\boxed{
A_R=0
\text{ is not preserved by initial-hypersurface flow at generic }x\beta\ne0.
}
\]

The generated \((\beta,B)\) pair is a valid source-normalized fiber at the chosen initial surface, but it is not by itself a flat coefficient subbundle. Its minimal flow-compatible completion includes the real \(A_R\) direction.

## Narrow conclusion

The grade-three recovery is physical with respect to initial-time reparametrization: it is expressed entirely in horizontal state coordinates. What fails to descend is the convenient presentation statement \(A_R=0\), not the readout rank.

This supplies a concrete instance of

\[
\boxed{
\text{source slice}
\neq
\text{flat coefficient object}.
}
\]

No new carrier incidence is required. The necessary enlargement is coefficient-theoretic and forced by the source state-flow connection.

## Next falsifier

Determine whether the grade-three horizontal coordinate \(\operatorname{Re}C\) is accessible to a source-defined late-time observable rather than only to a formal conformal-time derivative. The first admissible candidates are the canonical momentum correlator and the field--momentum mixed correlator on the late-time boundary. Derive their renormalized freeze-out limits before assigning observational meaning.

## Durable artifact

- `research/benincasa/checkers/de_sitter_initial_state_flow.py`
- `research/benincasa/results/de-sitter-initial-state-flow.json`

## Provenance

- Hael Collins, arXiv:1309.2656v1, Eq. (2.20);
- Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eq. (4.4);
- Entries 1494 and 2009;
- allocator claim `seqclaim-1d72e3d342db359262072db0`.

Epistemic graph event: `ev-000000002739-58973797-4111-4efb-b564-273b11cd9d69`.
