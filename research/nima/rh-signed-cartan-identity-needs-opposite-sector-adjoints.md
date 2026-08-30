# A signed Cartan identity needs opposite sector adjoints

## Positivity obstruction

The proposed Cartan–Clifford identity is

\[
dQ+Qd=aN,
\qquad
a=\Re s-\frac12,
\]

with `N` source-invertible away from the seam.

If the contraction operator is the ordinary Hilbert adjoint

\[
Q=d^*,
\]

then

\[
\langle x,(dd^*+d^*d)x\rangle
=
\lVert d^*x\rVert^2+
\lVert dx\rVert^2
\geq0.
\]

Thus a positive number operator `N` cannot satisfy

\[
dd^*+d^*d=aN
\]

when `a` is negative. One positive Hilbert adjoint cannot realize the signed
normal-displacement law on both half-planes.

## Exact one-even, one-odd witness

Take

\[
d_c=
\begin{pmatrix}
0&c\\
0&0
\end{pmatrix}.
\]

Then

\[
d_cd_c^*+d_c^*d_c=c^2I.
\]

The anticommutator depends on the square of the coefficient and cannot recover
its sign. In particular, `c=1` and `c=-1` produce the same positive Laplacian.

## Required two-sector correction

There are three coherent ways forward.

### Sector-signed adjoints

Use

\[
Q_+=d_+^*
\]

in the right sector and

\[
Q_-=-d_-^*
\]

in the left sector. Then the two anticommutators have opposite signs. The
reciprocal functor must exchange the sectors and reverse the contraction
orientation.

### Unsigned normal coordinate

Seek

\[
dQ+Qd=|a|N.
\]

This gives a positive contraction on both sides but is non-holomorphic and
nondifferentiable at the seam. The absolute value must emerge from the doubled
source geometry rather than be imposed.

### Indefinite pairing

Use a Krein, symplectic, or Clifford adjoint for which the anticommutator is not
positive. Then signed `a` is possible in one algebra, but positivity can no
longer be used to prove invertibility; the algebraic number operator must carry
that burden.

## Categorical meaning

The two half-planes require two differently oriented dagger structures. The
reciprocal functor is not dagger-preserving in the naive sense; it is
dagger-reversing on the contraction port.

Thus the Ubersector needs the typed packet

\[
(\mathcal C_+,\dagger_+),
\qquad
(\mathcal C_-,\dagger_-),
\qquad
R\dagger_+R^{-1}=-\dagger_-.
\]

The minus sign is not a presentation convention. It is the orientation needed
for the same normal-displacement law to contract both sectors.

## Seam consequence

At `a=0`, the signed anticommutator vanishes. The two dagger structures meet
but do not select a contraction. This permits seam cohomology and explains why
the seam must remain an independent carrier.

Any seam incidence must also intertwine the two opposite adjoint structures.
Otherwise boundary terms produced by integration by parts will fail to cancel
or will be assigned the wrong sector sign.

## DPC

For a theta/Tate Cartan identity, require:

1. the inner product or indefinite pairing in each sector;
2. the exact definition of both adjoints;
3. reciprocal transport of the adjoint operation, including its sign;
4. the source number operator `N` and its invertibility;
5. all boundary terms in the anticommutator domain;
6. a seam incidence intertwining the two dagger orientations;
7. completion-stable closedness of `d` and `Q`.

Reject:

- one positive Hilbert adjoint used with signed `a` on both sides;
- replacing `a` by its absolute value without a doubled-source derivation;
- moving the sign into an untyped basis convention;
- an indefinite adjoint followed by an unjustified positivity claim;
- cancellation of boundary terms only after scalar expectation.

## Verdict

The Cartan–Clifford mechanism survives, but it forces a sharper two-sector
type: opposite contraction adjoints joined by a sign-reversing reciprocal
coherencer. A single positive dagger category cannot support the required
signed normal identity.

