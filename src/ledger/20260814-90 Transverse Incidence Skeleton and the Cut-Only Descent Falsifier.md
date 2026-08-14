# Transverse Incidence Skeleton and the Cut-Only Descent Falsifier

## Record

Date: 2026-08-14

Status: exact finite \(n=8\) incidence theorem and falsification of natural
Cut-only descent for the free scalar occurrence object.  This entry does not
define a Grothendieck topology, prove a complete/regular/bounded cd-structure,
or identify the dependent route correspondence with a cdh square.

## Closed scalar faces

Let \(\mathcal T_8\) be the 132 triangulations of the octagon.  For every
noncrossing dissection \(S\), define the closed support face

\[
X_S=\{T\in\mathcal T_8:S\subseteq T\}.
\]

Together with the empty object, these faces form the finite base incidence
category used in this audit.  Exact-core pieces are not substituted for
closed at-least-core faces.

The checker enumerates 903 nonempty faces, with associahedral face vector

\[
(f_0,f_1,f_2,f_3,f_4,f_5)
=(132,330,300,120,20,1).
\]

Every one of the 408,156 unordered intersections is exactly

\[
X_S\cap X_T=
\begin{cases}
X_{S\cup T},&S\cup T\text{ noncrossing},\\
\varnothing,&S\cup T\text{ crossing}.
\end{cases}
\]

Thus the closed scalar faces supply a genuine finite Cartesian incidence
skeleton.

## Transverse square audit

Three previously established transverse families give 2,008 undeformed
coordinate squares:

\[
324\ \text{physical/physical},\qquad
1012\ \text{independent scalar/scalar},\qquad
672\ \text{independent scalar/physical}.
\]

Saturation along every closed-face inclusion performs 91,488 base-change
checks and leaves 17,964 distinct supported squares.  All tested squares are
pullbacks with monomorphic legs.  The typed monic self-intersection identities
pass 365,952 checks.  The base changes split as

\[
6800\ \text{nondegenerate},\qquad
20400\ \text{degenerate},\qquad
64288\ \text{with an empty leg}.
\]

This proves a transverse **Cartesian/excision calculus**.  It does not prove
that these squares generate covers.

## Exact Cut-only falsifier

Let \(\mathcal D_{\rm phys}\) be the eight octagon diagonals with opposite
endpoint parity and let

\[
B_{\rm cut}=\bigcup_{D\in\mathcal D_{\rm phys}}X_{\{D\}}.
\]

The exact support count is

\[
|B_{\rm cut}|=128<132=|\mathcal T_8|.
\]

The four omitted triangulations contain no physical diagonal.  They are
exactly the zero-core/contact vertices.  Consequently, for the free occurrence
module, simultaneous restriction to all physical Cuts has

\[
\boxed{
\operatorname{rank}\ker\!\left(
\mathbb Z[\mathcal T_8]
\longrightarrow
\bigoplus_{D\in\mathcal D_{\rm phys}}\mathbb Z[X_{\{D\}}]
\right)=4.
}
\]

More strongly, none of the 2,008 proper transverse face pairs covers the
actual triangulation support of its ambient face.  Therefore the natural
cellular interpretation of these squares is not a Cut-only coverage.

There is an important categorical nuance.  In the abstract face poset, the
two axes of each tested square have categorical join equal to the ambient
face.  All 1,813,224 representable square-descent identities pass.  One may
therefore declare an artificial non-spatial subcanonical topology on that
poset.  But the physical occurrence object is not separated for it: its
contact kernel restricts to zero on every Cut.  Sheafification would erase
scalar data rather than reconstruct it.

Hence the naive claim

\[
\boxed{
\text{transverse physical Cut squares alone define the natural scalar descent site}
}
\]

is falsified at eight points.

## Dependent routes remain transfers

For the representative dependent configuration

\[
P=\{13,35,57\},\qquad
S=\{02,04,06\},\qquad
Q=\{03,05\},
\]

the supports have sizes 5, 4, and 8, while

\[
P\cap S=\varnothing,\qquad
|P\cap Q|=|S\cap Q|=1.
\]

No ordinary scalar pullback square contains the coefficient overlap used by
the route-to-cube construction.  The pentagon/square coherence is therefore a
derived transfer or excess-intersection datum, not a base cdh square.

## Corrected descent objective

The smallest faithful replacement for Cut-only descent is a constructible
recollement separating the Cut boundary from the locally closed contact
sector.  Schematically, after the relevant closed/open typing is fixed, one
expects a Cousin triangle of the form

\[
i_*i^!\mathsf J
\longrightarrow
\mathsf J
\longrightarrow
j_*j^*\mathsf J
\xrightarrow{\partial_{\rm Cousin}}
i_*i^!\mathsf J[1],
\]

where one term retains the zero-core/contact data and the other is the
factorization boundary object.  An equivalent recognition topology may use
physical Cuts together with ultraviolet/contact boundary data; entry 48's
conservativity theorem already has exactly this logical form.

This correction aligns with entry 89.  Its exact boundary-costalk pairing

\[
\Phi_{03}^{\rm gr,\partial}
\]

cannot be promoted to a full half-object from road data alone, while entry
66's alternating-conductor chain lift

\[
\boldsymbol\sigma_{\rm alt}
\]

is the first missing map on the circuit side.  The sharp new conjecture is
that these are two faces of the same connecting datum:

\[
\boxed{
\boldsymbol\sigma_{\rm alt}
\ \text{is induced by, or Verdier-dual to, the contact-to-Cut Cousin
connecting morphism.}
}
\]

This is not proved.  It is falsified by incompatible support, a different
dihedral character, failure of the chain-map identity, or a nonmatching
factorization boundary.

## Next exact test

Construct the integral cellular pair

\[
(K_5,B_{\rm cut}),
\]

where \(K_5\) is the octagon associahedron.  Compute the signed relative
boundary matrices, Smith normal forms, \(D_8\)-action, and the Cousin
connecting morphism carried by the four zero-core vertices and their incident
cells.  Then compare its support and character with

\[
\chi_N
=\operatorname{sgn}_{\rm polarity}\otimes\operatorname{or}(C_3)
\]

and entry 66's alternating conductor.  A tautological direct sum on vertex
occurrences is insufficient; the test must retain cellular attachments and
coefficient maps.

## Exact certificate

Run:

```text
rustfmt --check research/voevodsky/check_n8_scalar_cd_site.rs
rustc --edition=2021 -D warnings -O research/voevodsky/check_n8_scalar_cd_site.rs -o "$env:TEMP\\marici-n8-scalar-cd-site.exe"
& "$env:TEMP\\marici-n8-scalar-cd-site.exe"
```

Certificate SHA-256:

```text
b13e57a630241eaae39fd15392718f2ccd2aa1c3f14349f42ce79d0fe177f8f2
```

## Internal dependencies

- Entry 31: scalar product-associahedral faces.
- Entries 32 and 37: transverse physical and mixed Beck--Chevalley maps.
- Entry 48: Cuts plus ultraviolet boundary data are conservative.
- Entries 76, 82, and 83: dependent route/cube transfer typing.
- Entry 88: three-road quotient and crosscap-counit gap.
- Entry 89: exact boundary-costalk pairing and contact-extension ambiguity.
- `research/voevodsky/context.md`.
- `research/voevodsky/check_n8_scalar_cd_site.rs`.
