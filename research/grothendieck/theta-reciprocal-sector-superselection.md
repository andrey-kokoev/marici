# Reciprocal-sector superselection as the explanation of the critical seam

Author: `marici.Grothendieck`

## 0. Operator stimulus

The operator asked for Explanation and Understanding, not another equivalent
inequality.  The preceding exact results supplied:

1. a labelled theta/Euler Hilbert Carrier;
2. a scalar observer that becomes singular before the Carrier does;
3. reciprocal half-planes;
4. a value-one vacuum--tail incidence;
5. integral phase defects at zeros.

The question is why the two reciprocal sheets should be allowed to cancel
only at the critical seam.  Their Hilbert types give a hard-to-vary answer.

## 1. Reciprocal-real involution

Let

\[
s^\vee=1-\bar s.
\]

This is reflection across the critical line.  Its fixed locus is

\[
s=s^\vee
\quad\Longleftrightarrow\quad
\operatorname{Re}s=\frac12.
\]

Associate to each point the labelled Dirichlet state

\[
k_s=\sum_{n\ge1}n^{-s}e_n.
\]

The exact Hilbert criterion is

\[
k_s\in\ell^2(\mathbb N)
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac12.
\]

For the reflected sheet,

\[
k_{s^\vee}\in\ell^2(\mathbb N)
\quad\Longleftrightarrow\quad
1-\operatorname{Re}s>\frac12,
\]

or

\[
\operatorname{Re}s<\frac12.
\]

Therefore

\[
\boxed{
\begin{array}{c|c|c}
\text{region}&k_s&k_{s^\vee}\\
\hline
\operatorname{Re}s>1/2&\text{Hilbert state}&\text{dual/distributional sheet}\\
\operatorname{Re}s<1/2&\text{dual/distributional sheet}&\text{Hilbert state}\\
\operatorname{Re}s=1/2&\text{critical boundary type}&\text{same boundary type}
\end{array}
}
\]

Off the seam, the sheets are not two vectors of the same Hilbert type.

## 2. Why one half is forced

The line is selected simultaneously by:

1. the fixed-point equation `s=s^vee`;
2. equality of reciprocal integrability exponents
   \[
   \operatorname{Re}s=1-\operatorname{Re}s;
   \]
3. the Hilbert--Schmidt threshold
   \[
   \sum_n n^{-2\operatorname{Re}s}<\infty;
   \]
4. the two-copy prime threshold
   \[
   \sum_p p^{-2\operatorname{Re}s}<\infty.
   \]

Every route yields

\[
\boxed{\operatorname{Re}s=\frac12.}
\]

The offset is therefore not fitted to the observed zeros.  It is the unique
self-dual boundary between the coefficient and reciprocal-dual
representations.

## 3. The superselection principle

Destructive cancellation is meaningful only after two contributions have
been transported into a common comparison object.  A Hilbert vector and a
distributional covector may pair, but they cannot be identified or added as
though they were two vectors in one fiber.

This suggests the source law:

\[
\boxed{
\textbf{Reciprocal-sector superselection.}\quad
\text{A faithful completed observation cannot identify and cancel the two
reciprocal sheets while they belong to different representation types.}
}
\]

On the seam, the two types reach the same critical boundary and modular
sewing supplies their relative pairing.  Cancellation is then
type-authorized.

RH becomes the assertion that the physical scalar observer respects this
superselection rule.

## 4. Coefficient--Betti interpretation

The distinction resembles the paired coefficient--Betti system:

\[
\text{coefficient state}
\quad\leftrightarrow\quad
\text{dual readout}.
\]

In the right chamber, `k_s` is naturally on the coefficient/Hilbert leg and
`k_(s^vee)` belongs to the reciprocal dual leg.  In the left chamber their
roles reverse.  The critical seam is the self-dual locus where the two legs
can be compared without choosing an off-center metric identification.

Thus a zero off the seam would mean that scalar projection had silently
forgotten which leg was a state and which was a dual observer.  This is
exactly the kind of unfaithful quotient already prohibited elsewhere in the
Marici programme.

## 5. Vacuum--tail meaning

The modular scalar identity

\[
2X(z)=1-\mathcal O(z)
\]

is the decategorified readout.  The value `1` is the seam-created vacuum
unit, while `O(z)` is the labelled residual tail.

The superselection explanation of

\[
\mathcal O(z)=1
\]

is:

\[
\boxed{
\text{vacuum--tail equality is a valid scalar shadow only where the
reciprocal state and dual-state types coincide.}
}
\]

