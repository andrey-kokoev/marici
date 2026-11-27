from ramsey_double_flank_geometry import D, run, sha256, save, json


def main():
    charts = [run(first) for first in range(9)]
    previous = json.loads((D.parent / 'ramsey_double_flank_geometry.json').read_text())
    for chart in previous['charts']:
        assert json.loads(json.dumps(charts[chart['first']])) == chart
    results = []
    for first, chart in enumerate(charts):
        mirror = charts[8-first]['reading_gaps']
        assert chart['reading_gaps'] == {9-gap: n for gap, n in mirror.items()}
        misses = [c for c in chart['cases'] if c['gap'] not in (first, first+1)]
        results.append(dict(first=first, usable=len(chart['cases']), noncontact=len(misses), example=next(iter(misses), None)))
    print(results)
    protocol = D.parent / 'ramsey_double_flank_contact_protocol.md'
    save(D.parent / 'ramsey_double_flank_contact.json', dict(protocol_sha=sha256(protocol.read_bytes()).hexdigest(), results=results, charts=charts))


if __name__ == '__main__':
    main()
