# User-friendly extensions to the Disease Ontology

This repository creates user-friendly extensions to the [Disease Ontology](http://disease-ontology.org "Disease Ontology Homepage") (DO) [[1](https://doi.org/10.1093/nar/gkr972 "Disease Ontology: a backbone for disease semantic integration")]. Simple TSV files are extracted from the OBO-formatted ontology including datasets for term names, cross-references, and subsumption relationships. Additionally, a slim term set is extracted, which we use for our [drug repurposing research](https://doi.org/10.15363/thinklab.4, "Thinklab · Repurposing drugs on a hetnet").

## Notebooks

[`DO-xrefs.ipynb`](DO-xrefs.ipynb) extracts cross-references from `download/HumanDO.obo` and produces easy-to-read mappings files. `data/xref-prop.tsv` contains propagated cross-references, so that for example xrefs to *relapsing remitting multiple sclerosis* would be transmitted to *multiple sclerosis*.

[`slim.ipynb`](slim.ipynb) reads [DO Slim](https://doi.org/10.15363/thinklab.d44#144 "Creating a slim DO") terms and generates slim-specific datasets.

## Directories

`IGS_scripts` contains the [scripts](https://github.com/IGS/disease-ontology/tree/master/scripts) from the `IGS/disease-ontology` [repo](https://github.com/IGS/disease-ontology). These scripts were converted into python 3 and a few conversion errors were manually fixed.

[`download`](download) contains a subversion checkout of the master DO.

[`data`](data) contains created datasets which include:

+ [`term-names.tsv`](data/term-names.tsv) — names including synonyms for DO terms
+ [`xrefs.tsv`](data/xrefs.tsv) — cross-references to external disease vocabularies
+ [`xrefs-prop.tsv`](data/xrefs-prop.tsv) — cross-references where diseases inherit all cross-references of the diseases they subsume
+ [`slim-terms.tsv`](data/slim-terms.tsv) — a ([semi-manually created](http://doi.org/10.15363/thinklab.d44#144 "Creating a slim DO")) slim term set referred to as DO Slim
+ [`slim-terms-prop.tsv`](data/slim-terms-prop.tsv) — all subsume relationships for DO Slim
+ [`xrefs-slim.tsv`](data/xrefs-slim.tsv) — cross-references to external disease vocabularies for slim terms
+ [`xrefs-prop-slim.tsv`](data/xrefs-prop-slim.tsv) — cross-references for slim terms where diseases inherit all cross-references of the diseases they subsume.

## License

Disease Ontology content and derivatives are licensed under [CC-BY 3.0](https://creativecommons.org/licenses/by/3.0/ "Creative Commons Attribution 3.0 Unported"). All original content is licensed under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/ "CC0 1.0 Universal: Public Domain Dedication").
