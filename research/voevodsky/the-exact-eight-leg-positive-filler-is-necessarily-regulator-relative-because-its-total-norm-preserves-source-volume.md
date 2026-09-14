# The exact eight-leg positive filler is necessarily regulator-relative because its total norm preserves source volume

## Isometric four-leg feature

For Tate and reference projections, the four-leg relative feature is

\[
\Psi_Lx
=
\frac1{\sqrt2}
(Q_L^Tx,
(I-Q_L^T)x,
Q_L^0x,
(I-Q_L^0)x).
\]

Its ordinary positive Gram is exactly

\[
\boxed{
\Psi_L^*\Psi_L
=I.
}
\]

Thus

\[
\boxed{
\|\Psi_Lx\|
=
\|x\|.
}
\]

The relative Tate information appears only in the signed readout, not in a reduction of total positive norm.

## Eight-leg norm

The ordered-product feature is

\[
\Theta_L(g)
=
\frac1{\sqrt2}
(\Psi_L(PA_g),
\Psi_L(A_g)).
\]

Therefore

\[
\boxed{
\|\Theta_L(g)\|^2
=
\frac12
\left(
\|PA_g\|^2
+
\|A_g\|^2
\right).
}
\]

At finite outer regulator `Z_R`, this becomes

\[
\boxed{
\|\Theta_{L,R}(g)\|^2
=
\frac12
\left(
\|PZ_RA_g\|_{HS}^2
+
\|Z_RA_g\|_{HS}^2
\right)
}
\]

up to the exact inherited left/right regulator placement.

## Divergent source volume

On the noncompact semilocal carrier, a nonzero scaling-convolution observer is not Hilbert--Schmidt without physical/outer localization. Typically

\[
\|Z_RA_g\|_{HS}^2
\to\infty
\]

as the regulator exhausts the carrier.

Consequently

\[
\boxed{
\|\Theta_{L,R}(g)\|
\to\infty.
}
\]

No cancellation is possible in the ordinary positive norm because all eight legs are summed with positive signs.

## No strong Hilbert limit

Suppose the finite regulated feature spaces are embedded isometrically into one Hilbert space `K`. If

\[
\Theta_{L,R}(g)
\]

converged strongly as `R->infinity`, its norms would remain bounded and converge.

Since the norms diverge,

\[
\boxed{
\Theta_{L,R}(g)
\text{ has no strong Hilbert-space limit}
}
\]

for every observer with divergent source volume.

This obstruction is independent of the Tate gamma phase.

## Dyadic refinement cannot repair divergence

Every dyadic/Halmos refinement map is an isometry:

\[
R_n^*R_n=I.
\]

Hence

\[
\boxed{
\|R_n\Theta_{L,R}(g)\|
=
\|\Theta_{L,R}(g)\|.
}
\]

Increasing defect depth only redistributes positive mass among atom and angle slots. It cannot remove source-volume divergence.

Therefore the countable filtered refinement also has no ordinary strong limit after regulator removal.

## Signed readout remains finite

The signed involution satisfies

\[
\Theta_{L,R}^*
K_8
\Theta_{L,R}
=
\frac12
(P\Delta Q_L+
\Delta Q_LP)
\]

in the regulated carrier. Common positive source-volume contributions cancel only after applying `K_8`.

Under the trace-class and placement arguments,

\[
\boxed{
\langle
\Theta_{L,R}(h),
K_8
\Theta_{L,R}(g)
\rangle
\longrightarrow
W_S(g*h^*).
}
\]

Thus signed matrix coefficients can converge while ordinary feature norms diverge.

This is a standard relative/Krein phenomenon, not a contradiction.

## Correct limiting object

The positive feature should be retained as a regulator-indexed family

\[
\boxed{
\{\Theta_{L,R,N,n,F}\}
}
\]

with:

- isometric depth refinements;
- conductor restrictions;
- exact finite-regulator positive Grams;
- convergent signed boundary readouts.

Its limit is naturally a pro-Hilbert, correspondence, or relative-Krein object. It is not one vector in an ordinary Hilbert direct limit with finite norm.

