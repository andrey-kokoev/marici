# Hankel rank without a singular gap is not stable explanation

## Bounded question

When does exact finite Hankel rank survive noise and completion, and what
quantitative invariant distinguishes algebraic observability from stable
predictive reconstruction?

## Frozen finite context map

At cutoff \(X\), choose finite source-normalized preparation and test spaces
\(P_X\) and \(S_X\). Let

\[
H_X:P_X\longrightarrow S_X^*
\]

be the finite Hankel or context-response map.

Exact predictive faithfulness on a declared \(r\)-dimensional state sector is

\[
\ker H_X=\{0\}.
\]

Stable predictive faithfulness additionally requires a lower bound

\[
\|H_Xx\|\geq c\|x\|
\]

with \(c>0\) independent of cutoff on that sector.

The first condition is algebraic. The second is topological and quantitative.

## Singular-gap theorem

Let the nonzero singular values of \(H_X\) be

\[
\sigma_1(H_X)\geq\cdots\geq\sigma_r(H_X)>0.
\]

Then the sharp lower observability constant on the orthogonal complement of the
kernel is

\[
c_X=\sigma_r(H_X).
\]

The norm of the pseudoinverse is

\[
\|H_X^\dagger\|=\frac{1}{\sigma_r(H_X)}.
\]

Thus exact rank controls whether reconstruction exists, while the smallest
nonzero singular value controls its sensitivity.

Uniformly stable reconstruction requires

\[
\inf_X\sigma_r(H_X)>0.
\]

## Smallest completion-collapse witness

Take

\[
H_N=
\begin{pmatrix}
1&0\\
0&N^{-1}
\end{pmatrix}.
\]

For every finite \(N\),

\[
\operatorname{rank}H_N=2
\]

and

\[
\det H_N=N^{-1}>0.
\]

Nevertheless,

\[
\sigma_2(H_N)=N^{-1}\longrightarrow0,
\]

and

\[
\|H_N^{-1}\|=N\longrightarrow\infty.
\]

The normalized state \(e_2=(0,1)^{\mathsf T}\) has output

\[
\|H_Ne_2\|=N^{-1}\longrightarrow0.
\]

In the limit,

\[
H_\infty=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\]

so one predictive direction becomes an exact kernel.

Every finite stage is faithful. Faithfulness does not survive completion.

## Distance to rank loss

For a finite matrix of rank \(r\), the operator-norm distance to the set of
matrices of rank at most \(r-1\) is

\[
\sigma_r(H_X).
\]

Therefore a small final singular value means that a perturbation of that size
can erase one predictive mode completely. Rank is discontinuous at the
boundary, while singular values measure distance to that boundary.

This gives a falsifiable robustness interpretation. A claimed \(r\)-state
explanation with \(\sigma_r\) below the admitted measurement or modelling error
cannot support stable reconstruction of all \(r\) directions.

## Effective rank is tolerance-relative

Given error tolerance \(\varepsilon\), define the observable effective rank as
the number of singular values exceeding \(\varepsilon\). This is an engineering
quantity, not an exact algebraic invariant.

Two reports must therefore be kept separate:

- exact rank under exact arithmetic;
- effective rank under a declared norm and tolerance.

Changing \(\varepsilon\) changes effective rank. It does not change the exact
process.

## Source normalization is mandatory

Singular values depend on the norms assigned to preparation and test
coordinates. Rescaling one source basis vector by \(N\) can make the hostile
matrix appear well-conditioned, but it also changes what counts as a normalized
state or bounded probe.

A singular-gap claim is meaningful only after freezing:

- source-state norm or topology;
- test norm and instrument budget;
- cutoff embeddings;
- coordinate weights;
- and permitted similarity transformations.

Arbitrary coordinate rescaling is not a physical repair. It moves cost into
state preparation or measurement gain.

## Similarity and balancing

Minimal linear realizations are unique up to similarity, but reachability and
observability matrices change under arbitrary similarity. A numerically poor
state coordinate system can make one side appear ill-conditioned.

The Hankel input-output operator is invariant as an abstract map between frozen
preparation and test spaces. Its singular spectrum becomes canonical only after
those spaces carry source-authorized inner products. Balanced realization can
distribute conditioning symmetrically; it cannot create a missing input-output
singular gap.

## Rank, determinant, and trace

Positive determinant at each cutoff does not give a uniform gap. In dimension
\(r\),

\[
|\det H_X|
=
\prod_{j=1}^{r}\sigma_j(H_X).
\]

One factor may collapse while all remain positive. A positive trace is still
weaker because it can remain bounded away from zero while several modes vanish.

Strict finite positivity and completion-stable coercivity are different
theorems.

## Growing state spaces

When the cutoff dimension grows, the smallest singular value of the entire map
may tend to zero simply because new weakly coupled directions are continually
added. The programme must state which claim it needs:

- uniform observation of every cutoff direction;
- uniform observation of one fixed theorem-critical subspace;
- compactness with controlled singular-value decay;
- or convergence after quotienting negligible directions.

Calling all four completion stability would hide distinct mathematical tasks.

If every normalized state must remain visible, the full lower bound is required.
If only a quotient matters, the quotient and its kernel need to be frozen before
the bound is evaluated.

