# Kraus-support route or invariant quantum barrier

## Bounded question

For a finite family of source-authorized quantum operations, when does some
finite channel word produce a positive probability of entering a target
subspace, and what representation-independent certificate proves that every
authorized word fails?

This packet treats finite-dimensional completely positive maps. It does not
identify mathematical channel authority with laboratory control.

## Frozen model

Let \(H\) be finite-dimensional, let \(\rho\geq0\) be a nonzero source state,
and let \(P_B\) be the orthogonal projector onto the target subspace \(B\).
Let the finite authorized family be

\[
\Phi_g(X)=\sum_{\alpha}K_{g,\alpha}XK_{g,\alpha}^*,
\qquad g\in\mathcal G.
\]

The maps may be trace preserving or trace nonincreasing. A channel word
\(w=g_k\cdots g_1\) opens a probabilistic route when

\[
\operatorname{Tr}\bigl(P_B\Phi_w(\rho)\bigr)>0.
\]

The controller is assumed able to select \(w\), not an individual Kraus
index sequence.

## Positive support lemma

For every positive operator \(X\),

\[
\operatorname{supp}\Phi_g(X)
=
\operatorname{span}_{\alpha}
K_{g,\alpha}\operatorname{supp}X.
\]

Indeed, write \(X=X^{1/2}X^{1/2}\). Each summand is

\[
K_{g,\alpha}XK_{g,\alpha}^*
=
(K_{g,\alpha}X^{1/2})(K_{g,\alpha}X^{1/2})^*.
\]

The kernel of a sum of positive operators is the intersection of their
kernels. Taking orthogonal complements gives the span of their ranges. Since
\(X^{1/2}\) has range \(\operatorname{supp}X\), the formula follows.

Consequently,

\[
\operatorname{Tr}(P_BX)>0
\quad\Longleftrightarrow\quad
P_B\operatorname{supp}X\neq0
\]

for positive nonzero \(X\). There is no destructive cancellation between
Kraus branches at this probability layer.

## Reachable-support filtration

Set

\[
R_0=\operatorname{supp}\rho
\]

and

\[
R_{k+1}
=
R_k+
\sum_{g\in\mathcal G}\sum_{\alpha}K_{g,\alpha}R_k.
\]

Induction gives

\[
R_k
=
\operatorname{span}
\left\{
K_{g_j,\alpha_j}\cdots K_{g_1,\alpha_1}R_0:j\leq k
\right\}.
\]

Define the probabilistic constructor distance

\[
d_{\rm CP}(\rho,B)
=
\min\{k:P_BR_k\neq0\},
\]

with value infinity if the set is empty.

## CP route-or-barrier theorem

Exactly one of the following occurs.

### Positive-probability route

For a least \(k\), \(P_BR_k\neq0\). Then some Kraus-product branch of length
at most \(k\) has nonzero target overlap. Forgetting its Kraus labels produces
a channel word \(w\) of the same length, and positivity implies

\[
\operatorname{Tr}\bigl(P_B\Phi_w(\rho)\bigr)>0.
\]

Conversely, positive target probability for a word of length \(k\) forces at
least one of its Kraus-product branches to meet \(B\). Therefore
\(d_{\rm CP}\) is exactly the shortest authorized channel-word length having
positive target probability.

### Invariant quantum barrier

The filtration stabilizes at the smallest subspace \(R_\infty\) containing
\(\operatorname{supp}\rho\) and invariant under every authorized Kraus
operator. If

\[
P_BR_\infty=0,
\]

then every authorized channel word has zero target probability.

Conversely, any subspace \(R\) satisfying

\[
\operatorname{supp}\rho\subseteq R,
\qquad
K_{g,\alpha}R\subseteq R,
\qquad
P_BR=0
\]

for all authorized labels is a complete prohibition certificate.

As in the linear theorem, the filtration either finds a route or stabilizes
after at most \(\dim H-\dim R_0\) strict dimension increases.

## Kraus-representation independence

The theorem must not depend on a chosen Kraus frame. If
\(\{L_\beta\}\) is another Kraus representation of the same map, then after
padding by zero operators there is an isometry of coefficient spaces such
that every \(L_\beta\) is a linear combination of the \(K_\alpha\), and vice
versa on their operator spans. Hence for every subspace \(R\),

\[
\operatorname{span}_\beta L_\beta R
=
\operatorname{span}_\alpha K_\alpha R.
\]

Thus the one-step support transformer

\[
R\longmapsto\operatorname{supp}\Phi(P_R)
\]

is intrinsic to the completely positive map. So are the reachable filtration,
constructor distance, and canonical invariant barrier.

Individual branch names are gauge data. Existence of a target-reaching branch
is intrinsic because it is equivalent to positive target probability.

