import os

import pandas as pd
import numpy as np

DATA_PATH = "./ml-latest-small/ratings.csv"
CACHE_DIR = "./cache/"


def load_data(data_path):
    '''
    加载数据
    :param data_path: 数据集路径
    :param cache_path: 数据集缓存路径
    :return: 用户-物品评分矩阵
    '''
    # 数据集缓存地址
    cache_path = os.path.join(CACHE_DIR, "ratings_matrix.cache")

    print("开始加载数据集...")
    if os.path.exists(cache_path):  # 判断是否存在缓存文件
        print("加载缓存中...")
        ratings_matrix = pd.read_pickle(cache_path)
        print("从缓存加载数据集完毕")
    else:
        print("加载新数据中...")
        # 设置要加载的数据字段的类型
        dtype = {"userId": np.int32, "movieId": np.int32, "rating": np.float32}
        # 加载数据，我们只用前三列数据，分别是用户ID，电影ID，已经用户对电影的对应评分
        ratings = pd.read_csv(data_path, dtype=dtype, usecols=range(3))
        # 透视表，将电影ID转换为列名称，转换成为一个User-Movie的评分矩阵
        ratings_matrix = ratings.pivot_table(index=["userId"], columns=["movieId"], values="rating")
        # 存入缓存文件
        ratings_matrix.to_pickle(cache_path)
        print("数据集加载完毕")
    return ratings_matrix


if __name__ == '__main__':
    ratings_matrix = load_data(DATA_PATH)
    print(ratings_matrix)




def compute_pearson_similarity(ratings_matrix, based="user"):
    '''
    计算皮尔逊相关系数
    :param ratings_matrix: 用户-物品评分矩阵
    :param based: "user" or "item"
    :return: 相似度矩阵
    '''
    user_similarity_cache_path = os.path.join(CACHE_DIR, "user_similarity.cache")
    item_similarity_cache_path = os.path.join(CACHE_DIR, "item_similarity.cache")
    # 基于皮尔逊相关系数计算相似度
    # 用户相似度
    if based == "user":
        if os.path.exists(user_similarity_cache_path):
            print("正从缓存加载用户相似度矩阵")
            similarity = pd.read_pickle(user_similarity_cache_path)
        else:
            print("开始计算用户相似度矩阵")
            similarity = ratings_matrix.T.corr()
            similarity.to_pickle(user_similarity_cache_path)

    elif based == "item":
        if os.path.exists(item_similarity_cache_path):
            print("正从缓存加载物品相似度矩阵")
            similarity = pd.read_pickle(item_similarity_cache_path)
        else:
            print("开始计算物品相似度矩阵")
            similarity = ratings_matrix.corr()
            similarity.to_pickle(item_similarity_cache_path)
    else:
        raise Exception("Unhandled 'based' Value: %s"%based)
    print("相似度矩阵计算/加载完毕")
    return similarity

if __name__ == '__main__':

    ratings_matrix = load_data(DATA_PATH)

    user_similar = compute_pearson_similarity(ratings_matrix, based="user")
    print(user_similar)
    item_similar = compute_pearson_similarity(ratings_matrix, based="item")
    print(item_similar)





