# `D(S3)` charge measurement factorizes into flux class and centralizer Fourier stages

Owner: `marici.Kitaev`

## Question

Can the source-derived eight-charge PVM be decomposed into physically
meaningful stages, and what hidden apparatus records would accidentally make
the measurement too fine?

Yes. The central charge observable factors exactly into:

1. a gauge-invariant conjugacy-class measurement;
2. a conditional measurement of the irreducible centralizer charge.

The sequential Lüders instrument is exactly the primitive central charge PVM.
However, a naive implementation that retains the based holonomy element, a
chosen conjugating frame, or Fourier matrix indices performs a finer
noncentral measurement. Those garbage ports must be coherently uncomputed or
proved operationally irrelevant.

## Claim boundary

This packet gives an exact algebraic instrument factorization and a typed
apparatus blueprint. It does not supply native gates for coherent holonomy
extraction, conditional centralizer transport, nonabelian Fourier transforms,
or garbage uncomputation.

The localized endpoint and crossed-product convention are frozen from the
preceding central-idempotent packet. This is not a torus ground-sector
measurement.

## Flux-class PVM

For each conjugacy class `C` of a finite group `G`, define

\[
R_C
=
\sum_{g\in C}(g,e)
=
\sum_{g\in C}B^g.
\]

The projectors satisfy

\[
R_CR_{C'}=\delta_{C,C'}R_C,
\qquad
\sum_CR_C=I.
\]

Because conjugation permutes the elements inside `C`, every `R_C` commutes
with the based gauge action. Thus flux class is a gauge-invariant magnetic
record even though an individual `B^g` is not.

For `S3`, the three outcomes are identity flux, transposition flux, and
three-cycle flux.

## Charge refinement

Let `Q_(C,pi)` be the primitive central idempotent associated with conjugacy
class `C` and irreducible centralizer representation `pi`.

The orbit-stabilizer formula gives