## Why an ordinary Hilbert direct limit does not help

An inductive limit of isometric feature spaces preserves each finite norm. It does not renormalize a family whose norm increases with the outer regulator.

If outer-regulator inclusions send

\[
Z_RA_g
\mapsto
Z_{R'}A_g,
\]

they are not isometries on the observer-generated vectors because the later vector contains additional orthogonal volume mass.

Thus outer-regulator direction is not the same kind of inductive system as dyadic depth.

It must be represented by source-labelled correspondences or by a quotient removing a common volume module.

## Non-isometric routes to a finite positive boundary

There are three possible routes:

### Common-submodule quotient

Identify an actual common positive bulk feature in Tate and reference rows and quotient/remove it before taking the limit.

### Jordan minimalization

Pass from the eight-leg dilation to the minimal two-polarity feature

\[
(A_{S,+}^{1/2},
A_{S,-}^{1/2}).
\]

This is finite on the graph domain but the minimalization map from raw regulated rows is not generally bounded uniformly in the regulator.

### Relative Hilbert module

Retain the common infinite volume as a shared module and define only relative norms/readouts. Positivity then lives in each finite regulator, while the limit is relative rather than an ordinary vector norm.

None is achieved merely by adding more dyadic nodes.

## Minimalization obstruction

The eight-leg feature has total Gram `I` on the source carrier, whereas the minimal Tate boundary has positive Gram `|A_S|`.

A bounded source-label-preserving map from the former to the latter would require Douglas domination

\[
\boxed{
|A_S|
\preceq
CI.
}
\]

But the Tate logarithmic derivative is unbounded in spectral frequency and/or conductor. Therefore no bounded global minimalization exists on the Plancherel carrier.

Minimalization is necessarily:

- graph-domain valued;
- conductor filtered;
- or unbounded.

## Relation to positive arithmetic claims

The existence of a positive eight-leg dilation is unconditional projection algebra. It does not imply that the Weil form itself is positive.

The signed readout uses a fundamental symmetry with both signs. Weil positivity would require the negative minimal leg to vanish on the admitted global source domain, a much stronger arithmetic statement.

Hence the regulator-relative positive filler does not conceal a proof of RH.

## Revised convergence vocabulary

The following statements must be distinguished:

1. **finite positivity:** every regulated feature has an ordinary positive Gram;
2. **depth coherence:** dyadic refinements are exact isometries;
3. **signed boundary convergence:** `K_8` matrix coefficients converge to `W_S`;
4. **strong positive-leg convergence:** raw feature vectors converge in Hilbert norm.

The first three are viable/established under the declared analytic hypotheses. The fourth is false for raw eight-leg features with divergent source volume.

## Categorical consequence

The positive `C_34` filler is a filtered relative realization:

\[
\boxed{
\text{finite positive features}
+
\text{strict internal refinements}
+
\text{convergent signed readout}.
}
\]

It is not an ordinary finite-energy terminal feature.

At the simplicial level, outer-regulator arrows must remain pro-arrows/spans. Depth arrows can remain genuine isometries.

## Acceptance test for a stronger result

Any claim of strong positive boundary convergence must exhibit a modified residual feature `widehat Theta_(L,R)` satisfying:

\[
\sup_R
\|\widehat\Theta_{L,R}(g)\|<\infty
\]

on a declared dense core, together with:

1. a source-derived common-bulk projection or quotient;
2. compatibility with the signed readout;
3. cutoff/conductor transition maps;
4. identification of its limiting Gram with a positive closed form.

Without such a construction, norm convergence is ruled out by the exact isometry calculation.

## Disposition

The exact positive dilation preserves total source volume:

\[
\boxed{
\Psi_L^*\Psi_L=I,
\qquad
\|\Theta_{L,R}(g)\|^2
\ge
\frac12
\|Z_RA_g\|_{HS}^2.
}
\]

Therefore raw positive boundary legs diverge with the outer regulator. The completed object is necessarily regulator-relative/pro-Hilbert unless a non-isometric common-bulk removal or graph-domain minimalization is supplied. Signed `C_34` convergence remains compatible with this divergence.
