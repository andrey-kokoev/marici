# The C,C,C to C associator has an exact bright-dark interferometer

Owner: `marici.Kitaev`

## Question

What is the smallest source-native experiment in the established electric
sector of `D(S3)` that distinguishes fusion-probability data from a coherent
associator constructor?

The already frozen microscopic `Rep(S3)` fragment supplies the answer. In its
declared trivalent gauge, the total-`C` multiplicity space has left and right
fusion-tree bases indexed by `A,B,C`. The recoupling matrix contains a perfect
bright-dark interference pair. Basis-channel probabilities erase this pair's
relative sign; a coherent superposition exposes it with unit contrast.

## Claim boundary

This packet derives an operational discriminator from the existing exact
electric-sector associator. It does not recompute the Clebsch--Gordan maps,
extend the result to flux or dyon sectors, or prove that the required coherent
preparation, reassociation, and readout have been physically compiled.

The result is therefore a source-derived finite prediction and a specification
for an operational test. It is not yet an executable topological instrument.

## Frozen source frame

Let `A`, `B`, and `C` denote the trivial, sign, and two-dimensional standard
representations of `S3`. The pure-electric charges inside `D(S3)` form the
subcategory `Rep(S3)`, and

\[
C\otimes C=A\oplus B\oplus C.
\]

For total charge `C`, write the orthonormal left-associated fusion paths as

\[
|A_L\rangle,\quad |B_L\rangle,\quad |C_L\rangle
\]

and the right-associated paths as

\[
|A_R\rangle,\quad |B_R\rangle,\quad |C_R\rangle.
\]

The pre-existing microscopic packet fixes every intertwiner sign by requiring
the first nonzero matrix entry to be positive. In that gauge and in channel
order `A,B,C`, its exact overlap matrix is

\[
F_{ef}=\langle e_L|f_R\rangle,
\qquad
F=
\begin{pmatrix}
\frac12&\frac12&\frac1{\sqrt2}\\
-\frac12&-\frac12&\frac1{\sqrt2}\\
\frac1{\sqrt2}&-\frac1{\sqrt2}&0
\end{pmatrix}.
\]

The established symbolic result gives

\[
F^{\mathsf T}F=FF^{\mathsf T}=I_3.
\]

No modular datum is used in this derivation. The matrix came from explicit
overlaps of left- and right-associated Clebsch--Gordan embeddings.

## What basis-channel probabilities retain

Prepare one left channel at a time and measure one right channel at a time.
The resulting probability table is

\[
P_{ef}=|F_{ef}|^2
=
\begin{pmatrix}
\frac14&\frac14&\frac12\\
\frac14&\frac14&\frac12\\
\frac12&\frac12&0
\end{pmatrix}.
\]

For a fixed right output `f`, let

\[
v_f=
\begin{pmatrix}
F_{Af}\\F_{Bf}\\F_{Cf}
\end{pmatrix}.
\]

The corresponding right-channel effect on the left multiplicity space is

\[
E_f=v_fv_f^*.
\]

Basis preparations reveal only the diagonal entries of `E_f`. They do not
reveal the off-diagonal products

