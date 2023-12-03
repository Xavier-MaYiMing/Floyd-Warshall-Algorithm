#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/4 21:46
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : Floyd_Warshall.py
# @Statement : The Floyd-Warshall algorithm for the shortest path problem
# @Reference : Floyd R W. Algorithm 97: shortest path[J]. Communications of the ACM, 1962, 5(6): 345.


def main(network):
    """
    The main function of the Floyd-Warshall algorithm
    :param network: {node1: {node2: length, node3: length, ...}, ...}
    :return:
    """
    # Step 1. Initialization
    nn = len(network)  # node number
    inf = float('inf')
    dis_mat = [[inf for _ in range(nn)] for _ in range(nn)]
    path_mat = [[[] for _ in range(nn)] for _ in range(nn)]
    for node1 in range(nn):
        dis_mat[node1][node1] = 0
        path_mat[node1][node1] = [node1]
        for node2 in network[node1].keys():
            dis_mat[node1][node2] = network[node1][node2]
            path_mat[node1][node2] = [node1, node2]

    # Step 2. The main loop:
    for k in range(nn):
        for i in range(nn):
            for j in range(nn):
                if dis_mat[i][j] > dis_mat[i][k] + dis_mat[k][j]:
                    dis_mat[i][j] = dis_mat[i][k] + dis_mat[k][j]
                    path_mat[i][j] = path_mat[i][k].copy()
                    path_mat[i][j].pop()
                    path_mat[i][j].extend(path_mat[k][j])
    return {'path': path_mat, 'length': dis_mat}


if __name__ == '__main__':
    test_network = {
        0: {1: 62, 2: 44, 3: 67},
        1: {0: 62, 2: 32, 4: 52},
        2: {0: 44, 1: 33, 3: 32, 4: 52},
        3: {0: 67, 2: 32, 4: 54},
        4: {1: 52, 2: 52, 3: 54}
    }
    print(main(test_network))
