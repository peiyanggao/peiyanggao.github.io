---
layout: single
title: "Conferences"
permalink: /conferences/
author_profile: true
---

International and domestic conferences I have attended as an oral or poster presenter.

<style>
.conf-section-title {
  font-size: 1.4em;
  font-weight: 700;
  color: #1a1a1a;
  margin-top: 2em;
  margin-bottom: 1em;
  padding-bottom: 0.4em;
  border-bottom: 2px solid #2a7ae2;
}

.conf-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.conf-card {
  background: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 6px;
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  cursor: pointer;
}

.conf-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.conf-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}

.conf-card-body {
  padding: 12px 14px;
}

.conf-card-meta {
  font-size: 0.95em;
  color: #2a2a2a;
  font-weight: 600;
  line-height: 1.4;
}

/* 灯箱 */
.conf-lightbox {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.92);
  z-index: 9999;
  cursor: pointer;
}

.conf-lightbox.active {
  display: flex;
  align-items: center;
  justify-content: center;
}

.conf-lightbox img {
  max-width: 92%;
  max-height: 88%;
  object-fit: contain;
}

.conf-lightbox-caption {
  position: absolute;
  bottom: 24px;
  left: 0;
  right: 0;
  text-align: center;
  color: white;
  font-size: 15px;
  font-weight: 500;
}
</style>

<div class="conf-section-title">Oral Presentations</div>

<div class="conf-grid">

  <div class="conf-card" data-img="/images/conferences/oral/aaic-2025-oral.jpg" data-caption="AAIC 2025 · Toronto · Jul 2025">
    <img src="/images/conferences/oral/aaic-2025-oral.jpg" alt="AAIC 2025">
    <div class="conf-card-body">
      <div class="conf-card-meta">AAIC 2025<br>Toronto · Jul 2025</div>
    </div>
  </div>
  
  <div class="conf-card" data-img="/images/conferences/oral/aaic-2024-oral.jpg" data-caption="AAIC 2024 · Philadelphia · Jul 2024">
    <img src="/images/conferences/oral/aaic-2024-oral.jpg" alt="AAIC 2024">
    <div class="conf-card-body">
      <div class="conf-card-meta">AAIC 2024<br>Philadelphia · Jul 2025</div>
    </div>
  </div>

  <div class="conf-card" data-img="/images/conferences/oral/JSN-2025-oral.jpg" data-caption="JSN 66th Annual Meeting · Osaka · May 2025">
    <img src="/images/conferences/oral/JSN-2025-oral.jpg" alt="JSN 2025">
    <div class="conf-card-body">
      <div class="conf-card-meta">JSN 66th Annual Meeting<br>Osaka · May 2025</div>
    </div>
  </div>

  <div class="conf-card" data-img="/images/conferences/oral/ctad-2025-oral.jpg" data-caption="China CTAD Advandced Workshop · Shanghai · 2025">
    <img src="/images/conferences/oral/ctad-2025-oral.jpg" alt="CTAD 2025">
    <div class="conf-card-body">
      <div class="conf-card-meta">China CTAD Advandced Workshop<br>Shanghai · Sept 2025</div>
    </div>
  </div>
  
  <div class="conf-card" data-img="/images/conferences/oral/Changsha-2025-oral.jpg" data-caption="The 11th Academic Conference on Dementia and Cognitive Impairment of the Neurology Branch of the Chinese Medical Association · Changsha · 2025">
    <img src="/images/conferences/oral/Changsha-2025-oral.jpg" alt="Dementia 2025">
    <div class="conf-card-body">
      <div class="conf-card-meta">The 11th Academic Conference on Dementia and Cognitive Impairment of the Neurology Branch of the Chinese Medical Association<br>Changsha · Nov 2025</div>
    </div>
  </div>

</div>

<div class="conf-section-title">Poster Presentations</div>

<div class="conf-grid">

  <div class="conf-card" data-img="/images/conferences/poster/aan-2025-poster.jpg" data-caption="AAN 2025 · San Diego · Apr 2025">
    <img src="/images/conferences/poster/aan-2025-poster.jpg" alt="AAN 2025 poster">
    <div class="conf-card-body">
      <div class="conf-card-meta">AAN 2025<br>San Diego · Apr 2025</div>
    </div>
  </div>

  <div class="conf-card" data-img="/images/conferences/poster/aaic-2024-poster1.jpg" data-caption="AAIC 2024 · Philadelphia · Jul 2024">
    <img src="/images/conferences/poster/aaic-2024-poster1.jpg" alt="AAIC 2024 poster 1">
    <div class="conf-card-body">
      <div class="conf-card-meta">AAIC 2024<br>Philadelphia · Jul 2024</div>
    </div>
  </div>

  <div class="conf-card" data-img="/images/conferences/poster/aaic-2024-poster2.jpg" data-caption="AAIC 2024 · Philadelphia · Jul 2024">
    <img src="/images/conferences/poster/aaic-2024-poster2.jpg" alt="AAIC 2024 poster 2">
    <div class="conf-card-body">
      <div class="conf-card-meta">AAIC 2024<br>Philadelphia · Jul 2024</div>
    </div>
  </div>

  <div class="conf-card" data-img="/images/conferences/poster/aaic-2023-poster.jpg" data-caption="AAIC 2023 · Amsterdam · Jul 2023">
    <img src="/images/conferences/poster/aaic-2023-poster.jpg" alt="AAIC 2023 poster">
    <div class="conf-card-body">
      <div class="conf-card-meta">AAIC 2023<br>Amsterdam · Jul 2023</div>
    </div>
  </div>

</div>

<div class="conf-lightbox" id="conf-lightbox">
  <img id="conf-lightbox-img" src="" alt="">
  <div class="conf-lightbox-caption" id="conf-lightbox-caption"></div>
</div>

<script>
document.querySelectorAll('.conf-card').forEach(card => {
  card.addEventListener('click', function() {
    const lightbox = document.getElementById('conf-lightbox');
    const lightboxImg = document.getElementById('conf-lightbox-img');
    const lightboxCaption = document.getElementById('conf-lightbox-caption');
    lightboxImg.src = this.getAttribute('data-img');
    lightboxCaption.textContent = this.getAttribute('data-caption');
    lightbox.classList.add('active');
  });
});

document.getElementById('conf-lightbox').addEventListener('click', function() {
  this.classList.remove('active');
});

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    document.getElementById('conf-lightbox').classList.remove('active');
  }
});
</script>
