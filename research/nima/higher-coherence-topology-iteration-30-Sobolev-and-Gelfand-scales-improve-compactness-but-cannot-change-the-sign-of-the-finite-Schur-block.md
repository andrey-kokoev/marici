# Higher-coherence topology iteration 30: Sobolev and Gelfand scales improve compactness, but cannot change the sign of the finite Schur block

## Candidate topology

Embed the compact-support core in a scale

\[
\mathcal S
\subset H^{s_1}_{w_1}
\subset H^{0,\log}
\subset H^{-s_1}_{w_1^{-1}}
\subset\mathcal S'.
\]

Choose positive regularity and spatial weights so endpoint traces,
translations, primitive distributions, and the archimedean logarithmic
multiplier are all continuous between adjacent rungs.

The hope is that prime translations become compact or small relative to the
archimedean block on a better-balanced rung.

## Tail improvement

On a fixed support window, the prime contribution is order zero, while the
archimedean symbol grows like `log|u|`. Preconditioning by the positive
archimedean form gives schematically

\[
K_L=A_L^{-1/2}T_{P,L}A_L^{-1/2}.
\]

Because the factors `A_L^(-1/2)` decay at high frequency, localization makes
`K_L` compact under the standard commutator estimates. Stronger Sobolev rungs
can improve its singular-value decay and make endpoint traces finite rank or
compact graph perturbations.

Thus interpolation strengthens the high-frequency reduction from iteration
28 and may improve numerical conditioning of the finite Schur certificate.

## Sign invariance

Let `J:H_1->H_0` be an injective dense comparison between two admissible rungs.
The same quadratic form is transported by congruence:

\[
W_1(f,f)=W_0(Jf,Jf).
\]

If a source-core vector has

\[
W_0(Jf,Jf)<0,
\]

no equivalent Sobolev or interpolation norm makes that value positive.
Topology can alter boundedness, compactness, and the size of estimates; it
cannot change the algebraic sign of the form on a common vector.

In particular, the low-mode Schur complement `S_L` changes coordinates under a
bounded invertible rung comparison but preserves inertia. A negative eigenvalue
cannot be removed by renorming.

## Artificial suppression trap

One may assign large norm to prime-sensitive low modes so their operator norm
looks small. If the positive form itself is not transformed by the same
congruence, this changes the physical Green pairing. If it is transformed
correctly, the negative direction remains negative.

A noninvertible embedding can delete that direction, but then source
faithfulness or density is lost.

## Useful outcome

The Gelfand scale remains valuable for:

- admitting `K_1`, delta, principal-value, and seam traces;
- proving prime translations relatively compact;
- obtaining Schatten estimates for the preconditioned tail;
- approximating the finite Schur block stably;
- separating graph adjoints from rigged transposes.

It does not supply positivity of the finite block.

## Verdict for topology 30

Sobolev/interpolation topology can optimize the analytic realization and make
the infinite tail compact with better quantitative control. Positivity still
reduces to the same finite source form, whose inertia is invariant under every
faithful bounded change of rung.

The next nonredundant topology to test is a weighted Bergman/Fock topology in
the spectral parameter, where entire-function growth and zero distributions
are controlled globally rather than pointwise.