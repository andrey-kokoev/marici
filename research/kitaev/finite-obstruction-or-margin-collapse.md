# Finite obstruction or margin collapse

## Bounded question

Once a source model has been normalized into a compact carrier with closed
finite constraints, what exact forms can a completion failure take?

## Frozen compact audit

Let \(X\) be a compact space of normalized candidate realizations. Let

\[
C_1,C_2,\ldots
\]

be closed source constraints, ordered by the declared cutoff or dependency
schedule. Define the nested feasible sets

\[
K_N=\bigcap_{n=1}^N C_n
\]

and

\[
K_\infty=\bigcap_{n=1}^{\infty}C_n.
\]

Let

\[
m:X\to[0,\infty)
\]

be a continuous capability margin. Examples include a least singular value,
least Gram eigenvalue, target success floor, determinant modulus, spectral gap,
or distance from a forbidden kernel stratum.

The desired strict property is existence of \(x\in K_\infty\) with

\[
m(x)>0.
\]

## Optimal slack sequence

When \(K_N\neq\varnothing\), define

\[
\gamma_N=\max_{x\in K_N}m(x).
\]

The maximum exists by compactness. Because the feasible sets are nested,

\[
\gamma_{N+1}\leq\gamma_N.
\]

Thus the optimal finite capability margin has a limit.

## Margin-limit theorem

If every \(K_N\) is nonempty, then \(K_\infty\) is nonempty and

\[
\lim_{N\to\infty}\gamma_N
=
\max_{x\in K_\infty}m(x).
\]

### Proof

The inequality from right to left is immediate because
\(K_\infty\subseteq K_N\).

Choose a maximizer \(x_N\in K_N\). Compactness gives a convergent subnet, or a
subsequence in the metrizable finite-dimensional cases used in the programme,
with limit \(x_*\). For every fixed \(j\), the tail lies in \(K_j\), and
\(K_j\) is closed, so \(x_*\in K_j\). Hence \(x_*\in K_\infty\). Continuity
gives

\[
m(x_*)=\lim_N\gamma_N.
\]

Therefore the limit cannot exceed the best margin on \(K_\infty\), completing
the equality.

## Completion dichotomy

Relative to the frozen ordering, exactly one of the following occurs.

### Finite obstruction

For a first \(N\),

\[
K_N=\varnothing.
\]

The first \(N\) constraints form a finite incompatibility witness. A smaller
unsatisfiable core may exist inside the prefix and should be extracted when
possible.

### Globally feasible with positive margin

Every \(K_N\) is nonempty and

\[
\gamma_\infty=lim_N\gamma_N>0.
\]

Then some global realization satisfies every constraint with a strictly
positive margin.

### Globally feasible but capability collapses

Every \(K_N\) is nonempty, yet

\[
\gamma_N\downarrow0.
\]

The completed constraint diagram has realizations, but every global realization
lies on the zero-margin boundary. This is the only way the strict capability
can disappear for the first time at completion inside the compact audit.

The third case is not failure of carrier existence. It is failure of the open
capability property.

## Uniform margins become finitely refutable

Fix a desired threshold \(\varepsilon>0\). If

\[
\gamma_\infty<\varepsilon,
\]

then monotone convergence gives some finite \(N\) for which

\[
\gamma_N<\varepsilon.
\]

Thus a declared uniform margin is finitely refutable. What can evade every
finite zero/nonzero test is only the unquantified open property
\(m>0\).

This is why pricing the margin changes the logical type of the theorem.

## Canonical hostile sequence

In the collapse case, choose exact maximizers \(x_N\). Then

\[
x_N\in K_N,
\qquad
m(x_N)=\gamma_N\to0.
\]

Every cluster point lies in \(K_\infty\cap m^{-1}(0)\). This maximizing
sequence is a canonical hostile family relative to the cutoff ordering and
margin.

One may also choose near-maximizers when exact optimization is unavailable:

\[
m(x_N)\geq\gamma_N-\varepsilon_N,
\qquad
\varepsilon_N\to0.
\]

They have the same limiting diagnosis.

## Four programme instances

### Invertibility

For a bounded finite matrix realization \(A(x)\), take

\[
m(x)=\sigma_{\min}(A(x)).
\]

Strict invertibility is \(m>0\). Completion-only loss means the best achievable
least singular value tends to zero.

### Observability

For an observability Gramian \(W(x)\), take

\[
m(x)=\lambda_{\min}(W(x)).
\]

Finite observability at each cutoff is not enough; the optimal observability
slack curve decides completion stability.

### Joint effect frames

For a frozen randomized word family with aggregate target effect \(Q(x)\), use

\[
m(x)=\lambda_{\min}(Q(x)|_A).
\]

Margin collapse produces asymptotically dark normalized source states.

### Constructor descent

For a normalized target current \(L(x)\) controlled by \(Q(x)\), a bounded
domination margin may be expressed through the reciprocal sharp generalized
eigenvalue. Vanishing reciprocal margin means domination constants diverge.

