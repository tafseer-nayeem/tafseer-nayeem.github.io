---
layout: archive
title: "Education & Awards"
permalink: /education-awards/
author_profile: true
---


<!-- ===== Education & Awards (equal-height awards grid) — DROP-IN ===== -->

<style>
  /* ========= Global knobs (tune here) ========= */
  :root{
    /* Education card geometry */
    --logo-w: 160px;
    --logo-max-h: 110px;
    --card-gap: 18px;

    /* Typography */
    --fs-h2:   1.35rem;   /* section headings */
    --fs-title:1.00rem;   /* education card title */
    --fs-sub:  .92rem;    /* institution line */
    --fs-body: .92rem;    /* meta lines */
    --fs-chip: .74rem;    /* chips */

    /* Chip colors */
    --badge-blue:  #4682B4;
    --badge-teal:  #0F766E;

    /* Award outline palette */
    --gold-ink: #7A5A00;
    --gold-bg:  #FFF8E6;
    --gold-brd: #E7C76A;

    /* Card chrome */
    --card-brd:   #e5e7eb;
    --card-bg:    #fff;
    --card-shadow:0 1px 2px rgba(0,0,0,.04);

    /* Awards grid knobs */
    --aw-grid-gap: 16px;      /* gap between award cards */
    --aw-card-pad: 14px;      /* padding inside award cards */
    --aw-title-fs: .98rem;
    --aw-meta-fs:  .90rem;
    --aw-chip-fs:  .72rem;

    /* Optional award thumbnail lane */
    --aw-thumb-w: 110px;      /* width of image lane */
    --aw-thumb-ratio: 4 / 3;  /* 1/1, 4/3, 16/9 etc. */
    --aw-thumb-brd: #e5e7eb;
  }

  /* ========= Section heading ========= */
  .sec-title{
    margin: 14px 0 8px;
    font-size: var(--fs-h2);
    color:#1f2937; letter-spacing:.2px;
  }
  @media (max-width:640px){
    :root{ --fs-h2:1.15rem; }
  }

  /* ========= Education cards ========= */
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

  .logo-wrap{
    width:var(--logo-w); max-height:var(--logo-max-h);
    display:grid; place-items:center;
    border:1px solid var(--card-brd); border-radius:12px;
    background:#fff; overflow:hidden;
  }
  .logo-wrap img{ max-width:100%; max-height:100%; width:auto; height:auto; }

  .cv-title{ margin:0 0 6px 0; font-size:var(--fs-title); line-height:1.28; }
  .cv-title a{
    text-decoration:none;
    background-image: linear-gradient(currentColor,currentColor);
    background-size:0% 2px; background-repeat:no-repeat; background-position:0 100%;
    transition: background-size .22s ease;
  }
  .cv-title a:hover{ background-size:100% 2px; }

  .cv-sub{ margin:0 0 8px 0; font-size:var(--fs-sub); color:#374151; }
  .meta{
    display:flex; flex-direction:column; gap:4px;
    margin: 0 0 10px 0; font-size:var(--fs-body); color:#374151;
  }
  .meta-row{ display:block; }
  .meta-label{ font-weight:600; color:#374151; margin-right:.35rem; }
  .meta a{ text-decoration:underline; text-underline-offset:2px; }

  .chip{
    display:inline-flex; align-items:center; justify-content:center;
    padding:4px 8px; margin-right:6px; margin-bottom:6px;
    border-radius:999px; line-height:1; white-space:nowrap;
    font-size:var(--fs-chip); font-weight:700; letter-spacing:.2px; text-transform:uppercase;
    border:1px solid #d1d5db; background:#eef2f7; color:#374151;
  }
  .chip-blue{ background:var(--badge-blue); color:#fff; border-color:transparent; }
  .chip-teal{ background:var(--badge-teal); color:#fff; border-color:transparent; }

  /* ========= Awards: equal-height two-column FLEX grid ========= */
  .awards-grid{
    display:flex;
    flex-wrap:wrap;
    gap: var(--aw-grid-gap);
    align-items: stretch;        /* equal height within each row */
  }
  .award-card{
    flex: 1 1 calc(50% - var(--aw-grid-gap));  /* two columns, responsive */
    display:flex; gap:12px;                    /* thumb lane + body */
    padding: var(--aw-card-pad);
    border:1px solid var(--card-brd);
    border-radius:12px;
    background:var(--card-bg);
    box-shadow: var(--card-shadow);
    transition: box-shadow .2s ease, transform .2s ease, border-color .2s ease;
    min-width: 300px;
  }
  .award-card:hover{
    box-shadow: 0 10px 28px rgba(0,0,0,.08);
    transform: translateY(-2px);
    border-color:#e2e8f0;
  }

  /* Optional thumb lane (omit this div if you don’t have an image) */
  .award-thumb{
    flex: 0 0 var(--aw-thumb-w);
    display:grid; place-items:center;
    width: var(--aw-thumb-w);
    aspect-ratio: var(--aw-thumb-ratio);
    border:1px solid var(--aw-thumb-brd);
    border-radius:10px;
    background:#fff; overflow:hidden;
  }
  .award-thumb img{
    max-width:100%; max-height:100%;
    width:auto; height:auto; display:block;   /* no cropping */
  }

  /* Body */
  .award-body{ flex:1 1 auto; display:flex; flex-direction:column; justify-content:center; }

  .award-title{ margin:0 0 6px 0; font-size:var(--aw-title-fs); line-height:1.28; }
  .award-title a{
    text-decoration:none;
    background-image:linear-gradient(currentColor,currentColor);
    background-size:0% 2px; background-repeat:no-repeat; background-position:0 100%;
    transition: background-size .22s ease;
  }
  .award-title a:hover{ background-size:100% 2px; }

  .award-meta{ margin:0 0 8px 0; font-size:var(--aw-meta-fs); color:#374151; }

  .pub-award-line{ margin:2px 0 4px 0; }
  .award-badge{
    display:inline-flex; align-items:center; justify-content:center; gap:6px;
    padding:4px 10px; border-radius:999px; line-height:1.05;
    font-size: var(--aw-chip-fs); font-weight:800; letter-spacing:.2px;
    color:var(--gold-ink); background:var(--gold-bg); border:1px solid var(--gold-brd);
    text-transform:none; white-space:nowrap;
    transition: transform .16s ease, box-shadow .16s ease, filter .16s ease;
  }
  .award-badge:hover{ transform:translateY(-1px); box-shadow:0 6px 14px rgba(0,0,0,.06); filter:saturate(1.03); }

  .award-list{ margin: 6px 0 0 18px; padding:0; }
  .award-list li{ margin:2px 0; }

  /* Mobile */
  @media (max-width: 900px){
    .award-card{ flex-basis: 100%; }
  }
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
      <span class="chip">Ongoing</span>
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
      <span class="chip">completed</span>
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
      <span class="chip">completed</span>
    </div>
  </div>
</div>

<h2 class="sec-title" id="awards">Awards</h2>

<div class="awards-grid">

  <!-- Pair 1: these two will now match in height with the UofL card if placed in same row -->

  <article class="award-card">
    <!-- Omit this block if you have no image -->
    <!-- <div class="award-thumb"><img src="..." alt=""></div> -->
    <div class="award-body">
      <h3 class="award-title">Graduate Recruitment Scholarship</h3>
      <div class="award-meta">University of Alberta · 2021 – 2022</div>
      <div><span class="chip">scholarship</span></div>
    </div>
  </article>

  <article class="award-card">
    <div class="award-body">
      <h3 class="award-title">Graduate awards and scholarships (UofL)</h3>
      <div class="award-meta">School of Graduate Studies (S.G.S) and GSA</div>
      <ul class="award-list">
        <li>Research Dissemination Travel Award (S.G.S)</li>
        <li>Graduate Student’s Association (GSA) Travel Award</li>
        <li>Dean’s Scholarship (S.G.S)</li>
        <li>International Tuition Award (S.G.S)</li>
      </ul>
    </div>
  </article>

  <!-- Pair 2: equal-height with its row partner -->
  <article class="award-card">
    <div class="award-body">
      <h3 class="award-title">IUT-OIC Full Free Scholarship</h3>
      <div><span class="chip">full scholarship</span></div>
    </div>
  </article>

  <article class="award-card">
    <div class="award-body">
      <h3 class="award-title">PhD Early Achievement Award (nomination)</h3>
      <div class="award-meta">2023</div>
      <div><span class="chip">nomination</span></div>
    </div>
  </article>

  <!-- Add more award cards as needed … -->

</div>

<p style="margin-top:14px;"><a href="#">Back to Top</a></p>




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

