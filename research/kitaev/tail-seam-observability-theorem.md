# Tail-plus-seam observability theorem

## Abstract finite theorem

Let a finite-dimensional state evolve by

\[
\partial_q\Psi=A\Psi,
\qquad y=J\Psi.
\]

For \(L>0\), define

\[
W(L)=\int_0^L e^{A^*q}J^*Je^{Aq}\,dq.
\]

Since \(\Psi(q)=e^{Aq}\Psi(0)\), direct substitution gives

\[
\int_0^L\|y(q)\|^2dq
=\langle\Psi(0),W(L)\Psi(0)\rangle.
\]

The following are equivalent:

1. \(W(L)>0\);
2. no nonzero initial state has zero output throughout \([0,L]\);
3. the observability matrix

   \[
   \mathcal O(A,J)=
   \begin{pmatrix}J\\JA\\\vdots\\JA^{n-1}\end{pmatrix}
   \]

   has rank \(n\);
4. over an algebraically closed coefficient field, the PBH condition has no
   witness \(Av=\lambda v\), \(Jv=0\), \(v\ne0\).

The equivalence follows because a zero Gram integral forces the analytic
function \(Je^{Aq}v\) to vanish identically; its first \(n\) derivatives give
the Krylov rows. Cayley--Hamilton supplies all higher derivatives. PBH is the
dual invariant-subspace formulation.

## Minimal seam repair theorem

Let

\[
\mathcal N_C=\ker\mathcal O(A,J_C)
\]

be the Clark-unobservable subspace. An augmentation \(J_S\) repairs the pair
exactly when

\[
\mathcal N_C\cap\ker\mathcal O(A,J_S)=0.
\]

Therefore at least \(\dim\mathcal N_C\) independent scalar Krylov functionals
are required on \(\mathcal N_C\). For a one-dimensional invariant hidden
line, one row nonzero on that line is necessary and sufficient.

This is a dynamical refinement of kernel-reference completion: the extra row
need not be pointwise injective on the entire state space, only jointly
injective after propagation by \(A\).

## Exact two-state witness

Take

\[
A=0,
\qquad J_C=(1\;0),
\qquad J_S=(0\;1).
\]

Then \(v=(0,1)^T\) is the minimal PBH witness:

\[
Av=0,
\qquad J_Cv=0,
\qquad J_Sv=1.
\]

At \(L=1\),

\[
W_C=\operatorname{diag}(1,0),
\qquad W_{C+S}=I.
\]

Thus one independent seam row is the minimal repair.

## Sheet action

Let

\[
R=\operatorname{diag}(1,-1).
\]

It commutes with \(A\), leaves the Clark output even, makes the seam output
odd, and preserves the hidden line as a subspace. A symmetry-related Clark
copy satisfies \(J_CR=J_C\) and adds no observability rank. This gives the
general warning: sheet multiplicity does not repair an invisible state when
the added outputs lie in the original Krylov row space.

## Completion-collapse hostile family

For cutoff \(N\), set

\[
A_N=0,
\qquad J_{C,N}=\operatorname{diag}(1,N^{-1}),
\qquad J_{S,N}=(0\;1).
\]

Every finite Clark pair is observable, with

\[
W_{C,N}=\operatorname{diag}(1,N^{-2})>0.
\]

Nevertheless

\[
\lambda_{\min}(W_{C,N})=N^{-2}\to0.
\]

For the normalized escape sequence \(v_N=(0,1)^T\),

\[
\|J_{C,N}v_N\|=N^{-1}\to0,
\qquad
\|J_{S,N}v_N\|=1.
\]

The augmented Gramian is

\[
W_{C+S,N}=\operatorname{diag}(1,1+N^{-2}),
\]

so its lower bound is uniformly one. This proves exactly that finite
observability at every cutoff is weaker than completion-stable observability.

## Primitive and square-current rows

An additional current is independent precisely when its Krylov rows increase
the rank of \(\mathcal O(A,J_C)\). A row proportional to an existing Clark row
does nothing, regardless of its physical name. A row nonzero on the hidden
invariant subspace repairs it.

The checker demonstrates both possibilities with rational candidate rows.
It does not identify them with the actual theta primitive or square currents.
Those rows must be derived from their source channels before their rank can be
audited.

## Finite versus completion-stable observability

For each cutoff, finite observability is

\[
W_X(L)>0.
\]

Completion-stable observability over a compact spectral set \(K\) requires a
single constant \(c_K>0\) such that

\[
\lambda_{\min}W_X(L;s)\ge c_K
\]

for every admitted cutoff and \(s\in K\). Pointwise positivity of every
finite Gramian supplies no such constant.

## Source-authority boundary

The theorem determines how to test rows once supplied. It does not derive the
theta/Tate objects

\[
A_X, J_X^{\rm Clark}, J_X^{\rm seam},
J_X^{k=1}, J_X^{k=2},
\]

their domains, cutoff embeddings, or completed topology. Grothendieck must
derive those data from the doubled-tail operator and currents. A fitted seam
row chosen because it kills the computed nullspace has no source authority.

The RH-bearing question is consequently exact:

\[
\boxed{
\text{Is }(A_X,J_X^{\rm full})\text{ uniformly observable on compact
off-seam spectral sets through completion?}}
\]

## Verification

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_tail_seam_observability.py
```

The checker uses exact rational matrices, emits the PBH rejection witness,
verifies the minimal seam repair and sheet action, and evaluates the hostile
family through cutoff eight while proving its symbolic \(N^{-2}\) collapse.
