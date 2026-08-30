# Physical parallels separate architecture, spectrum, and orientation

## Status

Research synthesis. It compares the theta/Tate two-sector programme with
established physical and operator-theoretic structures. The correspondences
are diagnostic, not identifications, until source maps are constructed.

## Spectral rotation

Center the functional equation at

\[
z=s-\frac12
\]

and rotate to the frequency variable

\[
\lambda=-iz.
\]

The critical line becomes the real \(\lambda\)-axis. The two \(z\)-half-planes become
the upper and lower spectral half-planes. Reciprocal growth and decay become
the standard off-real-frequency dichotomy.

This rotation makes several physical comparisons exact at the level of
analytic domains, while leaving their dynamics to be derived.

## 1. Lax–Phillips scattering: closest architecture

Lax–Phillips theory starts with a unitary evolution and distinguished incoming
and outgoing subspaces. In translation representations they become half-line
support spaces; Fourier transformation turns the corresponding causal
structure into upper- and lower-half-plane analyticity. The scattering
operator maps the incoming representation to the outgoing one and is unitary
on the real spectral boundary.

The theta/Tate correspondence is:

- direct and reciprocal tails correspond to incoming and outgoing sectors;
- Fourier–Tate sewing corresponds to the scattering operator;
- the critical line corresponds to the real-frequency boundary;
- the boundary-bearing internal state corresponds to the interaction space;
- the scalar completed section corresponds to one transmission amplitude.

This explains why unitarity is insufficient. A lossless scattering device can
have a zero transmission coefficient by destructive interference while its
internal field remains nonzero.

The local Tate ratio is structurally closer to a scattering phase than the
completed zeta section is. The completed scalar behaves more like one matrix
coefficient or characteristic determinant of the full scattering system.

## 2. Transfer matrices and canonical systems: closest energy identity

A one-dimensional transmission line or layered optical medium evolves a
two-component state of right- and left-moving waves. Its transfer matrix
preserves a symplectic or indefinite flux form on the physical frequency
axis. Off that axis, reciprocal singular values describe growing and decaying
evanescent modes.

Canonical systems have the schematic form

\[
JY'=\lambda H(q)Y,
\qquad
H(q)\ge0.
\]

Their Green identity converts the positive bulk form defined by (H) into a
boundary flux relation. This is exactly the shape sought for the doubled
Clark–Green system.

The obstruction is equally exact: constructing a positive canonical
Hamiltonian from the completed scalar kernel would only restate the
Weil/Pick criterion. The Hamiltonian and its boundary supply must be derived
from labelled theta/Tate data before scalar projection.

## 3. Evans functions and Krein signature: closest RH proof shape

In spectral stability theory, a linearized physical system has stable and
unstable solution bundles. The Evans function is an analytic determinant that
vanishes when those bundles intersect, producing a global eigenmode. Zeros in
the unstable half-plane represent dynamical instability; imaginary-axis
zeros represent neutral modes.

After the spectral rotation, RH has the same formal shape:

- the critical line is the neutral axis;
- the two sectors are reciprocal stable and unstable bundles;
- a zeta zero is an intersection or matching mode;
- an off-line zero is an unstable mode.

Krein theory adds the key qualification. A scalar Evans function locates
modes but does not by itself carry their orientation or stability signature.
Krein signature is extra quadratic-form data that determines whether neutral
modes can leave the axis under collision. This mirrors the present result:
the scalar completed section detects cancellations, while the missing
source-derived boundary form must carry orientation.

The precise RH-grade target suggested by this parallel is an Evans–Krein
realization constructed forward from the source, not an Evans determinant
fitted to \(\Xi\).

## 4. Tomita–Takesaki modular theory: closest origin of the half-weight

Given a cyclic and separating vacuum for an operator algebra, Tomita–Takesaki
theory produces a modular operator \(\Delta\) and a conjugation \(J\). The modular
flow \(\Delta^{it}\) is unitary, \(J\) exchanges the algebra with its commutant, and
the half-power \(\Delta^{1/2}\) appears in the polar decomposition of the basic
antilinear involution. Thermal correlation functions acquire analytic strip
structure and reciprocal boundary values.

