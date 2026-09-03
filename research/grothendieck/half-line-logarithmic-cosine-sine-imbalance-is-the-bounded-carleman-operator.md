# The half-line logarithmic cosine--sine imbalance is the bounded Carleman operator

## Exact identity

Let `C` and `S` be the unitary cosine and sine transforms on `L^2(0,infinity)`:

`C phi(xi)=sqrt(2/pi) integral_0^infinity cos(xi x)phi(x)dx`,

`S phi(xi)=sqrt(2/pi) integral_0^infinity sin(xi x)phi(x)dx`.

For smooth compactly supported `phi`, polarization and

`cos(xi x)cos(xi y)-sin(xi x)sin(xi y)=cos(xi(x+y))`

give

`integral_0^infinity log(xi)(|C phi|^2-|S phi|^2)dxi`

`=(2/pi) double_integral phi(x)conj(phi(y))`

` * [integral_0^infinity log(xi)cos(xi(x+y))dxi] dxdy`.

The distributional cosine transform is

`integral_0^infinity log(xi)cos(a xi)dxi=-pi/(2a)`

for `a>0`. Therefore

`integral log(xi)(|C phi|^2-|S phi|^2)dxi`

`=-double_integral phi(x)conj(phi(y))/(x+y) dxdy`.

The right side is minus the Carleman quadratic form.

## Boundedness

The Carleman operator

`H phi(x)=integral_0^infinity phi(y)/(x+y)dy`

is bounded self-adjoint on `L^2(0,infinity)` with norm `pi`. Hence

`|integral log(xi)(|C phi|^2-|S phi|^2)dxi|`

`<=pi ||phi||_2^2`.

This proves the uniform order-zero bound for the principal logarithmic boundary remainder. Endpoint dilation and arbitrary profile variation cannot make it diverge.

## From the half-line model to the interval

The exact digamma multiplier differs from `log|u|` by a bounded function after a harmless low-frequency regularization. Replacing `log xi` by `log(1+xi)` changes only a low-frequency integrable multiplier plus a bounded high-frequency correction. On a finite interval these contribute bounded operators.

Each interval endpoint has the same half-line Carleman boundary symbol. Standard localization with a partition of unity leaves bounded interior commutators. Consequently

`Gamma_L-log(1+sqrt(-Delta_D))`

is an order-zero bounded remainder. A publication proof must track the two endpoint charts, low-frequency regularization, and Fourier constants, but the potentially unbounded boundary symbol is now explicitly controlled.

## Consequence

Voevodsky's interval logarithmic Gårding criterion is satisfied qualitatively:

`Gamma_L >= log(1+sqrt(-Delta_D))-C_L I`

for some finite source-independent analytic constant `C_L`. Combining this with the explicit fixed-support prime norm yields a computable high-mode positive reserve.

The remaining positivity gate is finite--tail coupling and certified enclosure of the finitely many low eigenvalues. The boundary remainder is no longer the first obstruction.

## Disposition

The half-line remainder is identified exactly with a classical bounded operator. The next task is numerical constants for interval localization and the exact digamma-minus-log correction.
