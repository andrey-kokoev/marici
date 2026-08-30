# Absent-transition trichotomy and constructor closure

## Explanatory problem

When an endpoint record reports no transition, three explanations are possible:

1. the transition packet exists but the readout erases it;
2. the present constructor word has zero transition, but another authorized
   route has nonzero transition;
3. every authorized route has zero transition.

This packet makes the alternatives mutually exclusive, gives a finite decision
procedure, and states what an inserted context can and cannot prove.

## Frozen typed model

Let \(S\) be a finite-dimensional state space. Let \(P_A\) and \(P_B\) select
the declared source and target sectors. Let \(\mathcal G\) be a finite family of
authorized constructors, and let \(\mathcal M=\langle\mathcal G\rangle\) be the
monoid of typed constructor words they generate.

For a word \(w\in\mathcal M\) with operator \(T_w\), define its complete
source-to-target transition packet by

\[
X_w=P_BT_wP_A.
\]

Let

\[
\ell:V\longrightarrow Y
\]

be the declared endpoint readout on the transition-packet space \(V\). The
reported record is

\[
r_w=\ell(X_w).
\]

The current route is a frozen word \(w_0\). The problem begins when

\[
r_{w_0}=0.
\]

## Exact trichotomy

Assume \(X_w\), \(\ell\), and the authorized monoid \(\mathcal M\) are all
typed. Exactly one of the following holds.

### Readout-hidden transition

\[
X_{w_0}\neq0,
\qquad
\ell(X_{w_0})=0.
\]

The current route carries nonzero transition data in the kernel of the endpoint
readout. A richer observation of the same completed word can reveal it without
claiming that a new route existed beforehand.

### Route-deficient transition

\[
X_{w_0}=0,
\qquad
X_w\neq0
\]

for at least one authorized word \(w\in\mathcal M\). The present route is
genuinely zero, but the source and target are connected by another admitted
constructor factorization.

### Constructor-relative prohibition

\[
X_w=0
\]

for every \(w\in\mathcal M\). No route built from the authorized constructors
connects the declared sectors.

These cases are mutually exclusive because they first decide whether the
current complete packet is nonzero and then, only when it is zero, decide
whether any alternative authorized word is nonzero.

## The unresolved status

The trichotomy is not available when any of the following is missing:

- a complete transition packet finer than the endpoint record;
- a typed readout map;
- a frozen constructor family;
- a completeness theorem for its finite closure;
- the source and target sector maps.

In that situation the correct status is unresolved, not prohibited. Failure to
find a route is not a selection rule.

## Finite constructor-closure decision theorem

Let \(\mathcal A\subseteq\operatorname{End}(S)\) be the unital algebra generated
by \(\mathcal G\). In finite dimension, construct it iteratively:

\[
\mathcal A_0=\operatorname{span}\{I\},
\]

and

\[
\mathcal A_{k+1}
=
\operatorname{span}
\left(
\mathcal A_k
\cup
\{GA:G\in\mathcal G,\ A\in\mathcal A_k\}
\right).
\]

The ascending chain stabilizes after at most \((\dim S)^2\) dimension increases.
At stabilization it equals \(\mathcal A\).

Define the reachable transition space

\[
\mathcal R_{B\leftarrow A}
=
P_B\mathcal A P_A.
\]

Then constructor-relative prohibition holds exactly when

\[
\mathcal R_{B\leftarrow A}=0.
\]

If this space is nonzero while \(X_{w_0}=0\), the current route is deficient.
A breadth-first word search inside the growing algebra can provide a shortest
nonzero witness word.

This is a finite completeness theorem for linear constructor closure. It is not
a theorem about constructors omitted from \(\mathcal G\).

## Symmetry certificate for prohibition

A source-derived conserved grading can prove prohibition without enumerating
every word. Suppose

\[
S=\bigoplus_q S_q
\]

and every authorized constructor preserves the grading. If \(P_A\) and \(P_B\)
select different grades, then

\[
P_B\mathcal A P_A=0.
\]

This is a hard-to-vary explanation: the same invariant excludes every composite
word, not merely the observed one.

Adding a constructor that changes the grade does not reveal a hidden violation
of the old rule. It enlarges the constructor family and invalidates the old
prohibition hypothesis outside its declared scope.

## Observation versus insertion

Two experimental extensions must be typed separately.

An observational extension applies a new readout \(q\) to the same packet:

\[
q(X_{w_0}).
\]

It diagnoses readout blindness when

\[
\ell(X_{w_0})=0,
\qquad
q(X_{w_0})\neq0.
\]

A constructive extension replaces the word by a different word \(w\):

\[
X_{w_0}\longmapsto X_w.
\]

It diagnoses route deficiency when

