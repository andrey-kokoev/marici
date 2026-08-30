# Five-site mod-two Frobenius collapse

## Hostile test

Let

\[
A=\mathbf F_2[(C_2)^5]
\cong
\mathbf F_2[\epsilon_1,\ldots,\epsilon_5]/(\epsilon_i^2).
\]

The absolute Frobenius endomorphism is \(F(x)=x^2\). Every positive-degree
monomial contains at least one \(\epsilon_i\), so its square vanishes. Cross
terms cancel in characteristic two. Hence

\[
\boxed{F:A\longrightarrow A
\text{ is augmentation followed by inclusion of constants}.}
\]

Its image has dimension one and its kernel is the full 31-dimensional
augmentation ideal. In particular, every nonempty branch norm satisfies

\[
F(N_B)=N_B^2=0.
\]

The reduced quotient is merely \(A_{\mathrm{red}}=\mathbf F_2\), on which
Frobenius is the identity.

## Arithmetic verdict

The bad-prime locus \(V(2)\) records a real integral normalization defect,
and its special fiber retains a rich nilpotent branch-incidence filtration.
But absolute Frobenius collapses that entire filtration. The conditional deck
algebra therefore supplies no nontrivial Frobenius spectrum, closed-point
count, local Euler factor, or route to an \(L\)-function.

This is a hostile obstruction to promoting the bad-prime shadow into
Frobenius arithmetic. It does not rule out a separately sourced geometric
space or cohomology theory with a nontrivial Frobenius action. Such an object
would be new typed input and must be derived independently.

## Scope

Absolute algebra Frobenius is not being identified with geometric Frobenius.
No physical relative-chain specialization or Carrier-derived arithmetic is
asserted.

## Verification

`checkers/five_site_mod2_frobenius_collapse.py` checks all 32 basis squares,
all 496 unordered cross-term cancellations, and all 31 branch norms.
