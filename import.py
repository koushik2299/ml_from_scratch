import numpy as np
import mlflow
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import warnings
from imblearn.combine import SMOTETomek
warnings.filterwarnings('ignore')

print("All imports work successfully!")
