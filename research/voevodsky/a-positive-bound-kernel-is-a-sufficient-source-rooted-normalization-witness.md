# A positive-bound kernel is a sufficient source-rooted normalization witness

For primitive rows A_i·x<=b_i, a Farkas certificate of target v·x<=T is `(m,c)` with `m>=0,c>=0,A^T m=v,b·m+c=T`. A typed source-rooted **sufficient** witness for consuming surplus is `d>=0`, `A^T d=0`, and `B=b·d>0`. Then `N_d(m,c)=(m+(c/B)d,0)` preserves both the target normal and bound, and nonnegativity. This abstracts the interval relation d=(1,1), B=L; the primitive bound contribution is indispensable.

Fresh `check_general_syzygy_normalizer.py` checks ten exact rational two-dimensional triangle examples with source `x>=0,y>=0,x+y<=1`: d=(1,1,1), B=1. It separately refuses (i) a source with no nonzero normal kernel, (ii) a kernel of zero bound contribution on x=0, and (iii) a vector whose normal does not cancel. Equal target endpoints alone cannot supply any of these witnesses.

The criterion is **not** a necessary characterization of all zero-surplus proofs, nor a canonical choice if several positive-bound kernel directions exist. Distinct d may produce distinct normalized multipliers, reviving a proof-level policy problem even where all public target inclusions agree. The next test must exhibit a multi-kernel source and compare two such normal forms, or justify a typed policy/2-cell. The free proof-history 4-cell and analytic S,A,R,C,G map remain independent unmet gates.
