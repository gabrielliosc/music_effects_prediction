import pickle

class Model:
    
    def load_model(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                model = pickle.load(file)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def predict_effects(model, X_input):
        """
        Realiza a predição de uma pessoa com base no modelo treinado
        """
        music_terapy = model.predict(X_input)
        return music_terapy