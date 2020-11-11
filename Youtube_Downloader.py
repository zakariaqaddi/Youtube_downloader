import pafy


# ----------------------------------déclaration des variables----------------------------------

Resolution_video = []
Resolution_audio = []
Choix = ['video', 'audio', 'playlist_video', 'playlist_audio']
Playlist_videos = []
Playlist_audios = []
# ----------------------------------Telechargement d'un vidéo-----------------------


def resolution_video():
    videostreams = video.streams
    for i in videostreams:
        Resolution_video.append(i)
    print(Resolution_video)


def video_download(y):
    print('la taille de la vidéo est : ', Resolution_video[y-1].get_filesize())
    Resolution_video[y-1].download()
    print('la vidéo est téléchargée')

# ----------------------------------Telechargement d'un audio-----------------------


def resolution_audio():
    audiostreams = video.audiostreams
    for i in audiostreams:
        Resolution_audio.append(i)
    print(Resolution_audio)


def audio_download(y):
    print('la taille du audio est : ', Resolution_audio[y-1].get_filesize())
    Resolution_audio[y-1].download()
    print('le audio est téléchargé')


# ---------------------------------Telechargement d'une Playliste de videos----------------------------------------

def download_playlist_video(x):
    #  Préparation de la liste des résolutions vidéos
    for i in len(x['items']):
        Playlist_videos.append(x['items'][i]['pafy'].getbest())
  # download playlist_videos
    for i in Playlist_videos:
        i.download()


def playlist_informations(x):
    print(x['title'])
    print(len(x['items']))

# ---------------------------------Telechargement d'une Playliste de audios----------------------------------------


def download_playlist_audio(x):
    #  Préparation de la liste des résolutions vidéos
    for i in len(x['items']):
        Playlist_audios.append(x['items'][i]['pafy'].getbestaudio())
  # download playlist_videos
    for i in Playlist_audios:
        i.download()


def playlist_informations(x):
    print(x['title'])
    print(len(x['items']))


# --------------------------------------la fonction principale---------------------------------
try:
    print('Bienvenue, ce petit programme vous permet de télécharger video, audio ou playlist')
    print(Choix)
    Uchoix = int(
        input("Entrer l'indice de votre choix, les indices commencent par 1 :  "))

    if Uchoix == 1:
        url = input('Entrer le lien de la vidéo :')
        video = pafy.new(url)
        print(video.title)
        resolution_video()
        resolution_choisit = int(
            input(
                "Enter le numéro qui correspond à la résolution choisit (on commence par 1 !): "))
        video_download(resolution_choisit)

    elif Uchoix == 2:
        url = input('Entrer le lien de la video:')
        video = pafy.new(url)
        print(video.title)
        resolution_audio()
        resolution_choisit = int(
            input(
                "Enter le numéro qui correspond à la résolution choisit (on commence par 1 !): "))
        audio_download(resolution_choisit)

    elif Uchoix == 3:
        url = input('Entrer le lien de la playlist :')
        playlist = pafy.get_playlist(url)
        playlist_informations(playlist)
        download_playlist_video(playlist)

    elif Uchoix == 4:
        url = input('Entrer le lien de la playlist :')
        playlist = pafy.get_playlist(url)
        playlist_informations(playlist)
        download_playlist_audio(playlist)
except:
    print('Oups! vous avez commit un erreur quelque part, vérifiez votre url ou connexion ')
