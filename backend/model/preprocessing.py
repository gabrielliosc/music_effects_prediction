import pandas as pd

class PreProcessing:

    def preprocessing_steps(dataset):
        """ Cuida de todo o pré-processamento. """
        
        df = dataset.drop(['Timestamp', 'Permissions'], axis=1)

        #Substituição dos valores NaN
        df['Music effects'].fillna('No Answer', inplace=True)
        df['Primary streaming service'].fillna('No Answer', inplace=True)
        df['While working'].fillna('No Answer', inplace=True)
        df['Instrumentalist'].fillna('No Answer', inplace=True)
        df['Composer'].fillna('No Answer', inplace=True)
        df['Foreign languages'].fillna('No Answer', inplace=True)
        df['Age'].fillna(0, inplace=True)
        df['BPM'].fillna(0, inplace=True)

        #Mudança do tipo da coluna
        df['Age'] = df['Age'].astype(int)

        #Mudança nas colunas categoricas
        categorical_columns = ['Primary streaming service', 'Fav genre', 'While working', 'Instrumentalist', 'Composer', 'Exploratory', 'Foreign languages']
        df_encoded = pd.get_dummies(df, columns=categorical_columns)

        #Mapeia colunas de frequência para valores numéricos
        frequency_columns = [col for col in df_encoded.columns if 'Frequency' in col]
        mapping = {'Never': 0, 'Rarely': 1, 'Sometimes': 2, 'Very frequently': 3}
        df_encoded[frequency_columns] = df_encoded[frequency_columns].applymap(lambda x: mapping[x])

        #Mapeia a coluna target para valores númerico
        label_mapping = {'No Answer': 0, 'No effect': 1, 'Improve': 2, 'Worsen': 3}
        df_encoded['Music effects'] = df_encoded['Music effects'].map(label_mapping)

        df_encoded.insert(26, "Primary_streaming_service_No_Answer", False, True)
        df_encoded.insert(35, "Fav_genre_Gospel", False, True)
        df_encoded.insert(48, "While_working_No_Answer", False, True)
        df_encoded.insert(51, "Instrumentalist_No_Answer", False, True)
        df_encoded.insert(54, "Composer_No_Answer", False, True)
        df_encoded.insert(59, "Foreign_languages_No_Answer", False, True)

        return df_encoded

    def form_prep(query):
        """ Prepara o formulário para ser predito pelo modelo. """
        # Cria um dataframe com as respostas do formulário
        column_names = [
                        "Age",
                        "Hours per day",
                        "BPM",
                        "Frequency [Classical]",
                        "Frequency [Country]",
                        "Frequency [EDM]",
                        "Frequency [Folk]",
                        "Frequency [Gospel]",
                        "Frequency [Hip hop]",
                        "Frequency [Jazz]",
                        "Frequency [K pop]",
                        "Frequency [Latin]",
                        "Frequency [Lofi]",
                        "Frequency [Metal]",
                        "Frequency [Pop]",
                        "Frequency [R&B]",
                        "Frequency [Rap]",
                        "Frequency [Rock]",
                        "Frequency [Video game music]",
                        "Anxiety",
                        "Depression",
                        "Insomnia",
                        "OCD",
                        "Primary streaming service_Apple Music",
                        "Primary streaming service_I do not use a streaming service.",
                        "Primary streaming service_No Answer",
                        "Primary streaming service_Other streaming service",
                        "Primary streaming service_Pandora",
                        "Primary streaming service_Spotify",
                        "Primary streaming service_YouTube Music",
                        "Fav genre_Classical",
                        "Fav genre_Country",
                        "Fav genre_EDM",
                        "Fav genre_Folk",
                        "Fav genre_Gospel",
                        "Fav genre_Hip hop",
                        "Fav genre_Jazz",
                        "Fav genre_K pop",
                        "Fav genre_Latin",
                        "Fav genre_Lofi",
                        "Fav genre_Metal",
                        "Fav genre_Pop",
                        "Fav genre_R&B",
                        "Fav genre_Rap",
                        "Fav genre_Rock",
                        "Fav genre_Video game music",
                        "While working_No",
                        "While working_No Answer",
                        "While working_Yes",
                        "Instrumentalist_No",
                        "Instrumentalist_No Answer",
                        "Instrumentalist_Yes",
                        "Composer_No",
                        "Composer_No Answer",
                        "Composer_Yes",
                        "Exploratory_No",
                        "Exploratory_Yes",
                        "Foreign languages_No",
                        "Foreign languages_No Answer",
                        "Foreign languages_Yes"
                    ]
        #Cria um dicionario com as respostas do formulário
        dataset = {
            "Age": [query.age],
            "Hours per day": [query.hours_per_day],
            "BPM": [query.bpm],
            "Frequency [Classical]": [query.freq_classical],
            "Frequency [Country]": [query.freq_country],
            "Frequency [EDM]": [query.freq_edm],
            "Frequency [Folk]": [query.freq_folk],
            "Frequency [Gospel]": [query.freq_gospel],
            "Frequency [Hip hop]": [query.freq_hip_hop],
            "Frequency [Jazz]": [query.freq_jazz],
            "Frequency [K pop]": [query.freq_k_pop],
            "Frequency [Latin]": [query.freq_latin],
            "Frequency [Lofi]": [query.freq_lofi],
            "Frequency [Metal]": [query.freq_metal],
            "Frequency [Pop]": [query.freq_pop],
            "Frequency [R&B]": [query.freq_rnb],
            "Frequency [Rap]": [query.freq_rap],
            "Frequency [Rock]": [query.freq_rock],
            "Frequency [Video game music]": [query.freq_vg_music],
            "Anxiety": [query.anxiety],
            "Depression": [query.depression],
            "Insomnia": [query.insomnia],
            "OCD": [query.ocd],
            "Primary streaming service_Apple Music": [query.primary_streaming_service_Apple_Music],
            "Primary streaming service_I do not use a streaming service.": [query.primary_streaming_service_I_do_not_use_a_streaming_service],
            "Primary streaming service_No Answer": [query.primary_streaming_service_No_Answer],
            "Primary streaming service_Other streaming service": [query.primary_streaming_service_Other_streaming_service],
            "Primary streaming service_Pandora": [query.primary_streaming_service_Pandora],
            "Primary streaming service_Spotify": [query.primary_streaming_service_Spotify],
            "Primary streaming service_YouTube Music": [query.primary_streaming_service_YouTube_Music],
            "Fav genre_Classical": [query.fav_genre_classical],
            "Fav genre_Country": [query.fav_genre_country],
            "Fav genre_EDM": [query.fav_genre_edm],
            "Fav genre_Folk": [query.fav_genre_folk],
            "Fav genre_Gospel": [query.fav_genre_gospel],
            "Fav genre_Hip hop": [query.fav_genre_hip_hop],
            "Fav genre_Jazz": [query.fav_genre_jazz],
            "Fav genre_K pop": [query.fav_genre_k_pop],
            "Fav genre_Latin": [query.fav_genre_latin],
            "Fav genre_Lofi": [query.fav_genre_lofi],
            "Fav genre_Metal": [query.fav_genre_metal],
            "Fav genre_Pop": [query.fav_genre_pop],
            "Fav genre_R&B": [query.fav_genre_rnb],
            "Fav genre_Rap": [query.fav_genre_rap],
            "Fav genre_Rock": [query.fav_genre_rock],
            "Fav genre_Video game music": [query.fav_genre_vg_music],
            "While working_No": [query.while_working_no],
            "While working_No Answer": [query.while_working_no_answer],
            "While working_Yes": [query.while_working_yes],
            "Instrumentalist_No": [query.instrumentalist_no],
            "Instrumentalist_No Answer": [query.instrumentalist_no_answer],
            "Instrumentalist_Yes": [query.instrumentalist_yes],
            "Composer_No": [query.composer_no],
            "Composer_No Answer": [query.composer_no_Answer],
            "Composer_Yes": [query.composer_yes],
            "Exploratory_No": [query.exploratory_no],
            "Exploratory_Yes": [query.exploratory_yes],
            "Foreign languages_No": [query.foreign_languages_no],
            "Foreign languages_No Answer": [query.foreign_languages_no_answer],
            "Foreign languages_Yes": [query.foreign_languages_yes]
        }
        form = pd.DataFrame(dataset, columns=column_names)

        return form