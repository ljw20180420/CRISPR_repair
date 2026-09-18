# TODO

# Idea

- CRISPR_repair
  - 延切化简
  - 用ref的后缀序列计算它与当前query延伸末端的微同源
  - 解耦合两端query的依赖，从而将复杂度从O3降低到O2
  - 简单的用repeat匹配连接两段嵌合匹配(一种简单结构的图匹配)
  - 类比editing距离和affine gap距离，定义repair距离

- No penalty is necessary for melting. Penalty for annealing is enough to prevent repeated annealing and melting.
- Assume single 3' end elongation.
- Cis forward score degrades after across the cleveage site.

# Limitation

- Not include temporary extension.
- Not allow trans forward annealing to elongation both 3' end. This is rare however.
