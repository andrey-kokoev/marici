# A saturated five-port Green adjoint cannot promote the unchanged Evans state

## Question

Can the unchanged Evans history enter the conservative kernel while the five
Green residual ports remain a faithful direct sum?

## Claim boundary

No. The ordinary history-tail residual is nonzero at every parameter, including
all Xi zeros. Therefore a saturated residual with that port retained as an
independent coordinate cannot vanish. Any proposed cancellation must pass
through an explicit source-authorized codiagonal with nontrivial kernel. This
is an architecture no-go, not a proof that no such codiagonal exists.

## Saturated residual

Let the five port residuals be

\[
 r^{(0)},\quad r^{(1)},\quad r^{({\rm wall})},\quad
 r^{({\rm recip})},\quad r^{({\rm link})},
\]

with each component in its own copy of the arithmetic target. The saturated
residual is

\[
 R_{\rm sat}(z)
 =\bigl(r^{(0)}(z),r^{(1)}(z),r^{({\rm wall})}(z),
 r^{({\rm recip})}(z),r^{({\rm link})}(z)\bigr).
\]

The ordinary-tail theorem gives

\[
 r^{(0)}(z)\ne0
\]

for every fixed \(z\): consecutive sufficiently late prime shells have strict
real sign. Hence

\[
 R_{\rm sat}(z)\ne0
\]

for every \(z\), including every zero of \(\tau\).

Thus the unchanged Evans vector is never a kernel state of a conservative
pencil whose lower equation is the faithful five-port direct sum.

## Joint-column adjoint codiagonal

Cancellation occurs only after a map

\[
 C:
 U^{(0)}\oplus U^{(1)}\oplus U^{({\rm wall})}
 \oplus U^{({\rm recip})}\oplus U^{({\rm link})}
 \longrightarrow U_{\rm ar}
\]

forms the arithmetic equation

\[
 r_U(z)=C R_{\rm sat}(z).
\]

For the declared joint incidence column, this map need not be invented: it is
the adjoint of the source diagonal that inserts one arithmetic coefficient
into all five typed ports, with the Green metric and reciprocal signs fixed.
Equivalently, \(B_\Sigma^\dagger\) is the source-weighted sum of the five port
adjoints.

This codiagonal is nonfaithful as an observation of the saturated target; its
kernel can contain nonzero port packets. It must not be identified with the
retained joint graph, but its existence is already part of the joint-column
adjoint once every port normalization is frozen.

The required chain condition is

\[
 C R_{\rm sat}(z)=\tau(z)h_U(z).
\]

At a Xi zero this places \(R_{\rm sat}(z)\) in \(\ker C\); it does not make the
individual ports vanish. The open theorem is this kernel identity, not the
abstract existence of a summation map.

## Positive-form consequence

If the conservative Green energy is the orthogonal positive sum of all five
port norms, then

\[
 \|R_{\rm sat}(z)\|^2
 \ge \|r^{(0)}(z)\|^2>0.
\]

No skew linking term or scalar determinant identity can turn that faithful
positive direct sum into a zero vector. Cancellation requires that the lower
equation use the source codiagonal before positivity is applied, or that the
history be modified by a separately divisor-preserving chain comparison.

This is why G3 coercivity may govern only the complement. Applying it to the
full saturated divisor-bearing residual erases the Xi kernel.

## Source-authority requirement

The adjoint codiagonal is fully defined only after the joint incidence specifies:

- the common target topology;
- all five coefficients and reciprocal signs;
- the wall and Wronskian comparison;
- prime and grade behavior;
- cutoff naturality;
- compatibility with the arithmetic source metric;
- the Green adjoint relation that makes \(C\) part of the operator rather than
  a fitted readout.

A scalar ratio chosen to make \(CR_{\rm sat}=0\) at known zeros is not the
source adjoint. Nor can equality of determinant sections alter or manufacture
its coefficients.

## Multiplicity

For a zero of order \(m\), divisor-preserving promotion requires

\[
 C R_{\rm sat}^{(j)}(z_0)=0,
 \qquad 0\le j<m.
\]

Even a source-derived codiagonal that cancels the zeroth residual may fail on
higher jets. Local-module length therefore remains a separate test.

## SCC consequence

The corrected model should distinguish:

1. `saturated_five_port_residual`, constructed and nowhere zero because of its
   ordinary component;
2. `joint_column_adjoint_codiagonal`, constructed only to the extent that all
   five source normalizations and the common Green metric are frozen;
3. `codiagonal_residual_divisible_by_xi`, open;
4. `conservative_parameter_root_chain`, dependent on every residual jet.

Without node 2, the phrase `prime_shell_adjoint_residual_family` hides the
nonfaithful operation on which cancellation depends. If any port normalization
is still open, node 2 must remain partial rather than being fitted from node 3.

## Disposition

The saturated retained architecture rejects unchanged-Evans promotion as a
five-coordinate kernel statement. On the declared joint-column architecture,
the source adjoint supplies the nonfaithful codiagonal; the unproved step is
that its fixed five-port sum satisfies exact Xi divisibility. The alternative
is a new multiplicity-preserving history comparison. Neither divisibility nor
such a comparison is currently constructed. No RH conclusion is authorized.
