# Theta projective meaning loss

Author: `marici.Grothendieck`

## 0. Operator stimuli and discovery provenance

This branch was opened by the operator, not by extrapolation from the
radial-score programme.  The decisive sequence was:

1. The operator proposed that RH zeros might arise through destructive
   interference between two planes or sheets, rather than by locating
   independently existing spectral objects.
2. The operator asked why the critical line is shifted from the apparent
   natural origin and suggested a symmetric unfolded fold.  This led to the
   centered coordinate `s=1/2+iz`, where the offset `1/2` is recognized as
   the fixed midpoint of `s -> 1-s`, not a dynamical displacement.
3. After the programme had pursued Hermite--Biehler and radial-score
   positivity, the operator challenged the phrase “every zero lies there”
   as potentially misleading and proposed the alternative: the line is
   where something loses its meaning, producing the observed zeros.

The third stimulus caused the material change of research direction.  It
forced separation of:

\[
\text{source state}
\longrightarrow
\text{two-sheet projective meaning}
\longrightarrow
\text{scalar sum readout}.
\]

Only the last arrow loses information at a zero.  The source and its two
sheet coordinates need not disappear.  Formalizing that observation exposed
the projective ratio `rho=F(-z)/F(z)` and showed that RH requires avoidance of
only the destructive value `rho=-1` off the fixed locus.  This in turn
revealed that the previously pursued Hermite--Biehler inequality
`|rho|>1` is a strictly stronger sufficient target.

The operator's language of “loss of meaning” then prompted the second exact
reduction: nonvanishing on an open half-plane is equivalent to existence of
a coherent holomorphic logarithm there.  Off-line zeros are consequently
interior phase defects; RH localizes every such defect to the common
symmetry boundary.

The reusable meta-heuristic is:

\[
\boxed{
\text{When an existence statement sounds ontologically forced, ask whether
the observed event is instead a failure of a particular readout to remain
faithful.}
}
\]

Here that question weakened the live theorem from orientation of an entire
projective region to avoidance of one destructive incidence divisor.

## 1. The semantic correction

Put

\[
X(z)=\xi\left(\frac12+iz\right),
\qquad
F(z)=\int_0^\infty\Phi(u)e^{izu}\,du.
\]

The completed readout is

\[
X(z)=F(z)+F(-z).
\]

A zero does not mean that the theta source, or either sheet, has ceased to
exist.  It means that the scalar projection has erased the distinction
carried by the two-sheet state

\[
\mathcal C(z)=(F(z),F(-z)).
\]

With `pi(a,b)=a+b`, the zero condition is

\[
\mathcal C(z)\in\ker\pi.
\]

Thus RH has the exact projective-faithfulness formulation

\[
\boxed{
\mathcal C(\mathbb C\setminus\mathbb R)\cap\ker\pi=\varnothing.
}
\]

The real `z`-axis is the fixed locus of the completed real structure and is
the critical line in the original `s`-plane.  RH says that loss under this
particular scalar projection occurs only on that symmetry-authorized locus.

## 2. The faithful quotient coordinate

Where `F(z)` is nonzero, define the projective sheet ratio

\[
\rho(z)=\frac{F(-z)}{F(z)}.
\]

Then

\[
X(z)=0
\quad\Longleftrightarrow\quad
\rho(z)=-1.
\]

The exact sheet symmetries are

\[
\rho(-z)=\rho(z)^{-1},
\qquad
\rho(\bar z)=\overline{\rho(z)}^{-1}.
\]

Consequently

\[
|\rho(x)|=1
\qquad(x\in\mathbb R)
\]

whenever the ratio is defined.  Boundary zeros of `X` are the points at
which this unit-circle-valued projective coordinate reaches the destructive
phase `-1`.

The minimal RH theorem is therefore

\[
\boxed{
\rho(z)\ne-1
\qquad(\operatorname{Im}z\ne0).
}
\]

This is a one-value omission theorem, not intrinsically a positivity theorem.

## 3. Hermite--Biehler was stronger than required

For `Im(z)>0`, the previously proposed Hermite--Biehler gate is

\[
|F(-z)|>|F(z)|,
\]

or equivalently

\[
|\rho(z)|>1.
\]

This certainly excludes `rho=-1`, but it excludes the entire closed unit
disk.  RH excludes only one projective value.  Hence

\[
\boxed{
\text{Hermite--Biehler orientation}
\Longrightarrow
\text{projective faithfulness}
\Longleftrightarrow
\text{RH},
}
\]

while the reverse implication to Hermite--Biehler is not established and
should not be assumed for this canonical half-source `F`.

This matters strategically.  Failure of the radial-score inequality or of
the full amplitude inequality would falsify that sufficient route, not RH.
Those inequalities may be attempting to orient far more of projective space
than the zero theorem requires.

## 4. Meaning loss as an incidence event