This resembles:

- the exchange (s\leftrightarrow1-s);
- the structural half-weight (1/2);
- the two reciprocal source sectors;
- unitary motion on the seam;
- and a vacuum state relating both perspectives.

But modular faithfulness does not imply that every vacuum matrix coefficient
is nonzero. A separating vacuum prevents operator annihilation of the vacuum;
it does not prevent orthogonality after transport. Modular theory may explain
the two-sector geometry without proving RH transversality.

## 5. Osterwalder–Schrader reflection positivity: closest orientation model

Euclidean quantum field theory splits configurations into positive- and
negative-time halves. Reflection maps one half to the other. A reflected
sesquilinear form is required to be positive; quotienting its null space and
completing produces the physical Hilbert space and its time evolution.

This is the cleanest physical example in which sewing two halves supplies an
orientation rather than mere symmetry. A theta analogue would require a
source-derived reflected form on the complete labelled Poisson boundary
module.

The analogy has a hard gate. A zero of one scalar readout is not automatically
a null vector of the reflected norm. That bridge must be proved. The known
prime-two hostile also rules out naive local acute-cone positivity, so any
reflection-positive form would need all arithmetic and archimedean channels
coupled globally.

## 6. Schwinger–Keldysh doubling: closest path-accounting model

The closed-time-path formalism carries forward and backward histories
together. Equal histories make the visible closed-loop evolution cancel, but
response, noise, and influence data live in the difference sector. A Keldysh
rotation separates common and difference variables.

This closely matches:

- symmetric and antisymmetric Clark variables;
- endpoint silence with nonzero path energy;
- the Gramian cocycle;
- and dynamic storage plus boundary supply.

Its limitation is conceptual: it uses physical time, whereas the theta flow
parameter is scale. It is a useful accounting architecture, not authority to
interpret scale as time.

## Comparative verdict

No single physical theory supplies the whole RH mechanism.

- Lax–Phillips explains the two analytic sectors and scattering seam.
- Canonical systems explain the desired bulk-to-boundary energy identity.
- Evans/Krein theory explains zeros as neutral or unstable matching modes and
  shows why a scalar determinant lacks orientation.
- Modular theory explains why reciprocal conjugation and a half-weight may be
  structural.
- Reflection positivity models the kind of source law that could create a
  physical positive Hilbert space.
- Schwinger–Keldysh theory explains why endpoint cancellation does not erase
  path information.

The most faithful combined physical picture is a modularly doubled,
boundary-bearing scattering system whose characteristic determinant is an
Evans function and whose source current supplies a Krein or
reflection-positive signature.

## Concrete tests imported from physics

The parallels become useful only through falsifiable constructions:

1. Lax–Phillips test: derive genuine incoming and outgoing subspaces and show
   the source evolution acts by the required semigroups.
2. Canonical-system test: derive the Hamiltonian and Green boundary form
   without using \(\Xi\) or its zeros.
3. Evans test: prove that the source block pencil and the completed scalar
   have the same zero multiplicities under graph completion.
4. Krein test: construct a source quadratic signature that is not recoverable
   from the scalar Evans function alone.
5. Modular test: identify a cyclic separating source vacuum and the actual
   algebra/commutant exchange.
6. Reflection-positivity test: build the reflected form and apply the hostile
   prime and archimedean sources.
7. Keldysh test: verify that the Gramian and boundary supply obey their path
   cocycle laws.

Failure of any source map closes that particular physical interpretation
without affecting the others.

## Sources

- P. Lax and R. Phillips, scattering theory for acoustic equations and the
  incoming/outgoing translation framework:
  https://iumj.org/article/2242/
- M. Takesaki, Tomita modular theory:
  https://www.mathnet.ru/eng/mat725
- K. Osterwalder and R. Schrader, Euclidean Green-function axioms and
  reflection-positive reconstruction:
  https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf
- R. Kollár and P. Miller, Evans functions and Krein signatures:
  https://arxiv.org/abs/1209.3185
- R. Brunetti, D. Guido, and R. Longo, modular localization:
  https://arxiv.org/abs/math-ph/0203021
