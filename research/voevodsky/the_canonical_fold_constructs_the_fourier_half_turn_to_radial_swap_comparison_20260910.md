# The canonical fold constructs the Fourier-half-turn to radial-swap comparison

## Question

Is the comparison map in

\[
CF^2=W_uC
\]

still absent mathematically, or does the previously constructed whole-line fold supply it?

## Claim boundary

The canonical phase-decorated fold supplies an exact unitary comparison between whole-line reflection and the reciprocal radial swap. Since source audit identifies causal reflection with the Fourier half-turn, this constructs the carrier, differential, wall, and Hilbert-dagger parts of the comparison. It does not authorize the undeclared G4 carrier or select its arithmetic loading.

## Problem

Prior work separately constructs:

- whole-line causal reflection \(R\);
- the reciprocal radial double;
- the radial swap \(W_u\);
- the source identity \(R=F^2\) on the history representation.

Their composition had not been written as the required sewing comparison.

## Bold conjecture

A new fitted fiber isomorphism is needed to intertwine the Fourier half-turn with radial reciprocity.

## Named rivals

1. The phase-decorated whole-line fold is already the intertwiner.
2. The fold matches the differential but not the wall relation.
3. The fold is metric but fails the adjoint/transpose comparison.

## Canonical fold

For \(|u|=1\), define

\[
(C_uq)_+(r)=q(r),
\qquad
(C_uq)_-(r)=u q(-r),
\qquad r\ge0.
\]

Then

\[
C_u:L^2(\mathbb R)
\longrightarrow
L^2(\mathbb R_+)\oplus L^2(\mathbb R_+)
\]

is unitary.

It intertwines the whole-line derivative with the oppositely oriented radial double:

\[
C_u\partial_t
=
\begin{pmatrix}
\partial_r&0\\
0&-\partial_r
\end{pmatrix}C_u.
\]

At the wall,

\[
(C_uq)_-(0)=u(C_uq)_+(0),
\]

so its trace lands exactly in

\[
\Lambda_u=\{(c,uc):c\in\mathbb C\}.
\]

No wall phase is fitted after folding.

## Half-turn intertwining

Let whole-line reflection be

\[
(Rq)(t)=q(-t)
\]

and let

\[
W_u=
\begin{pmatrix}0&u^{-1}\\u&0\end{pmatrix}.
\]

Direct substitution gives

\[
W_uC_uq
=
\bigl(q(-r),u q(r)\bigr)
=
C_uRq.
\]

Therefore

\[
C_uR=W_uC_u.
\]

Using the source history identity \(R=F^2\),

\[
C_uF^2=W_uC_u.
\]

This rejects the bold conjecture: no additional fiber isomorphism is needed on the declared whole-line/radial history carrier.

## Green form

Integration by parts on the radial double gives boundary matrix

\[
J_\partial=\operatorname{diag}(-1,1).
\]

The fold maps the whole-line cut into the maximal-isotropic wall graph \(\Lambda_u\). Reflection reverses cut orientation, and correspondingly

\[
W_u^*J_\partial W_u=-J_\partial.
\]

Thus the comparison preserves the line-valued Green structure with the required orientation reversal.

## Dagger comparison

Because \(C_u\) is unitary on the Hilbert carrier,

\[
C_uA^*= (C_uAC_u^{-1})^*C_u
\]

for operators on their transported domains. On the test/dual rigging, the same fold acts continuously by restriction and contragredient transpose. Hence the Real comparison between history transpose and Hilbert adjoint is induced by one map, provided each operator domain is transported by \(C_u\).

This does not turn primitive distributional rows into Hilbert vectors; their transpose remains on the dual rung.

## Labelled and response extension

Applying \(C_u\) fiberwise preserves prime and grade labels. It transports source-generated endpoint and flux traces because these are evaluations of the folded history and density. The rapid radial response and oriented Laplace cocycle then live on the folded radial coordinates.

Extension to every retained primitive, square, connected, and archimedean response stratum follows only for strata whose realization maps are already natural under the same fold. No external G4 equality is inferred from this internal extension.

## Exact remaining authority boundary

The mathematical comparison

\[
C_uF^2=W_uC_u
\]

is constructed. What remains absent is a G4 declaration that:

1. its conservative carrier is this reciprocal radial double;
2. its reciprocal sewing is \(W_u\);
3. its source injection is the folded completed-theta history;
4. its arithmetic loading is the forward Euler-to-theta coefficient candidate.

## Disposition

The half-turn sewing comparison is no longer a missing internal map. The canonical fold constructs it exactly and supplies carrier, differential, wall, metric, and dagger compatibility. External G4 identification is now an owner-declaration gate plus the canonical loading proof, not an unresolved search for a comparison operator.