\[
Q_{C,\pi}R_{C'}
=
\delta_{C,C'}Q_{C,\pi}.
\]

Moreover,

\[
\sum_{\pi\in\widehat{Z_c}}Q_{C,\pi}=R_C.
\]

Therefore the charge projectors refine the flux-class projectors. The class
record answers which magnetic orbit is present; the conditional centralizer
record answers which electric charge lives on that orbit.

For `S3`, the refinement sizes are:

| flux class | centralizer | charge outcomes |
|---|---|---:|
| identity | `S3` | 3 |
| transpositions | `C2` | 2 |
| three-cycles | `C3` | 3 |

The full count is eight.

## Sequential Lüders theorem

First apply the flux-class Lüders branch

\[
\mathcal I_C(\rho)=R_C\rho R_C.
\]

Conditioned on class `C`, apply the charge-refinement branch

\[
\mathcal J_{\pi|C}(\sigma)
=
Q_{C,\pi}\sigma Q_{C,\pi}.
\]

Since

\[
Q_{C,\pi}R_C=Q_{C,\pi},
\]

the composite branch is

\[
\mathcal J_{\pi|C}\mathcal I_C(\rho)
=
Q_{C,\pi}\rho Q_{C,\pi}.
\]

This is exactly the branch of the complete central charge PVM. Summing all
branches gives

\[
\rho
\longmapsto
\sum_{C,\pi}
Q_{C,\pi}\rho Q_{C,\pi}.
\]

Thus the two-stage measurement is neither weaker nor stronger than the
primitive central PVM when no additional apparatus coordinate survives.

## What the first stage preserves

Stopping after class measurement leaves coherent matrix elements between
different centralizer charges inside the same flux class. It removes only
coherence between distinct magnetic classes.

The second stage removes coherence between distinct charge blocks within that
class while preserving the full matrix algebra inside each simple charge
block.

This gives a nested record-control frontier: no record, then a flux-class
record, then the full charge record.

Each arrow refines the pointer algebra and shrinks the cross-block future
algebra accordingly.

## Coherent class extraction

A conceptual class extractor begins by computing the based plaquette holonomy
into a workspace register:

\[
|\mathbf g\rangle|e\rangle
\longmapsto
|\mathbf g\rangle|h(\mathbf g)\rangle.
\]

It then computes the conjugacy class label into the retained pointer:

\[
|h\rangle|0\rangle
\longmapsto
|h\rangle|C(h)\rangle.
\]

To realize only `R_C`, the element-valued holonomy workspace must be
uncomputed before the class pointer becomes the sole retained record.

If the element register is measured, lost, or copied into the environment,
the apparatus has recorded `g`, not merely its conjugacy class. That record
selects a based gauge frame and dephases superpositions inside the conjugacy
orbit.

Correct final class probabilities do not repair this excessive back-action.

## Conditional centralizer Fourier stage

Within a class `C`, choose a representative `c` and coherently transport each
element

\[
g=x_gc x_g^{-1}
\]

to the reference centralizer `Z_c`.

The stabilizer group algebra is decomposed by its Fourier transform. Retaining
only the irrep label `pi` implements the centralizer character projector.

For the three `S3` classes, the conditional transforms are:

- identity flux: the nonabelian Fourier transform of `S3`, retaining only the
  irrep label;
- transposition flux: the two-point Fourier transform of `C2`;
- three-cycle flux: the three-point Fourier transform of `C3`.

The `C3` branch requires coherent cube-root phases. The identity branch has a
two-dimensional irrep and therefore Fourier row and column indices in addition
to the irrep label.

## Fourier-index overmeasurement

A full group Fourier basis for a nonabelian group has coordinates

\[
(\pi,i,j).
\]

The central charge PVM retains only `pi`. Recording `i` or `j` resolves matrix
coordinates inside the simple block. By the center-maximality theorem, such a
record destroys some within-block future operators.

Therefore a correct charge apparatus must either:

- never expose the Fourier matrix indices;
- coherently erase them after transferring `pi`;
- or explicitly admit the finer instrument and its reduced future algebra.

Discarding an entangled index register is not erasure. It produces the finer
nonselective dephasing even when the visible output displays only `pi`.

## Conjugating-frame garbage

The choice `x_g` used to identify `Z_g` with `Z_c` is not a physical charge
label. Different choices differ by a centralizer element and yield the same
transported character.

If an apparatus retains `x_g`, it records a gauge-frame coordinate absent from
the central PVM. This can distinguish implementations that should be
equivalent at the charge level and can break gauge covariance.

The frame register must be uncomputed, quotiented by an authorized invariant
map, or retained as an explicitly additional output with a new disturbance
audit.

## Minimal clean output

The clean coherent isometry for the intended charge record has the form

\[
W
=
\sum_{C,\pi}
Q_{C,\pi}\otimes|C,\pi\rangle_R,
\]

with every workspace returned to one source-independent state.

The output record space needs at least eight mutually orthogonal states. It may
be represented by one eight-level pointer or three clean qubits.

This dimension statement concerns a perfect single-shot record. Fault
detection or correction of later pointer errors requires a larger code, as
established in the separate six-bit record theorem.

## Charge clock equivalence

Choose eight distinct phases `lambda_a` and define the central unitary

\[
U_Q
=
\sum_{a=1}^{8}\lambda_aQ_a.
\]

Exact phase estimation of `U_Q` gives the charge label. Conversely, a clean
charge extractor can implement phase kickback by applying the desired phase
to the record label and uncomputing the extractor.

Thus clean charge extraction and coherent access to a nondegenerate central
charge clock are interconvertible, modulo pointer preparation, controlled
powers, and uncomputation.

This does not make either primitive. It locates the missing interaction in a
single equivalent form.

## Relation to the earlier apparatus obstruction

The frozen native surface contains no record--data interaction, so it cannot
implement the clean extractor or controlled charge clock. The previously
postulated five-body conditional Hamiltonian closes that cut only as an
apparatus enlargement.

The new factorization does not evade the obstruction. It refines the target
of that enlargement:

1. magnetic class extraction;
2. conditional stabilizer Fourier transform;
3. erasure of element, frame, and Fourier-index garbage;
4. retention of only the eight-valued charge label.

A lower-arity construction can now be judged against these exact semantic
requirements.

## Fault boundaries

Different faults attack different layers.

### Holonomy acquisition fault

The workspace contains the wrong based element before class reduction. A
later record code can faithfully protect the wrong charge label.

### Class-map fault

An element is assigned to the wrong conjugacy class. The conditional
centralizer branch may then execute the wrong Fourier transform.

### Fourier-phase fault

The `C2`, `C3`, or `S3` character phase is wrong, mixing or mislabeling
electric charges within the correct flux class.

### Garbage-uncomputation fault

The visible label is correct while a hidden element, frame, or matrix-index
register remains entangled and causes excess dephasing.

### Final record fault

The clean charge label is acquired correctly and a later storage bit flips.
Only this last layer is covered by the final classical record code.

The first failed layer must be reported; a final-label checksum cannot repair
an upstream instrument error that lands on another valid codeword.

## Hostile fixtures

### Element measurement presented as class measurement

Measure the based holonomy `g`, compute `C(g)`, and hide the element output in
an unobserved environment. The hidden record still dephases the gauge orbit.

### Class-only record called full charge

Distinguish the three conjugacy classes and ignore the `3,2,3` centralizer
charge multiplicities.

### Full Fourier basis called central charge

Record nonabelian Fourier matrix indices together with the irrep label and
claim preservation of the full simple-block algebra.

### Frame choice retained

Store `x_g` as a diagnostic output and call the instrument gauge invariant.

### Correct probabilities used to infer correct instrument

Match the eight charge probabilities while leaving hidden garbage entangled.
Effects agree, but branch maps and future capability differ.

### Final code applied upstream

Use the six-bit classical record code to claim correction of a holonomy or
Fourier acquisition fault that produces a valid wrong charge label.

### Charge clock called native

Define `U_Q` spectrally and infer controlled powers from its mathematical
existence.

## Falsifiers

- The class projectors fail orthogonality, completeness, or gauge invariance.
- The charge projectors fail to refine their class projectors.
- Sequential class and conditional-charge Lüders branches differ from
  `Q_(C,pi) rho Q_(C,pi)`.
- Retaining a based element or Fourier index produces no additional
  disturbance despite distinguishing a finer algebra.
- A record space of dimension below eight carries eight perfectly
  distinguishable charge labels.
- A class-only measurement separates all eight charges.
- A clean extractor and charge clock fail the stated phase-kickback
  interconversion under the declared controls.
- Final-label coding is promoted to correction of upstream coherent
  acquisition faults.

## Shared Carrier geometry and coefficient lens

Shared Carrier geometry supplies staged refinement, workspace cuts,
conditional branching, retained-versus-erased ports, and the rule that hidden
garbage changes the future Carrier.

The quantum coefficient lens supplies conjugacy classes, centralizer Fourier
analysis, Lüders instruments, phase kickback, and within-block disturbance.

The two-stage skeleton is reusable. Its `S3`, `C2`, and `C3` transforms and
the meaning of their labels are coefficient-specific.

## Disposition

The localized eight-charge observable now has an exact staged instrument
target: gauge-invariant flux class followed by conditional centralizer irrep.
The sequential ideal branches equal the primitive central PVM exactly.

The main new obstruction is garbage sensitivity. A physical implementation
must erase the element-valued holonomy, conjugating frame, and nonabelian
Fourier matrix indices. Otherwise it records a finer noncentral coordinate
and sacrifices more endpoint capability than the visible charge label
suggests.

This is the correct next specification for a microscopic `D(S3)` charge
apparatus. No checker, build, or Git operation was run for this research-only
packet.
