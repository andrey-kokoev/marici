# The aligned plus chain is triangular in two polynomial charts

For an even shortened depth `4<=a<=g+4`, put `L=a-4`.  Its terminal source
coefficient is

\[
c_L=
\frac{g!(g+3)!}{(g-a+4)!(a-1)!}.
\]

Away from `d=g+3`, the magnetic leading coefficient at the common row `d-3`
is

\[
\boxed{
\lambda_{g,d,a}
=(d-g-3)
\frac{g!(g+3)!}{(g-a+4)!(a-1)!}.
}
\]

After reflecting the exponent coordinate about `d-3`, the column degree is
`a-3`.  These degrees are strictly increasing with pole depth, and every
leading coefficient is nonzero.  The aligned columns are therefore a
triangular polynomial basis.

On the divisor `d=g+3`, the common leading coefficient vanishes.  Reflect
instead about row `d-4`.  The replacement leading coefficient is

\[
\boxed{
\widetilde\lambda_{g,a}
=
\frac{g!(g+3)!}{(g-a+4)!(a-1)!}
\frac{g^2+9g+16-(2g+4)a}{g-a+5}.
}
\]

It cannot vanish at integral depth.  Indeed, a zero would require

\[
a=rac{g+7}{2}+rac1{g+2},
\]

which is never an integer for `g>=2`.  In this chart the degrees are `a-4`,
again strictly increasing.

Thus the growing aligned plus-chain has no internal rank defect in either
chart.  Its apparent support core is a presentation effect caused by a common
endpoint, and `q=2g+3` is an atlas transition rather than a kernel locus.

The remaining global step is now a boundary-compatibility statement: show
that eliminating this triangular basis leaves exactly the previously computed
even `2x2` or odd `3x3` collision response against `(0,-)`.
