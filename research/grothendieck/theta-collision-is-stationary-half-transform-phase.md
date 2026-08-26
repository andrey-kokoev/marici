# Theta collision is stationary half-transform phase

## Bounded question

What invariant does the remaining finite double-zero collision measure, and
which earlier theta transport problem does it recover?

## Half-transform curve

For fixed support length \(L>0\), define

\[
H_L(x)=\int_0^L\Phi(u)e^{ixu}\,du
=C_L(x)+iS_L(x).
\]

The even completed truncation is

\[
X_L(x)=2C_L(x).
\]

Where \(H_L(x)\ne0\), write

\[
H_L(x)=R_L(x)e^{i\theta_L(x)}.
\]

Logarithmic differentiation gives

\[
\theta_L'(x)
=
\operatorname{Im}\frac{H_L'(x)}{H_L(x)}
=
\operatorname{Re}
\frac{\int_0^L u\Phi(u)e^{ixu}\,du}
     {\int_0^L \Phi(u)e^{ixu}\,du}.
\]

## Evaluation at a seam zero

At a real zero of \(X_L\), one has \(C_L(x)=0\).  If \(S_L(x)\ne0\), then

\[
\theta_L'(x)
=
\frac{\int_0^L u\Phi(u)\sin(xu)\,du}
     {\int_0^L \Phi(u)\sin(xu)\,du}.
\]

Also,

\[
X_L'(x)
=-2\int_0^L u\Phi(u)\sin(xu)\,du.
\]

Hence

\[
X_L(x)=X_L'(x)=0
\]

is exactly a stationary imaginary-axis crossing of the oriented curve
\(x\mapsto H_L(x)\), provided the curve does not itself pass through the
origin.

If \(H_L(x)=0\), the phase chart is undefined; this is a separately typed
origin-crossing collision and must be excluded directly.  It cannot be hidden
by division through \(H_L\).

## Minimal transversality theorem

The required theorem is weaker than global phase monotonicity.  It asks only:

1. \(H_L(x)\ne0\) whenever \(C_L(x)=0\);
2. \(\theta_L'(x)\ne0\) at every imaginary-axis crossing;
3. the crossing orientation alternates as required by successive simple real
   zeros; no common sign is asserted.

These conditions imply that every zero of \(X_L\) is simple.  Since the
small-window divisor starts real and no zero can enter from infinity, they
would keep the entire support-flow divisor real.

## Return of the signed-band problem

The numerator and denominator at a crossing are signed sine-band sums:

\[
S_L(x)=\int_0^L\Phi(u)\sin(xu)\,du,
\]

\[
M_L(x)=\int_0^L u\Phi(u)\sin(xu)\,du.
\]

The cosine constraint

\[
\int_0^L\Phi(u)\cos(xu)\,du=0
\]

selects the crossings at which their ratio matters.  Thus the earlier
adjacent-band variation-diminishing programme was not irrelevant; it was
trying to orient this phase velocity before the correct conditional locus had
been isolated.

The new target is substantially weaker than uniform quadrant positivity:
prove that the signed sine measure has nonzero first barycenter only on the
codimension-one cosine-zero locus.

## Positivity is insufficient

A positive source alone does not enforce transversality.  The two-atom source

\[
\mu=\delta_0+\delta_L
\]

has

\[
C(x)=1+\cos(Lx).
\]

At every odd multiple of \(\pi/L\), both \(C\) and \(C'\) vanish.  The
half-transform passes through the origin there.  Smooth positive hostile
approximations can approach the same degeneracy.

Therefore the missing law must distinguish the completed theta density from
generic positive even or positive half-line sources.

## Source-specific opportunity

At a crossing, the required transversality is the conditional inequality

\[
S_L(x)M_L(x)\ne0.
\]

This is invariant under rescaling of \(\Phi\).  It is a paired signed-band
statement: neither the unweighted nor the position-weighted sine sum may lose
orientation whenever the cosine sum vanishes.  Their product need not have one
common sign across successive crossings; simple real zeros normally alternate
crossing direction.

The most economical attack is therefore:

1. partition \([0,L]\) into canonical sine half-period bands;
2. impose the cosine-zero constraint before estimating;
3. transport adjacent negative and positive bands using the exact theta
   density ratio;
4. prove that position weighting strengthens rather than reverses the
   surviving orientation;
5. reject the route at the first band pair where the transported ratio crosses
   its required bound.

## Deutsch--Popper conjecture

For the completed theta source, every imaginary-axis crossing of every finite
half-transform \(H_L\) is source-transverse. Equivalently, on the cosine-zero
locus,

\[
S_L(x)M_L(x)\ne0.
\]

The conjecture is falsified by one explicit \((L,x)\) for which the cosine
integral vanishes and either \(S_L(x)=0\) or \(M_L(x)=0\).

## Result

The remaining RH gate is not an undefined global positivity theorem.  It is
conditional phase transversality of one source-generated half-transform.  Its
algebraic content is the orientation agreement of two signed sine-band sums
on the cosine-zero locus.
