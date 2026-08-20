# Generic-Q raw log-smoothness audit for the frozen `q_G12` residue

## Verdict

The exact raw discriminant census has no `Q` component, but the requested
relative/log Gauss-Manin theorem is **not derivable from the frozen data**.

The checker proves, over the full multivariate ring `Q[x,y,z]`, that the
irreducible source polynomial `Q` divides none of the 1,719 nonconstant
surface, line, pair-incidence, or triple-incidence conditions constructed
from the ledger-161 data.  It does not use the old `x=1,y=2` specialization.

Exhaustiveness for a log Gauss-Manin object fails one step earlier: no
source-fixed labelled and sheeted log divisor is specified for the two
four-pole residue summands.  Consequently there is also no specified
simultaneous log resolution or lifted physical relative/Borel--Moore chain.
The raw projective arrangement cannot stand in for that missing datum: it is
not SNC at generic kinematics.

The executable certificate is
[`check_generic_q_log_smoothness.rs`](check_generic_q_log_smoothness.rs).
It does not modify any ledger file.

## Frozen algebra

Put

\[
 E=x+y+z,\qquad h=x^2+y^2-z^2,
\]

\[
 A=(x-y)^2-z^2,\qquad B=(x+y)^2-z^2,
\]

\[
 Q=4AB-(A+B-E^2)^2.
\]

The compactified branch model is

\[
 \overline S:\quad W^2=\overline K(a,b,s),
\]

\[
\begin{aligned}
\overline K={}&x^2(a^2-(E^2+y^2)s^2)^2\\
&-h(a^2-(E^2+y^2)s^2)(b^2-(E^2+x^2)s^2)\\
&+y^2(b^2-(E^2+x^2)s^2)^2+E^2ABs^4.
\end{aligned}
\]

This is exactly the homogenization of the frozen affine `K0(a,b)`.

## Exact irreducibility of `Q`

Use the invertible linear coordinate change `z=E-x-y`.  Then

\[
 Q=-16y^2x^2+8E^2(E-y)x+E^3(8y-5E).
\]

It is primitive as a polynomial in `x` over `Q[y,E]`: every divisor of its
leading coefficient divides `y`, while `y` does not divide `8E^2(E-y)`.
Its quadratic discriminant is exactly

\[
 \operatorname{Disc}_x(Q)
 =64E^3(E-2y)^2(E+2y).
\]

The irreducible, nonassociate linear factors `E` and `E+2y` have odd
valuations.  The discriminant is therefore not a square in `Q(y,E)`, so the
quadratic is irreducible there.  Gauss's lemma and the invertible coordinate
change prove that the source `Q` is irreducible in `Q[x,y,z]`.

For every candidate `P`, the checker performs fraction-free pseudo-division
of `P` by `Q` in `z`.  The leading `z` coefficient of `Q` is the nonzero
constant `-5`; hence

\[
 \operatorname{prem}_z(P,Q)=0
 \quad\Longleftrightarrow\quad
 Q\mid P\text{ in }\mathbb Q[x,y,z].
\]

Every reported remainder is nonzero.  `--emit-polynomials` prints each exact
candidate and its exact remainder.

## Surface and branch-cover singularities

Write `U=a^2`, `V=b^2`, `T=s^2`.  The gradient of the biquadratic branch
quartic is controlled by

\[
N=
\begin{pmatrix}
2x^2&-h&G_a\\
-h&2y^2&G_b\\
G_a&G_b&2H
\end{pmatrix},
\]

where

\[
G_a=h(x^2+E^2)-2x^2(y^2+E^2),
\]

\[
G_b=h(y^2+E^2)-2y^2(x^2+E^2),
\]

\[
H=z^2(E^4-hE^2+x^2y^2).
\]

The exact determinant identities are

\[
\det N=-2E^2(AB)^2,
\]

\[
\det N_{UV}=-AB,
\]

