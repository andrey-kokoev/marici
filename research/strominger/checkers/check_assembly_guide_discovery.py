"""Check assembly-guide links, search terms, entrypoint pointers and code identity.

Navigation checks only; scientific example replay is a separate verification.
"""
import ast
import hashlib
import json
import re
import subprocess
import shlex
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GUIDE = ROOT / 'docs/arrow-assembly.md'
MARKDOWN = ['AGENTS.md', 'README.md', 'research/matter/README.md',
            'papers/witness-generators/README.md',
            'research/voevodsky/relative-geometric-source-constructor.md',
            'research/voevodsky/relative-geometric-reversible-mode-motion.md',
            'research/nima/twelve-triangle-positive-geometry.md',
            'research/voevodsky/electron-proton-assembly-relation.md']
SCRIPTS = ['research/voevodsky/checkers/assemble_relative_geometry.py',
           'research/voevodsky/checkers/evolve_relative_geometry_modes.py',
           'research/nima/checkers/assemble_triangle_arrow_source.py',
           'research/voevodsky/checkers/check_electron_tetrahedral_spinor.py']


def links(path):
    return re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8'))


def main():
    checks = {}
    for filename in MARKDOWN:
        path = ROOT / filename
        checks['guide_link:' + filename] = any(
            (path.parent / link.split('#')[0]).resolve() == GUIDE.resolve()
            for link in links(path) if '://' not in link)
    broken = []
    for link in links(GUIDE):
        if '://' not in link and not (GUIDE.parent / link.split('#')[0]).exists():
            broken.append(link)
    checks['guide_local_links_resolve'] = not broken
    text = GUIDE.read_text(encoding='utf-8')
    searches = {}
    for term in ['arrow assembly', 'electron', 'proton', 'assembly measures']:
        command = ['rg', '-l', '-i', '-F', term, 'docs', 'AGENTS.md', 'README.md', 'research/matter/README.md']
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=30)
        matches = result.stdout.replace('\\', '/').splitlines()
        checks['search:' + term] = result.returncode == 0 and 'docs/arrow-assembly.md' in matches
        searches[term] = {'command': command, 'returncode': result.returncode, 'matches': matches}
    for line in text.splitlines():
        if line.startswith('python '):
            tokens = shlex.split(line)
            checks['command_script:' + tokens[1]] = (ROOT / tokens[1]).is_file()
            if '--source' in tokens:
                source = tokens[tokens.index('--source') + 1]
                checks['command_input:' + source] = (ROOT / source).is_file()
    receipt = json.loads((ROOT / 'research/strominger/results/assembly-guide/verification.json').read_text())
    checks['example_receipt_passed'] = receipt['status'] == 'passed' and all(receipt['checks'].values())
    checks['replayed_sources_still_current'] = all(
        hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == expected
        for filename, expected in receipt['evidence_sha256'].items())
    code_hashes = {}
    for filename in SCRIPTS:
        content = (ROOT / filename).read_text(encoding='utf-8')
        tree = ast.parse(content)
        checks['script_pointer:' + filename] = 'docs/arrow-assembly.md' in ast.get_docstring(tree)
        # Exclude the module documentation from this baseline of executable code.
        if isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant):
            tree.body.pop(0)
        code_hashes[filename] = hashlib.sha256(ast.dump(tree, include_attributes=False).encode()).hexdigest()
    out = {'status': 'passed' if all(checks.values()) else 'failed',
           'scope': 'Navigation and local link checks; not scientific replay or a repository-wide search ranking test',
           'checks': checks, 'broken_links': broken, 'search_executions': searches,
           'executable_ast_baseline_sha256': code_hashes,
           'guide_sha256': hashlib.sha256(GUIDE.read_bytes()).hexdigest()}
    dest = ROOT / 'research/strominger/results/assembly_guide_discovery.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
