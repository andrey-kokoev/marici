# Higher-coherence topology iteration 14: semifinite noncommutative Lp retains local energy, but relative-trace cancellation loses positivity

## Candidate topology

Let `N` be the scaling-group von Neumann algebra with canonical faithful normal
semifinite trace `tau`. Use the measurable-operator spaces

\[
L^p(\mathcal N,\tau),
\qquad 1\le p\le\infty,
\]

or the measure topology on affiliated operators. This retains finite prime
corners while allowing infinite-volume bulk operators and trace-per-unit-volume
limits.

## Positive local residual

Represent the fixed-prime Haar defect by

\[
R_p(z)
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)
|b_z\rangle\langle b_z|.
\]

On a finite trace corner,

\[
\tau(|b_z\rangle\langle b_z|)=E_p(b_z)>0.
\]

Faithfulness gives, in the positive orientation,

\[
\tau(R_p(z))=0
\quad\Longleftrightarrow\quad
R_p(z)=0.
\]

Likewise,

\[
\|R_p(z)\|_{L^1}
=
\left|1-p^{-2\operatorname{Re}z}\right|E_p(b_z).
\]

Thus noncommutative `L^p` topology preserves exactly the local information
that the Calkin quotient discarded. It does not absorb the residual.

## Measure-topology escape

A sequence of projections can converge to zero in measure if their traces tend
to zero. The fixed prime projection does not: its trace is the retained positive
energy. Moving the state among shrinking prime corners would violate the
source label and noncollapse condition. Hence measure convergence gives no new
escape for the compatible fixed-prime class.

## Semifinite bulk subtraction

The canonical Plancherel trace correctly identifies the universal volume term:

\[
\tau(\lambda(g)^*\lambda(g))=\|g\|_2^2.
\]

Connes's finite part is a relative trace

\[
\operatorname{Tr}_{\rm cutoff}
-
\operatorname{vol}_\Lambda\tau.
\]

This subtraction can cancel divergent common bulk contributions and is a
legitimate higher-coherence normalization. But a difference of positive traces
is signed. It need not be positive on squares.

No faithful positive trace can annihilate the identity-volume sector: if
`Tau(I)=0`, faithfulness forces `Tau` to vanish on every bounded positive
element.

## Consequence for repeated cones

Higher cones may successively subtract common semifinite bulk modules while
retaining a finite boundary functional. The remaining boundary value is
precisely where the sign problem lives. Repeating the relative subtraction
does not generate positivity of that finite part.

A positive conclusion would require an additional representation of the
boundary functional as:

- a square;
- a positive index pairing;
- or a spectral-shift integral with controlled sign.

## Verdict for topology 14

Semifinite/noncommutative `L^p` topology is the strongest tested topology for
simultaneously retaining local positive energy and renormalizing infinite bulk
volume. It leaves the Haar residual fully visible. Relative traces can absorb
bulk divergence but not prove boundary positivity.

The next nonredundant topology to test is a spectral-shift/scattering topology,
where the residual may be represented by a signed boundary phase whose sign is
controlled by monotonicity rather than by an ordinary positive trace.