The representation must make the chosen reciprocal continuous on the compact
domain; kernel changes otherwise require stratification.

## Noncompact escape is a different certificate

If the normalized candidate space \(X\) is not compact, the theorem does not
apply. A finite-feasible sequence can leave every compact subset without
approaching a boundary point in the declared space.

Examples include:

- unbounded inverse operators;
- unbounded graph norms;
- increasing carrier dimension;
- translations escaping to infinity;
- and factor coordinates without source normalization.

The correct witness then has two parts:

1. every finite prefix is satisfied;
2. a declared coercive quantity diverges or no convergent normalized subnet
   exists.

Calling both phenomena “margin collapse” hides whether the limit point exists
inside the carrier.

## Multiple margins

For finitely many continuous margins \(m_1,ldots,m_r\), joint strict
capability is captured by

\[
m(x)=\min_j m_j(x).
\]

For infinitely many margins, pointwise positivity of each is weaker than one
uniform lower bound. The source packet must specify whether it requires:

- every individual margin positive;
- a common positive infimum;
- or a weighted/topological seminorm family.

These are different completion claims.

## What defines first

“First” is not supplied by compactness. It is supplied by the audit schedule:

- temporal order;
- spatial support radius;
- constructor word length;
- arithmetic cutoff;
- dependency partial order;
- or declared information cost.

Given that order, the first finite obstruction is the least prefix with empty
feasible set. In a collapse case there is no first zero-margin prefix; the
primary invariant is instead the monotone slack curve \(N\mapsto\gamma_N\).

Changing the order can change the first prefix but not the full intersection or
the completed optimal margin.

## DPC: capability-slack explanation

The conjecture is:

> Whenever all finite normalized closed constraints are satisfiable but a
> strict completed capability fails, the explanation is a source-derived
> continuous margin whose optimal finite slack converges to zero. If no such
> margin is typed, “loss at completion” is only a restatement of failure, not a
> mechanism.

Within the frozen compact scalar-margin model this is a theorem. The open
research content is finding the correct source-derived margin and proving its
continuity or identifying the noncompact escape that prevents one.

## Critics

### Maximizing over realizations may ignore a fixed physical trajectory

Correct. The optimal slack answers existential realizability. If the source
selects one distinguished compatible trajectory, its own margin sequence must
be audited separately. The optimization must not replace source authority.

### A continuous scalar margin may not capture a kernel-stratified problem

Correct. One may need separate compact strata or a lower-semicontinuous defect
functional. Continuity is a theorem hypothesis, not presentation convenience.

### Computing \(\gamma_N\) can be hard

Correct. The result classifies the obstruction even when optimization is not
efficient. Certified upper and lower bounds can still bracket the slack curve.

## Machine-readable classification

```json
{
  "code": "finite_obstruction_or_margin_collapse",
  "audit_order": "declared cutoff order",
  "compact_normalized_domain": true,
  "constraint_prefix": "N",
  "finite_feasible": true,
  "capability_margin": "m",
  "optimal_slack": "gamma_N",
  "classification": "finite_incompatibility | positive_global_margin | completion_margin_collapse",
  "first_empty_prefix": null,
  "limit_margin": 0
}
```

For a noncompact domain, the code must instead identify the escaping coercive
quantity and must not claim compact margin collapse.

## Exact falsifiers

- A nonempty prefix reported as the first finite obstruction.
- A claimed collapse while \(\inf_N\gamma_N>0\).
- A claimed positive global margin exceeding \(\lim_N\gamma_N\).
- A discontinuous or undefined defect presented as the theorem's continuous
  margin without stratification.
- A noncompact coordinate space silently treated as compact.
- Different cutoff tables treated as restrictions of one fixed table.
- A source-selected realization replaced by an unauthorized optimizer.
- A different audit order used to revise “first” without declaring the change.

## Deutschian explanation

In a compact normalized theory, capability cannot vanish mysteriously between
all finite stages and completion. Its best possible slack must be squeezed
continuously to the boundary. The slack curve says how and how fast.

If no such boundary sequence exists, either a finite law already fails or the
model omitted the noncompact degree of freedom through which the obstruction
escapes. This converts infinity from a location where exceptions hide into a
diagnostic choice between finite inconsistency, boundary collapse, and
noncompact escape.

## Claim boundary

This packet proves the dichotomy for nested closed constraints on a compact
space with a continuous scalar margin. It does not choose the physically
correct margin or make its finite optimization computationally efficient.

## Process calibration

Pre-objective: excitement 10/10, confidence 9.5/10, expected information gain
10/10. The target was an exhaustive classification of completion failure after
normalization and closed-law compactness.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Completion failure now has three typed certificates: finite
incompatibility, compact boundary-margin collapse, or noncompact escape. The
monotone optimal slack curve replaces vague appeals to the infinite limit.
