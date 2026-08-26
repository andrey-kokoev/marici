# Positivity Improvement Separates Survival from Faithful Observability

## The correction

Positivity improvement is not itself a faithfulness theorem. Let (C\subset V)
be a proper cone and let

\[
\Phi(C\setminus\{0\})\subset\operatorname{int}C.
\]

This guarantees survival of every nonzero positive input under every nonzero
positive dual probe. It does not imply that (\Phi) is injective on (V), or
even on a normalized base of (C).

The smallest hostile is the replacer map on the positive quadrant,

\[
R(x_1,x_2)=(x_1+x_2)(1,1).
\]

Every nonzero positive vector is sent to the cone interior, and the induced
projective map has zero diameter. Nevertheless

\[
R(1,0)=R(0,1),\qquad R(1,-1)=0.
\]

Thus maximal projective mixing can coexist with total loss of normalized-state
distinctions and a nontrivial linear kernel. In operator language, the
trace-and-prepare channel sends every density matrix to one fixed full-rank
state. It is positivity improving but not informationally faithful.

## Three independent completion reserves

A completion argument must type three different quantities.

### Radial gain

For a source-normalized base

\[
B_\rho=\{x\in C:\rho(x)=1\},
\]

define

\[
g(\Phi)=\inf_{x\in B_\rho}\rho(\Phi x).
\]

This prevents the entire positive image from attenuating to zero. Projective
geometry cannot see it: replacing (\Phi) by (\alpha\Phi) leaves every
projective invariant unchanged while multiplying (g) by (\alpha).

### Anchored interior margin

Choose source-derived reference data: an interior order unit (u\), the
normalizing functional (\rho), and their transported dual frame. The margin

\[
\delta(\Phi)=
\inf_{x\in B_\rho}
\inf_{f\in B_u^*} f(\Phi x),
\qquad
B_u^*=\{f\in C^*:f(u)=1\},
\]

measures distance from the boundary in that frame. Raw coordinate minima are
not invariant under an untransported diagonal cone gauge. A valid source
equivalence must transport (C,u,\rho), and the probes together.

### Linear or contextual separation

If the theorem concerns arbitrary amplitude differences rather than merely
survival of positive states, it additionally needs injectivity of the admitted
observation family:

\[
\bigcap_{J\in\mathcal J}\ker(J\Phi)=\{0\}
\]

on the declared state or quotient domain. Neither (g>0), (\delta>0), nor
strict projective contraction implies this condition.

## Projective contraction is not enough

For a strictly positive (2\times2) matrix

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

the projective cross-ratio (ad/(bc)) is unchanged by positive diagonal
conjugation and scalar multiplication. It measures relative mixing, not radial
gain or placement relative to a frozen source frame.

Two exact hostile families separate the missing data:

\[
A_\varepsilon=
\begin{pmatrix}1&1\\ \varepsilon&2\varepsilon\end{pmatrix}
\]

has constant cross-ratio (2), while its normalized image approaches the
boundary of the standard source cone as (\varepsilon\to0). Also

\[
\Phi_N=N^{-1}A
\]

has unchanged projective action but radial gain tending to zero.

Therefore a completion-stable survival theorem needs both an anchored
interior bound and radial gain. A faithfulness theorem needs an additional
kernel-separation bound.

## Consequence for the theta/Tate route

Before positivity improvement can exclude a scalar zero, the source theory
must establish all of the following:

1. the relevant completed state lies in a source-derived proper cone;
2. the arithmetic correspondence preserves and improves that cone before
   trace;
3. the scalar readout is a nonzero positive dual functional in the transported
   source frame;
4. radial gain and anchored interior margin are uniform in the cutoff;
5. if state reconstruction is claimed, the admitted observation family is
   independently jointly separating.

If the theta/Tate amplitude is signed or complex and no ordered real form is
derived, positivity improvement is simply inapplicable. If the cone is chosen
from the desired scalar sign, the argument is circular.

## Falsifiers

- A trace-and-prepare or rank-one replacer channel passes strict positivity but
  erases normalized-state distinctions.
- A projectively fixed family attenuates radially to zero.
- A bounded cross-ratio family approaches the boundary in the frozen source
  frame.
- A diagonal gauge improves the reported margin without transporting the
  unit, trace, and probes.
- Cone membership is assigned after inspecting the scalar zero set.
- Positive-state survival is reported as injectivity on signed or complex
  amplitudes.

## Claim boundary

This is a finite ordered-linear compiler theorem. It neither constructs the
theta/Tate cone nor proves that the RH source state belongs to one. It does not
derive the arithmetic correspondence, a uniform completion estimate, or RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. Coordinate margin, projective mixing, radial gain, linear faithfulness,
and source cone membership were frozen as separate branches. Diagonal gauges,
scalar attenuation, and a rank-one replacer were preregistered hostiles.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Positivity improvement was retyped as a survival theorem rather than a
faithfulness theorem. Projective mixing split from radial gain and anchored
boundary distance, while the replacer hostile proved that all three positivity
notions remain independent of contextual separation. Source cone membership
is the unresolved theorem-changing input.
