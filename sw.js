// Service Worker · Química · Gorka
// v6 — añadidos T1 (autoeval 4.2) y 3 más en T8 (autoeval T8).
const CACHE = 'quimica-gorka-v6';
const ASSETS = [
  './',
  './index.html',
  './formulario.html',
  './shared/quimica.css',
  './manifest.json',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).catch(() => {}));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  // Network-first SIEMPRE para HTML — fuerza siempre la versión más nueva.
  if (e.request.mode === 'navigate' || url.pathname.endsWith('.html')) {
    e.respondWith(
      fetch(e.request, { cache: 'no-store' })
        .then((r) => {
          const copy = r.clone();
          caches.open(CACHE).then((c) => c.put(e.request, copy));
          return r;
        })
        .catch(() => caches.match(e.request).then((m) => m || caches.match('./index.html')))
    );
  } else {
    // Cache-first para CSS/JS/imágenes (estables).
    e.respondWith(
      caches.match(e.request).then((m) => m || fetch(e.request))
    );
  }
});
