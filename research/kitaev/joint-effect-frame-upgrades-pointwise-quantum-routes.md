# Joint effect frames upgrade pointwise quantum routes

## Bounded question

Suppose no nonzero source direction is permanently target-dark, but different
directions may require different authorized channel words. When can these
pointwise routes be compiled into a finite protocol having a uniform positive
success margin?

## Frozen model

Let \(A\subseteq H\) be a finite-dimensional source subspace with projector
\(P_A\), and let \(P_B\) project onto a target subspace. For every authorized
channel word \(w\), define its target effect on the source by

\[
E_w=P_A\Phi_w^*(P_B)P_A.
\]

Then \(E_w\geq0\), and for a source state \(\rho\) supported in \(A\),

\[
\operatorname{Tr}\bigl(P_B\Phi_w(\rho)\bigr)
=
\operatorname{Tr}(E_w\rho).
\]

The effect includes every unobserved Kraus branch. No branch-selective control
is assumed.

## Three quantitative route notions

The following are different.

### Statewise route coverage

Every nonzero \(v\in A\) has some authorized word, possibly depending on
\(v\), such that

\[
\langle v,E_wv\rangle>0.
\]

Equivalently,

\[
\bigcap_w\ker E_w=\{0\}.
\]

### One-word uniform route

One authorized word satisfies

\[
E_w\geq\varepsilon P_A
\]

for some \(\varepsilon>0\). The same word succeeds with probability at least
\(\varepsilon\) on every normalized source state.

### Randomized finite-word uniform route

A finite list \(w_1,\ldots,w_r\) and probabilities \(p_j>0\) satisfy

\[
Q=\sum_{j=1}^r p_jE_{w_j}\geq\varepsilon P_A.
\]

The controller samples \(j\), applies the entire word \(w_j\), and ignores its
Kraus branch. Its average target probability is at least \(\varepsilon\).

One-word uniformity implies randomized uniformity, which implies statewise
coverage. Neither converse to the first implication holds in general.

## Finite effect-frame theorem

In finite-dimensional \(A\), statewise route coverage is equivalent to the
existence of a randomized finite-word uniform route.

Moreover, at most \(\dim A\) words are required.

### Proof

Begin with \(N_0=A\). If \(N_j\neq0\), statewise coverage supplies an
authorized word \(w_{j+1}\) for which \(E_{w_{j+1}}\) does not vanish on all of
\(N_j\). Set

\[
N_{j+1}=N_j\cap\ker E_{w_{j+1}}.
\]

The dimension strictly drops. After at most \(\dim A\) choices,

\[
\bigcap_{j=1}^r\ker E_{w_j}=\{0\}.
\]

For positive operators,

\[
\ker\left(\sum_jp_jE_{w_j}\right)
=
\bigcap_j\ker E_{w_j}
\]

whenever every \(p_j>0\). Hence \(Q\) is positive definite on \(A\). In
finite dimension its least eigenvalue is positive, so

\[
Q\geq\lambda_{\min}(Q)P_A.
\]

The reverse direction is immediate: if the average is positive on \(v\), at
least one summand is positive on \(v\).

## What is being compiled

The theorem compiles a jointly faithful family of target effects into a
classically randomized experiment. It does not compile the family into one
channel word.

This is the same algebraic pattern as adding logical loop probes to syndrome:
each individual effect may have a kernel, while their complete finite family
has trivial common kernel. The coefficient lens is now the positive cone, so
the aggregate is a sum of effects rather than an ordered channel product.

## Smallest witness that one word need not suffice

On a two-dimensional source let

\[
E_0=|0\rangle\langle0|,
\qquad
E_1=|1\rangle\langle1|.
\]

Each effect has a one-dimensional kernel, so neither word has a uniform
margin. Their kernels intersect trivially. Choosing either word with
probability one half gives

\[
Q=\frac12E_0+\frac12E_1=\frac12I.
\]

Thus the randomized protocol succeeds with average probability at least one
half on every source state. Calling this a one-word controller would erase the
constructor type.

## Optimal randomized margin

For a frozen finite candidate list, the best guaranteed margin is

\[
\varepsilon_*=
\max_{p_j\geq0,\ \sum_jp_j=1}
\lambda_{\min}\left(\sum_jp_jE_{w_j}\right).
\]

Equivalently, maximize \(\varepsilon\) subject to

\[
\sum_jp_jE_{w_j}\geq\varepsilon P_A.
\]

This is a semidefinite optimization problem. It prices only classical word
randomization. Word length, loss, time, and device cost require additional
constraints on the admissible distribution.

The dual hostile state minimizes the best weighted detection probability. At
an optimum it identifies the source directions responsible for the smallest
eigenvalue and therefore the next observation word with highest potential
information gain.

## Common-word obstruction