The scale of `C(z)` is irrelevant to cancellation, so the natural Carrier is
the projective curve

\[
\widehat{\mathcal C}(z)=[F(z):F(-z)]\in\mathbb{CP}^1.
\]

The scalar projection has one destructive divisor,

\[
\mathfrak D=[1:-1].
\]

Then

\[
X(z)=0
\quad\Longleftrightarrow\quad
\widehat{\mathcal C}(z)=\mathfrak D.
\]

In these terms the conjecture is

\[
\boxed{
\widehat{\mathcal C}^{-1}(\mathfrak D)\subseteq\mathbb R.
}
\]

This separates three structures that had been conflated:

1. the full theta Carrier `C`, which remains defined;
2. the projective relative-sheet meaning `C-hat`, which remains defined
   unless both sheets vanish;
3. the scalar readout `X`, whose amplitude and phase disappear at destructive
   incidence.

Thus “meaning loss” is precisely typed: it is loss of the scalar sum channel,
not annihilation of the source object.

## 5. The new minimal attack

The ratio obeys the exact integral equation

\[
\rho(z)
=\frac{\int_0^\infty\Phi(u)e^{-izu}\,du}
       {\int_0^\infty\Phi(u)e^{izu}\,du}.
\]

The next source theorem should explain why this meromorphic projective curve
cannot hit `-1` in the upper half-plane.  There are three strictly weaker
possibilities than Hermite--Biehler positivity:

1. a winding theorem showing that `rho+1` has no interior winding;
2. a modular homotopy retracting the upper-half-plane image away from `-1`;
3. a source-derived invariant curve or slit in `CP^1` separating the image
   from the destructive divisor without separating it from the whole unit
   disk.

The sharp falsifier for any proposed mechanism is an admissible positive
even source with all claimed modular properties whose ratio reaches `-1`
off the real axis.

## 6. Cayley chart and the residue warning

The Cayley coordinate

\[
m(z)=i\frac{1-\rho(z)}{1+\rho(z)}
\]

has poles exactly at zeros of `X`.  A Herglotz theorem for `m` would force
those poles to the real axis and would therefore prove RH.  But Herglotz
positivity also fixes the signs of residues and is again stronger than mere
real-pole localization.

Accordingly, positivity remains a valuable explanatory certificate, but it
must now be labelled correctly:

\[
\boxed{
\text{positivity is one possible orientation of semantic faithfulness,
not the definition of semantic faithfulness.}
}
\]

## 7. Scope

The projective-incidence formulation is exactly equivalent to the real-zero
statement, apart from removable points where numerator and denominator of
`rho` vanish simultaneously; those must be handled through the homogeneous
Carrier `C` rather than the affine ratio.  No value-omission theorem has yet
been proved, and RH is not proved.

## 8. Coherent meaning is a holomorphic logarithm

The phrase “the scalar readout retains meaning” has an exact analytic form.
On a simply connected domain, a nonvanishing holomorphic function admits a
holomorphic logarithm.  Therefore

\[
X(z)=e^{L_+(z)}
\qquad(\operatorname{Im}z>0)
\]

for some holomorphic `L_+` if and only if `X` has no zero in the upper half
plane.  Reality supplies the corresponding lower-half-plane logarithm.
Consequently

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\text{the completed scalar readout has a coherent holomorphic logarithm
on each open spectral half-plane.}
}
\]

The real axis is their common symmetry boundary.  At a boundary zero the
amplitude vanishes and the phase cannot be continued through the point, but
neither open chamber acquires an interior defect.

Equivalently, the logarithmic connection

\[
\omega=\frac{X'(z)}{X(z)}\,dz
\]

is holomorphic and exact in each open chamber.  An off-axis zero of
multiplicity `m` creates a residue `m` and the argument-principle charge

\[
\frac{1}{2\pi i}\oint\omega=m.
\]

Thus the zero-line statement can be read as localization of every phase
defect on the fixed boundary, rather than confinement of pre-existing
spectral particles to a line.

## 9. Revised explanatory target

Hermite--Biehler theory supplies a positive metric that would trivialize the
phase bundle, but a metric is more structure than a trivialization.  The
minimal source-derived theorem may instead be:

\[
\boxed{
\text{modular sewing constructs a zero-charge phase trivialization of
the projected theta Carrier in each open chamber.}
}
\]

This changes what should be sought in the theta identities.  A successful
identity need not make the amplitude difference positive everywhere.  It
may instead produce:

1. a nonvanishing modular transition function for the scalar sum channel;
2. a homotopy of the projective image avoiding `[1:-1]`;
3. an exact logarithmic primitive whose seam discontinuity is supported only
   on the real axis; or
4. a conserved winding number that vanishes in the primitive tail and cannot
   change before reaching the fixed boundary.

These are semantic-faithfulness certificates.  Positivity is one possible
way to construct them, not the only one.
