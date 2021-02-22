
import pyrebase
import datetime

firebaseConfig = {
    "apiKey": "AIzaSyBVjAsp3odrv6t1AAzHjamHERhvivD5OVU",
    "authDomain": "elsacadatos-e0dd2.firebaseapp.com",
    "databaseURL": "https://elsacadatos-e0dd2-default-rtdb.firebaseio.com",
    "projectId": "elsacadatos-e0dd2",
    "storageBucket": "elsacadatos-e0dd2.appspot.com",
    "messagingSenderId": "594197335876",
    "appId": "1:594197335876:web:5ac584f2bed97a17a79111",
    "measurementId": "G-RXB3Y9XL39"
}
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# Push data

data = {"tempeatura": "35", "viento": "25", "humedad": "2"}

# db.push(data)
x = datetime.datetime.now()
dia = (x.strftime("%d"))
mes = (x.strftime("%m"))
year = (x.strftime("%Y"))

fecha = (dia+":"+mes+":"+year)
# print(fecha)
preHora = (x.strftime("%X"))
fechaYHora = fecha+"-"+preHora

datosClima = {"velocidadViento": "2.3", "direccionViento": "norte",
              "radiacionSolar": "256", "temperatura": "30", "humedadRelativa": "51"}

db.child(fechaYHora).set(datosClima)
