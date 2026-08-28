# Record-conditioned correction requires a common compensator on every tester fiber

Owner: \`marici.Kitaev\`

## Question

What exact condition upgrades observable constructor nonclosure to an
authorized decoder that repairs every reachable residual?

## Claim boundary

This is a finite algebraic decoder theorem. It does not derive physical
corrections, noise models, or fault-tolerant execution.

## Frozen data

Let \(H\subseteq K\) be the reachable kernel residuals. Let

\[
T:H\to Y
\]

be the complete authorized record map, including every admitted detector
context. Let \(\mathcal C\) be the authorized correction words with evaluation

\[
\gamma:\mathcal C\to K.
\]

Corrections act on residuals by left multiplication. Exact repair means return
to the physical identity.

A record-conditioned decoder is a map

\[
D:Y\to\mathcal C.
\]

It succeeds exactly when

\[
\gamma(D(T(k)))\,k=1
\]

for every \(k\in H\).

## Common-compensator theorem

A successful decoder exists if and only if every nonempty record fiber

\[
H_y=\{k\in H:T(k)=y\}
\]

admits one authorized correction \(a_y\in\gamma(\mathcal C)\) satisfying

\[
a_yk=1
\]

for every \(k\in H_y\).

The proof is direct. A decoder supplies the common correction
\(a_y=\gamma(D(y))\). Conversely, choosing one common correction for each
nonempty fiber defines a decoder.

Because left inverses in a group are unique, exact repair to the identity
forces every correctable fiber to be a singleton:

\[
a_yk_1=a_yk_2=1
\quad\Longrightarrow\quad
k_1=k_2.
\]

Therefore exact record-conditioned repair requires both:

1. \(T\) is injective on \(H\);
2. every inverse \(k^{-1}\) lies in the authorized correction image.

These conditions are also sufficient.

## Alarm visibility is weaker

The detector-relative systole only asks whether a residual leaves the identity
fiber. A binary alarm can distinguish \(1\) from every nonidentity residual
while merging all nonidentity residuals into one record.

Such an alarm detects failure perfectly but cannot select a correction when
\(H\) contains two distinct nonidentity elements. This is the minimal
observable-but-undecodable hostile.

Take

\[
H=\{1,a,b\},
\qquad
a\ne b,
\]

and define \(T(1)=0\), \(T(a)=T(b)=1\). Assume both inverses are individually
authorized. The alarm is faithful for identity detection, but one correction
chosen at record \(1\) cannot invert both \(a\) and \(b\).

## Repair modulo a safe subgroup

Sometimes repair need only return the residual to a declared safe normal
subgroup \(S\trianglelefteq K\), not to the identity. Success becomes

\[
\gamma(D(T(k)))\,k\in S.
\]

A decoder exists exactly when every record fiber admits one common correction
sending the whole fiber into \(S\).

If all authorized corrections are available inside \(K\), this is equivalent
to each tester fiber lying in one right coset of \(S\):

\[
k_1k_2^{-1}\in S
\]

for all \(k_1,k_2\) with \(T(k_1)=T(k_2)\).

Thus the tester equivalence must refine the safe-coset equivalence. Exact repair
is the special case \(S=\{1\}\).

## Correction cost and uniformity

Let \(d_{\mathcal C}(a)\) be the least authorized implementation cost of a
correction evaluating to \(a\). For each fiber define

\[
\rho(y)
=
\inf\left\{
d_{\mathcal C}(a):
ak\in S\text{ for every }k\in H_y
\right\}.
\]

The decoder is pointwise available when every \(\rho(y)\) is finite. It is
uniformly bounded when

\[
\sup_{y\in T(H)}\rho(y)<\infty.
\]

As before, an infinite supremum statement needs care: arbitrarily expensive
finite corrections do not supply a uniform decoder, and an unattained infimum
does not supply an exact correcting word.

## Toric-code instance

Local syndrome identifies endpoints of an error chain but merges chains that
differ by noncontractible logical cycles. These errors occupy one syndrome
fiber but require corrections differing by logical operators.

Hence syndrome is an alarm and a local-defect coordinate, not a complete
decoder coordinate. Adding two independent noncontractible loop records makes
the smallest-torus residual map injective modulo stabilizers. Only then can a
record-conditioned logical repair be selected, assuming the corresponding
corrections are authorized.

This restates the established result:

\[
\text{syndrome detection}
\ne
\text{logical classification}
\ne
\text{physical recovery}.
\]

## Controller-redundancy instance

Two replicated command bits plus equality comparison detect one differential
flip, but the mismatch record does not identify which copy is wrong. The record
fiber contains two distinct faults requiring opposite corrections.

Three copies plus majority refine the record sufficiently to choose the
single-fault correction under the independent-flip model. Common-mode flips
remain in the identity record fiber and cannot be corrected from replica data.

Thus detection, localization, and correction correspond to progressively finer
tester fibers.

## SCC verdicts

The SCC gate should return three separately typed verdicts:

- algebraic closure: every reachable relation residual is the identity;
- observable closure: every nonidentity residual is separated from the identity
  by the authorized context-closed tester family;
- correctable closure: every complete record fiber admits one authorized common
  compensator into the declared safe subgroup, with the required cost bound.

The correctable verdict must include a fiber witness, correction constructor,
safe subgroup, and uniformity status. A single boolean alarm is insufficient.

## Deutschian explanation

Correction is not caused by knowing that something went wrong. It is possible
only when the record rules out every residual requiring an incompatible
response.

The hard-to-vary explanation is fiberwise: all states producing one record must
share one lawful compensator. If two incompatible residuals remain in the same
fiber, no decoder cleverness can repair both; new information or a coarser
repair target is required.

## Falsifiers

- Identity detection is promoted to residual identification.
- Every residual has an inverse, but no record-conditioned selection exists.
- Two residuals in one record fiber require different corrections.
- Repair modulo \(S\) is claimed although a fiber crosses two right cosets.
- Correction words exist only outside the authorized constructor family.
- Pointwise finite correction cost is promoted to a uniform bound.
- A majority decoder is claimed against common-mode faults.

## Disposition

Observable nonclosure upgrades to correctable closure exactly when each complete
tester fiber admits one common authorized compensator into the declared safe
subgroup. For exact repair, this reduces to injective residual readout plus
authorized inverses.

No checker, build, or Git operation was run for this research-only packet.
