# Two conjugate cube-root dark tests certify clean return only under a shared-branch model

Owner: `marici.Kitaev`

## Bounded question

Can the `G`-dyon relation

\[
1+\omega+\omega^2=0
\]

make the controlled-twist phase reference self-certifying, without borrowing
an external complex quadrature?

There is an exact conditional theorem. Two conjugate dark-port equations force
three returned environment vectors to be identical. One equation is
insufficient, even against a rank-two hostile return. The two equations audit
one instrument only if both settings act on the same repeatable branch-return
map. Setting-dependent drift or common-mode replacement remains outside the
certificate.

## Frozen three-branch model

Prepare one resolved `G` dyon and a three-valued coherent path register. After
the three path operations close, let the unobserved returned vectors be

\[
\eta_0,\qquad\eta_1,\qquad\eta_2.
\]

These vectors include every motion, ribbon, controller, and environmental
degree of freedom not read at the path output. They need not initially be
equal.

Use the `G` twist to weight the paths by zero, one, and two full twists. A real
equal-amplitude recombination port then has dark amplitude

\[
D_+=\eta_0+\omega\eta_1+\omega^2\eta_2.
\]

The conjugate analysis setting has amplitude

\[
D_-=\eta_0+\omega^2\eta_1+\omega\eta_2.
\]

Vanishing detector probability is equivalent to vanishing of the
corresponding vector, provided the detector is trace-complete over the
unobserved return space.

## Exact two-dark theorem

The pair of conditions

\[
D_+=0,
\qquad
D_-=0
\]

holds exactly when

\[
\eta_0=\eta_1=\eta_2.
\]

Subtracting the two dark equations gives

\[
(\omega-\omega^2)(\eta_1-\eta_2)=0.
\]

Because the two cube roots are distinct, this forces

\[
\eta_1=\eta_2.
\]

Substitution into either equation and use of

\[
\omega+\omega^2=-1
\]

then gives

\[
\eta_0=\eta_1.
\]

The converse is immediate. Thus the two dark tests are exactly the two
nontrivial character rows of the three-point Fourier transform. Their common
kernel is the trivial-character line.

## One dark port admits a rank-two hostile return

One equation has a large kernel. Choose unit vectors `eta_0` and `eta_1` with

\[
\langle\eta_0,\eta_1\rangle={i\over\sqrt3}.
\]

Define

\[
\eta_2=-\omega\eta_0-\omega^2\eta_1.
\]

Then

\[
D_+=0.
\]

Moreover,

\[
\|\eta_2\|^2
=2+2\operatorname{Re}
\left(
\omega\langle\eta_0,\eta_1\rangle
\right)
=1.
\]

Because the overlap has modulus strictly below one, `eta_0` and `eta_1` are
linearly independent. The returned environment Gram matrix therefore has rank
two even though the first dark detector is exactly silent.

This is a stronger falsifier than an unknown scalar phase on one common ray.
One cube-root cancellation can hide genuine which-path information.

## What the theorem certifies

When both equations refer to one frozen branch-return map, their joint
vanishing proves exact clean return:

- no relative environment record survives among the three branches;
- no path-dependent loss survives if the detector includes the loss space;
- the intended cube-root weights remain available as relative phases;
- the reference can supply the second real quadrature required by the electric
  fusion-corridor audit.

A common vector may still carry a common phase, deformation, or environmental
state. Such common-mode data cancel from the relative reference and are
harmless for the quadrature comparison unless they alter later coupling.

## The shared-branch typing gate

The proof compares two linear functionals of the same triple

\[
(\eta_0,\eta_1,\eta_2).
\]

Two experimental settings do not automatically have that type. If their
returned vectors are

\[
(\eta_0^+,\eta_1^+,\eta_2^+)
\]

and

\[
(\eta_0^-,\eta_1^-,\eta_2^-),
\]

then the observed conditions are only

\[
\eta_0^++\omega\eta_1^++\omega^2\eta_2^+=0
\]

and

\[
\eta_0^-+\omega^2\eta_1^-+\omega\eta_2^-=0.
\]

Each triple can independently occupy the kernel of its own row. No equality
of branch returns follows.

Therefore the certificate requires one of the following additional
constructors.

- A stationary repeatable channel theorem identifying the branch-return map
  across the two settings.
- A simultaneous two-copy instrument with a certified common preparation and
  fault model.
- One larger coherent instrument that exposes both character projections of
  one stored branch-return state before it is discarded.

The last option avoids temporal drift but requires coherent storage or copying
of the path-return state. It is not supplied by the modular twist scalar.

## Orientation and common-mode replacement

Replacing every `G` twist by the conjugate `H` twist exchanges the two dark
equations. Joint darkness is unchanged. The certificate therefore remains
valid without choosing ribbon orientation.

That invariance is appropriate for clean-return and Gram-rank certification.
It also means the test cannot decide whether the delivered phase reference is
`omega` or `omega^2`. Signed logical-phase identification still needs a
ribbon-orientation anchor.

A more serious common-mode fault may replace both analysis settings together
with another internally consistent instrument. Dark-port consistency alone
cannot establish that the resulting reference couples to the declared
electric corridor matrix element. The coupling port requires its own typed
test.

## Loss and postselection boundary

If the dark detector observes only a postselected success sector, an
orthogonal loss component can escape both equations. The environment vectors
must therefore live in the complete output dilation, including failure flags,
or the omitted probability must be measured independently.

Conditional darkness plus unreported loss is not clean return.

## Constructor status

The source algebra supplies:

- the exact order-three twist;
- its conjugate under ribbon reversal;
- the two Fourier-character equations;
- the proof that their common kernel is the uniform return line.

The source algebra does not yet supply:

- a local controlled-twist Hamiltonian;
- a real equal-amplitude three-path splitter and recombiner;
- a trace-complete dark detector;
- a shared-branch or stationarity theorem across the conjugate settings;
- a protected coupling from this reference into the electric fusion-qutrit
  tester.

The phase-reference problem has therefore been reduced, not eliminated. Its
new first obstruction is the physical realization of two character projections
on one typed branch-return map.

## Exact falsifiers

- One dark equation claimed to imply clean return.
- The rank-two hostile triple above claimed impossible.
- Dark probabilities from two setting-dependent triples combined as though
  they acted on one triple.
- A postselected detector claimed to exclude unobserved loss.
- Joint darkness claimed to orient `G` versus `H`.
- The modular relation claimed to provide a controlled three-path apparatus.
- A stable reference claimed to prove that its later coupling to the electric
  corridor is correct.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies the branch-return module, character-row
projections, common-kernel test, repeatability gate, and common-mode fault
warning.

The quantum coefficient lens supplies the order-three ribbon phase, the
`G/H` conjugation, the three-point Fourier characters, and the interpretation
of common return as absence of quantum which-path leakage.

## Result

Two conjugate cube-root dark tests are jointly faithful on one three-branch
return packet and exactly certify a common environment vector. One test is
not faithful. The joint theorem does not self-authorize its physical premise:
both dark rows must interrogate the same branch-return map. This exposes the
next constructor cleanly as a shared-state two-character instrument rather
than another scalar twist invariant.

No build or checker was run for this research-only packet.
