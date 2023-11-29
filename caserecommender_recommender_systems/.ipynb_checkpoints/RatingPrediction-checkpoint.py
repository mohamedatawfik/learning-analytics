from caserec.utils.cross_validation import CrossValidation
from caserec.recommenders.rating_prediction.itemknn import ItemKNN

input_file = "C:/Users/qinth/Downloads/ml-100k/ml-100k/u.data"
prediction_dir = "C:/Users/qinth/Downloads/ml-100k/testItemKNN_RP/"
recommender_RP = ItemKNN()
CrossValidation(input_file, recommender_RP, prediction_dir, k_folds=3, write_predictions=True).compute()