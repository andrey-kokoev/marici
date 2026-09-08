# Ordered supported Gysin for `(t04,t35)`

## Scope

This constructs the codimension-two Cartier duality map for the actual
four-column normalization/conductor comparison from the preceding native
245-state calculation. It retains the endpoint difference line, the ordered
conormal determinant, both independent `u03` normal grades, and the complete
endpoint/Q diagrams under tensoring.

The construction is over the conductor/Rees coefficient base. It does not
postulate a face carrying both crossing diagonals `04` and `35`, identify a
Rees parameter with a physical channel coordinate, or invert a normal
parameter. Its primitive value evaluates the conductor two-extension. A direct
scalar trace sending the native degree-one class `gamma` to one is a different
problem, and the calculation below proves such a trace does not exist in the
specified ordinary coefficient category.

## 1. Base, support, and two endpoint frames

Retain the previous rings `B`, `B_+`, `B_-`, `C` and their difference exact
sequence. All six short Rees graphs are `u_d=t_d X_d`; the three long normal
parameters remain independent. Write

\[
 A=\mathcal C/(u_{03}),\quad s=t_{04},\quad t=t_{35},
 \quad J=(s,t),\quad D=A/J,\quad i:\operatorname{Spec}D\hookrightarrow\operatorname{Spec}A.
\]

In words: take the conductor at the already retained exceptional resonance,
then the closed pair of spectator Rees divisors. `s,t` are independent
polynomial parameters in `A`, so they form a regular sequence.

Let `L_partial` be the oriented endpoint-difference line. Its frame is the
one induced by the source difference `epsilon_+ - epsilon_-`. The physical
ray-to-sheet frame is retained as

\[
 J_\partial=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 J_\partial(-1,1)^T=(1,-1)^T.
\]

In words: the ordered ray boundary maps to the ordered sheet difference,
without averaging or a half-difference. This is the source's endpoint matrix,
not a new normalization.

The conormal lines are

\[
 \ell_s=D[s],\quad\ell_t=D[t],\quad
 \mathcal L=\det(J/J^2)=\ell_s\wedge\ell_t.
\]

Here `[s]` and `[t]` denote conormal symbols, not invertible functions. The
symbols retain their stated order. The physical channel orientation
`[dX03]`, the `u03` normal line, and any external Cartier filtration are
unchanged spectator data; none is identified with `ell_s` or `ell_t`.

## 2. Actual comparison resolution and its ordered reduction

Use homological degrees 2,1,0. Let

\[
 P_2=A z,\quad P_1=A^4,\quad P_0=A\langle r_0,r_c,r_d\rangle,
 \qquad c=04,\ d=35.
\]

Its differentials are precisely the previous sheet restriction matrix and
its kernel:

\[
 w=\begin{pmatrix}t\\s\\t\\s\end{pmatrix},\qquad
 M=\begin{pmatrix}0&-t&s&0\\1&0&-1&0\\0&1&0&-1\end{pmatrix}.
\]

The four `P_1` columns are the two positive-sheet cycles followed by the
negatives of the two negative-sheet cycles. The augmentation is
`(a0,ac,ad) -> a0 mod(s,t)`. Thus `P` resolves the supported endpoint-oriented
line `D tensor L_partial`.

For the standard ordered Koszul complex `K=K_A(s,t)`, use

\[
 d_1=(s,t),\qquad d_2=(-t,s)^T,
 \qquad d(e_s\wedge e_t)=s e_t-t e_s.
\]

The explicit projection `p:P->K` is

\[
 p_0=(1,0,0),\qquad
 p_1=\begin{pmatrix}0&0&1&0\\0&-1&0&0\end{pmatrix},\qquad p_2=-1.
\]

The inclusion `j:K->P` is

\[
 j_0=(1,0,0)^T,\qquad
 j_1=\begin{pmatrix}1&0\\0&-1\\1&0\\0&-1\end{pmatrix},\qquad j_2=-1.
\]

The only nonzero component of its contracting homotopy is

\[
 H_0=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\\0&0&-1\end{pmatrix}:P_0\to P_1.
\]