\[
F_{ef}\overline{F_{e'f}}.
\]

Those products are exactly the interference data needed to predict a coherent
superposition of fusion routes.

## General two-route fringe theorem

Choose two distinct left channels `e` and `e'` and prepare

\[
|\psi_\phi\rangle
=
\frac{|e_L\rangle+e^{i\phi}|e'_L\rangle}{\sqrt2}.
\]

The probability of the right channel `f` is

\[
p_f(\phi)
=
\frac{|F_{ef}|^2+|F_{e'f}|^2}{2}
+
\operatorname{Re}
\left(
e^{i\phi}F_{ef}\overline{F_{e'f}}
\right).
\]

Thus the basis-channel probability packet fixes the constant term but leaves
the fringe term undetermined. Measurements at two complementary phases recover
the real and imaginary parts of that product. Repeating this for a connected
set of nonzero channel pairs reconstructs every rank-one effect `E_f`.

The family of effects reconstructs each column of `F` up to an independent
right-output phase. That residual freedom is precisely the right trivalent
frame gauge. Recovering a particular matrix representative requires calibrated
open ports; recovering its gauge orbit does not.

## Exact bright-dark witness

For the right channel `C`, the frozen matrix has

\[
v_C=
\begin{pmatrix}
1/\sqrt2\\1/\sqrt2\\0
\end{pmatrix}.
\]

Define

\[
|+_{AB}\rangle
=
\frac{|A_L\rangle+|B_L\rangle}{\sqrt2},
\qquad
|-_{AB}\rangle
=
\frac{|A_L\rangle-|B_L\rangle}{\sqrt2}.
\]

Then

\[
\langle C_R|+_{AB}\rangle=1,
\qquad
\langle C_R|-_{AB}\rangle=0,
\]

and therefore

\[
p_C(+_{AB})=1,
\qquad
p_C(-_{AB})=0.
\]

More generally,

\[
p_C(\phi)
=
\frac{1+\cos\phi}{2}
=
\cos^2\!\left(\frac\phi2\right).
\]

This is a unit-visibility fringe. Separate preparation of `A_L` and `B_L`
gives probability `1/2` in both cases and cannot determine whether their
coherent sum is bright or dark.

## Smallest hostile fixed-frame pair

Let

\[
D=\operatorname{diag}(1,-1,1),
\qquad
F'=DF.
\]

Then

\[
|F'_{ef}|^2=|F_{ef}|^2
\]

for every basis input and output. Yet the same calibrated preparations obey

\[
p'_C(+_{AB})=0,
\qquad
p'_C(-_{AB})=1.
\]

As abstract fusion data, `F` and `F'` differ by a left trivalent gauge change.
They must not be advertised as inequivalent fusion categories. Relative to a
frozen source preparation frame, however, they define different coherent
input-output instruments. The hostile pair proves exactly what the scalar
table fails to specify: the attachment between the abstract gauge orbit and
the calibrated physical ports.

## Three equivalence levels

This finite example separates three notions that have repeatedly been blurred
across the programme.

### Basis-probability equivalence

Two transformations are equivalent when they agree on

\[
|F_{ef}|^2
\]

for the declared basis preparations and basis effects. This relation forgets
all route interference.

### Coherent effect equivalence

Two transformations are equivalent when every right-channel effect agrees on
all coherent left inputs. This reconstructs the projectors

\[
E_f=v_fv_f^*
\]

and therefore the columns up to independent output phases.

### Calibrated constructor equivalence

Two transformations are equivalent when they implement the same coherent map
relative to the frozen preparation and readout frames, including coherent
comparisons between right outputs when those comparisons are admitted.

The first is a scalar diagnostic shadow. The second is an instrument on one
open multiplicity port. The third is the ordered constructor attached to
calibrated source and target interfaces.

## Minimal operational packet

For this real electric fragment, the smallest phase discriminator needs:

1. a verified preparation of `|A_L>`;
2. a verified preparation of `|B_L>`;
3. a coherent relative-phase control producing `|+_{AB}>` and `|-_{AB}>`;
4. a right-tree `C`-channel effect;
5. a nondestructive or repeated-shot record of the right-channel probability;
6. an independent calibration showing that the phase control is not inferred
   from the target associator itself.

The last item prevents circular reconstruction. A mixer whose specification
already assumes `F` is not independent evidence for `F`.

If arbitrary complex associators are admitted, the two real settings are not
enough. Two complementary control phases are then required to recover both
quadratures of each off-diagonal product.

## Source availability versus physical availability

The source theory already provides:

- the charges `A,B,C`;
- the two fusion trees;
- normalized trivalent intertwiners;
- the exact recoupling matrix;
- the predicted bright-dark fringe.

It has not yet provided:

- a localized preparation constructor for coherent `A/B` intermediate paths;
- a physically calibrated phase reference between those paths;
- a reassociation protocol with a fault contract;
- a right-tree channel measurement instrument;
- a proof that these controls preserve the intended topological code space;
- a scaling theorem showing bounded cost and fault spread.

The distinction is structural. Possession of a source-derived `F` matrix gives
a prediction for an executable context. It does not manufacture that context.

## Relation to the constructor-algebra problem

The endpoint-algebra result established associative generation from two
flux-resolved ports. The present experiment tests a different layer: coherent
composition of fusion paths. Even perfect endpoint algebra tomography does not
by itself produce the phase-calibrated reassociation instrument.

Conversely, passing this one electric-sector fringe would not prove control of
the full `D(S3)` endpoint algebra. It would establish one nontrivial arrow from
source categorical data to a coherent operational context.

The natural next extension is not another scalar invariant. It is one mixed
flux or dyon associator in which braiding is genuinely nonsymmetric and the
basepoint or ribbon transport enters the open-channel map.

## Falsifiers

- The frozen channel order or intertwiner gauge differs from the source packet.
- The displayed matrix is not the exact prior microscopic matrix.
- Basis probabilities are claimed to determine a fixed-frame coherent map.
- A row or column gauge change is called a distinct fusion category.
- The bright and dark states are named without a calibrated relative phase.
- The preparation mixer is derived from the target associator and then used as
  independent evidence for that associator.
- A fusion-channel probability is promoted to a coherent process amplitude.
- Passing the electric fringe is promoted to full mixed-sector coherence.
- A source-level matrix is called physically executable without locality,
  nondisturbance, and fault evidence.

## Disposition

The smallest exact phase-sensitive realization test is now specified. In the
frozen electric `Rep(S3)` frame, one coherent `A/B` input pair and one right-`C`
effect produce a perfect bright-dark contrast. The existing basis fusion table
cannot predict which calibrated superposition is bright.

The remaining obstruction has sharpened from missing associator data to a
constructor question: can the source supply an independently calibrated
coherent channel mixer, reassociation operation, and right-tree readout while
preserving the protected sector?

No fresh checker or build was run for this research-only packet. The exact
matrix is inherited from the previously verified microscopic fragment and its
saved result artifact.
