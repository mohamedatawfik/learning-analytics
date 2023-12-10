"""
    Running KNN Recommenders [Rating Prediction]

    - Cross Validation
    - Simple

"""

from caserec.recommenders.rating_prediction.user_attribute_knn import UserAttributeKNN
from caserec.recommenders.rating_prediction.item_attribute_knn import ItemAttributeKNN
from caserec.recommenders.rating_prediction.itemknn import ItemKNN
from caserec.recommenders.rating_prediction.userknn import UserKNN
from caserec.utils.cross_validation import CrossValidation

db = '../datasets/ml-100k/u.data'
folds_path = '../datasets/ml-100k/'

tr = '../datasets/ml-100k/folds/0/train.dat'
te = '../datasets/ml-100k/folds/0/test.dat'

"""

    UserKNN

"""

# # Cross Validation
recommender = ItemKNN()
#
CrossValidation(input_file=db, recommender=recommender, dir_folds=folds_path, header=1, k_folds=5, write_predictions='TRUE').compute()
