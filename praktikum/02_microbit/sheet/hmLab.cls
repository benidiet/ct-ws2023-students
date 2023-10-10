\ProvidesClass{hmLab}
\NeedsTeXFormat{LaTeX2e}

\LoadClassWithOptions{scrartcl}
\ProcessOptions\relax

\RequirePackage{graphicx}
\RequirePackage[utf8]{inputenc}

\newcommand{\course}[1]{\def\@course{#1}}%
\newcommand{\semester}[1]{\def\@semester{#1}}%
\newcommand{\labno}[1]{\def\@labno{#1}}%

\def\@title{\includegraphics[height=1.5cm]{HM_Schriftzug_Logo_rot_RGB} \\[\bigskipamount]
  \@course, \@semester}
\def\@date{}

\addtokomafont{subtitle}{\Large}

\let\oldsubtitle\subtitle
\renewcommand{\subtitle}[1]{\oldsubtitle{%
    Praktische Übung \@labno: #1}}

\renewcommand\thesubsection{Aufgabe~\@labno.\arabic{subsection}:}
\newcommand{\excercise}{\subsection}

\RequirePackage[shortlabels]{enumitem}
\RequirePackage{lastpage}

\RequirePackage{scrlayer-scrpage}
\cfoot*{Seite \thepage\ / \pageref*{LastPage}}
\chead{\@course\ -- \@semester, Praktische Übung \@labno}

\RequirePackage{xcolor}
\RequirePackage{listings}
\RequirePackage{hyperref}
\RequirePackage{tabularx}
