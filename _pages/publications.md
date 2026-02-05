---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

**Full List:** [ [**Google Scholar**](https://scholar.google.com/citations?hl=en&user=qoeylgEAAAAJ&view_op=list_works&sortby=pubdate) \| [**ACL Anthology**](https://aclanthology.org/people/m/mir-tafseer-nayeem/) \| [**DBLP**](https://dblp.org/pid/125/2693.html) ]

<!--
<span style ="color:BlueViolet"> [\**indicates equal contribution*]</span>

[comment]: # \| [**Favorite Quotes**](#favorite-quotes)

[comment]: # <br/>

## Samples
--------------

## For just accepted papers
Accepted for publication at **EMNLP 2024** (Findings)

Proceedings of

## For Blinking NEW
<span class="blinking">🆕</span>

## Lines
<hr style="border: 1px solid #ddd;" />
-----------

## Sample Website 
https://jdf-prog.github.io/publications/

## Preprints
<hr style="border: 1px solid #ddd;" />

![arXiv 2024](https://img.shields.io/badge/arXiv%202024-blue?style=for-the-badge)
* [**LFOSum: Summarizing Long-form Opinions with Large Language Models**](https://arxiv.org/abs/2410.13037)<br/>
📰 <span style ="color:Maroon"> Uploaded to arXiv **(cs.CL)** </span> <br/>
👨‍💻  **Mir Tafseer Nayeem** and Davood Rafiei <br/>
👉 [![Paper](https://img.shields.io/badge/Paper-D3D3D3)](https://arxiv.org/abs/2410.13037)
-->

<style>
  /* ===========================
     Publication card
     =========================== */
  .pub-item{
    /* Thumb/badge size knobs */
    --thumb-w: 170px;        /* image column width */
    --thumb-max-h: 120px;    /* max visible image height (desktop/tablet) */
    --badge-w: 120px;        /* conference badge width */

    /* FONT SIZE knobs */
    --font-title: .90rem;    /* title font size */
    --font-meta: .85rem;     /* "Accepted for..." font size */
    --font-auth: .85rem;     /* authors font size */
    --font-links: 12px;      /* link pill font size */
    --font-badge: 12px;      /* conference badge text size */

    display:grid;
    grid-template-columns: var(--thumb-w) 1fr;
    gap:18px;
    align-items:start;
    padding:16px 18px;
    margin:18px 0;
    border:1px solid #e5e7eb;
    border-radius:12px;
    background:#fff;
    box-shadow:0 1px 2px rgba(0,0,0,.04);

    /* hover elevation */
    transition: box-shadow .22s ease, transform .22s ease, border-color .22s ease;
  }
  .pub-item:hover{
    box-shadow:0 10px 28px rgba(0,0,0,.08);
    transform: translateY(-2px);
    border-color:#e2e8f0;
  }

  .pub-left{
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:10px;
  }

  /* ADAPTIVE THUMBNAIL (desktop/tablet): bounded box, rounded */
  .thumb-wrap{
    width: var(--thumb-w);
    max-height: var(--thumb-max-h);
    display:grid;
    place-items:center;
    border:1px solid #e5e7eb;
    border-radius:12px;
    background:#fff;
    overflow:hidden;  /* clip tiny overflow while preserving radius */
    transition: box-shadow .2s ease;
  }
  .thumb-wrap img{
    max-width:100%;
    max-height:100%;
    width:auto;
    height:auto;      /* preserves aspect ratio */
    border-radius: inherit;
    transition: transform .28s ease, filter .28s ease;
  }
  /* subtle image zoom on card hover */
  .pub-item:hover .thumb-wrap img{ transform: scale(1.03); }

  /* generic tiny pill */
  .tag-badge{
    display:inline-flex; align-items:center; justify-content:center;
    padding:3px 7px;                                /* compact for ergonomics */
    border-radius:999px;
    line-height:1.05; letter-spacing:.2px; text-transform:uppercase;
    font-weight:700;
    font-size: calc(var(--font-badge) - 2px);       /* keep smaller than main badge */
    border: 1px solid transparent;
    white-space:nowrap;
    transition: transform .16s ease, box-shadow .16s ease, filter .16s ease;
  }
  .tag-badge:hover{
    transform: translateY(-1px);
    box-shadow: 0 4px 10px rgba(0,0,0,.06);
    filter: saturate(1.03);
  }
  /* color variants */
  .tag-oral     { color:#fff; background:#b45309; border-color:#9a3f07; } /* amber */
  .tag-spotlight{ color:#fff; background:#4f46e5; border-color:#4338ca; } /* indigo */
  .tag-poster   { color:#111827; background:#e5e7eb; border-color:#d1d5db; } /* gray */
  
  /* --- award line and badge --- */
.pub-award-line{
  display:block;
  margin:6px 0 8px;             /* spacing between meta ↔ award ↔ authors (tune here) */
}

/* Pill itself */
.award-badge{
  display:inline-flex; align-items:center; justify-content:center; gap:6px;
  padding:5px 12px;             /* ← TUNE height/width of the pill */
  border-radius:999px; line-height:1.05;
  font-weight:800; letter-spacing:.2px;
  text-transform:none;          /* sentence case */
  font-size: var(--font-badge); 
  border:1px solid transparent; white-space:nowrap;
  transition: transform .16s ease, box-shadow .16s ease, filter .16s ease;
}
.award-badge:hover{
  transform: translateY(-1px);
  box-shadow:0 6px 14px rgba(0,0,0,.06);
  filter:saturate(1.03);
}

/* Academic, outline gold */
.award-outline-gold{
  color:#7A5A00;
  background:#FFF8E6;
  border-color:#E7C76A;
}

/* Optional stronger emphasis (solid gold) */
.award-solid-gold{
  color:#fff;
  background:#B58500;
  border-color:#9A6F00;
}

/* Mobile: keep badge compact (safe on narrow screens) */
@media (max-width: 480px){
  .pub-award-line{ margin:4px 0 8px; }                       /* tighten vertical rhythm */
  .award-badge{
    padding:3px 8px;                                         /* smaller pill on phones */
    font-size: calc(var(--font-badge, 12px) - 2px);          /* slightly smaller text */
  }
}

/* Tune the blue badge color in one place */
:root{
  --badge-blue: #155284ff; /* steel blue (default) */
}

.conf-badge-blue{
  display:inline-flex; align-items:center; justify-content:center;
  padding:8px 14px; min-width: var(--badge-w, 120px);
  line-height:1; border-radius:999px;
  font-size: var(--font-badge, 12px); font-weight:700; letter-spacing:.3px;
  text-transform:uppercase; color:#fff;
  background: var(--badge-blue);                  /* ← uses variable */
  white-space:nowrap;
  transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
}
.conf-badge-blue:hover{
  transform: translateY(-1px);
  box-shadow: 0 6px 16px color-mix(in srgb, var(--badge-blue) 28%, transparent);
  filter: saturate(1.05);
}

/* Tune the teal badge color in one place */
:root{
  --badge-teal: #0e5c56ff; /* default: teal */
}

.conf-badge-teal{
  display:inline-flex; align-items:center; justify-content:center;
  padding:8px 14px; min-width: var(--badge-w, 120px);
  line-height:1; border-radius:999px;
  font-size: var(--font-badge, 12px); font-weight:700; letter-spacing:.3px;
  text-transform:uppercase; color:#fff;
  background: var(--badge-teal);                 /* ← uses variable */
  white-space:nowrap;
  transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
}
.conf-badge-teal:hover{
  transform: translateY(-1px);
  box-shadow: 0 6px 16px color-mix(in srgb, var(--badge-teal) 28%, transparent);
  filter: saturate(1.05);
}

/* Tune the badge color in one place */
:root{
  --badge-green: #073511ff;
}

.conf-badge-green{
  display:inline-flex; align-items:center; justify-content:center;
  padding:8px 14px; min-width: var(--badge-w, 120px);
  line-height:1; border-radius:999px;
  font-size: var(--font-badge, 12px); font-weight:700; letter-spacing:.3px;
  text-transform:uppercase; color:#fff;
  background: var(--badge-green);                 /* ← uses the variable */
  white-space:nowrap;
  transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
}
.conf-badge-green:hover{
  transform: translateY(-1px);
  box-shadow: 0 6px 16px color-mix(in srgb, var(--badge-green) 28%, transparent);
  filter: saturate(1.05);
}

/* Tune the NAACL navy badge color in one place */
:root{
  --badge-navy: #242D8C; /* NAACL navy */
}

.conf-badge-navy{
  display:inline-flex; align-items:center; justify-content:center;
  padding:8px 14px; min-width: var(--badge-w, 120px);
  line-height:1; border-radius:999px;
  font-size: var(--font-badge, 12px); font-weight:700; letter-spacing:.3px;
  text-transform:uppercase; color:#fff;
  background: var(--badge-navy);               /* ← uses the variable */
  white-space:nowrap;
  transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
}
.conf-badge-navy:hover{
  transform: translateY(-1px);
  box-shadow: 0 6px 16px color-mix(in srgb, var(--badge-navy) 28%, transparent);
  filter: saturate(1.05);
}

:root{ --sienna-new: #4f324fff; } /* lighter/darker, just tweak --sienna-new (e.g., #7A4A79 lighter, #5A315A darker). */

.conf-badge-sienna{
  display:inline-flex; align-items:center; justify-content:center;
  padding:8px 14px; min-width: var(--badge-w, 120px);
  line-height:1; border-radius:999px;
  font-size: var(--font-badge, 12px); font-weight:700; letter-spacing:.3px;
  text-transform:uppercase; color:#fff; background: var(--sienna-new);
  white-space:nowrap;
  transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
}
.conf-badge-sienna:hover{
  transform: translateY(-1px);
  box-shadow: 0 6px 16px color-mix(in srgb, var(--sienna-new) 28%, transparent);
  filter: saturate(1.05);
}

/* Tune the violet badge color in one place */
:root{
  --badge-violet: #460b7dff; /* BlueViolet (default) */
}

.conf-badge-violet{
  display:inline-flex; align-items:center; justify-content:center;
  padding:8px 14px; min-width: var(--badge-w, 120px);
  line-height:1; border-radius:999px;
  font-size: var(--font-badge, 12px); font-weight:700; letter-spacing:.3px;
  text-transform:uppercase; color:#fff;
  background: var(--badge-violet);               /* ← uses variable */
  white-space:nowrap;
  transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
}
.conf-badge-violet:hover{
  transform: translateY(-1px);
  box-shadow: 0 6px 16px color-mix(in srgb, var(--badge-violet) 28%, transparent);
  filter: saturate(1.05);
}

/* NeurIPS badge — distinct cool tone (Aegean blue) */
:root { --neurips-badge: #0a365bff; } /* TUNE this if you want a different shade */

.conf-badge-aegean{
  display:inline-flex; align-items:center; justify-content:center;
  padding:8px 14px; min-width: var(--badge-w, 120px);
  line-height:1; border-radius:999px;
  font-size: var(--font-badge, 12px); font-weight:700; letter-spacing:.3px;
  text-transform:uppercase; color:#fff; background: var(--neurips-badge);
  white-space:nowrap;
  transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
}
.conf-badge-aegean:hover{
  transform: translateY(-1px);
  box-shadow: 0 6px 16px color-mix(in srgb, var(--neurips-badge) 28%, transparent);
  filter: saturate(1.05);
}

.badge-nocaps{
  text-transform: none;
  letter-spacing: .15px; /* a touch tighter than all-caps spacing */
}
  /* compact text (uses variables above) */
.pub-title{ margin:0 0 4px 0; font-size: var(--font-title); line-height:1.28; }
.pub-title a{
    text-decoration:none;
    background-image: linear-gradient(currentColor,currentColor);
    background-size: 0% 2px;                 /* animated underline */
    background-repeat:no-repeat;
    background-position:0 100%;
    transition: background-size .22s ease, color .22s ease;
  }
.pub-title a:hover{ background-size: 100% 2px; }

  /* Make the meta line flex so the ORAL pill aligns vertically */
.pub-meta{
    margin:0 0 4px 0;
    font-size: var(--font-meta);
    color:#7a1f1f;
    display:flex; align-items:center; gap:8px; flex-wrap:wrap;
  }

.pub-authors{ margin:0 0 8px 0; font-size: var(--font-auth); color:#374151; }
.pub-authors .me{ font-weight:700; }

.pub-links a{
    display:inline-block; padding:6px 10px;
    margin-right:8px; margin-bottom:6px;
    border-radius:8px; border:1px solid #d1d5db;
    background:#f3f4f6; text-decoration:none; font-size: var(--font-links);
    transition: background-color .16s ease, border-color .16s ease, transform .16s ease, box-shadow .16s ease;
  }
.pub-links a:hover{
    background:#eef2f7; border-color:#cbd5e1;
    transform: translateY(-1px);
    box-shadow:0 6px 14px rgba(0,0,0,.06);
  }

/* Focus states for keyboard accessibility */
.pub-item:focus-within{ outline:2px solid #bfdbfe; outline-offset:2px; }
.pub-title a:focus-visible,
.pub-links a:focus-visible,
.conf-badge-blue:focus-visible,
.conf-badge-teal:focus-visible,
.thumb-wrap:focus-visible{
outline:3px solid #93c5fd; outline-offset:3px; border-radius:10px;
}

/* Respect reduced-motion preferences */
@media (prefers-reduced-motion: reduce){
    .pub-item, .thumb-wrap img, .pub-links a,
    .conf-badge-blue, .conf-badge-teal, .pub-title a{
      transition: none !important;
    }
}

  /* Device-friendly (no cropping on phones; full-width image with auto height) */
@media (max-width: 640px){
    .pub-item{
      grid-template-columns:1fr;
      --thumb-w: 100%;
      --thumb-max-h: none;   /* disable fixed cap on phones */
      gap:14px;
      padding:12px 14px;
    }
    .thumb-wrap{
      width:100%;
      max-height:none;       /* let the image define the height */
      overflow:visible;      /* no clipping */
      border: none;          /* move border to the image for clean corners */
    }
    .thumb-wrap img{
      width:100%;
      height:auto;
      border:1px solid #e5e7eb;
      border-radius:12px;
    }
  }
@media (max-width: 480px){
    .pub-item{
      gap:12px;
      padding:10px 12px;
    }
    .conf-badge-blue,
    .conf-badge-teal{
      min-width: calc(var(--badge-w) - 12px);
      padding:7px 12px;
      font-size: calc(var(--font-badge) - 1px);
    }
    .tag-badge{
      padding:2px 6px;
      font-size: calc(var(--font-badge) - 3px);
    }
  }
@media (max-width: 360px){
    .pub-item{
      gap:10px;
      padding:8px 10px;
    }
  }

/* Workshop Badge */
  /* Stack the main venue badge and the sub-badge vertically */
  .badge-stack{
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:6px; /* space between ACL 2017 and Workshop */
  }
/* Sub-badge: smaller pill */
  .sub-badge{
    display:inline-flex; align-items:center; justify-content:center;
    padding:3px 8px;                 /* TUNE: pill size */
    border-radius:999px; line-height:1;
    font-weight:700; letter-spacing:.2px; text-transform:uppercase;
    font-size: calc(var(--font-badge, 12px) - 4.5px); /* TUNE: sub-badge text size */
    border:1px solid transparent; white-space:nowrap;
  }
/* Color for "Workshop" sub-badge */
  .sub-badge-workshop{
    color:#fff;
    background:#4F46E5;  /* indigo */
    border-color:#4338CA;
  }
/* Optional hover polish */
  .sub-badge-workshop:hover{
    filter:saturate(1.05);
    transform: translateY(-1px);
    box-shadow:0 6px 14px rgba(79,70,229,0.18);
    transition: transform .16s ease, box-shadow .16s ease, filter .16s ease;
  }
/* Mobile: keep it compact */
  @media (max-width:640px){
    .sub-badge{ font-size: calc(var(--font-badge, 12px) - 4px); padding:2px 7px; }
  }

.eq {
  font-size: 1.2em !important;   /* FORCE big star */
  font-weight: 650;
  color: #111827;                 /* academic gold */
  vertical-align: baseline;       /* stop shrinking */
  position: relative;
}

.pub-year{
  margin: 32px 0 12px;
  font-size: 1.55rem;
  font-weight: 650;
  color: #0a0d15;
  border-bottom: 2px solid #e5e7eb;
  padding-bottom: 4px;
  letter-spacing: .2px;
}

</style>

<p style="color:#4b5563; font-size:0.95rem; font-style: italic; margin-top:6px;">
  <span class="eq">*</span> indicates equal contribution
</p>

<h2 class="pub-year">2026</h2>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://arxiv.org/abs/2601.13260" aria-label="Tokenizer LLM (EACL 2026)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/Tokenizer-EACL2026.png"
        alt="Stop Taking Tokenizers for Granted: They Are Core Design Decisions in Large Language Models — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-violet">EACL 2026</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://arxiv.org/abs/2601.13260">
        Stop Taking Tokenizers for Granted: They Are Core Design Decisions in Large Language Models
      </a>
    </h3>
    <div class="pub-meta">Published at <b>EACL 2026</b>(Main)</div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span><span class="eq">*</span>, Sawsan Alqahtani<span class="eq">*</span>, Md Tahmid Rahman Laskar, Tasnim Mohiuddin, and M Saiful Bari
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2601.13260">Paper</a>
    </div>
  </div>
</div>

<h2 class="pub-year">2025</h2>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://arxiv.org/abs/2509.00285" aria-label="OpinioRAG paper" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/OpinioRAG-COLM2025.png"
        alt="OpinioRAG thumbnail" loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-blue">COLM 2025</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://arxiv.org/abs/2509.00285">
        OpinioRAG: Towards Generating User-Centric Opinion Highlights from Large-scale Online Reviews
      </a>
    </h3>
    <div class="pub-meta">Published at <b>COLM 2025</b></div>
    <div class="pub-authors"><span class="me">Mir Tafseer Nayeem</span> and Davood Rafiei</div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2509.00285">Paper</a>
      <a href="https://tafseer-nayeem.github.io/OpinioRAG/">Website</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://arxiv.org/abs/2510.09947" aria-label="Beyond Fertility (NeurIPS 2025 Workshop)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/NeurIPS2025-STRR.png"
        alt="Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <div class="badge-stack">
      <span class="conf-badge-aegean badge-nocaps">NeurIPS 2025</span>
      <span class="sub-badge sub-badge-workshop" aria-label="Workshop">Workshop</span>
    </div>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://arxiv.org/abs/2510.09947">
        Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation
      </a>
    </h3>
    <div class="pub-meta">Published at <b>NeurIPS 2025</b>(Workshop)</div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span><span class="eq">*</span>, Sawsan Alqahtani<span class="eq">*</span>, Md Tahmid Rahman Laskar, Tasnim Mohiuddin, and M Saiful Bari
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2510.09947">Paper</a>
      <a href="https://github.com/tafseer-nayeem/STRR">Code</a>
      <a href="https://tafseer-nayeem.github.io/files/NeurIPS2025_STRR_poster.pdf">Poster</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://arxiv.org/abs/2508.17647" aria-label="SurveyGen paper" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/SurveyGen-EMNLP2025.png"
        alt="SurveyGen thumbnail" loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-teal">EMNLP 2025</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://arxiv.org/abs/2508.17647">
        SurveyGen: Quality-Aware Scientific Survey Generation with Large Language Models
      </a>
    </h3>
    <div class="pub-meta">
      Published at <b>EMNLP 2025</b>(Main)
      <span class="tag-badge tag-oral" aria-label="Oral presentation">Oral</span>
    </div>
    <div class="pub-authors">Tong Bao, <span class="me">Mir Tafseer Nayeem</span>, Davood Rafiei, and Chengzhi Zhang</div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2508.17647">Paper</a>
      <a href="https://github.com/tongbao96/SurveyGen">Code</a>
      <a href="https://tafseer-nayeem.github.io/files/EMNLP2025/EMNLP2025_SurveyGen_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/EMNLP2025/EMNLP2025_SurveyGen_poster.pdf">Poster</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://arxiv.org/abs/2508.09450" aria-label="Fair Narratives paper" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/ChartEthics-EMNLP2025.png"
        alt="From Charts to Fair Narratives thumbnail" loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-teal">EMNLP 2025</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://arxiv.org/abs/2508.09450">
        From Charts to Fair Narratives: Uncovering and Mitigating Geo-Economic Biases in Chart-to-Text
      </a>
    </h3>
    <div class="pub-meta">Published at <b>EMNLP 2025</b>(Main)</div>
    <div class="pub-authors">
      Ridwan Mahbub<span class="eq">*</span>,
      Mohammed Saidul Islam<span class="eq">*</span>,
      <span class="me">Mir Tafseer Nayeem</span>,
      Md Tahmid Rahman Laskar,
      Mizanur Rahman,
      Shafiq Joty,
      and Enamul Hoque
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2508.09450">Paper</a>
      <a href="https://tafseer-nayeem.github.io/files/EMNLP2025/EMNLP2025_ChartEthics_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/EMNLP2025/EMNLP2025_ChartEthics_poster.pdf">Poster</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://arxiv.org/abs/2510.07545" aria-label="Chart Judge paper" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/ChartJudge-EMNLP2025.png"
        alt="Chart Judge thumbnail" loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-teal">EMNLP 2025</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://arxiv.org/abs/2510.07545">
        Deploying Tiny LVLM Judges for Real-World Evaluation of Chart Models: Lessons Learned and Best Practices
      </a>
    </h3>
    <div class="pub-meta">Published at <b>EMNLP 2025</b>(Industry Track)</div>
    <div class="pub-authors">
      Md Tahmid Rahman Laskar, 
      Mohammed Saidul Islam, 
      Ridwan Mahbub, 
      Mizanur Rahman, 
      Amran Bhuiyan, 
      Israt Jahan,
      <span class="me">Mir Tafseer Nayeem</span>,
      Shafiq Joty,
      Enamul Hoque,
      and Jimmy Huang
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2510.07545">Paper</a>
      <a href="https://github.com/tahmedge/chart_lvlm_judge">Code</a>
    </div>
  </div>
</div>


<div class="pub-item">
  <div class="pub-left">
    <a href="https://arxiv.org/abs/2508.09716" aria-label="Chart Deception paper" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/VisDeception-VIS2025.png"
        alt="The Perils of Chart Deception thumbnail" loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-green">IEEE VIS 2025</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://arxiv.org/abs/2508.09716">
        The Perils of Chart Deception: How Misleading Visualizations Affect Vision-Language Models
      </a>
    </h3>
    <div class="pub-meta">
       Published at <b>IEEE VIS 2025</b>
      <span class="tag-badge tag-oral" aria-label="Oral presentation">Oral</span>
    </div>
    <div class="pub-award-line">
      <a href="https://ieeevis.org/year/2025/info/awards/best-paper-awards" aria-label="Best Short Paper Award — IEEE VIS 2025 best paper awards"
         target="_blank" rel="noopener noreferrer">
      <span class="award-badge award-outline-gold"> 🏆 Best Short Paper Award </span>
      </a>
    </div>
    <div class="pub-authors">
      Ridwan Mahbub, Mohammed Saidul Islam, Md Tahmid Rahman Laskar,
      Mizanur Rahman, <span class="me">Mir Tafseer Nayeem</span>, and Enamul Hoque
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2508.09716">Paper</a>
      <a href="https://github.com/vis-nlp/visDeception">Code</a>
      <a href="https://www.yorku.ca/laps/newsroom/2025/12/01/professor-enamul-hoque-prince-and-team-win-best-paper-award-at-ieee-vis/">Media Coverage</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/2025.acl-industry.83/" aria-label="Judging the Judges (ACL 2025)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/ChartJudge-ACL2025.png"
        alt="Judging the Judges thumbnail" loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-navy">ACL 2025</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/2025.acl-industry.83/">
        Judging the Judges: Can Large Vision-Language Models Fairly Evaluate Chart Comprehension and Reasoning?
      </a>
    </h3>
    <div class="pub-meta">Published at <b>ACL 2025</b>(Industry Track)</div>
    <div class="pub-authors">
      Md Tahmid Rahman Laskar, Mohammed Saidul Islam, Ridwan Mahbub, Ahmed Masry,
      Mizanur Rahman, Amran Bhuiyan, <span class="me">Mir Tafseer Nayeem</span>,
      Shafiq Joty, Enamul Hoque, and Jimmy Huang
    </div>
    <div class="pub-links">
      <a href="https://aclanthology.org/2025.acl-industry.83/">Paper</a>
      <a href="https://github.com/tahmedge/chart_lvlm_judge">Code</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/2025.naacl-industry.65/" aria-label="eC-Tab2Text (NAACL 2025)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/eC-Tab2Text-NAACL2025.png"
        alt="eC-Tab2Text thumbnail" loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-sienna">NAACL 2025</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/2025.naacl-industry.65/">
        eC-Tab2Text: Aspect-Based Text Generation from e-Commerce Product Tables
      </a>
    </h3>
    <div class="pub-meta">Published at <b>NAACL 2025</b>(Industry Track)</div>
    <div class="pub-authors">
      Luis Antonio Gutiérrez Guanilo,
      <span class="me">Mir Tafseer Nayeem</span>,
      Cristian López, and Davood Rafiei
    </div>
    <div class="pub-links">
      <a href="https://aclanthology.org/2025.naacl-industry.65/">Paper</a>
      <a href="https://github.com/Luis-ntonio/eC-Tab2Text">Code &amp; Dataset</a>
    </div>
  </div>
</div>

<h2 class="pub-year">2024</h2>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/2024.emnlp-main.277/" aria-label="KidLM (EMNLP 2024)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/KidLM-EMNLP2024.png"
        alt="KidLM: Advancing Language Models for Children — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-teal">EMNLP 2024</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/2024.emnlp-main.277/">
        KidLM: Advancing Language Models for Children – Early Insights and Future Directions
      </a>
    </h3>
    <div class="pub-meta">Published at <b>EMNLP 2024</b>(Main)</div>
    <div class="pub-award-line">
      <a href="https://2024.emnlp.org/program/best_papers/" aria-label="Best Resource Paper Award — EMNLP 2024 best papers"
         target="_blank" rel="noopener noreferrer">
      <span class="award-badge award-outline-gold"> 🏆 Best Resource Paper Award </span>
      </a>
    </div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span> and Davood Rafiei
    </div>
    <div class="pub-links">
      <a href="https://huggingface.co/datasets/tafseer-nayeem/KidLM-corpus">Corpus</a>
      <a href="https://huggingface.co/collections/tafseer-nayeem/kidlm-672e5afcdc68cedc1c5df812">Models &amp; Collection</a>
      <a href="https://www.ualberta.ca/en/computing-science/news-and-events/news/2024/november/best-paper-award-at-emnlp-2024.html">Media Coverage</a>
      <a href="https://tafseer-nayeem.github.io/files/EMNLP2024/EMNLP2024_KidLM_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/EMNLP2024/EMNLP2024_KidLM_poster.pdf">Poster</a>
      <a href="https://x.com/mtnayeem/status/1855726698324742581">X Thread</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/2024.findings-emnlp.191/" aria-label="LVLM Chart Comprehension (EMNLP 2024 Findings)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/ChartEval-EMNLP2024.png"
        alt="Are Large Vision Language Models up to the Challenge of Chart Comprehension and Reasoning? — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-teal">EMNLP 2024</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/2024.findings-emnlp.191/">
        Are Large Vision Language Models up to the Challenge of Chart Comprehension and Reasoning
      </a>
    </h3>
    <div class="pub-meta">Published at <b>EMNLP 2024</b>(Findings)</div>
    <div class="pub-authors">
      Mohammed Saidul Islam,
      Raian Rahman,
      Ahmed Masry<span class="eq">*</span>,
      Md Tahmid Rahman Laskar<span class="eq">*</span>,
      <span class="me">Mir Tafseer Nayeem</span><span class="eq">*</span>,
      and Enamul Hoque
    </div>
    <div class="pub-links">
      <a href="https://github.com/saidul-islam98/LVLM-ChartEval">Code</a>
      <a href="https://tafseer-nayeem.github.io/files/EMNLP2024/EMNLP2024_ChartEval_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/EMNLP2024/EMNLP2024_ChartEval_poster.pdf">Poster</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/2024.findings-acl.771/" aria-label="XL-HeadTags (ACL 2024 Findings)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/XL-HeadTags-ACL2024.png"
        alt="XL-HeadTags: Leveraging Multimodal Retrieval Augmentation — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-navy">ACL 2024</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/2024.findings-acl.771/">
        XL-HeadTags: Leveraging Multimodal Retrieval Augmentation for the Multilingual Generation of News Headlines and Tags
      </a>
    </h3>
    <div class="pub-meta">Published at <b>ACL 2024</b>(Findings)</div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span><span class="eq">*</span>,
      Faisal Tareque Shohan<span class="eq">*</span>,
      Samsul Islam,
      Abu Ubaida Akash,
      and Shafiq Joty
    </div>
    <div class="pub-links">
      <a href="https://github.com/faisaltareque/XL-HeadTags">Code</a>
      <a href="https://huggingface.co/datasets/faisaltareque/XL-HeadTags">Dataset &amp; Models</a>
      <a href="https://tafseer-nayeem.github.io/files/ACL2024/ACL2024_XL-HeadTags_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/ACL2024/ACL2024_XL-HeadTags_poster.pdf">Poster</a>
      <a href="https://x.com/mtnayeem/status/1853936728408809835">X Thread</a>
    </div>
  </div>
</div>


<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/2024.lrec-main.201/" aria-label="BenLLM-Eval (COLING 2024)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/BenLLM-COLING2024.png"
        alt="BenLLM-Eval: A Comprehensive Evaluation into the Potentials and Pitfalls of LLMs on Bengali NLP — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-sienna">COLING 2024</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/2024.lrec-main.201/">
        BenLLM-Eval: A Comprehensive Evaluation into the Potentials and Pitfalls of Large Language Models on Bengali NLP
      </a>
    </h3>
    <div class="pub-meta">Published at <b>COLING 2024</b></div>
    <div class="pub-authors">
      Mohsinul Kabir<span class="eq">*</span>,
      Mohammed Saidul Islam<span class="eq">*</span>,
      Md Tahmid Rahman Laskar,
      <span class="me">Mir Tafseer Nayeem</span>,
      M Saiful Bari,
      and Enamul Hoque
    </div>
    <div class="pub-links">
      <a href="https://github.com/saidul-islam98/BenLLMeval">Code</a>
      <a href="https://tafseer-nayeem.github.io/files/LREC-COLING-2024/LREC-COLING-2024_BenLLM-Eval_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/LREC-COLING-2024/LREC-COLING-2024_BenLLM-Eval_poster.pdf">Poster</a>
    </div>
  </div>
</div>

<h2 class="pub-year">2023</h2>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://dl.acm.org/doi/10.1145/3583780.3615172" aria-label="Product Entity Matching via Tabular Data (CIKM 2023)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/PEM-CIKM2023.png"
        alt="Product Entity Matching via Tabular Data — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-green">CIKM 2023</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://dl.acm.org/doi/10.1145/3583780.3615172">
        Product Entity Matching via Tabular Data
      </a>
    </h3>
    <div class="pub-meta">Published at <b>ACM CIKM 2023</b></div>
    <div class="pub-authors">
      Ali Naeimabadi,
      <span class="me">Mir Tafseer Nayeem</span>,
      and Davood Rafiei
    </div>
    <div class="pub-links">
      <a href="https://tafseer-nayeem.github.io/files/CIKM2023/CIKM2023_PEM_paper.pdf">Paper</a>
      <a href="https://tafseer-nayeem.github.io/files/CIKM2023/CIKM2023_PEM_poster.pdf">Poster</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/2023.findings-eacl.125/" aria-label="Reviewer Expertise & Temporal Helpfulness (EACL 2023 Findings)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/EACL2023-RHP.png"
        alt="On the Role of Reviewer Expertise in Temporal Review Helpfulness Prediction — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-violet">EACL 2023</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/2023.findings-eacl.125/">
        On the Role of Reviewer Expertise in Temporal Review Helpfulness Prediction
      </a>
    </h3>
    <div class="pub-meta">Published at <b>EACL 2023</b>(Findings)</div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span> and Davood Rafiei
    </div>
    <div class="pub-links">
      <a href="https://github.com/tafseer-nayeem/RHP">Code</a>
      <a href="https://huggingface.co/datasets/tafseer-nayeem/review_helpfulness_prediction">Dataset</a>
      <a href="https://tafseer-nayeem.github.io/files/EACL2023/EACL2023_RHP_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/EACL2023/EACL2023_RHP_poster.pdf">Poster</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/2023.eacl-main.4/" aria-label="Shironaam (EACL 2023)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/Shironaam-EACL2023.png"
        alt="Shironaam: Bengali News Headline Generation using Auxiliary Information — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-violet">EACL 2023</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/2023.eacl-main.4/">
        Shironaam: Bengali News Headline Generation using Auxiliary Information
      </a>
    </h3>
    <div class="pub-meta">Published at <b>EACL 2023</b>(Main)</div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span><span class="eq">*</span>,
      Abu Ubaida Akash<span class="eq">*</span>,
      Faisal Tareque Shohan,
      and Tanvir Islam
    </div>
    <div class="pub-links">
      <a href="https://github.com/dialect-ai/BenHeadGen">Code</a>
      <a href="https://huggingface.co/datasets/dialect-ai/shironaam">Dataset</a>
      <a href="https://tafseer-nayeem.github.io/files/EACL2023/EACL2023_Shironaam_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/EACL2023/EACL2023_Shironaam_poster.pdf">Poster</a>
    </div>
  </div>
</div>

<h2 class="pub-year">2021</h2>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://ojs.aaai.org/index.php/AAAI/article/view/17495" aria-label="Simple or Complex? (AAAI 2021)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/AAAI2021-Readability.png"
        alt="Simple or Complex? Learning to Predict Readability of Bengali Texts — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-blue">AAAI 2021</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://ojs.aaai.org/index.php/AAAI/article/view/17495">
        Simple or Complex? Learning to Predict Readability of Bengali Texts
      </a>
    </h3>
    <div class="pub-meta">Published at <b>AAAI 2021</b>(Main)</div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span><span class="eq">*</span>,
      Susmoy Chakraborty<span class="eq">*</span>,
      and Wasi Uddin Ahmad
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2012.07701">Paper</a>
      <a href="https://github.com/tafseer-nayeem/BengaliReadability">Code</a>
      <a href="https://github.com/tafseer-nayeem/BengaliReadability/tree/main/Data">Dataset</a>
      <a href="https://tafseer-nayeem.github.io/files/AAAI2021/AAAI2021_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/AAAI2021/AAAI2021_poster.pdf">Poster</a>
      <a href="https://youtu.be/U05Pf9Y4tCQ">Demo Video</a>
      <a href="https://x.com/mtnayeem/status/1334590638105378817">X Thread</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://www.aclweb.org/anthology/2021.eacl-main.224" aria-label="Unsupervised Abstractive Summarization of Bengali Text Documents (EACL 2021)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/EACL2021-Summarization.png"
        alt="Unsupervised Abstractive Summarization of Bengali Text Documents — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-violet">EACL 2021</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://www.aclweb.org/anthology/2021.eacl-main.224">
        Unsupervised Abstractive Summarization of Bengali Text Documents
      </a>
    </h3>
    <div class="pub-meta">Published at <b>EACL 2021</b>(Main)</div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span><span class="eq">*</span>,
      Radia Rayan Chowdhury<span class="eq">*</span>,
      TT Mim,
      MSR Chowdhury,
      and T Jannat
    </div>
    <div class="pub-links">
      <a href="https://github.com/tafseer-nayeem/BengaliSummarization">Code</a>
      <a href="https://github.com/tafseer-nayeem/BengaliSummarization/tree/main/Dataset">Dataset</a>
      <a href="https://tafseer-nayeem.github.io/files/EACL2021/EACL2021_presentation.pdf">Slides</a>
      <a href="https://tafseer-nayeem.github.io/files/EACL2021/EACL2021_poster.pdf">Poster</a>
      <a href="https://youtu.be/LrnskktiXcg">Demo Video</a>
      <a href="https://x.com/mtnayeem/status/1350551479283662848">X Thread</a>
    </div>
  </div>
</div>

<h2 class="pub-year">2019</h2>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://link.springer.com/chapter/10.1007/978-3-030-15719-7_14" aria-label="Neural Diverse Abstractive Sentence Compression (ECIR 2019)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/ECIR2019-Compression.png"
        alt="Neural Diverse Abstractive Sentence Compression Generation — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-green">ECIR 2019</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://link.springer.com/chapter/10.1007/978-3-030-15719-7_14">
        Neural Diverse Abstractive Sentence Compression Generation
      </a>
    </h3>
    <div class="pub-meta">Published at <b>ECIR 2019</b></div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span>,
      Tanvir Ahmed Fuad,
      and Yllias Chali
    </div>
    <div class="pub-links">
      <a href="https://tafseer-nayeem.github.io/files/ECIR_2019_paper.pdf">Paper</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://www.sciencedirect.com/science/article/pii/S0885230818303449"
       aria-label="Neural Sentence Fusion for Diversity Driven Abstractive Multi-Document Summarization (CSL 2019)"
       class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/CSL2019-NeuFuse.png"
        alt="Neural Sentence Fusion for Diversity Driven Abstractive Multi-Document Summarization — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-sienna">CS&L 2019</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://www.sciencedirect.com/science/article/pii/S0885230818303449">
        Neural Sentence Fusion for Diversity Driven Abstractive Multi-Document Summarization
      </a>
    </h3>
    <div class="pub-meta">
      Published in <b>Computer Speech &amp; Language,</b> Elsevier&mdash;58 (2019): 216&ndash;230
    </div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span><span class="eq">*</span>,
      Tanvir Ahmed Fuad<span class="eq">*</span>,
      Asif Mahmud,
      and Yllias Chali
    </div>
    <div class="pub-links">
      <a href="https://tafseer-nayeem.github.io/files/CSL_Journal_2019.pdf">Paper</a>
      <a href="https://github.com/tafseer-nayeem/NeuFuse">Code</a>
    </div>
  </div>
</div>

<h2 class="pub-year">2018</h2>

<div class="pub-item">
  <div class="pub-left">
    <a href="http://aclweb.org/anthology/C18-1102"
       aria-label="COLING 2018 — Paraphrastic Sentence Fusion" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/COLING2018-Fusion.png"
        alt="Abstractive Unsupervised Multi-Document Summarization using Paraphrastic Sentence Fusion — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-sienna">COLING 2018</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="http://aclweb.org/anthology/C18-1102">
        Abstractive Unsupervised Multi-Document Summarization using Paraphrastic Sentence Fusion
      </a>
    </h3>
    <div class="pub-meta">
      Published at <b>COLING 2018</b>
      <span class="tag-badge tag-oral" aria-label="Oral presentation">Oral</span>
    </div>
    <div class="pub-award-line">
      <a href="https://coling2018.org/coling-2018-best-papers/" aria-label="Area Chair Favorite Paper Award — COLING 2018 best papers"
         target="_blank" rel="noopener noreferrer">
      <span class="award-badge award-outline-gold"> 🏆 Area Chair Favorite Paper Award </span>
      </a>
  </div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span>,
      Tanvir Ahmed Fuad,
      and Yllias Chali
    </div>
    <div class="pub-links">
      <a href="https://tafseer-nayeem.github.io/files/COLING_2018_Presentation.pdf">Slides</a>
      <a href="https://github.com/tafseer-nayeem/NeuFuse">Code</a>
      <a href="https://twitter.com/mtnayeem/status/1007565988047409152?s=20">Twitter Thread</a>
    </div>
  </div>
</div>   

<h2 class="pub-year">2017</h2>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://dl.acm.org/citation.cfm?id=3133106"
       aria-label="Paraphrastic Fusion for Abstractive Multi-Sentence Compression Generation (CIKM 2017)"
       class="thumb-wrap">
      <!-- replace src if your thumbnail path differs -->
      <img
        src="https://tafseer-nayeem.github.io/images/publication/CIKM2017-ParaphrasticFusion.png"
        alt="Paraphrastic Fusion for Abstractive Multi-Sentence Compression Generation — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-green">CIKM 2017</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://dl.acm.org/citation.cfm?id=3133106">
        Paraphrastic Fusion for Abstractive Multi-Sentence Compression Generation
      </a>
    </h3>
    <div class="pub-meta">Published at <b>ACM CIKM 2017</b></div>
    <div class="pub-award-line">
      <a href="https://sigir.org/general-information/travel-grants/" aria-label="ACM SIGIR Student Travel Grant">
        <span class="award-badge award-outline-gold"> 🏆 ACM SIGIR Student Travel Grant </span>
      </a>
    </div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span> and Yllias Chali
    </div>
    <div class="pub-links">
      <a href="https://tafseer-nayeem.github.io/files/CIKM_2017_paper.pdf">Paper</a>
    </div>
  </div>
</div>

<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/I17-2071" aria-label="IJCNLP 2017 — Submodular + Compression + Merging" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/IJCNLP2017-Submodular.png"
        alt="Towards Abstractive Multi-Document Summarization Using Submodular Function-Based Framework, Sentence Compression and Merging — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <span class="conf-badge-blue">IJCNLP 2017</span>
  </div>
  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/I17-2071">
        Towards Abstractive Multi-Document Summarization Using Submodular Function-Based Framework, Sentence Compression and Merging
      </a>
    </h3>
    <div class="pub-meta">Published at <b>IJCNLP 2017</b></div>
    <div class="pub-authors">
      Yllias Chali,
      Moin Mahmud Tanvee,
      and <span class="me">Mir Tafseer Nayeem</span>
    </div>
    <div class="pub-links">
      <a href="https://aclanthology.org/I17-2071">Paper</a>
    </div>
  </div>
</div>


<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/W17-2407" aria-label="Extract with Order (ACL 2017 Workshop, Oral)" class="thumb-wrap">
      <img
        src="https://tafseer-nayeem.github.io/images/publication/ACL2017-ExtractWithOrder.png"
        alt="Extract with Order for Coherent Multi-Document Summarization — thumbnail"
        loading="lazy" decoding="async"
        sizes="(max-width: 640px) 100vw, var(--thumb-w)">
    </a>
    <div class="badge-stack">
      <span class="conf-badge-navy">ACL 2017</span>
      <span class="sub-badge sub-badge-workshop" aria-label="Workshop">Workshop</span>
    </div>
  </div>
  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://aclanthology.org/W17-2407">
        Extract with Order for Coherent Multi-Document Summarization
      </a>
    </h3>
    <div class="pub-meta">
      Published at <b>ACL 2017</b> (Workshop)
      <span class="tag-badge tag-oral" aria-label="Oral presentation">Oral</span>
    </div>
    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span> and Yllias Chali
    </div>
    <div class="pub-links">
      <a href="https://tafseer-nayeem.github.io/files/ACL_Workshop_2017_Presentation.pdf">Slides</a>
    </div>
  </div>
</div>

<style>
.blinking {
    color: red;           /* Set the color of the symbol */
    font-weight: bold;    /* Make it bold */
    font-size: 1.2em;     /* Adjust size as needed */
    margin-right: 8px;    /* Adds space between symbol and title */
    vertical-align: middle; /* Aligns symbol with text */
    animation: blinker 2s linear infinite;
}

@keyframes blinker {
    50% {
        opacity: 0;
    }
}
</style>


<!--

## 2014
<hr style="border: 1px solid #ddd;" />

![ICCI\*CC 2014](https://img.shields.io/badge/ICCI*CC%202014-007BB5?style=for-the-badge)
* [**Design of a Human Interaction Proof (HIP) using Human Cognition in Contextual Natural Conversation**](https://ieeexplore.ieee.org/document/6921454/) <br/>
📰 <span style ="color:Maroon"> Proceedings of **IEEE ICCI\*CC 2014** </span> <br/>
👨‍💻 **Mir Tafseer Nayeem**, Md Mamunur Rashid Akand, Nazmus Sakib, and Md. Wasi Ul Kabir <br/>
👉 [![Paper](https://img.shields.io/badge/Paper-D3D3D3)](https://tafseer-nayeem.github.io/files/IEEE_ICCICC14_paper.pdf)

-----------

* [**Human Cognition in Automated Turing Test Design**](https://dl.acm.org/citation.cfm?id=2807119) <br/>
📰 <span style ="color:Maroon"> International Journal of Software Science and Computational Intelligence (**IJSSCI**) 6.4 (2014): 1-19. </span> <br/>
👨‍💻 **Mir Tafseer Nayeem**, Md Mamunur Rashid Akand, Nazmus Sakib, and Md. Wasi Ul Kabir <br/>


## 2012
<hr style="border: 1px solid #ddd;" />

![CSE 2012](https://img.shields.io/badge/CSE%202012-007BB5?style=for-the-badge)
* [**Use of Human Cognition in HIP Design Via EmotIcons to Defend BOT Attacks**](https://ieeexplore.ieee.org/document/6417291/) <br/>
📰 <span style ="color:Maroon"> Proceedings of **IEEE CSE 2012** (Oral) </span> <br/>
👨‍💻 **Mir Tafseer Nayeem**, Md. Saddam Hossain Mukta, Samsuddin Ahmed, and Md. Mahbubur Rahman <br/>
👉 [![Paper](https://img.shields.io/badge/Paper-D3D3D3)](https://tafseer-nayeem.github.io/files/IEEE_CSE12_paper.pdf)


[comment]: # <br/>


# Favorite Quotes
-------------------
&nbsp; -- For space

[**Back to Top**](#)

<img src="https://tafseer-nayeem.github.io/images/quotes.png" alt="Favorite Quotes"
	title="Favorite Quotes" width="840" height="70">

*Image Source: Google Image Search*

-->

----------------------------------------

[**Back to Top**](#)

