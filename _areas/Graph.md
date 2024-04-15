---
layout: page
title: Graph Algorithms
permalink : /research-graph
img: graph.png
importance : 1
---

<div class="area-summary" markdown="1">
NP-hard 그래프 문제들을 대규모 그래프에서 풀 수 있는 세계 최고 성능의 알고리즘들을 개발한다. 대표적인 NP-hard 그래프 문제로는 Subgraph isomorphism이 있다. Subgraph isomorphism은 데이터 그래프에서 쿼리 그래프와 동형(isomorphic)인 부분 그래프(subgraph)를 찾는 문제이다.
- 대용량의 그래프 데이터에 대해서 subgraph isomorphism 문제를 푸는 세계 최고 성능의 알고리즘을 개발함 (Efficient subgraph matching: Harmonizing dynamic programming, adaptive matching order, and failing set together, SIGMOD 2019)
- 대용량의 그래프 데이터에 대해서 subgraph query processing 문제를 푸는 세계 최고 성능의 알고리즘을 개발함 (Versatile Equivalences: Speeding up Subgraph Query Processing and Subgraph Matching, SIGMOD 2021)
</div>

<!-- <style>
ul {
  padding-left: 20px;
}
</style> -->

#### 최근 주요 연구성과
2 papers in SIGMOD, 4 papers in VLDB, 3 papers in ICDE, 1 paper in VLDB Journal
- Subgraph Isomorphism, Subgraph Matching 
  - [VLDB 2023] BICE: Exploring Compact Search Space by Using Bipartite Matching and Cell-Wide Verification
  - [VLDB Journal 2023] Fast subgraph query processing and subgraph matching via static and dynamic equivalences
  - [SIGMOD 2021] Versatile Equivalences: Speeding up Subgraph Query Processing and Subgraph Matching
  - [SIGMOD 2019] Efficient Subgraph Matching: Harmonizing dynamic programming, adaptive matching order, and failing set together
  
- Supergraph Search
  - [VLDB 2020] IDAR: Fast supergraph search using DAG integration

- Continuous Subgraph Matching
  - [ICDE 2024] Time-Constrained Continuous Subgraph Matching Using Temporal Information for Filtering and Backtracking
  - [VLDB 2021] Symmetric Continuous Subgraph Matching with Bidirectional Dynamic Programming

- Graph Isomorphism
  - [ICDE 2021] Scalable graph isomorphism: Combining pairwise color refinement and backtracking via compressed candidate space

- Graph Isomorphism Query Processing
  - [ICDE 2022] Efficient Graph Isomorphism Query Processing using Degree Sequences and Color-Label Distributions

- Subgraph Cardinality Estimation
  - [VLDB 2024] Cardinality Estimation of Subgraph Matching: A Filtering-Sampling Approach