# Cyclic restriction of the spin representation realizes the affine discriminant

> Typing correction: cyclic restriction realizes a regular character grading whose label set has the same cyclic type as the affine cokernel. It does not define an additive map from harmonic state vectors to residue classes, nor does it attach affine lattice pairs to physical states. See `cyclic-restriction-is-a-grading-not-a-state-to-residue-attachment.md`.

## Independently quantized physical lattice

An oriented axis on the celestial sphere selects its rotation stabilizer
\(SO(2)\).  The character lattice of this compact group is

\[
X^*(SO(2))\cong\mathbb Z,
\]

with physical angular-momentum weights \(m\in\mathbb Z\).  This lattice is
quantized independently of the affine magnetic cocircuit.

For the spin-\(s\) representation singled out by the cocircuit calculation,
set

\[
l=2s-1,
\qquad
n=2l+1=4s-1.
\]

The weights of \(\mathcal H_l\) are

\[
-l,-l+1,\ldots,l.
\]

They are \(n\) consecutive integers.

## Minimal cyclic restriction

Restrict the axis rotations to

\[
C_n=\left\langle r_n\right\rangle,
\qquad
r_n=R_{2\pi/n}.
\]

On the weight state \(|l,m\rangle\),

\[
r_n|l,m\rangle
=\exp(2\pi i m/n)|l,m\rangle.
\]

Reduction modulo \(n\) maps the \(n\) consecutive weights bijectively onto
\(\mathbb Z/n\).  Equivalently,

\[
\mathcal H_l\big|_{C_n}
\cong\mathbb C[C_n],
\]

the regular representation: every character occurs exactly once.

This order is forced by a minimality theorem.  If \(N<n\), pigeonhole forces
two of the \(n\) weights to have the same \(C_N\) character.  At \(N=n\), all
weights are separated and all characters occur.  For \(N>n\), the weights
remain separated but the restriction is not regular because some characters
are absent.  Thus \(n\) is the unique minimal complete cyclic observation.

## Exact attachment to the affine frame

The general-spin affine frame is

\[
F_s=
\begin{pmatrix}
2&n\\
3&n
\end{pmatrix},
\qquad n=4s-1.
\]

Define

\[
\ell_s:\mathbb Z^2\longrightarrow\mathbb Z/n,
\qquad
\ell_s(x,y)=3x-2y\pmod n.
\]

It annihilates both affine columns:

\[
\ell_s(2,3)=0,
\qquad
\ell_s(n,n)=n=0\pmod n.
\]

It is surjective because \(\ell_s(1,1)=1\).  Since
\(|\det F_s|=n\), it induces an isomorphism

\[
\overline\ell_s:
\operatorname{coker}F_s
\xrightarrow{\sim}
X^*(SO(2))/nX^*(SO(2)).
\]

The right side is precisely the character-label packet exposed by the
minimal cyclic restriction of \(\mathcal H_{2s-1}\).

## Spin-two result

For \(s=2\),

\[
l=3,qquad n=7,
\]

and

\[
\mathcal H_3\big|_{C_7}\cong\mathbb C[C_7].
\]

The weights \(-3,-2,-1,0,1,2,3\) give all residues modulo seven.  The affine
discriminant coordinate

\[
3x-2y\pmod7
\]

is therefore canonically identified with the seven cyclic rotation
characters once the axis and its orientation are marked.

## Where the missing constructor lives

The missing comparison constructor is the axis-marked cyclic restriction
functor

```text
AxisMarkedCyclicRestriction
  oriented_axis
  spin_s_representation H_(2s-1)
  weight_lattice X*(SO(2))
  minimal_order n=dim H_(2s-1)
  cyclic_subgroup C_n
  affine_frame F_s
  comparison ell_s(x,y)=3x-2y mod n
```

It lives between representation formation and finite phase observation:

```text
spin representation H_(2s-1)
          |
          | restrict along oriented SO(2) -> C_n
          v
regular C_n character packet  <---->  coker(F_s)
          |
          | evaluate generator rotation
          v
U(1) phase
```

The ordered puncture pair or an oriented contour axis supplies the required
axis context.  Without that mark, the construction is not canonical under
the full rotation group; Aspect's authority gate must reject an unmarked
version.

## Physical scope

This does not make the full radiative state space finite.  Continuous
amplitudes in each harmonic mode remain continuous.  What becomes finite is
the angular-momentum character label seen by the minimal cyclic rotation
probe.

Thus the seven is a finite charge/character sector inside continuous
radiation:

- the charge lattice is the independently quantized rotation-weight lattice;
- the quotient is forced by minimal complete observation of one physical
  representation block;
- the comparison with the affine frame has genuine Smith index seven;
- executable realization is conditional on a source-authorized oriented axis
  and rotation operation.

## Remaining authority boundary

The completed puncture and contour constructions provide oriented geometric
axes, and celestial rotations are source symmetries.  A fully operational
claim still requires the apparatus contract to admit the discrete rotation
\(R_{2\pi/7}\) as an executable intervention on the same prepared harmonic
packet.  The mathematical and physical charge-lattice comparison is now
defined; instrument executability remains a separate gate.
