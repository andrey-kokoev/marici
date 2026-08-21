# Finite p-group norm homology is the augmentation ideal modulo the norm line

Epistemic-graph event: 1367.

## Theorem

Let `K` be a nontrivial finite `p`-group, let `A=F_p[K]`, and write
`epsilon:A -> F_p` for augmentation, `I=ker(epsilon)`, and

`nu_K=sum_(g in K) g`.

For every `x in A`, left and right multiplication merely permute the terms of
the norm, hence

`x nu_K=epsilon(x)nu_K=nu_K x`.

Consequently multiplication `m_nu` by `nu_K` has

`ker(m_nu)=I`,  `im(m_nu)=F_p nu_K`.

Because `epsilon(nu_K)=|K|=0` in `F_p`, the norm line lies in `I`; equivalently
`nu_K^2=|K|nu_K=0`.  Its square-zero homology therefore is

`H(A,m_nu)=I/(F_p nu_K)`,

of dimension `|K|-2`.  The norm line is the invariant line, hence the socle
of the regular module: a vector fixed by every group element has constant
coefficients, and the augmentation ideal is the Jacobson radical of the
group algebra of a finite `p`-group.

For `m` independent regular fibers, the homology is the direct sum of `m`
copies and has dimension `m(|K|-2)`.

## Hostile controls

- `K=C2` in characteristic two is the unique nontrivial acyclic case.
- Every group of order eight, including nonabelian `D8` and `Q8`, leaves six
  residual dimensions per regular fiber.
- The dimension is group-independent, while the radical/Loewy filtration can
  distinguish groups of the same order.  The elementary-abelian Hilbert
  series of Ledger 1344 is therefore a refinement, not a universal grading.

## Scope

This is a theorem about the regular modular group algebra and its norm
correspondence.  It does not construct the unavailable physical
relative-chain pushforward, prove that a physical branch quotient realizes a
regular fiber, or identify these algebraic classes with physical readouts.
