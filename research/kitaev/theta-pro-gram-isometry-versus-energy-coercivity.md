# Pro-Gram completion makes observation isometric but does not supply coercive energy

Owner: `marici.Kitaev`

## Bounded question

Does passing from raw labelled coefficients to the constructor-generated
pro-Gram topology repair the adjacent-label completion collapse in a way that
has independent RH force?

## Observation completion theorem

Let (E\) be the finite labelled source packets and let a finite authorized
constructor family (F\) define

\[
\mathcal O_Fc=(G Cc)_{C\in F},
\qquad
q_F(c)^2=\sum_{C\in F}\|GCc\|^2.
\]

After quotienting by \(\ker\mathcal O_F\), the (q_F\)-completion is canonically
isometric to

\[
\overline{\operatorname{Ran}\mathcal O_F}
\subseteq\bigoplus_{C\in F}Y_C.
\]

Thus \(\mathcal O_F\) has lower bound one in the topology it defines. This is
an exact universal property, not an independently derived coercivity theorem.
It says the selected observations survive their own completion.

An RH-bearing energy (B_F\) still requires a source theorem such as

\[
c\,q_F(x)^2\le B_F(x)\le C\,q_F(x)^2
\]

with positive cutoff-independent constants and with (B_F\) identified with
the completed Green/Poisson energy before scalarization.

## Fixed finite continuous-family no-go

Suppose every feature atom

\[
q\longmapsto y_C(q)=GC e_q
\]

is norm-continuous in the logarithmic label (q\). For any labels
(q_m,r_m\) with \(|q_m-r_m|\to0\), the raw-normalized packets

\[
x_m=2^{-1/2}(e_{q_m}-e_{r_m})
\]

satisfy

\[
q_F(x_m)^2
=\frac12\sum_{C\in F}\|y_C(q_m)-y_C(r_m)\|^2\to0.
\]

Therefore no fixed finite family of norm-continuous analytic constructors is
uniformly observable relative to raw labelled \(\ell^2\). Adding finitely many
derivatives, endpoints, or smooth currents cannot change this conclusion.

## What could evade the no-go

There are only three typed escape routes:

1. **Change the source topology.** Use the pro-Gram topology and cease claiming
   a lower bound relative to raw \(\ell^2\).
2. **Add a discrete source port.** A valuation-cylinder or exact label port can
   separate nearby analytic labels, but must be independently authorized and
   retained through completion.
3. **Restrict admissible states.** Source dynamics may exclude adjacent
   differences. This requires an observability theorem for the admissible
   invariant subspace.

An unbounded derivative divided by label spacing is not automatically a fourth
route; its domain, closability, and source authority must be established.

## Infinite constructor family

A complete family of finite valuation cylinders can separate every finite
arithmetic packet by unique factorization. But no fixed finite subfamily
identifies arbitrarily many new prime labels. The resulting topology is truly
pro-generated: joint faithfulness does not imply that one finite observation
energy controls the completion.

Consequently the statement

\[
q_C(c)=0\text{ for every authorized }C\Longrightarrow c=0
\]

is weaker than existence of one finite (F\) and one coercive completed Green
energy. This is the same distinction as an infinite jet atlas versus a finite
executable detector.

## Hostile fixtures

- Gaussian translates and any fixed finite derivative tower have feature
  differences tending to zero with the label spacing.
- Defining the source norm to equal (q_F\) makes the lower bound exactly one
  but proves no independent energy inequality.
- A discontinuous alternating label bit restores separation in a toy model
  but fails analytic Gram descent and therefore requires a typed discrete port.
- A cutoff-dependent constructor family can separate every finite cutoff while
  supplying no fixed completion topology or uniform energy certificate.

## Disposition

The constructor pro-Gram completion legitimately preserves its declared
observation coordinates. It does not by itself prove completion-stable
observability of the theta source or off-seam nonvanishing. The remaining
source theorem must choose between a discrete arithmetic port and a dynamical
restriction, then derive a finite coercive Green/Poisson energy on that typed
state space.

## Claim strength

Abstract completion theorem and fixed-finite-continuous-family no-go. No claim
is made that every authorized theta constructor is norm-continuous or that a
discrete port is physically operative.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_pro_gram_coercivity_gap.py`.
The result is written to
`research/kitaev/results/theta-pro-gram-coercivity-gap.json`.
