# Prime creation and opposite seam translation form an exact weight-zero bicomplex

## The compensating arrow exists

Ledger 3827 proved that a cross-label differential cannot commute with Mellin
energy unless another channel carries the opposite weight. The moving seam
coordinate supplies exactly such a channel.

Let `c_p` be fermionic creation of a previously absent prime label. On the
squarefree label Fock space,

\[
c_p^2=0,
\qquad
c_pc_q+c_qc_p=0.
\]

Let

\[
H_{\rm lab}e_n=(\log n)e_n.
\]

Then

\[
[H_{\rm lab},c_p]=(\log p)c_p.
\]

On a seam coordinate `q`, let `Q` be multiplication by `q` and define the
backward translation

\[
(R_pf)(q)=f(q+\log p).
\]

Direct calculation gives

\[
[Q,R_p]=-(\log p)R_p.
\]

Therefore the combined arrow

\[
d_p=c_p\otimes R_p
\]

has total weight zero:

\[
[H_{\rm lab}+Q,d_p]=0.
\]

This is the exact compensating reservoir requested by ledger 3827. Prime
creation and opposite seam motion are two faces of one weight-preserving
operation.

## Nilpotence

The translations commute, while the prime creations anticommute. Hence for
every finite prime set

\[
d=\sum_p d_p
\]

satisfies

\[
d^2=0.
\]

No scalar Euler product or zeta zero enters this construction.

## Full-line contraction

On the full seam line, `R_p` is invertible. Fix one prime and let `i_p` be
fermionic contraction. With

\[
h_p=i_p\otimes R_p^{-1},
\]

the canonical anticommutation relations give

\[
dh_p+h_pd=1.
\]

Thus the full-line combined complex is contractible. The construction by
itself has no divisor and cannot encode RH. This is a useful control.

## Half-line boundary defect

The physical seam coordinate is a half-line. There `R_p` is the left-shift
coisometry. Its right-shift adjoint `S_p` satisfies

\[
R_pS_p=1,
\qquad
S_pR_p=1-P_p,
\]

where `P_p` projects onto the moving window

\[
[0,\log p).
\]

Using

\[
h_p=i_p\otimes S_p
\]

gives

\[
dh_p+h_pd
=1-(i_pc_p)\otimes P_p.
\]

The failure of contraction is therefore not an arbitrary analytic residual.
It is exactly the source-typed prime moving-seam window. On the full line the
defect disappears; on the half-line it is forced by the boundary.

## Meaning

This is the first explicit cross-label differential satisfying all of the
algebraic requirements posed in ledger 3825:

- it changes integer labels;
- it changes parity;
- its total Mellin-position weight is zero;
- it squares to zero;
- its failure of contraction is a named source window.

It also explains why earlier finite prime and moving-seam calculations kept
meeting. They are the label and control legs of one Koszul-Toeplitz complex.

## Remaining gates

The construction is not yet a stable inverse or an RH proof. One must still:

1. replace the squarefree algebraic Fock packet by the complete prime-power
   and archimedean source object;
2. identify the correct Hilbert or rigged completion of the infinite sum;
3. retain the primitive and square currents rather than hiding them in a
   regularized determinant;
4. compute reciprocal sewing of the boundary projections `P_p`;
5. prove that the completed boundary defect yields the theta Evans section or
   inner-factor record rather than only the Euler multiplier;
6. test whether a Blaschke-modified hostile fails to lift.

The sharpest immediate test is finite: compute the two-prime square and
three-prime cube with the half-line defect projections retained. If their
mixed boundary terms are merely commuting coboundaries of one global
potential, the bicomplex adds provenance but no zero-confining holonomy.

## Scope

This constructs the previously missing weighted cross-label differential and
its exact half-line contraction defect. It does not establish analytic
completion, determinant--Evans agreement, nontrivial holonomy, stable inverse
continuation, or RH.
