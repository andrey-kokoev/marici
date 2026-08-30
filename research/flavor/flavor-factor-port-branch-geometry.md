# Factor-port branch geometry (WP385)

## Bounded question

Can factorization of the WP378 residual lower WP384's microscopic probe
degree while preserving exactly the same selected physical16 shell?

## Invariant factorization

On the nondegenerate domain with positive $\alpha\rho$, define

\[
\beta=2\sqrt{\alpha\rho},\qquad D=\Delta_u\Delta_d.
\]

Then

\[
F=C^2-\beta^2D^2=UV,
\qquad U=C-\beta D,\quad V=C+\beta D.
\]

Both factors have bifundamental field degree 12. A reference probe coupled to
one factor therefore has field degree 13 rather than WP384's degree 25. Two
factor-resolved ports distinguish the two shell branches by signatures
$(U,V)=(0,2\beta D)$ and $(U,V)=(-2\beta D,0)$.

## Union versus intersection

The desired shell is the union

\[
F=0\quad\Longleftrightarrow\quad UV=0.
\]

Independent positive factor penalties instead give

\[
U^2+V^2=2C^2+2\beta^2D^2,
\]

This vanishes only at the intersection $C=D=0$. For the hostile point
$C=\beta D$ with nonzero $D$, the original residual vanishes but the
separate penalty equals $4\beta^2D^2$. It therefore overselects.

Preserving the union requires

\[
U^2V^2=F^2,
\]

which restores field degree 48. Factorization lowers individual interface
degree only when the detector is allowed to expose and retain branch data.

## Groupoid and authority

The factor pair is weak-basis invariant when $C$, $D$, and $\beta$ are
source-defined invariants. Choosing the sign of $\beta$ permutes $U$ and
$V$; a labelled pair of ports fixes that permutation and hence defines an
augmented stabilizer-groupoid experiment. The ports reveal relative branch
membership, not an absolute phase.

Neither the factorization nor the ports derive $\beta$. Since $\beta$
contains the same free source ratio as WP378, they remain conditional
separators and presentation rigidifiers of branch labels, not numerical
selectors.

## Disposition

WP385 demonstrates a genuine degree-versus-geometry tradeoff. Two degree-13
interfaces can read the two branches, but independent positive penalties
change the admissible shell from a union to an intersection. The exact
equivalent positive selector retains degree 48.

The smallest falsifier is any nonzero point on $C=\beta D$. The remaining
gate is a source mechanism that preserves the union through executable
lower-degree operations without fitting $\beta$ or multiplying the factors
back into the original high-degree contact.

Run `uv run --with sympy python
research/flavor/checkers/wp385_factor_port_branch_geometry.py` to regenerate
the result.
