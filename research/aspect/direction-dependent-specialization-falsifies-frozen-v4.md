# Direction-dependent specialization falsifies frozen v4

## Target

Frozen v4 attaches one radical jet filtration to a singular stratum and allows a normal parameter or normal cone. It does not resolve normal directions into their own strata or define gluing between direction-dependent filtrations.

## Hostile packet

Consider

\[
G(x,y)=
\begin{pmatrix}x&0\\0&y\end{pmatrix}.
\]

At the origin the radical is two-dimensional. The first crossing form in normal direction \((a,b)\) is

\[
B_{(a,b)}=
\begin{pmatrix}a&0\\0&b\end{pmatrix}.
\]

For generic directions it has rank two. On either coordinate direction it has rank one. Thus no single nondegenerate first crossing form exists over the whole punctured normal cone.

The filtration also depends on the approach curve:

- along \((x,y)=(t,t)\), both radical directions return at first order and \(\det G=t^2\);
- along \((x,y)=(t,t^2)\), the directions return at orders one and two and \(\det G=t^3\);
- along \((x,y)=(t,0)\), one direction never returns and the path remains singular.

These are not coordinate presentations of one fixed filtration. They are distinct specialization types meeting at the same singular point.

## Decision

Frozen v4 is falsified.

Its normal-cone field can name the set of directions, but it cannot represent the change of filtration across that set. It lacks:

- a projectivized normal-direction object;
- a blowup or normal-resolution arrow;
- exceptional-direction strata;
- direction-indexed radical filtrations;
- gluing cells between generic and exceptional directions.

Adding more jets at the origin does not solve the problem. The obstruction is directional incidence, not insufficient Taylor order along one chosen path.

## Required future repair

A future v5 would need to replace a singular point by its resolved normal directions. For this packet, the projectivized normal cone is a line of directions with two exceptional points corresponding to the coordinate axes.

The required data are:

1. a blowup or equivalent normal-resolution object;
2. a filtration over each resolved direction;
3. strata where the leading crossing rank drops;
4. transition maps between generic and exceptional direction charts;
5. compatibility with radical quotient, associator, exchange, and exposure cells;
6. invariance under changes of generators of the same divisor ideal.

## Network meaning

At a transverse intersection of two defect divisors, network topology depends on which composite comparison is approached and how. A single additive channel count at the intersection is insufficient. The exceptional-direction data decide whether branches share an adapter, require replicated local cells, or remain singular.

This gives a precise discriminator between expressions such as \(3+2+1\) and \(2(2+1)+1\): their difference can live on the resolved normal-direction space even when the unresolved singular fiber has the same total rank.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v4_direction_dependent_specialization_falsifier.py
```
