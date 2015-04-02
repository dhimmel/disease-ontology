# disease-ontology

Code and data for the [Disease Ontology](http://disease-ontology.org/) (DO) [[paper](//dx.doi.org/10.1093/nar/gkr972)].

`DO-xrefs.ipynb` extracts cross-references from `download/HumanDO.obo` and [produces](http://nbviewer.ipython.org/github/dhimmel/disease-ontology/blob/gh-pages/DO-xrefs.ipynb) easy-to-read mappings files. `data/xref-prop.tsv` contains propagated cross-references so that xrefs to *relapsing remitting multiple sclerosis* would be transmitted to *multiple sclerosis*.

`IGS_scripts` contains the [scripts](https://github.com/IGS/disease-ontology/tree/master/scripts) from the `IGS/disease-ontology` [repo](https://github.com/IGS/disease-ontology). These scripts were converted into python 3 and a few conversion errors were manually fixed.

`download` contains a subversion checkout of the master DO.

`data` contains files created by us.

See our project on ThinkLab for more information:
http://thinklab.com/p/rephetio
