# 3837 — The Source Prescription Fixes the Same Bypass at Both Active Conductors

## Question

Do the logarithmic sheet switches on the two literal physical wall segments require an arbitrary finite-part convention, or does the frozen source prescribe their local passage?

## Frozen data

Use the (q_{\mathcal G_{12}})-residue Cayley–Menger polynomial (K(a,b;x,y,z)), the strict positive triangle chamber, and the two wall coordinates

\[
q_1=b-y-z,
\qquad
q_2=a-x-z.
\]

On the walls, Entry 3826 gives

\[
K|_{q_1=0}=R_1(a)^2,
\qquad
K|_{q_2=0}=R_2(b)^2.
\]

No independent wall period or finite subtraction is admitted.

## Exact transverse models

Define

\[
S_1=\left.\frac{\partial K}{\partial b}\right|_{b=y+z},
\qquad
S_2=\left.\frac{\partial K}{\partial a}\right|_{a=x+z}.
\]

Then locally

\[
K=R_i^2+q_iS_i+O(q_i^2).
\]

Exact reduction on the conductor gives

\[
S_1\bmod R_1
=
\frac{2(y+z)(x-y-z)(x-y+z)(x+y-z)(x+y+z)^2}{x},
\]

\[
S_2\bmod R_2
=
\frac{2(x+z)(x-y-z)(x-y+z)(x+y-z)(x+y+z)^2}{y}.
\]

Every factor except (x-y-z) is positive in the strict triangle chamber. Hence

\[
S_1<0,
\qquad
S_2<0
\]

at the selected positive conductor roots.

The transversality resultants are

\[
\operatorname{Res}_a(R_1,S_1)
=4(y+z)^2(x-y-z)^2(x-y+z)^2(x+y-z)^2(x+y+z)^4,
\]

\[
\operatorname{Res}_b(R_2,S_2)
=4(x+z)^2(x-y-z)^2(x-y+z)^2(x+y-z)^2(x+y+z)^4.
\]

They do not vanish in the strict triangle chamber. Thus both conductor crossings are nondegenerate; their only degenerations occur on already frozen triangle or soft support.

## Source boundary value

The source prescription (q_i\mapsto q_i-i0) gives, at either crossing,

\[
K\mapsto r_i^2-i0S_i=r_i^2+i0|S_i|.
\]

Therefore both literal wall segments inherit the same source-normalized square-root bypass. The local passage is not a free finite-part choice.

At ((x,y,z)=(2,3,4)), the exact transverse values are

\[
S_1=-8505,
\qquad
S_2=-4860.
\]

## Narrow result

The physical (i\epsilon) prescription fixes the local branch passage at both active conductors, and no new support divisor is required. This does not split the unsplit five-wall relative cocycle into independently meaningful wall periods, nor does it yet compute the complete source-normalized Leray covector.

## Durable artifacts

- `research/benincasa/checkers/check_rank26_active_conductor_transverse_i0_model.py`
- `research/benincasa/results/rank26-active-conductor-transverse-i0-model.json`

The checker passes all eight exact gates.

## Next falsifier

Transport the oriented wall forms through these two prescribed local bypasses and test whether their regulated endpoint and conductor terms combine into a lift-independent relative-chain functional. Any dependence on separately chosen wall finite parts rejects the proposed physical covector; cancellation inside the unsplit source cocycle advances the direct rank-26 readout.
