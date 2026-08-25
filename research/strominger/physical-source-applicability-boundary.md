# Physical source boundary for the parity-kernel engine

## Scope and conclusion

This packet compares the parity-kernel engine with the radiative phase space
used in the leading and subleading BMS/memory source packets.  The comparison
is source-first: it uses the Bondi shear type, its sphere transition law, and
the derivative order in the PSZ constraint.  It does not choose a source map
by asking which map would realize a known engine kernel.

The first conclusion is a no-go theorem:

> A nonzero finite Laurent polynomial cannot be the component of a globally
> smooth Bondi shear `C_zz` on the celestial sphere.

Consequently the engine lattice is not a subspace of the standard smooth
radiative phase space.  It is a local algebraic test space.  Its towers and
exceptional circuits acquire physical meaning only after an independently
specified punctured or distributional source constructor is supplied.

The second conclusion is an operator-grade gate.  The local magnetic density
in the PSZ spin-memory constraint is

\[
 \operatorname{Im}\!\left[\partial_{\bar z}D_z^3C_{zz}\right].
\]

The engine fold at grade `g` applies `D_z` with weights
`2,3,...,g+1`, hence has exactly `g` covariant derivatives before the final
mixed derivative.  The PSZ density therefore selects engine grade `g=3`.
The exceptional circuits `E_1` and `E_2`, which exist only at engine grade
two, are not classes of this source-derived PSZ port.

## 1. Source object and boundary conditions

The standard source object is the Bondi shear

\[
 C=C_{zz}(u,z,\bar z)\,dz^2+C_{\bar z\bar z}(u,z,\bar z)\,d\bar z^2
\]

on each sphere cut of null infinity, subject to the corner and reality
conditions frozen in `soft-bms-memory-conventions.md` and
`subleading-triangle-conventions.md`.  In particular:

- `N_zz=partial_u C_zz` vanishes at the stationary corners;
- the magnetic-parity corner constraint is retained;
- antipodal matching is an external scattering input, not a gauge quotient;
- smooth radiative data are global tensor fields on `S^2`.

Point-particle fluxes and Green kernels can introduce distributions at named
punctures.  That is a different constructor: its punctures, distributional
orders, matching conditions, and allowed test functionals must be declared.
The mere existence of a Laurent pole does not supply those data.

## 2. Exact chart-transition no-go

Use the north chart `z` and the south chart `w=1/z`.  Since `C` is a covariant
spin-two tensor,

\[
 C_{ww}(w,\bar w)
 =\left(\frac{dz}{dw}\right)^2 C_{zz}(1/w,1/\bar w)
 =w^{-4}C_{zz}(1/w,1/\bar w).
\]

Write a finite Laurent component as

\[
 C_{zz}=\sum_{p,q}c_{pq}z^p\bar z^q.
\]

Regularity at `z=0` requires every occupied exponent to obey
`p>=0` and `q>=0`.  In the south chart the same monomial becomes

\[
 c_{pq}w^{-p-4}\bar w^{-q},
\]

so regularity at `w=0` requires `p<=-4` and `q<=0`.  No exponent pair
satisfies both sets of inequalities.  Distinct Laurent monomials remain
distinct after the invertible exponent transform, so cancellation cannot
remove a forbidden leading monomial.  Therefore

\[
 \boxed{\Gamma(S^2,\operatorname{Sym}^2T^*S^2)
 \cap \mathbb C[z^{\pm1},\bar z^{\pm1}]\,dz^2=\{0\}.}
\]

This does not say that smooth spin-two tensors vanish.  Their stereographic
components generally contain powers of `(1+z*bar(z))` and are not finite
Laurent polynomials.

## 3. Consequences for the named engine classes

Every engine source vector is a finite Laurent polynomial in the component
`C_zz`.  Hence, under the standard smooth constructor:

\[
 \operatorname{im}(\text{physical smooth source}\to S_{g,A,I})=0
\]

if the codomain is required literally to be the finite Laurent source
lattice.  In particular:

- no tower `D_{g,a}=z^{-a}bar(z)^{-(g+a-1)}` is constructible as a
  nonzero smooth Bondi shear;
- neither grade-two circuit `E_1` nor `E_2` is constructible in that lattice;
- rational exactness of the folded one-form does not repair source
  singularity;
- the complementary `(E,M)` port theorem remains an engine theorem, not a
  physical reconstruction theorem.

There are two logically separate failures for `E_1,E_2`: they are singular
finite Laurent data, and their grade is not the PSZ spin-memory grade.

## 4. Physical target versus the engine full target

The engine full target is the free lattice of every Laurent numerator
coefficient after a common denominator is cleared.  The cited physical
readouts are instead:

- a local curl constraint density;
- a charge paired with a sphere test field;
- a Green-kernel and contour integral giving the spin-memory delay.

None of the source packets identifies these functionals with independent
access to every Laurent coefficient.  Therefore the proposition

\[
 \text{physical target}=Y_{g,\mathbb Z}^{\mathrm{full}}
\]

is falsified as a presently typed claim: the two sides are different kinds
of object, and no source-derived isomorphism has been supplied.  This does
not yet compute the kernel of every possible family of contour probes.  It
sets the required next test: prove joint faithfulness of the complete PSZ
contour/charge family on an explicitly declared punctured radiative source
quotient.

## 5. Gauge and repair boundary

The physical repair/gauge complex precedes the engine:

\[
 \{\text{Bondi representatives}\}
 \longrightarrow
 \{\text{radiative shear/news modulo Bondi and polarization gauge}\}
 \longrightarrow
 \{\text{local curl density, charges, memory records}\}.
\]

The engine identity

\[
 dF_g(D)=-M_g(D)\,dz\wedge d\bar z
\]

is not this repair complex.  It classifies closed folded forms after an
engine datum has already been admitted.  A circuit in `ker M_g` cannot be
called physical gauge without a preceding map from an authorized radiative
history and a proof that the relevant equivalence descends.

## 6. Constructor-extension alternatives

A nontrivial physical comparison can proceed in either of two ways:

1. **Smooth harmonic constructor.** Replace the finite Laurent lattice by
   spin-weighted spherical harmonics, transport the fold and parity ports,
   and recompute the kernel.  The existing Laurent theorem does not transfer
   automatically.
2. **Punctured/distributional constructor.** Declare punctures and source
   fluxes, derive the allowed principal parts from the Green kernels or hard
   scattering data, include boundary terms at every puncture, and derive the
   contour/charge target.  Arbitrary Laurent coefficients remain forbidden
   unless the source map generates them.

The next move is the second route because it is the only one that could make
the engine pole towers relevant to celestial soft insertions.  Its central
falsifier is whether the PSZ/HMLS Green-kernel image contains even one named
tower after all tensor weights and boundary terms are retained.

## Evidence

`checkers/physical_source_applicability_boundary_checks.py` verifies the
chart transition, the empty intersection of north/south regular Laurent
supports, the singularity of every named class over a bounded hostile range,
and the unique PSZ derivative-grade match.

