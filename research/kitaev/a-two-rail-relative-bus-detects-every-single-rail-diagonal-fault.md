# A two-rail relative bus detects every single-rail diagonal fault

## Bounded question

What is the smallest coherent encoding of a six-state holonomy bus for which
every diagonal phase fault confined to one physical rail has only a scalar
accepted action on the logical holonomy?

One rail is impossible. Two rails suffice through a relative-coordinate Bell
code. The repair is exact for the declared diagonal fault family and does not
measure the holonomy.

## Relative-coordinate code

Let \(G\) be a finite group of order \(N\). On two \(N\)-state rails define

\[
|h\rangle_L
=\frac1{\sqrt N}\sum_{a\in G}|a,ah\rangle,
\qquad
h\in G.
\]

The first rail carries a uniformly coherent offset. The logical group element
is the relative coordinate between the rails.

The codewords are orthonormal. Indeed,

\[
\langle h|k\rangle_L
=\frac1N\sum_a\langle a,ah|a,ak\rangle
=\delta_{h,k}.
\]

The code therefore embeds one full \(N\)-dimensional logical group register
into two physical group registers.

For \(S_3\), the physical carrier has dimension 36 and the logical bus remains
six dimensional.

## Single-rail diagonal detection

Let

\[
D_f|a\rangle=f(a)|a\rangle
\]

be an arbitrary diagonal operator on one rail. It need not be unitary.

On the first rail,

\[
\langle h|D_f\otimes I|k\rangle_L
=\delta_{h,k}\frac1N\sum_af(a).
\]

On the second rail,

\[
\langle h|I\otimes D_f|k\rangle_L
=\delta_{h,k}\frac1N\sum_af(ah)
=\delta_{h,k}\frac1N\sum_af(a).
\]

Thus

\[
P_L(D_f\otimes I)P_L
=\overline f P_L,
\]

and

\[
P_L(I\otimes D_f)P_L
=\overline f P_L,
\]

where

\[
\overline f=\frac1N\sum_af(a).
\]

Every accepted single-rail diagonal fault acts as a scalar on the complete
logical holonomy space. Its nonconstant component leaves the code and is
detectable by a coherent code-return test.

## Return test after uncompute

Prepare

\[
|e\rangle_L
=\frac1{\sqrt N}\sum_a|a,a\rangle.
\]

Compute the holonomy into the relative coordinate by applying the controlled
right multiplications only to the second rail:

\[
|a,a\rangle
\longmapsto
|a,ah\rangle.
\]

After the logical predicate phase and inverse multiplication sequence, the
ideal bus returns to \(|e\rangle_L\). Projecting coherently onto this entangled
return state detects every nonconstant diagonal fault on either rail.

For a unitary phase \(|f(a)|=1\), the acceptance amplitude is \(\overline f\)
and the acceptance probability is

\[
|\overline f|^2.
\]

Conditional on acceptance, the data action from the fault is a scalar. No
holonomy-dependent phase survives in the accepted branch.

## Faults at intermediate circuit boundaries

At an intermediate compute boundary, the second rail has label \(ap\), where
\(p\) is the partial ordered edge product. A diagonal fault there contributes

\[
f(ap).
\]

The accepted amplitude is still

\[
\frac1N\sum_af(ap)=\overline f,
\]

independent of \(p\). Right translation permutes the summation variable.

Therefore the theorem holds for a rail-only diagonal fault inserted at any
boundary between ideal controlled multiplication gates. It also holds before
or after the logical predicate because the predicate and these faults are
diagonal in the two-rail group basis.

It does not cover an arbitrary fault occurring inside a multiplication gate,
which may couple the data control and the second rail.

## Logical predicate without reading holonomy

Define the relative predicate projector

\[
Q_q
=\sum_{a\in G}|a,aq\rangle\langle a,aq|.
\]

On the logical code,

\[
Q_q|h\rangle_L=\delta_{q,h}|h\rangle_L.
\]

Hence

\[
e^{-i\theta Q_q}
\]

implements the desired logical element predicate coherently. No measurement of
\(h\) is required.

This moves the primitive phase from a one-rail basis-state predicate to a
two-rail relative-coordinate predicate. The latter is an additional physical
constructor and must be compiled; the code theorem does not make it free.

## One-rail lower bound

Suppose one \(N\)-state physical rail encodes an \(N\)-dimensional logical bus
without an extra carrier. Its code projector is the identity on the full
physical space.

For a nonconstant diagonal operator \(D_f\),

\[
P D_f P=D_f
\]

is not proportional to \(P\). Therefore no one-rail encoding of full logical
dimension can detect every nonconstant diagonal fault.

At least two physical rails are necessary. The relative-coordinate code meets
that lower bound for the declared diagonal fault family.

## Correlated two-rail faults remain logical

For a product diagonal fault on both rails,

\[
D_f\otimes D_g,
\]

the code compression is

\[
\langle h|D_f\otimes D_g|k\rangle_L
=\delta_{h,k}
\frac1N\sum_af(a)g(ah).
\]

The resulting correlation function can depend on \(h\). Such a fault may pass
the code test while applying a nontrivial logical phase.

For \(S_3\), choose

\[
f=g=\operatorname{sgn}.
\]