## What the theorem does not grant

The following layers are distinct.

1. A Kraus branch has nonzero target amplitude.
2. The unconditioned channel word has positive target probability.
3. The probability has a useful lower bound.
4. The controller can herald or select the favorable branch.
5. The target state can be prepared deterministically and robustly.

The theorem proves the equivalence of the first two and decides whether they
ever occur. It proves none of the last three.

For trace-nonincreasing operations, target success must be evaluated before
renormalization. Conditioning on survival changes the reported probability but
does not manufacture a route when the unnormalized target weight is zero.

## Dual barrier

If \(R_\infty\) is invariant under all Kraus operators, then
\(R_\infty^\perp\) is invariant under all adjoints \(K_{g,\alpha}^*\). When the
target lies in this orthogonal complement, it is a backward-invariant dark
sector.

This is the quantum selection-rule certificate: every authorized environmental
branch preserves the same separating subspace.

## Minimal examples

### Amplitude damping

With damping parameter \(0<\gamma\leq1\), take

\[
K_0=|0\rangle\langle0|+
\sqrt{1-\gamma}|1\rangle\langle1|,
\qquad
K_1=\sqrt\gamma|0\rangle\langle1|.
\]

Starting from \(|1\rangle\), the target \(|0\rangle\) is reached in one
channel use because \(K_1|1\rangle\neq0\). The unconditioned probability is
\(\gamma\). The controller does not thereby acquire authority to command the
\(K_1\) branch.

### Dephasing barrier

For Kraus operators diagonal in the computational basis, each computational
basis ray is invariant. Starting from \(|0\rangle\), the ray
\(\operatorname{span}\{|0\rangle\}\) is a barrier against reaching
\(|1\rangle\), although off-diagonal coherence of other states may change.

### Polarizer filter

An ideal polarizer at angle \(\theta\) is the single-Kraus,
trace-nonincreasing map \(X\mapsto P_\theta XP_\theta\). The crossed-polarizer
route is therefore a special case with no hidden branch labels. Its
unnormalized target weight records transmission loss; renormalizing after each
filter would erase the very cost that selects a finite optimal route.

### Toric-code noise

For a Pauli noise channel, Kraus products are error strings. A positive
probability of entering a logical-error sector appears when an authorized
error string reaches the relevant normalizer class. Minimum support weight is
the protected-sector analogue of constructor distance. This does not imply
that an experimenter can select that error branch, and it does not replace a
fault-tolerance threshold theorem.

## Finite certificate

A route certificate contains:

- the shortest channel word;
- one Kraus-index word with nonzero target overlap;
- the exact positive target contribution from that branch.

A prohibition certificate contains:

- a basis for the stabilized \(R_\infty\);
- invariance checks for every authorized map, expressed intrinsically as
  \(\operatorname{supp}\Phi_g(P_{R_\infty})\subseteq R_\infty\);
- the target-dark check \(P_BR_\infty=0\).

The intrinsic invariance check avoids making the certificate depend on an
arbitrary Kraus decomposition.

## Exact falsifiers

- A shorter channel word with positive target probability than the reported
  distance.
- A purported barrier for which one authorized map sends a supported state
  outside the barrier.
- A target vector lying in the claimed target-dark reachable support.
- A result that changes under replacement by an equivalent Kraus family.
- Inferring deterministic preparation from one positive branch contribution.
- Renormalizing a trace-decreasing route before reporting its success weight.
- Adding a measurement of the environment and branch-conditioned feedback
  without separately authorizing that interface.
- Promoting nonzero probability to robust control without a uniform lower
  bound.

## Deutschian explanation

A quantum transition is forbidden relative to the authorized channels when a
single invariant support sector traps every environmental branch and excludes
the target. A transition is merely route-deficient when a shortest channel
word breaks that sector and at least one branch deposits positive weight in the
target.

The explanation is resistant to variation for a specifically quantum reason:
positive branch weights cannot cancel. A proposed counter-route must either
identify an authorized Kraus-support action leaving the barrier or fail with
zero target probability. What may still vary is likelihood, heralding, and
physical controllability; those require additional constructor data.

## Claim boundary

This is an exact finite-dimensional theorem about support reachability under a
frozen family of completely positive maps. It does not classify infinite
operator-algebra closures, prove uniform lower probabilities, authorize access
to an environment, or compile abstract channels into physical devices.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The hoped-for gain was a quantum route theorem in which positivity
removes the cancellation ambiguity of the linear span.

Post-objective: excitement 10/10, confidence 9.5/10, realized information gain
10/10. The support transformer is Kraus-frame invariant, and a surviving
branch is exactly equivalent to positive unconditioned target probability.
The remaining sharp boundary is between positive-probability reachability and
branch-selective or deterministic control.