\[
X_{w_0}=0,
\qquad
X_w\neq0.
\]

Confusing these operations produces the false statement that an inserted
constructor revealed a transition already present in the original word.

## Minimal readout repair

If \(X_{w_0}\neq0\) lies in \(\ker\ell\), one added linear probe \(q\) can detect
that particular packet whenever

\[
q(X_{w_0})\neq0.
\]

To repair the entire readout rather than one witness, the combined map

\[
(\ell,q):V\longrightarrow Y\oplus Z
\]

must be injective on the claimed quotient. Equivalently,

\[
q|_{\ker\ell}
\]

must be injective after authorized gauge is removed.

A witness-sensitive row is not automatically a jointly faithful interface.

## Operational replacement for direct packet access

Direct inspection of \(X_{w_0}\) is unnecessary when a frozen observation
family

\[
Q=(q_1,\ldots,q_m):V/G\longrightarrow Z
\]

is proved jointly faithful on the authorized quotient. Then

\[
Q(X_{w_0})=0
\]

implies that \(X_{w_0}\) is zero modulo authorized gauge.

The operational decision protocol becomes:

1. apply the jointly faithful observational family to the unchanged word;
2. if some component is nonzero while the original endpoint record is zero,
   classify the transition as readout-hidden;
3. if the complete observation family vanishes, search the authorized
   constructor closure for another nonzero word;
4. classify success as route deficiency and complete closure failure as
   constructor-relative prohibition.

Without joint faithfulness, silence of every available probe leaves hidden
versus zero unresolved. Adding constructor words before settling this question
can demonstrate reachability but cannot retrospectively classify the original
word.

## Minimal route repair

If the current word is zero but \(\mathcal R_{B\leftarrow A}\neq0\), define

\[
d_{\mathcal G}(A,B)
=
\min\{|w|:P_BT_wP_A\neq0\}.
\]

This constructor distance is the minimum authorized word length opening the
transition. It is algebraic and does not include physical loss, time, locality,
or fault cost unless those weights are supplied independently.

A weighted version replaces word length with a source-authorized constructor
cost. The least-cost nonzero word is then the minimal route repair.

## Robust classification

Exact nonzero transition can be operationally negligible. Given authorized
norms and a resource budget \(B\), define

\[
\Gamma(B)
=
\sup_{w:\operatorname{cost}(w)\le B}
\|P_BT_wP_A\|.
\]

The sectors are algebraically connected when \(\Gamma(B)>0\) for some finite
\(B\). They are robustly connected over a regime when an independently declared
lower bound survives the relevant cutoff, noise, and completion limits.

Thus a nonzero postselected amplitude proves route existence but not reliable
capability. Constructor-relative prohibition, algebraic reachability, robust
reachability, and executable control are different strengths.

## Polarizer classification

Take

\[
P_A=P_0,
\qquad
P_B=P_{\pi/2}.
\]

For the direct word,

\[
X_{w_0}=P_{\pi/2}P_0=0.
\]

Therefore the extinguished direct transition is not readout-hidden in the ideal
Jones model.

If the only allowed intermediate projectors are \(P_0\) and \(P_{\pi/2}\), every
word changing between the two rays contains an orthogonal adjacent pair. The
transition is prohibited relative to that restricted constructor family.

Once an intermediate \(P_\theta\) with

\[
0<\theta<\frac{\pi}{2}
\]

is authorized,

\[
P_{\pi/2}P_\theta P_0\neq0.
\]

The enlarged family reclassifies the endpoint pair as route-connected. The
third polarizer constructs the witness route; it does not reveal a nonzero
direct packet.

With fixed insertion survival \(\eta<1\), arbitrarily refined routes remain
algebraically nonzero but lose robust transmission. This separates route
existence from executable route quality.

## Toric-code classification

Local syndrome is a compressed readout. Two Pauli errors in different logical
homology classes can have the same syndrome while remaining distinct complete
error classes. This is readout-hidden information, repaired by noncontractible
loop probes.

By contrast, changing one logical sector to another requires an admitted logical
operator or decoder actuation. A readout probe can identify the sector but does
not create the repair route. Syndrome observability and decoder reachability are
therefore different sides of the trichotomy.

## Ordered-operator classification

A central trace can vanish on a nonzero operator packet. A noncentral endpoint
probe can detect the same operator word, so the transition was readout-hidden.

If the operator packet itself is zero for the current product but becomes
nonzero after inserting another noncommuting factor, the route was deficient.
Scalar zero alone cannot distinguish these cases because it does not determine
the complete operator packet.

## Smallest exact witness suite

All three cases occur in two-dimensional real or complex linear algebra.

### Hidden witness

Take \(V=M_2(\mathbf C)\), endpoint readout \(\ell(X)=\operatorname{tr}X\), and

