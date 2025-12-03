---
layout: archive
title: "Education & Awards"
permalink: /education-awards/
author_profile: true
---

<!-- ===== Education & Awards ===== -->

<style>
  /* ========= Global knobs you can tune once ========= */
  :root{
    /* Card geometry */
    --logo-w: 160px;        /* left column width for logos */
    --logo-max-h: 110px;    /* max visible logo height */
    --card-gap: 18px;

    /* Typography */
    --fs-h2:   1.20rem;     /* section headings */
    --fs-title:1.00rem;     /* card title */
    --fs-sub:  .92rem;      /* institution line */
    --fs-body: .92rem;      /* meta lines */
    --fs-chip: .74rem;      /* degree/status chips */

    /* Badges / chips */
    --badge-blue:  #4682B4;
    --badge-teal:  #0F766E;
    --badge-gray:  #6B7280;

    /* Award outline palette */
    --gold-ink: #7A5A00;
    --gold-bg:  #FFF8E6;
    --gold-brd: #E7C76A;

    /* Card chrome */
    --card-brd:   #e5e7eb;
    --card-bg:    #fff;
    --card-shadow:0 1px 2px rgba(0,0,0,.04);
  }

  /* ========= Section headings ========= */
  .sec-title{
    margin: 14px 0 8px;
    font-size: var(--fs-h2);
    color:#1f2937; letter-spacing:.2px;
  }

  /* ========= Reusable card ========= */
  .cv-card{
    display:grid; grid-template-columns: var(--logo-w) 1fr;
    gap: var(--card-gap);
    align-items:start;
    padding:16px 18px; margin:18px 0;
    border:1px solid var(--card-brd); border-radius:12px;
    background:var(--card-bg); box-shadow:var(--card-shadow);
    transition: box-shadow .22s ease, transform .22s ease, border-color .22s ease;
  }
  .cv-card:hover{ box-shadow:0 10px 28px rgba(0,0,0,.08); transform:translateY(-2px); border-color:#e2e8f0; }

  /* Left column: adaptive logo (no cropping) */
  .logo-wrap{
    width:var(--logo-w); max-height:var(--logo-max-h);
    display:grid; place-items:center;
    border:1px solid var(--card-brd); border-radius:12px;
    background:#fff; overflow:hidden;
  }
  .logo-wrap img{ max-width:100%; max-height:100%; width:auto; height:auto; }

  /* Right column: text */
  .cv-title{ margin:0 0 6px 0; font-size:var(--fs-title); line-height:1.28; }
  .cv-title a{
    text-decoration:none;
    background-image: linear-gradient(currentColor,currentColor);
    background-size:0% 2px; background-repeat:no-repeat; background-position:0 100%;
    transition: background-size .22s ease;
  }
  .cv-title a:hover{ background-size:100% 2px; }

  .cv-sub{ margin:0 0 8px 0; font-size:var(--fs-sub); color:#374151; }

  /* Meta rows (each item on its own line) */
  .meta{
    display:flex; flex-direction:column; gap:4px;
    margin: 0 0 10px 0; font-size:var(--fs-body); color:#374151;
  }
  .meta-row{ display:block; }
  .meta-label{
    font-weight:600; color:#374151; margin-right:.35rem;
  }
  .meta a{ text-decoration:underline; text-underline-offset:2px; }

  /* Chips */
  .chip{
    display:inline-flex; align-items:center; justify-content:center;
    padding:4px 8px; margin-right:6px; margin-bottom:6px;
    border-radius:999px; line-height:1; white-space:nowrap;
    font-size:var(--fs-chip); font-weight:700; letter-spacing:.2px; text-transform:uppercase;
    border:1px solid transparent; background:#f3f4f6; color:#111827;
  }
  .chip-blue{ background:var(--badge-blue); color:#fff; }
  .chip-teal{ background:var(--badge-teal); color:#fff; }
  .chip-gray{ background:#eef2f7; color:#374151; border-color:#d1d5db; }

  /* Award badge line */
  .pub-award-line{ display:block; margin:6px 0 8px; }
  .award-badge{
    display:inline-flex; align-items:center; gap:6px; justify-content:center;
    padding:4px 10px; border-radius:999px; line-height:1.05;
    font-weight:800; letter-spacing:.2px; text-transform:none;
    font-size: calc(var(--fs-chip) + .02rem);
    border:1px solid transparent; white-space:nowrap;
    transition: transform .16s ease, box-shadow .16s ease, filter .16s ease;
  }
  .award-outline-gold{ color:var(--gold-ink); background:var(--gold-bg); border-color:var(--gold-brd); }
  .award-badge:hover{ transform:translateY(-1px); box-shadow:0 6px 14px rgba(0,0,0,.06); filter:saturate(1.03); }

  /* Compact list inside a card (for grouped awards) */
  .cv-list{ margin:0 0 6px 18px; padding:0; }
  .cv-list li{ margin:2px 0; }

  /* Mobile */
  @media (max-width: 640px){
    .cv-card{ grid-template-columns:1fr; }
    .logo-wrap{ width:100%; max-height:180px; }
  }
</style>

<h2 class="sec-title" id="education">Education</h2>


<!-- PhD -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/edu/uofa.png"
         alt="University of Alberta logo" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">
      <a href="https://www.ualberta.ca/index.html">PhD in Computing Science</a>
    </h3>
    <div class="cv-sub">University of Alberta (UofA), Edmonton, Canada</div>
    <div class="meta">
      <span class="meta-row">
        <span class="meta-label">Tentative thesis title:</span>
        “User-Centric Modeling and Synthesis in Language Technologies”
      </span>
      <span class="meta-row">
        <span class="meta-label">Supervisor:</span>
        <a href="https://webdocs.cs.ualberta.ca/~drafiei/">Prof. Davood Rafiei</a>
      </span>
      <span class="meta-row">
        <span class="meta-label">Committee:</span>
        <a href="https://webdocs.cs.ualberta.ca/~zaiane/">Prof. Osmar Zaiane</a>,
        <a href="https://lili-mou.github.io/">Prof. Lili Mou</a>
      </span>
    </div>
    <div>
      <span class="chip chip-blue">PhD</span>
      <span class="chip chip-teal">Huawei PhD Fellowship</span>
      <span class="chip chip-gray">Ongoing</span>
    </div>
  </div>
</div>

<!-- MSc -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/edu/uofl.png"
         alt="University of Lethbridge logo" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">
      <a href="https://www.uleth.ca/">MSc in Computer Science</a>
    </h3>
    <div class="cv-sub">University of Lethbridge (UofL), Lethbridge, Canada</div>
    <div class="meta">
      <span class="meta-row">
        <span class="meta-label">Thesis:</span>
        <a href="https://tafseer-nayeem.github.io/files/MSc_Thesis.pdf">
          Methods of Sentence Extraction, Abstraction, and Ordering for Automatic Text Summarization
        </a>
      </span>
      <span class="meta-row">
        <span class="meta-label">Presentation:</span>
        <a href="https://tafseer-nayeem.github.io/files/MSc_Thesis_Presenation.pdf">slides</a>
      </span>
      <span class="meta-row">
        <span class="meta-label">Supervisor:</span>
        <a href="http://www.cs.uleth.ca/~chali/">Prof. Yllias Chali</a>
      </span>
      <span class="meta-row">
        <span class="meta-label">Committee:</span>
        <a href="http://directory.uleth.ca/users/wendy.osborn">Prof. Wendy Osborn</a>,
        <a href="http://directory.uleth.ca/users/john.anvik">Prof. John Anvik</a>
      </span>
    </div>
    <div>
      <span class="chip chip-blue">MSc</span>
      <span class="chip chip-gray">completed</span>
    </div>
  </div>
</div>

<!-- BSc -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/edu/iut.png"
         alt="Islamic University of Technology logo" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">
      <a href="https://www.iutoic-dhaka.edu/">BSc in Computer Science and Information Technology</a>
    </h3>
    <div class="cv-sub">Islamic University of Technology (IUT), Dhaka, Bangladesh</div>
    <div class="meta">
      <span class="meta-row">
        <span class="meta-label">Thesis:</span>
        Designing a Probabilistic Path Selection Model for Vehicular Networks
      </span>
      <span class="meta-row">
        <span class="meta-label">Supervisor:</span>
        <a href="https://scholar.google.com/citations?user=5sjCt8cAAAAJ&hl=en">Prof. Muhammad Mahbub Alam</a>
      </span>
    </div>
    <div>
      <span class="chip chip-blue">BSc</span>
      <span class="chip chip-gray">completed</span>
    </div>
  </div>
</div>

<h2 class="sec-title" id="awards">Awards</h2>

<!-- VIS 2025 Best Short Paper -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/awards/vis.png"
         alt="IEEE VIS icon" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">
      <a href="https://ieeevis.org/year/2025/info/program/papers_list">Best Short Paper Award</a>
    </h3>
    <div class="cv-sub">VIS 2025</div>
    <div class="pub-award-line">
      <a href="https://ieeevis.org/year/2025/info/awards/best-paper-awards" target="_blank" rel="noopener noreferrer">
        <span class="award-badge award-outline-gold">🏆 Best short paper award</span>
      </a>
    </div>
  </div>
</div>

<!-- EMNLP 2024 Best Resource Paper -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/awards/emnlp.png"
         alt="EMNLP icon" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">
      <a href="https://2024.emnlp.org/program/best_papers/">Best Resource Paper Award</a>
    </h3>
    <div class="cv-sub">EMNLP 2024</div>
    <div class="pub-award-line">
      <a href="https://2024.emnlp.org/program/best_papers/" target="_blank" rel="noopener noreferrer">
        <span class="award-badge award-outline-gold">🏆 Best resource paper award</span>
      </a>
    </div>
  </div>
</div>

<!-- Huawei Fellowship -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/awards/huawei.png"
         alt="Huawei Fellowship icon" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">Huawei PhD Fellowship</h3>
    <div class="cv-sub">2022 – 2027</div>
    <div>
      <span class="chip chip-teal">fellowship</span>
      <span class="chip chip-gray">multi-year</span>
    </div>
  </div>
</div>

<!-- PhD Early Achievement nomination -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/awards/uofa.png"
         alt="UofA icon" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">PhD Early Achievement Award (nomination)</h3>
    <div class="cv-sub">2023</div>
    <div><span class="chip chip-gray">nomination</span></div>
  </div>
</div>

<!-- UofA Graduate Recruitment Scholarship -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/awards/uofa.png"
         alt="UofA icon" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">Graduate Recruitment Scholarship</h3>
    <div class="cv-sub">University of Alberta · 2021 – 2022</div>
    <div><span class="chip chip-gray">scholarship</span></div>
  </div>
</div>

<!-- COLING 2018 Area Chair Favorite -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/awards/coling.png"
         alt="COLING icon" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">
      <a href="http://coling2018.org/coling-2018-best-papers/">Area Chair Favorite Paper Award</a>
    </h3>
    <div class="cv-sub">COLING 2018</div>
    <div class="pub-award-line">
      <a href="http://coling2018.org/coling-2018-best-papers/" target="_blank" rel="noopener noreferrer">
        <span class="award-badge award-outline-gold">🏆 Area chair favorite paper award</span>
      </a>
    </div>
  </div>
</div>

<!-- SIGIR Student Travel Grant -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/awards/sigir.png"
         alt="SIGIR icon" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">
      <a href="https://sigir.org/general-information/travel-grants/">ACM SIGIR Student Travel Grant</a>
    </h3>
    <div class="cv-sub"></div>
    <div><span class="chip chip-gray">travel grant</span></div>
  </div>
</div>

<!-- SGS/GSA grouped items -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/awards/sgs.png"
         alt="SGS/GSA icon" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">Graduate awards and scholarships (UofL)</h3>
    <div class="cv-sub">School of Graduate Studies (S.G.S) and GSA</div>
    <ul class="cv-list">
      <li>Research Dissemination Travel Award (S.G.S)</li>
      <li>Graduate Student’s Association (GSA) Travel Award</li>
      <li>Dean’s Scholarship (S.G.S)</li>
      <li>International Tuition Award (S.G.S)</li>
    </ul>
  </div>
</div>

<!-- IUT-OIC full scholarship -->
<div class="cv-card">
  <div class="logo-wrap">
    <img src="https://tafseer-nayeem.github.io/images/awards/iut.png"
         alt="IUT-OIC icon" loading="lazy" decoding="async">
  </div>
  <div>
    <h3 class="cv-title">IUT-OIC Full Free Scholarship</h3>
    <div class="cv-sub"></div>
    <div><span class="chip chip-gray">full scholarship</span></div>
  </div>
</div>

<p style="margin-top:16px;"><a href="#">Back to Top</a></p>


---------------------------------------------


# Education

## 🎓 PhD in Computing Science
---------------------------------
* [University of Alberta (UofA)](https://www.ualberta.ca/index.html), Edmonton, Canada.
* **Tentative Thesis Title:** *"User-Centric Modeling and Synthesis in Language Technologies"*
* **Supervisor:** [Prof. Davood Rafiei](https://webdocs.cs.ualberta.ca/~drafiei/)
* **Committee Members:** [Prof. Osmar Zaiane](https://webdocs.cs.ualberta.ca/~zaiane/) and [Prof. Lili Mou ](https://lili-mou.github.io/)


## 🎓 MSc in Computer Science
--------------------------------

* [University of Lethbridge (UofL)](https://www.uleth.ca/), Lethbridge, Canada.
<!-- **CGPA:  4.00** <span style ="color:Green"> [*out of 4.00* ] </span>-->
* **Thesis Title:** [*"Methods of Sentence Extraction, Abstraction, and Ordering for Automatic Text Summarization"*](https://tafseer-nayeem.github.io/files/MSc_Thesis.pdf) 
* **Thesis Presentation:** [<span style ="color:Green"> [**Presentation**] </span>](https://tafseer-nayeem.github.io/files/MSc_Thesis_Presenation.pdf) 
* **Supervisor:** [Prof. Yllias Chali](http://www.cs.uleth.ca/~chali/)
* **Committee Members:** [Prof. Wendy Osborn](http://directory.uleth.ca/users/wendy.osborn) and [Prof. John Anvik ](http://directory.uleth.ca/users/john.anvik)


## 🎓 BSc in Computer Science and Information Technology
-----------------------------------------------------------


* [Islamic University of Technology (IUT)](https://www.iutoic-dhaka.edu/), Dhaka, Bangladesh.
<!-- **CGPA:  3.92** <span style ="color:Green"> [*out of 4.00* ] </span>-->
* **Thesis title:** *"Designing a Probabilistic Path Selection Model for Vehicular Networks"*
<!-- * **Thesis Presentation:** [<span style ="color:Green"> [**Presentation**] </span>](https://tafseer-nayeem.github.io/files/BSc_Thesis_Presentation.pdf) -->
* **Supervisor:** [Dr. Muhammad Mahbub Alam](https://scholar.google.com/citations?user=5sjCt8cAAAAJ&hl=en), Professor, CSE Department.


<!-- <a href="https://tafseer-nayeem.github.io/education-awards/"> <img src="https://tafseer-nayeem.github.io/images/educations.png" alt="Education"
	title="Education" width="500" height="50"> </a>
-->
------------------------------------------------------
------------------------------------------------------

# Awards
---------
* [<span style="color:Red"> **Best Short Paper Award** </span>](https://ieeevis.org/year/2025/info/program/papers_list) at **VIS 2025**.
* [<span style="color:Red"> **Best Resource Paper Award** </span>](https://2024.emnlp.org/program/best_papers/) at **EMNLP 2024**.
* <span style="color:Red"> **Huawei PhD Fellowship** </span> [2022 - 2027].
* Nominated for **PhD Early Achievement Award** [2023].
* University of Alberta Graduate Recruitment Scholarship [2021 - 2022].
<!-- * [<span style="color:Red"> **Best Paper Nomination** </span>](http://coling2018.org/coling-2018-best-papers/) at **COLING 2018**. -->
* [<span style="color:Red"> **Area Chair Favorite Paper Award** </span>](http://coling2018.org/coling-2018-best-papers/) paper at **COLING 2018**.
* **ACM SIGIR** Student Travel Grant.
* School of Graduate Studies (**S.G.S**) Research Dissemination Travel Award.
* Graduate Student’s Association (**GSA**) Travel Award.
* School of Graduate Studies (**S.G.S**) Dean’s Scholarship, UofL.
* School of Graduate Studies (**S.G.S**) International Tuition Award, UofL.
* **IUT-OIC** Full Free Scholarship

<!-- 
<a href="https://tafseer-nayeem.github.io/education-awards/"> <img src="https://tafseer-nayeem.github.io/images/awards.png" alt="Awards"
	title="Awards" width="550" height="30"> </a>
-->
--------------------------------------------

[**Back to Top**](#)

