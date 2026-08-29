# Arithmetic incidence must lift to the complete Green feature space

## Feature-factor route

Assume the complete polarized Green form has a source-derived feature factorization
\[
b_s[h,h]=\|J_sh\|_{\mathcal Z_s}^2,
\]
where
\[
J_s:\mathcal V_s\longrightarrow\mathcal Z_s
\]
is the assembled Green feature map.

The sharp positive constructor is a bounded arithmetic lift
\[
\Lambda_s:\mathcal A\longrightarrow\mathcal Z_s
\]
such that
\[
\langle S_sc,h\rangle
=
\langle\Lambda_sc,J_sh\rangle_{\mathcal Z_s}
\]
for every coefficient \(c\) and test vector \(h\). In rigged-dual notation,
\[
S_s=J_s^*\Lambda_s.
\]

This is the instrument-level lift: arithmetic synthesis is the scalar shadow, while \(\Lambda_sc\) is its continuation-residue packet in the complete Green feature space.

## Immediate consequences

If the factorization exists, then
\[
|\langle S_sc,h\rangle|
\le
\|\Lambda_s\|\,\|c\|_{\mathcal A}\,\|J_sh\|_{\mathcal Z_s},
\]
hence
\[
|\langle S_sc,h\rangle|^2
\le
\|\Lambda_s\|^2\|c\|_{\mathcal A}^2\,b_s[h,h].
\]

Moreover,
\[
h\in\ker J_s
\quad\Longrightarrow\quad
\langle S_sc,h\rangle=0.
\]
Since \(\ker J_s\) is the Green radical, radical annihilation is automatic.

Thus one complete feature lift proves the exact joint Green-form domination gate with
\[
M_C=\sup_{s\in C}\|\Lambda_s\|.
\]

## Equivalence and canonical minimal lift

Conversely, suppose the joint form estimate holds. For each \(c\), the rule
\[
J_sh\longmapsto\langle S_sc,h\rangle
\]
is well-defined and bounded on \(\operatorname{ran}J_s\), because radical annihilation identifies all representatives. It extends to \(\overline{\operatorname{ran}J_s}\), and Riesz representation gives a unique minimal lift
\[
\Lambda_s^{\min}c\in\overline{\operatorname{ran}J_s}.
\]

Any other lift differs by a vector in
\[
(\overline{\operatorname{ran}J_s})^\perp.
\]
Therefore the lift is canonical after imposing the minimal-range condition
\[
\operatorname{ran}\Lambda_s\subseteq\overline{\operatorname{ran}J_s}.
\]

The feature-lift theorem is equivalent to joint domination, but it exposes the source constructor that must actually be built.

## Complete feature packet

The codomain \(\mathcal Z_s\) must be assembled before the lift is tested. Schematically it contains:

- primitive-current features;
- square-current features;
- connected-tail features;
- seam graph features;
- endpoint features;
- archimedean reservoir features;
- reciprocal-sheet features;
- all source-declared mixed comparison features.

The feature norm need not be an orthogonal channel sum. Cross terms are part of the Green geometry and must remain visible in \(J_s\).

Separate identities
\[
S_{s,i}=J_{s,i}^*\Lambda_{s,i}
\]
do not imply
\[
S_s=J_s^*\Lambda_s.
\]
They omit exactly the mixed feature directions and joint radical exposed by the previous hostile.

## Source-native lifting square

The desired constructor is the commutative square
\[
\begin{array}{ccc}
\mathcal A & \xrightarrow{\Lambda_s} & \mathcal Z_s\\
& \searrow_{S_s} & \downarrow J_s^*\\
&&\mathcal V_s^*
\end{array}
\]
with \(\Lambda_s\) uniformly bounded on compact parameter patches.

This square must be natural under cutoff and reciprocal transport. If
\[
j_{X,Y}:\mathcal A_X\to\mathcal A_Y,
\qquad
z_{X,Y}:\mathcal Z_{X,s}\to\mathcal Z_{Y,s}
\]
are the coefficient and feature inclusions, require
\[
z_{X,Y}\Lambda_{X,s}
=
\Lambda_{Y,s}j_{X,Y}
\]
and
\[
z_{X,Y}J_{X,s}
=
J_{Y,s}\iota_{X,Y}.
\]
The reciprocal equations use the declared conjugate-linear feature exchange.

## First-failure classification

Attempting the lift channel by channel yields a precise obstruction packet.

1. **Missing feature constructor:** a boundary channel has no map into \(\mathcal Z_s\).
2. **Radical mismatch:** \(S_s\) does not vanish on \(\ker J_s\).
3. **Unbounded lift:** the minimal \(\Lambda_s^{\min}\) exists pointwise but its norm diverges.
4. **Cutoff drift:** the lift does not commute with labelled inclusion.
5. **Reciprocal drift:** Real transport does not intertwine the lift.
6. **Mixed-feature failure:** channel lifts exist, but no single assembled \(\Lambda_s\) realizes all pairings.
7. **Completion collapse:** finite lifts are uniformly absent or lose norm control in the limit.

This reports an exact missing port rather than a failed scalar inequality.

## Mandatory mixed-feature hostile

Reuse
\[
b((x,y),(x,y))=|x+y|^2.
\]
A complete feature map is
\[
J(x,y)=x+y\in\mathbb C.
\]
For synthesis
\[
\langle Sc,(x,y)\rangle=c(x-y),
\]
no \(\Lambda:\mathbb C\to\mathbb C\) can satisfy
\[
c(x-y)=\langle\Lambda c,x+y\rangle
\]
for all \(x,y\). Setting \(x=1,y=-1\) makes the right side zero and the left side \(2c\).

Yet each coordinate-axis restriction has an apparent one-channel lift. The obstruction is exactly failure to lift into the assembled feature space.

## Euler and Fredholm consequence

Once a compact-locally bounded complete lift exists, the normalized unweighted synthesis is \(\Lambda_s\) on the minimal feature range. Composing with the Euler diagonal gives
\[
T_s=\Lambda_sD_E,
\]
up to the canonical reduced-feature identification. Hence \(T_s\) is compact and retains the primitive, square, and connected Schatten grades.

This proves Fredholm discreteness. It still does not prove
\[
1\notin\sigma(T_sT_s^*).
\]
The RH-bearing gap estimate remains later.

## Next source calculation

Construct \(J_s\) explicitly from the complete polarized Green identity and ask whether each arithmetic prime-power incidence vector has a coherent bounded representative in \(\mathcal Z_s\). The desired theorem is:

> arithmetic incidence admits one cutoff-natural, Real-natural, compact-locally bounded lift into the complete assembled Green feature space.

A positive theorem closes the Fredholm compactness gate. A negative theorem names the first missing or incompatible feature. Either outcome is more informative than another scalar summability computation.
