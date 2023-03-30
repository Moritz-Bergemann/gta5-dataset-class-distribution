Class distribution of the GTA5 dataset, retrieved from [Playing for Data: Ground Truth from Computer Games](https://arxiv.org/abs/1608.02192).

The distribution was produced using the attached script, [`class_count.py`](./class_count.py). Ensure the `DATASET_LABELS_PATH` constant in the script is set appropriately before running.

## Distribution
| Train Label | Name(s)       | # Pixels    | Proportion (%) | RGB           | Class (full train set) |
|-------------|---------------|-------------|----------------|---------------|------------------------|
|           0 | road          | 16099193283 |          32.10 | (128, 64,128) |                      7 |
|           1 | sidewalk      |  4155428633 |           8.29 | (244, 35,232) |                      8 |
|           2 | building      |  8478285320 |          16.91 | ( 70, 70, 70) |                     11 |
|           3 | wall          |   925367586 |           1.85 |  -102,102,156 |                     12 |
|           4 | fence         |   317481282 |           0.63 |  -190,153,153 |                     13 |
|           5 | pole          |   531401266 |           1.06 |  -153,153,153 |                     17 |
|           6 | traffic light |    67288808 |           0.13 | (250,170, 30) |                     19 |
|           7 | traffic sign  |    40463971 |           0.08 | (220,220,  0) |                     20 |
|           8 | vegetation    |  3810296251 |           7.60 | (107,142, 35) |                     21 |
|           9 | terrain       |  1074861777 |           2.14 |  -152,251,152 |                     22 |
|          10 | sky           |  6784666433 |          13.53 |   -70,130,180 |                     23 |
|          11 | person        |   181828023 |           0.36 | (220, 20, 60) |                     24 |
|          12 | rider         |    15321782 |           0.03 | (255,  0,  0) |                     25 |
|          13 | car           |  1259269812 |           2.51 | (  0,  0,142) |                     26 |
|          14 | truck         |   564950248 |           1.13 | (  0,  0, 70) |                     27 |
|          15 | bus           |   184638969 |           0.37 | (  0, 60,100) |                     28 |
|          16 | train         |    32522117 |           0.06 | (  0, 80,100) |                     31 |
|          17 | motorcycle    |    15799033 |           0.03 | (  0,  0,230) |                     32 |
|          18 | bicycle       |     2718199 |           0.01 | (119, 11, 32) |                     33 |
|         255 | void          |  5605086111 |          11.18 | -             | -                      |
| Total       | -             | 50146868904 |            100 | -             | -                      |