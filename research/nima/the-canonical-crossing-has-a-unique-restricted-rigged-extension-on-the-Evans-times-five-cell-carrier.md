# The canonical crossing has a unique restricted rigged extension on the Evans-times-five-cell carrier

## Scope

A full extension of `T_PB` to every strong-dual pair tensor is unnecessary.
The independent Evans test uses only a regular theta/Evans first leg and one of
five fixed second-leg distributions.

Let

\[
\mathcal S\subset L^2\subset\mathcal S'
\]

be the Schwartz rigging and let

\[
M_5=\operatorname{span}(\Phi,\mathbf1,\delta_0,K,V)
\subset\mathcal S'.
\]

The theta forcing and stable Evans histories are rapidly decreasing on each
weighted stable chart, so their chart restrictions define admissible regular
first legs.

## Partial-transpose construction

For every continuous scalar coordinate `ell` of the bordered target, the
regular crossing defines a continuous bilinear form

\[
b_\ell(f,g)=\ell(T_{PB}(f\otimes g)),
\qquad f,g\in\mathcal S.
\]

On a theta-generated first leg `f`, shell localization, multiplication by the
rapid theta coefficients, differentiation, endpoint trace, and Laplace
readout leave the uncontracted second-leg kernel in `S`. Thus there is a
Schwartz function

\[
h_{\ell,f}\in\mathcal S,
\qquad
b_\ell(f,g)=\langle g,h_{\ell,f}\rangle.
\]

Define the restricted rigged crossing by partial transpose:

\[
\boxed{
\ell(T_{PB}^{\rm rig}(f\otimes S))
:=\langle S,h_{\ell,f}\rangle,
\qquad S\in M_5.
}
\]

This agrees with the original crossing when the second leg is regular. Since
`S` is dense and the target coordinates separate the bordered response, the
extension is unique on the stated restricted carrier.

## Four formerly missing evaluations

The construction gives, coordinatewise,

\[
T_{PB}^{\rm rig}(f\otimes\delta_0):
\quad h_{\ell,f}(0),
\]

\[
T_{PB}^{\rm rig}(f\otimes\mathbf1):
\quad\int_{\mathbb R}h_{\ell,f}(q)\,dq,
\]

\[
T_{PB}^{\rm rig}(f\otimes K):
\quad\int_{\mathbb R}|q|h_{\ell,f}(q)\,dq,
\]

and

\[
T_{PB}^{\rm rig}(f\otimes V):
\quad\langle V,h_{\ell,f}\rangle.
\]

All are finite because `h_(ell,f)` is Schwartz. No distribution product is
used.

## Fourier covariance

Fourier transform is continuous on `S` and `S'`, and partial transpose gives

\[
T_{PB}^{\rm rig}(Ff\otimes FS)
=F_B T_{PB}^{\rm rig}(f\otimes S)
\]

whenever the regular crossing obeys its declared Fourier/Tate covariance.
Therefore the orbit

\[
\delta_0\leftrightarrow\mathbf1,
\qquad
K\mapsto V\mapsto-K
\]

is preserved automatically rather than assigned as new output data.

## Seam, cutoff, and jets

Translation is continuous on both sides of the Schwartz rigging and commutes
with partial transpose. Finite prime restriction acts only on labels and hence
commutes exactly. Parameter differentiation acts on the regular first leg;
theta decay supplies one common Schwartz majorant for every finite jet on a
compact spectral set. Thus moving seams, cutoffs, and finite parameter jets
commute with `T_PB^rig`.

## Application to the defect point

The independent bridge is now well typed:

\[
T_{PB}^{\rm rig}\epsilon_{\rm Ev}^{(j)}(u_z)
=
T_{PB}^{\rm rig}
\left((u_z\otimes\Phi)\oplus(u_z\otimes F^jK_1)\right).
\]

The identity

\[
\partial K_1=D_1
\]

is preserved by distributional duality and therefore by the extended crossing.

## Remaining computation

The extension closes the domain/type gate. It does not evaluate the
coordinate kernels `h_(ell,u_z)`. The next step is to extract those kernels
from the explicit shell-localization formula and form the transverse defect.
Only that frozen result may be tested for nonzero `tau`-divisibility.