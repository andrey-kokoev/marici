"""Generate the public, offline-capable matter atlas from the validated registry."""
import argparse
import json
from pathlib import Path
from check_catalog import validate

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / 'website/public/experiments'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail on missing or stale generated assets; do not write.')
    args = parser.parse_args()
    raw = (HERE / 'element-isotope-catalog.json').read_text(encoding='utf-8')
    data = json.loads(raw)
    result = validate(data)
    template = (HERE / 'catalog.template.html').read_text(encoding='utf-8')
    marker = '__CATALOG_JSON__'
    if template.count(marker) != 1:
        raise ValueError('Template must contain exactly one data marker')
    # Escape HTML delimiters so record text can never terminate the JSON script.
    payload = json.dumps(data, ensure_ascii=True).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    html = template.replace(marker, payload)
    graph_raw = (HERE / 'standard-model-graph.json').read_text(encoding='utf-8')
    json.loads(graph_raw)
    assets = {
        OUT / 'matter-catalog.html': html,
        OUT / 'matter-catalog.json': raw,
        ROOT / 'website/public/standard-model-graph.json': graph_raw,
    }
    for target, content in assets.items():
        if args.check:
            if not target.is_file() or target.read_text(encoding='utf-8') != content:
                raise ValueError(f'Stale asset: {target.relative_to(ROOT)}')
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding='utf-8')
    print(json.dumps({**result, 'public_url': '/experiments/matter-catalog.html', 'assets_current': True, 'check_only': args.check}, indent=2))


if __name__ == '__main__':
    main()
