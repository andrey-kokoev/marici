---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The e6 Bridge Uses Only the Existing Radial and Energy-Sum Divisors

## Question

Entry 370 left open whether the common \(e_6\) second-Rees bridge survives
at every exceptional center in the total-energy double-soft resolution.
The hard-to-vary claim tested here is

\[
\boxed{\text{the }e_6\text{ bridge acquires an undeclared pole or loses its
line at an Entry-370 center.}}
\]

This is a test of one source-defined line and one marked extension column.
It is not a pullback of the complete rank-twelve connection.

## Frozen source objects

The generic total-energy marked extension has

\[
g_{111}^{\rm top}\longmapsto \frac{e_6}{8(x+y)}.
\]

Entry 209 independently established, by exact finite-field reduction at
1024 generic points in each derivative direction, that
\(\langle e_6\rangle\) is an invariant line in the algebraic plane
\(\langle e_6,v_{\rm alg}\rangle\). No projector is fitted here.

## Radial pullback

On the three standard charts of the radial blowup of \((E,x,y)=(0,0,0)\),

\[
\begin{array}{c|c|c}
\text{chart}&(E,x,y)&x+y\\ \hline
E&(u,ur,us)&u(r+s)\\
x&(ur,u,us)&u(1+s)\\
y&(ur,us,u)&u(1+s).
\end{array}
\]

Consequently the bridge is meromorphic after the predeclared Cartier twist
by the radial exceptional divisor and the strict transform of \(x+y=0\):

\[
\boxed{D_{\rm bridge}=D_{\rm radial}+\widetilde{\{x+y=0\}}.}
\]

Both divisors already belong to the frozen normal/energy arrangement.

## Exceptional centers

At the four elliptic modulus base points

\[
[0:1:0],\quad[0:0:1],\quad[2:1:0],\quad[2:0:1],
\]

use the \(x\)- or \(y\)-chart according to the nonzero coordinate.  In
every case the strict factor \(1+s\) equals one. Thus the bridge has only
the radial pole there and acquires no pole from the point-center blowup.

At the four finite conductor--energy tangencies in the \(E\)-chart,

\[
(r,s)=\left(\tfrac12,1\right),\left(1,\tfrac12\right),
\left(\tfrac32,-1\right),\left(-1,\tfrac32\right),
\]

the strict factors \(r+s\) are respectively

\[
\frac32,\quad\frac32,\quad\frac12,\quad\frac12.
\]

Hence the bridge is regular along each tangency center away from the common
radial factor. The divisor \(r+s=0\), where a pole remains, is exactly the
strict transform of the existing energy-sum divisor \(x+y=0\).

## Verdict

The tested claim is falsified:

\[
\boxed{\text{the invariant }e_6\text{ bridge extends through all Entry-370
centers using only }D_{\rm radial}+\widetilde{\{x+y=0\}}.}
\]

No new support factor and no new carrier datum are required for this line.
This closes the \(e_6\)-bridge part of Entry 370's falsifier and strengthens
H2 at the level of one algebraic subline and its marked extension.

## Classification

| Datum | Classification |
|---|---|
| \(\langle e_6\rangle\) | algebraic/Tate coefficient line |
| radial pole \(u^{-1}\) | existing flagged normal geometry |
| strict pole \((x+y)^{-1}\) | existing energy-divisor support |
| four modulus base points | existing signed-energy incidence |
| four conductor--energy tangencies | coefficient-support resolution centers |
| residual new pole | none |
| new carrier datum | none found |

## Epistemic scope and remaining falsifier

The certificate checks exact pullback factors and their nonvanishing at all
eight listed centers. It uses the previously certified invariance of
\(\langle e_6\rangle\). It does not reconstruct or extend every entry of
the rank-twelve Gauss--Manin connection.

The remaining high-entropy test is therefore the full multivariate marked
connection: reconstruct the rank-twelve connection over \((E,x,y)\), pull
it to the frozen resolution, and determine whether every off-diagonal pole
is logarithmic on the existing energy/conductor/Cut boundary. A pole on a
new irreducible base divisor, or unavoidable loss of the extension after
the permitted Cartier/Rees twists, would update H2 toward H3.

## Evidence

- `research/benincasa/marici-gm/src/bin/e6_bridge_exceptional_extension.rs`;
- `research/benincasa/e6-bridge-exceptional-extension-certificate.json`;
- `research/benincasa/full-marked-total-energy-nilpotent.json`;
- `research/benincasa/rees-normalization-E0-E1.json`;
- Entries 209 and 370.
