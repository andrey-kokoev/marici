# Secondary conductor–Morse calculation: supported block and remaining identification

## Result

The actual conductor comparison has been dualized with its independent
`u03`-normal retained. After the **codimension-two Gysin shift**, its
secondary cohomology is one line over

\[
D=\mathcal C/(u_{03},t_{04},t_{35}).
\]

An explicit representative has a primitive normal Bockstein. This is a
calculation in the supported coefficient/resonance complex. It is not yet a
calculation of the physical conductor–Morse difference: no common-complex
realization of the two independently specified homotopies is supplied by the
inputs inspected here.

The prior assertion `Psi03(eta_partial) = [qJ]_framed` was not established.
Its purported proof multiplied three independently normalized scalars and
invoked uniqueness without constructing an object or map in that uniqueness
problem. The scalar product does not supply the missing composite, source
identification, or homotopy. This assertion is not used below. The matrix
proofs of supported purity and native blowdown are separate and remain inputs.

## 1. The equation that must be checked

For the physical source `J_M` and target `F0`, the secondary difference is

\[
\Delta_J=H_C-e_F h_M.
\]

Its degree is one in the common cohomological mapping complex. Its closure
requires the actual identities

\[
\delta h_M=q_J,\qquad \delta e_F=0,\qquad
\delta H_C=e_Fq_J.
\]

The graded composition rule then gives `delta Delta_J=0`. The first and third
identities must hold in compatible complexes. An equality of residues is not
a substitute for either identity.

The source's seven-triangle occurrence-loaded carrier was reconstructed and
replayed:

\[
d H_M=q_J-X_3\widetilde\xi.
\]

Here `X3` denotes the short source label corresponding to diagonal `35`, not
`X03`. Normalized blowdown sends seven triangles to five and preserves this
identity. Only after the specified relative projection removes the gallery
term does this become a nullhomotopy of the projected `qJ`. These flag
complexes are retained as distinct objects in the verifier. No map from them
to the conductor dual is manufactured.

Marici's Entry 109 states precisely the common-mapping-complex requirement.
The inspected global-transform checker compares a signature dictionary with
its own copy; it does not construct the required `H_C`.

## 2. Exact pair calculation

Write

\[
u=u_{03},\quad s=t_{04},\quad t=t_{35},\quad
A=\mathcal C/(u),\quad D=A/(s,t).
\]

The spectator coefficient ring is the preceding conductor ring. Its six
short occurrence coordinates have already been set to zero. The three
long occurrence coordinates and independent long-normal parameters remain;
`s,t` are independent polynomial variables. Monodromy-unit localizations do
not invert `u`, `s`, or `t`.

The actual resolution is

\[
P_2=Az\xrightarrow{w}P_1=A^4\xrightarrow{M}P_0=A^3,
\]

\[
w=(t,s,t,s)^T,\qquad
M=\begin{pmatrix}0&-t&s&0\\1&0&-1&0\\0&1&0&-1\end{pmatrix}.
\]

Its dual differential is `d0=-M^T`, `d1=w^T`. Thus

\[
P^\vee:
A^3\xrightarrow{\begin{pmatrix}0&-1&0\\t&0&-1\\-s&1&0\\0&0&1\end{pmatrix}}
A^4\xrightarrow{(t,s,t,s)}A.
\]

For a degree-one closed cochain `v=(a,b,c,d)`, closure is

\[
t(a+c)+s(b+d)=0.
\]

Regularity of `(s,t)` gives a unique polynomial `h` such that

\[
a+c=sh,\qquad b+d=-th.
\]

No base-ring inversion is used: this is the regular-pair syzygy, or exact
polynomial divisibility. The unique degree-zero primitive is

\[
b_0=(-h,-a,d),\qquad d^0 b_0=v.
\]

Therefore

\[
H^0(P^\vee)=H^1(P^\vee)=0,\qquad H^2(P^\vee)=D.
\]

In particular, any **already well-typed** pair of degree-one trivializations
of the same degree-two cochain in this pair complex differ by the displayed
boundary. This local statement does not compute the physical mapping fibre
with a different source and extra comparison data.

The positively ordered Gysin class is `eta=-z^vee`. It is not itself a
nullhomotopy: a putative equation `delta H=eta` would require

\[
t(H_1+H_3)+s(H_2+H_4)=-1.
\]

Reduction modulo `(s,t)` disproves that equation. This is why a unit Ext²
class cannot be substituted for a degree-one conductor trivialization.

