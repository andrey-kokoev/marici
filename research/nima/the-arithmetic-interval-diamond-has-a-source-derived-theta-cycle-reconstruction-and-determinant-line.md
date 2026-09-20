# The arithmetic interval diamond has a source-derived theta-cycle reconstruction and determinant line

## Question and obligation

Can the history-plus-cycle constructor be realized on arithmetic intervals with the actual theta correlation atom, rather than on an unrelated cyclic matrix model?

Active SCC obligation: finite forward realization and attachment-presentation transport. The conjecture is that the recorded theta injectivity theorem, combined with an exact chord selector, supplies a finite analytical reconstruction and hence determinant-line transport. The rival omits the cycle selector; a second rival collapses the common interval refinement to two stage totals.

## Source and common refinement

Use the multiplicative interval diamond

\[
2\to4\to12,\qquad 2\to6\to12.
\]

The initial factor 2 places the support in [log 2,infinity), the domain of the recorded theta injectivity theorem. The arrows are multiplication by 2 or 3. Work in the unweighted labelled interval basis; a half-density basis change must be supplied separately and is not implicit in the matrices below.

Order the four edges as (2,4),(4,12),(2,6),(6,12). Order the three atoms as

\[
I_1=[\log2,\log4),\quad
I_2=[\log4,\log6),\quad
I_3=[\log6,\log12).
\]

The middle atom has length log(3/2). The coefficient synthesis is

\[
J=\begin{pmatrix}1&0&1&0\\0&1&1&0\\0&1&0&1\end{pmatrix}.
\]

Thus c maps to f_c=sum_i (Jc)_i 1_(I_i). The route cycle h=(1,1,-1,-1) satisfies Jh=0. Endpoint incidence has exactly the same one-dimensional kernel.

## Analytical realization from the recorded atom

Take D=0 in the prior theta interval transform:

\[
H_i(s)=\int_{I_i}\Phi_1(v)\Phi_1(v+s)\,dv,\qquad s\ge0,
\]

where

\[
\Phi_1(u)=e^{u/2}(2\pi^2e^{4u}-3\pi e^{2u})e^{-\pi e^{2u}}.
\]

These three functions are in L2(0,infinity): their integration intervals are compact and the second atom has Gaussian decay in e^(2s). They are linearly independent. Indeed, a vanishing combination would be T_0 f=0 for an L1 step function f supported above log 2. The source theorem in `research/voevodsky/the_completed_theta_correlation_is_injective_on_the_arithmetic_interval_range_20260912.md` implies f=0, and disjoint interval interiors then force every coefficient to vanish.

This argument imports the recorded analytic theorem explicitly. The checker below does not numerically evaluate the theta integrals or re-prove that theorem.

Let H:C^3->L2 send y to sum_i y_i H_i. Its Gram matrix

\[
G=H^*H
\]

is positive definite, so the coefficient extractor on im H is the source-derived finite map

\[
L=G^{-1}H^*,\qquad LH=I.
\]

This Gram is used only for reconstruction. It is not substituted for an Euler return operator, and its entries are not chosen to match a determinant. At fixed intervals its inverse is bounded; no cutoff-uniform estimate follows.

## Two forest presentations and reconstruction

Choose chord e_3 in forest presentation A and chord e_1 in presentation B:

\[
Z_A=(0,0,0,1),\qquad Z_B=(0,1,0,0),\qquad
C_A=\begin{pmatrix}J\\Z_A\end{pmatrix},\quad
C_B=\begin{pmatrix}J\\Z_B\end{pmatrix}.
\]

Both C matrices are invertible. Define the actual analytical responses

\[
\mathcal O_Ac=(HJc,Z_Ac),\qquad
\mathcal O_Bc=(HJc,Z_Bc).
\]

Their common response space is im H direct-sum C, of dimension four. Reconstruction is explicit:

\[
\mathcal R_A(f,w)=C_A^{-1}(Lf,w),\qquad
\mathcal R_A\mathcal O_A=I.
\]

The same formula holds for B. The source norm pulls back from

\[
\|\mathcal O_Ac\|^2
=(Jc)^*G(Jc)+|Z_Ac|^2,
\]

which is positive for every nonzero c. This is finite response noncollapse, not Haar-cycle closure or an identification with the Evans graph metric.

## Presentation transport and determinant line

Use source reconstruction, not a fitted adapter:

\[
\mathcal T_{BA}=\mathcal O_B\mathcal R_A.
\]

On response coefficients (x,y,z,w) this is

\[
T_{BA}=C_BC_A^{-1}
=\begin{pmatrix}
1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&1&-1
\end{pmatrix}.
\]

The interval response is unchanged; the new cycle coordinate is z-w. Treating cycle reversal as merely w -> -w would lose its boundary coupling. This is a forest-presentation change, not a prime swap or fourth-to-first successor seam.

Any chain of forest presentations composes by cancellation of the intermediate C matrix. The fourth exterior power therefore supplies an actual determinant-line map of the finite analytical response space. In these two frames,

\[
\det T_{BA}=-1.
\]

This sign is a frame-orientation factor, not a new divisor or physical anomaly. Dividing by det(C_B)/det(C_A) gives the identity in the common source orientation.

For comparison with the earlier plus-convention det3 bookkeeping, K=T_BA-I has Tr K=-2 and Tr K^2=4. Thus det3(I+K)=-exp(4); removal of its low counterterm recovers -1, and source-frame normalization recovers 1. These coordinates belong to forest transport, not to the Euler primitive and square currents. No holomorphic parameter-family claim follows from using an L2 Gram extractor at this fixed source.

## Finite hostiles and transport scope

The cycle h has zero theta history but nonzero selected chord coordinate. This identifies the actual lost source direction if the cycle port is omitted.

The ordered two-port projections of (x,y,z) are

\[
P_{23}(x,y,z)=(x,y+z),\qquad
P_{32}(x,y,z)=(x+y,z).
\]

The retained ratio-window hostile (0,1,-1) is invisible to the first and visible to the second. It is not an artificial response vector: it lifts through C_A to the explicit source coefficient vector (-2,-1,2,0). Thus the old two-port obstruction is present on this arithmetic interval source itself.

Multiplication of every endpoint by a positive label factor preserves incidence and atom order; the checker verifies the factor-5 example exactly. This statement is combinatorial. The theta functions must be recomputed on translated intervals; the fixed Phi_1 kernel is not claimed translation-invariant. At each new finite support where the injectivity theorem applies, the same reconstruction construction is available with its own Gram matrix.

## Disposition

Constructed, conditional only on the cited analytic injectivity theorem: a faithful theta-history-plus-cycle realization of this finite arithmetic interval diamond, its explicit reconstruction map, source-induced forest transitions, and determinant-line transport retaining the log(3/2) window.

This improves on the previous toy model by using the recorded theta atom and actual multiplicative interval incidence. It is still not the desired full determinant bridge: the prime-power weights and low Euler trace identities, the complete source-state packet, reciprocal four-chart successor seam, archimedean sewing, and cutoff-uniform reconstruction remain unproved. No formula here interprets the earlier -4/5 fixture residual.

Verification: `uv run --with sympy python research/nima/checkers/check_arithmetic_diamond_cycle_determinant.py`, exit 0; 16 exact incidence, source-lift, forest-transition and determinant checks. Results: `research/nima/results/arithmetic-diamond-cycle-determinant.json`. Analytical theta integrals were not numerically evaluated.
