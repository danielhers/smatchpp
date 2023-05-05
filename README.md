# SMATCH++

Contains standardized and optimal Smatch solving.

## Example configurations

### Recommended for average case: ILP alignment, dereification, corpus metrics and confidence intervals

- Efficiency: + 
- Optimality: +++
- Graph standardization: ++ 

```
python smatchpp/main.py -a <amrs1> \
			-b <amrs2> \
			-solver ilp \
			-edges dereify \
			-score_dimension main \
			-score_type micromacro \
			-log_level 20 \
			--bootstrap \
			--remove_duplicates
```

### Hill-climber alignment, dereification, corpus metrics and confidence intervals

- Efficiency: ++ 
- Optimality: +
- Graph standardization: ++

```
python smatchpp/main.py -a <amrs1> \
			-b <amrs2> \
			-solver hillclimber \
			-edges dereify \
			-score_dimension main \
			-score_type micromacro \
			-log_level 20 \
			--bootstrap \
			--remove_duplicates
```


### Fast ILP with graph compression, corpus metrics and confidence intervals

- Efficiency: ++ 
- Optimality: +++
- Graph standardization: + 

```
python smatchpp/main.py -a <amrs1> \
			-b <amrs2> \
			-solver ilp \
			-edges dereify \
			-score_dimension main \
			-score_type micromacro \
			-log_level 20 \
			--bootstrap \
			--remove_duplicates \
			--lossless_graph_compression
```

### ILP with reification, corpus metrics and confidence intervals

- Efficiency: -
- Optimality: +++
- Graph standardization: +++

```
python smatchpp/main.py -a <amrs1> \
			-b <amrs2> \
			-solver ilp \
			-edges reify \
			-score_dimension main \
			-score_type micromacro \
			-log_level 20 \
			--bootstrap \
			--remove_duplicates \
			--lossless_graph_compression
```

### ILP alignment, corpus sub-aspect metrics and confidence intervals

Efficiency: + 
Optimality: +++
Graph standardization: + 

```
python smatchpp/main.py -a <amrs1> \
			-b <amrs2> \
			-solver ilp \
			-edges reify \
			-score_dimension all-multialign \
			-score_type micromacro \
			-log_level 20 \
			--bootstrap \
			--remove_duplicates \
			--lossless_graph_compression
```

### Other configurations

See

```
python smatchpp/main.py --help
```

## Additional functionality

### Custom triple matching

Can be implemented in `score.py`

### Changing subgraph metrics

See `subgraph_extraction.py` 

## Pip install

coming.

## Citation

If you like the project, consider citing

```
@inproceedings{opitz-2023-smatch,
    title = "{SMATCH}++: Standardized and Extended Evaluation of Semantic Graphs",
    author = "Opitz, Juri",
    booktitle = "Findings of the Association for Computational Linguistics: EACL 2023",
    month = may,
    year = "2023",
    address = "Dubrovnik, Croatia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-eacl.118",
    pages = "1595--1607"
}
```
