# Path observability is a Gramian cocycle, not endpoint shear

## Bounded question

Can the endpoint shear of a composed source path determine the path's faithful
observation energy?

## Typed segment data

Let \(S_{a,b}:X_a\to X_b\) be the state transport over a segment and let
\(J_{a,b}:X_a\to Y_{a,b}\) collect all source-authorized observations made on
that segment. Its observation energy and Gramian are

\[
E_{a,b}(x)=\|J_{a,b}x\|^2,
\qquad
W_{a,b}=J_{a,b}^*J_{a,b}.
\]

For consecutive segments, the second observation acts on the transported
state. Therefore

\[
J_{a,c}=
\begin{pmatrix}
J_{a,b}\\
J_{b,c}S_{a,b}
\end{pmatrix}
\]

and the exact relationship-energy law is

\[
W_{a,c}
=W_{a,b}+S_{a,b}^*W_{b,c}S_{a,b}.
\]

This is an additive cocycle twisted by state transport. It is not a function
of the total endpoint shear \(S_{a,c}\) alone.

## Faithfulness theorem

Because every Gramian is positive semidefinite,

\[
\ker W_{a,c}
=ker W_{a,b}
\cap
S_{a,b}^{-1}(\ker W_{b,c}).
\]

Thus the concatenated observation is faithful exactly when no nonzero initial
state is hidden on the first segment and transported into the hidden subspace
of the second. Neither segment need be faithful separately; complementary
rows can repair one another dynamically.

## Identity endpoint with positive path energy

Take the rank-two shears

\[
S_1=S(F),\qquad S_2=S(-F),\qquad S_2S_1=I,
\]

with \(F\ne0\), and use the same one-row sensor

\[
C=(1,0)
\]

on both segments. Then

\[
W_1=C^*C,
\qquad
W_2=C^*C,
\]

while the full path Gramian is

\[
W(F)=W_1+S(F)^*W_2S(F)
=
\begin{pmatrix}
2&F\\
\overline F&|F|^2
\end{pmatrix}.
\]

Its determinant is \(|F|^2>0\), so it is positive definite. The endpoint
transport is nevertheless the identity. The constant identity path with no
observations has the same endpoint and zero Gramian. Endpoint shear therefore
cannot reconstruct path energy or observability.

## Positive finite Gramians can collapse

Set \(F_N=1/N\). Every

\[
W_N=
\begin{pmatrix}
2&1/N\\
1/N&1/N^2
\end{pmatrix}
\]

is positive definite, since its leading principal minors are \(2\) and
\(1/N^2\). But for the normalized vector \(e_2\),

\[
e_2^*W_Ne_2=\frac1{N^2}\longrightarrow0.
\]

Hence \(\lambda_{\min}(W_N)\to0\). Cutoffwise faithfulness does not imply
completion-stable observability, even when every total endpoint shear is
exactly the identity.

## Relation to conserved forms

The Hermitian form of milestone 2633 and the observation Gramian have different
types. A conserved form satisfies \(S^*HS=H\) and may be indefinite. A Gramian
is positive semidefinite and accumulates by the twisted additive law above.
Conservation cannot replace observability, and positive observation energy need
not be conserved.

Grothendieck's terminal-amplitude shear supplies the required state transport
for the cocycle. It does not supply the observation rows \(J_{a,b}\). Those
must be derived independently from the tail, seam, primitive, square, and
archimedean source channels.

## Carrier geometry versus coefficient lens

Path concatenation and transport belong to shared Carrier geometry. The
adjoint, positive norm, authorized sensor rows, and lower observability bound
belong to the chosen coefficient and interface lens. A total holonomy or shear
is geometric transport data, not a positive record of what was observed along
the path.

## Exact audit and falsifiers

The checker verifies the symbolic Gramian cocycle, the kernel-intersection law
on exhaustive small rational fixtures, the identity-total-shear positive
Gramian, and the collapsing family through exact principal minors and normalized
witness energies.

The relationship-energy theorem is falsified by any typed concatenation whose
direct stacked observation Gramian differs from the cocycle. Uniform
observability is falsified by any normalized state sequence with energy tending
to zero. An endpoint-only reconstruction is falsified by two paths with equal
total transport and unequal Gramians.

## Claim boundary

This is an abstract finite-dimensional compiler theorem. It does not derive
the theta/Tate observation rows, prove their finite or uniform observability,
construct a positive reciprocal tail-seam energy, establish passivity, or prove
RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
9/10. The alternatives were endpoint determination and an independently
compositional observation object. The cocycle, kernel, identity-path hostile,
and collapsing lower direction were frozen measurements.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Endpoint determination was eliminated by equal-holonomy paths with
different Gramians. The observation object acquired an exact cocycle and
kernel law. Finite positivity was separated from uniform observability by an
exact \(1/N^2\) witness. Theta source rows remain unresolved.
