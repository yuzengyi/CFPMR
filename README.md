# Improved Collaborative Filtering for Personalized Movie Recommendations Using K-Means Clustering

**Author:** Qihao Yang  
**Institution:** College of Education, Zhejiang University of Technology, Hangzhou, China  
**Contact:** 1183613243@qq.com

## Abstract
This project focuses on improving personalized movie recommendations using a collaborative filtering algorithm enhanced with K-means clustering. In addition to collaborative filtering for initial data processing, the system employs K-means clustering, advanced activation functions, attention mechanisms, multi-head attention, and regularization techniques to improve accuracy. The optimized model achieves 99% accuracy when predicting the corrected rating for User 6 on Movie 2. The source code is available in the repository.

**Keywords:** K-means clustering, Collaborative filtering algorithm, Attention mechanism, Regularization

## Table of Contents
- [Improved Collaborative Filtering for Personalized Movie Recommendations Using K-Means Clustering](#improved-collaborative-filtering-for-personalized-movie-recommendations-using-k-means-clustering)
  - [Abstract](#abstract)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Methods](#methods)
    - [Data Preprocessing](#data-preprocessing)
    - [Constructing a K-means Clustering Model](#constructing-a-k-means-clustering-model)
    - [Filtering Strategy](#filtering-strategy)
    - [Feedforward Neural Network](#feedforward-neural-network)
  - [Results](#results)
  - [Conclusions](#conclusions)

## Introduction
Personalized recommendation systems have become a focal point in enhancing user experience across multiple industries, with collaborative filtering (CF) being a popular approach. CF has proven highly effective for recommending items, particularly in fields such as movie recommendations, where user preferences vary greatly. This project aims to enhance CF by integrating K-means clustering to dynamically group users based on movie preferences. We further explore the use of modern machine learning techniques to improve the accuracy of movie recommendations.

## Methods
### Data Preprocessing
The dataset consists of 19 movie genres such as Action, Adventure, Comedy, etc. During preprocessing, one-hot encoding is used for categorical features like genres, transforming them into Euclidean space for similarity calculations.

### Constructing a K-means Clustering Model
The K-means clustering model is used to identify user clusters based on genre preferences. The Euclidean distance is used to determine the similarity between samples, and cluster centroids are dynamically adjusted until the clustering process converges.

### Filtering Strategy
An additional filtering layer ensures that movies previously watched by users are not recommended again. Instead, movies are recommended based on proportional preferences across genres.

### Feedforward Neural Network
The recommendation model uses a feedforward neural network consisting of an embedding layer and three fully connected layers to predict user ratings. Techniques such as advanced activation functions (LeakyReLU), attention mechanisms, and multi-head attention are applied to further improve the model's performance.

## Results
Experimental results show that incorporating K-means clustering and enhancing CF with machine learning techniques yields a significant improvement in recommendation accuracy. The optimized model achieved an accuracy of 99.36% compared to the original accuracy of 81.19% after adjustments such as increasing the number of hidden layers and integrating attention mechanisms.

## Conclusions
This project successfully demonstrates that personalized movie recommendations can be improved by integrating K-means clustering with collaborative filtering and utilizing modern neural network enhancements. In the future, we plan to explore additional techniques such as deep learning and other clustering methods to enhance the personalized recommendation capabilities further.