## 3. Retain the independent resonance normal

Before restricting to `u=0`, lift `P` to `P_C` over `C` and form

\[
\widetilde P=K_{\mathcal C}(u)\otimes P_{\mathcal C},\qquad
\mathcal M_{\mathrm{loc}}
=\operatorname{Hom}_{\mathcal C}(\widetilde P,\mathcal C)[2].
\]

The shift is the actual two-divisor duality shift. It is not an identification
of the external Cartier filtration with cellular chain degree.

The homological ranks of `Ptilde` are `(3,7,5,1)`. Consequently the shifted
Hom ranks are `(3,7,5,1)` in cohomological degrees `(-2,-1,0,1)`.

Let `e_u` denote the degree-one basis of `K(u)`, with `d e_u=u`. In the basis
ordered by the `K(u)` factor first, the unshifted Hom differentials are

\[
D^0=\begin{pmatrix}-M^T\\-uI_3\end{pmatrix},\qquad
D^1=\begin{pmatrix}w^T&0\\uI_4&-M^T\end{pmatrix},\qquad
D^2=(-u,t,s,t,s).
\]

The matrices are constructed from the tensor differential; every square is
checked to vanish. Partial purity is a quasi-isomorphism to

\[
\left[
\mathcal C/(s,t)\xrightarrow{-u}\mathcal C/(s,t)
\right]
\]

in cohomological degrees zero and one, with its line factors retained.
Hence the only unspecialized cohomology of `M_loc` is

\[
H^1(\mathcal M_{\mathrm{loc}})=D\langle\tau\rangle.
\]

All other cohomology groups vanish. This exactness follows from the regular
sequence `(s,t,u)` and the previously constructed pair-purity
quasi-isomorphism, not from the finite monomial controls.

## 4. Explicit primitive secondary Bockstein

Define in the full shifted Hom complex

\[
\alpha=-p_u^\vee\otimes z^\vee\in\mathcal M_{\mathrm{loc}}^0,
\qquad
\tau=e_u^\vee\otimes z^\vee\in\mathcal M_{\mathrm{loc}}^1.
\]

The exact matrix identity is

\[
\delta\alpha=u\tau.
\]

Every boundary coefficient in degree one lies in `(u,s,t)`, and the
coefficient of `tau` is one, so `[tau]` is nonzero and primitive over `D`.
After derived restriction to `u=0`, both adjacent grades remain:

\[
H^0(\mathcal M_{\mathrm{loc}}\otimes^{L}\mathcal C/(u))=D[\bar\alpha],
\qquad
H^1(\mathcal M_{\mathrm{loc}}\otimes^{L}\mathcal C/(u))=D[\bar\tau].
\]

The first connecting operation of the `u`-filtration is therefore

\[
\beta_u([\bar\alpha])=[\bar\tau].
\]

This formula uses the declared coordinate `u`. In normal-line invariant
form it reads

\[
\beta([\bar\alpha])=[u]\otimes[\bar\tau].
\]

The target retains `L_partial^vee`, the ordered dual determinant for `(s,t)`,
and, on `tau`, the independent dual `u`-normal. Under `u'=a u`, `tau` changes
by `a^{-1}` and `[u]` by `a`; the invariant formula is unchanged. No equality
with the physical `[dX03]` normal has been made.

The existing sheet/normal reflection is extended by the identity on the
retained `u03` coordinate. The resulting matrices square to one and commute
semilinearly with the full differential. The endpoint sign and ordered-pair
normal sign cancel as before. Both `alpha` and `tau` are fixed in this
framed convention. Neither an endpoint section nor a new polarity sign is
introduced.

## 5. The exact coefficient test for a transported secondary class

A degree-one cochain in `M_loc` has one coefficient:

\[
v=\nu(s,t,u)\tau.
\]

Its class is

\[
[v]=\overline\nu\,[\tau],\qquad
\overline\nu=\nu\bmod(u,s,t).
\]

This includes arbitrary spectator coefficients. It is not a choice among
only `0`, `1`, and `-1`.

The checker explicitly decomposes any polynomial in `(u,s,t)` against the
last row `(-u,t,s,t,s)` to construct its boundary. The residue coefficient
is therefore a complete invariant for this local block.

To apply this test to the physical difference, a source-defined map

\[
\Xi:\operatorname{RHom}(J_M,F_0)\longrightarrow\mathcal M_{\mathrm{loc}}
\]

must first be constructed with its support/endpoint/normal comparisons. If
that map is supplied and both homotopies are defined, then

