# The `B`-charge sector bridge is blind to three-cycle orientation so complex control needs a second port

Owner: `marici.Kitaev`

## Bounded question

Can the compensating `B`-charge reference that connects the two native qutrit
sectors also supply the missing cube-root complex orientation by winding its
transfer path around a three-cycle flux?

No. `B` is the sign representation. Its monodromy is minus one around a
transposition and plus one around a three-cycle. It detects the real `C2`
parity of flux but is completely blind to the orientation of the `C3`
centralizer.

The standard electric charge `C` does respond to a three-cycle, but its
unresolved action is a real two-dimensional rotation with conjugate
eigenvalues `omega` and `omega` conjugate. A complex phase appears only after
an oriented eigenchannel or dyon character is selected. Sector connectivity
and complex orientation are therefore two independently typed ports.

## Claim boundary

The monodromy and character calculations are exact for the untwisted quantum
double of `S3`, up to the conventional choice of clockwise versus
counterclockwise winding, which exchanges a three-cycle with its inverse.

The result rules out obtaining cube-root orientation from `B` monodromy alone.
It does not rule out a more elaborate dyon-assisted charged bridge whose
microscopic path couples an independent `C3` character to the multiplicity
qutrit. Such a coupling must be derived rather than inferred from charge
transfer.

## Electric representations

Let `tau` be a transposition and `rho` a three-cycle. The three irreducible
electric representations have characters

\[
\chi_A(\tau)=1,
\qquad
\chi_A(\rho)=1,
\]

\[
\chi_B(\tau)=-1,
\qquad
\chi_B(\rho)=1,
\]

and

\[
\chi_C(\tau)=0,
\qquad
\chi_C(\rho)=-1.
\]

Their dimensions are one, one, and two.

For a pure electric charge with representation `pi`, a complete winding around
a flux representative `g` acts on the charge space by `pi(g)`, with `g`
replaced by its inverse under orientation reversal.

## The sign bridge sees only real parity

For `B`, the charge space is one-dimensional and

\[
\pi_B(\tau)=-1,
\qquad
\pi_B(\rho)=+1.
\]

Thus two `B`-transfer routes that differ by one winding around a transposition
flux can acquire a relative sign. Two routes that differ only by winding
around a three-cycle flux acquire no relative phase at all.

In particular, replacing `rho` by `rho` inverse changes nothing:

\[
\pi_B(\rho^{-1})=1.
\]

The `B` bridge cannot distinguish clockwise from counterclockwise
three-cycle orientation and cannot select `omega` versus its conjugate.

## The standard charge sees a real rotation

Choose a real basis for the standard representation. One may take

\[
\pi_C(\tau)
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\]

and

\[
\pi_C(\rho)
=
\begin{pmatrix}
-1/2&-\sqrt3/2\\
\sqrt3/2&-1/2
\end{pmatrix}.
\]

The three-cycle action is a real rotation through `2 pi/3`. After
complexification its eigenvalues are

\[
\omega,
\qquad
\overline\omega,
\qquad
\omega=e^{2\pi i/3}.
\]

Complex conjugation exchanges the two eigenspaces. The unresolved real
two-dimensional transport preserves the common real structure even though
its complex eigenvalues are nonreal.

Therefore the statement that `C` sees cube roots is not yet a complex
constructor. One must coherently resolve and orient the conjugate eigenchannels.

## Central Wilson shadows remain real

The normalized central charge--flux readouts are character averages. For the
sign charge,

\[
W_B(\tau)=-1,
\qquad
W_B(\rho)=1.
\]

For the standard charge,

\[
W_C(\tau)=0,
\qquad
W_C(\rho)=-\frac12.
\]

The latter value is the average

\[
-\frac12
=
\frac{\omega+\overline\omega}{2}.
\]

Thus the central scalar probe combines the two oriented cube-root channels
into one real shadow. It confirms nontrivial three-cycle response while
discarding the orientation needed for complex control.

## Oriented eigenchannel projectors

Over the complexified `C` charge space, define projectors

\[
P_\omega,
\qquad
P_{\overline\omega}
\]

onto the two three-cycle eigenlines. They obey

\[
\pi_C(\rho)
=
\omega P_\omega
+
\overline\omega P_{\overline\omega}.
\]

The real structure exchanges them:

\[
K P_\omega K=P_{\overline\omega}.
\]

An unresolved winding retains both projectors and remains real. Selecting one
projector, or comparing the two with a signed orientation, breaks the real
structure. That selection is an additional physical measurement or reference
port.

The three-cycle dyons `G` and `H` supply precisely the conjugate centralizer
characters. Their twists and resolved path phases can label the two
eigenchannels, conditional on a controlled path comparison and a fixed
orientation convention.

## Two-port necessity theorem

Consider a native sector-hopping protocol whose only charged reference is `B`
and whose flux dependence enters only through monodromy of that `B` charge.
Every monodromy coefficient belongs to

\[
\{+1,-1\}.
\]

