# Projective density plus geometric injection gives a polylog compiler but not a raw-noise threshold

Owner: `marici.Kitaev`

## Bounded question

What quantitative compiler follows from the fixed projectively universal
qutrit gate set, and how does its logical word length compose with the
repeat-until-success implementation of the sixth-root vacuum-edge gate?

The standard Solovay--Kitaev theorem applies after passing to a finite
inverse-closed generating set for the determinant kernel, or equivalently
working directly in `PU(3)`. Any target projective qutrit gate has an
`epsilon` approximation of polylogarithmic word length.

Each injected edge gate succeeds independently in the ideal branch model with
probability `3/4`. A logical word containing `N_Q` such gates has expected
injection-attempt count `4 N_Q/3`. Capping each injection at `n` attempts gives
heralded-abort probability at most `N_Q 4^{-n}`.

These are compiler and stopping-time theorems. They do not yield a raw-noise
threshold. Without encoded correction, physical branch error accumulates at
least through a word-length budget and must shrink with target accuracy.

## Claim boundary

The Solovay--Kitaev conclusion is conditional on the exact projective-density
theorem, a finite inverse-closed logical alphabet, and a fixed coarse net or
equivalent base compiler. The traditional construction gives word length of
order `log(1/epsilon)` to a constant power; newer algorithms improve the
exponent.

The retry calculation assumes the ideal `3/4` success probability on every
attempt, exact restoration after a failure, and fresh branch conditions.
Correlated physical faults can violate those assumptions even when the ideal
outcome probabilities remain correct.

## Finite inverse-closed alphabet

Let `G` contain:

- the two electric braid transpositions;
- the fixed gate
  \[
  Q_A=e^{i\pi P_A/3};
  \]
- their exact inverses.

The braid generators have finite order, and

\[
Q_A^{-1}=Q_A^5.
\]

Thus `G` is finite and inverse closed. The preceding theorem proves that its
projective image is dense in `PU(3)`.

The determinant image is the finite group of sixth roots. If one wants to
invoke a theorem stated only for `SU(3)`, take the kernel of the determinant
map. It has finite index in the generated group and admits a finite
inverse-closed Schreier generating set. Its closure is `SU(3)`.

Projective compilation and determinant-kernel compilation therefore encode
the same physical qutrit targets up to global phase.

## Solovay--Kitaev consequence

Fix a projective operator metric and a sufficiently fine constant-accuracy
base net. There are constants `C`, `c`, and `epsilon_0`, depending on the
generator set and the chosen compilation scheme, such that every target
projective qutrit gate `U` and every positive `epsilon` below `epsilon_0` admit
a word `w` with

\[
d_{\rm proj}(w,U)\leq\epsilon
\]

and

\[
L(w)
\leq
C\log^c\!\left(\frac1\epsilon\right).
\]

The traditional Dawson--Nielsen recursion gives an exponent near `3.97` and
extends to `SU(d)`. Modern variants give smaller exponents. The qualitative
Marici conclusion needs only that `c` is finite.

Primary references include:

- Christopher M. Dawson and Michael A. Nielsen, *The Solovay-Kitaev
  algorithm*, https://arxiv.org/abs/quant-ph/0505030;
- Greg Kuperberg, *Breaking the cubic barrier in the Solovay-Kitaev
  algorithm*, https://arxiv.org/abs/2306.13158.

The theorem replaces the earlier unquantified statement that dense words
exist with a constructive polylogarithmic length guarantee.

## Coarse-net authority

Solovay--Kitaev recursion does not create its initial constant-accuracy net.
For a fixed finite-dimensional compact group, density and compactness ensure
that some finite base net exists. An executable compiler must still provide
one of:

- an enumerated and verified base dictionary;
- a search algorithm with a proved covering radius;
- another source-authorized coarse compiler.

The base-net cost is constant with respect to final accuracy but may be large
and cannot be erased from implementation claims.

## Logical word composition

Let a compiled word have total logical length

\[
L=L_B+N_Q,
\]

where `L_B` counts deterministic electric braid gates and `N_Q` counts
injected sixth-root edge gates, including braid conjugates.

The logical approximation theorem bounds `L`. The physical execution cost
must additionally expand each `Q` symbol into its measurement-assisted retry
gadget.

## Exact retry distribution

For one ideal injected gate, let `T` be the number of attempts through the
first success. Then

\[
\Pr(T=t)
=
\left(\frac14\right)^{t-1}
\frac34,
\qquad
t=1,2,\ldots.
\]

Therefore

\[
\mathbb E[T]=\frac43
\]

and

\[
\mathbb E[T-1]=\frac13.
\]

The second number is the expected count of failed attempts and inverse
cube-root restorations per successfully injected edge gate.

For a word with `N_Q` injections, linearity of expectation gives

\[
\mathbb E[T_{\rm total}]
=
\frac{4N_Q}{3}
\]

and expected failure-correction count

\[
\frac{N_Q}{3}.
\]

Independence is unnecessary for these expectation identities if every
conditional attempt retains the same success probability. It is required for
the simple product distribution and stronger concentration claims.

## Bounded runtime with a heralded abort

Cap each injected gate at `n` attempts. For one gate, the probability that all
`n` attempts fail is

\[
4^{-n}.
\]

A union bound over `N_Q` injections gives

\[
p_{\rm abort}
\leq
N_Q4^{-n}.
\]

To make this at most a declared `delta`, it suffices to choose

\[
n
\geq
\left\lceil
\log_4\!\left(\frac{N_Q}{\delta}\right)
\right\rceil.
\]

The total attempted-injection count is then at most `N_Q n` before a completed
run or a heralded abort. The abort record must remain explicit. Discarding it
and renormalizing silently changes the implemented channel.

