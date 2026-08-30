# The two boundary covectors form a canonical bivector before they form a scalar current

## Replace contraction by exterior comparison

The completed augmentation current \(a\) and primitive current \(b\) both
belong to \(\mathcal S_P'\).  Their inner product is not canonically defined,
but their exterior product is:

\[
\mathcal W=a\wedge b\in\Lambda^2\mathcal S_P'.
\]

For test packets \(x,y\in\mathcal S_P\), its evaluation is

\[
\mathcal W(x,y)
=
a(x)b(y)-a(y)b(x).
\]

Every term is a legitimate test--distribution pairing.  No Hilbert pivot,
heat time, or dual--dual contraction is introduced.

This is the geometrically correct first comparison.  Two same-variance
boundary observations determine an oriented area form, not a scalar metric
contraction.

## The primitive--augmentation bivector is nonzero

On the prime basis, take

\[
a(e_p)=1,
\qquad
b(e_p)=\frac{\log p}{\sqrt p}.
\]

Then

\[
\mathcal W(e_2,e_3)
=
\frac{\log3}{\sqrt3}
-
\frac{\log2}{\sqrt2}.
\]

The function \(\log x/\sqrt x\) is strictly increasing on \((1,e^2)\), so
this value is positive.  Hence the two completed currents are genuinely two
independent boundary directions.  Treating them as one scalar seam defect is
a lossy projection.

## Source covariance

Every source constructor \(C\) acting continuously on the test space induces
the contragredient action \(C^*\) on covectors and therefore

\[
(C^*a)\wedge(C^*b)
=
\Lambda^2(C^*)(a\wedge b).
\]

This functoriality requires no metric.  In particular, the boundary object
can be transported through Adams, Fourier--Tate, and cutoff maps before any
scalar readout is selected.  Orientation reversal is recorded by the sign of
the exterior square rather than inferred from a phase after completion.

## What remains unresolved

The bivector does not by itself prove zero confinement.  A scalar Green law
requires evaluation on a source-derived test two-chain

\[
\chi\in\Lambda^2\mathcal S_P.
\]

Then \(\mathcal W(\chi)\) is canonical only if \(\chi\) is canonical.  The
finite flat-comb/control pair supplies such a two-chain at each cutoff, but
Aspect's escape theorem shows that its flat-comb leg has no state-valued
limit.  Thus scalarization, not formation of the completed boundary object,
is the remaining obstruction.

This retypes the target:

1. construct the completed bivector current \(\mathcal W\);
2. derive its conservation law without scalarizing it;
3. identify a source-authorized test two-cycle or relative fundamental class;
4. evaluate only at the final physical readout.

If no completed test two-cycle exists, the correct theorem may remain
bivector-valued.  A scalar proof that chooses a pivot earlier is then a change
of theory rather than a coordinate choice.

## Relation to the multi-tower picture

The input and response towers are not closed by a fifth scalar wall.  Their
first completed coherence is the exterior comparison tower

\[
\Lambda^2(	ext{boundary covectors}).
\]

The control tower is separately responsible for supplying the test
two-cycle.  This explains why the completed object looked like one seam while
actually containing two irreducible directions: the scalar endpoint was the
evaluation of a two-form, not the primitive object itself.

