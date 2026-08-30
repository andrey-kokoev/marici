# Bilateral Completion Leaves One Antisymmetric Tail Fiber

## Exact three-cell decomposition

Let (\Phi) be the even completed source. For (D\ge0), split its exponentially tilted full-line autocorrelation into three source-defined cells:

\[
P_y(D)
=\int_0^\infty
\Phi(v+D)\Phi(v)e^{y(2v+D)}\,dv,
\]

\[
Q_y(D)
=\int_0^\infty
\Phi(v+D)\Phi(v)e^{-y(2v+D)}\,dv,
\]

and the straddling-seam cell

\[
M_y(D)
=\int_0^D
\Phi(r)\Phi(D-r)e^{y(2r-D)}\,dr.
\]

Splitting the full integration line at (-D) and (0) gives

\[
A_y(D)=P_y(D)+Q_y(D)+M_y(D).
\]

The seam cell is reciprocal-even: changing (y) to (-y) and then (r) to (D-r) leaves it fixed.

## The rank defect

The full autocorrelation and the moving seam determine

\[
P_y+Q_y=A_y-M_y.
\]

But the Krein separation density is

\[
\rho_y=P_y-Q_y.
\]

As a linear observation of the three cells (P,Q,M), the pair (A,M) has rank two and kernel

\[
\operatorname{span}\{(1,-1,0)\}.
\]

That kernel is exactly the Krein channel. Bilateral completion and explicit seam retention therefore still leave one unresolved antisymmetric tail fiber.

## Meaning of the additional comparison channel

The missing channel is not another copy of the seam and not another scalar positivity test. It must detect the orientation of the two reciprocal tails before they are summed. Equivalently, it must be odd under their exchange.

This supplies a precise answer to the proposed extra-wall intuition. The existing objects provide:

1. the positive tail cell;
2. the reciprocal tail cell;
3. the moving seam cell;
4. their completed scalar sum.

The unresolved fifth datum is the oriented comparison between the two tails. The physical Krein readout is a compression of that datum, but using the readout itself as the missing port would be circular. A successful construction must derive an odd comparison current independently from labelled theta/Tate transport.

Candidates include the primitive boundary current, the prime-square current, or an oriented Mellin-scale flux. Their eligibility is determined by one test: under reciprocal sheet exchange they must reverse sign, while the completed sum and seam cell remain invariant.

## Falsifier

Any proposed global completion carrying only (A_y,M_y), or any collection of reciprocal-even functions of them, cannot determine (\rho_y). Two packets shifted by opposite multiples of (1,-1,0) have identical completed and seam data but different Krein orientation.

The cheapest next calculation is therefore not another scalar transform. It is the sheet parity and boundary incidence of each source-authorized current. If none supplies an independent odd coordinate, the present completion is provably unfaithful to the RH-bearing comparison.

## Verification

The exact symbolic checker `research/grothendieck/checkers/bilateral_tail_seam_rank_defect.py` verifies the decomposition matrix, its rank-two observation, its one-dimensional antisymmetric kernel, and the nontrivial action of the Krein functional on that kernel. It writes `research/grothendieck/results/bilateral_tail_seam_rank_defect.json`.