\[
X_{w_0}=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Then \(X_{w_0}\neq0\) while \(\ell(X_{w_0})=0\). The additional row

\[
q(X)=X_{11}-X_{22}
\]

returns two. The word was hidden by central scalar cancellation.

### Route-deficient witness

Take \(P_A=P_0\), \(P_B=P_{\pi/2}\), and current word

\[
X_{w_0}=P_BP_A=0.
\]

After authorizing \(P_{\pi/4}\),

\[
P_BP_{\pi/4}P_A\neq0.
\]

The original packet remains zero; a new route exists.

### Prohibition witness

Take \(P_A=|0\rangle\langle0|\), \(P_B=|1\rangle\langle1|\), and let every
authorized generator be diagonal in this basis. Their entire generated algebra
is diagonal, so

\[
P_B\mathcal A P_A=0.
\]

The grading by basis sector is the finite prohibition certificate.

## Software-system translation

An endpoint returning no record can mean:

- the domain event occurred but the projection or query omitted it;
- the current workflow never emitted the event, though another authorized
  command sequence would;
- a domain invariant forbids every authorized command sequence from emitting
  it.

Adding logging tests the first possibility. Adding a workflow step tests the
second. Proving an invariant addresses the third. More logging cannot repair a
missing workflow route, and a new command cannot prove that the old event was
hidden.

## Deutschian explanation

The explanation is not the label attached after observing zero. It is the
source-derived structure that predicts how the zero responds to two independent
classes of criticism:

1. change the readout while preserving the constructor word;
2. change the constructor word while preserving the declared endpoints and
   composition law.

A readout-hidden explanation predicts that the first class can expose a
nonzero packet. A route-deficient explanation predicts that only the second
class can produce a nonzero packet. A prohibition explanation supplies an
invariant or complete closure theorem predicting failure of every authorized
constructor word.

The alternatives are hard to vary because they make incompatible
counterfactual predictions before the discriminating context is applied.

## Critics

### Intervention changes the plant

Correct. That is why constructive insertion cannot diagnose hidden content of
the old word. It diagnoses reachability in the enlarged constructor family.

### A nonzero route can be postselection artefact

Nonzero conditional amplitude proves only algebraic route existence. Overall
success probability and deterministic control require separate typing.

### The constructor family can be chosen to force the answer

Correct. Prohibition is always relative to an independently authorized family.
Adding or excluding a constructor after seeing the result is a problem shift
unless the source enlargement was frozen beforehand.

### Noise removes exact zeros

Then the exact trichotomy must be replaced by normed margins and model
comparison. A small scalar record cannot distinguish a small packet from a large
packet nearly annihilated by the readout.

### Complete internal packets may be inaccessible

Then hidden versus route-deficient remains unresolved. A theoretical state
variable does not become observed merely because the model names it.

## Finite decision protocol

Given a zero endpoint record:

1. freeze \(P_A\), \(P_B\), the current word, the complete packet type, the
   readout, and the authorized constructor generators;
2. determine whether the current complete packet is zero;
3. if it is nonzero, compute the readout kernel and synthesize a source-authorized
   separating probe;
4. if it is zero, compute the finite constructor algebra and
   \(P_B\mathcal A P_A\);
5. if that space is nonzero, extract a shortest or least-cost witness word;
6. if it is zero, identify the invariant or closure certificate proving
   constructor-relative prohibition;
7. repeat with norms, costs, noise, and completion only after the algebraic type
   is settled;
8. report unresolved whenever the packet, closure, or authority is incomplete.

## Exact falsifiers

- A nonzero complete packet with zero endpoint record falsifies a route-deficient
  classification of the current word.
- A nonzero authorized word falsifies constructor-relative prohibition.
- A complete zero constructor closure falsifies route deficiency.
- An inserted-word success does not falsify the claim that the original word is
  zero.
- An alternative readout success on the same word does not prove an alternative
  constructor route.
- A bounded search without a closure theorem cannot certify prohibition.
- A route whose success margin collapses cannot certify robust capability.

## Claim boundary

This is a finite linear constructor theorem and a source-typed explanatory
protocol. It does not assert that every physical sector admits a complete linear
packet, a finitely generated constructor algebra, nondisturbing alternate
readouts, or executable access to every algebraic word.

## Process calibration

Pre-objective: excitement 10/10, confidence 8.5/10, expected information gain
10/10. The target was a hard-to-vary decision theory separating invariant
prohibition, readout blindness, and route deficiency. The main confound was the
plant-changing character of insertion.

Mid-objective: excitement 10/10, confidence 9.5/10, expected information gain
remains 10/10. The trichotomy is exact after adding the unresolved status and
typing observational extensions separately from constructive extensions.
