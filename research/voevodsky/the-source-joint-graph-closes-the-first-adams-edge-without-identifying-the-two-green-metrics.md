# The source joint graph closes the first Adams edge without identifying the two Green metrics

## Question

Must the first-Adams constructor prove equality between the Stieltjes and theta-history Green matrices, or does prior source architecture retain both realizations as a joint graph?

## Claim boundary

Prior research selects the joint graph of the two source-derived realizations. In that architecture, no metric equality or ratio map is required: the two forms coexist as a direct-sum positive form over their common labelled source. Combining that local result with the retained-source global graph theorem closes the first-Adams edge in the multi-rung faithful architecture. It does not implement a contract that insists on one output metric or the four matrix-unit equality.

## Common labelled source

For each prime and grades \(1,2\), let

$$
E_{p,12}
=\mathbb Ce_{p,1}\oplus\mathbb Ce_{p,2},
$$

with source-fixed orientation

$$
S_{12}=\operatorname{diag}(-1,+1).
$$

Prior research constructs two maps from this same source:

$$
A_{p,12}:E_{p,12}	o\mathcal H_{\rm win,wall},
$$

$$
C_{p,12}:E_{p,12}	o\mathcal H_{\rm cut,Wr}.
$$

The first is the window/front/resolved realization; the second is the theta cut-atom/Wronskian realization. Euler coefficients are realized before applying either scalar trace.

## Local joint graph

The source-authorized local object is

$$
\Gamma_{p,12}
=
\{(A_{p,12}x,C_{p,12}x):x\in E_{p,12}\}.
$$

It carries the direct-sum form

$$
\|(A_{p,12}x,C_{p,12}x)\|_\Gamma^2
=
\|A_{p,12}x\|_{\rm res,wall}^2
+
\|C_{p,12}x\|_{\rm cut,Wr}^2.
$$

Both legs are positive and nondegenerate on their source images, so the joint graph has zero radical. Stokes linking and Wronskian traces are bounded on their respective legs and retain the same source coordinates.

Thus the constructor relation is common provenance, not an isometry

$$
G_{\rm St}=Q^*G_\theta Q.
$$

## Why a ratio map is unnecessary

The scalar ratio \(S_{12}D_{p,12}\) appears only after choosing Stokes and Wronskian trace frames. Defining the constructor by that ratio discards the two source realizations and risks fitting one metric to the other.

The joint graph instead records

$$
x\longmapsto(A_{p,12}x,C_{p,12}x)
$$

before scalarization. Equality of scalar shadows follows from the common source coefficient where proved, while unequal positive energies remain valid typed observations.

## Global completion

Let \(E\) be the declared labelled projective/rigged source completion and collect all prime-grade maps into

$$
T=(A,C,\text{response},\text{endpoints},\text{connected grades},\ldots).
$$

On the multi-rung product target, existing estimates place:

- primitive histories on their projective/strong-dual rung;
- square rows on the twisted dual rung;
- connected grades on trace-class/nuclear rungs;
- response functions on Schwartz/relative-history rungs.

Retain the source and form

$$
J_Tx=(x,Tx).
$$

The continuous idempotent

$$
P_T=J_T\pi_E
$$

shows that the completed global joint graph is complemented and closed. This argument does not require the divergent primitive leg to lie in an unweighted Hilbert direct sum.

## Cutoffs and radical

Prime and grade cutoffs commute with every labelled leg before codiagonalization. The retained source coordinate separates points, so the global positive radical is zero. Connected grades attach as a separate nuclear coordinate and do not alter the primitive/square graph closure.

## Contract fork

Two distinct interface requirements must now be separated:

1. **faithful multi-rung joint-graph G4:** the first-Adams edge is constructed by common source provenance and complemented graph completion;
2. **single-metric output G4:** one must additionally prove the four matrix-unit equality or a source-derived quotient/congruence.

The second is strictly stronger and does not follow from the first. The current `polarized-prime-cell-open-theorem.v1` encodes the second requirement, while prior source architecture supplies the first.

## Evans boundary

Closing the first-Adams edge as a joint graph does not prove the unchanged Evans trace lies in the final Fourier response relation. The prime-shell adjoint residual remains the membership equation after all typed legs are assembled.

## Disposition

In the faithful retained multi-rung architecture, the first-Adams constructor and its global completion are closed: retain the common labelled source and both Green realizations as a complemented joint graph. The four matrix-unit equality remains open only for the stronger source-forgetting single-metric interface. Aspect must choose which interface the successor G4 contract requires.