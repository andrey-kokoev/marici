# Gram residue uses the quadratic representation, and wall removal does not make multiplication compact

## Linear versus quadratic representation

Let \(\mathcal F_{\mathrm{cell}}\) be the coefficient space and let

\[
e_{\mathrm{wall}}
\]

be the constant-wall basis vector. The linear multiplication representation is

\[
\pi:\mathcal F_{\mathrm{cell}}
\to
\mathcal B(H_q),
\qquad
\pi(e_{\mathrm{wall}})=-I.
\]

The coefficient Gram residue is

\[
R_{\mathrm{coeff}}
=
|e_{\mathrm{wall}}\rangle
\langle e_{\mathrm{wall}}|.
\]

It is not an element of the original coefficient vector space. Therefore the expression

\[
\pi(R_{\mathrm{coeff}})
\]

is undefined until \(\pi\) is lifted to a quadratic or operator-system representation.

## Induced Gram representation

For rank-one coefficient operators, define

\[
\Gamma_\pi
\left(
|u\rangle\langle v|
\right)
=
\pi(u)^*\pi(v).
\]

Then

\[
\Gamma_\pi(R_{\mathrm{coeff}})
=
\pi(e_{\mathrm{wall}})^*
\pi(e_{\mathrm{wall}})
=
(-I)^*(-I)
=
I.
\]

The sign is fixed: a positive Gram residue maps to \(+I\), not \(-I\). The negative wall orientation exists at the linear-history level and disappears after taking the Gram.

This distinction prevents a sign error in the residue-intertwining diagram.

## Correct residue diagram

The required limit statement is

\[
\Gamma_\pi
\left(
\lim_{\sigma\downarrow0}
2\sigma G_\sigma^{\mathrm{coeff}}
\right)
=
\lim_{\sigma\downarrow0}
2\sigma
\Gamma_\pi
\left(
G_\sigma^{\mathrm{coeff}}
\right)
=
I.
\]

To justify it, one needs:

1. a topology on the coefficient Gram operator system;
2. continuity of \(\Gamma_\pi\) on the bounded residue family;
3. convergence of the rescaled coefficient Gram;
4. domination on the analytic core.

Continuity of the linear map \(\pi\) alone does not automatically imply continuity of the quadratic lift on an unbounded family.

## Coefficient subtraction

If the coefficient decomposition is source-derived,

\[
G_\sigma^{\mathrm{coeff}}
=
\frac1{2\sigma}R_{\mathrm{coeff}}
+
G_{\mathrm{reg},\sigma}^{\mathrm{coeff}},
\]

then

\[
\Gamma_\pi
\left(
G_\sigma^{\mathrm{coeff}}
\right)
=
\frac1{2\sigma}I
+
\Gamma_\pi
\left(
G_{\mathrm{reg},\sigma}^{\mathrm{coeff}}
\right).
\]

Subtracting \(I/(2\sigma)\) after representation is authorized only through this identity.

## Compactness trap after wall removal

Even when the wall is removed correctly, multiplication does not become compact automatically.

Let \(r(q)\) be a nonzero bounded remainder function. On the non-atomic space

\[
L^2(\mathbb R,dq),
\]

the multiplication operator

\[
M_r\psi=r\psi
\]

is compact only if \(r=0\) almost everywhere.

Indeed, if \(|r|\ge\epsilon\) on a set of positive measure, split that set into countably many disjoint positive-measure subsets and choose normalized indicator functions. Their images under \(M_r\) remain mutually orthogonal with norms at least \(\epsilon\), so no subsequence converges.

Therefore decay of

\[
W_t+1
\]

at spatial infinity or at large prime scale does not make its multiplication representation compact.

## Determinant-class consequence

A nonzero multiplication remainder on \(L^2(\mathbb R)\) is generally neither compact nor trace class. Hence one cannot form an ordinary Fredholm determinant from

\[
I+\Gamma_\pi(G_{\mathrm{reg}})
\]

merely because the identity residue was removed.

A determinant-class object requires an additional source-authorized operation, such as:

- compression to a discrete or finite-measure spectral subspace with compact embedding;
- an integral Green kernel providing smoothing;
- a relative determinant in an authorized operator ideal;
- a determinant-line construction before the multiplication representation.

## What wall removal does prove

The coefficient wall theorem explains the unique nondecaying representation direction:

\[
e_{\mathrm{wall}}\mapsto-I.
\]

Removing it may produce a controlled relative operator in a weaker sense:

- bounded;
- locally compact after localization;
- compact between different weighted spaces;
- form-compact relative to a declared generator.

Each property must be proved separately. None follows from coefficient rank one.

## Revised order

The admissible programme is:

1. split the wall in coefficient space;
2. prove the coefficient Gram residue;
3. lift \(\pi\) to the quadratic representation \(\Gamma_\pi\);
4. prove residue-limit intertwining;
5. identify the represented regular operator;
6. classify its actual ideal property;
7. use only the determinant notion authorized by that ideal.

## Minimal hostiles

### Wrong sign lift

The wall vector maps to \(-I\), and the Gram projector is incorrectly declared to map to \(-I\). Positivity is violated.

### Linear/quadratic type confusion

The linear representation \(\pi\) is applied directly to a coefficient projector outside its domain.

### False compactness

The wall is removed and the remaining multiplier decays, so it is called compact. A disjoint-support orthonormal sequence disproves the claim.

### Unsupported determinant

A Fredholm determinant is formed without proving that the represented regular part belongs to a determinant ideal.

## Current frontier

The coefficient-rank resolution is correct, with one refinement:

\[
R_{\mathrm{coeff}}
\xmapsto{\Gamma_\pi}
I.
\]

But the next operator theorem is not automatically compactness. It is residue-limit intertwining followed by an honest ideal classification of the represented regular part. For pure multiplication, nonzero regular remainders remain noncompact.
