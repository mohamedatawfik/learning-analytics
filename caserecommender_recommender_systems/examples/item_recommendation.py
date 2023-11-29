"""
    Running KNN Recommenders [Item Recommendation]

    - Cross Validation
    - Simple

"""

from caserec.recommenders.item_recommendation.user_attribute_knn import UserAttributeKNN
from caserec.recommenders.item_recommendation.item_attribute_knn import ItemAttributeKNN
from caserec.recommenders.item_recommendation.itemknn import ItemKNN
from caserec.recommenders.item_recommendation.userknn import UserKNN
from caserec.utils.cross_validation import CrossValidation

db = '../datasets/ml-100k/u.data'
folds_path = '../datasets/ml-100k/'

tr = '../datasets/ml-100k/folds/0/train.dat'
te = '../datasets/ml-100k/folds/0/test.dat'

"""

    ItemKNN

"""

# # Cross Validation
recommender = ItemKNN(as_binary=True)
#
CrossValidation(input_file=db, recommender=recommender, dir_folds=folds_path, header=1, k_folds=5, write_predictions='TRUE').compute()

