"""Register/copy only scattering net evidence; preserve unrelated snapshots/pins."""
import json
from pathlib import Path
from collect import HOME, ROOT, registry, digest

SOURCE = ROOT / 'research/scattering/high-energy'


if __name__ == '__main__':
    inventory_path = HOME / 'inventory.json'
    inventory = json.loads(inventory_path.read_text(encoding='utf-8'))
    entries = {entry['source']: entry for entry in inventory['files']}
    paths = [p for p in SOURCE.iterdir() if p.suffix in {'.md', '.py', '.json'}]
    paths += list((SOURCE / 'contracts').glob('*.json'))
    paths += list((SOURCE / 'results').glob('high-energy-net-*.json'))
    paths += [ROOT / 'research/nima/scc-models/high-energy-scattering-net-wiring-v1.json']
    for path in paths:
        name = path.relative_to(ROOT).as_posix()
        target = HOME / 'collection' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())
        entries[name] = {'source': name, 'collected': target.relative_to(HOME).as_posix(),
                         'sha256': digest(path), 'reason': 'high-energy scattering net source/evidence wiring'}
    inventory['files'] = [entries[name] for name in sorted(entries)]
    inventory_path.write_text(json.dumps(inventory, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    selected = {name: entry['reason'] for name, entry in entries.items()}
    result = registry(selected)
    (HOME / 'registry.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    if not any(entry['id'] == 'scattering.high-energy.v1' and entry['classification'] == 'conjecture-net contract'
               for entry in result['nets']):
        raise ValueError('Scattering contract failed registry classification')
    print(json.dumps({'status': 'registered', 'source': 'scattering.high-energy.v1',
                      'scattering_snapshots_updated': len(paths), 'binary_archives_copied': False,
                      'unrelated_inventory_pins_refreshed': False}))
