# Two finite hostiles separate scalar agreement from typed Adams sewing

## Hostile one: correct scalar shadow, radical leakage

Let the primitive and square Green energies both be represented on \(\mathbb C^2\) by

\[
C_1=C_2=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]

Their Green radicals are the second coordinate. Let the declared scalar observer see only the first coordinate.

For a desired scalar mixed coefficient \(a\), compare

\[
K_{\mathrm{good}}=
\begin{pmatrix}
a&0\\
0&0
\end{pmatrix}
\]

with

\[
K_{\mathrm{leak}}=
\begin{pmatrix}
a&0\\
0&\varepsilon
\end{pmatrix},
\qquad \varepsilon\ne0.
\]

Both produce the same scalar total under the declared observer:

\[
e_1^*K_{\mathrm{good}}e_1
=
e_1^*K_{\mathrm{leak}}e_1
=
a.
\]

But

\[
K_{\mathrm{leak}}e_2=\varepsilon e_2\ne0,
\]

so

\[
\ker C_2\nsubseteq\ker K_{\mathrm{leak}}.
\]

Likewise its adjoint acts nontrivially on the primitive radical. The form cannot descend to either gauge-reduced Green space. No pseudoinverse normalization repairs this: support compression merely erases the unauthorized action after it has already made the unreduced form ill-defined.

This is the smallest hostile requested by Kitaev.

## Hostile two: contraction with the wrong reciprocal character

After radical reduction, take one-dimensional defect spaces and

\[
C_1=C_2=1.
\]

For \(0<r\le1\), define

\[
K_\theta=re^{i\theta}.
\]

It is contractive:

\[
\lVert K_\theta\rVert=r\le1.
\]

Its mate is

\[
K_\theta^*=re^{-i\theta}.
\]

If the source reciprocal sewing assigns the seam character \(\chi\), then an oriented Adams edge must satisfy the typed covariance law

\[
R_1K_\theta R_2^{-1}
=
\chi\,K_\theta^*
\]

for the declared reciprocal maps \(R_1,R_2\). Replacing the edge by its adjoint changes \(\chi\) to \(\chi^{-1}\). The two orientations therefore have identical norm and scalar magnitude but different seam character whenever the source does not identify \(\chi\) with \(\chi^{-1}\).

In the scalar gauge \(R_1=R_2=1\), strict equality of edge and mate requires

\[
e^{2i\theta}=1.
\]

Thus \(\theta\notin\pi\mathbb Z\) is the minimal phase hostile: both orientations are contractions, but they are not the same typed seam arrow.

## The ordered audit

The finite Adams-cell checker must run in this order:

1. verify both radical inclusions;
2. descend the mixed form to quotient supports;
3. compute the normalized contraction norm;
4. compute the reciprocal covariance character;
5. compare that character with the source orientation;
6. only then evaluate the scalar Euler/Mellin shadow.

The scalar check belongs last because it cannot detect either hostile.

## Consequence for the relative three-port cell

For the two-chart packet indexed by

\[
(F_{\mathrm{in}},F_{\mathrm{out}},W_{\mathrm{const}}),
\]

the relative Green matrix \(G_{\mathscr C_p}\) must be tested before contraction with the scalar observer. If \(J_1,J_2\) are primitive and square incidence columns, the candidate mixed block is

\[
K_{\alpha,p}=J_1^*G_{\mathscr C_p}J_2.
\]

The radical hostile tests whether \(G_{\mathscr C_p}\) couples a gauge-null face or overlap direction. The orientation hostile tests whether exchanging inner and outer fronts sends \(K_{\alpha,p}\) to the source-authorized reciprocal mate with the correct character.

These are independent gates:

\[
\text{quotient descent}
\quad\not\Rightarrow\quad
\text{typed reciprocal orientation},
\]

and

\[
\text{contractivity}
\quad\not\Rightarrow\quad
\text{correct seam character}.
\]

## Next source datum

The needed source extraction is now two pieces rather than one opaque matrix:

- the radical subspace of the relative three-port Green form;
- the reciprocal action on its oriented front basis.

Once those are known, the two minimal hostiles become executable without yet knowing the full completed RH operator.
