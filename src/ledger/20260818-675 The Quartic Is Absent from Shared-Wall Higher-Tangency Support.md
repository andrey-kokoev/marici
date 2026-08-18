---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 675 — The Quartic Is Absent from Shared-Wall Higher-Tangency Support

## Hard-to-vary claim

Entry 671 derives quadratic contact between each physical shared wall and
the Cayley--Menger divisor.  A possible geometric home for the algebraic
quartic would be degeneration of that weighted corner: at a repeated
tangential root, the wall-normal derivative of \(K_E\) could vanish on
\(\mathcal Q=0\).

Freeze the three shared walls and eliminate the tangential coordinate from

\[
K_E|_{q_{g_i}}=0,
\qquad
\partial_t(K_E|_{q_{g_i}})=0,
\qquad
\partial_{n_i}K_E=0.
\]

No marked sections or carrier cells are added.

## Symbolic elimination

For each shared wall, \(K_E|_{q_{g_i}}\) is exactly the square of a
quadratic tangency factor \(T_i(t)\).  Compute

\[
R_i=\operatorname{Res}_t(T_i,\partial_{n_i}K_E).
\]

Over \(\mathbb Q[x,y,z]\), the factorizations are

\[
R_1=
4(y+z)^2
(x-y-z)^2(x-y+z)^2(x+y-z)^2
(x+y+z)^4,
\]

\[
R_2=
4(x+z)^2
(x-y-z)^2(x-y+z)^2(x+y-z)^2
(x+y+z)^4,
\]

and

\[
\begin{aligned}
R_3={}&
4z(x+z)(y+z)
(x-y-z)^2(x-y+z)^2(x+y-z)^2(x+y+z)^2\\
&\times(x+2y+z)(2x+y+z).
\end{aligned}
\]

Thus higher tangency is supported on signed-energy, total-energy, soft, and
linear wall-alignment divisors already visible in the frozen energy/wall
geometry.

## Quartic comparison

Exact polynomial gcd gives

\[
\gcd(R_i,\mathcal Q)=1
\qquad(i=1,2,3),
\]

and therefore

\[
\boxed{
\gcd(R_1R_2R_3,\mathcal Q)=1.
}
\]

The claim is falsified:

\[
\boxed{
\mathcal Q
\text{ is not the degeneration divisor of the shared-wall weighted corner.}
}
\]

This strengthens Entry 672.  The complete minimal syzygy module neither
jumps on tested \(\mathcal Q\)-fibers nor acquires a higher
Cayley--Menger/shared-wall tangency there.

## Classification

- existing carrier: the three shared walls and \(K_E=0\);
- higher-tangency support: existing linear energy/wall divisors;
- \(\mathcal Q\): absent;
- new carrier datum: none.

## Scope

The elimination is symbolic over \(\mathbb Q[x,y,z]\).  It identifies the
support where the quadratic local model degenerates.  It does not construct
the weighted Stokes comparison or the physical relative-chain pairing.

## Updated frontier

The remaining credible home of \(\mathcal Q\) is no longer an absolute
divisor, module-rank locus, ordinary conductor, or weighted-corner
degeneration.  Test it only in a source-derived secondary object:

\[
\text{physical relative-chain pairing}
\quad\text{or}\quad
\operatorname{Ext}^1(\mathbb V_{\rm ell},\mathcal T_7).
\]

No scalar projector or fitted pairing is admissible.

## Evidence

- \`research/benincasa/derive_shared_wall_higher_tangency_support.py\`;
- \`research/benincasa/shared-wall-higher-tangency-support.json\`;
- Entries 671--672.

## Outcome contract

~~~json
{
  "claim": "Q is the degeneration divisor of the shared-wall quadratic tangency.",
  "status": "falsified",
  "wall_resultant_gcds_with_Q": ["1", "1", "1"],
  "product_gcd_with_Q": "1",
  "higher_tangency_support": "linear energy, soft, and wall-alignment divisors",
  "new_carrier_datum": false,
  "next_experiment": "Test Q only in a source-derived physical-chain pairing or algebraic-elliptic extension class."
}
~~~
