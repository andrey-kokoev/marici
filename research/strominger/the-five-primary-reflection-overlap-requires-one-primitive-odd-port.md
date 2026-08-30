# The Five-Primary Reflection Overlap Requires One Primitive Odd Port

> Scope correction: this theorem classifies repair ports conditional on a source-derived higher-spin attachment. In the completed Bondi/Einstein magnetic source only spin two is authorized, and its modulus seven is not exceptional. The spin-four instance is a formal covariant Laurent extension, not a physical Einstein sector.

## Result

Let (s\geq1), (n=4s-1), and let the two reflected affine observations be

\[
\ell(x,y)=3x-2y,
\qquad
\ell_X(x,y)=3y-2x
\pmod n.
\]

Their joint kernel has order

\[
\lvert\ker(\ell,\ell_X)\rvert=\gcd(n,5).
\]

Consequently the reflected packet is already faithful unless

\[
s\equiv4\pmod5.
\]

At precisely those spins, one additional primitive reflection-odd port

\[
r(x,y)=x-y\pmod n
\]

restores faithfulness. Thus the algebraic repair demand is periodic: zero extra ports off the exceptional congruence class and exactly one primitive odd port on it.

This is a statement about the observation lattice. It predicts the type of a missing constructor; it does not by itself authorize a physical instrument implementing (r).

## Proof

Adding and subtracting the reflected observations gives

\[
q_+=\ell+\ell_X=x+y,
\qquad
q_-=\ell-\ell_X=5(x-y).
\]

Because (n) is odd, multiplication by (2) is invertible modulo (n). The even coordinate (x+y) is therefore primitive. The only possible loss occurs in the odd coordinate, where multiplication by (5) has kernel of order (gcd(n,5)). This proves the kernel formula.

If (5\nmid n), then (5^{-1}) exists modulo (n), and

\[
r=5^{-1}(\ell-\ell_X).
\]

The proposed odd port is then a derived readout and adds no information.

If (5\mid n), write (d=n/5). The five elements

\[
j(d,-d),\qquad j=0,1,2,3,4,
\]

lie in the joint kernel. Their odd-port values are (2jd), which are distinct modulo (n). Hence (r) separates the entire fivefold fibre.

Finally, the augmented packet contains (x+y) and (x-y). Since (2) is invertible modulo (n), these reconstruct

\[
x=\frac{(x+y)+(x-y)}2,
\qquad
y=\frac{(x+y)-(x-y)}2.
\]

The augmented observation is therefore injective for every integer spin.

## Minimality and source authority

At an exceptional spin the original packet has a nontrivial fibre of prime order five, so no repair with zero additional information can be faithful. A single cyclic scalar port is sufficient exactly when its restriction to that fibre is nonzero. The primitive odd port has this property because multiplication by (2) is invertible modulo five.

One must not obtain this repair by formally dividing (q_-) by five on the exceptional stratum. Division is unavailable there and would turn a failed observation into fictitious authority. A legitimate repair requires an independently source-authorized constructor whose readout is primitive on the reflection-odd lattice.

More generally, consider any scalar port

\[
p_{u,v}(x,y)=ux+vy\pmod n.
\]

On the kernel generator (d(1,-1)), it has value (d(u-v)). Therefore it repairs the exceptional fibre if and only if

\[
u-v\not\equiv0\pmod5.
\]

This classifies every one-port linear repair. The essential property is not the literal coordinate (x-y), but primitivity on the reflection-odd quotient. Ports with (u\equiv v\pmod5) remain blind and must be rejected even if they add a numerically nonzero field to the record.

For spin four, (n=15). The blind fibre is

\[
(0,0),(3,12),(6,9),(9,6),(12,3),
\]

and (r) reports respectively (0,6,12,3,9). The five states become distinguishable with one port.

## Interpretation

The factor five is not a new five-state carrier appended to the system. It measures an imprimitive embedding of the reflection-odd coordinate into the two-chart observation packet. The exceptional congruence class is where that embedding ceases to be faithful.

The resulting distinction is sharp:

- the affine discriminant (n=4s-1) is the size of the oriented cyclic charge packet;
- reflection combines two oriented charts;
- the coefficient five measures their odd-coordinate overlap;
- the extra port repairs observation faithfulness only when that overlap acquires a kernel.

## Bounded replay

The dependency-free checker enumerates every pair in ((\mathbb Z/n)^2) for (1\leq s\leq20). It verifies the kernel and image formulas, the redundancy of (r) away from the exceptional class, its separation of the exceptional fibre, augmented injectivity, the explicit spin-four packet, and the complete (u-v) criterion for scalar repair ports modulo fifteen.

Run:

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/primitive_odd_port_periodic_repair_checks.py
```

Machine-readable output is written to `research/strominger/results/primitive_odd_port_periodic_repair_checks.json`.
