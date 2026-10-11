"""Replay complete legacy evidence without writing/deleting historical receipts.
uv run --with scipy python research/nima/checkers/collect_quantum_readout_diagnostics.py
"""
import ast
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT/'quarantine/20261007-quantum-readout-evidence'


def replay(path, mutate_bell=False):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    removed = []
    class Writes(ast.NodeTransformer):
        def visit_Expr(self,node):
            f = node.value.func if isinstance(node.value,ast.Call) else None
            if isinstance(f,ast.Attribute) and isinstance(f.value,ast.Name) and f.value.id == 'out':
                if f.attr == 'unlink':
                    removed.append('unlink')
                    return None
                if f.attr == 'write_text':
                    removed.append('write_text')
                    return ast.copy_location(ast.parse('_captured.append(result)').body[0],node)
            return self.generic_visit(node)
    tree = Writes().visit(tree)
    expected = ['unlink','write_text'] if path.name == 'check_gram_selection_principle.py' else ['write_text']
    assert sorted(removed) == sorted(expected)
    if mutate_bell:
        at = [i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign)
              and any(isinstance(t,ast.Name) and t.id == 'a' for t in n.targets)]
        assert len(at) == 1
        tree.body[at[0]:at[0]] = ast.parse('G_bell = [row[:] for row in G_sep]').body
    env = {'__file__':str(path),'__name__':'__main__','_captured':[]}
    with redirect_stdout(io.StringIO()):
        exec(compile(ast.fix_missing_locations(tree),str(path),'exec'),env)
    assert len(env['_captured']) == 1
    return env


def main():
    receipts = [ROOT/'results'/f for f in ('gram-selection-principle.json','entanglement-from-gram.json')]
    before = [p.read_bytes() if p.exists() else None for p in receipts]
    gp,bp = (ARCHIVE/'checkers'/f for f in ('check_gram_selection_principle.py','check_entanglement.py'))
    g,b = replay(gp),replay(bp)
    hostile = replay(bp,mutate_bell=True)
    assert hostile['G_bell'] == hostile['G_sep'] and hostile['S'] == b['S']
    pairs = g['_captured'][0]['two_slit_pairs']
    failures = {name:row['tests'][0] for name,row in pairs.items()
                if abs(row['tests'][0]['I']-row['tests'][0]['expected']) > 1e-8}
    assert len(failures) == 10
    assert before == [p.read_bytes() if p.exists() else None for p in receipts]
    paths = [Path(__file__).resolve(),gp,bp]
    result = {
        'schema':'marici.nima.quantum-readout-transport.v1',
        'evidence_role':'complete legacy replay; numerical reports are raw data, not proof',
        'filler_names':list(g['FILLERS']),
        'vectors':[g['image_vec'](f) for f in g['FILLERS'].values()],
        'unasserted_zero_phase_pair_mismatches':failures,
        'legacy_bell_gram':b['G_bell'],'legacy_product_gram':b['G_sep'],
        'legacy_bell_S':b['S'],'state_replaced_by_product_S':hostile['S'],
        'legacy_product_same_x_correlation':b['expectation_product'](b['math'].pi/2),
        'historical_receipts_unchanged':True,
        'source_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):
                         hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (ROOT/'results/quantum-readout-transport.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'unchecked_pair_failures':len(failures),'bell_state_replacement_ignored':True,
                      'legacy_product_same_x_correlation':result['legacy_product_same_x_correlation']}))


if __name__ == '__main__':
    main()
