# Closed constructor diagrams globalize in fixed dimension

## Bounded question

Does adding source-authorized constructor covariance destroy the compactness
theorem for normalized memory factorizations, or can finite constructor diagrams
also be globalized?

## Frozen constructor diagram

Fix a finite carrier dimension \(d\). Allow variables of the following types:

- density operators \(\rho_p\) for past/source labels;
- effects \(E_f\) for future/readout labels;
- completely positive trace-preserving maps \(D_g\) for authorized
  constructors;
- completely positive instrument branches when their sums are trace
  preserving;
- and finite-dimensional unitary, isometric, or stochastic maps when required
  by the source typing.

Impose equations and closed inequalities such as

\[
H_{f,p}=\operatorname{Tr}(E_f\rho_p),
\]

\[
\rho_{gp}=D_g(\rho_p),
\]

\[
D_{gh}=D_g\circ D_h,
\]

\[
E_{g^*f}=D_g^*(E_f),
\]

and the Choi positivity and trace constraints defining the admitted channels.

The label sets and constructor monoid may be infinite. The carrier dimension is
fixed.

## Compact diagram theorem

Suppose every finite subset of the declared equations and closed inequalities
has a simultaneous realization in dimension \(d\), using normalized states,
bounded effects, and source-typed finite-dimensional channels. Then the entire
constructor diagram has one global dimension-\(d\) realization.

### Proof

In fixed finite dimension:

- the density-operator space is compact;
- the effect interval \(0\leq E\leq I\) is compact;
- the Choi set of completely positive trace-preserving maps is compact;
- fixed-size instrument tuples whose sum is trace preserving are compact;
- the unitary group and fixed-size stochastic-map sets are compact.

Take the product of one appropriate compact coordinate space for every declared
state, effect, constructor, and instrument variable. Each probability,
covariance, composition, positivity, and normalization law above defines a
closed subset because finite-dimensional matrix operations are continuous.

Finite satisfiability gives the finite-intersection property. Compactness gives
a point satisfying every declared law simultaneously.

## Consequence for word coherence

It is unnecessary to choose compatible finite realizations by hand. Different
cutoffs may use different bases and channel coordinates. Compactness selects a
global compatible point provided that all overlap and composition laws were
included among the finitely satisfiable constraints.

Therefore “the finite models use incompatible gauges” is not a valid global
obstruction in the normalized fixed-dimensional closed-diagram setting. Gauge
choices are coordinates inside a compact feasibility problem.

What can fail is finite satisfiability after enough composition laws are added.
The first finite inconsistent subdiagram is then the exact obstruction packet.

## Strict invertibility is not closed

The theorem explains why finite nonvanishing is fundamentally different.
Strict positivity and invertibility are open conditions, not closed ones.

Consider one scalar variable \(x\in[0,1]\) with constraints

\[
x>0
\]

and

\[
x\leq\frac1n
\]

for every positive integer \(n\). Every finite subfamily is satisfiable by a
small positive \(x\). The full family is not: all upper bounds force \(x=0\),
contradicting strict positivity.

Replacing the open condition by one closed uniform margin

\[
x\geq\varepsilon>0
\]

makes failure visible at a finite stage. This is the exact logical reason that
finite zero-freeness does not globalize while normalized factor existence does.

## Uniform margins are closed constructors

For effects, channels, or observability Gramians, a fixed bound such as

\[
Q_N\geq\varepsilon I
\]

is a closed constraint. If every finite part of one normalized diagram admits
the same declared \(\varepsilon>0\), compactness preserves the margin globally.

If each finite part merely admits some \(\varepsilon_N>0\), with no common
value, the claim is only strict positivity and may collapse. Quantifying the
margin before the cutoff limit is therefore part of the constructor type.

## Continuity is a separate nonclosed law

Let the label space be

\[
X=\{0\}\cup\{1/n:n\geq1\}.
\]

Demand a scalar state coordinate satisfying

\[
f(0)=0,
\qquad
f(1/n)=1.
\]

Every finite restriction extends to a continuous function on \(X\), because
only finitely many isolated points are constrained. No global continuous
function satisfies all values, since \(1/n\to0\).

Continuity is not closed under arbitrary pointwise convergence. Thus product
compactness of the values does not globalize an unqualified continuity law.

A fixed modulus of continuity repairs the problem. For example, a common
Lipschitz bound

\[
\|f(x)-f(y)\|\leq Ld(x,y)
\]

is a family of closed constraints and survives compactness. More generally,
equicontinuity plus compact range supplies the relevant compact function space.

