# Factual News Graph (FANG) - Reproducibility Experiments
**Note:** This repository is a fork of the [FANG](https://github.com/nguyenvanhoang7398/FANG) code repository. The only difference to that repository (in the state it was in as of January 29, 2022) is the additional `reproducibility-experiments` folder containing logfiles/scripts documenting attempts to reproduce the results reported in the FANG [paper](https://arxiv.org/abs/2008.07939). All parts of the README from [Factual News Graph (FANG)](#factual-news-graph-fang) onwards are also same as the original README.
## Links
* [Notebook for (trying to) execute FANG on Google Colab runtime with GPU](https://colab.research.google.com/drive/1P-uTqataDAZ0OoTfzb3FxvQUjxhxkNQL?usp=sharing)

## Content of `reproducibility-experiments`
 * `local-machine-logs`: contains logs and related information for the attempts to fit FANG and baseline models on local machines (unfortunately, not all sessions were logged)
 * `colab-notebooks`: contains a notebook detailing the setup used to get FANG code running on Google Colab's VMs (`FANG_Google_Colab.ipynb`) and a notebook documenting a successful fit of the GCN baseline model, including test set result statistics  (`old_FANG_Google_Colab_with-GCN-results.ipynb` - see output of second code cell after step 6). For the latter, the created GCN models are also included in a ZIP archive.
 * `scripts`: contains the script used to shuffle the train, validation, and test splits of the dataset

# Factual News Graph (FANG)
This is the implementation of FANG - a graph representation learning framework for fake news detection. 

For more details, please refer to our paper.
[Van-Hoang Nguyen, Kazunari Sugiyama, Preslav Nakov, Min-Yen Kan, FANG: Leveraging Social Context for Fake News Detection Using Graph Representation (CIKM 2020)](https://dl.acm.org/doi/10.1145/3340531.3412046)


## Installation
```bash
conda env create -f environment. yml 
```

## Requirements
### Packages
* conda 4.8.2
* python 3.7.7
* torch 1.5.1
* tensorboard 1.15.0
### Hardware
* GPU: Titan RTX 24220MiB total memory
* CPU: 16GiB total memory

## Data
We provided the processed data used in our experiments in `data/news_graph`

| Description | File name | Format |
| ----- | ----- | ----- |
| Social entities | entities.txt | |
| Social entity's features | entity_features.tsv | entity_id [tab] feature_1_value [tab] feature_2_value... |
| User-news support interactions with negative sentiment | support_negative.tsv | user_id [tab] news_id [tab] seconds_since_publication |
| User-news support interactions with neutral sentiment | support_neutral.tsv | user_id [tab] news_id [tab] seconds_since_publication |
| User-news deny interactions | deny.tsv | user_id [tab] news_id [tab] seconds_since_publication |
| User-news report interactions | report.tsv | user_id [tab] news_id [tab] seconds_since_publication |
| News information | news_info.tsv | news_id [tab] labels [tab] title |
| Indicator whether certain pair of entities should be closed or far, only used for evaluation, not for as labels | rep_entities.tsv | entity_1_id [tab] entity_2_id [tab] closed/far [tab] stance |
| Source-source citation interactions | source_citation.tsv | source_1_id [tab] source_2_id |
| Source-news publication interactions | source_publication.tsv | source_id [tab] news_id |
| User-user friendship interactions | user_relationships.tsv | user_1_id [tab] user_2_id |
| Train-val-test splits (representative of a fold) | train_test_{training percentage}.json | {"train": train_entities, "val": validate_entities, "test": test_entities} | 

Unprocessed data, including news and users who engage them can be found in `data/fang_fake.csv` and `data/fang_real.csv`.

## Run Graph Learning Frameworks
```
usage: run_graph.py [-h] [-t TASK] [-m MODEL] [-p PATH] [--percent PERCENT]
                    [--temporal] [--use-stance] [--use-proximity]
                    [--epochs EPOCHS] [--attention]
                    [--pretrained_dir PRETRAINED_DIR]
                    [--pretrained_step PRETRAINED_STEP]

Graph Learning

optional arguments:
  -h, --help            show this help message and exit
  -t TASK, --task TASK  task name
  -m MODEL, --model MODEL
                        model name
  -p PATH, --path PATH  path to dataset
  --percent PERCENT
  --temporal            whether to use temporality
  --use-stance          whether to use stance
  --use-proximity       whether to use proximity
  --epochs EPOCHS       number of epochs
  --attention           whether to use attention
  --pretrained_dir PRETRAINED_DIR
                        path to pre-trained model directory
  --pretrained_step PRETRAINED_STEP
                        pre-trained model step
```

Training FANG for `30` epochs at `90%` data with `temporality`, `stance loss` and `proximity loss`.
```
python run_graph.py -t fang -m graph_sage -p data/news_graph --percent 90 --epochs=30 --attention --use-stance --use-proximity --temporal
```

Training GCN baseline for `1000` epochs at `90%` data.
```
python run_graph.py -t news_graph -m gcn -p data/news_graph --percent 90 --epochs=1000
```

## Other resources
* Relation filtering, Stance detection, Sentiment Classification models can be found [here](https://github.com/nguyenvanhoang7398/FANG-helper)
* Social media retriever used to crawl unprocessed data, implemented by Kai Shu et al. can be found [here](https://github.com/KaiDMML/FakeNewsNet/)
* The implementation of GraphSage from which this code was adapted can be found [here](https://github.com/twjiang/graphSAGE-pytorch)

## Cite
Please cite our paper as below if you use this code in your work:

```
@inproceedings{10.1145/3340531.3412046,
author = {Nguyen, Van-Hoang and Sugiyama, Kazunari and Nakov, Preslav and Kan, Min-Yen},
title = {FANG: Leveraging Social Context for Fake News Detection Using Graph Representation},
year = {2020},
isbn = {9781450368599},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3340531.3412046},
doi = {10.1145/3340531.3412046},
abstract = {We propose Factual News Graph (FANG), a novel graphical social context representation and learning framework for fake news detection. Unlike previous contextual models that have targeted performance, our focus is on representation learning. Compared to transductive models, FANG is scalable in training as it does not have to maintain all nodes, and it is efficient at inference time, without the need to re-process the entire graph. Our experimental results show that FANG is better at capturing the social context into a high fidelity representation, compared to recent graphical and non-graphical models. In particular, FANG yields significant improvements for the task of fake news detection, and it is robust in the case of limited training data. We further demonstrate that the representations learned by FANG generalize to related tasks, such as predicting the factuality of reporting of a news medium.},
booktitle = {Proceedings of the 29th ACM International Conference on Information &amp; Knowledge Management},
pages = {1165–1174},
numpages = {10},
keywords = {representation learning, fake news, social networks, graph neural networks, disinformation},
location = {Virtual Event, Ireland},
series = {CIKM '20}
}
```
