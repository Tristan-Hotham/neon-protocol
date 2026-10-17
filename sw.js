const SHELL = 'np-shell-v8', MUSIC = 'np-music-v1';
self.addEventListener('install', e => { e.waitUntil(caches.open(SHELL).then(c => c.addAll(['./', 'index.html', 'manifest.webmanifest', 'icon.svg', 'music/index.json']))); self.skipWaiting(); });
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('fetch', e => {
  const r = e.request; if (r.method !== 'GET') return;
  const url = new URL(r.url); if (url.origin !== location.origin) return;
  if (url.pathname.endsWith('.ogg')) {
    if (r.headers.has('range')) return;                                  // let the browser stream ranges itself
    e.respondWith(caches.open(MUSIC).then(c => c.match(r).then(hit => hit || fetch(r).then(res => { if (res.status === 200) c.put(r, res.clone()); return res; }))));
    return;
  }
  e.respondWith(fetch(r).then(res => { if (res.status === 200) caches.open(SHELL).then(c => c.put(r, res.clone())); return res; }).catch(() => caches.match(r)));
});