## Algebraic versus analytic constructors

The completion boundary is now sharper.

### Closed algebraic constructors

Finite-dimensional channel composition, covariance, adjunction, normalization,
positivity, finite group relations, and bounded instrument closure globalize
from finite satisfiability.

### Uniform analytic constructors

Continuity with a frozen modulus, uniform spectral margins, bounded generator
norms, and closed graph bounds can also be encoded as closed compact
constraints.

### Noncompact or open constructors

Bare nonvanishing, invertibility without an inverse bound, unbounded generators,
closability without a common graph control, dimension growth, and continuity
without equicontinuity can fail only in completion.

The first question for any proposed completion obstruction should therefore be:
is the missing property closed on a compact normalized constructor space?

## Application to ordered process models

For a fixed finite number of slots and fixed internal memory dimension, the
sets of causally normalized combs and testers are compact. Closed link-product
and marginal constraints therefore globalize exactly as above.

With indefinitely many slots, one may introduce a compatible finite comb for
each prefix and impose all marginal-consistency equations. If every finite
constraint packet has a realization inside fixed compact local dimensions, the
abstract compatible process family exists.

This does not automatically construct a single bounded operator on an infinite
tensor product or prove physical implementability with finite energy and time.
Those are additional analytic realization questions.

## Finite obstruction synthesis

When the global closed diagram does not exist, compactness guarantees that some
finite constraint subset is already inconsistent. A minimal obstruction audit
should search for a smallest unsatisfiable core containing:

- the involved state, effect, and constructor labels;
- their normalization constraints;
- the necessary composition or covariance equations;
- and the finite matrix witness of infeasibility.

This gives a precise meaning to first failure for an algebraic constructor
diagram: first relative to a declared enumeration or dependency partial order
of closed constraints.

For an open or noncompact property, no finite inconsistent core need exist. The
correct witness is then an escaping normalized sequence or collapsing margin.

## DPC: closed-law completion principle

The conjecture is:

> A purported “emergent obstruction at infinity” is explanatory only after the
> relevant source law is shown to be open, noncompact, dimension-growing, or
> otherwise outside a normalized closed constructor diagram. If the law is
> closed on a fixed compact carrier and every finite packet is satisfiable, no
> new obstruction can appear solely at completion.

This conjecture is a theorem for the finite-dimensional diagram class frozen in
this packet. Its conjectural content concerns whether a concrete source theory
has been typed into that class without omitting an essential unbounded or
topological constructor.

## Critics

### Tychonoff compactness is nonconstructive

Correct. It proves existence, not an algorithm, rate, or canonical global
gauge. Effective synthesis needs quantitative compactness or finite
presentation.

### Physical channel families may depend continuously on parameters

Correct. Pointwise channel variables globalize, but parameter continuity needs
a common modulus or another compact-function theorem.

### Infinite-time dynamics is more than compatible finite marginals

Correct. The abstract process family may lack a preferred Hilbert-space
realization, stationary generator, finite energy, or executable control law.
Those requirements must be added and classified by closedness.

## Exact falsifiers

- A claimed completion-only obstruction for a law that is closed on the frozen
  compact coordinate space and finitely satisfiable.
- A composition equation omitted from finite packets and demanded only after
  taking the limit.
- Strict positivity treated as a closed constraint without a common margin.
- Pointwise convergence presented as preservation of continuity without a
  uniform modulus.
- Unnormalized Choi or factor coordinates used to manufacture gauge escape.
- Fixed-dimensional compactness invoked while carrier dimension grows.
- An abstract compatible comb family promoted to a finite-energy physical
  implementation without an analytic realization theorem.

## Deutschian explanation

Closed finite-dimensional laws cannot fail for the first time at infinity
because every finite demand lives inside one compact possibility space and
closed laws survive its limit points. A genuine completion obstruction must
identify what can escape that space.

This turns “the limit is subtle” into a hard-to-vary diagnosis: name the open
condition, the unbounded quantity, the lost modulus, the growing carrier, or
the inconsistent overlap. If none exists, the alleged obstruction is an
artifact of coordinates or incomplete finite typing.

## Claim boundary

This packet proves a compactness theorem for fixed-dimensional normalized
constructor diagrams with closed finite-dimensional laws. It does not supply
effective synthesis or classify unbounded and infinite-dimensional source
theories.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The target was whether algebraic constructor covariance itself permits
completion escape.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Closed finite-dimensional constructor laws globalize. The true
completion frontier is now sharply confined to open conditions, noncompact
variables, lost uniform moduli, or growing carrier dimension.
