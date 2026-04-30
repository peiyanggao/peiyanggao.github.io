---
layout: archive
title: "Photography"
permalink: /photography/
author_profile: true
---

A personal collection of film photographs taken over the years. All shot on 35mm film.

<style>
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 12px;
  margin-top: 30px;
}

.photo-gallery a {
  display: block;
  overflow: hidden;
  border-radius: 4px;
  background: #f5f5f5;
}

.photo-gallery img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  display: block;
  transition: transform 0.3s ease;
}

.photo-gallery a:hover img {
  transform: scale(1.05);
}

/* 灯箱样式 */
.lightbox {
  display: none;
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.9);
  z-index: 9999;
  cursor: pointer;
}

.lightbox.active {
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox img {
  max-width: 90%;
  max-height: 90%;
  object-fit: contain;
}

.lightbox-caption {
  position: absolute;
  bottom: 20px;
  left: 0;
  right: 0;
  text-align: center;
  color: white;
  font-size: 14px;
}
</style>

<div class="photo-gallery">
  <a href="#" data-img="/images/photograph/film-001.jpg" data-caption="Qingdao · 2022">
    <img src="/images/photograph/film-001.jpg" alt="Film photo 1">
  </a>
  <a href="#" data-img="/images/photograph/film-002.jpg" data-caption="Amsterdam, Rijksmuseum · 2023">
    <img src="/images/photograph/film-002.jpg" alt="Film photo 2">
  </a>
  <a href="#" data-img="/images/photograph/film-003.jpg" data-caption="Amsterdam, RAI · 2023 · AAIC">
    <img src="/images/photograph/film-003.jpg" alt="Film photo 3">
  </a>
  <a href="#" data-img="/images/photograph/film-004.jpg" data-caption="Taiwu Town · 2024">
    <img src="/images/photograph/film-004.jpg" alt="Film photo 4">
  </a>
  <a href="#" data-img="/images/photograph/film-005.jpg" data-caption="Toronto · 2025 · AAIC">
    <img src="/images/photograph/film-005.jpg" alt="Film photo 5">
  </a>
  <a href="#" data-img="/images/photograph/film-006.jpg" data-caption="Frankfurt, Airport · 2025">
    <img src="/images/photograph/film-006.jpg" alt="Film photo 6">
  </a>
  
</div>

<div class="lightbox" id="lightbox">
  <img id="lightbox-img" src="" alt="">
  <div class="lightbox-caption" id="lightbox-caption"></div>
</div>

<script>
document.querySelectorAll('.photo-gallery a').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');
    lightboxImg.src = this.getAttribute('data-img');
    lightboxCaption.textContent = this.getAttribute('data-caption');
    lightbox.classList.add('active');
  });
});

document.getElementById('lightbox').addEventListener('click', function() {
  this.classList.remove('active');
});

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    document.getElementById('lightbox').classList.remove('active');
  }
});
</script>
