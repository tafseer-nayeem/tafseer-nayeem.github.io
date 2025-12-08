---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<style>
:root{
  --accent:#1F6CAB;
  --ink:#111827;
  --muted:#374151;
  --rule:#e5e7eb;
  --chip-bg:#eef2f7;
  --chip-ink:#374151;

  --section-gap:22px;
  --para-gap:10px;
}

.home a{
  color:var(--accent); text-decoration:none;
  background-image:linear-gradient(currentColor,currentColor);
  background-size:0% 2px; background-repeat:no-repeat; background-position:0 100%;
  transition:background-size .22s ease;
}
.home a:hover{ background-size:100% 2px; }

.lead{
  margin:var(--para-gap) 0;
  color:var(--muted);
  line-height:1.65;
  font-size:1.03rem;
  text-align:justify;
}

.chip{
  display:inline-flex; align-items:center; justify-content:center;
  padding:4px 10px; border-radius:999px; line-height:1;
  font-size:.78rem; font-weight:800; letter-spacing:.2px;
  border:1px solid #d1d5db; background:var(--chip-bg); color:var(--chip-ink);
}
.chip-accent{ background:var(--accent); color:#fff; border-color:transparent; }

.date-badge{
  display:inline-block; padding:3px 10px; border-radius:999px; line-height:1;
  font-size:.78rem; font-weight:800; letter-spacing:.2px;
  background:var(--chip-bg); color:var(--chip-ink);
  margin-right:10px;
}

.section-title{
  margin:var(--section-gap) 0 8px;
  font-size:1.35rem; color:var(--ink);
  letter-spacing:.2px; line-height:1.25;
  display:flex; align-items:center; gap:10px;
}

.thin-rule{ border:0; height:1px; background:var(--rule); margin:12px 0 12px; }

.news-list{ list-style:none; padding:0; margin:8px 0 0 0; }
.news-list li{ margin:8px 0; color:var(--muted); }

.expand-button{
  background:var(--chip-bg); color:var(--chip-ink);
  border:1px solid #bfc7d1; padding:7px 14px; border-radius:8px;
  font-size:.82rem; font-weight:700; cursor:pointer;
  transition:box-shadow .18s ease;
  margin:8px 0;
}
.expand-button:hover,.expand-button:focus{ box-shadow:0 6px 14px rgba(0,0,0,.10); }

#moreUpdates ul{ list-style:none; padding:0; margin:0; }
#moreUpdates li{ margin:8px 0; color:var(--muted); }

@media (max-width:640px){
  .section-title{ font-size:1.28rem; }
  .lead{ font-size:1.02rem; }
}
</style>

<div class="home">

<p class="lead">
I’m Mir <b>Tafseer</b> Nayeem, a PhD candidate in <a href="https://www.ualberta.ca/computing-science/index.html">Computing Science</a> at the <a href="https://www.ualberta.ca/index.html">University of Alberta</a>, advised by <a href="https://webdocs.cs.ualberta.ca/~drafiei/">Prof. Davood Rafiei</a>. My research centers on user-centric language modeling. I study how user attributes—age, dialect, intent, and preferences—can be incorporated into large language models and downstream synthesis tasks (e.g., summarization, opinion generation) to build inclusive, adaptive, and context-aware NLP systems.
</p>

<p class="lead">
Support: <span class="chip chip-accent">Huawei PhD Fellowship</span>.
Recognition: <span class="chip">Best Resource Paper (EMNLP 2024)</span>
<span class="chip">Area Chair Favorite (COLING 2018)</span>
<span class="chip">Best Short Paper (VIS 2025)</span>.
</p>

<p class="lead" style="margin-top:6px;">
See my <a href="https://tafseer-nayeem.github.io/cv/">CV</a> and <a href="https://tafseer-nayeem.github.io/publications/">publications</a>.
</p>

<h2 class="section-title">Announcements</h2>
<hr class="thin-rule"/>

<ul class="news-list">
  <li><span class="date-badge">Sep 2025</span> 🏆 <a href="https://arxiv.org/abs/2508.09716">ChartDeception</a> received the <b>Best Short Paper Award</b> at <a href="https://ieeevis.org/year/2025/info/program/papers_list">VIS 2025</a>.</li>
  <li><span class="date-badge">Aug 2025</span> 📌 Three papers accepted at <a href="https://2025.emnlp.org/">EMNLP 2025</a>.</li>
  <li><span class="date-badge">Jul 2025</span> 📌 One paper accepted at <a href="https://colmweb.org/">COLM 2025</a>.</li>
  <li><span class="date-badge">Jun 2025</span> 📌 One paper accepted at <a href="https://ieeevis.org/year/2025/welcome">VIS 2025</a>.</li>
  <li><span class="date-badge">May 2025</span> 🧑‍⚖️ Serving as an <b>Area Chair (AC)</b> for <a href="https://2025.emnlp.org/">EMNLP 2025</a>.</li>
  <li><span class="date-badge">May 2025</span> 📌 One paper accepted at <a href="https://2025.aclweb.org/">ACL 2025</a> (Industry Track).</li>
  <li><span class="date-badge">Mar 2025</span> 🧑‍⚖️ Serving as an <b>Area Chair (AC)</b> for <a href="https://2025.aclweb.org/">ACL 2025</a>.</li>
  <li><span class="date-badge">Feb 2025</span> 📌 One paper accepted at <a href="https://2025.naacl.org/">NAACL 2025</a> (Industry Track).</li>
  <li><span class="date-badge">Nov 2024</span> 🏆 <a href="https://aclanthology.org/2024.emnlp-main.277/">KidLM</a> received the <b>Best Resource Paper Award</b> at <a href="https://2024.emnlp.org/">EMNLP 2024</a>.</li>
  <li><span class="date-badge">Sep 2024</span> 📌 Two papers accepted at <a href="https://2024.emnlp.org/">EMNLP 2024</a>.</li>
  <li><span class="date-badge">May 2024</span> 📌 One paper accepted at <a href="https://2024.aclweb.org/">ACL 2024</a>.</li>
</ul>

<button onclick="toggleVisibility('moreUpdates')" class="expand-button">View More News</button>

<div id="moreUpdates" style="display:none;">
  <ul>
    <li><span class="date-badge">Feb 2024</span> 📌 One paper accepted at <a href="https://lrec-coling-2024.org/">LREC-COLING 2024</a>.</li>
    <li><span class="date-badge">Aug 2023</span> 📌 One paper accepted at <a href="https://uobevents.eventsair.com/cikm2023/">CIKM 2023</a>.</li>
    <li><span class="date-badge">Jan 2023</span> 📌 Two papers accepted at <a href="https://2023.eacl.org/">EACL 2023</a>.</li>
    <li><span class="date-badge">Jun 2022</span> 🏅 Awarded the <b>Huawei PhD Fellowship</b>.</li>
    <li><span class="date-badge">Sep 2021</span> 🎓 Started PhD in <a href="https://www.ualberta.ca/computing-science/index.html">Computing Science</a>, University of Alberta.</li>
    <li><span class="date-badge">Feb 2021</span> 📌 One paper accepted at <a href="https://2021.eacl.org/">EACL 2021</a>.</li>
    <li><span class="date-badge">Jan 2021</span> 📌 One paper accepted at <a href="https://aaai.org/Conferences/AAAI-21/">AAAI 2021</a>.</li>
    <li><span class="date-badge">Jun 2018</span> 🏆 <a href="http://aclweb.org/anthology/C18-1102">Paper</a> received <b>Area Chair Favorite Paper Award</b> at <a href="http://coling2018.org/coling-2018-best-papers/">COLING 2018</a>.</li>
  </ul>
</div>

<hr class="thin-rule"/>
<p style="margin-top:12px;"><a href="#">Back to Top</a></p>

</div>

<script>
function toggleVisibility(id){
  var el=document.getElementById(id);
  el.style.display=(el.style.display==="none"||!el.style.display)?"block":"none";
}
</script>
