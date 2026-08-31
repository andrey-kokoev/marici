# RH G1.4 prime diagonality is exact on the retained labelled carrier

## Question

Does the completed first-Adams Green carrier contain cross-prime blocks, or
must they merely satisfy an off-diagonal bound?

## Source idempotents

The arithmetic source is the labelled projective direct sum

\[
E=\bigoplus_pE_p,
\qquad
E_p=E_{p,12}\oplus E_{p,\ge3}.
\]

Let \(P_p\) be the prime idempotent and \(P_{p,k}\) the finer grade
idempotent.  These are source coordinates, not decompositions inferred from
analytic orthogonality.

The completed history incidence satisfies the exact relation

\[
P_{q,\ell}\mathcal I P_{p,k}
=\delta_{pq}\delta_{\ell k}\mathcal I_{p,k}.
\]

The window, cut-atom, wall, causal-history, and Wronskian target spaces are all
formed as corresponding labelled direct sums before any scalar evaluator.

## Componentwise diagonality

Each retained component commutes with prime projections:

\[
AP_p=P_pA,
\qquad
CP_p=P_pC,
\qquad
HP_p=P_pH,
\qquad
R_{\ge3}P_p=P_pR_{\ge3}.
\]

The connected return has the corrected target

\[
R_{\ge3}e_{p,k}=\kappa_p^{(k)}j_p,
\]

where \(j_p\) is the Wronskian generator in the \(p\)-fibre.  It does not land
in one common unlabelled line.

The lawful Wronskian codiagonal is fibrewise:

\[
\kappa_p^{(\le2)}j_p
\oplus
\kappa_p^{(\ge3)}j_p
\longmapsto
\kappa_pj_p.
\]

It sums grades at fixed \(p\) only.  Consequently it preserves every prime
idempotent.

## Green form

On the retained graph

\[
\mathcal Jx=(x,Ax,Cx),
\]

the positive form is a direct sum

\[
G=\bigoplus_pG_p.
\]

For \(p\ne q\),

\[
G(P_px,P_qy)=0.
\]

The same statement holds for the bounded ordered linking polarization because
its wall and Wronskian coordinates remain prime-labelled until the terminal
evaluator.  Thus the off-diagonal kernel is exactly zero; no Schur or
Hilbert--Schmidt estimate is needed.

## Within-prime grade mixing

Prime diagonality does not imply grade diagonality.  The primitive and square
windows at one prime have a nonzero Gram overlap, and the fibrewise Wronskian
codiagonal may combine their output with the connected return.  These are
blocks inside \(G_p\), not cross-prime terms.

Retaining \(E_{p,12}\oplus E_{p,\ge3}\) through the quadratic construction
preserves the provenance of those within-prime terms even when a later output
coordinate sums them.

## Terminal scalar evaluator

A later arithmetic evaluator may apply

\[
\varepsilon((z_p)_p)=\sum_pz_p.
\]

Its scalar square contains products with \(p\ne q\).  Those terms belong to the
terminal readout polarization, not to the G1 completed Green carrier.  Moving
\(\varepsilon\) before the Green form would erase prime labels and contradict
the declared construction order.

Likewise, placing translated theta atoms from different primes in one
unlabelled \(L^2\) space would create analytic overlap.  The source
construction instead uses transported labelled fibres; equal ambient formulas
do not authorize forgetting their idempotents.

## Cutoff naturality

For the finite prime cutoff

\[
P_X=\sum_{p\le X}P_p,
\]

all retained maps commute with \(P_X\), and

\[
G(P_Xx,P_Xy)=\sum_{p\le X}G_p(x_p,y_p).
\]

The connected return converges absolutely, while the projective source and
history incidences converge in every declared Köthe rung.  No cutoff-dependent
renormalization is introduced.

## Hostile alternatives

Prime diagonality fails if any of the following changes are made:

1. replace \(j_p\) by one common Wronskian generator before polarization;
2. apply the terminal scalar evaluator before forming the Green form;
3. erase source idempotents because translated analytic formulas inhabit an
   isomorphic ambient function space;
4. recompute local normalizations as the prime cutoff changes.

None is part of the selected retained constructor.

## Disposition

On the source-retained labelled architecture, G1.4 is exact:

\[
P_qGP_p=0
\qquad(p\ne q).
\]

The completed off-diagonal bound is therefore zero.  Prime and grade cutoffs
are natural, and the only codiagonal used inside G1 is grade aggregation within
one fixed prime fibre.

This makes G1.4 a closure candidate together with G1.1--G1.3.  It does not
control cross-prime terms created by a later scalar evaluator and does not
establish G2--G4 or RH.