\[
\det N_{UT}=-AB(E^2-x^2)^2,
\qquad
\det N_{VT}=-AB(E^2-y^2)^2.
\]

Together with the three axis coefficients `x^2`, `y^2`, and `H`, these are
an exhaustive coordinate-stratified singularity test: at a putative
singular point, respectively three, two, or one of `a,b,s` are nonzero.
The checker also tests the named codimension-one factors individually.

On `D_infinity={s=0}` the binary quartic is

\[
x^2a^4-ha^2b^2+y^2b^4
\]

and has exact discriminant

\[
16x^2y^2(AB)^2.
\]

The coordinate-line discriminants are

\[
\operatorname{Disc}(\overline K|_{a=0})
=16y^2H\,[AB(E^2-y^2)^2]^2,
\]

\[
\operatorname{Disc}(\overline K|_{b=0})
=16x^2H\,[AB(E^2-x^2)^2]^2.
\]

None of these determinant, coefficient, or discriminant polynomials has a
`Q` factor.

## Complete raw marked-line census

The eight nonconstant source lines are

| label | projective equation | active in residue union |
|---|---|---:|
| `q_g1` | `b-(y+z)s=0` | yes |
| `q_g2` | `a-(x+z)s=0` | yes |
| `q_g3` | `a+b+zs=0` | yes |
| `q_g12` | `a+b+(x+y)s=0` | no |
| `q_g23` | `b-xs=0` | yes |
| `q_g31` | `a-ys=0` | yes |
| `q_G23` | `a+Es=0` | no |
| `q_G31` | `b+Es=0` | no |

The active-five set is only the union of the two printed four-pole summands

\[
\{q_{g1},q_{g2},q_{g3},q_{g23}\},\qquad
\{q_{g1},q_{g2},q_{g3},q_{g31}\}.
\]

It is not itself the pole set of one summand.

For `sigma,tau in {+1,-1}`, the twelve signed face lines are

\[
a+(\sigma E-\tau y)s=0,
\]

\[
b+(\sigma E-\tau x)s=0,
\]

\[
-\sigma a+b-\tau zs=0.
\]

The checker includes all twelve, `a=0`, `b=0`, and `D_infinity`, for a total
of 23 labelled projective lines.

Each signed face line has a source-forced square restriction.  Before
homogenization, exact square roots are

\[
R_{ca}=-E(a^2+b^2-z^2)-\sigma a(E^2+b^2-x^2),
\]

\[
R_{cb}=-E(a^2+b^2-z^2)-\sigma b(E^2+a^2-y^2),
\]

\[
R_{ab}=a(E^2+b^2-x^2)-\sigma b(E^2+a^2-y^2).
\]

After imposing the corresponding affine face equation and homogenizing the
resulting quadratic, the checker verifies

\[
\overline K|_{L}=R_L^2
\]

for every signed branch.  Its line-degeneration condition is therefore the
binary-quadratic discriminant of `R_L`; the other lines use the full
binary-quartic discriminant.  This gives 23 exact line conditions: 15 label
occurrences on 12 forced-square supports and eight ordinary quartics.

## Pair and triple incidence formulae

Represent every projective line by

\[
\ell_i=(\alpha_i,\beta_i,\gamma_i),\qquad
L_i=\alpha_i a+\beta_i b+\gamma_i s.
\]

For every pair, the checker computes the exact projective intersection

\[
p_{ij}=\ell_i\times\ell_j.
\]

The exact branch-at-intersection condition is

\[
P_{ij}=\overline K(p_{ij})=0.
\]

For affine-parallel lines the common scaling factor in `p_ij` is removed:
the branch value is evaluated at their fixed point
`[a:b:s]=[beta_i:-alpha_i:0]`, while the nonzero component of the cross
product is separately retained as the exact line-coincidence condition.
There is no parameter-dependent direction: parallelism itself is either
universal or impossible.

For every triple, the exact concurrence condition is

