import * as THREE from 'three';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.166.1/examples/jsm/loaders/GLTFLoader.js';

const root = document.getElementById('root');

function mountHome() {
  if (location.pathname !== '/' || !root) return;

  root.innerHTML = `
    <main class="nv-home">
      <section class="nv-hero">
        <div class="nv-particles" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
        <div class="nv-copy">
          <h1>Welcome to<br>the Future of<br><strong>Autonomous<br>EVs</strong></h1>
        </div>
        <div class="nv-model" aria-label="Interactive 3D Navisights vehicle"><span>Loading vehicle…</span></div>
      </section>
      <section class="nv-stats" aria-label="Vehicle specifications">
        <article><strong>25</strong><b>KM/HR</b><span>Maximum Speed</span></article>
        <article><strong>100</strong><b>KG</b><span>Payload Capacity</span></article>
        <article><strong>250</strong><b>KG</b><span>Total Vehicle Weight</span></article>
      </section>
    </main>`;

  createVehicle(root.querySelector('.nv-model'));
}

function createVehicle(host) {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(32, 1, 0.01, 100);
  camera.position.set(5.6, 3.3, 5.6);
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.setClearColor(0x000000, 0);
  host.append(renderer.domElement);

  scene.add(new THREE.HemisphereLight(0xeaffff, 0x06030c, 2.8));
  const key = new THREE.DirectionalLight(0xffffff, 3.8);
  key.position.set(5, 7, 5);
  scene.add(key);
  const fill = new THREE.DirectionalLight(0x7d64ff, 2.2);
  fill.position.set(-5, 3, -4);
  scene.add(fill);

  const loader = new GLTFLoader();
  loader.load('/navisights-trike/navisights_trike_assy_file.gltf', (gltf) => {
    const vehicle = gltf.scene;
    vehicle.traverse((part) => {
      if (part.isMesh) { part.castShadow = true; part.receiveShadow = true; }
    });
    const bounds = new THREE.Box3().setFromObject(vehicle);
    const center = bounds.getCenter(new THREE.Vector3());
    const longestSide = bounds.getSize(new THREE.Vector3()).length();
    vehicle.position.sub(center);
    vehicle.position.y = -0.8;
    vehicle.scale.setScalar(4.4 / longestSide);
    vehicle.rotation.y = -0.58;
    scene.add(vehicle);
    host.querySelector('span')?.remove();
  }, undefined, () => {
    host.querySelector('span').textContent = 'Vehicle model unavailable.';
  });

  function resize() {
    const width = host.clientWidth;
    const height = host.clientHeight;
    if (!width || !height) return;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  }
  new ResizeObserver(resize).observe(host);
  resize();

  let last = performance.now();
  function render(now) {
    scene.rotation.y += (now - last) * 0.00006;
    last = now;
    renderer.render(scene, camera);
    requestAnimationFrame(render);
  }
  requestAnimationFrame(render);
}

const styles = document.createElement('style');
styles.textContent = `
  html, body, #root { min-height: 100%; margin: 0; background: #000 !important; }
  .nv-home { min-height: 100vh; overflow: hidden; color: #fff; background: #000; font-family: 'Afacad Flux', Arial, sans-serif; }
  .nv-hero { position: relative; display: grid; grid-template-columns: 1fr 1fr; align-items: center; min-height: min(760px, 78vh); padding: 5rem clamp(2rem, 12vw, 14rem); isolation: isolate; }
  .nv-copy { z-index: 1; }
  .nv-copy h1 { margin: 0; font-weight: 300; font-size: clamp(3.8rem, 5.3vw, 6.1rem); line-height: .98; letter-spacing: -.045em; }
  .nv-copy strong { display: inline-block; margin-top: .12em; font-weight: 800; background: linear-gradient(115deg, #7c1d9e 5%, #c12d70 95%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .nv-model { position: relative; width: min(100%, 700px); height: clamp(380px, 60vh, 650px); justify-self: center; }
  .nv-model canvas { width: 100%; height: 100%; display: block; filter: drop-shadow(0 20px 32px rgba(69, 65, 189, .18)); }
  .nv-model > span { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #c892d7; font: 600 .85rem Raleway, sans-serif; letter-spacing: .1em; white-space: nowrap; }
  .nv-particles i { position: absolute; width: 7px; height: 7px; border-radius: 50%; background: #cce6e5; opacity: .62; box-shadow: 0 0 14px #d7ffff; }
  .nv-particles i:nth-child(1) { left: 3%; top: 72%; } .nv-particles i:nth-child(2) { left: 9%; top: 88%; } .nv-particles i:nth-child(3) { left: 41%; top: 77%; } .nv-particles i:nth-child(4) { left: 60%; top: 71%; }
  .nv-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2rem; max-width: 1120px; margin: 0 auto; padding: 3.5rem 2rem 5rem; text-align: center; }
  .nv-stats article { display: grid; justify-items: center; }
  .nv-stats strong { font-size: clamp(4.6rem, 7vw, 7.2rem); font-weight: 300; line-height: .9; background: linear-gradient(115deg, #7e249e, #c52d6c); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .nv-stats b { margin-top: .55rem; font: 500 clamp(1.7rem, 2.2vw, 2.35rem) 'Afacad Flux', sans-serif; }
  .nv-stats span { margin-top: .15rem; font: 400 clamp(1.2rem, 1.7vw, 1.6rem) 'Afacad Flux', sans-serif; }
  @media (max-width: 760px) { .nv-hero { grid-template-columns: 1fr; min-height: auto; padding: 4rem 1.5rem 1rem; } .nv-copy { text-align: center; } .nv-model { height: 410px; width: 100%; } .nv-stats { grid-template-columns: 1fr; gap: 3rem; padding-top: 2rem; } }
`;
document.head.append(styles);

if (location.pathname === '/' && root) {
  const keepHomeMounted = new MutationObserver(() => {
    if (!root.querySelector('.nv-home')) mountHome();
  });
  keepHomeMounted.observe(root, { childList: true });
  setTimeout(mountHome, 0);
}
