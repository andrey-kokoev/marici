# Reflection transport is rigid in slope but not in offset

A Deutsch-style explanation must be hard to vary.  To test this, consider the
affine-binomial source family

\[
\mathcal F_a(t,x)
=(1+t)^{ua+u_0}(1-xt)^{va+v_0}.
\]

Demanding the observed pole-depth shift

\[
\frac{\mathcal F_{a+2}}{\mathcal F_a}
=\left(\frac{1-xt}{1+t}\right)^2
\]

uniquely fixes

\[
u=-1,\qquad v=1.
\]

This follows from the valuations at the independent divisors `t=-1` and
`xt=1`.  Thus the opposite pole-depth slopes are rigid.

However, the additive exponents `u_0,v_0` cancel from the quotient.  In
particular, the one-parameter family

\[
\mathcal F_a^{(h)}(t,x)
=(1+t)^{-a}(1-xt)^{a-h}
\]

has exactly the same square reflection character for every `h`.

Applying the magnetic Euler operator does not remove this freedom.  For every
`h`:

- the transported numerator remains quadratic in grade variable `t`;
- its shift under `a -> a+2` is still
  \[
  2(1+x)(2tx-1);
  \]
- the magnetic contiguous law remains order four.

Yet the deformation is not merely a coordinate gauge.  Changing `h=4` to
`h=5` changes the numerator by

\[
N_5-N_4=-tx^2(t+1)
\]

and changes the right endpoint character from
`(4-a) rising g` to `(5-a) rising g`.

Therefore the current explanation is only partially rigid:

\[
\boxed{
\text{reflection geometry fixes the transport slopes, but not the offset }h=4.
}
\]

Finite memory, the square shift character, and order-four magnetic transport
all survive a genuine neighboring family.  Some additional source principle
must select `h=4`.  Candidate selectors include the original differential
order, the admissible pole-depth lattice, reflection parity at the finite
boundary, or compatibility with the electric sector.  Until one of these
fixes `h`, the transport law is a strong mechanism but not yet a complete
hard-to-vary explanation.

The checker proves this classification symbolically within the stated
affine-binomial/Euler ansatz.