All remaining pure-electric fusion and measurement constructors preserve the
common real structure. Their compositions therefore remain real. Such a
protocol cannot generate a non-projectively-real qutrit holonomy.

Hence a complex native controller needs at least two distinct coefficient
ports:

1. an invertible `B`-charge port that balances total charge and connects the
   total-`A` and total-`B` qutrit sectors;
2. an oriented `C3` character port that distinguishes `omega` from its
   conjugate.

The first supplies connectivity. The second supplies complex orientation.
Neither factors through the other.

## Why a `C`-charge bus is not an immediate replacement

One might replace the invertible `B` reference by a `C` charge because `C`
responds to three-cycle flux. This changes the problem rather than solving it.

- `C` has dimension two and is not invertible.
- Its fusion can branch into `A`, `B`, and `C`.
- An unresolved `C` bus carries a real two-dimensional rotation.
- Resolving one cube-root eigenline introduces an oriented complex reference.
- A mobile `C` bus can spread one fault across every qutrit share it visits.

Any `C`-bus proposal must type its internal eigenchannel, fusion leakage,
reference return, and fault propagation. It cannot inherit the clean torsor
role of the invertible sign charge for free.

## Revised charged-route architecture

The smallest plausible complex sector-hopping constructor now has three
layers.

### Relational sign transport

Use the `B` reference to connect the two qutrit sectors while conserving one
fixed global charge.

### Oriented three-cycle interferometer

Use a `G`/`H` dyon, an oriented `C` eigenchannel, or an equivalent boundary
reference to produce a controlled distinction between the conjugate
cube-root phases.

### Multiplicity coupling

Derive a physical interaction that makes the oriented phase act
nontrivially on the qutrit bridge coordinate `R`, rather than only as a global
phase on an ancillary path.

The third layer is essential. Possessing both references side by side does
not imply phase kickback into the qutrit.

## Minimal coupling equation

Let the oriented port have basis labels `plus` and `minus`, carrying phases
`omega` and its conjugate. A useful controlled route must induce qutrit bridge
matrices

\[
R_+,
\qquad
R_-.
\]

Complex orientation reaches the logical carrier only if

\[
R_-^*R_+
\]

is not projectively real or otherwise enlarges the admitted logical group.

If

\[
R_+=\omega X,
\qquad
R_-=\overline\omega X
\]

for one common bridge `X`, then the relative route is a scalar cube-root
phase. It is observable only inside a further coherent path comparison and
does not by itself change a projective qutrit state.

A nontrivial qutrit gate requires the orientation to couple differently to
the multiplicity coordinates, or to be injected through an ancillary
measurement protocol whose branch corrections are typed.

## Fault and reference separation

The two ports have different common-mode faults.

- A sign-reference fault exchanges or mislabels the total-`A` and total-`B`
  sector frame.
- A three-cycle-orientation fault conjugates `omega` and its conjugate while
  leaving all pure-electric data real.
- A coupling fault preserves both reference labels but applies the wrong
  qutrit bridge matrix.

One diagnostic bit cannot be assumed faithful on all three fault families.
They belong to separate coordinates of the constructor packet.

## Exact falsifiers

- The sign representation is assigned a cube-root value on a three-cycle.
- Clockwise and counterclockwise three-cycle winding are distinguished by `B`
  monodromy.
- The real standard-representation rotation is called an oriented complex
  eigenchannel without resolving its conjugate pair.
- The central `C` Wilson value `-1/2` is promoted to either `omega` branch.
- A `B`-only sector bridge is claimed to break the pure-electric real
  structure.
- A noninvertible `C` bus is substituted for the `B` torsor without fusion and
  leakage typing.
- A dyon twist acting only as a global path phase is called a projective
  qutrit gate.
- Possession of separate `B` and `G/H` references is claimed to imply a
  coupling between them.
- The conjugate orientation is fixed using only pure-electric probes.
- Sign-frame, orientation-frame, and multiplicity-coupling faults are merged
  into one syndrome coordinate without a joint-faithfulness proof.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies independent ports, route winding, unresolved
versus resolved channels, coupling incidence, reference faults, and the
separation of connectivity from orientation.

The quantum coefficient lens supplies `S3` characters, charge--flux
monodromy, real representation forms, cube-root eigenchannels, dyon
centralizer characters, Wilson traces, and projective phase kickback.

## Disposition

The previous proposal is now sharpened. A `B`-charge reference is the minimal
invertible resource for connecting the two native qutrit sectors, but its
three-cycle monodromy is trivial. It cannot also serve as the complex
orientation reference.

The native controller requires a second, oriented `C3` character port and an
explicit coupling that transports its conjugate-phase distinction into the
qutrit multiplicity holonomy. The best source target is therefore not merely
two `B`-transfer paths, but a relational `B` sector bridge crossed with a
controlled `G/H` or oriented-`C` interferometer, followed by the three-SIC-line
closure audit.

No build, checker, or Git operation was run for this research-only packet.
