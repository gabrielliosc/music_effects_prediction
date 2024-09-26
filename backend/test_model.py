from model.validate import Verify
from backend.model.model import Model
from model.preprocessing import PreProcessing
import pandas as pd


# Parâmetros    
url_dados = "../data/backend_test.csv"

# Carga dos dados
dataset = pd.read_csv(url_dados, sep=';')

#Pré-processamento
dataset = PreProcessing.preprocessing_steps(dataset)

X = dataset.drop(columns=['Music effects']).values	
y = dataset['Music effects'].values #Target
    
# Método para testar modelo SVM a partir do arquivo correspondente
def test_svm_model():
    # Importando modelo de SVM
    svm_path = './music_model.pkl'
    svm_model = Model.load_model(svm_path)

    # Obtendo as métricas do SVM
    accuracy_svm = Verify.validate(svm_model, X, y)
    
    # Testando as métricas do SVM
    assert accuracy_svm >= 0.7