Joint faithfulness does not imply that some product or mixture is an authorized
single word. The effects live after Heisenberg pullback:

\[
E_w=P_A\Phi_w^*(P_B)P_A.
\]

Adding effects represents classical mixing of complete experiments. Composing
channels changes \(w\) and generally does not add their effects. Therefore an
argument replacing \(E_{w_1}+E_{w_2}\) by the effect of an undeclared composite
commits a sum-versus-product typing error.

## Completion-stable form

For a cutoff family \(A_N\), effects \(E_{w,N}\), and one fixed finite word
list with one fixed probability vector, completion-stable control requires

\[
\inf_N
\lambda_{\min}
\left(
\sum_jp_jE_{w_j,N}
\right)>0.
\]

Pointwise positive definiteness at every cutoff does not imply this bound.

### Two-dimensional collapse

Let

\[
E_{0,N}=|0\rangle\langle0|,
\qquad
E_{1,N}=N^{-1}|1\rangle\langle1|.
\]

Every cutoff is jointly faithful. For any fixed mixture with positive weight on
both words,

\[
\lambda_{\min}(Q_N)leq N^{-1},
\]

so the margin collapses. The invisible state has not appeared at any finite
stage; inverse effect norms escape in the limit.

This is the exact finite-dimensional hostile model for completion losing
strict invertibility while preserving every finite zero/nonzero certificate.

## Growing-word obstruction

Even if each cutoff admits a positive aggregate, completion stability fails as
a fixed constructor claim when the required word list grows with \(N\). The
finite effect-frame theorem supplies at most \(\dim A_N\) words at each cutoff,
not one cutoff-independent finite family.

A legitimate pro-system theorem must freeze:

- the authorized word family or a uniform cost budget;
- the mixing law;
- the source normalization;
- and the comparison maps between cutoffs.

Otherwise cutoffwise randomized observability is not a completed controller.

## Relation to invariant barriers

The qualitative route theorem asks whether the common kernel is nontrivial.
The present theorem measures how far the common kernel is from appearing:

\[
\text{barrier absent}
\quad\Longleftrightarrow\quad
\varepsilon_*>0
\]

at a fixed finite cutoff, after finite classical randomization is admitted.

In completion, the qualitative barrier may remain absent at every stage while
\(\varepsilon_*\) tends to zero. The limiting obstruction is then not a finite
invariant subspace but a sequence of asymptotically dark normalized states.

## Critics

### Randomization does not guarantee each run succeeds

Correct. The guarantee is on average over the declared classical randomizer
and quantum channel. Per-run success or deterministic state transfer is a
stronger task.

### The chosen word may depend on knowing the input

Statewise coverage alone has that weakness. The finite effect-frame theorem
removes it: the randomized distribution is fixed independently of the unknown
input state.

### Positive effects might come from unauthorized measurements

Only effects pulled back from frozen authorized channel words and the frozen
target projector may enter the frame. Arbitrary positive operators would make
the theorem operationally empty.

### Mixing may be unavailable

Then the theorem remains a joint-faithfulness result, not an executable
protocol. Classical randomization is a separately typed constructor.

## Exact falsifiers

- A nonzero source vector in the common kernel of the claimed effect frame.
- A reported margin larger than the least eigenvalue of the aggregate effect.
- A state-dependent choice of word presented as a fixed controller.
- An additive effect aggregate presented as one composed channel word.
- A Kraus branch selected without an authorized environment measurement.
- A cutoff-dependent word family presented as one finite completed protocol.
- Positive margins at all cutoffs with no uniform lower bound presented as
  completion-stable control.
- An effect not derived from an authorized channel word and target readout.

## Deutschian explanation

Uniform probabilistic capability does not require one universally effective
route. It requires a finite set of complementary routes whose dark sectors
have no common direction, plus an authorized classical mechanism for choosing
among them. The source of robustness is therefore not repetition of one weak
route but transversal coverage of its kernel by other routes.

Completion failure has an equally concrete explanation: normalized source
directions can rotate or escape toward the joint dark boundary faster than the
finite effects control them. Every finite packet remains faithful, yet the
cost of inversion diverges. The missing theorem is a uniform frame bound, not
another finite nonvanishing check.

## Claim boundary

This is an exact finite-dimensional effect-frame theorem and a precise
completion falsifier. It does not prove that classical randomization is
physically available, optimize constrained channel words, or establish a
uniform frame bound for any infinite source system.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The target was to locate the smallest additional constructor separating
positive reachability from uniform probabilistic control.

Post-objective: excitement 10/10, confidence 9.5/10, realized information gain
10/10. The missing constructor is exactly classical randomization over a finite
jointly faithful effect frame. At fixed finite dimension, pointwise route
coverage already supplies such a frame with at most \(\dim A\) words. The
remaining hard obstruction is solely uniformity across completion.
