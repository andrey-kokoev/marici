"""Pattern extended: 20, 24, 28, 32 point carriers."""
print("=== Extended pattern: 4n points = n SM generations ===")

for n in [5, 6, 7, 8]:
    pts = 4 * n
    print(f"\nS{pts} ({pts} points) -> {n} x S4 -> {n} SM generations")
    extra = ""
    if pts % 8 == 0:
        extra = f" + Z2 mirror ({pts//8} twin Higgs sectors)"
    elif pts >= 16:
        extra = " + GUT possibility"
    print(f"  Physics: {n} generations{extra}")
    print(f"  Status: exceeds observed 3 generations")

# Special structures at specific sizes
print("\n=== Special unification structures ===")
print("S20 (20): S4 x S4 x S4 x S4 x S4 = 5 gen, no special GUT")
print("S24 (24): S4 x S4 x ... (6x) = 6 gen, or S6 x S4 x S4?")
print("  Also: 4! = 24 = order of S4? Not a carrier size.")
print("  Spin(24) spinor = 2^11 = 2048, not 24.")
print("S28 (28): 7 gen, no special structure")
print("S32 (32): S4 x S4 x ... (8x) = 8 gen")
print("  OR: S16 x S16 -> 2 x SO(10) = two-family GUT")
print("  OR: Cl(5) = 32D (5D Clifford algebra)")
print("  OR: SO(10) x SO(10): two GUT copies (bipartite model)")

print("\n=== Minimality selection ===")
print("S4 = 1 gen (minimal SM, but only 1 generation)")
print("S8 = 2 gen + twin Higgs (mirror symmetry)")
print("S12 = 3 gen (matches observation, minimal for 3 generations)")
print("S16+ = 4+ gen (exceeds observation, requires GUT or extra sectors)")
print()
print("Selection principle: S12 is the smallest carrier that gives")
print("3 SM generations without extra mirror or GUT sectors.")
print("This matches observed physics exactly.")

result = {
    'pattern': '4n points = n SM generations (S4 x S4 x ... x S4)',
    'S20': '5 generations (too many)',
    'S24': '6 generations, or 4! = 24 (S4 order)',
    'S28': '7 generations',
    'S32': '8 generations, or SO(10) x SO(10), or Cl(5) algebra',
    'observed': '3 generations',
    'minimal_3_gen_carrier': 'S12 (12 points)',
}

print(f"\n{json.dumps(result, indent=2)}")