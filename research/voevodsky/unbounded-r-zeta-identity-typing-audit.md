# Typing audit of the unbounded radial comparison identity

## Question

Does the proposed identity

\[
Q_\zeta(f,g)=G_{G4}(R_\zeta f,R_\zeta g)
\]

supply the completion theorem missing from finite Green positivity?

## Claim boundary

This packet audits the logical shape of Grothendieck's target. It does not construct \(Q_\zeta\), \(G_{G4}\), or \(R_\zeta\), and therefore does not establish an RH-bearing positivity statement.

## Classification

The target is relevant and correctly stronger than finite Gram positivity. It is a source-typed morphism between closed form domains modulo radicals. It becomes an identification only after proving that the induced map on quotient form spaces is an isometry with dense range and that those quotient form spaces are complete. Dense range of an isometry into a complete target then gives surjectivity.

The phrase “identity” must refer to equality of closed forms under this induced unitary comparison, not equality of raw presentations.

## Independent gates

### Domain closure

Equality on a common algebraic core is insufficient. On \(\ell^2\), let

\[
R(x_n)=(nx_n)
\]

on finitely supported sequences and define \(Q(f)=\|Rf\|^2\). The displayed form equality holds on the dense core, but that core form is not closed: its closure has the larger weighted domain

\[
\left\{x:\sum n^2|x_n|^2<\infty\right\}.
\]

Thus the source and target closed domains must be identified, not inferred from core equality.

### New completed radical

Let finite positive forms assign weight \(1/N\) to one fixed direction and weight one to the others. Every finite stage is positive definite, while the limiting form has that direction in its radical. Positivity at every stage does not preserve the quotient.

### Reduced-minimum-modulus collapse

Let \(R(x_n)=(x_n/n)\) on \(\ell^2\). It is injective and has dense range, but

\[
\inf_{\|x\|=1}\|Rx\|=0.
\]

Hence dense quotient range and injectivity do not supply coercivity or a bounded inverse on the range.

## Circularity gate

Grothendieck's proposed common source operator factorization

\[
B=CR_\zeta
\]

is the correct noncircular shape only if \(B\), \(C\), their domains, and \(R_\zeta\) are independently source-derived. Defining any one of them by forcing the desired equality transports the RH-bearing assertion into an assumption.

## Relation to attachment variance

This target strengthens the analytic completion of the Green under-attachment. It does not create a projection from the enlarged Green object, so it does not turn that construction into an over-extension. Nor does it supply unrestricted pushouts or displayed univalence.

## Disposition

The proposed target survives the audit as a well-typed research programme, not a theorem. Its first missing typed object is an independently derived common core and intertwiner satisfying \(CR_\zeta=B\). Closure, radical stability, and quotient coercivity are separate acceptance tests and cannot be merged into finite positivity.

## Verification

- `research/grothendieck/unbounded-positivity-as-r-zeta-identity-target.md`
- `research/voevodsky/checkers/check_unbounded_r_zeta_identity_gates.py`
- `research/voevodsky/results/unbounded_r_zeta_identity_gates.json`
