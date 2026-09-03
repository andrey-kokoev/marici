# Generic fiber dimension of the four-ray Bargmann map

## Question

Even away from the explicit zero collision, can one complex four-ray Bargmann invariant generically identify a labelled qubit-ray configuration modulo simultaneous unitary action?

## Claim boundary

This packet treats generic labelled quadruples of rank-one projectors on \(\mathbb C^2\). It establishes a local dimension obstruction at regular points. It does not compute the special fiber of Kitaev's frozen discrete `D(S3)` family at \(-1/8\).

## Quotient dimension

A qubit ray lies in \(\mathbb{CP}^1\), of real dimension two. Four labelled rays therefore have real dimension eight. Simultaneous projective-unitary action has generic orbit dimension three, leaving a five-dimensional generic quotient.

The ordered Bargmann invariant is one complex scalar, hence at most two real coordinates. At a regular point where its real and imaginary parts have Jacobian rank two, its quotient fiber has local dimension at least

\[
5-2=3.
\]

Thus one complex loop coordinate is generically far from faithful.

## Exact affine calculation

Fix the first ray as \([1:0]\). Write the remaining rays as normalized affine vectors proportional to

\[
(1,z_2),\quad(1,z_3),\quad(1,z_4).
\]

The ordered Bargmann invariant is

\[
B=
\frac{(1+\overline z_2z_3)(1+\overline z_3z_4)}
{(1+|z_2|^2)(1+|z_3|^2)(1+|z_4|^2)}.
\]

The six real affine variables retain a one-dimensional stabilizer of the fixed first ray, acting by common phase rotation of the \(z_i\). The checker evaluates the exact Jacobian of \((\operatorname{Re}B,\operatorname{Im}B)\) at a rational complex fixture and obtains rank two. The prequotient local fiber has dimension four; removing the stabilizer direction leaves dimension three.

## Consequence

Any claim that one Bargmann value reconstructs a generic four-ray associator configuration is dimensionally impossible. Faithfulness can still occur on a finite or specially constrained source family, but that constraint must be explicit and source-derived. In that case the correct test is direct fiber enumeration or an exact injectivity theorem on the constrained quotient.

## Kitaev placement

Kitaev's frozen electric projectors may occupy a zero-dimensional or otherwise restricted family, so generic nonfaithfulness does not settle the \(-1/8\) fiber. It changes the burden of proof: faithfulness must come from the frozen-family restriction, not from the Bargmann observable alone.

## Disposition

The four-copy observable has a generic three-real-dimensional unresolved quotient fiber for labelled qubit rays. The pending request for Kitaev's explicit admissible-family quotient is therefore necessary, not merely a request for presentation detail.

## Verification

- `research/voevodsky/checkers/check_bargmann_generic_fiber_dimension.py`
- `research/voevodsky/results/bargmann_generic_fiber_dimension.json`
