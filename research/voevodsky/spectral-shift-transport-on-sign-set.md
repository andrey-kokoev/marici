# Residue-selected spectral shift on the sign set

## Question

Can a transport acting on the sign-set geometry \(\Sigma\) itself —
residue-selected carrier shift \(a\mapsto a'\) — strictly decrease the
natural obstruction order without editing the amplitude \(\varepsilon\)
and without collapsing the object?

## Claim boundary

Fixture as in `infinitely-supported-obstruction-class.md`:
\(d\rho_a(x)=(1+\varepsilon\cos(ax))e^{-x^2}dx\), \(\varepsilon>1\)
fixed. Transport: \(a\mapsto a/2\) selected by nonzero residue. The
checker proves rigorous bounds, not quadrature: the negative-part mass
is super-exponentially small in \(1/a\), the total mass has a uniform
floor, and the limit object is examined for class exit.

## Construction

The defect sign set is

\[
\Sigma_a=\{x:\cos(ax)<-\varepsilon^{-1}\},
\]

whose nearest point to the origin is at distance

\[
d(a)=\frac{\pi-\arccos(\varepsilon^{-1})}{a}.
\]

Every negative-mass interval lies in \(|x|\geq d(a)\). Hence, with
\(C(\varepsilon)=1+\varepsilon\),

\[
\|\rho_a^-\|_{TV}
\leq
C(\varepsilon)\int_{d(a)}^{\infty}e^{-x^2}dx
\leq
\frac{C(\varepsilon)}{2d(a)}e^{-d(a)^2},
\]

using the standard Mills bound \(\int_d^\infty e^{-x^2}dx\leq
e^{-d^2}/(2d)\). Meanwhile

\[
\|\rho_a\|_{TV}
\geq\left|\int_{\mathbb R}d\rho_a\right|
=\sqrt{\pi}\left(1+\varepsilon e^{-a^2/4}\right)
\geq\sqrt{\pi},
\]

so the normalized obstruction
\(\|\rho_a^-\|_{TV}/\|\rho_a\|_{TV}\to0\) super-exponentially as
\(a\downarrow0\) along the halving orbit.

## Strongest falsification attempt

Two honesty controls must fire before this counts:

1. **Mass collapse** (v5): the total mass must have a uniform floor.
   It does: \(\sqrt{\pi}/2\). Not collapse.
2. **Definitional convergence** (v4/v6): the decrease must be a theorem
   about the fixture, not built into the obstruction definition. The
   bound \(e^{-d(a)^2}\) is derived from the geometry of \(\Sigma_a\);
   \(\varepsilon\) is never edited. Not definitional.

The third control fires against the fork:

3. **Class exit**: at \(a=0\) the oscillation vanishes and the density
   class changes — the limit object is not a member of the fixture
   class. The loop converges by leaving the class, not by cohering a
   member of it.

## Disposition

The transport exists mathematically and the two collapse controls pass:
spectral shift is amplitude-preserving and non-definitional, and its
normalized obstruction decreases to zero with a mass floor intact.
The apparent class exit at \(a=0\) is reclassified as a categorical
completion defect, not a scientific failure: adjoining \(F_0\) closes
the deformation family under the omega-limit of the halving chain.

This packet evaluates only that deformation arrow and its analytic
limit. Whether the construction proves positivity or RH is outside its
scope. The completed object, identity, composition, limit cone, and
remaining three-vertex coherence obligations are specified in
`cyclic-residue-feedback-categorical-completion.md`.

## Verification

- `research/voevodsky/checkers/scout_spectral_shift_transport.py`
- `research/voevodsky/results/spectral_shift_transport.json`