Then

\[
\frac16\sum_a
\operatorname{sgn}(a)\operatorname{sgn}(ah)
=\operatorname{sgn}(h).
\]

The correlated sign phase on both rails reproduces the hostile logical
holonomy phase exactly.

The two-rail code therefore requires a fault model in which one elementary
fault cannot apply a correlated diagonal operator to both rails. Physical rail
separation and separately sourced controls are part of the theorem's
implementation boundary.

## Translation and general operator faults

The code was designed for the diagonal sector left invisible by one-rail clean
return. It is not a distance-two quantum code for the full single-rail operator
algebra.

Group translations, arbitrary matrix units, leakage, and data-rail gate faults
require separate propagation and recovery analysis. Some translations move or
mix logical relative coordinates rather than leaving a purely orthogonal
syndrome.

Combining this phase code with the earlier computational-label check may cover
more operator sectors, but compositional coverage must be proved on the joint
fault span. Two separately successful checks do not automatically form a full
quantum error-correcting code.

## Relation to the one-rail Peter-Weyl obstruction

On one rail, every Peter-Weyl function of holonomy survives in the clean
branch. In the two-rail code, any such function applied to only one physical
label compresses to its uniform average.

All nontrivial irreducible matrix coefficients have zero group average. They
are therefore rejected completely by the ideal code projector. Only the
trivial representation survives acceptance.

This includes:

- the sign character;
- all four standard-representation matrix coefficients;
- both gauge-invariant harmful class-function directions;
- and the frame-sensitive diagonal directions.

The code converts the Peter-Weyl decomposition into a sharp syndrome split:
trivial representation accepted, every nontrivial single-rail diagonal sector
rejected.

## Fault-filtered constructor claim

Under the following contracts:

1. ideal preparation of \(|e\rangle_L\);
2. ideal controlled multiplication contacts outside the one declared fault;
3. at most one rail-local diagonal fault at a circuit boundary;
4. ideal relative predicate phase;
5. ideal inverse contacts;
6. coherent return projection before data output is used;

the accepted data operation equals the intended element-flux phase up to a
global scalar. Every harmful nonconstant single-rail diagonal component is
rejected.

This is a conditional one-fault detection theorem for the previously invisible
phase sector, not a complete fault-tolerant endpoint gadget.

## Exact falsifiers

- Nonorthogonal logical states \(|h\rangle_L\).
- A single-rail diagonal function whose code compression depends on \(h\).
- A nontrivial irreducible matrix coefficient with nonzero uniform average.
- A one-rail full-dimension code detecting every diagonal operator.
- The correlated two-rail sign fault claimed scalar on the code.
- Return projection performed after corrupted data has already escaped.
- The relative predicate treated as an already admitted local primitive.
- The diagonal-sector theorem claimed to cover arbitrary multiplication-gate
  faults.
- Two rails called independent without a spacetime common-cause audit.

## Machine-readable result

```json
{
  "code": "two_rail_relative_bus_diagonal_fault_detection",
  "group": "S3",
  "logical_dimension": 6,
  "physical_rails": 2,
  "physical_dimension": 36,
  "codeword": "|h>_L = 1/sqrt(6) sum_a |a,a*h>",
  "single_rail_diagonal_compression": "uniform_average_times_identity",
  "nontrivial_peter_weyl_sectors_rejected": true,
  "holonomy_measured": false,
  "one_rail_possible": false,
  "two_rail_diagonal_fault_minimum": true,
  "correlated_two_rail_faults_detected": false,
  "correlated_sign_fault_logical_action": "sign(h)",
  "translation_faults_covered": false,
  "inside_gate_faults_covered": false,
  "relative_predicate_compiled": false,
  "physical_rail_independence_required": true
}
```

## Deutschian explanation

The logical holonomy is stored as a relation between two individually
featureless labels. A phase fault on either label asks about an absolute label,
but every absolute label occurs equally often for every logical holonomy. Its
accepted effect can therefore depend only on the uniform average and cannot
distinguish logical states.

A fault touching both labels can compare them and recover the relative
coordinate. That is why the correlated sign phase becomes
\(\operatorname{sgn}(h)\). The protection comes from causal separation of the
two shares, not from redundancy alone.

## Shared Carrier geometry and quantum coefficient lens

The Carrier construction is secret-sharing-like: the operative coordinate is a
relation, while either individual share has a logical-state-independent
marginal. A one-share diagonal observation contains no logical information.

The quantum coefficient lens turns this privacy property into coherent error
detection through code compression. It rejects nontrivial Peter-Weyl sectors
without measuring the relational holonomy.

## Claim boundary

This packet proves the two-rail code, its minimum rail count for diagonal fault
detection, intermediate-boundary invariance, and the correlated-fault
obstruction. It does not compile the relative predicate, protect arbitrary
single-rail operators, handle faults inside contacts, or establish a
gauge-covariant microscopic realization.

## Process calibration

Excitement is 10/10 and confidence in the algebraic code theorem is 10/10. The
previously invisible five-dimensional clean phase sector now has a minimal
conditional repair. The next task is to determine whether the relative
predicate and controlled multiplication can be implemented without coupling
the two rails into one common-mode fault domain.
