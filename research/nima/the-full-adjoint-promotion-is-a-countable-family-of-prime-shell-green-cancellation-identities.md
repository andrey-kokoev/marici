# The full adjoint promotion is a countable family of prime-shell Green cancellation identities

## Nested centered columns

Order the primes as

\[
p_1<p_2<\cdots
\]

and write \(L_n=\log p_n\). The centered primitive columns are nested theta
cuts. Their difference

\[
s_n
=
p_{n+1}^{1/2}b_{p_{n+1}}
-p_n^{1/2}b_{p_n}
\]

is the source theta shell on

\[
(L_n,L_{n+1}],
\]

together with its two endpoint wall coordinates and the corresponding
regular derivative ports.

## Adjoint-zero implication

If

\[
B_\Sigma^\dagger u=0,
\]

then \(u\) is orthogonal to every incidence column. Therefore

\[
\langle s_n,u\rangle_{G}=0
\]

for every \(n\), where \(\langle\cdot,\cdot\rangle_G\) is the declared
wall-extended Green pairing.

Thus arithmetic adjoint cancellation is equivalent to a countable family of
local shell identities, plus the limiting common-mode condition.

## Port decomposition

Decompose each shell pairing into retained orthogonal ports:

\[
\langle s_n,u\rangle_G
=
I_n^{(0)}(u)
+I_n^{(1)}(u)
+I_n^{({\rm wall})}(u)
+I_n^{({\rm recip})}(u)
+I_n^{({\rm link})}(u).
\]

These terms denote, respectively:

- ordinary theta-tail overlap;
- regular derivative overlap;
- endpoint jump response;
- reciprocal history contribution;
- ordered Stokes/Wronskian polarization, when present.

The full residual vanishes precisely when

\[
I_n^{(1)}+I_n^{({\rm wall})}
+I_n^{({\rm recip})}+I_n^{({\rm link})}
=
-I_n^{(0)}
\]

for every prime shell.

## Evans-tail sign

For the right Evans state at any fixed parameter \(z\), the ordinary term has
strictly negative real part on every sufficiently late shell:

\[
\operatorname{Re}I_n^{(0)}(u_z)<0.
\]

Therefore the remaining Green ports must provide a nonzero compensating real
part shell by shell. Global endpoint matching

\[
\tau(z)=0
\]

supplies only one scalar identity and does not imply this infinite family.

## Why norm closure does not provide cancellation

The scale-independent wall-extended norm of each cut atom proves boundedness
of the incidence. It does not specify the signs or phases of the cross pairing
with \(u_z\). Norm identities cannot be substituted for the shell equalities.

Likewise, trace-class convergence of \(B_\Sigma^\dagger GB_\Sigma\) proves
existence of the relative determinant but does not force
\(B_\Sigma^\dagger u_z=0\).

## Smallest finite falsifier

At cutoff \(X\), compute the last two primitive columns and evaluate

\[
\mathcal S_{p,q}(z)
=
\left\langle
q^{1/2}b_q-p^{1/2}b_p,
 u_z
\right\rangle_G
\]

for consecutive primes \(p<q\le X\). One nonzero shell residual at a tested Xi
zero falsifies promotion of the unchanged Evans state at that cutoff.

A valid theorem must derive \(\mathcal S_{p,q}(z)=0\) from source Green/Stokes
identities uniformly through completion; it may not fit wall coefficients
after inspecting the zero.

## Disposition

The remaining arithmetic adjoint theorem is no longer an opaque vector
condition. It is an infinite, cutoff-natural family of prime-shell Green
cancellation identities whose ordinary component has eventual strict sign.
No current source identity cancels that component shell by shell. No RH
conclusion is authorized.
