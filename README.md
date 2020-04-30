# Run SuSiE Run!
## Hayley Sowards Python Project Spring 2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)

I'm creating a script/package I'm calling Run SuSiE Run. This package has several goals:
1. Allow me and others in my lab to easily pull GWAS summary stats and reference panel data
2. Make a LD (linkage disequilibrium) matrix with the reference panel data
3. Align and clean the summary stats and LD matrix
4. Fine-map the region using 2 different programs:
    - SuSiE, written in R
    - DAP-G, written in C++

*Important Note: This package, when used in it's full extent, references data that is not publicly available*

To access this repository locally, enter the following code into command line:

```
git clone https://github.com/hsowards/project_spring_2020
```

Then open notebooks/RSR.ipynb, which will walk you through the process of finemapping from start to finish.
