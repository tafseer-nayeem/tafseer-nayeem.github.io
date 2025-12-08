---
layout: archive
title: "Activities"
permalink: /activities/
author_profile: true
---

<style>
/* ===== Activities page typography and accents ===== */
:root{
  --accent:#1F6CAB;     /* links and accent */
  --ink:#111827;        /* main headings */
  --muted:#374151;      /* body text */
  --rule:#e5e7eb;       /* thin separators */
  --chip-bg:#eef2f7;    /* badges background */
  --chip-ink:#374151;   /* badges text */
}

/* Section titles */
.section-title{
  margin: 26px 0 10px;
  font-size: 1.40rem;           /* larger a bit*/
  color: var(--ink);
  letter-spacing: .2px;
  line-height: 1.25;
  display:flex; align-items:center; gap:10px;
}

/* Subheads (Area Chair, Reviewer, etc.) */
.subhead{
  margin: 18px 0 8px;
  font-size: 1.18rem;
  color: var(--ink);
  display:flex; align-items:center; gap:8px;
}

/* Small circular icon badge, consistent with your chips */
.i{
  display:inline-grid; place-items:center;
  width:26px; height:26px; border-radius:999px;
  background:var(--chip-bg); color:var(--chip-ink);
  font-size:.9rem; line-height:1;
}

/* Thin horizontal rule to separate major groups */
.thin-rule{ border:0; height:1px; background:var(--rule); margin: 12px 0 14px; }

/* Link style consistent with publication page */
.activities a{
  color: var(--accent); text-decoration:none;
  background-image:linear-gradient(currentColor,currentColor);
  background-size:0% 2px; background-repeat:no-repeat; background-position:0 100%;
  transition: background-size .22s ease;
}
.activities a:hover{ background-size:100% 2px; }

/* Year → items layout with clearer scale */
.year-list{ list-style:none; padding:0; margin: 2px 0 8px 0; }
.year-list li{
  display:grid; grid-template-columns: 56px 1fr; gap: 6px;
  padding: 1px 0;
}
.year{ color: var(--muted); font-weight:700; font-size:1.1rem; }  /* bigger year */
.items{ color: var(--muted); font-size:1.02rem; line-height:1.35; }

