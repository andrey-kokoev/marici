# Deutsch--Popperian conjecture: a criticism margin needs an authorized source metric

## Status

This packet repairs a coordinate defect in the criticism-margin proposal. A
smallest singular value is not explanatory evidence until both the source metric
and the observation metric have independent authority.

## 1. The rescaling attack

Let \(L:S\to Y\) be injective modulo gauge and define

\[
c(L)=\inf_{x\notin K}
\frac{\|Lx\|_Y}{\operatorname{dist}_S(x,K)}.
\]

Replace the source coordinate by \(x'=\alpha x\) while retaining a Euclidean
coordinate norm. The matrix becomes

\[
L'=\alpha^{-1}L
\]

and hence

\[
c(L')=|\alpha|^{-1}c(L).
\]

The reported margin can therefore be made arbitrarily good or bad without
changing any experiment. A naked singular value is presentation-dependent.

## 2. Invariant formulation

Let \(d_S\) be a metric on source classes \(\mathcal E/G\), and let \(d_Y\) be a
metric on contextual records. Define

\[
c_{S,Y}(N)
=
\inf_{[R]\neq[R']}
\frac{d_Y(N(R),N(R'))}{d_S([R],[R'])}.
\]

Under an authorized reparameterization, both the realization and the metrics
must be transported. The ratio is then invariant. Holding a coordinate norm
fixed while changing coordinates is not an authorized comparison.

Thus a criticism margin is meaningful only as a property of

\[
(N,d_S,d_Y),
\]

not of the observation matrix alone.

## 3. Sources of metric authority

Several inequivalent source metrics are legitimate, provided their roles are
declared.

### Constructor-word metric

Distance is the minimum weighted number of authorized generator changes needed
to transform one source presentation into another. This is algebraic and does
not claim physical executability.

### Actuation-cost metric

Distance is the least physical control cost of producing the source difference.
This requires an implemented actuator model and cannot be inferred from abstract
constructor syntax.

### Statistical metric

Distance is derived from local distinguishability of source distributions or
channels. Fisher, Hellinger, trace, or completely bounded metrics require their
own experiment and ancilla assumptions.

### Energy or action metric

Distance is supplied by a source-derived quadratic form. It is authoritative
only if the form and its normalization arise before the desired positivity or
observability conclusion.

These metrics answer different questions and must not be silently exchanged.

## 4. Control-theoretic factorization

For a finite linear plant, let \(W_c\) be a controllability Gramian and \(W_o\)
an observability Gramian over declared horizons. If \(x\) is reachable, its
minimum actuation energy is

\[
\|x\|_{\mathrm{act}}^2=x^*W_c^{\dagger}x.
\]

Its observed output energy is

\[
\|x\|_{\mathrm{obs}}^2=x^*W_ox.
\]

After quotienting gauge and unreachable directions, the intrinsic
actuation-to-observation margin is the smallest generalized ratio

\[
c_{mathrm{ao}}^2
=
\inf_{x\neq0}
\frac{x^*W_ox}{x^*W_c^{\dagger}x}.
\]

This ratio is invariant under state similarity when both Gramians transform
covariantly. It measures how visible a unit-cost producible difference is.

It still depends on the declared actuator and observation horizons. That
dependence is substantive, not a coordinate defect.

## 5. Budgeted criticism profile

Let \(\mathbf C_B\) contain source-authorized contexts whose cost is at most
\(B\). Define

\[
c(B)
=
\inf_{d_S([R],[R'])=1}
\sup_{c\in\mathbf C_B}
d_Y\bigl(N_c(R),N_c(R')\bigr).
\]

The function \(c(B)\) is the criticism profile. It separates three cases:

1. \(c(B)=0\) for every finite \(B\): the distinction is not finitely
   criticizable by the admitted interface;
2. \(c(B)>0\) only beyond a growing threshold: criticism exists but has a
   scaling cost;
3. \(c(B)\ge c_*>0\) at a fixed budget: robust bounded-cost criticism.

A yes-or-no full-abstraction statement forgets this resource structure.

## 6. Completion profile

For cutoffs \(N\), write \(c_N(B)\). Completion-stable criticism at budget
schedule \(B_N\) requires

\[
\inf_N c_N(B_N)>0.
\]

Different schedules express different claims:

- fixed \(B_N\) tests uniform bounded-resource criticism;
- polynomial \(B_N\) tests scalable criticism;
- unrestricted \(B_N\) tests only abstract finite distinguishability.

Reporting the schedule prevents an exponentially expensive discriminator from
being advertised as an effective explanation.

## 7. Toric-code witness

Algebraically, two noncontractible loop bits distinguish the four logical
sectors on the smallest torus. On a family of lattices, a loop probe has support
growing with the systole.

Under a constructor-word metric, the logical distinction remains simple: one
logical generator changes the class. Under a local physical actuation metric,
creating or measuring the corresponding loop can have size-dependent cost.

Therefore the same algebraic full-abstraction theorem may have different
criticism profiles under global-loop access and geometrically local access. This
is not a contradiction. It records different interfaces.

## 8. Three-lens consequence

The additive, phase, and ordered lenses carry different natural metrics.

- Additive current differences may use a norm on coefficient vectors.
- Phase differences require a circular or projective metric and a frame policy.
- Ordered holonomies require an operator or channel metric sensitive to
  noncommuting composition.

Comparing all three with one Euclidean scalar norm destroys their typing. A
small scalar residual need not mean a small ordered-operator difference.

## 9. Minimal finite falsifier

Take

\[
L=
\begin{pmatrix}
1&0\\
0&\varepsilon
\end{pmatrix}.
\]

With the Euclidean source norm, the margin is \(\varepsilon\). Introduce the
coordinate change

\[
T=
\begin{pmatrix}
1&0\\
0&\varepsilon
\end{pmatrix}.
\]

If the source norm is incorrectly reset to Euclidean after the change, the new
matrix is the identity and the margin appears to be one. If the source metric is
transported by \(T\), the intrinsic ratio is unchanged.

The first-invalid certificate contains:

- the coordinate transformation;
- the old and new observation matrices;
- the old and asserted source metrics;
- the failure to transport the metric;
- the artificial change in reported margin.

## 10. Strengthened DPC

A robust explanation must expose a criticism profile invariant under authorized
reparameterization. Its source metric, observation metric, context cost, and
completion schedule must be derived independently of the conclusion being
tested.

The explanation is not strengthened by a large coordinate-dependent singular
value. It is strengthened when a source-significant change produces a reliably
detectable consequence at a declared cost.

## 11. Critic

Resource cost belongs partly to implementation, whereas explanation can be
mathematical and nonphysical. Requiring a physical actuation metric would wrongly
deny explanatory status to abstract theories.

The repair is to maintain two profiles:

- an algebraic criticism profile based on authorized constructor complexity;
- an executable criticism profile based on implemented control and measurement
  cost.

The first supports mathematical explanation. The second supports physical
testability. Neither authorizes claims belonging to the other.

## 12. Bottom line

An observation kernel is invariant under coordinate change. A numerical margin
is not, unless its source and observation metrics transform with the model.

The programme should therefore replace unqualified smallest-eigenvalue claims by
the question:

> Relative to which source-significant change, observation geometry, authorized
> contexts, and resource schedule does this explanatory distinction remain
> visible?