## Overall ideal resource scaling

Combining Solovay--Kitaev word length with the attempt cap gives a deterministic
resource envelope, excluding a flagged abort, of order

\[
\log^c\!\left(\frac1\epsilon\right)
\left[
1+
\log\!\left(
\frac{\log(1/\epsilon)}{\delta}
\right)
\right].
\]

The inner logarithm absorbs fixed powers and generator fractions. This bound
is intentionally coarse. It proves polylogarithmic dependence on synthesis
accuracy and logarithmic dependence on the inverse abort probability.

Expected physical attempts omit the extra retry logarithm and remain a
constant factor above the number of injected symbols.

## Raw physical-error budget

Let `M` be the number of elementary physical locations actually executed in a
nonaborted run. Suppose each location differs from its ideal channel by at
most `eta` in diamond distance, with no active fault-tolerant suppression.
Telescoping gives only

\[
\epsilon_{\rm phys}
\leq
M\eta.
\]

If the logical synthesis error is `epsilon_syn`, the conditional completed-run
error obeys the coarse budget

\[
\epsilon_{\rm total}
\leq
\epsilon_{\rm syn}+M\eta,
\]

with the heralded abort probability reported separately.

Therefore fixed raw error `eta` does not support arbitrarily accurate and long
computation under this bound. To maintain a target physical contribution
`epsilon_phys`, one needs

\[
\eta
\lesssim
\frac{\epsilon_{\rm phys}}{M}.
\]

Polylogarithmic word length softens this requirement but does not turn it into
a threshold theorem.

## Conditional encoded scaling

Suppose an independently proved fault-tolerant gadget family provides logical
error per compiled symbol

\[
\eta_L(d)
\leq
A e^{-\alpha d}
\]

for physical error below a declared threshold and code-distance parameter
`d`. To keep the total logical physical error below `epsilon_phys`, it suffices
to choose

\[
d
\geq
\frac1\alpha
\log\!\left(
\frac{AM}{\epsilon_{\rm phys}}
\right).
\]

This is a conditional composition rule, not a threshold proof for the current
`D(S3)` constructor. The source must establish locality, malignant-fault
counting, recovery, and the exponential gadget estimate.

## Coherent systematic fault

If every intended edge gate `Q_A` is replaced by one common miscalibrated gate
`Q_A'`, retry and Solovay--Kitaev recursion do not average the error to zero.
The compiler approximates targets in the ideal generated group while the
apparatus executes words in a displaced representation.

Worst-case telescoping still permits error proportional to the count of
miscalibrated symbols. More importantly, internal relations and route-success
probabilities can remain consistent under a common conjugation or orientation
fault.

The three-SIC-line survival audit should therefore be inserted as an
independent calibration layer, not inferred from compiler success.

## Retry fault locality

Ideal attempts have separate outcome labels, but they may share:

- one `B`-charge reference;
- one `G/H` orientation reference;
- one mobile charged route;
- the same qutrit data;
- one clock and feed-forward controller.

A single persistent fault can affect every retry. The physical fault graph is
not the ideal geometric distribution. Before attempts can be counted as
independent locations, the constructor must reset or error-correct every
shared stateful component.

## Machine-level execution contract

A compiled target packet should report at least:

1. target projective gate and synthesis tolerance;
2. base-net version and compiler theorem;
3. logical word and counts `L_B`, `N_Q`;
4. per-injection attempt cap `n`;
5. heralded-abort bound `N_Q 4^{-n}`;
6. worst-case and expected physical location counts;
7. branch correction and reset operations;
8. per-location or encoded-gadget error assumptions;
9. accumulated error bound;
10. common-mode calibration tests and fault correlations.

Without these fields, projective density remains a mathematical reachability
result rather than an executable compiler certificate.

## Exact falsifiers

- The logical alphabet is not dense or not inverse closed while the traditional
  Solovay--Kitaev theorem is invoked without modification.
- A determinant-sixth-root restriction is treated as an obstruction in
  projective space.
- The base constant-accuracy net is assumed costless and unverified.
- Polylogarithmic word length is called exact finite synthesis.
- One injected gate has expected attempt count other than `4/3` under the
  frozen ideal branch probabilities.
- The no-success probability after `n` attempts differs from `4^{-n}`.
- A runtime cap is imposed while its abort event is discarded.
- Expected runtime is substituted for a worst-case or tail bound.
- Fixed raw physical error is claimed compatible with arbitrary target
  accuracy using only telescoping.
- A conditional exponential logical-error model is presented as a proved
  threshold for the current constructor.
- Ideal retry labels are treated as independent physical fault locations
  despite shared stateful references.
- Common coherent generator miscalibration is modeled as independent
  zero-mean noise.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies finite alphabets, recursive compilation,
word length, base nets, stopping times, heralded aborts, resource envelopes,
and shared-state fault incidence.

The quantum coefficient lens supplies projective gate metrics, `SU(3)`
compilation, diamond-distance accumulation, branch channels, encoded logical
error, and coherent generator miscalibration.

## Disposition

The projectively universal discrete qutrit alphabet admits a constructive
polylogarithmic compiler. Its probabilistic injected generator has exact
constant expected overhead and a logarithmically controllable heralded-abort
tail.

This closes the qualitative-to-algorithmic logical compiler arrow. It does not
close the physical fault-tolerance arrow. Without encoded suppression, raw
error scales with executed word length; with encoded suppression, the required
distance grows only logarithmically conditional on a separately proved
threshold theorem. The next source task is to build and fault-filter the
single `Q_A` injection gadget that this compiler repeatedly calls.

No build, checker, or Git operation was run for this research-only packet.
