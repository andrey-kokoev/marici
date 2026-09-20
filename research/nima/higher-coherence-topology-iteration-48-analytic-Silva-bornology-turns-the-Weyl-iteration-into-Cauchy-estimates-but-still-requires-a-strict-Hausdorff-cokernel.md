# Higher-coherence topology iteration 48: analytic Silva bornology turns the Weyl iteration into Cauchy estimates, but still requires a strict Hausdorff cokernel

## Distinction from iteration 2

Iteration 2 used a strict LF limit in support/coherence degree and showed that a
fixed-prime residual cannot escape to infinity. Here the inductive parameter is
instead the radius of a complex spectral neighborhood. The purpose is to
control all normal derivatives in the Weyl argument of iteration 47.

## Candidate topology

Let `B_(rho,delta)` be a Banach space of labelled holomorphic packets on
`|u|<rho`, with exponential Köthe weight `delta`. Form a regular Silva/DFS-type
inductive system by shrinking the radius and relaxing the weight:

\[
\mathcal A
=
\underset{\rho\downarrow0,\,\delta' <\delta}{\operatorname{ind\,lim}}
B_{\rho,\delta}.
\]

Compact restriction maps make bounded sets localize in one controlled analytic
step. This is the bornology of analytic germs with labelled decay.

## Cauchy control of the Weyl iteration

If `q` is bounded on `|u|<rho`, Cauchy's estimate on a smaller disk
`|u|<r<rho` gives

\[
\|D^nq\|_r
\le
\frac{n!}{(\rho-r)^n}\|q\|_\rho,
\]

up to the controlled Köthe loss from the label multiplier `L_lambda`.
Multiplication by `u^n` contributes `r^n`. Hence, for `Uq=0`,

\[
\|q\|_r
\le
\left(\frac{r}{\rho-r}\right)^n\|q\|_\rho.
\]

Choosing `r<rho/2` and letting `n` tend to infinity forces `q=0` on the smaller
germ. This supplies the all-order estimate that a single Hilbert norm could
not provide.

## Conditional torsion-free theorem

Consequently, a Hausdorff analytic-germ module carrying a continuous regular
connection and satisfying the Weyl relation has no `u`-torsion, provided its
bounded disks admit the Cauchy estimates above. Applied to the codiagonal
cokernel, this would kill `[H_border]` and produce the labelled lift.

## The strictness bottleneck

The quotient

\[
Q=H/C(K)
\]

has this analytic Silva structure only if `C(K)` is closed and bornologically
strict in `H`, and the induced connection preserves the quotient bounded disks.
If the image is dense but nonclosed, the Hausdorff quotient may erase the very
class being tested; the non-Hausdorff quotient may contain infinitesimal
classes to which Cauchy norm estimates do not apply.

The established Köthe recovery proves closedness of the labelled incidence
before common-history codiagonalization. It does not prove strictness of the
codiagonal image `C(K)`.

## Finite-cutoff limitation

Every finite cutoff has a finite-dimensional closed image and satisfies the
analytic estimate. The relevant requirement is uniformity of restriction and
recovery constants as the cutoff grows. Otherwise the limit quotient can lose
strictness even though all finite quotients are well behaved.

## Residual consequence

If strictness is proved, the chain is short:

\[
\tau[H_{\rm border}]=0
\Longrightarrow
[H_{\rm border}]=0
\Longrightarrow
H_{\rm border}=C(S)
\Longrightarrow
R=\tau S.
\]

This would be a genuine topological closure of the relative-Haar gate.

## Verdict for topology 48

Analytic Silva bornology successfully supplies the uniform all-derivative
control needed by the normal Weyl commutator. It reduces the remaining problem
to one sharp functional-analytic statement: the common-history codiagonal must
have strict closed image in the analytic labelled germ topology.

The next nonredundant topology to test is a quotient graph/closed-range topology
built from the codiagonal itself, checking whether a source-derived parametrix
or tame estimate can establish that strictness without defining the topology
circularly.