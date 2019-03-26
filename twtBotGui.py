import tweepy
import os
import sys
import easygui
#LA GUI ANTES Q NADA
palabrasAFiltrar = easygui.enterbox('Palabras a filtrar')
msgCaptado = easygui.enterbox('Mensaje a devolver')

# Autenticando para ingresar a la Api
consumer_key = 'OoOw26lBzTatV9MRDgITIMmYI'
consumer_secret = 'xnH7qWFalAVsc8Kdhzz7UleIQQQXYqYTwUmqEi4g7j9h6CRpLO'
access_token = '512498967-ht2iMB1gSiU1a7oMzvgselrB7wwAZvgM9Q5DizWV'
access_token_secret = 'Sy1Cth7glfGNOap9yYY1v7zjwxQfRCOFOSXMdTYhfJCls'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#LA DIRECCION DE LA IMAGENE EN EL EQUIPO
##im = os.path.abspath('/Users/ALEXX/Pictures/man.jpg')
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_error(self, status):
        if status == 420:#error de alta itineracion
            #returning False in on_data disconnects the stream
            print ("DESCONECTADO DEL ROBOT POR ALTA ITINERACION")
            return False
        print (status)

    def on_status(self, status):
        sn=status.user.screen_name #nombre de usuario
        twId=status.id #id del tweet
        texto=status.text#todo el texto
        print(texto+" @"+sn)
        #EL MENSAJE A RETWITEAR
        msg = "@%s " % (sn) + msgCaptado 
        api.update_status(msg, twId)#respuesta a un tweet
        #api.update_with_media(im,msg,twId)#tweet con imagen y usuario filtrado
        #api.retweet(twId)#retwt de un twt

        #####LA GUI QU DEVUELVE MSGS########
        msge = "@"+ sn + " " + texto
        title = "Personas a las que se spamea"
        if easygui.ccbox(msge, title):  # Continue y Cancele Object  
            pass  # user chose Continue
        else:  # user chose Cancel
            sys.exit(0)

##El filtrado en todo Twter
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#LAS PALABrAS QUE SE qUIEREN FILTRAR
myStream.filter(track=[palabrasAFiltrar], async=True)

