# Independent tensor sewing selects a logarithmic residual action conditionally

## Question and frozen additional requirement

The [mixed residual construction](comparison-mixed-residual-quartic.md) produces
all even degrees but does not select their relative inclusion in an action.
Test whether an additive scalar readout of independent product preparations fixes
that summation. Additivity is an explicit new requirement, not a theorem that the
Carrier physically imposes it. The counting pairing and multiplicative probe
remain the preceding experiment's declared representation.

SCC obligations: source product realization and scalar sewing. This is independent
tensor sewing, not sequential composition of two comparisons on one carrier.

## Source-derived sewing law

For the existing source swap P and a nonzero real/rational probe phi, define

\[
N(\phi)=\langle\phi,\phi\rangle,\qquad
c(\phi)=\frac{\langle\phi,P\phi\rangle}{N(\phi)},\qquad
e(\phi)=\frac{S_P(\phi)}{N(\phi)}=\frac{1-c(\phi)}2.
\]

The denominator is the matrix element of the identity comparison. Normalization
makes c=1 for identity and removes overall probe scaling. These are functions on
probe rays, not an identified spacetime scalar field. Reading only the source's
fixed selected point gives c=1 and zero action; a non-fixed probe is needed to
observe a nontrivial comparison.

The actual independent product operations give

\[
N(\phi\otimes\psi)=N(\phi)N(\psi),\qquad
c_{P\otimes P}(\phi\otimes\psi)=c_P(\phi)c_P(\psi).
\]

These factorization identities are checked over a generic commutative ring before
any divisions. The normalized residual therefore composes as

\[
e\star f=e+f-2ef.
\]

This is the multiplicative formal-group law in the coordinate c=1-2e. Agda proves
its associativity, unit and multiplicative-coordinate identity. The mixed term is
exactly the preceding composition defect in normalized coordinates.

## Unique normalized formal additive readout

Require a characteristic-zero formal series A with

\[
A(e\star f)=A(e)+A(f),\qquad A(0)=0,\qquad A'(0)=1.
\]

The last condition matches the normalized quadratic action to leading order and
fixes an otherwise free overall scale. Formal differentiation in f at zero gives

\[
(1-2e)A'(e)=1.
\]

For `A(e)=sum a_n e^n`, this forces

\[
a_1=1,\qquad (n+1)a_{n+1}=2n a_n,
\qquad a_n=\frac{2^{n-1}}n.
\]

Thus

\[
A(e)=-\tfrac12\log(1-2e)
=e+e^2+\tfrac43e^3+2e^4+\cdots.
\]

Uniqueness is a written all-order formal-series argument. Exact symbolic checks
solve for the first ten coefficients from the differential equation, rather than
loading a logarithm coefficient table, and verify the original two-variable sewing
identity through total degree seven. The logarithmic candidate satisfies the full
identity in formal series, since c(e star f)=c(e)c(f) and both have constant one.

The previous n-slot mixed energy obeys `E_n/N^n=2^(n-1)e^n`. Hence the additive
readout weights that normalized level by **1/n**, not by one. The former ordinary
geometric series `e/(1-2e)` fails this sewing test. This is a conditional selection
of relative tower coefficients, not a prediction of a physical coupling.

## Exact quartic truncation fails, but admits a controlled local approximation

Retaining only `A_2(e)=e+e^2` gives the exact defect

\[
A_2(e\star f)-A_2(e)-A_2(f)=4ef(ef-e-f).
\]

The actual rational source probe `(0,2,1,0)` has N=5, c=4/5 and e=1/10. Pairing it
with itself produces e star e=9/50 and truncation defect **-19/2500**.

No nonconstant finite polynomial in e can satisfy exact sewing. If its degree is
m with leading coefficient a_m, the coefficient of `e^m f^m` on the composite side
is `(-2)^m a_m`; neither the separate side nor a lower power contributes. In
characteristic zero this contradicts a_m nonzero. This argument is not a claim
about all possible nonlinear field coordinates.

In the normalized contrast coordinate `x=(phi01-phi10)/sqrt(N)`,

\[
A(x)=-\tfrac12\log(1-x^2)
=\tfrac12x^2+\tfrac14x^4+\tfrac16x^6+\cdots.
\]

Its quadratic derivative at zero is one and fourth derivative is six. For
`|x|<1`, the error after the quartic obeys

\[
\frac{x^6}{6}\leq A(x)-\frac{x^2}{2}-\frac{x^4}{4}
\leq\frac{x^6}{6(1-x^2)}.
\]

This follows by bounding the positive series tail. It supports a small-contrast
approximation, not exact quartic truncation.

The number six is not the earlier physical coupling. If instead the even probe
component has fixed norm one and the odd component has amplitude u, then

\[
c=\frac{1-u^2}{1+u^2},\qquad
A=\tfrac12\log\frac{1+u^2}{1-u^2}=u^2+\tfrac13u^6+\cdots.
\]

The quartic coefficient in u is zero. The two formulas describe the same readout
under `x^2=2u^2/(1+u^2)`. Without a source-defined physical field and kinetic term,
a fourth derivative in one chosen chart is not an invariant scattering coupling.

## Domain and composition controls

For real probes, the orthogonal involution gives -1<=c<=1. The real logarithmic
branch above is finite for c>0, equivalently 0<=e<1/2. The source also permits:

- `(0,1,0,0)`: c=0, where the logarithm is singular;
- `(0,1,-1,0)`: c=-1, whose sign cannot be discarded.

There is no nontrivial finite additive real readout extending multiplicatively
through c=0: `L(0)=L(0)+L(c)` would force every L(c)=0. An extended infinite value
or an excluded zero locus is necessary. Away from zero, `-log|c|/2` and the sign
can be retained separately. That sign is a state-dependent overlap sign, not the
previous determinant character of P.

Nor is tensor sewing sequential-comparison additivity. On the rational probe
above, P followed by P is identity and has c=1, whereas two independent copies
have c=16/25. Thus no contradiction with the earlier obstruction to nonzero real
additive actions on a finite comparison group is implied.

## Disposition

The source product operations determine the normalized residual composition law.
The added tensor-additivity and leading-normalization requirements then determine
a logarithmic formal readout and its 1/n tower weights. They do not establish that
this is the physical action, select a physical field chart or kinetic term, supply
spacetime/quantum data, or predict the fixture's coupling 3/5. The source zero and
negative-overlap sectors prevent a silently global positive-log interpretation.

## Verification

`agda/ComparisonTensorSewing.agda` freshly passes safe/cubical compilation, including
26 local dependencies. It proves source norm/overlap product identities, their
energy relation, normalized ring sewing identities and the exact truncation defect.
Logarithm uniqueness and the all-degree polynomial obstruction are written
arguments; symbolic checks cover the indicated coefficients and finite source
controls, not a formal analytic-completion theorem.

```text
pwsh -NoProfile -File research/nima/checkers/check_comparison_tensor_sewing.ps1 -Fresh
uv run --with sympy python research/nima/checkers/check_comparison_tensor_sewing.py
uv run --with sympy python research/aspect/scc/scc.py check nima-comparison-tensor-sewing
```

Receipts: `results/agda-ComparisonTensorSewing.json` and
`results/comparison-tensor-sewing.json`. Current formal source hashes are verified.
New files/evidence remain uncommitted; no existing researcher source was edited.
No independent review, physical selection, commit or push is claimed.
Report event `ev-000000015613-9b4bb2a1-4ce9-447f-ae82-df66af9c95da` at sequence
15613 is admitted but uncommitted. No computation remains active; graph admission
is not truth certification.
