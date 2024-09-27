from sklearn.metrics import accuracy_score
from model.model import Model

class Verify:

    def validate(model, X_test, Y_test):
        """ 
        Faz uma predição e avalia o modelo.
        """
        predicoes = Model.predict_effects(model, X_test)
        
        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return accuracy_score(Y_test, predicoes)
