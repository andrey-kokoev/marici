---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 774 — The Cyclic Hom Pole Lattice Is Locally Stable

## Local operator

Use the splitting convention

\[
dX+XA_T-A_EX=C.
\]

For every smooth labelled support \(f=0\), the checker constructs the normal
Hom residue \(R_f\) after first combining the two diagonal blocks.  This is
essential at \(u^2+1=0\): the apparent order-two poles in \(A_T\) and \(A_E\)
cancel in the Hom operator.

The characteristic polynomials are

\[
\begin{array}{c|c}
\text{occurrence orbit}&\chi_{R_f}(\lambda)\\
\hline
u,v,y,1-y,1+y,u-2,v-2,u^2+1&\lambda^4\\
v-u,\ y-u^2,\ y+u^2&\lambda^2(\lambda-1)^2\\
P_6&\lambda^2(\lambda+\tfrac12)^2.
\end{array}
\]

The three roots at \(m=1\) were additionally verified by exact determinant
reduction modulo their divisor equations.  All other displayed spectra were
constant on five exact generic points of each labelled divisor; the
quadratic orbit \(u^2+1\) was evaluated over
\(\mathbf F_{p^2}=\mathbf F_p[i]/(i^2+1)\).  Positive orders through sixteen
give the same kernel census.

### Convention bridge to Entry 775

Entry 775 writes the dual Hom operator as

\[
dX+A_EX-XA_T.
\]

Its residue is the negative of the convention above.  Consequently the
nonzero eigenvalue on \(v-u=0\) is \(-1\) there and \(+1\) here.  The present
choice is the literal coefficient convention in the finite splitting matrix
used by Entries 763 and 769.  This sign difference does not affect the
stabilization claim: in either convention there is no admissible root above
the already tested order one.

Hence the only positive indicial resonance is

\[
\boxed{m=1}
\]

on the three already licensed simple-pole orbits.  There is no resonance
above the corresponding component of

\[
e_{\rm Hom}=(1,1,1,0,0,1,1,1,1,1,1,2).
\]

## The exceptional forcing pole

On \(u^2+1=0\), the homogeneous Hom connection is regular while the affine
cocycle has order two.  Writing \(f=u^2+1\), the leading recurrence is

\[
-x_{-1}=C_{-2}.
\]

Thus the double forcing pole fixes a unique simple principal part.  For a
hypothetical homogeneous term \(f^{-m}x_{-m}\) with \(m\ge2\), the leading
equation is

\[
-m x_{-m}=0,
\]

so no larger meromorphic pole is admitted.  The order two in
\(e_{\rm Hom}\) is therefore conservative rather than deficient.

## Chart units and infinity shear

Entry 770's relation

\[
d_0d_1d_2=8
\]

changes local representatives only by units at affine generic points.  The
normalization boundary is handled separately by the transported target
column shear \((0,6)\).  That shear is supported at infinity and is already
included in Entries 765 and 769's degree-thirty bound; it does not increase
any finite affine indicial root.

All 23 affine support classes therefore stabilize at their transported
components of \(e_{\rm Hom}\).  Combining this local result with Entry 769's
exhaustive degree-thirty inconsistency gives

\[
\boxed{
C\notin\operatorname{im}\nabla_{\rm Hom}
\quad\text{for rational gauges on the finite cyclic atlas}.
}
\]

This is coefficient-extension nonsplitting.  It does not create a new
carrier divisor and does not yet identify the extension class with the
physical relative integration chain.

## Evidence

- `research/benincasa/check_local_hom_indicial_stabilization.py`;
- `research/benincasa/local-hom-indicial-stabilization.json`;
- Entries 765, 769--773;
- allocator claim `seqclaim-2f1ca2c7890959c0c0b2f1f2`.
- epistemic event
  `ev-000000000390-9b10e7a7-da32-443f-bffe-6e030f9df0d1`.

## Next falsifier

Return to the supported physical comparison.  Test whether this now-proved
rationally nonsplit cyclic extension pairs nontrivially with the weighted
relative integration-chain specialization.  If the pairing vanishes, the
extension remains coefficient data invisible to the physical period; if it
survives, compute whether its supported comparison cone carries
\(\mathcal Q\).
