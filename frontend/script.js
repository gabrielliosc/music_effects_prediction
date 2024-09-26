const handleFormSubmit = e => {
    e.preventDefault()
    const prediction = {
        0: "It's not possible to predict your experience with music therapy.",
        1: "You are likely to have a negative experience with music therapy.",
        2: "You are likely to have a neutral experience with music therapy.",
        3: "You are likely to have a positive experience with music therapy.",
    }
    predict()
        .then(data => {
            const result = document.getElementById("result")
            const outcome = document.getElementById("outcome")
            outcome.classList.remove("hidden")
            result.innerHTML = prediction[data["outcome"]]
        })
        .catch(err => console.error(err))
}

async function predict() {
    //Get the data from the form
    const form = document.getElementById("myForm")

    const age = form.elements["age"].value
    const hoursPerDay = form.elements["hours"].value
    const bpm = form.elements["bpm"].value
    const freqClassical = form.elements["freqClassical"].value
    const freqCountry = form.elements["freqCountry"].value
    const freqEDM = form.elements["freqEDM"].value
    const freqFolk = form.elements["freqFolk"].value
    const freqGospel = form.elements["freqGospel"].value
    const freqHipHop = form.elements["freqHipHop"].value
    const freqJazz = form.elements["freqJazz"].value
    const freqKPop = form.elements["freqKPop"].value
    const freqLatin = form.elements["freqLatin"].value
    const freqLoFi = form.elements["freqLoFi"].value
    const freqMetal = form.elements["freqMetal"].value
    const freqPop = form.elements["freqPop"].value
    const freqRnb = form.elements["freqRnb"].value
    const freqRap = form.elements["freqRap"].value
    const freqRock = form.elements["freqRock"].value
    const freqVideoGameMusic = form.elements["freqVideoGameMusic"].value
    const anxiety = form.elements["anxiety"].value
    const depression = form.elements["depression"].value
    const insomnia = form.elements["insomnia"].value
    const ocd = form.elements["ocd"].value

    const appleMusic = form.elements["streaming"].value === "apple"
    const notUseStreaming = form.elements["streaming"].value === "none"
    const noAnswer = form.elements["streaming"].value === "noAnswer"
    const otherStreaming = form.elements["streaming"].value === "other"
    const pandora = form.elements["streaming"].value === "pandora"
    const spotify = form.elements["streaming"].value === "spotify"
    const youtubeMusic = form.elements["streaming"].value === "youtube"
    
    const favGenreClassical = form.elements["favGenre"].value === "classical"
    const favGenreCountry = form.elements["favGenre"].value === "country"
    const favGenreEDM = form.elements["favGenre"].value === "edm"
    const favGenreFolk = form.elements["favGenre"].value === "folk"
    const favGenreGospel = form.elements["favGenre"].value === "gospel"
    const favGenreHipHop = form.elements["favGenre"].value === "hipHop"
    const favGenreJazz = form.elements["favGenre"].value === "jazz"
    const favGenreKPop = form.elements["favGenre"].value === "kPop"
    const favGenreLatin = form.elements["favGenre"].value === "latin"
    const favGenreLoFi = form.elements["favGenre"].value === "loFi"
    const favGenreMetal = form.elements["favGenre"].value === "metal"
    const favGenrePop = form.elements["favGenre"].value === "pop"
    const favGenreRnb = form.elements["favGenre"].value === "rnb"
    const favGenreRap = form.elements["favGenre"].value === "rap"
    const favGenreRock = form.elements["favGenre"].value === "rock"
    const favGenreVideoGameMusic = form.elements["favGenre"].value === "videoGameMusic"

    const whileWorkingNo = form.elements["whileWorking"].value === "no"
    const whileWorkingNoAnswer = form.elements["whileWorking"].value === "noAnswer"
    const whileWorking = form.elements["whileWorking"].value === "yes"

    const instrumentalistNo = form.elements["instrumentalist"].value === "no"
    const instrumentalistNoAnswer = form.elements["instrumentalist"].value === "noAnswer"
    const instrumentalist = form.elements["instrumentalist"].value === "yes"

    const composerNo = form.elements["composer"].value === "no"
    const composerNoAnswer = form.elements["composer"].value === "noAnswer"
    const composer = form.elements["composer"].value === "yes"

    const exploratoryNo = form.elements["exploratory"].value === "no"
    const exploratory = form.elements["exploratory"].value === "yes"

    const foreignLanguagesNo = form.elements["foreignLanguages"].value === "no"
    const foreignLanguagesNoAnswer = form.elements["foreignLanguages"].value === "noAnswer"
    const foreignLanguages = form.elements["foreignLanguages"].value === "yes"

    const query = `age=${age}&hours_per_day=${hoursPerDay}&bpm=${bpm}&freq_classical=${freqClassical}&freq_country=${freqCountry}&freq_edm=${freqEDM}&freq_folk=${freqFolk}&freq_gospel=${freqGospel}&freq_hip_hop=${freqHipHop}&freq_jazz=${freqJazz}&freq_k_pop=${freqKPop}&freq_latin=${freqLatin}&freq_lofi=${freqLoFi}&freq_metal=${freqMetal}&freq_pop=${freqPop}&freq_rnb=${freqRnb}&freq_rap=${freqRap}&freq_rock=${freqRock}&freq_vg_music=${freqVideoGameMusic}&anxiety=${anxiety}&depression=${depression}&insomnia=${insomnia}&ocd=${ocd}&primary_streaming_service_Apple_Music=${appleMusic}&primary_streaming_service_I_do_not_use_a_streaming_service=${notUseStreaming}&primary_streaming_service_No_Answer=${noAnswer}&primary_streaming_service_Other_streaming_service=${otherStreaming}&primary_streaming_service_Pandora=${pandora}&primary_streaming_service_Spotify=${spotify}&primary_streaming_service_YouTube_Music=${youtubeMusic}&fav_genre_classical=${favGenreClassical}&fav_genre_country=${favGenreCountry}&fav_genre_edm=${favGenreEDM}&fav_genre_folk=${favGenreFolk}&fav_genre_gospel=${favGenreGospel}&fav_genre_hip_hop=${favGenreHipHop}&fav_genre_jazz=${favGenreJazz}&fav_genre_k_pop=${favGenreKPop}&fav_genre_latin=${favGenreLatin}&fav_genre_lofi=${favGenreLoFi}&fav_genre_metal=${favGenreMetal}&fav_genre_pop=${favGenrePop}&fav_genre_rnb=${favGenreRnb}&fav_genre_rap=${favGenreRap}&fav_genre_rock=${favGenreRock}&fav_genre_vg_music=${favGenreVideoGameMusic}&while_working_no=${whileWorkingNo}&while_working_no_answer=${whileWorkingNoAnswer}&while_working_yes=${whileWorking}&instrumentalist_no=${instrumentalistNo}&instrumentalist_no_answer=${instrumentalistNoAnswer}&instrumentalist_yes=${instrumentalist}&composer_no=${composerNo}&composer_no_Answer=${composerNoAnswer}&composer_yes=${composer}&exploratory_no=${exploratoryNo}&exploratory_yes=${exploratory}&foreign_languages_no=${foreignLanguagesNo}&foreign_languages_no_answer=${foreignLanguagesNoAnswer}&foreign_languages_yes=${foreignLanguages}`

    response = await fetch('http://localhost:5000/predict?' + query)
    data = await response.json()
    
    return data;
}



