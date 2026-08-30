# Smith factors exactly decide an integral Mackey trace

Epistemic-graph event: 1356.

## Trace criterion

Let `S:Z^n->Z^m` be an integral Betti pushforward and let `d>0`.  There exists
an integral trace `T:Z^m->Z^n` satisfying

`S T=d I_m`

if and only if `S` has full row rank and every nonzero Smith invariant factor
`s_i` of `S` divides `d`.

In Smith bases, `S=[diag(s_1,...,s_m) 0]`.  The equation is solved by placing
`d/s_i` in the corresponding entries of `T`; integrality is exactly the
divisibility condition.  Necessity follows because `d Z^m` must lie in
`im(S)`, equivalently the cokernel of `S` is killed by `d`.

Thus the smallest possible norm scalar is

`d_min=lcm_i(s_i)`.

Any Mackey claim with prescribed geometric degree `d` fails integrally when
`d_min` does not divide `d`.

## Hostile controls

- `S=[2]`, `d=3`: no integral `T` exists because `2` does not divide `3`.
- `S=[2]`, `d=4`: `T=[2]` works, although `S` is not integrally split.
- A quotient incidence matrix with all Smith factors `1` admits an integral
  `d`-trace for every `d`; its canonical fiber trace is additional structure,
  not forced by the Smith condition alone.

When solutions exist, they form an affine space under maps landing in
`ker(S)`.  Hence the norm equation decides existence but not canonical trace
selection.

## Five-site consequence

The formal one-bit deck pushforward has only unit Smith factors, and the
fiber trace realizes `S T=2 I`.  A physical relative pushforward, if found,
must be checked degreewise: every Smith factor must divide the branch degree
`2^k`.  Any odd Smith factor or excessive two-adic exponent is an immediate
integral falsifier, independent of the boundary commutator.
