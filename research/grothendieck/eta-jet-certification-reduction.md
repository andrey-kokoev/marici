# Regular eta jets replace Laurent data

The outstanding input to the first quarter-point localizer certificate is a
rigorous enclosure of four Stieltjes constants. They need not be imported as
opaque Laurent data. Put

\[
 \eta(s)=(1-2^{1-s})\zeta(s),\qquad L=\log 2,
\]

and write `eta(1+e)=sum(c_j e^j)`. Multiplication by the zero `1-2^{-e}`
cancels the zeta pole before numerics. Coefficient comparison gives

\[
\begin{aligned}
c_0={}&L,\\
c_1={}&L\gamma_0-L^2/2,\\
c_2={}&-L\gamma_1-L^2\gamma_0/2+L^3/6,\\
c_3={}&L\gamma_2/2+L^2\gamma_1/2+L^3\gamma_0/6-L^4/24,\\
c_4={}&-L\gamma_3/6-L^2\gamma_2/4-L^3\gamma_1/6
       -L^4\gamma_0/24+L^5/120.
\end{aligned}
\]

Here `c_j=eta^(j)(1)/j!`. Since `L>0`, this triangular system reconstructs
the four constants successively with interval arithmetic. Thus the remaining
analytic input reduces to certified enclosures of the regular jet

\[
 \log2,\eta(1),\eta'(1),\ldots,\eta^{(4)}(1).
\]

Formally,

\[
 \eta^{(j)}(1)=(-1)^j\sum_{n\ge1}
 \frac{(-1)^{n-1}(\log n)^j}{n}.
\]

For `j>0` the summand is not initially decreasing. A rigorous evaluator must
split the finite prefix through `n>e^j`, then enclose or accelerate the
monotone tail with directed rounding. Ordinary floating-point summation does
not close that obligation. Direct truncation is also impractical: at order
four the elementary remainder needs a cutoff near `3.31e18` for `10^-12`.
A remainder-proved acceleration is mandatory. See
`eta-naive-tail-certification-no-go.md`.

Certified eta jets, the triangular map, the exact `l_j` formulas, and the
existing radius-`10^-12` rational boxes would certify both first localizer
signs without zero locations. This remains one finite corner, not RH.

## Durable verification

- Checker: `checkers/eta_jet_stieltjes_reconstruction.py`
- Result: `results/eta-jet-stieltjes-reconstruction.json`