An off-seam equality would be a scalar coincidence unsupported by a faithful
typed lift.

## 6. What this explains at once

The proposal explains:

1. **Why two half-planes:** they are the state and reciprocal-dual sectors.
2. **Why the offset is `1/2`:** it is their unique type-equality locus.
3. **Why the Euler readout fails at `1`:** the all-label covector becomes
   unbounded before the Hilbert state leaves its chamber.
4. **Why the Carrier survives to `1/2`:** quadratic label energy remains
   finite throughout the anomaly corridor.
5. **Why zeros are meaning loss:** scalar cancellation forgets the
   state-versus-observer distinction.
6. **Why zeros carry integers:** failure of a determinant-line
   trivialization has integral winding.
7. **Why finite probes fail at the seam:** the normalized Carrier converges
   weakly to zero and escapes every compact observer.
8. **Why modular completion is essential:** it constructs the relative
   boundary pairing between the two sector types.

This compression is difficult to vary without breaking several independently
derived facts.

## 7. The missing theorem is faithfulness of descent

The explanation becomes a proof only if one constructs a diagram

\[
\begin{array}{ccc}
\text{typed reciprocal Carrier}&\longrightarrow&\text{relative boundary object}\\
\downarrow&&\downarrow\\
\text{labelled theta/Euler data}&\longrightarrow&X(s)
\end{array}
\]

such that:

1. the upper map preserves the state/dual sector grading;
2. its scalar descent is exactly the completed xi readout;
3. the destructive kernel has empty intersection with either open-sector
   image; and
4. boundary intersection reproduces the value-one incidence and its
   multiplicity.

The third clause is RH.  It must follow from the typed construction, not be
installed as an axiom.

## 8. Deutsch--Popperian conjecture

\[
\boxed{
\begin{array}{l}
\textbf{Typed reciprocal-faithfulness conjecture.}\\
\text{The completed theta/Euler scalar is the descent of a
state--dual}\\
\text{Carrier whose sector grading is faithful off the self-dual seam.}\\
\text{Therefore its destructive projection kernel intersects the Carrier}\\
\text{only where }\operatorname{Re}s=1/2.
\end{array}
}
\]

This is the present best Explanation of RH in the programme.  It does not say
that positivity pushes zeros onto a line.  It says that only the self-dual
line authorizes the identification whose scalar shadow is a zero.

## 9. Falsifiers

The explanation fails if:

1. a source-derived morphism identifies the state and dual legs off the seam;
2. the completed scalar cannot be lifted without forgetting their grading;
3. an admissible typed Carrier has an off-seam vector in the destructive
   kernel;
4. the physical readout requires a higher-copy type whose self-dual boundary
   is not selected by `S_2`; or
5. the proposed “sector” is defined from zero locations rather than the
   theta/Euler source.

The smallest hostile test is a two-sector model with the same involution,
Schatten thresholds, and modular boundary pairing but an off-seam
destructive incidence.  Such a model would show that type distinction alone
does not guarantee faithful descent.

## 10. Scope

The reciprocal involution, Hilbert membership dichotomy, unique self-dual
line, and vector/dual mismatch are exact.  Reciprocal-sector superselection
is the proposed explanatory law.  Its faithful completed descent has not
been constructed, and RH is not proved.

## 11. Hostile audit: typing alone is not a conservation law

The proposed explanation has an immediate hostile model.  In the centred
coordinate (z=s-1/2), choose (a\notin\mathbb R\cup i\mathbb R) and set

\[
 P_a(z)=
 \frac{(z^2-a^2)(z^2-\overline a^{,2})}{|a|^4}.
\]

Then (P_a) is even, real on both symmetry axes, satisfies (P_a(0)=1),
and inserts the reciprocal-real quartet

\[
 \{a,-a,\overline a,-\overline a\}.
\]

Consequently \(\widetilde X=P_aX\) has the same centred functional equation,
real structure, self-dual seam, and source-independent Schatten membership
table as (X), but it has off-seam destructive incidences.  The two sector
types have not prevented their scalar shadows from cancelling.

This falsifies the **bare** superselection claim.  A representation type says
which operations are continuous; it does not by itself say that a particular
meromorphic or distributional pairing is forbidden.  Different types may
still descend to the same complex number.

The surviving explanatory target must therefore include a conservation law
derived from the theta source:

