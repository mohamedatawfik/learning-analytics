"""
    Running MF / SVD Recommenders [Rating Prediction]

    - Cross Validation
    - Simple

"""

from caserec.recommenders.rating_prediction.svdplusplus import SVDPlusPlus
from caserec.recommenders.rating_prediction.nnmf import NNMF
from caserec.recommenders.rating_prediction.matrixfactorization import MatrixFactorization
from caserec.utils.cross_validation import CrossValidation

db = '../datasets/ml-100k/u.data'
folds_path = '../datasets/ml-100k/'

tr = '../datasets/ml-100k/folds/0/train.dat'
te = '../datasets/ml-100k/folds/0/test.dat'

"""

    UserKNN

"""

recommender = MatrixFactorization()

CrossValidation(input_file=db, recommender=recommender, dir_folds=folds_path, header=1, k_folds=5, write_predictions='TRUE').compute()

NNMF(tr, te, factors = 20).compute()