/* Great reviews badge and generic chips */
.chip{
  display:inline-flex; align-items:center; justify-content:center;
  padding:4px 10px; border-radius:999px; line-height:1;
  font-size:.78rem; font-weight:800; letter-spacing:.2px; text-transform:uppercase;
  border:1px solid #d1d5db; background:var(--chip-bg); color:var(--chip-ink);
}
.chip-accent{ background:var(--accent); color:#fff; border-color:transparent; }

/* Lists without heavy bullets */
.clean-list{ margin: 8px 0 0 1.15rem; }
.clean-list li{ margin: 6px 0; color: var(--muted); }

/* Talk list lines with a date badge */
.talk-list{ list-style:none; padding:0; margin:6px 0 0 0; }
.talk-list li{ margin:10px 0; color:var(--muted); }
.date-badge{
  display:inline-block; padding:3px 10px; border-radius:999px; line-height:1;
  font-size:.78rem; font-weight:800; letter-spacing:.2px; background:var(--chip-bg); color:var(--chip-ink);
  margin-right:10px;
}

/* Mobile tweaks */
@media (max-width:600px){
  .year-list li{ grid-template-columns: 70px 1fr; gap:12px; }
  .section-title{ font-size:1.45rem; }
  .subhead{ font-size:1.10rem; }
}
</style>

<div class="activities">

<h2 class="section-title"><span class="i">🧑‍💼</span> Professional Services</h2>
<hr class="thin-rule"/>

<h3 class="subhead"><span class="i">🧑‍⚖️</span> Area Chair (AC)</h3>
<ul class="year-list">
  <li>
    <span class="year">2026</span>
    <span class="items">
      <a href="https://2026.aclweb.org/">ACL</a>,
      <a href="https://2026.eacl.org/">EACL</a>,
      <a href="https://aclrollingreview.org/">ARR</a>
    </span>
  </li>
  <li>
    <span class="year">2025</span>
    <span class="items">
      <a href="https://2025.aclweb.org/">ACL</a>,
      <a href="https://2025.emnlp.org/">EMNLP</a>,
      <a href="https://aclrollingreview.org/">ARR</a>
    </span>
  </li>
</ul>

<h3 class="subhead"><span class="i">📝</span> Reviewer</h3>
<ul class="year-list">
  <li>
    <span class="year">2025</span>
    <span class="items">
      <a href="https://2025.naacl.org/">NAACL</a>
    </span>
  </li>
  <li>
    <span class="year">2024</span>
    <span class="items">
      <a href="https://2024.aclweb.org/">ACL</a>,
      <a href="https://2024.emnlp.org/">EMNLP</a>,
      <a href="https://2024.naacl.org/">NAACL</a>,
      <a href="https://2024.eacl.org/">EACL</a>,
      <a href="https://sigir-2024.github.io/">SIGIR</a>,
      <a href="https://www.wsdm-conference.org/2024/">WSDM</a>
    </span>
  </li>
  <li>
    <span class="year">2023</span>
    <span class="items">
      <a href="https://sigir.org/sigir2023/">SIGIR</a>,
      <a href="https://kdd.org/kdd2023/">KDD</a>,
      <a href="https://www.wsdm-conference.org/2023/">WSDM</a>,
      <a href="https://uobevents.eventsair.com/cikm2023/">CIKM</a>
    </span>
  </li>
  <li>
    <span class="year">2022</span>
    <span class="items">
      <a href="https://sigir.org/sigir2022/">SIGIR</a>,
      <a href="https://kdd.org/kdd2022/">KDD</a>,
      <a href="https://www.cikm2022.org/">CIKM</a>,
      <a href="https://icde2022.ieeecomputer.my/">ICDE</a>
    </span>
  </li>
</ul>

<!-- - **2020:** [ICCIT](https://iccit.org.bd/2020/) -->
<!-- - **2019:** [ICIET](http://www.enggtech.du.ac.bd/iciet-2019/) -->

<h4 class="subhead"><span class="i">🏅</span> Outstanding Reviews</h4>
<p class="items" style="margin:6px 0 8px 0;">
  High-quality reviews recognized by *ACL venues as
  <span class="chip chip-accent">Great Reviews</span>
</p>
<ul class="clean-list">
  <li>1/3 reviews recognized at <a href="https://2025.naacl.org/">NAACL 2025</a></li>
  <li>2/4 reviews recognized at <a href="https://2024.aclweb.org/">ACL 2024</a></li>
</ul>

<h2 class="section-title"><span class="i">🎤</span> Invited Talks</h2>
<hr class="thin-rule"/>

<ul class="talk-list">
  <li>
    <span class="date-badge">Nov 2024</span>
    Talk on <a href="https://aclanthology.org/2024.emnlp-main.277/">KidLM</a>, at
    <a href="https://www.ualberta.ca/en/computing-science/undergraduate-studies/course-directory/courses/honors-seminar.html">Honors Seminar</a>, University of Alberta
    (<a href="https://tafseer-nayeem.github.io/files/KidLM_seminar_slides.pdf">slides</a>)
  </li>
  <li>
    <span class="date-badge">Apr 2017</span>
    Talk on <a href="https://tafseer-nayeem.github.io/files/Introduction_to_NLTK.pdf">Introduction to NLTK</a>, University of Lethbridge
  </li>
  <li>
    <span class="date-badge">Feb 2017</span>
    Guest lecturer in CPSC 3750 - Artificial Intelligence, UofL
  </li>
</ul>

<h2 class="section-title"><span class="i">🖥️</span> Project Demonstrations</h2>
<hr class="thin-rule"/>

<ul class="clean-list">
  <li>Bengali Document Readability Checker (<a href="https://youtu.be/U05Pf9Y4tCQ">demo video</a>)</li>
  <li>Bengali Document Summarization Tool (<a href="https://youtu.be/LrnskktiXcg">demo video</a>)</li>
</ul>

<h2 class="section-title"><span class="i">👥</span> Leadership Activities</h2>
<hr class="thin-rule"/>

<ul class="clean-list">
  <li>
    Lab Manager, <a href="https://uofadblab.github.io/">Data & Language Intelligence (DaLI) Lab</a>, University of Alberta
    <span class="chip">2022 - current</span>
  </li>
  <li>
    Founding admin of a Discord server (~5,000+ members) supporting grad school applications
    <span class="chip">2021 - current</span>
  </li>
  <li>Member, Logistics & IT Support Committee, <a href="http://iccit.org.bd/2020/">ICCIT 2020</a></li>
  <li>Organizing Committee, Commonwealth of Learning (COL) TEL AUST Project (<a href="http://oasis.col.org/handle/11599/3220">report</a>)</li>
  <li>Organizer and host, <a href="https://www.intel.ai/">Intel Nervana AI Academy Workshop</a></li>
  <li>Convener, Project Showcasing, AUST CSE Week</li>
  <li>Organizing committee member, AUST CSE Fest; BUBT CSE Fiesta; IUT ICT Fest</li>
</ul>

<hr class="thin-rule"/>
<p style="margin-top:16px;"><a href="#">Back to Top</a></p>

</div>

<!-- 
----------------
- Organizing Committee Member & Researcher, **Commonwealth of Learning ([COL](https://www.col.org/)) TEL AUST** Project [<span style ="color:Green"> [**Report**] </span>](http://oasis.col.org/handle/11599/3220)
- Member, Logistics & IT Support Committee, [ICCIT 2020](http://iccit.org.bd/2020/)
- **Organizer and Host:** [Intel Nervana AI Academy - Workshop](https://www.intel.ai/).
<!-- - Member, *Bangladeshi Students' Organization at the University of Lethbridge* ([**BSOUL**](https://www.facebook.com/BSOULpage/)), Alberta, Canada. 
- Convener, Project Showcasing, **AUST CSE WEEK 2018**, Dhaka, Bangladesh.
- Organizing committee member in the **AUST CSE Fest 2013 and 2014**, Dhaka, Bangladesh.
- Organizing committee member in the **BUBT CSE FIESTA 2012**, Dhaka, Bangladesh.
- Organizing committee member in the **IUT ICT Fest 2011**, Dhaka, Bangladesh. 
-->