\[
\boxed{
\begin{array}{l}
\text{The completed observation functor preserves the reciprocal-sector}\
\text{grading and admits no source-compatible divisor insertion }P_a.\
\text{Its destructive incidence is a boundary morphism, hence is supported}\
\text{only on the self-dual seam.}
\end{array}}
\]

The phrase *source-compatible* is the entire burden.  Symmetry, order,
reality, integer multiplicity, and the \(S_2\) threshold do not define it.
It must be characterized positively by an operation on the labelled theta
Carrier--for example a modular sewing law, a determinant-line connection, or
a conserved relative index--and that characterization must exclude (P_a)
without referring to its zeros.

## 12. What “loss of integrality” can mean precisely

The hostile audit also separates divisor integrality from categorical
integrality.  Zero multiplicities are already integers in the hostile model,
so their integrality cannot explain RH.  The promising integer is instead a
relative index of the two polarized sectors.  Such an index is locally
constant while the corresponding pair remains Fredholm and can jump only
when transversality is lost.

This gives a precise version of the operator's intuition:

\[
\text{half-planes acquire distinct analytic types}
\longrightarrow
\text{a relative integer becomes defined}
\longrightarrow
\text{the integer can change only at loss of transversality}.
\]

The seam is the unique place where the reciprocal types exchange.  But a
usable theorem still requires an actual source-derived Fredholm pair whose
index jump multiplicity equals the zero multiplicity of (X).  Until that
object is constructed, “loss of integrality” is a geometric research
instruction, not a proof.

## 13. Revised Deutsch--Popperian conjecture

The stronger and less variable conjecture is:

\[
\boxed{
\begin{array}{l}
\textbf{Theta relative-index conjecture.}\\
\text{The completed theta Carrier canonically defines a reciprocal pair of}\
\text{polarized subspaces whose relative index is conserved in each open}\
\text{half-plane.  The completed scalar }X\text{ is its determinant section,}\
\text{and its divisor is exactly the loss-of-transversality divisor.}
\end{array}}
\]

If the reciprocal pairing can lose transversality only when its two analytic
types meet, RH follows.  Its smallest decisive falsifier is a
theta-compatible off-seam loss of transversality, not merely an artificial
quartet multiplier.

## 14. Boundary correction: the sectors do not meet inside Hilbert space

There is a necessary typing correction.  On the seam,

\[
 \sum_{n\ge1}|n^{-s}|^2=\sum_{n\ge1}\frac1n=\infty.
\]

Thus (k_s) and (k_{1-\overline s}) do not become two equal vectors in
\(\ell^2\).  They approach a common **failure of Hilbert realizability** from
opposite sides.  The self-dual line is therefore not an ordinary intersection
of two Hilbert sectors.  It is a boundary at which a relative object must be
formed by subtraction, renormalization, or modular sewing.

This turns the operator's “loss of meaning” intuition into a sharper sequence:

\[
\begin{array}{c}
\text{one reciprocal leg is a state and the other is a dual object}\
\downarrow\\
\text{at }\operatorname{Re}s=1/2\text{ both ordinary realizations fail}\
\downarrow\\
\text{only a completed relative pairing can retain a scalar meaning.}
\end{array}
\]

Zeros would then be failures of that *relative* scalar, not failures of either
raw leg.  This also explains why the constant-plus-tail completion matters:
the vacuum term is part of the boundary renormalization, not decorative
normalization.

## 15. Explanation versus restatement

The present understanding has two cleanly separated parts.

**Kinematics, already explained.**  Reciprocity exchanges the two
half-planes; quadratic/Hilbert--Schmidt summability fixes their boundary at
one half; normalized mass escapes every compact observer there; modular
completion supplies a finite relative scalar.  These facts explain why the
critical line is geometrically distinguished before any zero is inspected.

**Dynamics, still missing.**  Why does the completed relative scalar lose
transversality only on that distinguished boundary?  Neither symmetry,
positivity of the undeformed source, divisor integrality, nor representation
typing answers this.  The quartet multiplier proves their insufficiency.

So the next object should not be another scalar inequality.  It should be a
source-local conservation law with three checkable properties:

1. it is defined on labelled theta data before scalar projection;
2. its boundary determinant is exactly \(X\), including the vacuum term; and
3. an off-seam zero would force a forbidden change of its integer class.

That would be Understanding in the Deutschian sense: the line would be forced
by the same structure that defines the observable, and hostile symmetric
quartet insertions would fail because they lack that structure--not because
they were excluded by naming RH in another language.
