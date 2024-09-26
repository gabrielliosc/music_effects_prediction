from pydantic import BaseModel

class UserSchema(BaseModel):
    """
    Define como deve ser a estrutura que representa a busca.
    """
    age: int = 0
    hours_per_day: int = 0
    bpm: int = 0
    freq_classical: int = 0
    freq_country: int = 0
    freq_edm: int = 0
    freq_folk: int = 0
    freq_gospel: int = 0
    freq_hip_hop: int = 0
    freq_jazz: int = 0
    freq_k_pop: int = 0
    freq_latin: int = 0
    freq_lofi: int = 0
    freq_metal: int = 0
    freq_pop: int = 0
    freq_rnb: int = 0
    freq_rap: int = 0
    freq_rock: int = 0
    freq_vg_music: int = 0
    anxiety: int = 0
    depression: int = 0
    insomnia: int = 0
    ocd:  int = 0
    primary_streaming_service_Apple_Music: bool = False
    primary_streaming_service_I_do_not_use_a_streaming_service: bool = False
    primary_streaming_service_No_Answer: bool = False
    primary_streaming_service_Other_streaming_service: bool = False
    primary_streaming_service_Pandora: bool = False
    primary_streaming_service_Spotify: bool = False
    primary_streaming_service_YouTube_Music: bool = False
    fav_genre_classical: bool = False
    fav_genre_country: bool = False
    fav_genre_edm: bool = False
    fav_genre_folk: bool = False
    fav_genre_gospel: bool = False
    fav_genre_hip_hop: bool = False
    fav_genre_jazz: bool = False
    fav_genre_k_pop: bool = False
    fav_genre_latin: bool = False
    fav_genre_lofi: bool = False
    fav_genre_metal: bool = False
    fav_genre_pop: bool = False
    fav_genre_rnb: bool = False
    fav_genre_rap: bool = False
    fav_genre_rock: bool = False
    fav_genre_vg_music: bool = False
    while_working_no: bool = False
    while_working_no_answer: bool = False
    while_working_yes: bool = False
    instrumentalist_no: bool = False
    instrumentalist_no_answer: bool = False
    instrumentalist_yes: bool = False
    composer_no: bool = False
    composer_no_Answer: bool = False
    composer_yes: bool = False
    exploratory_no: bool = False
    exploratory_yes: bool = False
    foreign_languages_no: bool = False
    foreign_languages_no_answer: bool = False
    foreign_languages_yes: bool = False
    
class UserViewSchema(BaseModel):
    """
    Define como a predição de uma pessoa será representada
    """
    outcome: int = None

# Apresenta apenas os dados de um paciente    
def music_effects(outcome: int) -> UserViewSchema:
    """ Retorna uma representação do paciente seguindo o schema definido em
        UserViewSchema.
    """
    return {
        "outcome": outcome
    }

