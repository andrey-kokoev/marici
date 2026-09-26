# A formal flow and clock from rational composition

Active SCC obligations: forward realization, coherent truncation and attachment
transport. The Clifford product remains the explicitly chosen realization.
This leaf constructs a FORMAL completion from actual rational coefficient
arithmetic; it does not reuse a real exponential as evidence of convergence.

## Coefficients are constructed and unique

`agda/FormalRotorCoefficients.agda` recursively constructs positive factorial
denominators using `RationalComponentArithmetic.den-product`, then defines
coefficients c_n as their reciprocals. It proves in the constructed rational
ring, for every order,

\[
c_0=1,\qquad (n+1)c_{n+1}=c_n.
\]

It also proves uniqueness of any coefficient sequence satisfying those laws.
Fresh safe/cubical compilation passes, including the actual component, signed
and rational arithmetic imports. This establishes the coefficients as 1/n!
without supplying an analytic exponential. It does not select the Clifford
product from the native response data.

## Finite jets and their precise composition domain

For a formal indeterminate x, use matrices over the quotient Q[x]/(x^(N+1)):

\[
E_N(x)=\sum_{n=0}^N\frac{J^n x^n}{n!}.
\]

Projection from order N+1 to N preserves this matrix. Reversal and inversion
satisfy E_N(x)^T=E_N(-x) and E_N(x)E_N(-x)=1 in the jet quotient. Composition is

\[
E_N(x)E_N(y)=E_N(x+y)
\pmod{(x,y)^{N+1}}.
\]

The coefficient proof at every order is

\[
\frac{J^i}{i!}\frac{J^j}{j!}
=\binom{i+j}{i}\frac{J^{i+j}}{(i+j)!}.
\]

The completion is the inverse limit of these coherent jets, namely the formal
power-series matrix E(x). This is x-adic completion, not a real norm completion.

Two truncation distinctions are checked rather than hidden:

- Separate cutoffs x^(N+1)=y^(N+1)=0 do not justify comparing with E_N(x+y)
  unchanged. At N=1 the product contains -xy, which a total-degree-one cutoff
  discards but the separate-variable quotient retains.
- Differentiation lowers jet order. The correct finite ODE holds modulo x^N,
  not modulo x^(N+1). At N=1, E_1'=J while J*E_1=J-x. The discarded relation's
  derivative is not zero in the same quotient.

In the formal inverse limit, differentiation and the coefficient recurrence
therefore give E'=J*E exactly. The adjoint formal flow has generator [J,Q],
matching the previously derived quadratic Hamiltonian within its stated metric
and symplectic realization.

## The normalized formal clock follows from the rational group law

The audited Cayley law is F(t,u)=(t+u)/(1-tu). Differentiating its rational
identity selects the normalized formal logarithm

\[
\ell(t)=2\sum_{n\geq0}\frac{(-1)^n t^{2n+1}}{2n+1},
\qquad \ell'(t)=\frac{2}{1+t^2},\qquad \ell(0)=0.
\]

It obeys

\[
\ell(F(t,u))=\ell(t)+\ell(u),
\qquad \ell(-t)=-\ell(t),
\qquad E(\ell(t))=V(t).
\]

These are FORMAL identities over rational coefficients. For the first, formal
differentiation of the difference in t gives zero by the invariant-differential
identity proved in the prior leaf; its value at t=0 is zero. Characteristic zero
then fixes every coefficient. The last follows from the same linear formal ODE
and initial matrix value. The normalization ell'(0)=2 matches V'(0)=2J; another
clock scale would be an additional normalization choice.

Thus an additive local formal clock exists before supplying a real continuum.
No arctangent value, real period, winding or physical time follows merely from
writing these series.

## Keep the actual signed centers and comparisons

Use a separate chart W_g(x)=E(x)g for EACH existing signed Clifford unit g,
retaining its complete word history independently. Let o(g)=+1 for even units
and -1 for odd units. Then

\[
W_g(x)W_h(y)=W_{gh}(x+o(g)y).
\]

The finite matrix product gh is the original signed product, not a newly chosen
multiplicative section of the coarse action group. All eight centers, signs and
reversers remain present. The checker verifies all 64 center pairs coefficient
by coefficient through order twelve.

The local parameter is zero at each center; it does not assign a real elapsed
angle between different centers. In particular formal integration around 1
has not produced a finite-time path to J. Replacing all charts by their local
clock alone would erase the very signs this programme retains.

## Why formal completion is not real evaluation

A finite jet has x^(N+1)=0. Any scalar ring evaluation into the real numbers
must therefore send x to zero. Plugging a nonzero number into its polynomial
representative does not respect the quotient relation.

There is also no universal scalar evaluation of the ENTIRE formal-series ring
at a nonzero real number. For every positive integer n, both 1+n*x and 1-n*x
have rational formal square roots. Under a unital real-valued ring map, their
images must be nonnegative. Thus 1+n*a and 1-n*a are nonnegative for every n,
forcing a=0. This argument concerns a readout preserving the whole formal ring,
not the later evaluation of a selected convergent series or an analytic chart.

The particular E series may be given a real interpretation after proving its
norm convergence. That is a separate construction on a suitable selected
packet, not a universal real evaluation of the formal completion. It also does
not eliminate the native product/readout admission question.

## Verification and continuation

The exact checker covers orders zero through twelve, 455 ordinary composition
coefficients, 5824 signed-chart composition coefficients, inverse/reversion,
truncation, adjoint derivative, the formal Cayley clock law and E(ell(t))=V(t).
The general coefficient and formal-differential arguments above explain the
all-order identities; Agda formalizes the scalar coefficient recurrence and
uniqueness, not the entire formal power-series algebra.

```text
pwsh -NoProfile -File research/nima/checkers/check_formal_rotor_coefficients.ps1 -Fresh
uv run --with sympy python research/aspect/scc/scc.py check nima-retained-rational-flow-jets
```

Receipts: `results/agda-FormalRotorCoefficients.json` and
`results/retained-rational-flow-jets.json`.

A nonredundant local continuation is to prove convergence and comparison
preservation for the SELECTED rotor packet in a declared norm completion, with
explicit tail bounds. The owner-directed native Cayley-admission handoff remains
open independently. Neither formal solvability nor analytic convergence should
be promoted into source-admitted physical evolution.
