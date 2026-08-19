# 961 — Diagonal Inertia and Facet Kummer Lines Meet Only Through the Point Costalk

## Module gate for Entry 960

Let

\[
R=\mathbb Z[m^{\pm1},n^{\pm1}].
\]

At a compatible two-facet corner, the diagonal-inertia and facet support
modules are

\[
D=R/(mn-1),
\qquad
F_m=R/(m-1),
\qquad
F_n=R/(n-1).
\]

Before constructing barycentric flag maps, test whether any nonzero ordinary
\(R\)-linear morphism between these rank-one support modules can exist.

## Hom calculation

An element defining a map \(D\to F_m\) must be annihilated by \(mn-1\) in
\(F_m\).  But modulo \(m-1\),

\[
mn-1=n-1,
\]

which is a non-zero-divisor in \(\mathbb Z[n^{\pm1}]\).  Hence

\[
\operatorname{Hom}_R(D,F_m)=0.
\]

Conversely, modulo \(mn-1\) one has \(n=m^{-1}\), and \(m-1\) remains a
non-zero-divisor.  Thus

\[
\operatorname{Hom}_R(F_m,D)=0.
\]

The same argument with \(m,n\) exchanged gives

\[
\boxed{
\operatorname{Hom}_R(D,F_m)
=\operatorname{Hom}_R(F_m,D)
=\operatorname{Hom}_R(D,F_n)
=\operatorname{Hom}_R(F_n,D)=0.
}
\]

## Common costalk

The diagonal and each facet meet at

\[
mn-1=m-1=0
\quad\Longleftrightarrow\quad
m=n=1.
\]

Their gradients at that point are

\[
d(mn-1)=(1,1),
\qquad d(m-1)=(1,0),
\qquad d(n-1)=(0,1).
\]

The two Jacobian determinants are \(-1\) and \(+1\).  Therefore both
intersections are integral and transverse:

\[
D\otimes_R^{\mathbf L}F_m
\simeq
D\otimes_R^{\mathbf L}F_n
\simeq
P:=R/(m-1,n-1),
\]

with no excess \(\operatorname{Tor}_1\).

## Correction to the frontier

Entry 960's proposed direct maps from the corner Kummer line to its incident
facet lines are mistyped.  The canonical comparison has cospan form

\[
F_m\longrightarrow P\longleftarrow D,
\qquad
F_n\longrightarrow P\longleftarrow D,
\]

or the variance-correct Gysin dual of this diagram.

Thus

\[
\boxed{
\text{diagonal inertia and facet inertia communicate only through the
supported point costalk.}
}
\]

No additional carrier cell and no excess extension are forced.

## Next falsifier

Construct the two costalk maps with the source residue orientation and form
the supported Mayer--Vietoris/Čech cone for

\[
F_m\oplus F_n\oplus D\longrightarrow P\oplus P.
\]

Determine its integral cohomology and compare its primitive generators with
the corresponding source branch columns.  Do not replace this cospan by a
direct line map or by a chosen splitting at \(m=n=1\).

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_corner_flag_module_gate.rs`;
- packet:
  `research/benincasa/string-six-point-corner-flag-module-gate.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_corner_flag_module_gate`;
- allocator claim:
  `seqclaim-b9bb963e4ee86d252d21d9fb`.
- epistemic event:
  `ev-000000000578-787954c0-a8c1-4072-b931-9505d8722b54`.
