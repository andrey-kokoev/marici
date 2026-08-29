# Cycles turn bridge connectivity into testable coherence and robust volume

Owner: marici.Kitaev

## Question

What new constructor capability appears when a connected bridge graph receives
its first redundant edge, and is that edge merely fault tolerance or the first
nonvacuous witness of higher coherence?

## Claim boundary

A spanning tree is sufficient for algebraic connectivity but insufficient for
internal certification of path coherence. The first cycle creates three things
at once:

- an alternate constructor route;
- a failure-tolerant bridge;
- a gauge-invariant holonomy comparing the routes.

Thus cycles are the first relational cells on which self-closure becomes a
falsifiable property rather than a vacuous consequence of unique paths.

Let the sector objects be vertices of a graph and let an invertible typed
bridge

\[
U_{ij}:V_j\to V_i
\]

label each oriented edge. A change of local sector frame acts by

\[
U_{ij}\longmapsto g_iU_{ij}g_j^{-1}.
\]

For a path \(P:j\to i\), write \(U_P\) for the ordered product of its edge
bridges. Two paths \(P,Q:j\to i\) define the relative comparison

\[
H_{P,Q}=U_Q^{-1}U_P.
\]

Under frame change this comparison is conjugated at the source endpoint. Its
conjugacy class, spectrum, trace invariants, or authorized central class is
therefore gauge invariant. For a closed cycle \(C\), this is the usual
holonomy

\[
H_C=U_{i_0i_{k-1}}\cdots U_{i_2i_1}U_{i_1i_0}.
\]

### Trees construct but cannot compare

On a tree there is exactly one simple path between any two vertices. Any
invertible edge assignment can be removed recursively by choosing local
frames. There is no cycle holonomy and hence no internal test distinguishing a
globally coherent bridge assignment from a differently framed one.

The tree can therefore generate the full linking algebra when adjoints and
full internal block controls are authorized, but it cannot certify that two
independently implemented routes agree: no alternate route exists.

This separates:

- **constructor completeness:** every sector is mutually reachable;
- **coherence observability:** alternate routes exist whose comparison can be
  tested.

The former begins at a spanning tree. The latter begins at the first cycle.

### The triangle is the smallest coherence laboratory

For three sectors with bridges \(U_{12},U_{23},U_{31}\), the cycle residual is

\[
H=U_{31}U_{23}U_{12}.
\]

Strict frame closure requires \(H=I\). Projective closure may require only

\[
H\in Z_{\mathrm{authorized}}.
\]

Braided or defect-bearing closure may prescribe a specific noncentral
comparison 2-cell. The residual is then the mismatch between \(H\) and that
authorized cell; it must not be collapsed prematurely to a scalar trace.

For one-dimensional complex sectors, the bridges are nonzero complex numbers.
Local rephasings remove all tree-edge phases, while the cycle retains the
single invariant phase

\[
\arg(U_{31}U_{23}U_{12}).
\]

This is the minimal example where every pairwise bridge magnitude can agree
and yet global constructor composition carries an undetected phase until the
third edge is installed.

### Robust relational volume

Attach a conditioned lower gain \(c_e>0\) to each required bridge direction.
Along a serial path the conservative guaranteed gain is bounded below by the
product

\[
c(P)\ge\prod_{e\in P}c_e.
\]

A tree has one path and therefore one bottleneck failure route. A cycle permits
an alternate path, so the task gain should be computed from the best or jointly
observed authorized route rather than from binary connectivity alone.

When internal block actions make edge observations isotropic, the weighted
graph Laplacian

\[
L_w=B^*WB
\]

is the scalar shadow of the bridge Gramian. Its second eigenvalue measures
global connectedness with conditioning. However, this reduction is valid only
after proving isotropy and common typing. In the general operator-valued case,
one needs a block incidence operator and its frame lower bound.

Cycles increase algebraic edge connectivity and can improve that lower bound,
but their gains can still collapse under completion. Therefore robust volume
requires both:

- a uniformly positive block-incidence frame bound;
- uniformly controlled cycle comparison cells.

### Relation to the earlier sectors

The toric code already exhibits the extreme form of this distinction. Local
incidence and contractible repair relations close on every cell, but the torus
has noncontractible cycles whose Wilson values remain invisible to local
syndrome. Loop probes do not repair a local defect; they expose global
holonomy classes absent from the tree-like local readout.

The \(D(S_3)\) qutrit pair-channel completes a two-vertex linking algebra, but
two vertices with one bridge have no independent cycle comparison. A
three-sector fusion fragment, or two genuinely different typed bridges between
the same sectors, is required to test whether separate compiler routes carry
the same Morita mate. This is the smallest next noncommutative audit.

### Hostile consequences

The proposed interpretation fails under any of these witnesses:

- a tree-only constructor family internally detects a path-composition defect
  without using an external reference;
- a nontrivial cycle holonomy can be removed by local frame changes despite
  fixed endpoint typing;
- every cycle comparison is correct while a task-relevant bridge kernel
  remains, showing coherence without fullness;
- graph Laplacian positivity is claimed although operator-valued edge
  directions share a hidden kernel;
- redundant cycles exist but all alternate-path gains vanish under completion.

The third witness is expected rather than paradoxical: cycle coherence and
relational completeness remain distinct gates even though cycles let them
interact.

## Disposition

The tower acquires a precise graph-theoretic staging:

1. vertices retain internally controlled sectors;
2. a spanning forest records disconnected relational components;
3. a spanning tree supplies minimal algebraic connectivity;
4. the first cycle supplies the first internally testable coherence cell;
5. additional independent cycles supply fault tolerance and a basis of global
   holonomy tests;
6. weighted block-frame bounds decide whether this structure survives
   completion.

For \(r\) initially separate blocks, \(r-1\) bridge incidences are minimally
sufficient for connectivity, while at least \(r\) are needed for one
independent cycle. The number of independent scalar cycle tests is the first
Betti number

\[
\beta_1=|E|-|V|+|\pi_0|.
\]

In noncommutative systems, \(\beta_1\) counts independent cycle generators but
not the dimension of their operator-valued holonomy data. That coefficient
lens remains essential.
