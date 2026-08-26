# The Direct Target Seam Is the Unique Universally Robust Row

Keep the grounded Laplacian \(L>0\), target incidence \(h\), and candidate
seam incidence \(b\). Write

\[
R=h^*L^{-1}h,
\qquad
r_b=b^*L^{-1}b,
\qquad
\tau=b^*L^{-1}h.
\]

For a state \(u\) with energy \(E=u^*Lu\), the first-order seam score is

\[
S_b(u)=R|b^*u|^2-E|\tau|^2.
\]

Then

\[
S_b(u)\le0\quad\text{for every }u
\]

if and only if \(b\) is proportional to \(h\).

## Proof

The energy-dual inequality gives

\[
|b^*u|^2\le r_bE.
\]

Transfer-current Cauchy–Schwarz gives

\[
|\tau|^2\le Rr_b,
\]

with equality exactly when \(L^{-1/2}b\) and \(L^{-1/2}h\) are proportional,
equivalently \(b\parallel h\).

If \(b\parallel h\), equality holds in the transfer-current bound and the
energy-dual inequality makes \(S_b(u)\le0\) for all states. This is the direct
anchor-to-target seam direction.

If \(b\not\parallel h\), choose the Riesz witness

\[
u_b=L^{-1}b.
\]

Then

\[
b^*u_b=r_b,
\qquad
u_b^*Lu_b=r_b,
\]

and

\[
S_b(u_b)
=r_b(Rr_b-|\tau|^2)>0.
\]

Every nonparallel seam therefore worsens the target certificate for an
explicit state, at least for sufficiently small positive conductance.

## Exact chain witness

For the grounded chain

\[
L=\begin{pmatrix}2&-1\\-1&1\end{pmatrix},
\quad
h=\binom01,
\quad
b=\binom10,
\]

one has

\[
R=2,
\quad r_b=1,
\quad\tau=1,
\quad Rr_b-|\tau|^2=1.
\]

The Riesz witness is \(u_b=(1,1)^T\), and its score is one. For the direct
row \(b=h\), the transfer-current defect vanishes and the score is
nonpositive for every state.

## Restricted state classes

Universal robustness above quantifies over the full grounded coefficient
space. A nonparallel seam may still be robust on a proper source-authorized
state subspace if the Riesz witness and every other worsening direction are
inadmissible. The correct restricted theorem is

\[
S_b|_{\mathcal A}\le0
\]

for the frozen admissible state module \(\mathcal A\). Declaring a restriction
after finding the hostile witness would be answer-fitting; \(\mathcal A\)
must come from the source dynamics.

## Theta/Tate consequence

If Grothendieck needs a seam row whose certificate cannot worsen for any
admissible tail state, the direct target incidence is uniquely robust on the
full coefficient space. Any other seam requires a dynamical restriction or a
state-dependent score theorem. This separates a universally safe constructor
from an empirically favorable one.

## Falsifiers

- A nonparallel seam is called universally safe without excluding its Riesz
  witness from the source state class.
- The admissible state module is narrowed after the witness is found.
- Transfer-current equality is inferred from approximate numerical alignment.
- First-order robustness is promoted to finite-conductance robustness for a
  nonparallel seam without a separate theorem.
- Proportional algebraic incidence is confused with physical authority to add
  the direct edge.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to classify all seam directions with state-independent
first-order safety.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The direct target row is uniquely robust, every nonparallel row has an
explicit Riesz hostile, and restricted-state exceptions are precisely typed.
