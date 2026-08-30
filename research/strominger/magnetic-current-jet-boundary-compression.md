# Current width two is boundary compression of a full grade jet

Let \(f_a=(f_{a,0},\ldots,f_{a,g})\), with
\(f_{a,j}=C_a^{(j)}/j!\), and let \(S\) shift grade upward. Exact source
transfer is

\[
f_{a+1}=T_g(x)f_a,\qquad
T_g(x)=(I-xS)(I+S)^{-1}.
\]

The determinant is one. For \(x\ne-1\),

\[
(T_g-I)^k=(-1)^k(1+x)^kS^k(I+S)^{-k},
\]

so \(T_g\) is a single unipotent Jordan block of length \(g+1\). The full
jet is generically minimal; the tempting pair of top grades is not closed.

The current quotient nevertheless has width at most two on the consecutive
depth lattice. Therefore width two cannot be the transported-state dimension.
It is the dimension left by the path/current boundary observation after the
ordinary columns are quotiented out.

Exact quotient coordinates distinguish the two wedges. Across 105 bounded
low-wedge parameter cases, after sufficient cutoff the quotient is generated
by the finite source window

\[
[K_0],\ldots,[K_{\beta-1}],
\]

its dimension is two, every one of those currents is nonzero individually,
and

\[
[K_a]=0\qquad(a\ge\beta).
\]

Two hostile cases at cutoff 15 falsely had widths three and four; both
stabilized to width two at cutoff 20 and then obeyed the source-window law.
Thus the low-wedge class is confined between the two source atoms rather than
merely concentrated near them. In a representative high-wedge case
\((3,10,4)\), both coordinates remain active through the tested depth
interval. These coordinates are unchanged when the cutoff increases from
10 to 15 to 20.

This supports the refined classification:

- low wedge: lower-boundary source-atom collision class;
- middle band: one sewn intrinsic current class;
- high wedge: two separated reflected-chain classes.

Parity decimation does not lose the intrinsic Jordan filtration merely by
replacing \(T_g\) with \(T_g^2\), since \(T_g+I\) is invertible in
characteristic zero. Its larger quotient arises because the admissible repair
columns are decimated as well. Sampling and repair authority must therefore
remain separately typed.

The unbounded proof target is a boundary observation exact sequence from the
full jet module to two endpoint classes, followed by separate localization
proofs for the low and high wedges.