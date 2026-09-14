# The enhanced incidence lattice realizes the minimal two-leg source

## Question

Does the audited four-point enhanced incidence lattice contain two distinct chains with opposite conductor boundaries whose sum is the primitive cycle required by the minimal source complex?

## Claim boundary

This realizes the minimal source chain complex inside the audited occurrence/conductor lattice. It does not construct the cycle-form map sending the two chains separately to the logarithmic and face target legs, nor physical-chain compatibility.

## Audited incidence complex

Use the point order

\[
(++,+-,-+,--)
\]

and normalized incidence matrix

\[
K=
\begin{pmatrix}
0&0&1&-1\\
0&1&0&-1\\
1&-1&-1&1
\end{pmatrix}.
\]

The audited result states that \(K\) is surjective and

\[
\ker K=\mathbb Z(1,1,1,1)^T.
\]

The required conductor boundary is

\[
r_{\rm cond}=(0,-1,1)^T.
\]

## Positive two-leg realization

Define

\[
e_{\log}=(1,0,1,1)^T,
\qquad
e_{\rm face}=(0,1,0,0)^T.
\]

Then

\[
Ke_{\log}=r_{\rm cond},
\qquad
Ke_{\rm face}=-r_{\rm cond},
\]

and

\[
e_{\log}+e_{\rm face}=(1,1,1,1)^T
\]

is the primitive kernel cycle.

All integral solutions of \(Kx=r_{\rm cond}\) are

\[
x=(t,t-1,t,t)^T.
\]

Requiring both \(x\) and \((1,1,1,1)^T-x\) to be nonnegative forces \(t=1\). Hence the displayed pair is the unique nonnegative decomposition of the primitive cycle into opposite-boundary legs.

## Chain embedding

Let the minimal source differential be \((1,-1)\). Sending its two degree-one generators to \(e_{\log},e_{\rm face}\) and its degree-zero generator to \(r_{\rm cond}\) gives

\[
K
\begin{pmatrix}e_{\log}&e_{\rm face}\end{pmatrix}
=
r_{\rm cond}
\begin{pmatrix}1&-1\end{pmatrix}.
\]

Thus the minimal two-leg complex embeds as a chain subcomplex of the enhanced incidence complex.

## Remaining map

The source complex is now materialized algebraically in an audited source lattice. The missing arrow is the support-sensitive relative Stokes/cycle-form pairing that sends

\[
e_{\log}\mapsto(1,0)^T,
\qquad
e_{\rm face}\mapsto(0,1)^T,
\]

while intertwining \(K\) with the residue differential. The source audit explicitly retains physical-chain compatibility as unresolved.

## Computed result

The incidence identity \(\Phi_{\rm exc}=JK\), surjectivity of \(K\), primitive kernel, opposite boundaries, and chain embedding all verify exactly. The displayed chains are nonnegative. Since every solution of \(Kx=r_{\rm cond}\) differs by an integral multiple of the all-ones kernel vector, simultaneous nonnegativity of \(x\) and the complementary primitive-cycle chain forces the displayed decomposition uniquely.

## Disposition

The minimal two-leg source complex is realized as the unique nonnegative chain subcomplex of the audited enhanced incidence lattice. The missing arrow has moved from source-object assignment to comparison: a support-sensitive relative Stokes/cycle-form map must send the two realized incidence chains to the logarithmic and face target legs. Physical-chain compatibility remains explicitly unresolved in the source artifact.
