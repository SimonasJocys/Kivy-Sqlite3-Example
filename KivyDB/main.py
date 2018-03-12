#-*-coding: utf-8 -*-"
import sqlite3
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.properties import StringProperty,ObjectProperty
con=sqlite3.connect('db/veri.db')
cursor=con.cursor()
def veri_ekle(veri,sayi):
    cursor.execute("insert into bilgiler values(?,?)",(veri,sayi))
    con.commit()
def veri_guncelle(verit,no):
    cursor.execute("Update bilgiler set Ad=? where numara=?",(verit,no))
    con.commit()
def veri_sil(numara):
    cursor.execute("Delete from bilgiler where numara=?",(numara,))
    con.commit()
class Modal(ModalView):
    labeltext=StringProperty()
    def __init__(self,labeltext,**kwargs):
        super(Modal,self).__init__(**kwargs)
        self.labeltext=labeltext

class Main(ScreenManager):
    pass
class Ekle(Screen):
    pass
class Guncel(Screen):
    pass
class Delete(Screen):
    pass
class Goster(Screen):
    pass
class Anasayfa(Screen):
    pass
class Uygulama(App):
    def build(self):
        return Main()
    def islem(self):
        try:
            ad=self.root.ids.txtad.text
            sayi=random.randrange(999)
            veri_ekle(ad,sayi)
            m=Modal(labeltext="Kayıt başarılı")
            m.open()
        except:
            m=Modal(labeltext="Kayıt işlemi başarısız")
            m.open()


    def listele(self):
        self.root.ids.listg.adapter.data.clear()
        oku=cursor.execute("Select * From bilgiler")
        for i in oku.fetchall():
            self.root.ids.listg.adapter.data.append(str(i))
    def ekranlar(self,txt):
        if(txt=="ekle"):
            self.root.current="ekle"
        elif(txt=="goster"):
            self.root.current="egoster"
        elif(txt=="anasayfa"):
            self.root.current="anasayfa"
        elif(txt=="guncel"):
            self.root.current="guncele"
        elif(txt=="sil"):
            self.root.current="delete"
    def update(self):
        try:
            no=self.root.ids.txtno.text
            name=self.root.ids.txtname.text
            veri_guncelle(name,no)
            mod=Modal(labeltext="Güncelleme başarılı")
            mod.open()
        except:
            mod=Modal(labeltext="Güncelleme başarısız")
            mod.open()
    def delete(self):
        try:
            no=self.root.ids.txtdno.text
            veri_sil(no)
            mod=Modal(labeltext="Silme işlemi başarılı")
            mod.open()
        except:
            mod=Modal(labeltext="Silme işlemi başarısız")
            mod.open()

Uygulama().run()
