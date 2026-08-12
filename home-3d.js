import * as THREE from 'three';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.166.1/examples/jsm/loaders/GLTFLoader.js';

const modelUrl = '/navisights-trike/navisights_trike_assy_file.gltf';

function addStatsTreatment() {
  const title = [...document.querySelectorAll('h2')].find((node) => node.textContent.trim() === 'Maximum Speed');
  if (!title) return false;

  const grid = title.closest('section > div');
  if (!grid || grid.dataset.trikeStats) return true;
  grid.dataset.trikeStats = 'true';
  grid.classList.add('trike-stat-grid');
  [...grid.children].forEach((stat) => stat.classList.add('trike-stat'));
  return true;
}

function addModel() {
  const slot = document.querySelector('.order-first.md\\:order-last.z-10');
  if (!slot || slot.dataset.trikeMounted) return Boolean(slot);
  slot.dataset.trikeMounted = 'true';

  const stage = document.createElement('div');
  stage.className = 'trike-stage';
  stage.innerHTML = '<img class="trike-fallback" src="/view-1.jpg" alt="Navisights autonomous electric vehicle"><span class="trike-loading">Loading vehicle model…</span>';
  slot.append(stage);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(34, 1, 0.01, 100);
  camera.position.set(5.2, 3.1, 5.2);

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setClearColor(0x000000, 0);
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.shadowMap.enabled = true;
  stage.append(renderer.domElement);

  scene.add(new THREE.HemisphereLight(0xe7d9ff, 0x12051c, 2.4));
  const key = new THREE.DirectionalLight(0xffb5e7, 3.5);
  key.position.set(4, 6, 5);
  scene.add(key);
  const rim = new THREE.DirectionalLight(0x9b8cff, 3);
  rim.position.set(-5, 2, -4);
  scene.add(rim);

  const floor = new THREE.Mesh(
    new THREE.CircleGeometry(4.5, 64),
    new THREE.MeshBasicMaterial({ color: 0x7c3aed, transparent: true, opacity: 0.1 })
  );
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = -1.1;
  scene.add(floor);

  const loader = new GLTFLoader();
  loader.load(modelUrl, (gltf) => {
    const vehicle = gltf.scene;
    vehicle.traverse((child) => {
      if (child.isMesh) {
        child.castShadow = true;
        child.receiveShadow = true;
      }
    });
    const box = new THREE.Box3().setFromObject(vehicle);
    const size = box.getSize(new THREE.Vector3()).length();
    const center = box.getCenter(new THREE.Vector3());
    vehicle.position.sub(center);
    vehicle.position.y += -0.15;
    const scale = 4.25 / size;
    vehicle.scale.setScalar(scale);
    scene.add(vehicle);
    stage.querySelector('.trike-loading')?.remove();
    stage.querySelector('.trike-fallback')?.remove();
  }, undefined, () => {
    stage.querySelector('.trike-loading').textContent = 'Vehicle model could not load.';
  });

  function resize() {
    const { width, height } = stage.getBoundingClientRect();
    if (!width || !height) return;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  }
  new ResizeObserver(resize).observe(stage);
  resize();

  let previous = performance.now();
  function animate(now) {
    const delta = (now - previous) / 1000;
    previous = now;
    scene.rotation.y += delta * 0.18;
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);
  return true;
}

const timer = setInterval(() => {
  const modelReady = addModel();
  const statsReady = addStatsTreatment();
  if (modelReady && statsReady) clearInterval(timer);
}, 100);

const style = document.createElement('style');
style.textContent = `
  html, body, #root { min-height: 100%; background: #05000a !important; }
  .trike-stage { position: relative; width: min(100%, 680px); height: clamp(340px, 58vh, 680px); margin: 0 auto; }
  .trike-stage canvas { display: block; width: 100%; height: 100%; filter: drop-shadow(0 24px 35px rgba(168, 85, 247, .28)); }
  .trike-fallback { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; opacity: .9; mix-blend-mode: screen; filter: drop-shadow(0 24px 35px rgba(168, 85, 247, .28)); }
  .trike-loading { position: absolute; inset: 50% auto auto 50%; transform: translate(-50%, -50%); color: #f5d0fe; font: 600 14px Raleway, sans-serif; letter-spacing: .1em; white-space: nowrap; }
  .trike-stat-grid { width: min(100% - 2rem, 960px) !important; gap: 1rem; padding: 1rem 0; }
  .trike-stat { min-width: 170px; padding: 1.25rem 1rem; border: 1px solid rgba(216, 180, 254, .32); border-radius: 1rem; background: linear-gradient(145deg, rgba(76, 29, 149, .3), rgba(20, 4, 32, .7)); box-shadow: inset 0 1px rgba(255,255,255,.08), 0 16px 32px rgba(0,0,0,.25); }
  .trike-stat h1 { font-weight: 800; text-shadow: 0 0 24px rgba(236, 72, 153, .32); }
  @media (max-width: 767px) { .trike-stage { height: 390px; } .trike-stat-grid { width: min(100% - 2rem, 420px) !important; } }
`;
document.head.append(style);
