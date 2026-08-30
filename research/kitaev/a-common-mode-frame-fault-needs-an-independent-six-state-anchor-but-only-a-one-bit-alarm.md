# A common-mode frame fault needs an independent six-state anchor but only a one-bit alarm

## Bounded question

What is the smallest gauge-invariant relation that detects a coherent
displacement of the shared six-state frame used by both noncentral
\(D(S_3)\) flux ports?

The answer separates carrier capacity from readout capacity:

- an independently sourced regular \(S_3\) anchor is necessary for universal
  exact detection;
- one invariant alarm bit detects whether the compiler and anchor disagree;
- identifying and coherently correcting the drift requires a six-valued
  syndrome that transforms by conjugation.

## Two independently transported frames

Let \(A\) be the compiler frame and \(B\) an anchor frame. Both carry the
left-regular basis \(|r\rangle\). A gauge transformation acts diagonally:

\[
|a,b\rangle\longmapsto|xa,xb\rangle.
\]

The locked code is

\[
\mathcal C_{AB}
=\operatorname{span}\{|r,r\rangle:r\in S_3\}.
\]

It carries one logical regular torsor under the diagonal action. The invariant
locked state is

\[
|\Omega\rangle
=\frac1{\sqrt6}\sum_{r\in S_3}|r,r\rangle.
\]

The physical independence requirement is not statistical independence of the
two final labels. It is separation of their preparation and transport fault
domains before the locking comparison.

## Minimal invariant alarm

Define the equality projector

\[
P_=
=\sum_{r\in S_3}|r,r\rangle\langle r,r|.
\]

It commutes with the diagonal gauge action. The binary projective measurement

\[
\{P_=,I-P_=\}
\]

asks only whether the two frames agree. It reveals no absolute orientation.

Suppose a left displacement \(L_y\) affects the compiler frame but not the
anchor. On a locked basis state,

\[
|r,r\rangle\longmapsto|yr,r\rangle.
\]

For \(y\ne e\), this state is orthogonal to \(\mathcal C_{AB}\). Therefore the
binary alarm detects every nontrivial one-frame displacement with probability
one.

If the same displacement affects both frames,

\[
|r,r\rangle\longmapsto|yr,yr\rangle,
\]

the state remains in \(\mathcal C_{AB}\). The alarm is silent. Independence of
the anchor path is therefore a causal requirement, not an algebraic property
of the final projector.

## Logical and syndrome factorization

Every pair \((a,b)\) has a unique factorization

\[
y=ab^{-1},
\qquad
r=b.
\]

Hence the two-frame carrier admits the unitary relabelling

\[
|a,b\rangle
\longleftrightarrow
|r=b\rangle_L\otimes|y=ab^{-1}\rangle_S.
\]

The logical factor stores the anchor orientation. The syndrome factor stores
the compiler displacement relative to it. The locked code is exactly the
sector \(y=e\).

Under a diagonal gauge transformation,

\[
r\longmapsto xr,
\qquad
y\longmapsto xyx^{-1}.
\]

Thus the full drift syndrome is not gauge invariant as an element label. It is
gauge covariant under conjugation. Its identity sector is invariant, which is
why the binary alarm is a valid scalar record.

This is the coefficient-lens distinction in its smallest form:

- detection needs the central predicate \(y=e\);
- diagnosis needs the conjugation-covariant element \(y\);
- coherent correction needs controlled noncommutative action using that
  covariant syndrome.

## Exact correction and the retained syndrome

The error spaces

\[
\mathcal C_y
=\operatorname{span}\{|yr,r\rangle:r\in S_3\}
\]

are mutually orthogonal and decompose the full two-frame space. A relative
left-displacement error sends \(\mathcal C_e\) to \(\mathcal C_y\) without
changing the logical coordinate \(r\) in the factorized representation.

Consequently, the error set consisting of one-frame left displacements obeys
the exact quantum error-correction orthogonality condition. A recovery may
restore the two physical frames to equal labels while retaining \(y\) in a
syndrome register or environment.

The syndrome cannot also be reset cleanly for every error history without
exporting its Gram matrix. Correction restores the logical frame relation;
replenishment of the syndrome carrier is the reset problem already isolated in
the previous packet.

Measuring only the conjugacy class of \(y\) is sufficient to classify the
gauge-invariant error type but not generally to apply the element-resolved
inverse coherently. Class diagnosis is a quotient of the recovery controller.

## Why one bit detects but cannot correct

The binary alarm distinguishes \(\mathcal C_e\) from the direct sum

\[
\bigoplus_{y\ne e}\mathcal C_y.
\]

It does not say which inverse displacement is required. There are five
nontrivial error sectors. A classical invariant readout can refine them only to
the transposition and three-cycle classes without an additional frame.

Coherent correction avoids selecting an absolute element by retaining the
syndrome as a transforming quantum register. The correction constructor is
gauge covariant as a whole even though its internal control is element
resolved.

Therefore:

- one bit is the minimum readout for detection;
- a six-dimensional covariant syndrome is the natural exact recovery carrier;
- no invariant scalar encoding of fewer element labels automatically supplies
  the same coherent recovery operation.

## Anchor-size minimum

Consider a transitive anchor \(S_3/K\) rather than the full regular torsor.
Lock it equivariantly to the compiler frame by associating \(r\) with the coset
\(rK\).

