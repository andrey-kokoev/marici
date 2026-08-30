# A fixed local character frame gives an exact Adams type functor on the odd auxiliary sector

## Local phase fiber

For each prime \(p\), choose the source-relative character parameter \(\eta_p\) and displacement \(h_{\eta_p}\) used in the divisor-free odd construction.

Define the fixed local phase fiber

\[
F_p^{\mathrm{phase}}
=
\operatorname{span}
\left\{
f_{\eta_p}^{\mathrm{even}},
f_{\eta_p}^{\mathrm{odd}}
\right\}
\subset
\mathcal S(\mathbb Q_p).
\]

The parity-changing finite difference acts internally:

\[
P_{\eta_p}
f_{\eta_p}^{\mathrm{odd}}
=
2\sin\left(\frac{2\pi}{p}\right)
f_{\eta_p}^{\mathrm{even}}.
\]

This fiber is defined before any multiplicative prime-power grade.

## Grade-labelled source object

Let \(E_{p,k}\) be the one-dimensional external label line for the prime-power grade \((p,k)\). Define

\[
F_{p,k}^{\mathrm{odd}}
=
E_{p,k}\otimes F_p^{\mathrm{phase}}.
\]

The grade and the local additive phase are now separate typed factors:

\[
\text{multiplicative grade}
\quad\otimes\quad
\text{fixed additive conductor frame}.
\]

This is not an identification chosen after constructing unrelated fibers. It is one tensor-product source definition for all grades.

## Adams type map

For an Adams arrow \(k\to rk\), let

\[
\alpha_{r;p,k}:E_{p,k}\to E_{p,rk}
\]

be the canonical relabelling of the external grade basis. Define

\[
A_{r;p,k}^{\mathrm{odd}}
=
\alpha_{r;p,k}
\otimes
I_{F_p^{\mathrm{phase}}}.
\]

Then

\[
A_{1;p,k}^{\mathrm{odd}}=I
\]

and

\[
A_{s;p,rk}^{\mathrm{odd}}
A_{r;p,k}^{\mathrm{odd}}
=
A_{sr;p,k}^{\mathrm{odd}}.
\]

Thus the odd auxiliary type fibers form an exact functor on the divisibility action category.

## Grade-six diamond

At the first hostile diamond,

\[
1\to2\to6
\]

and

\[
1\to3\to6,
\]

both composites are

\[
\alpha_{6;p,1}
\otimes
I_{F_p^{\mathrm{phase}}}.
\]

Therefore

\[
A_{3;p,2}^{\mathrm{odd}}A_{2;p,1}^{\mathrm{odd}}
=
A_{2;p,3}^{\mathrm{odd}}A_{3;p,1}^{\mathrm{odd}}
=
A_{6;p,1}^{\mathrm{odd}}.
\]

No associator phase appears in this strict external-label presentation.

## Full weighted odd lift

Combine:

- Euler residue
  \[
  \rho_r(p,k)=\frac1r p^{-(r-1)k/2};
  \]
- moving-seam transport \(T_{r;k}\);
- the odd type map.

Then

\[
\Psi_{r;p,k}^{\mathrm{odd}}
=
M_{\rho_r(p,k)}
\otimes
T_{r;k}
\otimes
A_{r;p,k}^{\mathrm{odd}}
\]

satisfies

\[
\Psi_{s;p,rk}^{\mathrm{odd}}
\Psi_{r;p,k}^{\mathrm{odd}}
=
\Psi_{sr;p,k}^{\mathrm{odd}}.
\]

The odd auxiliary Adams tower is therefore functorial at finite level.

## Why this does not trivialize the full type bundle

Primitive, square, and connected Euler channels have different anomaly and operator-ideal types. They are not all identified by this construction.

The result applies only to the added local phase fiber whose conductor frame is deliberately held fixed while the external multiplicative grade changes.

Thus it gives a constructed subfunctor

\[
F^{\mathrm{odd}}
\subset
F^{\mathrm{full}},
\]

not a global trivialization of every RH type fiber.

## Competing dilation interpretation

There is another possible source action: multiplicative dilation may act directly on the local additive variable \(x\). Under such an action, the character parameter and conductor change.

That is a different constructor from external grade relabelling. It must not be silently identified with \(A_{r;p,k}^{\mathrm{odd}}\).

The present functor is authorized precisely when Adams acts on the prime-power grade, seam displacement, and Euler weight while leaving the local phase probe as a fixed observer frame.

A comparison with local additive dilation remains an independent naturality square.

## Completion profile

The fixed phase factor adds no constructor-depth order drift. All order growth comes from the Euler coefficient already computed:

\[
r_k=\frac{k}{2}+1,
\qquad
\eta_k=\frac12+\frac1k.
\]

Hence the exact type functor is compatible with the bounded intensive order profile of the odd Adams ray.

## Consequence for the SCC frontier

The formal slot

\[
\texttt{type\_fiber\_adams\_composition}
\]

remains open for the full RH packet.

But its odd auxiliary restriction now has an explicit source realization and passes the grade-six composition gate.

This should be recorded as partial constructor coverage rather than as closure of the whole slot.

## Hostiles

1. Promote the odd subfunctor to all primitive, square, and connected types.
2. let additive conductor drift while claiming the fixed-frame composition law.
3. identify external grade relabelling with local additive dilation.
4. forget the prime label in the phase fiber.
5. claim full Adams completion from the grade-six odd diamond alone.

## Verdict

The divisor-free finite phase port admits a canonical Adams type lift when it is defined as a fixed local observer fiber tensored with the external prime-power grade.

This closes type-fiber composition on the odd auxiliary sector, including the grade-six diamond, while leaving the full Euler anomaly bundle unresolved.
