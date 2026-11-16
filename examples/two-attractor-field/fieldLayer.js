import { attractors, sampleField, stepShuttle, targetWeights, initialTarget, passRadius, defaults } from './model.js';

// Model-specific scene content; lifecycle, camera and scheduling stay in the reference viewer.
export function createFieldLayer(THREE, scene, track) {
  let settings = defaults(), particles = [], accumulator = 0, steps = 0, target = null, switches = 0;
  const maxParticles = 1, trailLength = 40, trails = [];
  function lines(size, color, opacity = 1) {
    const data = new Float32Array(size);
    const geometry = track(new THREE.BufferGeometry());
    geometry.setAttribute('position', new THREE.BufferAttribute(data, 3));
    const material = track(new THREE.LineBasicMaterial({ color, transparent: opacity < 1, opacity }));
    const object = new THREE.LineSegments(geometry, material);
    object.frustumCulled = false; scene.add(object);
    return { data, geometry };
  }
  const arrows = lines(33 * 21 * 18, 0xffc66d);
  const trail = lines(maxParticles * (trailLength - 1) * 6, 0x77bfa9, 0.4);
  const grid = lines(28 * 6, 0x34445c);
  let g = 0;
  for (let x = -8; x <= 8; x++) for (const n of [x,-5,0,x,5,0]) grid.data[g++] = n;
  for (let y = -5; y <= 5; y++) for (const n of [-8,y,0,8,y,0]) grid.data[g++] = n;
  const pointData = new Float32Array(maxParticles * 3);
  const pointGeometry = track(new THREE.BufferGeometry());
  pointGeometry.setAttribute('position', new THREE.BufferAttribute(pointData, 3));
  const points = new THREE.Points(pointGeometry, track(new THREE.PointsMaterial({ color: 0x98f0d0, size: 4, sizeAttenuation: false })));
  points.frustumCulled = false; scene.add(points);
  const halos = [];
  for (const [i, a] of attractors.entries()) {
    const halo = new THREE.Mesh(track(new THREE.RingGeometry(passRadius - 0.025, passRadius, 64)),
      track(new THREE.MeshBasicMaterial({color:0xf4c430,side:THREE.DoubleSide,transparent:true,opacity:0.8})));
    halo.position.set(a.x,a.y,0.04);halo.visible=false;scene.add(halo);halos.push(halo);
    const marker = new THREE.Mesh(track(new THREE.SphereGeometry(0.15, 16, 12)), track(new THREE.MeshBasicMaterial({ color: i ? 0x79d6ff : 0xff887b })));
    marker.position.set(a.x, a.y, 0.1); scene.add(marker);
    // Real scene labels, retained when orbiting the planar model.
    const canvas = document.createElement('canvas');canvas.width = 64;canvas.height = 64;
    const ctx = canvas.getContext('2d');ctx.fillStyle = i ? '#79d6ff' : '#ff887b';
    ctx.font = 'bold 44px system-ui';ctx.textAlign = 'center';ctx.fillText(i ? 'B' : 'A', 32, 48);
    const texture = track(new THREE.CanvasTexture(canvas));
    const label = new THREE.Sprite(track(new THREE.SpriteMaterial({ map: texture, depthTest: false })));
    label.position.set(a.x, a.y + 0.55, 0.2);label.scale.set(0.6, 0.6, 1);scene.add(label);
  }
  function syncParticles() {
    let j = 0;
    particles.forEach((p, i) => {
      pointData.set([p.x, p.y, 0.18], i * 3);
      for (let k = 1; k < trailLength; k++)
        for (const v of [trails[i][k-1].x, trails[i][k-1].y, 0.08, trails[i][k].x, trails[i][k].y, 0.08]) trail.data[j++] = v;
    });
    pointGeometry.setDrawRange(0, particles.length);
    trail.geometry.setDrawRange(0, particles.length * (trailLength - 1) * 2);
    pointGeometry.attributes.position.needsUpdate = true;
    trail.geometry.attributes.position.needsUpdate = true;
  }
  function update(state) {
    settings = { ...settings, ...state };
    halos.forEach((halo,i)=>{halo.visible=i===target;});
    let index = 0;
    const segment = (x,y,u,v) => { for (const n of [x,y,0.03,u,v,0.03]) arrows.data[index++] = n; };
    for (const p of sampleField(target === null ? settings : targetWeights(settings,target))) {
      if (p.magnitude < 1e-10) continue;
      const length = 0.44 * Math.tanh(p.magnitude * 3), dx = p.vx / p.magnitude, dy = p.vy / p.magnitude;
      const x = p.x - dx * length / 2, y = p.y - dy * length / 2, tx = x + dx * length, ty = y + dy * length, head = length * 0.28;
      segment(x,y,tx,ty);
      segment(tx,ty,tx-head*dx-head*dy*.55,ty-head*dy+head*dx*.55);
      segment(tx,ty,tx-head*dx+head*dy*.55,ty-head*dy-head*dx*.55);
    }
    arrows.geometry.setDrawRange(0, index / 3);arrows.geometry.attributes.position.needsUpdate = true;
  }
  function advance(dt) {
    accumulator += dt;
    while (accumulator >= 1/120) {
      particles = particles.map((p,i) => {
        const result = stepShuttle(p, settings, settings.damping, 1/120, target);
        const next = result.particle;
        if (result.switched) { target = result.target; switches++; update(settings); }
        if (steps % 4 === 0) { trails[i].shift();trails[i].push({ ...next }); }
        return next;
      });
      accumulator -= 1/120;steps++;
    }
    syncParticles();
  }
  function reset() {
    particles = [];trails.length = 0;accumulator = 0;steps = 0;target = null;switches = 0;
    syncParticles();update(settings);
  }
  function place(x, y) {
    reset();
    const particle = { x, y, vx: 0, vy: 0 };
    target = initialTarget(x,y);update(settings);
    particles.push(particle);
    trails.push(Array.from({ length: trailLength }, () => ({ ...particle })));
    syncParticles();
  }
  reset();update(settings);
  return { update, advance, reset, place, snapshot: () => ({ steps, target, switches, particles: particles.map(p => ({ ...p })) }) };
}
