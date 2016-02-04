# User-friendly extensions to the Disease Ontology

Code and data for the [Disease Ontology](http://disease-ontology.org/) (DO) [[1](https://doi.org/10.1093/nar/gkr972)].

[`DO-xrefs.ipynb`](DO-xrefs.ipynb) extracts cross-references from `download/HumanDO.obo` and produces easy-to-read mappings files. `data/xref-prop.tsv` contains propagated cross-references, so that for example xrefs to *relapsing remitting multiple sclerosis* would be transmitted to *multiple sclerosis*.

`IGS_scripts` contains the [scripts](https://github.com/IGS/disease-ontology/tree/master/scripts) from the `IGS/disease-ontology` [repo](https://github.com/IGS/disease-ontology). These scripts were converted into python 3 and a few conversion errors were manually fixed.

[`download`](download) contains a subversion checkout of the master DO.

[`data`](data) contains files created by us.

See our project on ThinkLab for more information:
http://thinklab.com/p/rephetio

## License

Disease Ontology content and derivatives are licensed under [CC-BY 3.0](https://creativecommons.org/licenses/by/3.0/ "Creative Commons Attribution 3.0 Unported"). All original content is licensed under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/ "CC0 1.0 Universal: Public Domain Dedication").