\[
T_{ijk}=\det
\begin{pmatrix}
\alpha_i&\beta_i&\gamma_i\\
\alpha_j&\beta_j&\gamma_j\\
\alpha_k&\beta_k&\gamma_k
\end{pmatrix}=0.
\]

Checking all triples is sufficient for higher marked-line incidence on a
surface: every incidence of four or more supports contains a concurrent
triple.

The exact census is:

| class | count |
|---|---:|
| labelled lines | 23 |
| line/branch discriminants | 23 |
| all pairs | 253 |
| universally identical labelled pairs | 3 |
| universally affine-parallel, nonidentical pairs | 60 |
| nonconstant line-coincidence conditions | 60 |
| nonconstant branch-at-pair conditions | 250 |
| all triples | 1,771 |
| universally concurrent triples | 243 |
| impossible (nonzero constant determinant) triples | 168 |
| nonconstant triple-incidence conditions | 1,360 |

Every one of the 60 coincidence, 250 branch-at-pair, and 1,360 triple
polynomials has nonzero multivariate remainder modulo `Q`.

## Why this is not a log-smoothness theorem

Three labels have identical support for every kinematic value:

\[
q_{g1}=cb--,\qquad q_{g2}=ca--,\qquad q_{g3}=ab--.
\]

Before identifying those duplicate labels, the affine direction classes
have sizes `8,8,4,2`.  After identifying them, the distinct-support sizes are
still

\[
7,7,3,2.
\]

Every class meets `D_infinity` at one projective point.  At generic `Q=0`
the corresponding branch values are respectively `y^2`, `x^2`, and `z^2`,
none of which has `Q` as a component.  Thus the cover is etale at the generic
direction points, and each direction point lifts to two points through which
all those distinct marked supports and `D_infinity` pass.  The reduced raw
arrangement is therefore not SNC generically; this is not a special
`Q`-degeneration.

Moreover, the twelve face pullbacks split into two sheets because their
restrictions are exact squares.  Ledger 161 does not specify which sheet,
label, multiplicity, or variance belongs to `D_pole` versus `D_minor`, and
the active-five union conflates two separate four-pole summands.

This omission changes the discriminant problem itself.  For total pullbacks,
`Kbar(p_ij)=0` is the exact condition that the two points over a base-line
intersection coalesce.  For selected split components one must additionally
compare the signed values `W=+R_i`, `W=-R_i`, `W=+R_j`, and `W=-R_j` at that
intersection.  Which equalities are relevant cannot be determined until the
source fixes the sheet labels and divisor roles.  The raw pair census is
therefore not silently presented as an exhaustive sheet-level census.

The first missing datum is therefore:

> A source-fixed labelled and sheeted log divisor for each of the two
> four-pole residue summands.

Without that datum there is no defined log pair to resolve.  A simultaneous
log resolution and lifted physical relative/Borel--Moore chain are later
missing data.  This audit does not invent any of them.

Accordingly, the strongest justified statement is

\[
\boxed{Q\text{ is not a component of any codimension-one discriminant in the
explicit maximal raw support census.}}
\]

It is **not** justified to conclude that the source relative/log
Gauss--Manin connection is regular at generic `Q=0`, that its residue is zero
in a regular gauge, that its monodromy is the identity, or that a
`Q`-supported extension/sign line cannot occur.  Those conclusions require
the missing source-fixed log/relative object and chain.

## Reproduction

From a Visual Studio Developer Command Prompt:

```powershell
rustc --edition 2021 -D warnings -C opt-level=2 `
  research/benincasa/check_generic_q_log_smoothness.rs `
  -o target/check_generic_q_log_smoothness.exe
./target/check_generic_q_log_smoothness.exe
```

To print all exact expanded candidates and remainders:

```powershell
./target/check_generic_q_log_smoothness.exe --emit-polynomials
```

The verified run reported 5,261 fail-closed assertions and 1,719
multivariate `Q`-component rejections, with status
`EXHAUSTIVENESS_BLOCKED_NO_GAUSS_MANIN_THEOREM`.
