# The oriented conductor residue gives zero v_alg parity

Pointwise numerator values were insufficient because the Gysin pairing must include both the Poincare-residue Jacobian and the local smoothing coordinate.

On the normalized cusp chart \(X_1=1,X_2=r\), let

\[
N_v=2r^2a^2-2r^2b^2-r^4+r^2
\]

be the \(v_{\rm alg}\) numerator. On the conductor, parameterized by \(m\), its Poincare residue is

\[
\omega_v=rac{N_v\,da}{\partial_bQ}.
\]

The local smoothing coordinate is

\[
g(m)=\frac{m(m+1)(1-mr)}{(m^2r+1)^2}.
\]

Therefore the relevant local Gysin coefficients are

\[
\left.\frac{\omega_v}{dg}\right|_{p_i}.
\]

At the cyclically ordered points

\[
(p_{++},p_{-+},p_{--},p_{+-}),
\]

they equal

\[
r^2(r-1)(r+1)\,(-1,+1,-1,+1).
\]

Removing the common nonzero kinematic unit gives the primitive integral coefficient vector

\[
(-1,+1,-1,+1).
\]

The Bunch--Davies oriented Cech chain has primitive half-boundary

\[
(1,-1,1,-1).
\]

Their integral pairing is

\[
(-1)(1)+(1)(-1)+(-1)(1)+(1)(-1)=-4.
\]

Hence

\[
\left\langle2m,v_{\rm alg}^\vee\right\rangle
\equiv -4\equiv0\pmod2.
\]

Thus the second bit is

\[
b=0.
\]

Unlike the invalid base-divisor argument, this calculation occurs entirely in the fiber specialization geometry: it uses the conductor Poincare residue, the smoothing coordinate, and the oriented integral boundary chain.

Combined with the primitive paired-node calculation along the geometrically normalized \(e_6\)-line, it gives

\[
(a,b)=(1,0),
\]

subject only to the declared ordering in which \(e_6\) is the first coordinate and \(v_{\rm alg}\) the second.

Certificate:

- `research/voevodsky/checkers/valgebraic_conductor_residue_pairing.py`;
- `research/voevodsky/results/valgebraic_conductor_residue_pairing.json`.
