# Seam positivity does not exclude off-seam zeros without a two-point transport theorem

## The seam-only positivity trap

The reciprocal Dirac construction separates holomorphic multiplicity from
positive normal energy, but it exposes a decisive geometric restriction.

For

\[
s=\frac12+it,
\]

reciprocal reflection and complex conjugation coincide:

\[
1-s=\bar s.
\]

Only on this fixed locus can the algebraic reciprocal dual be identified with
a Hilbert adjoint and hence produce an ordinary positive norm.

Away from the seam,

\[
1-s\ne\bar s.
\]

Therefore a holomorphic pairing between the \(s\)-sheet and the
\(1-s\)-sheet is not automatically positive. Positivity on the critical line
cannot simply be analytically continued into either open half-strip.

## Why this matters for RH

To prove RH one must exclude a zero

\[
\xi(s_0)=0,
\qquad
\operatorname{Re}s_0\ne\frac12.
\]

The functional equation and reality generate a reciprocal-conjugate orbit,

\[
s_0,\quad 1-s_0,\quad \bar s_0,\quad 1-\bar s_0.
\]

A positive norm available only at fixed points of the involution says nothing
by itself about a kernel state living at \(s_0\). The argument needs a
source-authorized transport that converts the off-seam orbit into a seam
energy identity.

Absent such a transport, the implication

\[
\text{positive Green form on the seam}
\Longrightarrow
\text{no zeros off the seam}
\]

is invalid.

## Two legitimate routes

### Sectorial coercivity

Construct a Hermitian metric \(G(s)\) in each open sector such that the
boundary pencil satisfies

\[
\operatorname{Re}
\langle D(s)x,G(s)D(s)x\rangle
\ge
m_C\|D(s)x\|^2
\]

uniformly on every compact off-seam set \(C\).

This is stronger than seam positivity. The metric must be source-derived,
compatible with reciprocal sewing, and uniformly equivalent to the declared
source topology.

### Two-point orbit pairing

Keep the holomorphic reciprocal geometry and pair the conjugate points
\(s\) and \(\bar s\) on the four-point orbit. A candidate doubled state is

\[
\Psi_{s}
=
(x_s,\,
Jx_{1-\bar s}),
\]

where \(J\) is the source real structure. The required theorem is an identity

\[
\mathcal E_s(\Psi_s)
=
(2\operatorname{Re}s-1)\,
\mathcal M_s(\Psi_s)
+
\mathcal B_s(\Psi_s),
\]

with:

- \(\mathcal E_s\ge0\) a complete Green energy;
- \(\mathcal M_s>0\) on every nonzero closed boundary state;
- \(\mathcal B_s=0\) for a state satisfying the full reciprocal boundary
  condition.

For a kernel state, the left side and boundary term vanish. Strict positivity
of \(\mathcal M_s\) then forces

\[
2\operatorname{Re}s-1=0.
\]

This is the exact form of an RH-strength Green identity. It is not supplied by
the functional equation alone.

## The missing typed arrow

The scalar determinant theorem gives

\[
\xi(s_0)=0
\Longrightarrow
\ker D_+(s_0)\ne0.
\]

Reciprocal and real sewing give corresponding states at the other three orbit
points. The missing arrow is

\[
\text{four-point kernel orbit}
\longrightarrow
\text{one closed two-point Green state}.
\]

That arrow must preserve:

1. chiral determinant multiplicity;
2. reciprocal orientation;
3. the endpoint and archimedean attachments;
4. primitive, square, and connected strata;
5. the wall subtraction;
6. the response relation;
7. the completed source topology.

Merely placing the four vectors in a direct sum does not make a closed Green
state.

## Polarized commutator form

A source-native mechanism would be a commutator or Lagrange identity. Let
\(A\) be the scale generator and \(J\) the reciprocal real structure. The
desired fully polarized relation has the schematic form

\[
\langle D(s)x,Jy\rangle
-
\langle x,JD(1-\bar s)y\rangle
=
(2\operatorname{Re}s-1)\langle x,Wy\rangle
+
\operatorname{Flux}(x,y),
\]

where \(W>0\) is a source weight.

For reciprocal kernel partners with closed boundary flux, this reduces to

\[
(2\operatorname{Re}s-1)\langle x,Wy\rangle=0.
\]

The remaining theorem is not just positivity of \(W\). One must prove that the
reciprocal kernel pairing \(\langle x,Wy\rangle\) is nonzero. Otherwise an
off-seam kernel orbit may be isotropic.

This non-isotropy is the global diagonal or mixed observability margin in its
first-order form.

## Hostiles

1. A family positive on the seam but indefinite immediately off it.
2. A four-point kernel orbit whose reciprocal pairing is zero.
3. A formal orbit sum that violates one endpoint sewing condition.
4. A commutator identity with an uncontrolled boundary flux.
5. Finite-cutoff non-isotropy whose pairing tends to zero at completion.
6. A sectorial metric obtained by an unbounded, non-source-authorized change
   of coordinates.

## Verdict

The reciprocal Dirac double solves the holomorphic linearization problem, but
seam positivity alone cannot prove RH.

The decisive RH theorem must either establish sectorial coercivity off the
seam or construct a complete two-point orbit Green identity whose positive
mass term is multiplied by \(2\operatorname{Re}s-1\).

The smaller and more source-native target is the second route. The next
calculation is the fully polarized Lagrange identity for a reciprocal pair of
closed boundary states, followed by a uniform non-isotropy estimate for its
mass pairing.
