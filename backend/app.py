from model.model import Model
from model.preprocessing import PreProcessing
from schemas import *

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
user_tag = Tag(name="User", description="Predição de efeitos de músicas em pacientes")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')
    
# Rota de busca de paciente por nome
@app.get('/predict', tags=[user_tag],
        responses={"200": UserViewSchema, "404": ErrorSchema})
def get_prediction(query: UserSchema):    
    """Realiza a predição do impacto da música na saúde mental de uma pessoa.

    Args:
        age: int
        hours_per_day: int
        bpm: int
        freq_classical: int
        freq_country: int
        freq_edm: int
        freq_folk: int
        freq_gospel: int
        freq_hip_hop: int
        freq_jazz: int
        freq_k_pop: int
        freq_latin: int
        freq_lofi: int
        freq_metal: int
        freq_pop: int
        freq_rnb: int
        freq_rap: int
        freq_rock: int
        freq_vg_music: int
        anxiety: int
        depression: int
        insomnia: int
        ocd: int
        primary_streaming_service_Apple_Music: bool
        primary_streaming_service_I_do_not_use_a_streaming_service: bool
        primary_streaming_service_No_Answer: bool
        primary_streaming_service_Other_streaming_service: bool
        primary_streaming_service_Pandora: bool
        primary_streaming_service_Spotify: bool
        primary_streaming_service_YouTube_Music: bool
        fav_genre_classical: bool
        fav_genre_country: bool
        fav_genre_edm: bool
        fav_genre_folk: bool
        fav_genre_gospel: bool
        fav_genre_hip_hop: bool
        fav_genre_jazz: bool
        fav_genre_k_pop: bool
        fav_genre_latin: bool
        fav_genre_lofi: bool
        fav_genre_metal: bool
        fav_genre_pop: bool
        fav_genre_rnb: bool
        fav_genre_rap: bool
        fav_genre_rock: bool
        fav_genre_vg_music: bool
        while_working_no: bool
        while_working_no_answer: bool
        while_working_yes: bool
        instrumentalist_no: bool
        instrumentalist_no_answer: bool
        instrumentalist_yes: bool
        composer_no: bool
        composer_no_Answer: bool
        composer_yes: bool
        exploratory_no: bool
        exploratory_yes: bool
        foreign_languages_no: bool
        foreign_languages_no_answer: bool
        foreign_languages_yes: bool
        
    Returns:
        int: outcome da predição
    """
        
    # Carregando modelo
    ml_path = './music_model.pkl'
    model = Model.load_model(ml_path)
    x_input = PreProcessing.form_prep(query)
    # Realizando a predição
    outcome = int(Model.predict_effects(model, x_input)[0])
    
    try:

        return music_effects(outcome), 200
    
    except Exception as e:
        error_msg = "Não foi possível gerar a predição :/"
        return {"message": error_msg}, 400

if __name__ == '__main__':
    app.run(debug=True)