## Relation to diagnostic codes

For discrete signatures, minimum Hamming distance measures separation under
coordinate faults. For linear or continuous signatures, the smallest singular
value measures local Euclidean separation of normalized state directions.

Both are margins between valid explanations:

- Hamming distance protects finite symbolic distinctions;
- a singular gap protects continuous linear reconstruction.

Neither protects against a common-mode automorphism that moves the complete
valid family onto itself. That still requires an independent reference.

## Toric-code instance

On the frozen smallest torus, exact binary syndrome and loop probes separate
the declared finite quotient. No cutoff limit is involved.

In a growing lattice or noisy analogue readout, one must additionally control
how distinguishability scales with system size. Exact commutation and homology
classes do not supply detector signal strength, measurement error rate, or a
uniform decoder margin.

The algebraic code distance and the physical readout singular gap are distinct
layers of the implementation theorem.

## Control-theory instance

An observable pair at every finite cutoff can have an observability Gramian
whose smallest eigenvalue tends to zero. The state remains theoretically
identifiable, but reconstruction energy or noise amplification diverges.

For a Hankel map, the corresponding singular value measures simultaneous
reachability and observability of a predictive mode. A mode weakly generated or
weakly measured becomes fragile even before it enters an exact kernel.

## Software instance

Two internal states may produce distinct outputs only in a rare, tiny, or
high-precision field. They are exactly distinguishable in the specification but
not robustly distinguishable under serialization loss, sampling, or operational
tolerance.

Adding a field with vanishing signal scale can preserve schema-level injectivity
while providing no stable diagnostic interface. A source-normalized error budget
is required before calling the state recoverable.

## Theta/Tate hostile instance

Finite context matrices may have full rank for every cutoff while one tail or
seam direction has singular value tending to zero. The completed scalar process
then loses the operator coordinate even though no finite kernel witness exists.

The required theorem is not merely finite Hankel rank. It is a uniform lower
bound on the theorem-critical source-normalized singular directions, compatible
with the pro-Gram topology and the asymmetric primitive and square riggings.

A cutoff-dependent renormalization that restores the gap must be charged to the
source topology and constructor norms. It cannot be introduced after observing
the collapse.

## DPC: explanation needs a margin

The conjecture is:

> A finite-rank predictive explanation is completion-stable only when its
> theorem-critical modes have a source-normalized singular gap bounded away from
> zero. Exact rank establishes distinguishability in principle; the gap
> establishes that the distinction survives bounded perturbation and completion.

This converts robust explanation into a falsifiable quantitative claim.

## Critics

### Exact mathematics does not need conditioning

Exact finite identification does not. Any claim about limits, noise, finite
precision, or physical access does. Completion can turn arbitrarily small exact
responses into a genuine kernel.

### Rescaling can always set the smallest singular value to one

Only by changing the norms or cost of source and test coordinates. Without a
frozen normalization, the numerical gap has no invariant meaning.

### Compact operators naturally have singular values tending to zero

Correct. Then uniform inversion on the full infinite-dimensional state space is
impossible. The programme must weaken the target, choose a regularized quotient,
or prove that theorem-critical states avoid the collapsing directions.

### Rank loss at the limit may be harmless

It may be harmless if the lost direction is predictively or control equivalent.
That quotient must be justified before completion, not declared after the
failure appears.

### Statistical estimation can recover small modes with more samples

It can, at increasing cost. The required sample or energy growth is part of the
implementation theorem and diverges as the gap closes.

## Exact falsifiers

- Full rank at every cutoff used to infer a faithful limit.
- Positive determinants used to infer a uniform lower bound.
- A vanishing singular mode called observable without pricing inverse
  amplification.
- Cutoff-dependent basis rescaling used as an uncharged repair.
- Singular values reported without source and test norms.
- Whole-space coercivity claimed for a compact infinite-rank observation map.
- A collapsed direction quotiented only after it falsifies the desired theorem.

## Machine-readable stability packet

```json
{
  "code": "hankel_rank_without_uniform_gap",
  "finite_rank": 2,
  "smallest_singular_value": "1/N",
  "finite_kernel": false,
  "inverse_norm": "N",
  "limit_rank": 1,
  "source_norm_frozen": true,
  "uniform_reconstruction": false,
  "cutoff_rescaling_allowed": false
}
```

## Deutschian explanation

Rank says that two predictive directions are not exactly identical. A singular
gap says they remain distinguishable when preparation, observation, and model
are imperfect. As the gap closes, the explanation depends on resolving an
ever-smaller effect and its inverse becomes ever more violent.

The limiting kernel is not a surprise appearing from nowhere. It is the endpoint
of a finite sequence of increasingly fragile distinctions. The singular value
records that approach before exact faithfulness fails.

## Claim boundary

This packet proves the finite singular-gap and perturbation statements and gives
the smallest rank-collapse family. It does not derive source norms, noise models,
or a uniform lower bound for any infinite sector.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 10/10, and expected
information gain 10/10. The target was the quantitative completion gate beyond
exact Hankel rank.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Stable predictive explanation requires a source-normalized
singular gap; exact rank alone can collapse at completion.
