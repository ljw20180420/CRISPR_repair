# TODO

# Idea

- write a O(N^3) version as control, then implement O(N^2) version

- 延切化简
- 用ref的后缀序列计算它与当前query延伸末端的微同源
- 解耦合两端query的依赖，从而将复杂度从O3降低到O2
- 简单的用repeat匹配连接两段嵌合匹配(一种简单结构的图匹配)
- 类比editing距离和affine gap距离，定义repair距离

- 下限不减，螺旋升天
- 通过比较开关第四种snap back前后的匹配score来证明其存在性
- 延切定律AB和BA作为锚定点
- AB之后不能有A切，至多有一个B切
- BA类似
- 不失一般性，A/B延长部分不会被切，除非其被另一方用于延长，以此类推，总有不被切的延长
- title: a method to parse CRISPR repair result

- No penalty is necessary for melting. Penalty for annealing is enough to prevent repeated annealing and melting.
- Assume single 3' end elongation.
- Cis forward score degrades after across the cleveage site.

# Limitation

- Not include temporary extension.
- Not allow trans forward annealing to elongation both 3' end. This is rare however.
