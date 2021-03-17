\documentclass{article}

\usepackage{bm}
\DeclareFontFamily{U}{griff}{}
\DeclareFontShape{U}{griff}{m}{n}{<-> s*[2.2] griffm}{}
\DeclareFontShape{U}{griff}{b}{n}{<-> s*[2.2] griffb}{}
\DeclareSymbolFont{griff}{U}{griff}{m}{n}
\SetSymbolFont{griff}{bold}{U}{griff}{b}{n}
\DeclareMathSymbol{\rcurs}{\mathalpha}{griff}{"72}
\DeclareBoldMathCommand{\brcurs}{\rcurs}
\newcommand*\hrcurs{\hat{\brcurs}}

\begin{document}

\[
# Electrodynamics Retarded Fields
<p>It takes time for electromagnetic fields to travel from their source.  We can calculate how electromagnetic fields propagate from a current source by using the equations </p>
  \mathbf{E}(\mathbf{r}) = \frac{1}{4 \pi \epsilon_0} \int\limits_{\mathcal{V}} \frac{\rho(\mathbf{r}')}{\rcurs^2} \hrcurs d \tau'
\]

\end{document}



