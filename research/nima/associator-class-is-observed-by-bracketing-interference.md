# Associator class is observed by bracketing interference

## Question

What is the smallest operational probe that distinguishes a nontrivial
categorical-group associator from the strict object shadow?

## Claim boundary

For the \(C_2\) model, a coherent comparison of the two bracketings of three
odd sectors converts the associator sign into complementary interference
ports. This is an abstract finite instrument. It does not establish that any
particular physical sector supplies the required coherent path preparation.

## Two constructor paths

Take three copies of the odd object \(1\in C_2\). The two bracketings
\(((1\otimes1)\otimes1)\) and \((1\otimes(1\otimes1))\)

have the same object-level result. Their comparison amplitude is the
associator

\[
\omega(1,1,1).
\]

The strict model has comparison \(+1\). The nontrivial categorical group has
comparison \(-1\).

## Interference readout

Prepare the two paths coherently with equal amplitude and recombine them in
the symmetric and antisymmetric ports. Their normalized amplitudes are

\[
A_+=\frac{1+\omega}{2},
\qquad
A_-=\frac{1-\omega}{2}.
\]

For the strict model, the symmetric port is bright and the antisymmetric port
is dark. For the nontrivial model, the ports exchange:

\[
\begin{array}{c|cc}
&|A_+|^2&|A_-|^2\\
\hline
\omega=1&1&0\\
\omega=-1&0&1
\end{array}
\]

Thus an associator invisible to every single-path and object-level readout
becomes a deterministic port distinction after coherent path comparison.

## Gauge gate

An arbitrary phase attached to either path can counterfeit the signal. The
instrument is admissible only when:

1. both paths have the same typed source and target;
2. their preparation amplitudes share a source-fixed frame;
3. propagation outside the associator cell is calibrated or cancels by an
   independently authorized comparison;
4. the recombiner preserves the ordered path labels;
5. admissible two-cochain frame changes leave the measured relative phase
   invariant.

For the normalized \(C_2\) model, every source-local two-cochain has
\((\delta\beta)(1,1,1)=1\), so the sign at the hostile triple survives the
admissible rephasing class.

## Why ordinary scalar readout failed

Taking the magnitude of each path separately gives one in both models. The
distinction lives in their relative phase. Scalarization is not inherently
lossy; scalarizing before interference is. The lawful scalar record is the
intensity after the two paths have been recombined.

This identifies the ordering:

1. retain path labels;
2. apply the associator comparison;
3. interfere the paths;
4. record output intensity.

Reversing the last two operations erases the higher class.

## Cross-sector interpretation

- In optics, this is a two-route phase interferometer whose internal operation
  is rebracketing rather than geometric path length.
- In topological phases, fusion-tree interferometry is the native realization.
- In software, replaying two constructor trees into a comparison port can
  expose an authority-sensitive associator that equal endpoint bytes miss.
- In flavor or boundary completion, the proposal becomes physical only if two
  bracketed source operations can be coherently prepared and recombined before
  the final readout.

## DPC

To claim operational observability of a higher class:

1. identify a tuple where the cocycle has a gauge-invariant nontrivial value;
2. construct both bracketed paths from source operations;
3. prove common endpoints and ordered-label preservation;
4. calibrate every non-associator phase;
5. recombine before scalar detection;
6. require complementary-port exchange under the hostile class;
7. delete coherent recombination and confirm that the distinction disappears.

## Disposition

The nontrivial \(C_2\) associator has a finite operational witness: deterministic
exchange of two interference ports. The remaining sector-specific question is
whether the required coherent constructor-path instrument is source-derived.

## Verification

The checker check_associator_bracketing_interference.py evaluates all eight
\(C_2\) triples, confirms complementary normalized ports, isolates the unique
nontrivial odd triple, verifies invariance under all normalized sign
two-cochains, and confirms that separate path intensities are blind.
