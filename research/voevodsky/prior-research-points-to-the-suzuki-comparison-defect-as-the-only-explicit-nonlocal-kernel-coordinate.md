# Prior research points to the Suzuki comparison defect as the only explicit nonlocal kernel coordinate

## Search question

Which prior constructions contain a genuinely source-explicit, nonlocal, positive two-variable kernel that could populate the remaining augmented positive 2-simplex?

## Canonical de Branges kernel

The reflected multiplier supplies

\[
K_\Theta(z,w)
=
\frac{1-
\Theta(z)
\overline{\Theta(w)}}
{2\pi i(\bar w-z)}.
\]

This kernel has exactly the desired endpoint--gamma--prime boundary current, but

\[
K_\Theta\succeq0
\]

is equivalent to the Schur/Hermite--Biehler condition. It is the target kernel, not an independent positive constructor.

The finite-prime transition is not positive because each reflected Euler ratio changes orientation across the strip.

## Suzuki screw-line carrier

Suzuki constructs a source-explicit function

\[
S_t\in L^2(\mathbb R)
\]

unconditionally. Therefore

\[
G_{Suz}(t,u)
=
\frac12
\langle S_t,S_u\rangle_{L^2}
\]

is an unconditional positive nonlocal kernel containing endpoint, gamma, and prime data in one formula.

This is the closest existing object to the desired larger positive bulk.

However, equality with the arithmetic screw kernel

\[
G_{arith}(t,u)
=
g(t-u)-g(t)-g(u)+g(0)
\]

is equivalent to the zero-location theorem. Thus the useful object is not the asserted equality but the comparison defect

\[
\Delta_{Suz}(t,u)
=
G_{arith}(t,u)
-
G_{Suz}(t,u).
\]

The sign, rank, and factorization of \(\Delta_{Suz}\) are the most concrete nonlocal coordinates for the remaining obstruction.

## Projected Hardy resolvents

The boundary involution and Hardy projection define

\[
P_V
=
1_{\{1\}}(PQP)
\]

and the continuous family

\[
r_w=P_Vk_w.
\]

Its kernel

\[
K_V(z,w)
=
\langle P_Vk_w,k_z\rangle
\]

is positive unconditionally and total inside the intersection space \(V\).

Finite approximants

\[
r_w^{(n)}
=(PQP)^nk_w
\]

provide coherent positive kernels without selecting zeros.

The missing arithmetic identity is

\[
W(r_w*r_z^*)
=
2K_V(z,w).
\]

Hence define the resolvent comparison defect

\[
\Delta_V(z,w)
=
W(r_w*r_z^*)
-
2K_V(z,w).
\]

This is a second presentation of the same obstruction. The family may collapse when \(V=0\), so a lower survival bound is also required.

## Krein--Langer interpretation

The canonical arithmetic kernel has the exact decomposition

\[
K_\Theta
=
\frac{K_S-K_B}
{B\overline B}.
\]

Therefore any exact comparison between the unconditional positive Suzuki or projected-resolvent kernel and the arithmetic kernel must expose the model-space defect \(K_B\).

The most plausible identity has the structural form

\[
\Delta_{Suz}
=
-
R_B^*R_B
-
R_\partial^*R_\partial
+
R_{slack}^*R_{slack},
\]

with the terms determined by source maps rather than a posteriori Jordan decomposition.

If the comparison carrier is minimal and has no positive slack, the defect should reduce to the negative interior and endpoint features already classified.

This would identify the obstruction exactly but would not prove that it vanishes.

## Clifford and Green clue

The differentiated dual/canonical pairing produces the complete gamma--prime current. Ordered composition with the endpoint boost forces the mixed Clifford component

\[
B_{23}.
\]

Contour deformation identifies this with the source Green coupling. Thus any formula for \(\Delta_{Suz}\) should be derived through the same mixed boundary channel rather than by separately comparing prime, gamma, and endpoint pieces.

The Clifford carrier supplies the correct cross term, but its current realization is signed rather than positive.

## Phase-energy clue

The positive phase-energy carrier

\[
e_S=1+
\kappa_{loc,S}
\]

is the minimal known source norm on which the differentiated pairing and endpoint graph are bounded.

The bare prime Laplacian is too small at aligned resonances. Therefore any Suzuki comparison map should be defined first on the phase-energy augmented graph, not on the prime-edge completion alone.

## Falsified interpretations

Prior research rules out the following readings of the clue:

1. the de Branges kernel is positive merely because it is canonical;
2. the Suzuki norm already equals the Weil form;
3. projected Hardy resolvents are automatically arithmetic-faithful;
4. gamma and prime sectors factor as independent positive summands;
5. a local one-variable density can represent the complete positive kernel;
6. an abstract mixed contraction reconstructed from positive moments explains positivity.

## Most promising exact calculation

The next nonredundant calculation is the polarized comparison defect on the completed Gaussian source:

\[
\Delta_r(p,q)
=
W_r(p*q^*)
-
\langle
\Phi_{Suz,r}p,
\Phi_{Suz,r}q
\rangle.
\]

One should derive \(\Delta_r\) directly from the endpoint--gamma--prime formula and compare it with the independently known Krein--Langer feature:

\[
-A_{B,r}^*A_{B,r}
-
b_r^*b_r.
\]

There are three possible outcomes:

1. exact equality, which identifies Suzuki's positive carrier as the desired Schur bulk but leaves defect vanishing open;
2. equality plus a positive source-derived slack term, which yields a genuinely larger positive bulk candidate;
3. an additional indefinite remainder, showing that the Suzuki carrier is not aligned with the tetrahedral bulk.

## Why this calculation is optimal

It compares two objects that already exist independently:

1. the source-explicit unconditional Suzuki \(L^2\) carrier;
2. the source-explicit completed Weil form.

No GNS construction, Cholesky factorization, zero selection, or assumed Schur positivity is required to define their difference.

The result cannot by itself evade the arithmetic theorem, but it can determine whether prior research already contains the correct larger positive bulk and isolate its exact failure mode.

## Disposition

The search found one concrete clue stronger than the abstract kernel programme: Suzuki's screw-line \(L^2\) kernel is an unconditional nonlocal positive carrier with all arithmetic sectors present.

The optimal next step is not to assert its equality with the Weil kernel. It is to compute and factor the polarized comparison defect \(\Delta_{Suz}\) on the completed source graph and match it against the Krein--Langer plus odd-endpoint defect.
