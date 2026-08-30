# Cosmological quartic as a sourced port-adapter filter

Status: Deutsch--Popperian conjecture and finite falsification contract.

## Evidence boundary

The cosmological quartic \(\mathcal Q\) has repeatedly failed as:

- a new generic Carrier divisor;
- a generic rank-loss divisor of the marked-relative presentation;
- an intrinsic residue of the generic algebraic marked extension;
- a scalar connection on the fitting-conic quotient line;
- a singularity of the pure elliptic infinity--Gysin quotient.

Those failures do not exclude a role for \(\mathcal Q\) in a *typed
comparison*.  Nima's operational-module architecture and the C8
nontransverse calculation independently distinguish four stages:

\[
\text{Carrier}
\longrightarrow
\text{source relation}
\longrightarrow
\text{local coefficient module}
\longrightarrow
\text{physical readout}.
\]

For C8 the last two arrows factor visibly as

\[
\mathbf 1_{D(F)=R}
\times
\text{Bunch--Davies regulator-chamber selection}.
\]

This produces 8 canonically selected, 168 source-visible but unselected, and
112 routing-invisible occurrences without changing the Carrier.

## Hard-to-vary conjecture

If \(\mathcal Q\) has an intrinsic physical role in the homogeneous
three-site loop system, it is the support or filtration boundary of a
source-derived port-adapter comparison, not an undeclared Carrier wall or a
pole of an arbitrarily chosen coefficient representative.

Schematically, for a source-normalized adapter

\[
\mathsf A_{\rm src}\colon
(\mathcal M_{\rm loc},\Gamma_{\rm BD})
\longrightarrow
\mathcal R_{\rm phys},
\]

the allowed claim is

\[
\operatorname{Supp}
\operatorname{Cone}(\mathsf A_{\rm src})
\supseteq V(\mathcal Q),
\]

or the corresponding statement for a sourced associated grade, chamber
transition, or nearby-cycle specialization.  The adapter must exist before
its \(\mathcal Q\)-support is factored.

## Admissible locations

The preregistered locations are ordered by variance.

1. **Carrier support.** Rejected generically by the existing rank and
   divisor audits.  Proper intersections with existing walls remain typed,
   but are not new \(\mathcal Q\)-Carrier strata.
2. **Absolute coefficient singularity.** Rejected for the pure elliptic
   quotient, rank-four infinity--Gysin block, and generic marked algebraic
   extension.
3. **Constructor/base-change singularity.** Disfavored at the physical
   half twist: the bounded rank-26 module family has a common regular
   Plucker chart and stable rank through the tested pole depths.
4. **Source-accessibility filter.** Open.  A regular local module may have a
   smaller source-generated operational image.  This is meaningful only for
   true covariant jets or a source-labelled localization complex, not a
   frozen-point Krylov closure.
5. **Port-adapter coherence support.** Open.  A localization, Gysin, Leray,
   or nearby-cycle comparison may fail to commute or acquire a supported
   cone on \(V(\mathcal Q)\), even when both endpoint modules are regular.
6. **Physical readout/chamber filter.** Open.  The Bunch--Davies relative
   cycle may transport into inequivalent chambers or coefficient sheets
   across \(V(\mathcal Q)\).  C8 proves that this type of filter exists in a
   source-derived model, but does not identify it with \(\mathcal Q\).

The complete physical five-mark presentation supplies a concrete candidate
for item 5.  Its moving absolute-to-common localization adapter \(F\) has
mixed curvature

\[
\Theta=dF+A_{\rm common}F-FA_{\rm absolute}.
\]

After the source-derived derivative is retained, two of the three frozen
defect directions cancel and one direction remains.  Each parameter component
has rank one, while the two components jointly span rank two.  This is the
correct variance for an adapter-coherence filter.  Present evidence certifies
its rank and incidence pattern over several finite fields, but not stable
characteristic-zero coefficients or intrinsic divisor support.

The already-derived total-energy transport preserves the marked-relative
Čech closure and is quartic-free to all tested orders.  Therefore a generic
\(\mathcal Q\)-filter cannot be assigned to that one-parameter port.  If it
exists, it must occur in an independently sourced second kinematic direction,
in mixed transport/coherence, or in the transported physical pairing.

## Sequential typing rule

The known readouts are sequential:

\[
M_{12}\xrightarrow{\operatorname{Res}_W}W_3,
\qquad
\ker(\operatorname{Res}_W)=M_9,
\qquad
M_9\xrightarrow{R_\infty}V_{\rm ell}(-1).
\]

Therefore a \(\mathcal Q\)-filter may be tested only on the domain left by
the preceding source-derived port.  Parallelizing these maps by a chosen
splitting is inadmissible.  Likewise, a coordinate quotient or fitted scalar
connection cannot substitute for the missing adapter.

Caroline's flavor audit adds the cross-sector fiber rule:

\[
\boxed{\text{a finite fiber is not a singleton fiber}.}
\]

