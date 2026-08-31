# RH G1.1 closure candidate and G1.3 boundary

## Question

Do the retained-history results now satisfy the authoritative G1.1 gate, or
does arithmetic endpoint loading remain part of that gate?

## Authoritative gate separation

The publication ledger states:

- G1.1: source-derived causal history, uniform lower bounds for
  \(I\pm iH\), and incidence compression to \(\tau\);
- G1.3: typed coefficient polarization and endpoint-loading bound.

Therefore an additional Euler or prime loading is not part of G1.1 unless the
ledger is revised.  It belongs to G1.3.  The earlier qualification that G1.1
must remain open until arithmetic loading is identified mixed these two gates.

## Clause 1: source-derived causal history

On the retained relative history graph, causal history \(H\) and its reflected
adjoint \(H^*\) have a common closed form domain.  The reciprocal odd operator
is

\[
T=\frac{H-H^*}{2}.
\]

The retained graph carries the exact quarter-turn maps

\[
Q_\pm x=\frac1{\sqrt2}(x\pm iHx).
\]

This realizes history as a source graph rather than a fitted scalar block.

## Clause 2: uniform shifted-history lower bounds

The exact factorization is

\[
Q_\pm^*Q_\pm
=\frac12(I\pm iH)^*(I\pm iH).
\]

The theta-mass estimate gives

\[
Q_{L,\pm}^*Q_{L,\pm}\ge\frac18I
\]

uniformly in the retained labelled cutoff system.  Equivalently,

\[
\|(I\pm iH)x\|^2\ge\frac14\|x\|^2.
\]

This controls approximate as well as genuine \(\mp i\)-history modes.

## Clause 3: incidence compression

The source incidence is fixed by the exact twisted half-density histories:

\[
V_{\rm src}(e_0)=\Phi,
\qquad
V_{\rm src}(e_1)=\Phi'.
\]

Their traces are

\[
\operatorname{Tr}_{1/2}(\Phi)
=\begin{pmatrix}1/2\\1/2\end{pmatrix},
\qquad
\operatorname{Tr}_{1/2}(\Phi')
=\begin{pmatrix}1/4\\-1/4\end{pmatrix}.
\]

The relative Volterra identity and skew-adjointness give

\[
\langle\Phi',T\Phi\rangle=-\|\Phi\|_2^2,
\qquad
\langle\Phi,T\Phi'\rangle=\|\Phi\|_2^2.
\]

Hence

\[
V_{\rm src}^*iTV_{\rm src}
=i\tau
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
{\tau=-\|\Phi\|_2^2<0.}
\]

Thus \(\tau\) is a source compression, not a free parameter.

## Cutoff and label qualification

The history carrier is a retained direct sum over labels, and the theta block
is transported labelwise before arithmetic loading.  The compression above is
therefore the same source coefficient on each retained fibre and commutes with
finite label cutoffs.  This does not sum or erase prime and grade labels.

## Disposition

All three clauses named by G1.1 now have explicit source-derived formulas and
the required uniform operator bound.  G1.1 is therefore a closure candidate.

The following remain outside this closure claim:

- endpoint/radical descent and cutoff naturality beyond the retained history
  graph: G1.2;
- Euler/prime endpoint loading and its typed polarization bound: G1.3;
- prime off-diagonal control: G1.4;
- forgetting the retained source coordinate in an output-only pushforward;
- attaching the connected \(k\ge3\) return to the local first-Adams assembly.

No publication-ledger status is changed by this packet.  Status mutation should
follow review of the cited constructor identities and their closure domains.
No RH conclusion is authorized.
