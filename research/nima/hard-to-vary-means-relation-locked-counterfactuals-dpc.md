# Deutsch--Popperian conjecture: hard to vary means relation-locked counterfactuals

## Status

This packet gives an algebraic meaning to the claim that a good explanation is
hard to vary. The key object is not a small parameter count but a web of
source-derived relations that forces changes to propagate coherently across
many experimental contexts.

## 1. Source presentation

Present the admitted constructor system by generators and relations:

\[
\mathcal M
=
\langle g_1,\ldots,g_m\mid \rho_1,\ldots,\rho_k\rangle.
\]

A realization assigns operators \(C_i\) to the generators such that

\[
\rho_j(C_1,\ldots,C_m)=0
\]

for every relation. Contextual responses are obtained by composing these same
operators and applying typed readouts.

An arbitrary lookup table assigns one value to each context independently. A
constructor realization assigns values only through the shared generators and
their relations.

## 2. Variation space

Let \(\theta\) denote a realization and let \(T_\theta\mathcal E\) be its
infinitesimal variation space. Linearizing the source relations gives

\[
D\rho_\theta(\delta\theta)=0.
\]

The admissible tangent space is

\[
Z_\theta
=
\bigcap_j\ker D\rho_{j,\theta}.
\]

Infinitesimal gauge transformations form a subspace

\[
B_\theta\subseteq Z_\theta.
\]

The genuine local explanatory variations are therefore

\[
H_\theta=Z_\theta/B_\theta.
\]

This has the familiar shape of cocycles modulo coboundaries: relation-preserving
deformations modulo changes of presentation.

## 3. Observable covariation

Let \(N\) be the experimental nerve. Its derivative induces

\[
DN_\theta:H_\theta\longrightarrow T_{N(\theta)}\mathcal Y.
\]

The image of \(DN_\theta\) is the space of observation changes that the proposed
explanation permits locally. A lookup table typically permits independent
motion in all output coordinates. A relation-locked explanation permits only a
structured subspace.

The orthogonal or algebraic annihilator of that image contains critic rows
\(q\) satisfying

\[
q\,DN_\theta=0.
\]

These rows encode forced covariations among predictions. They are testable
consequences of reusing the same constructors.

## 4. Hard-to-vary criterion

A realization is locally hard to vary relative to its source presentation and
context family when:

1. its non-gauge deformation space \(H_\theta\) is smaller than the unconstrained
   output-variation space;
2. \(DN_\theta\) is injective on the claimed explanatory directions;
3. the image of \(DN_\theta\) obeys nontrivial source-derived covariation laws;
4. violating a predicted output generally forces violation of a declared
   relation or movement along an identified explanatory modulus.

Condition 1 alone is parameter counting. Conditions 2--4 turn it into a
criticizable structural claim.

## 5. Rigidity and flexibility

Three local regimes result.

### Rigid

\[
H_\theta=0.
\]

Every sufficiently small relation-preserving change is gauge. The realization
is locally unique up to authorized presentation.

### Identifiable moduli

\[
H_\theta\neq0,
\qquad
\ker DN_\theta=0.
\]

Real explanatory alternatives exist, and the context family distinguishes them.

### Hidden moduli

\[
\ker DN_\theta\neq0.
\]

Some non-gauge explanatory variations are invisible. Full abstraction fails
locally.

Completion adds a fourth regime: approximate hidden moduli, where the smallest
nonzero singular value of the metric-typed \(DN_\theta\) tends to zero.

## 6. Why few parameters are insufficient

A false model can have one parameter. A coordinate change can inflate or shrink
parameter counts. Conversely a correct effective theory can require many
coordinates while being tightly constrained by symmetry and locality.

The invariant content lies in:

- the authorized generator family;
- the relations among its composites;
- the quotient by gauge;
- the induced subspace of allowed contextual variations;
- the smallest context that detects a transverse violation.

