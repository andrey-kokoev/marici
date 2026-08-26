# Dyadic passive bath refinement

Owner: `marici.Aspect`

Strength: finite-cutoff theorem with an analytic uniform-error certificate.

## Bounded question

Can a sequence of finite frequency-bin bath dilations preserve exact quantum
passivity at every cutoff and converge uniformly to a declared
frequency-dependent transfer?

## Source and frame

The source is the explicitly declared rational response on \(0\leq x\leq1\),

\[
t(x)=\frac{1-x^2}{1+x^2},\qquad
l(x)=\frac{2x}{1+x^2}.
\]

It obeys \(t(x)^2+l(x)^2=1\). This is a mathematical passive response, not a
source-derived susceptibility of a material. The frequency frame, interval,
dyadic cells, and their ordering are fixed before sampling.

## Ports and constructor order

Each dyadic cell has one retained system port and one orthogonal bath port.
Constructor order is: choose the mesh, sample \((t,l)\) at the declared point,
form the exact two-port unitary, assemble the frequency-diagonal direct sum,
detect the system bins, then trace the bath. Both midpoint and left-endpoint
sampling are retained as explicit branches.

Every rational sample lies exactly on the passive unit circle, so every finite
cutoff preserves the output commutator. The detector remains frequency-bin
resolved; bin aggregation is a later readout map.

## Uniform convergence certificate

Direct differentiation gives

\[
|(t,l)'(x)|^2=\frac{4}{(1+x^2)^2}\leq4.
\]

Thus the response is 2-Lipschitz. On an \(n\)-cell mesh, midpoint sampling has
uniform vector-error bound \(1/n\), while left-endpoint sampling has bound
\(2/n\). The exact checker records the strictly decreasing bounds for
\(n=1,2,4,8\). Both branches converge; midpoint sampling has the sharper
certificate by a factor of two.

## Conserved quantities and hostile

System-plus-bath photon number and all finite-cutoff canonical commutators are
conserved. Retained system number may dissipate into the bath. A fixed one-bin
model is the smallest hostile: it is exactly passive and can preserve a scalar
calibration value, yet it supplies no vanishing refinement bound.

## Completion gate

This construction proves convergence to the response that was supplied. It
does not derive that response from source dynamics, establish retarded
analyticity outside the real interval, select a material spectral density, or
prove a fluctuation-dissipation relation. Those require independent source
authority and cannot be manufactured by mesh refinement.

Run:

```powershell
python research/aspect/checkers/dyadic_passive_bath_refinement.py
```