Direct multiplication gives `p j=1`, `dH+Hd=1-jp`, with the usual side
conditions. The matrix therefore splits into the ordered Koszul resolution
and two integral contractible pairs. The signs are not optional: in these
actual source bases,

\[
 j(e_s\wedge e_t)=-z.
\]

In words: the previous top-basis unit and the `(s,t)`-ordered Koszul unit
differ by a minus sign. The earlier certificate's coordinate `+1` used its
own top basis `z`; it did not fix this comparison with the ordered pair.

## 3. Supported purity map and the Gysin counit

Define `P^vee=Hom_A(P,A)` using the cohomological Hom differential. It has
ranks `(3,4,1)` in cohomological degrees `(0,1,2)`, and differentials

\[
 d^0=-M^T,\qquad d^1=w^T.
\]

The supported purity map is

\[
 \mathcal G_{s,t}:P^\vee
 \longrightarrow i_*\bigl(L_\partial^\vee\otimes_D\mathcal L^\vee\bigr)[-2].
\]

Its only nonzero component is

\[
 \mathcal G_{s,t}^2(\varphi)
 =-\overline{\varphi(z)}\,
 e_\partial^\vee\otimes([s]\wedge[t])^\vee.
\]

In words: extract the dual top coefficient, with the sign forced by the
ordered reduction, and reduce it on the support. The degree-one boundary
has coefficients `t,s,t,s`, so its image is zero modulo `J`. Exactness of the
ordered Koszul resolution proves this is a quasi-isomorphism, not only a
coefficient rule on selected cycles.

The corresponding adjunction counit has the chain representative

\[
 \epsilon:P^\vee\longrightarrow A\otimes L_\partial^\vee,
 \qquad \epsilon^0(a_0,a_c,a_d)=a_0,
 \qquad\epsilon^1=\epsilon^2=0.
\]

It is the dual of the lift of the quotient unit `A tensor L_partial -> P`,
`1 -> r0`. Together the purity map and this counit give the supported Gysin
roof

\[
 i_*\bigl(L_\partial^\vee\otimes\mathcal L^\vee\bigr)[-2]
 \xleftarrow{\ \mathcal G_{s,t}\ } P^\vee
 \xrightarrow{\ \epsilon\ } A\otimes L_\partial^\vee.
\]

No residue into an unrestricted unshifted coefficient line is asserted.
The positive ordered dual generator is `eta=-z^vee`, and

\[
 \mathcal G_{s,t}(\eta)
 =e_\partial^\vee\otimes([s]\wedge[t])^\vee,
 \qquad
 \bigl(\mathcal G_{s,t}(\eta)\bigr)
       (e_\partial\otimes[s]\wedge[t])=1.
\]

The original representative `+z^vee` evaluates to `-1` in this ordered
frame. The distinction is an explicit basis dictionary, not a free sign
chosen after the calculation.

**Line convention.** `J/J^2` is a line pair on `D`. It is not tensored
naively into `P^vee` over `A`: that would perform an extra, generally
non-flat base change. The invariant target above keeps the line on its
correct support. Scalar matrices use the prescribed free lifts of the two
parameter frames over `A`, followed by restriction to `D`.

The cohomological shift two here belongs to closed-immersion duality. It is
not obtained by adding external Cartier filtration degree to cellular degree.

## 4. Frame changes and reflection

For `s'=a s`, `t'=b t`, with `a,b` units and labels retained, the comparison
from the primed resolution to the old one has matrices

\[
 F_0=\operatorname{diag}(1,a,b),\quad
 F_1=\operatorname{diag}(a,b,a,b),\quad F_2=ab.
\]

They satisfy `M(s,t)F1=F0 M(as,bt)` and
`w(s,t)F2=F1 w(as,bt)`. The conormal determinant scales by `ab` and its dual
by `(ab)^(-1)`. Thus the invariant purity map glues under changes of the
normal frames. This uses inverses of transition units, never inverses of
`s,t`, an occurrence parameter, or an integer.

On the conductor comparison, exchange the sheets, the two spectator labels,
and `s,t`. The endpoint difference requires

\[
 R_0=-\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix},\quad
 R_1=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},\quad
 R_2=1.
\]

