# Compatible probes are the dual of the stable logical sector

## Question

For a directed system of logical vector spaces

\[
H_0\longrightarrow H_1\longrightarrow\cdots,
\qquad
H_\infty=\operatorname*{colim}_n H_n,
\]

what is the complete algebraic space of scalar probes compatible with every authorized constructor enlargement, and how many probes are minimally required for faithful readout?

## Claim boundary

Fix a coefficient field \(k\). A compatible scalar probe is a family

\[
p_n:H_n\longrightarrow k
\]

satisfying \(p_m f_{n,m}=p_n\). By the universal property of the colimit,

\[
\operatorname{Hom}_k(H_\infty,k)
\cong
\operatorname*{lim}_n\operatorname{Hom}_k(H_n,k).
\]

Therefore compatible scalar-probe cocones are exactly the dual space \(H_\infty^*\). The inverse-limit bonding maps are pullbacks

\[
f_{n,m}^*:H_m^*\longrightarrow H_n^*.
\]

A stage functional that has no compatible continuation is not a probe of the stable logical sector.

Let \(A\subseteq H_\infty^*\) be the subspace spanned by source-authorized probes. Their joint evaluation map is

\[
\operatorname{ev}_A:H_\infty\longrightarrow A^*,
\qquad
x\longmapsto(\alpha\mapsto\alpha(x)).
\]

Its kernel is the annihilator

\[
A^\perp=\{x\in H_\infty:\alpha(x)=0\text{ for every }\alpha\in A\}.
\]

Thus authorized probes are jointly faithful exactly when \(A^\perp=0\). If \(H_\infty\) is finite-dimensional, this is equivalent to

\[
A=H_\infty^*.
\]

If \(\dim H_\infty=d\), any family of scalar \(k\)-valued probes defining an injective map \(H_\infty\to k^r\) obeys \(r\ge d\). Equality is attainable algebraically by a dual basis. It is attainable physically only if a source-authorized dual basis exists.

This theorem concerns linear scalar probes over a field. It does not price implementation, prove physical accessibility, or determine minimal ports for noncommutative coefficient objects.

### Toric-code specialization

For a torus,

\[
H_\infty=H_1(T^2;\mathbf F_2)\simeq\mathbf F_2^2.
\]

Cellular subdivision preserves this space. The stable scalar-probe space is

\[
H_\infty^*=H^1(T^2;\mathbf F_2)\simeq\mathbf F_2^2.
\]

The primal-dual intersection pairing

\[
H_1(T^2;\mathbf F_2)\times H_1(T^{2,*};\mathbf F_2)
\longrightarrow\mathbf F_2
\]

is perfect. A pair of independent noncontractible dual loops therefore supplies a dual basis and separates all four logical classes. One scalar bit cannot be faithful because its kernel has dimension at least one.

Local syndrome probes vanish on the logical quotient: they detect endpoints of open strings but factor out closed cycles modulo boundaries. Their authorized span inside \(H_\infty^*\) is zero. Adding the two loop probes enlarges the authorized probe span from zero to the full dual.

The anticommutation statement is the operator-valued lift of the same pairing. For primal \(Z\)-loop \(Z_\gamma\) and dual \(X\)-loop \(X_{\gamma^*}\),

\[
Z_\gamma X_{\gamma^*}
=
(-1)^{\langle\gamma,\gamma^*\rangle}
X_{\gamma^*}Z_\gamma.
\]

Odd intersection gives anticommutation. The scalar logical label and the ordered Pauli algebra share the Carrier intersection geometry but use different coefficient lenses.

## Disposition

The minimum faithful scalar readout is controlled by the dimension of the stable logical sector, not by the largest finite-stage dimension and not by the number of syndrome coordinates.

The first falsifier is one of:

1. the proposed stage probes violate pullback compatibility;
2. the alleged stable space is not the colimit of the declared transition system;
3. the authorized probe span has a nonzero annihilator;
4. fewer than \(d\) scalar probes are claimed to inject a \(d\)-dimensional stable vector space;
5. a dual-basis argument is used to claim physical availability without source authority;
6. scalar duality is used to infer the noncommutative logical operator algebra without the intersection/commutation lift.

For Benincasa's directed depth system, the immediate finite target is the inverse system of dual transition maps. Its eventual authorized probe span can be computed without first choosing coordinates on every colimit class. A persistent primal class and a compatible dual probe must be reported together; either side alone does not establish a readable stable sector.
