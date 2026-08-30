# Detector-relative systoles separate kernel defect from visible failure

Owner: \`marici.Kitaev\`

## Question

When does a nontrivial constructor-kernel residual become an observable
failure, and how does the answer depend on the authorized downstream tester
family?

## Claim boundary

This packet proves a finite set-theoretic and algebraic theorem for a frozen
kernel-holonomy map, word filtration, and tester family. It does not derive a
physical detector or identify mathematical distinguishability with executable
measurement.

## Frozen residual data

Let

\[
h:N\to K
\]

be the kernel-holonomy map from target relators to the invisible constructor
kernel. Let \(c:N\to[0,\infty]\) be a declared relation cost. The algebraic
implementation systole is

\[
\operatorname{sys}_{\rm alg}(h)
=
\inf\{c(r):h(r)\ne1\}.
\]

This reports the cheapest nonidentity residual, whether or not any admitted
interface can observe it.

## Detector fiber

Freeze an authorized tester family

\[
\mathcal T=\{t:K\to Y_t\}.
\]

Define the identity-indistinguishable fiber

\[
V_{\mathcal T}
=
\{k\in K:t(k)=t(1)\text{ for every }t\in\mathcal T\}.
\]

No subgroup or quotient structure is assumed. The operational systole is

\[
\operatorname{sys}_{\mathcal T}(h)
=
\inf\{c(r):h(r)\notin V_{\mathcal T}\}.
\]

It is the cheapest closed target relation whose kernel residual changes at
least one authorized readout.

Because \(1\in V_{\mathcal T}\),

\[
\operatorname{sys}_{\rm alg}(h)
\le
\operatorname{sys}_{\mathcal T}(h).
\]

The inequality can be strict or the right side can be infinite.

## Faithfulness criterion

Without an attainment assumption, the exact equality criterion is simply

\[
\inf\{c(r):h(r)\ne1\}
=
\inf\{c(r):h(r)\notin V_{\mathcal T}\}.
\]

If the algebraic infimum is attained, equality is equivalent to at least one
algebraic minimizer lying outside \(V_{\mathcal T}\). A stronger sufficient
condition, independent of attainment, is

\[
V_{\mathcal T}\cap\operatorname{im}h=\{1\}.
\]

Then the detectors are jointly faithful on every residual that can actually be
generated, and algebraic nonclosure is equivalent to observable nonclosure at
every relation, so the two infima agree.

Faithfulness on all of \(K\) is unnecessary when the relator image occupies a
smaller subset.

## Monotonicity and saturation

If \(\mathcal T\subseteq\mathcal T'\), then

\[
V_{\mathcal T'}\subseteq V_{\mathcal T}
\]

and therefore

\[
\operatorname{sys}_{\mathcal T'}(h)
\le
\operatorname{sys}_{\mathcal T}(h).
\]

Adding detectors can reveal a cheaper failure but cannot hide an already
visible one.

Adding a tester whose value is determined by the existing family does not
change \(V_{\mathcal T}\) and does not change the operational systole. This is
tester saturation rather than genuine diagnostic enrichment.

## Contextual detector closure

Let \(\mathcal C\) be the authorized downstream constructor contexts acting on
kernel residuals. The context closure is

\[
\operatorname{Ctx}_{\mathcal C}(\mathcal T)
=
\{t\circ C:t\in\mathcal T,\ C\in\mathcal C\}.
\]

Its identity fiber can be strictly smaller than the direct detector fiber. A
kernel phase invisible to an uncontrolled channel can become visible after a
controlled-use context converts it into a relative phase.

Thus visibility is not a property of \(k\in K\) alone. It is a property of the
triple

\[
(k,\mathcal T,\mathcal C).
\]

## When a quotient exists

The raw identity fiber \(V_{\mathcal T}\) need not be a subgroup. A composable
visible-kernel quotient \(K/V_{\mathcal T}\) exists only if the induced
indistinguishability relation is a congruence for multiplication and for every
authorized constructor action.

When this holds, the invisible class of the identity is a normal invariant
subgroup \(K_{\mathcal T}\), and the operational residual factors through

\[
N\overset{h}{\longrightarrow}K
\longrightarrow K/K_{\mathcal T}.
\]

Without congruence, one may still define the operational systole, but one may
not call the detector fiber a quotient kernel.

## Pauli four-group

For the Pauli lift of \(C_2\times C_2\),

\[
h(xzx^{-1}z^{-1})=-I.
\]

A conjugation-channel tester identifies \(U\) and \(-U\). Hence \(-I\) belongs
to its identity fiber and the four-letter algebraic defect is operationally
invisible.

A controlled-unitary interference tester converts the sign into a relative
control phase. Then \(-I\notin V_{\mathcal T}\), and the four-letter relation
becomes an observable failure.

The extension did not change. The tester-context packet changed.

## Toric-code analogy

Local syndrome testers have an identity fiber containing noncontractible
logical cycles. Adding two independent Wilson-loop probes makes the combined
tester family faithful on the four logical residual classes of the smallest
torus.

This is the same theorem with a different coefficient lens:

- the Carrier supplies relators, residual fibers, and context closure;
- the quantum lens supplies Pauli commutation, phase visibility, and admissible
  controlled contexts.

## Three failure reports

A compiler audit should report three distinct statements:

1. algebraic failure: \(h(r)\ne1\);
2. observable failure: \(h(r)\notin V_{\mathcal T}\);
3. correctable failure: an authorized correction sends the residual to the
   identity without violating the constructor filtration.

None implies the next.

## Deutschian explanation

A residual is not observable merely because mathematics names it. It becomes a
failure at an interface only when an authorized context maps it outside the
identity’s complete tester fiber.

The hard-to-vary explanation therefore contains both halves:

- the kernel-holonomy law says what closed compositions retain;
- the tester-context closure says which retained distinctions can affect
  records.

Changing the detector changes operational visibility, not the underlying
extension. Changing the extension changes possible residuals, not automatically
their visibility.

## Falsifiers

- A nonidentity kernel residual is called detected without an admitted tester.
- The identity tester fiber is called a subgroup without checking congruence.
- A phase-blind channel test is used to certify controlled-unitary coherence.
- A redundant saturated tester is credited with lowering the systole.
- Joint faithfulness is demanded on all of \(K\) when only
  \(\operatorname{im}h\) is reachable.
- Context closure contains an unauthorized downstream constructor.
- Observable failure is promoted to available correction.

## Disposition

The operational first failure is the detector-relative systole, not the
algebraic systole. They coincide precisely under suitable joint faithfulness on
the reachable residual image. The correct invariant packet is therefore the
constructor extension together with its authorized tester-context closure.

No checker, build, or Git operation was run for this research-only packet.
