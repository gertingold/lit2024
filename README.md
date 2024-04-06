# lit2024
LIT 2024: Bücher mit Code online publizieren

Vortrag beim Linux-Infotag 2023 am 29.4.2023 in Augsburg.

Schon seit einigen Jahren erfreuen sich [Jupyter-Notebooks](https://jupyter.org) großer Beliebtheit, da sie es erlauben, Code und andere Inhalte wie Text oder Multimediaelemente zu integrieren. Damit ergeben sich interessante Möglichkeiten vor allem im Bereich der Datenanalyse, aber auch für die Lehre an Schule und Hochschule. Gerade im zweiten Fall, aber nicht nur dort, bietet es sich an, Jupyter-Notebooks sowohl direkt in der Lehre zu verwenden als auch als Basis zur Publikation des Lehrmaterials heranzuziehen und idealerweise frei zugänglich zu machen. Dabei kann der Ausgangspunkt in einem oder mehreren Jupyter-Notebooks bestehen. Alternativ kann man das Lehrmaterial in Markdown verfassen und mit Hilfe von [jupytext](https://jupytext.readthedocs.io/en/latest/index.html) in Jupyter-Notebooks umwandeln. Es ist dann auch sehr leicht möglich, das Material in ansprechender Weise online zu publizieren. Wir werden das Vorgehen unter Verwendung von [Jupyter Book](https://jupyterbook.org) zeigen, mit dessen Hilfe beispielsweise das [Material eines Python-Kurses](https://gertingold.github.io/epriprog) veröffentlicht wurde. Wir werden abschließend noch eine auf Javascript basierende Weiterentwicklung für das elektronische Publizieren ansprechen.

## Ausführen der Präsentation

Für die Präsentation wird [Slidev](https://sli.dev/) verwendet. Die Präsentation lässt sich folgendermaßen starten:

- `npm install`
- `npm run dev`
- gehe nach http://localhost:3030
