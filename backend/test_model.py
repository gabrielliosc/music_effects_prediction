from model.validate import Verify
from model.model import Model
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
    
# Método para testar modelo random forest a partir do arquivo correspondente
def test_rf_model():
    # Importando modelo de random forest
    rf_path = './music_model.pkl'
    rf_model = Model.load_model(rf_path)

    # Obtendo as métricas do random forest
    accuracy_rf = Verify.validate(rf_model, X, y)
    
    # Testando as métricas do random forest
    assert accuracy_rf >= 0.7

