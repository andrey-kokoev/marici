# Constructor logical resource accounting

Fresh preflight extension reports constructor_peak_agents, constructor_agent_allocations, constructor_fresh_names and total_fresh_name_bound. These fields concern successful ScanningSetProgram construction on validated finite values, not failed constructors or Python heap memory.

Let A be the exact final postcompile agent count already computed, and R the number of ifadd plus scan instructions. Total add calls = A+R: each such instruction removes exactly one temporary GM and no other constructor deletes agents. Fresh-name calls = A+R-2 because RET and ACK are the only fixed-name agent additions; every other add receives exactly one fresh name.

Peak live graph agents during compilation is exactly A, despite temporarily overlapping old/new gates. Before replacement, the fresh gate temporarily adds one agent; deleting its placeholder subtracts one; then ifadd adds two nonempty unary chains (at least two NILs), or scan adds one nonempty fuel chain (at least one NIL). Each completed replacement ends at least as high as its own temporary peak. All base compilation stages are monotone additions. Induction through conditional replacement followed by scan replacement therefore bounds every transient by the final A, which is itself attained. This argument depends on the present constructor ordering, not arbitrary replacement implementations.

The combined execution bound remains A+2T for logical live agents; total fresh names including construction are A+R-2+4T. No maximum Python dictionary size/bytes, tuple materialization, garbage-collector retention or allocation-failure transaction guarantee follows.

Instrumented every add/fresh across3110 constructor fixtures (all programs through length4 over six fixtures, two words). Exact peak, allocation and serial formulas all pass, including empty alternative budgets, adjacent GC/GS and nonzero cursor/fuel. The fresh15-suite closure also passes.

Next useful client-facing step: optional admission limits on these explicitly named logical quantities in the narrow facade, computed after input normalization but before graph construction. Such a policy can reject large unary expansions without claiming to constrain normalization of arbitrary iterators. Keep default behavior and rejection semantics explicit, and test threshold equality/one-below and no graph allocation on rejection. This is admission based on conservative bounds, not a process memory sandbox.