These satisfy the semilinear chain equations and square to one. The Koszul
reflection matrices are `-1`, minus the two-basis swap, and `+1`; `p`, `j`,
and `H` intertwine them strictly. The endpoint line and conormal determinant
each change sign, so their product has sign `+1`. This checks the loaded
even reflection rule without a second polarity twist.

At hexagon-label level the reflection is `v -> 3-v mod6`. It exchanges
`04` with `35`, exchanges the positive and negative endpoints, and sends the
blowup center `{03,13}` to `{03,02}`. The covariance above compares these
labelled charts. It is not an asserted reflection automorphism of the
unreflected blowup center.

## 5. Retain the independent resonance normal and complete endpoint/Q data

The pair Gysin is relative to `u03=0`; it does not silently remove the
derived normal of that equation. A free model over the unspecialized
conductor ring is

\[
 \widetilde P=K_{\mathcal C}(u_{03})\otimes_{\mathcal C}P_{\mathcal C}.
\]

Its homological ranks are `(3,7,5,1)`. The partial Gysin acts as the identity
on `K(u03)^vee` and as `G_{s,t}` on `P^vee`. After taking the derived `u03=0`
fibre it retains both adjacent normal grades. In cohomological conventions
the partial-duality output has these grades in degrees two and three.
A subsequent evaluation of the `u03` normal would be another operation and
has not been made. In particular, this construction supplies no equality
between that line and `[dX03]`.

The comparison matrices also have a flat coefficient lift to the glued
ambient Rees ring `B`: it is polynomial in the short occurrence variables
modulo the alternating monomial relations, hence free over the retained
conductor parameter subring before harmless monodromy-unit localizations.
For any of the supplied full native, retained, or old-target chain complexes
`E`, tensor purity with the identity:

\[
 P_{\mathcal B}^\vee\otimes_{\mathcal B} E
 \longrightarrow
 (E\otimes_{\mathcal B}^{L}\mathcal B/(s,t))[-2]
 \otimes L_\partial^\vee\otimes\mathcal L^\vee.
\]

In the framed bases every top-dual column tensored with a state `[F,H]` maps
to minus that state on the support. All other dual columns map to zero.
The same explicit construction applies to the duality counit, which selects
the `r0^vee` column. The checker verifies both complete chain equations on
all `8*245`, `8*225`, and `8*215` tensor columns.

Because the shift is even and the maps are coefficient natural, they commute
with the actual endpoint connecting maps, the road inclusions, the fixed
endpoint swap, and the seven-state `Q` projection. Neither the sixteen
endpoint states nor either retained normal grade is omitted. The endpoint
connecting squares are checked from the supplied target differential.

On a legal Cech stalk where `u04=s X04` is inverted, `s` is a unit and the
supported `(s,t)` fibre is empty; the supported output is then zero. The
same holds for `u35`. This follows from flat localization of the complete
map, not from putting an inverse on its supported source. The finite
polynomial construction is the one explicitly replayed by the checker.

These squares preserve the existing endpoint/Q objects and maps. They do
not create the independently missing normalization-to-physical connector
homotopy or a nonzero image in the physical `Q`-quotient.

## 6. The unit evaluates an extension, not a direct native scalar trace

The native class is `gamma=X04 p04`, with the equivalent representative
`-X35 p35`. Retain the previous first normal primitives

\[
 U_s=-r_{04},\qquad U_t=-t r_0+r_{35},
 \qquad dU_s=s\gamma,\quad dU_t=t\gamma.
\]

The next normal coherence is

\[
 sU_t-tU_s=g_*=-st r_0+t r_{04}+s r_{35},\qquad dg_*=0.
\]

The full native packet supplies only

\[
 dZ_*=f g_*,\qquad
 f=u_{03}+(1+u_{03})t_{13}X_{13}.
\]

In words: the two first normal homotopies do not yet form a Koszul lift of
`gamma`. Their comparison is the surviving exceptional class. Restricting
`g_*` to the two sheet cycle bases gives `(t,s,t,s)`, exactly the kernel
column `w` of the comparison resolution. The supported residue therefore
normalizes this two-extension/coherence obstruction. It does not prove a
primitive trace on `gamma`.

