---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

**Full List:** [ [**Google Scholar**](https://scholar.google.com/citations?hl=en&user=qoeylgEAAAAJ&view_op=list_works&sortby=pubdate) \| [**ACL Anthology**](https://aclanthology.org/people/m/mir-tafseer-nayeem/) \| [**DBLP**](https://dblp.org/pid/125/2693.html) ]

<span style ="color:BlueViolet"> [\**indicates equal contribution*]</span>

<!-- [comment]: # \| [**Favorite Quotes**](#favorite-quotes) -->

[comment]: # <br/>

<!--
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

/* Academic, restrained outline gold (recommended default) */
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

.conf-badge-blue{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:8px 14px;
    min-width: var(--badge-w);
    line-height:1;
    border-radius:999px;
    font-size: var(--font-badge);
    font-weight:700; letter-spacing:.3px;
    text-transform:uppercase;
    color:#fff; background:#4682B4;
    white-space:nowrap;
    transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
  }
.conf-badge-blue:hover{
    transform: translateY(-1px);
    box-shadow:0 6px 16px rgba(70,130,180,.25);
    filter:saturate(1.05);
  }

.conf-badge-teal{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:8px 14px;
    min-width: var(--badge-w);
    line-height:1;
    border-radius:999px;
    font-size: var(--font-badge);
    font-weight:700; letter-spacing:.3px;
    text-transform:uppercase;
    color:#fff; background:#0F766E;
    white-space:nowrap;
    transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
  }
.conf-badge-teal:hover{
    transform: translateY(-1px);
    box-shadow:0 6px 16px rgba(15,118,110,.25);
    filter:saturate(1.05);
  }

.conf-badge-green{
  display:inline-flex;align-items:center;justify-content:center;
  padding:8px 14px;min-width:var(--badge-w);line-height:1;border-radius:999px;
  font-size:var(--font-badge);font-weight:700;letter-spacing:.3px;text-transform:uppercase;
  color:#fff;background:#28a745;white-space:nowrap;
  transition:transform .18s ease,box-shadow .18s ease,filter .18s ease;
  }
.conf-badge-green:hover{
    transform:translateY(-1px);box-shadow:0 6px 16px rgba(40,167,69,.25);filter:saturate(1.05);
  }

  .conf-badge-navy{
    display:inline-flex; align-items:center; justify-content:center;
    padding:8px 14px; min-width: var(--badge-w, 120px);
    line-height:1; border-radius:999px;
    font-size: var(--font-badge, 12px); font-weight:700; letter-spacing:.3px;
    text-transform:uppercase; color:#fff; background:#242D8C; /* NAACL navy */
    white-space:nowrap;
    transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
  }
  .conf-badge-navy:hover{
    transform: translateY(-1px);
    box-shadow:0 6px 16px rgba(36,45,140,0.28);
    filter:saturate(1.05);
  }

.conf-badge-sienna{
  display:inline-flex; align-items:center; justify-content:center;
  padding:8px 14px; min-width: var(--badge-w, 120px);
  line-height:1; border-radius:999px;
  font-size: var(--font-badge, 12px); font-weight:700; letter-spacing:.3px;
  text-transform:uppercase; color:#fff; background:#A0522D; /* Sienna (academic brown) */
  white-space:nowrap;
  transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
}
.conf-badge-sienna:hover{
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(160, 82, 45, 0.28); /* tinted shadow for #df7d4fff */
  filter: saturate(1.05);
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
</style>

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
      Published at <b>EMNLP 2025</b>
      <span class="tag-badge tag-oral" aria-label="Oral presentation">Oral</span>
    </div>
    <div class="pub-authors">Tong Bao, <span class="me">Mir Tafseer Nayeem</span>, Davood Rafiei, and Chengzhi Zhang</div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2508.17647">Paper</a>
      <a href="https://github.com/tongbao96/SurveyGen">Code</a>
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
    <div class="pub-meta">Published at <b>EMNLP 2025</b></div>
    <div class="pub-authors">
      Ridwan Mahbub*,
      Mohammed Saidul Islam*,
      <span class="me">Mir Tafseer Nayeem</span>,
      Md Tahmid Rahman Laskar,
      Mizanur Rahman,
      Shafiq Joty,
      and Enamul Hoque
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2508.09450">Paper</a>
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
    <div class="pub-meta">Published at <b>EMNLP 2025</b> (Industry Track)</div>
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
    <span class="conf-badge-green">VIS 2025</span>
  </div>

  <div class="pub-right">
    <h3 class="pub-title">
      <a href="https://arxiv.org/abs/2508.09716">
        The Perils of Chart Deception: How Misleading Visualizations Affect Vision-Language Models
      </a>
    </h3>

    <div class="pub-meta">Published at <b>VIS 2025</b></div>
    <div class="pub-award-line">
      <span class="award-badge award-outline-gold" aria-label="Best short paper award">
        🏆 Best Short Paper Award
      </span>
    </div>

    <div class="pub-authors">
      Ridwan Mahbub, Mohammed Saidul Islam, Md Tahmid Rahman Laskar,
      Mizanur Rahman, <span class="me">Mir Tafseer Nayeem</span>, and Enamul Hoque
    </div>

    <div class="pub-links">
      <a href="https://arxiv.org/abs/2508.09716">Paper</a>
      <a href="https://github.com/vis-nlp/visDeception">Code</a>
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

    <div class="pub-meta">Published at <b>ACL 2025</b> (Industry Track)</div>

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
    <div class="pub-meta">Published at <b>NAACL 2025</b> (Industry Track)</div>
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

<div class="pub-item">
  <div class="pub-left">
    <a href="https://aclanthology.org/2024.emnlp-main.277/" aria-label="KidLM (EMNLP 2024)" class="thumb-wrap">
      <!-- replace src if your thumbnail path differs -->
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

    <div class="pub-meta">Published at <b>EMNLP 2024</b></div>

    <!-- Award (uses your .award-badge + .award-outline-gold styles) -->
    <div class="pub-award-line">
      <span class="award-badge award-outline-gold" aria-label="Best resource paper award">
        🏆 Best Resource Paper Award
      </span>
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

    <div class="pub-meta">Published at <b>EMNLP 2024</b> (Findings)</div>

    <div class="pub-authors">
      Mohammed Saidul Islam,
      Raian Rahman,
      Ahmed Masry*,
      Md Tahmid Rahman Laskar*,
      <span class="me">Mir Tafseer Nayeem</span>*,
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

    <div class="pub-meta">Published at <b>ACL 2024</b> (Findings)</div>

    <div class="pub-authors">
      <span class="me">Mir Tafseer Nayeem</span>*,
      Faisal Tareque Shohan*,
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

    <div class="pub-meta">Published in <b>COLING 2024</b></div>

    <div class="pub-authors">
      Mohsinul Kabir<sup>*</sup>,
      Mohammed Saidul Islam<sup>*</sup>,
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



![COLING 2024](https://img.shields.io/badge/COLING%202024-orange?style=for-the-badge)
* [**BenLLM-Eval: A Comprehensive Evaluation into the Potentials and Pitfalls of Large Language Models on Bengali NLP**](https://aclanthology.org/2024.lrec-main.201/)<br/>
📰 <span style ="color:Maroon"> Published in **COLING 2024** </span> <br/>
👨‍💻 Mohsinul Kabir\*, Mohammed Saidul Islam\*, Md Tahmid Rahman Laskar, **Mir Tafseer Nayeem**, M Saiful Bari, and Enamul Hoque <br/>
👉 [![Code](https://img.shields.io/badge/Code-D3D3D3)](https://github.com/saidul-islam98/BenLLMeval) [![Slides](https://img.shields.io/badge/Slides-D3D3D3)](https://tafseer-nayeem.github.io/files/LREC-COLING-2024/LREC-COLING-2024_BenLLM-Eval_presentation.pdf) [![Poster](https://img.shields.io/badge/Poster-D3D3D3)](https://tafseer-nayeem.github.io/files/LREC-COLING-2024/LREC-COLING-2024_BenLLM-Eval_poster.pdf)  


## 2023
<hr style="border: 1px solid #ddd;" />

![CIKM 2023](https://img.shields.io/badge/CIKM%202023-28a745?style=for-the-badge)
* [**Product Entity Matching via Tabular Data**](https://dl.acm.org/doi/10.1145/3583780.3615172)<br/>
📰 <span style ="color:Maroon"> Published in **ACM CIKM 2023** </span> <br/>
👨‍💻 Ali Naeimabadi, **Mir Tafseer Nayeem**, and Davood Rafiei <br/>
👉 [![Paper](https://img.shields.io/badge/Paper-D3D3D3)](https://tafseer-nayeem.github.io/files/CIKM2023/CIKM2023_PEM_paper.pdf) [![Poster](https://img.shields.io/badge/Poster-D3D3D3)](https://tafseer-nayeem.github.io/files/CIKM2023/CIKM2023_PEM_poster.pdf)

-----------

![EACL 2023](https://img.shields.io/badge/EACL%202023-blueviolet?style=for-the-badge)
* [**On the Role of Reviewer Expertise in Temporal Review Helpfulness Prediction**](https://aclanthology.org/2023.findings-eacl.125/)<br/>
📰 <span style ="color:Maroon"> Published in **EACL 2023** (Findings)</span> <br/>
👨‍💻 **Mir Tafseer Nayeem** and Davood Rafiei <br/>
👉 [![Code](https://img.shields.io/badge/Code-D3D3D3)](https://github.com/tafseer-nayeem/RHP) [![Dataset](https://img.shields.io/badge/Dataset-D3D3D3)](https://huggingface.co/datasets/tafseer-nayeem/review_helpfulness_prediction) [![Slides](https://img.shields.io/badge/Slides-D3D3D3)](https://tafseer-nayeem.github.io/files/EACL2023/EACL2023_RHP_presentation.pdf) [![Poster](https://img.shields.io/badge/Poster-D3D3D3)](https://tafseer-nayeem.github.io/files/EACL2023/EACL2023_RHP_poster.pdf)

-----------

![EACL 2023](https://img.shields.io/badge/EACL%202023-blueviolet?style=for-the-badge)
* [**Shironaam: Bengali News Headline Generation using Auxiliary Information**](https://aclanthology.org/2023.eacl-main.4/)<br/>
📰 <span style ="color:Maroon"> Published in **EACL 2023** </span> <br/>
👨‍💻 **Mir Tafseer Nayeem\***, Abu Ubaida Akash\*, Faisal Tareque Shohan, and Tanvir Islam <br/>
👉 [![Code](https://img.shields.io/badge/Code-D3D3D3)](https://github.com/dialect-ai/BenHeadGen) [![Dataset](https://img.shields.io/badge/Dataset-D3D3D3)](https://huggingface.co/datasets/dialect-ai/shironaam) [![Slides](https://img.shields.io/badge/Slides-D3D3D3)](https://tafseer-nayeem.github.io/files/EACL2023/EACL2023_Shironaam_presentation.pdf) [![Poster](https://img.shields.io/badge/Poster-D3D3D3)](https://tafseer-nayeem.github.io/files/EACL2023/EACL2023_Shironaam_poster.pdf)


## 2021
<hr style="border: 1px solid #ddd;" />

![AAAI 2021](https://img.shields.io/badge/AAAI%202021-4682B4?style=for-the-badge)
* [**Simple or Complex? Learning to Predict Readability of Bengali Texts**](https://ojs.aaai.org/index.php/AAAI/article/view/17495)<br/>
📰 <span style ="color:Maroon"> Published in **AAAI 2021** </span> <br/>
👨‍💻 **Mir Tafseer Nayeem\***, Susmoy Chakraborty\*, and Wasi Uddin Ahmad <br/>
👉 [![Paper](https://img.shields.io/badge/Paper-D3D3D3)](https://tafseer-nayeem.github.io/files/AAAI2021/AAAI2021_paper.pdf) [![Code](https://img.shields.io/badge/Code-D3D3D3)](https://github.com/tafseer-nayeem/BengaliReadability) [![Dataset](https://img.shields.io/badge/Dataset-D3D3D3)](https://github.com/tafseer-nayeem/BengaliReadability/tree/main/Data) [![Slides](https://img.shields.io/badge/Slides-D3D3D3)](https://tafseer-nayeem.github.io/files/AAAI2021/AAAI2021_presentation.pdf) [![Poster](https://img.shields.io/badge/Poster-D3D3D3)](https://tafseer-nayeem.github.io/files/AAAI2021/AAAI2021_poster.pdf) [![Demo Video](https://img.shields.io/badge/Demo%20Video-D3D3D3)](https://youtu.be/U05Pf9Y4tCQ) [![X Thread](https://img.shields.io/badge/X%20Thread-D3D3D3)](https://x.com/mtnayeem/status/1334590638105378817)

-----------

![EACL 2021](https://img.shields.io/badge/EACL%202021-blueviolet?style=for-the-badge)
* [**Unsupervised Abstractive Summarization of Bengali Text Documents**](https://www.aclweb.org/anthology/2021.eacl-main.224)<br/>
📰 <span style ="color:Maroon"> Published in **EACL 2021** </span> <br/>
👨‍💻 **Mir Tafseer Nayeem\***, Radia Rayan Chowdhury\*, TT Mim, MSR Chowdhury, and T Jannat <br/>
👉 [![Code](https://img.shields.io/badge/Code-D3D3D3)](https://github.com/tafseer-nayeem/BengaliSummarization) [![Dataset](https://img.shields.io/badge/Dataset-D3D3D3)](https://github.com/tafseer-nayeem/BengaliSummarization/tree/main/Dataset) [![Slides](https://img.shields.io/badge/Slides-D3D3D3)](https://tafseer-nayeem.github.io/files/EACL2021/EACL2021_presentation.pdf) [![Poster](https://img.shields.io/badge/Poster-D3D3D3)](https://tafseer-nayeem.github.io/files/EACL2021/EACL2021_poster.pdf) [![Demo Video](https://img.shields.io/badge/Demo%20Video-D3D3D3)](https://youtu.be/LrnskktiXcg) [![X Thread](https://img.shields.io/badge/X%20Thread-D3D3D3)](https://x.com/mtnayeem/status/1350551479283662848)


## 2019
<hr style="border: 1px solid #ddd;" />

![ECIR 2019](https://img.shields.io/badge/ECIR%202019-28a745?style=for-the-badge)
* [**Neural Diverse Abstractive Sentence Compression Generation**](https://link.springer.com/chapter/10.1007/978-3-030-15719-7_14)<br/>
📰 <span style ="color:Maroon"> Published in **ECIR 2019** </span> <br/>
👨‍💻 **Mir Tafseer Nayeem**, Tanvir Ahmed Fuad, and Yllias Chali <br/>
👉 [![Paper](https://img.shields.io/badge/Paper-D3D3D3)](https://tafseer-nayeem.github.io/files/ECIR_2019_paper.pdf)

-----------

![Computer Speech & Language](https://img.shields.io/badge/Computer%20Speech%20&%20Language-critical?style=for-the-badge)
* [**Neural Sentence Fusion for Diversity Driven Abstractive Multi-Document Summarization**](https://www.sciencedirect.com/science/article/pii/S0885230818303449) <br/>
📰 <span style ="color:Maroon"> Published in **Computer Speech & Language**, Elsevier 58 (2019): 216-230. </span> <br/>
👨‍💻 **Mir Tafseer Nayeem\***, Tanvir Ahmed Fuad\*, Asif Mahmud, and Yllias Chali <br/>
👉 [![Paper](https://img.shields.io/badge/Paper-D3D3D3)](https://tafseer-nayeem.github.io/files/CSL_Journal_2019.pdf) [![Code](https://img.shields.io/badge/Code-D3D3D3)](https://github.com/tafseer-nayeem/NeuFuse)


## 2018
<hr style="border: 1px solid #ddd;" />

![COLING 2018](https://img.shields.io/badge/COLING%202018-orange?style=for-the-badge)
* [**Abstractive Unsupervised Multi-Document Summarization using Paraphrastic Sentence Fusion**](http://aclweb.org/anthology/C18-1102) <br/>
📰 <span style ="color:Maroon"> Published in **COLING 2018** (Oral) </span> <br/>
👨‍💻 **Mir Tafseer Nayeem**, Tanvir Ahmed Fuad, and Yllias Chali <br/>
👉 [![Slides](https://img.shields.io/badge/Slides-D3D3D3)](https://tafseer-nayeem.github.io/files/COLING_2018_Presentation.pdf) [![Twitter Thread](https://img.shields.io/badge/Twitter%20Thread-D3D3D3)](https://twitter.com/mtnayeem/status/1007565988047409152?s=20) <br/>
🏆 [<span style="color:Red"> **Area Chair Favorite Paper Award** </span>](http://coling2018.org/coling-2018-best-papers/) <br/>
<!-- 🏆 [<span style="color:Red"> **Best Paper Nomination** </span>](http://coling2018.org/coling-2018-best-papers/) -->   


## 2017
<hr style="border: 1px solid #ddd;" />

![CIKM 2017](https://img.shields.io/badge/CIKM%202017-28a745?style=for-the-badge)
* [**Paraphrastic Fusion for Abstractive Multi-Sentence Compression Generation**](https://dl.acm.org/citation.cfm?id=3133106) <br/>
📰 <span style ="color:Maroon"> Published in **ACM CIKM 2017** </span> <br/>
👨‍💻 **Mir Tafseer Nayeem** and Yllias Chali <br/>
👉 [![Paper](https://img.shields.io/badge/Paper-D3D3D3)](https://tafseer-nayeem.github.io/files/CIKM_2017_paper.pdf) <br/>
🏆 [<span style="color:Red"> **ACM SIGIR Student Travel Grant** </span>](https://sigir.org/general-information/travel-grants/)

-----------

![IJCNLP 2017](https://img.shields.io/badge/IJCNLP%202017-4682B4?style=for-the-badge)
* [**Towards Abstractive Multi-Document Summarization Using Submodular Function-Based Framework, Sentence Compression and Merging**](http://www.aclweb.org/anthology/I17-2071) <br/>
📰 <span style ="color:Maroon"> Published in **IJCNLP 2017** </span> <br/>
👨‍💻 Yllias Chali, Moin Mahmud Tanvee, and **Mir Tafseer Nayeem** <br/>

-----------

![ACL 2017](https://img.shields.io/badge/ACL%202017-dc3545?style=for-the-badge)
* [**Extract with Order for Coherent Multi-Document Summarization**](http://www.aclweb.org/anthology/W17-2407) <br/>
📰 <span style ="color:Maroon"> Published in **ACL 2017** (Workshop, Oral) </span> <br/>
👨‍💻 **Mir Tafseer Nayeem** and Yllias Chali <br/>
👉 [![Slides](https://img.shields.io/badge/Slides-D3D3D3)](https://tafseer-nayeem.github.io/files/ACL_Workshop_2017_Presentation.pdf)


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

