# EDA_tools
EDA modules for CSV-like files
This script supports countplots, displots and heatmap.\
I apply the seaborn.displots because seaborn.distplot will be deprecated

## Quick Start
```console
$ python main.py
The number of non-category columns : 4
Non-category columns (including object): ['bill_depth_mm', 'bill_length_mm', 'body_mass_g', 'flipper_length_mm']
The number of non-numeric columns : 3
Non-numeric columns : ['island', 'sex', 'species']
The number of non-category columns : 5
Non-category columns (including object): ['distance', 'mass', 'number', 'orbital_period', 'year']
The number of non-numeric columns : 1
Non-numeric columns : ['method']
The number of non-category columns : 7
Non-category columns (including object): ['alcohol', 'ins_losses', 'ins_premium', 'no_previous', 'not_distracted', 'speeding', 'total']
The number of non-numeric columns : 1
Non-numeric columns : ['abbrev']
Not common columns : ['c3', 'c4', 'c6']
$
```

## Sample Results
![The number of species](https://user-images.githubusercontent.com/56813534/116774064-e17ed700-aa94-11eb-9b6c-f4c9212191c7.png)
![dist_graphDistribution of c5-Count](https://user-images.githubusercontent.com/56813534/116774070-ea6fa880-aa94-11eb-8fcd-58e2ee92f525.png)
![car_crashes_Correlation map](https://user-images.githubusercontent.com/56813534/116774076-f9565b00-aa94-11eb-9b21-45fc4d96d3f6.png)

