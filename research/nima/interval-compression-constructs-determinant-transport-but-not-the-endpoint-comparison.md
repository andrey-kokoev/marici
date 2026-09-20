# Interval compression constructs determinant transport but not the endpoint comparison

## Question and active obligation

SCC obligation: attachment transport followed by route/coherencer compatibility. The stratum is one fixed finite labelled carrier with all declared prefix frames invertible. No readout descent or completed comparison is claimed.

The conjecture tested is that convolution plus interval restriction supplies the missing operator assignment without fitting spectral data. Rivals are the positive Gram construction, arbitrary supplied frames, and a scalar moment fit. The candidate below instead constructs its frames from an independently declared matrix and labelled projections.

## Source operation and type

Fix a finite ordered carrier V over the rationals, a declared source operator C:V->V, and a rational coupling lambda. For the prefix projection P_m define

\[
F_m=I+\lambda P_mCP_m.
\]

Restrict to cuts for which F_m is invertible. All matrices use the same retained labelled carrier. In code matrices act on row vectors, so products follow the written route order. These are cut-indexed frames, not yet frames indexed by the full Evans source state G. Supplying C as the discrete convolution C_ij=phi(i-j) is an independent operation; no determinant target is used to choose it.

Construct

\[
T_{m,n}=F_m^{-1}F_n,\qquad K_{m,n}=T_{m,n}-I.
\]

This replaces the arbitrary-frame input of `based_determinant_packet.py` by the explicit constructor `interval_packet` in `check_interval_compression_determinant_constructor.py`.

The finite determinant line at each cut is a copy of the top exterior line of V; the map on an arrow is the top exterior power of T. This exists prior to choosing its scalar determinant coordinate. No assertion about the determinant line of an Evans complex follows from this definition.

## Composition and signed transport

Cancellation of the middle frame proves, for every admitted triple,

\[
T_{m,n}T_{n,r}=T_{m,r},\qquad
K_{m,r}=K_{m,n}+K_{n,r}+K_{m,n}K_{n,r}.
\]

The signed comparison between two alternative cuts is T_mn; reversal gives T_nm=T_mn^{-1}. In particular,

\[
T_{0,a}T_{a,b}=T_{0,b}.
\]

Thus a cut difference has an operator image, including its orientation. It is not asserted to depend only on the interval length or to be the source-authorized log(q/p) face. That identification still requires translation naturality with G.

Every path with the same endpoints telescopes, including the six orders of three additions. This is flat transport by construction, not evidence that every possible source holonomy is trivial. The common-frame construction excludes nontrivial loop holonomy on this cut groupoid.

## Order-three coordinate

Use the plus convention I+K throughout. Put

\[
r(K)=-\operatorname{Tr}K+\tfrac12\operatorname{Tr}K^2.
\]

Then

\[
\alpha_3(A,B)=r(A\star B)-r(A)-r(B)
=\operatorname{Tr}(A^2B)+\operatorname{Tr}(AB^2)
+\tfrac12\operatorname{Tr}((AB)^2).
\]

The cubic signs differ from the I-A convention in the earlier anomaly packet. The checker retains det3 as the exact pair (det(I+K),r(K)), representing det(I+K) exp(r(K)); no logarithm branch is chosen. Low-grade normalization yields the ordinary finite determinant character. None of this licenses separate ordinary traces for a completed S3 operator.

## Strongest finite falsifier and exact residual

Take six labelled coordinates and the discrete convolution

\[
C_{ij}=\begin{cases}1/4,&|i-j|=1,\\0,&\text{otherwise}.\end{cases}
\]

Set lambda=1 and retain all seven prefix cuts. Exact rational checks establish all cut triples, signed inverses, a detectable cut-difference map, all six addition orders, the anomaly formula and cocycle. The tested pair has anomaly -1/224.

Now independently retain the endpoint state g(j)=j. Its primitive increment from 0 to 1 is 1, but F_1=F_0=I, so

\[
\operatorname{Tr}K_{0,1}-[g(1)-g(0)]=-1.
\]

The proposed universal endpoint comparison fails. This tests a candidate using C alone against an independent endpoint coordinate; it is not a counterexample involving a proven theta-specific relation between C and g. Such a relation has not been supplied here. The constructor rejects an asserted low-current match on this fixture rather than repairing it by a scalar factor.

There is also a necessary structural test for any future candidate. If its primitive trace equals an additive based endpoint cocycle, the star law forces

\[
\operatorname{Tr}(K_{G,a}K_{S_aG,b})=0.
\]

This follows by taking the trace of the star composition equation. It must be derived from the source or else the low-grade target needs a different, explicitly justified comparison law. Additive endpoint transport cannot simply be identified with an arbitrary relative-operator trace.

The existing equal-low-moment spectra are also passed through this constructor as diagonal source matrices. Their primitive and square coordinates agree, while their exact connected determinants differ. This checks that the implementation does not erase the connected channel; it does not identify those matrices as Evans source realizations.

## Claim boundary and disposition

Constructed: a finite cut-indexed relative operator packet derived from an input source matrix by interval compression, with determinant-line maps, oriented cut comparisons, telescoping path composition, and exact order-three anomaly coordinates.

Rejected: promoting that packet to the endpoint–Euler comparison merely because determinant transport coheres. The counterexample localizes failure to primitive source-state dependence, upstream of completion.

Not constructed: a full-state G-indexed Evans assignment, identification of signed cut transport with the prime ratio face, reciprocal dagger naturality, archimedean sewing, cutoff bonding maps or topology, and full-packet noncollapse. Inverse transport is not a proof of dagger reciprocity.

No source input has been manufactured from the desired scalar section. The prior audit's universal single-operator impossibility claim was too strong; this finite constructor exists, but the requested source comparison remains unproved.

Verification: `python research/nima/checkers/check_interval_compression_determinant_constructor.py`, exit 0. Results: `research/nima/results/interval-compression-determinant-constructor.json`. Thirteen exact tests passed, including the required nonzero endpoint obstruction. These finite tests do not promote the rational convolution model to a theta realization.