For the displayed choice of primitives, `g_*` is not a boundary in the full
native complex: set every short occurrence and `u03` to zero while retaining
`s,t`. The exceptional differential and all target-to-exceptional attaching
columns become zero, and `g_*` remains nonzero.

There is a stronger no-lift statement, independent of those choices. For
this nonexistence test only, specialize the full source to

\[
 B'=\mathbb Z[x,y,s,t]/(xy),\qquad x=X04,\quad y=X35,
\]

with the other short occurrences and `u03` zero, retaining arbitrary
spectator coefficients. Compatible monodromy units may remain inverted.
All attaching columns have the factor `X13`, so vanish. Quotient the
exceptional complex by its `y_c,y_d,z_0,z_c,z_d` subcomplex; this is a genuine
chain quotient after `f=0`. The remaining complex has only

\[
 T_2=(B')^3\xrightarrow{
 \begin{pmatrix}-x&-sx&0\\-y&0&-ty\end{pmatrix}}
 T_1=(B')^2.
\]

The class `gamma=x p_c` is nonzero. Indeed after `s=t=0` the only column is
`(-x,-y)^T`, and the coefficient detector `[x](p_c coefficient)-[y](p_d
coefficient)` kills every boundary and evaluates `gamma` to one.

If a chain map from the shifted ordered `K(s,t)` to `T` induced `gamma`,
write its first homotopies as `A,B in T2`. There is no degree-three target,
so the top equation forces `sB-tA=0`. The pair `(s,t)` is regular in `B'`;
its free-module syzygy says `A=sV`, `B=tV`. The first equation then gives
`s(dV-gamma)=0`, hence `dV=gamma`, a contradiction. The same argument works
for a homologous representative. Any proposed full native map would
specialize and project to this impossible map.

Thus the embedded copy of `A/(s,t)` in degree-one native homology does not
supply an ordinary derived inclusion `K_B(s,t)[1] -> native` realizing its
generator. The supported Gysin constructed above is on the *dual comparison
resolution*, not such an inclusion.

A direct scalar output is also excluded. Every term of the native
representative is divisible by `X04`; the fully supported coefficient module
`D` has `X04=0`. Since the native complex is bounded free, every morphism to
`D[1]` in the ordinary coefficient derived category is represented by a
chain map, and every such map kills `gamma`. No such trace sends it to one.
This does not exclude a bivariant, support-dualized operation; the displayed
Gysin roof is precisely such a differently typed operation.

## 7. Reproduction and evidence

Run `python check_supported_gysin.py` after extracting the complete package.
It requires Python 3.10+ and the standard library only. It replays the previous
5,840-check normalization computation and its 6,706-check native predecessor,
then verifies 11,667 new exact identities. Algebraic exactness and the universal
non-lift statements use the proofs above; the finite checks are not
substituted for those proofs.

The JSON files export the full conductor/Koszul matrices, both chain maps,
contracting homotopy, reflection maps, dual differential, residue rule, native
syzygy, native representatives, source hashes, and scope exclusions.

### Primary mathematical references

- Stacks Project, [Koszul complexes, tag 0621](https://stacks.math.columbia.edu/tag/0621):
  ordered exterior differential, functoriality, tensor products, homotopies.
- Stacks Project, [regular sequences, tag 062F](https://stacks.math.columbia.edu/tag/062F):
  exactness of the ordered Koszul resolution.
- Stacks Project, [Cartier duality, tag 0B4B](https://stacks.math.columbia.edu/tag/0B4B):
  shifted dual normal line; iterate for the two regular parameters.
- Stacks Project, [Hom complexes, tag 0A8H](https://stacks.math.columbia.edu/tag/0A8H):
  dual differential and counit signs.

### Source data

Marici commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

- Entry 93, normalization/conductor square and signed sheet difference.
- Entry 115, multi-Rees graph and retained conormal symbols.
- Entry 400, fixed ray-to-sheet endpoint swap and its sign convention.
- The supplied `normalization_exceptional_pullback_package.zip`, including
  the native matrices, sheet restrictions, gamma, and its first homotopies.

The new supported Gysin, ordered sign dictionary, tensor naturality checks,
and native coherence obstruction are constructed here. No amplitude value,
raw global six-functor equivalence, or complete spatial connector is asserted.