After a compiler displacement \(L_y\), the equality relation fails to detect
the fault on orientation \(r\) precisely when

\[
yrK=rK,
\]

or equivalently

\[
r^{-1}yr\in K.
\]

If \(K\) contains any nonidentity element \(k\), choose \(y=k\) and \(r=e\).
That nontrivial displacement is invisible on at least one valid orientation.
Universal deterministic detection for every nontrivial \(y\) and every
orientation therefore forces

\[
K=\{e\}.
\]

The anchor must be the regular six-state torsor.

This is the same centralizer-intersection minimum obtained for jointly
resolving one transposition and one three-cycle. The two ports require a
faithful shared orientation; auditing every displacement of that orientation
requires an equally faithful independent anchor.

## Port-relative weakening

If the admitted compiler uses only a restricted port family, universal
orientation detection may be stronger than necessary. A drift is operationally
irrelevant when it fixes every admitted port.

For port elements \(q_1,\ldots,q_m\), the invisible stabilizer is

\[
K_{\mathrm{port}}
=\bigcap_j C_{S_3}(q_j).
\]

An anchor need only distinguish the quotient by this stabilizer. For one
transposition port, three orientations suffice. For one three-cycle port, two
suffice. For the pair that generates the full endpoint algebra, the
intersection is trivial and six are necessary.

The minimum is therefore relative to the declared executable constructor
family, not to every imaginable group label.

## Interaction with the relational flux compiler

The anchor should not be used as an untyped replacement control frame during a
pulse. Its role is to cross-check the compiler frame across an independently
sourced cut.

A complete pulse cycle must specify:

1. preparation or transport of the compiler and anchor frames;
2. locking or comparison before the pulse;
3. use of the compiler frame in the relational flux constructor;
4. comparison after the pulse;
5. coherent recovery or rejection conditioned on the syndrome;
6. disposition of the retained syndrome and consumed frame record.

If the same interaction or wire can displace both frames before both checks,
the proposed anchor has not crossed the relevant fault cut.

## Exact falsifiers

- A one-frame internal check claimed to detect its own global orientation
  displacement.
- The equality alarm claimed to identify the full displacement element.
- A class-valued scalar syndrome claimed sufficient for arbitrary
  element-resolved coherent correction.
- A quotient anchor \(S_3/K\) with nontrivial \(K\) claimed to detect every
  nontrivial displacement on every orientation.
- Two frames copied from one source called independent fault references.
- A common displacement of compiler and anchor claimed detectable by their
  equality relation.
- Syndrome reset claimed free after exact recovery.
- A six-state anchor demanded for a restricted port family whose joint
  stabilizer is nontrivial.

## Machine-readable result

```json
{
  "code": "independent_frame_anchor_minimum",
  "group": "S3",
  "full_two_port_constructor_family": ["transposition", "three_cycle"],
  "joint_port_stabilizer_order": 1,
  "minimum_anchor_dimension": 6,
  "minimum_detection_readout_outcomes": 2,
  "equality_alarm_gauge_invariant": true,
  "single_frame_displacement_detected": true,
  "joint_common_mode_displacement_detected": false,
  "full_syndrome_dimension": 6,
  "full_syndrome_transformation": "conjugation",
  "full_syndrome_scalar_invariant": false,
  "relative_displacement_errors_exactly_correctable": true,
  "syndrome_reset_free": false,
  "physical_path_independence_required": true
}
```

## Deutschian explanation

To discover that a compass moved, one needs another compass whose history did
not share the movement. The comparison “same or different” is invariant and
requires only one alarm bit. But undoing the movement requires knowing how the
compass moved, and that information itself has an orientation-dependent
transformation law.

The six-state anchor is not needed because the alarm contains six values. It is
needed because a smaller anchor has a nontrivial stabilizer: some real movement
leaves some anchor orientation unchanged. Carrier capacity and displayed
readout capacity answer different questions.

The final common mode is causal rather than algebraic. If compiler and anchor
share the same fault history, no comparison performed afterward can reconstruct
the counterfactual orientation they would have had without that fault.

## Shared Carrier geometry and quantum coefficient lens

The shared Carrier theorem is that universal common-mode detection requires a
cut-crossing reference whose stabilizer excludes every operationally relevant
drift. The alarm can be a small quotient even when the reference carrier is
large.

The quantum coefficient lens adds a coherent logical-syndrome factorization,
orthogonal error sectors, covariant quantum syndrome transport, and recovery
without measuring an absolute gauge element. An additive scalar lens sees the
alarm and conjugacy class but cannot by itself implement the ordered inverse.

## Claim boundary

This packet proves the binary equality detector, the logical-syndrome
factorization, exact correction of one-frame left-displacement errors with a
retained syndrome, and the regular-anchor minimum for universal detection. It
does not prove physical independence of any proposed anchor path, synthesize a
local recovery circuit, protect against arbitrary quantum noise, or construct
the full fault-tolerant endpoint compiler.

## Process calibration

Excitement is 10/10 and confidence in the finite algebra is 10/10. The result
locates the smallest audit interface beneath full two-port control: six states
of independent carrier capacity, one bit of invariant alarm capacity, and six
covariant syndrome sectors for exact recovery. The next step is to require a
spacetime fault model and decide when the anchor path genuinely crosses the
compiler frame's common-cause cut.