Injectivity, uniqueness, and reconstruction claims must therefore be tested
in a faithful quotient coordinate (flavor's `physical16`), never inferred
from the measured ten-coordinate projection.  The measured ten may certify
compatibility or finite ambiguity, but cannot distinguish points collapsed
by its projection.  Any theorem using it must preserve that distinction
explicitly.

The cosmological analogue is that equal scalar periods may certify compatible
readout or a finite adapter fiber, but cannot establish equality of two
source-labelled adapter points.  The faithful comparison object must retain
the marked-relative class, occurrence labels, connection, and relative-cycle
data before evaluating the terminal scalar period.

## First finite falsifier

### Exact mechanism witness

The source letters already define the regular symmetric matrix

\[
G_{\rm toy}=
\begin{pmatrix}
2A&A+B-E^2\\
A+B-E^2&2B
\end{pmatrix},
\qquad
\det G_{\rm toy}=\mathcal Q.
\]

An exact Rust checker verifies this polynomial identity, its second-normal
expansion, and

\[
\det(S^TG_{\rm toy}S)=\det(S)^2\det(G_{\rm toy})
\]

for a generic symbolic regular gauge.  At all six prepared generic quartic
samples the matrix is nonzero of rank one.  This proves that a regular
rank-two transport object can acquire a rank-one paired response on
\(V(\mathcal Q)\) without any endpoint singularity.  It is a mechanism
witness, not an identification of the physical response form.

A subsequent typing audit rejects the most direct realization
\(G_{ij}=\langle\Theta_i,\Theta_j\rangle\): the source supplies twisted
de Rham--Betti/Leray duality, but no canonical self-polarization on the
mixed-curvature Hom space.  A coordinate trace or dot product would be a
post-hoc choice.  The surviving physical realization must instead use
independently source-derived readout channels.  The literal numerator already
has two labelled summands, \(g_{23}\) and \(g_{31}\), suggesting the typed
response matrix

\[
R_{\alpha i}=\operatorname{Per}_{\Gamma_\alpha}(\Theta_i s),
\qquad
\alpha\in\{23,31\},\quad i\in\{u,v\},
\]

but only after both branch-relative Leray germs and their common localization
maps are constructed without splitting the unsplit physical source.

Evidence:

- `research/benincasa/marici-gm/src/bin/q_pairing_discriminant_toy.rs`;
- `research/benincasa/results/q-pairing-discriminant-toy.json`.
- `research/benincasa/results/q-pairing-typing-gate.json`.

### Finite-field gate on the existing mixed curvature

Before constructing a larger physical comparison cone, rerun the complete
dual-number presentation at generic points of \(V(\mathcal Q)\) and at held-out
generic fibers over at least two primes.  Test whether the intrinsic ranks,
source covector, and image incidence of \(\Theta\) change on the quartic.
This test uses the full presentation directly and does not require rational
reconstruction of a representative.

If generic quartic fibers preserve the same rank-one directional defect and
rank-two joint image, \(\mathcal Q\) is not support of this first adapter
coherence class.  If the class vanishes, jumps, or changes incidence
generically on \(\mathcal Q\), characteristic-zero reconstruction and gauge
invariance become mandatory before promotion.

### Full physical comparison

Construct the smallest source-normalized comparison square that retains:

- the rank-20 physical marked-relative object and its surviving wall maps;
- the canonical negative-tube Leray germ;
- the relevant localization/Gysin target;
- occurrence labels, orientations, deck character, and connection;
- no chosen splitting of the sequential residue filtration.

Then restrict the *comparison cone*, not either endpoint alone, to the
generic function field of \(V(\mathcal Q)\).  Compare it with a held-out
generic fiber and compute:

1. rank and cohomology;
2. logarithmic residue or nearby-cycle grade;
3. invariance under source-admissible triangular gauge;
4. compatibility with the transported Bunch--Davies cycle.

The generic and quartic fibers must first be compared in that faithful
relative quotient.  Equality only after scalar period evaluation is
insufficient.

The conjecture survives this test only if a nonzero \(\mathcal Q\)-supported
class remains after all four checks.

The local worktree contains a generic source-normalized four-stratum reduction
engine and canonical boundary maps.  Its finite-field certificate has rank
117, seven primitive-independent marked coordinates, zero cleared residuals,
and a zero forbidden absolute-to-marked block.  The wall quotient connection
is also explicit and flat.  What remains missing is narrower but decisive:

- wall-Laurent replication of the same common reduction;
- characteristic-zero certification of the multivariate extension block;
- the complete faithful physical marked-relative object and transported
  Leray covector needed for the terminal comparison.

The current characteristic-zero extension packet is a modular reconstruction
candidate whose exact source substitution is pending.  Its denominators may
therefore guide discovery but cannot establish \(\mathcal Q\)-support.

## Falsifiers

The conjecture fails in this sector if:

- the complete source-normalized adapter extends regularly and canonically
  across generic \(\mathcal Q=0\);
- any apparent \(\mathcal Q\)-factor is removable by an admissible regular
  gauge or disappears after respecting the sequential port domains;
- the filter can be produced only by choosing a splitting, primitive lift,
  coordinate projector, regulator hierarchy, or desired period value;
- the required map is absent from the frozen source and cannot be derived
  from its localization, relative-cycle, or nearby-cycle data.

No negative result here would remove the established algebraic-letter
quartic from the integrated formula.  It would say only that its physical
provenance is not a sourced port-adapter filter in this comparison.
