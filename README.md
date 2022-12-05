### Floyd-Warshall Algorithm

##### Reference: Floyd R W. Algorithm 97: shortest path[J]. Communications of the ACM, 1962, 5(6): 345.

The Floyd-Warshall Algorithm for the shortest path problem

| Variables | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| network   | Dictionary, {node1: {node2: length, node3: length, ...}, ...} |
| nn        | The number of nodes                                          |
| dis_mat   | List, dis_mat\[i\]\[j\] denotes the length of the shortest path from node i to node j |
| path_mat  | List, path_mat\[i\]\[j\] denotes the shortest path from node i to node j |

#### Example

![](https://github.com/Xavier-MaYiMing/Floyd-Warshall-Algorithm/blob/main/SPP_example.png)

```python
if __name__ == '__main__':
    test_network = {
        0: {1: 62, 2: 44, 3: 67},
        1: {0: 62, 2: 32, 4: 52},
        2: {0: 44, 1: 33, 3: 32, 4: 52},
        3: {0: 67, 2: 32, 4: 54},
        4: {1: 52, 2: 52, 3: 54}
    }
    print(main(test_network))
```

##### Output

```python
{
    'path': [
        [[0], [0, 1], [0, 2], [0, 3], [0, 2, 4]], 
        [[1, 0], [1], [1, 2], [1, 2, 3], [1, 4]], 
        [[2, 0], [2, 1], [2], [2, 3], [2, 4]], 
        [[3, 0], [3, 2, 1], [3, 2], [3], [3, 4]], 
        [[4, 2, 0], [4, 1], [4, 2], [4, 3], [4]]
    ], 
    'length': [
        [0, 62, 44, 67, 88], 
        [62, 0, 32, 65, 52], 
        [44, 33, 0, 32, 52], 
        [67, 64, 32, 0, 54], 
        [104, 52, 52, 54, 0]
    ]
}
```

