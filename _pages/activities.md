---
layout: archive
title: "Activities"
permalink: /activities/
author_profile: true
---

<style>
/* Typography + spacing tuned for an academic CV page */
:root{
  --accent:#1F6CAB;          /* link/accent */
  --ink:#1f2937;             /* headings */
  --muted:#374151;           /* body */
  --rule:#e5e7eb;            /* thin separators */
  --chip-bg:#eef2f7;
  --chip-ink:#374151;
}

.section-title{
  margin: 22px 0 8px;
  font-size: 1.35rem;
  color: var(--ink);
  letter-spacing: .2px;
}

.subhead{
  margin: 14px 0 6px;
  font-size: 1.05rem;
  color: var(--ink);
}

.thin-rule{
  border:0; height:1px; background:var(--rule);
  margin: 16px 0 12px;
}

/* Links: subtle underline grow on hover (consistent with pubs page) */
.activities a{
  color: var(--accent);
  text-decoration: none;
  background-image: linear-gradient(currentColor,currentColor);
  background-size:0% 2px; background-repeat:no-repeat; background-position:0 100%;
  transition: background-size .22s ease;
}
.activities a:hover{ background-size:100% 2px; }

/* Year → items layout (no boxes) */
.year-list{ list-style:none; padding:0; margin: 4px 0 10px 0; }
.year-list li{
  display:grid; grid-template-columns: 72px 1fr; gap: 12px;
  padding: 2px 0;
}
.year{ color: var(--muted); font-weight:600; }
.items{ color: var(--muted); }

