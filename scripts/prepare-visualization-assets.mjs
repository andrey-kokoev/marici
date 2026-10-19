import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { prepareResearchLab } from './prepare-research-lab.mjs'

function withGalleryReturn(html, name) {
  const container = html.match(/<aside\b[^>]*>/) || html.match(/<main\b[^>]*>/)
  if (!container) throw new Error(`${name}: no navigation container`)
  return html.replace(container[0], container[0] + '<p class="publication-return" style="margin:0 0 12px;font:14px/1.5 system-ui"><a href="/experiments/" target="_self" style="color:#91d9ff">← Construction gallery</a></p>')
}

// Publish copies only: research pages and screenshots remain authoritative.
export async function prepareVisualizationAssets(root) {
  const out = path.join(root, 'website/public/experiments')
  await fs.mkdir(path.join(out, 'previews'), { recursive: true })
  await prepareResearchLab(root, out)
  // Publish the packet proposal from its authored source; reuse local Three.js.
  const packetOut = path.join(out, 'minimal-data-packet')
  await fs.mkdir(path.join(packetOut, 'vendor'), { recursive: true })
  for (const file of ['index.html', 'style.css', 'app.js', 'scene.js', 'model.mjs', 'electron.js', 'electron-model.mjs', 'preview.svg', 'tetra-preview.svg', 'electron-preview.svg', 'sketch.jpg']) {
    await fs.copyFile(path.join(root, 'research/voevodsky/demos/minimal-data-packet', file), path.join(packetOut, file))
  }
  for (const file of ['three.min.js', 'OrbitControls.js', 'THREE-LICENSE.txt']) {
    await fs.copyFile(path.join(root, 'research/nima/demos/paw-cycle/vendor', file), path.join(packetOut, 'vendor', file))
  }
  const electronTrialPath = 'research/voevodsky/results/electron-configuration-dimension-trial-v1.json'
  const electronTrial = JSON.parse(await fs.readFile(path.join(root, electronTrialPath), 'utf8'))
  if (!electronTrial.verification_passed || !Object.values(electronTrial.checks).every(Boolean) || !electronTrial.display_fixture) throw new Error('Electron packet trial is missing or failed; rerun check_electron_configuration_dimension_trial.py')
  for (const [file, expected] of Object.entries(electronTrial.source_sha256)) {
    if (createHash('sha256').update(await fs.readFile(path.join(root, file))).digest('hex') !== expected) throw new Error(`Stale electron packet trial: ${file}; rerun check_electron_configuration_dimension_trial.py`)
  }
  await fs.copyFile(path.join(root, electronTrialPath), path.join(packetOut, 'electron-trial.json'))
  await fs.copyFile(path.join(root, 'research/voevodsky/results/electron_tetrahedral_spinor_store.json'), path.join(packetOut, 'electron-native-store.json'))
  const photonPath = 'research/strominger/results/photon_shared_edge_seed.json'
  const photon = JSON.parse(await fs.readFile(path.join(root, photonPath), 'utf8'))
  if (photon.status !== 'passed' || !Object.values(photon.checks).every(Boolean)) throw new Error('Photon retained-stage record has failed checks')
  for (const [file, expected] of Object.entries(photon.source_hashes)) {
    const actual = createHash('sha256').update(await fs.readFile(path.join(root, file))).digest('hex')
    if (actual !== expected) throw new Error(`Stale photon evidence: ${file}; rerun the source checker`)
  }
  await fs.copyFile(path.join(root, photonPath), path.join(out, 'photon-shared-edge-seed.json'))
  for (const [source, publicName] of [
    ['reversed_matter_seeds', 'reversed-matter-seeds'],
    ['positron_reversed_seed', 'positron-reversed-seed'],
    ['polarization_reversal_transport', 'polarization-reversal-transport'],
    ['neutron-real-complex-checks', 'neutron-real-complex-checks'],
  ]) {
    const file = path.join(root, `research/strominger/results/${source}.json`)
    const record = JSON.parse(await fs.readFile(file, 'utf8'))
    if (record.status !== 'passed' || !Object.values(record.checks).every(Boolean)) throw new Error(`${source}: failed source checks`)
    for (const [dependency, expected] of Object.entries(record.source_hashes)) {
      if (createHash('sha256').update(await fs.readFile(path.join(root, dependency))).digest('hex') !== expected) throw new Error(`${source}: stale evidence ${dependency}`)
    }
    await fs.copyFile(file, path.join(out, `${publicName}.json`))
  }
  await fs.copyFile(path.join(root, 'research/strominger/inputs/neutron-real-complex-arrows.json'), path.join(out, 'neutron-real-complex-arrows.json'))
  const sources = [
    ['proton-neutron-assembly', [
      ['href="../../research/nima/checkers/check_twelve_packets_to_tetrahedron.py"', 'href="https://github.com/andrey-kokoev/marici/blob/main/research/nima/checkers/check_twelve_packets_to_tetrahedron.py"'],
      ['href="../../research/nima/checkers/check_twelve_triangle_positive_geometry.py"', 'href="https://github.com/andrey-kokoev/marici/blob/main/research/nima/checkers/check_twelve_triangle_positive_geometry.py"'],
    ]],
    ['electron-spinor-construction', []],
    ['fourth-construction', []],
    ['proton-source-assembly', [
      ['href="../../research/nima/checkers/check_twelve_packets_to_tetrahedron.py"', 'href="https://github.com/andrey-kokoev/marici/blob/main/research/nima/checkers/check_twelve_packets_to_tetrahedron.py"'],
      ['href="../../research/nima/checkers/check_twelve_triangle_positive_geometry.py"', 'href="https://github.com/andrey-kokoev/marici/blob/main/research/nima/checkers/check_twelve_triangle_positive_geometry.py"'],
    ]],
    ['retained-direction-observatory', [
      ['href="../../research/voevodsky/second-interface-observability.md"', 'href="https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/second-interface-observability.md"'],
    ]],
    ['potential-fold-explorer', [
      ['href="tetrahedron-dual-belt.html"', 'href="proton-neutron-assembly.html"'],
      ['two-tetrahedron assembly</a>', 'assembly workbench</a>'],
      ['href="../../research/voevodsky/retained-potential-realization.md"', 'href="https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/retained-potential-realization.md"'],
    ]],
    ['three-arrow-receiver', [
      ['href="../../research/voevodsky/three-arrow-receiver.md"', 'href="https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/three-arrow-receiver.md"'],
      ['href="../../research/voevodsky/three-arrow-receiver-geometry.md"', 'href="https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/three-arrow-receiver-geometry.md"'],
    ]],
  ]
  for (const [name, replacements] of sources) {
    let html = await fs.readFile(path.join(root, `papers/witness-generators/${name}.html`), 'utf8')
    for (const [from, to] of replacements) {
      if (html.split(from).length !== 2) throw new Error(`${name}: publication link replacement no longer unique: ${from}`)
      html = html.replace(from, to)
    }
    const marker = '<!-- Generated by scripts/prepare-visualization-assets.mjs; edit the research source instead. -->\n'
    // Keep the assembly source publisher's ownership sentinel compatible.
    if (name === 'proton-neutron-assembly') {
      html = html.replace('<!doctype html>', '<!doctype html>\n<!-- Generated by research/voevodsky/checkers/prepare_assembly_ledger_asset.py; edit the source assembly instead. -->')
    }
    await fs.writeFile(path.join(out, `${name}.html`), marker + withGalleryReturn(html, name), 'utf8')
  }
  for (const [source, name] of [
    ['retained_direction_observatory.png', 'observatory.png'],
    ['retained_phase_assembly.png', 'assembly.png'],
    ['potential_fold_explorer_modes.png', 'fold.png'],
    ['three_arrow_receiver_centers.png', 'receiver.png'],
  ]) await fs.copyFile(path.join(root, 'research/voevodsky/results', source), path.join(out, 'previews', name))
  await fs.copyFile(path.join(root, 'research/nima/results/barycentric-witness-packet.svg'), path.join(out, 'barycentric-witness-packet.svg'))
  for (const [source, name] of [
    ['proton-source-assembly', 'source-assembly'],
    ['electron-spinor-construction', 'spinor'],
    ['fourth-construction', 'fourth'],
    ['relational-growth', 'relational-growth'],
    ['paw-cycle', 'paw-cycle'],
    ['two-paws', 'two-paws'],
  ]) await fs.copyFile(path.join(root, `docs/visualization-previews/${source}.png`), path.join(out, `previews/${name}.png`))
  const demoNotes = {
    'relational-growth': 'Independent ordered-parent products, not fixed-vertex closure or a selected physical growth law. The view is a projection of supplied embedding coordinates.',
    'paw-cycle': 'The axes, rotations, unit-edge geometry and completion rule are supplied. Playback is illustrative, not physical time or an automatic quotient.',
    'two-paws': 'Local versus global path admission is an explicit choice. Individual tetrahedron volumes are not a union volume, mass or a derived filling of K6.',
  }
  for (const [name, note] of Object.entries(demoNotes)) {
    const target = path.join(out, 'retained-demos', name)
    await fs.rm(target, { recursive: true, force: true })
    await fs.mkdir(target, { recursive: true })
    for (const file of ['index.html', 'app.js']) {
      await fs.copyFile(path.join(root, 'research/nima/demos', name, file), path.join(target, file))
    }
    if (name === 'paw-cycle') {
      await fs.cp(path.join(root, 'research/nima/demos/paw-cycle/vendor'), path.join(target, 'vendor'), { recursive: true })
    }
    const index = path.join(target, 'index.html')
    let html = await fs.readFile(index, 'utf8')
    if (html.split('<main>').length !== 2) throw new Error(`${name}: expected one main element`)
    html = html.replace('<main>', `<main><p role="note" style="border:1px solid #526680;border-radius:6px;padding:12px;overflow-wrap:anywhere">Publication scope: ${note} No particle identity or measured parameter is established.</p>`)
    if (name === 'relational-growth') {
      for (const file of ['recursive-independent-family-comparison.md', 'dowker-identification-and-product-recurrence.md']) {
        const from = `href="../../${file}"`
        if (html.split(from).length !== 2) throw new Error(`${name}: publication link replacement no longer unique: ${from}`)
        html = html.replace(from, `href="https://github.com/andrey-kokoev/marici/blob/main/research/nima/${file}"`)
      }
    }
    await fs.writeFile(index, '<!-- Generated publication copy; edit research/nima/demos instead. -->\n' + withGalleryReturn(html, name), 'utf8')
  }
}