\[
\Xi_*[\Delta_J]
=
\left(
\Xi(H_C-e_Fh_M)(e_u\otimes z)\bmod(u,s,t)
\right)[\tau].
\]

The present calculation does not assign either of those two top-component
values. In particular, the positive Bockstein calculated in Section 4 is not
proved equal to the conductor–Morse difference just because both have a
possible unit coordinate.

## 6. The native obstruction is also explicit

The earlier native factorization retains

\[
\mathcal L_f:
\mathcal B z\xrightarrow{f(-t,s)^T}\mathcal B^2
\xrightarrow{(s,t)}\mathcal B p,
\]

in homological degrees `3,2,1`, where

\[
f=u_{03}+(1+u_{03})t_{13}X_{13}.
\]

Its native images are `gamma`, the two first primitives, and `Z_*`.
They satisfy `s U_t-t U_s=g_*`, `d Z_*=f g_*`.

Let `D_B=B/(s,t)` and `M_f=B/(f)`. The two homology groups are `D_B` in
degree one and `M_f` in degree two. Their nontrivial attachment (the
Postnikov invariant) is the two-extension

\[
0\longrightarrow M_f
\xrightarrow{1\mapsto(-t,s)}
\mathcal B^2/f\mathcal B(-t,s)
\xrightarrow{(s,t)}\mathcal B
\longrightarrow D_B\longrightarrow0.
\]

Pushing out the standard ordered Koszul two-extension along
`B -> B/(f)` yields this exact sequence. Its class is

\[
1\in\operatorname{Ext}_{\mathcal B}^2(D_B,M_f)
\cong\mathcal B/(f,s,t),
\]

with the ordered determinant retained. This is the invariant of the
specified four-generator native source, not a relabeling of the still
unknown physical `Delta_J`.

The lift criterion can be proved without a dimension count. A degree-zero
map `K_B(s,t)[1] -> L_f` with bottom coefficient `c`, middle matrix `F`,
and top coefficient `h` must satisfy

\[
(s,t)F=c(s,t),\qquad F(-t,s)^T=fh(-t,s)^T.
\]

The regular syzygy implies

\[
F=cI+(-t,s)^T(r_1,r_2),\qquad
c=fh+t r_1-s r_2.
\]

Thus its induced bottom homology coefficient must lie in `f D_B`.
Conversely these formulas supply every such lift. A primitive coefficient
one cannot lift across `f=s=t=0`; multiplication by `f` has the explicit
lift `(f, f I_2,1)`.

This exhibits a genuine nonzero obstruction in the native source. It also
shows why the Gysin two-extension cannot be treated as an already chosen
primitive of the required physical chain equation.

## 7. Verification and scope

`check_secondary.py` reads the exact preceding comparison matrices, constructs
the full tensor/Hom differential, verifies the universal primitive and
Bockstein equations, checks reflection and partial purity, and reconstructs
the source's seven-triangle Morse identity. It passes 529 exact checks.
Polynomial controls are supplementary; the proofs give the unbounded results.

A fresh replay of the earlier supported-Gysin package passed its 11,667
checks and the earlier 5,840 and 6,706 checks. The input matrix hash is retained
in the new certificate. The new certificate explicitly reports that the
physical `Delta_J` is **not determined**; it does not assert missing maps.

Reproduce locally:

```bash
python check_secondary.py
python dependencies/supported_gysin_pair/check_supported_gysin.py
```

### Sources

Marici, fixed commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`:

- `src/ledger/20260814-109 Closed Dual-Star No-Go and the Seven-Triangle Secondary Cobordism.md`:
  definition and typing requirements of the secondary conductor–Morse class.
- `research/voevodsky/check_d03_normalized_blowdown_counit.py`:
  actual occurrence-loaded seven-triangle differential and blowdown.
- `research/voevodsky/check_global_mixed_variance_transform.py`:
  signature-level integration audit, which does not instantiate this comparison.
- Supplied `supported_gysin_t04_t35_package.zip`: actual pair matrices,
  endpoint/normal frames, and native representatives.

Primary mathematical references:

- Stacks Project, Hom complexes: https://stacks.math.columbia.edu/tag/0A8H
- Regular sequences and Koszul exactness: https://stacks.math.columbia.edu/tag/062F
- Cartier duality and the shifted dual normal line: https://stacks.math.columbia.edu/tag/0B4B
- Connecting homomorphisms of complexes: https://stacks.math.columbia.edu/tag/0117