/* Chips reused from your other pages */
.chip{
  display:inline-flex; align-items:center; justify-content:center;
  padding:3px 8px; border-radius:999px; line-height:1;
  font-size:.75rem; font-weight:700; letter-spacing:.2px; text-transform:uppercase;
  border:1px solid #d1d5db; background:var(--chip-bg); color:var(--chip-ink);
  margin-right:6px; margin-bottom:4px;
}
.chip-accent{ background:var(--accent); color:#fff; border-color:transparent; }

/* Talks: date badge + compact line */
.talk-list{ list-style:none; padding:0; margin: 6px 0 0 0; }
.talk-list li{ margin: 8px 0; color: var(--muted); }
.date-badge{
  display:inline-block; padding:2px 8px; border-radius:999px; line-height:1;
  font-size:.75rem; font-weight:700; letter-spacing:.2px; background:var(--chip-bg); color:var(--chip-ink);
  margin-right:8px;
}

/* Plain ULs under leadership/projects */
.clean-list{ margin: 6px 0 0 1.1rem; }
.clean-list li{ margin: 6px 0; }

/* Mobile: slightly tighter columns */
@media (max-width:600px){
  .year-list li{ grid-template-columns: 64px 1fr; }
}
</style>

<div class="activities">

<h2 class="section-title">Professional Services</h2>
<hr class="thin-rule"/>

<h3 class="subhead">Area Chair (AC)</h3>
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

<h3 class="subhead">Reviewer</h3>
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

<h4 class="subhead">Outstanding Reviews</h4>
<p class="items" style="margin:4px 0 8px 0;">
  High-quality reviews recognized by venues as
  <span class="chip chip-accent">Great Reviews</span>
</p>
<ul class="clean-list">
  <li>1/3 reviews recognized at <a href="https://2025.naacl.org/">NAACL 2025</a></li>
  <li>2/4 reviews recognized at <a href="https://2024.aclweb.org/">ACL 2024</a></li>
</ul>

<h2 class="section-title">Invited Talks</h2>
<hr class="thin-rule"/>

<ul class="talk-list">
  <li>
    <span class="date-badge">Nov 2024</span>
    Talk on <a href="https://aclanthology.org/2024.emnlp-main.277/">KidLM</a>, at
    <a href="https://www.ualberta.ca/en/computing-science/undergraduate-studies/course-directory/courses/honors-seminar.html">Honors Seminar</a>, University of Alberta.
    (<a href="https://tafseer-nayeem.github.io/files/KidLM_seminar_slides.pdf">slides</a>)
  </li>
  <li>
    <span class="date-badge">Apr 2017</span>
    Talk on <a href="https://tafseer-nayeem.github.io/files/Introduction_to_NLTK.pdf">Introduction to NLTK</a>, University of Lethbridge.
  </li>
  <li>
    <span class="date-badge">Feb 2017</span>
    Guest lecturer in CPSC 3750 — Artificial Intelligence, UofL.
  </li>
</ul>

<h2 class="section-title">Project Demonstrations</h2>
<hr class="thin-rule"/>

<ul class="clean-list">
  <li>Bengali Document Readability Checker (<a href="https://youtu.be/U05Pf9Y4tCQ">demo video</a>)</li>
  <li>Bengali Document Summarization Tool (<a href="https://youtu.be/LrnskktiXcg">demo video</a>)</li>
</ul>

<h2 class="section-title">Leadership Activities</h2>
<hr class="thin-rule"/>

<ul class="clean-list">
  <li>
    Lab Manager, <a href="https://uofadblab.github.io/">Data & Language Intelligence (DaLI) Lab</a>, University of Alberta.
    <span class="chip">2022–current</span>
  </li>
  <li>
    Founding admin of a Discord server (~5,000+ members) supporting grad school applications.
    <span class="chip">2021–current</span>
  </li>
  <li>
    Member, Logistics & IT Support Committee, <a href="http://iccit.org.bd/2020/">ICCIT 2020</a>.
  </li>
  <li>
    Organizing Committee, Commonwealth of Learning (COL) TEL AUST Project.
    (<a href="http://oasis.col.org/handle/11599/3220">report</a>)
  </li>
  <li>Organizer and host, <a href="https://www.intel.ai/">Intel Nervana AI Academy Workshop</a>.</li>
  <li>Convener, Project Showcasing, AUST CSE Week.</li>
  <li>Organizing committee member, AUST CSE Fest; BUBT CSE Fiesta; IUT ICT Fest.</li>
</ul>

<p style="margin-top:16px;"><a href="#">Back to Top</a></p>

</div>


----------------

- **2024:** [ACL](https://2024.aclweb.org/), [EMNLP](https://2024.emnlp.org/), [NAACL](https://2024.naacl.org/), [EACL](https://2024.eacl.org/), [SIGIR](https://sigir-2024.github.io/), [WSDM](https://www.wsdm-conference.org/2024/)
- **2023:** [SIGIR](https://sigir.org/sigir2023/), [KDD](https://kdd.org/kdd2023/), [WSDM](https://www.wsdm-conference.org/2023/), [CIKM](https://uobevents.eventsair.com/cikm2023/)
- **2022:** [SIGIR](https://sigir.org/sigir2022/), [KDD](https://kdd.org/kdd2022/), [CIKM](https://www.cikm2022.org/), [ICDE](https://icde2022.ieeecomputer.my/)
<!-- - **2020:** [ICCIT](https://iccit.org.bd/2020/) -->
<!-- - **2019:** [ICIET](http://www.enggtech.du.ac.bd/iciet-2019/) -->

### 🏆 Outstanding Reviews

High-quality reviews that are strong, decisive, helpful, and well-written are recognized as **Great Reviews**.

- 🏅 1/3 reviews recognized at [NAACL 2025](https://2025.naacl.org/)  
- 🏅 2/4 reviews recognized at [ACL 2024](https://2024.aclweb.org/)  


## 👨‍🏫 Invited Talks
----------------
- <span style="color:Blue"> [Nov 2024] </span> - Talk on [KidLM](https://aclanthology.org/2024.emnlp-main.277/), at [Honors Seminar](https://www.ualberta.ca/en/computing-science/undergraduate-studies/course-directory/courses/honors-seminar.html) - University of Alberta (UofA), Canada. [[Slides](https://tafseer-nayeem.github.io/files/KidLM_seminar_slides.pdf)]
- <span style="color:Blue"> [Apr 2017] </span> - Talk on [Introduction to NLTK](https://tafseer-nayeem.github.io/files/Introduction_to_NLTK.pdf), University of Lethbrdige (UofL), AB, Canada. 
- <span style="color:Blue"> [Feb 2017] </span> - Guest Lecturer in CPSC 3750 - Artificial Intelligence course at UofL.

## 💻 Project Demonstrations 
----------------
* Bengali Document Readability Checker [[Demo Video]](https://youtu.be/U05Pf9Y4tCQ).
* Bengali Document Summarization Tool [[Demo Video]](https://youtu.be/LrnskktiXcg).


## 👨‍⚖️ Leadership Activities
------------------------
- **Lab Manager**, [Data & Language Intelligence (DaLI) Lab](https://uofadblab.github.io/), University of Alberta. `[2022 – Current]`
- **Founding Admin** of a Discord server comprising approximately **5,000+ members** dedicated to assisting prospective students with grad school applications. `[2021 - Current]`
- **Member**, Logistics & IT Support Committee, [ICCIT 2020](http://iccit.org.bd/2020/) Conference.
- **Organizing Committee**, Commonwealth of Learning (**[COL](https://www.col.org/)**) TEL AUST Project. [<span style ="color:Green"> [**Report**] </span>](http://oasis.col.org/handle/11599/3220)
- **Organizer and Host**, [Intel Nervana AI Academy - Workshop](https://www.intel.ai/).
- **Convener**, Project Showcasing, AUST CSE WEEK.
- **Organizing Committee Member**, AUST CSE Fest. 
- **Organizing Committee Member**, BUBT CSE FIESTA. 
- **Organizing Committee Member**, IUT ICT Fest.

----------------------

<!-- - 
- Organizing Committee Member & Researcher, **Commonwealth of Learning ([COL](https://www.col.org/)) TEL AUST** Project [<span style ="color:Green"> [**Report**] </span>](http://oasis.col.org/handle/11599/3220)
- Member, Logistics & IT Support Committee, [ICCIT 2020](http://iccit.org.bd/2020/)
- **Organizer and Host:** [Intel Nervana AI Academy - Workshop](https://www.intel.ai/).
<!-- - Member, *Bangladeshi Students' Organization at the University of Lethbridge* ([**BSOUL**](https://www.facebook.com/BSOULpage/)), Alberta, Canada. 
- Convener, Project Showcasing, **AUST CSE WEEK 2018**, Dhaka, Bangladesh.
- Organizing committee member in the **AUST CSE Fest 2013 and 2014**, Dhaka, Bangladesh.
- Organizing committee member in the **BUBT CSE FIESTA 2012**, Dhaka, Bangladesh.
- Organizing committee member in the **IUT ICT Fest 2011**, Dhaka, Bangladesh. 
-->


[**Back to Top**](#)