Hard-to-vary therefore means relation-locked, not merely concise.

## 7. One-qubit Clifford witness

Let \(H\) and \(S\) be generator images. Their composites are constrained by

\[
H^2=I,
\qquad
S^4=I,
\qquad
(HS)^3=e^{i\pi/4}I.
\]

A table may change the predicted response of \(HSH\) without changing the rows
for \(H\), \(S\), or related words. A generator realization cannot do so: a
change to \(HSH\) must arise from a change in \(H\), \(S\), the representation
law, or the phase frame, and it propagates to other words containing those
generators.

Scalar conjugation data can miss the phase relation. Controlled interference
adds a context transverse to that hidden phase direction. The additional
context does not merely confirm another table entry; it tests whether the same
generator representation governs both ordinary and controlled composition.

## 8. Toric-code witness

Star and plaquette operators are not independent syndrome-table entries. They
are built from shared edge Pauli operators and constrained by operator
commutation and global product relations.

Changing the Pauli assignment on one edge forces simultaneous changes in the
adjacent star and plaquette commutators. An arbitrary syndrome table could alter
one incidence entry alone. The source presentation forbids that isolated edit.

Likewise the anticommutation of intersecting noncontractible loops is locked to
the primal--dual intersection pairing. Altering one logical commutator without
altering the intersection representation is a transverse variation and hence a
finite falsifier of the proposed realization.

## 9. Software-architecture translation

A lookup table resembles separately mocked endpoint responses. A relation-locked
realization resembles one shared domain model whose commands, events, queries,
and projections are generated from common state-transition rules.

The architecture is explanatory when changing a domain invariant produces the
same predicted migration across every API surface. Contract tests then check
cross-endpoint covariations, not only isolated response examples.

Duplicating business rules independently in each endpoint enlarges the
variation space: one response can be patched without forcing coherent changes
elsewhere. The system becomes easier to vary and harder to explain.

## 10. Finite audit

For a finite polynomial or matrix realization:

1. list source-authorized generators and relations;
2. compute the linearized relation matrix \(D\rho_\theta\);
3. compute \(Z_\theta=\ker D\rho_\theta\);
4. compute infinitesimal gauge directions \(B_\theta\);
5. form the quotient deformation basis for \(H_\theta\);
6. compute the contextual Jacobian \(DN_\theta\);
7. report hidden moduli \(\ker DN_\theta\);
8. compute annihilator rows giving forced output covariations;
9. search for the smallest authorized context detecting each transverse
   violation;
10. audit the metric-typed smallest singular value through cutoff.

The smallest hostile witness is an output perturbation not lying in
\(\operatorname{im}DN_\theta\) that nevertheless fits all tests used during
model construction.

## 11. Strengthened DPC

A good explanation is hard to vary when its independently authorized source
generators and relations constrain a broad family of counterfactual outputs to
vary together, while admitted criticism is sensitive to every relevant
non-gauge deformation.

This combines two demands:

- generative compression through shared constructors;
- critical exposure through transverse contexts.

Compression without exposure is an elegant hidden model. Exposure without
shared constructors is a lookup table. Explanation requires both.

## 12. Critic

Relations can be manufactured after observing the data. A sufficiently baroque
presentation can encode the entire table as one generator with one enormous
relation, appearing maximally rigid.

The repair is source precedence and extension risk. Generators and relations
must be independently derived, or frozen before the contexts used to test them.
They must also govern conservative extensions not used in their construction.
Rigidity obtained only by redescribing the fitted output has no explanatory
authority.

## 13. Bottom line

The operational signature of a hard-to-vary explanation is not that it refuses
all modification. It is that every authorized modification has a structured
downstream footprint, and deviations transverse to those footprints are
detectable.

The programme should therefore ask:

> Which observable covariations are forced by reusing the same source
> constructors, and what is the smallest authorized intervention that breaks
> each covariation if the explanation is wrong?
