from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from csv import DictReader
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget, OneLineIconListItem
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
import webbrowser
import sqlite3
from kivymd.uix.button import MDRectangleFlatButton

Window.size = (300, 500)  # to be removed

home_helper = """
#:import MapView kivy_garden.mapview.MapView

ScreenManager:
    HomeScreen:
    SearchScreen:
    IntroScreen:
    LinksScreen:
    AssoScreen:
    LawScreen:
    PremrepScreen:
    MoreaedScreen:
    MorePSScreen:
    LieuScreen:
    TwoScreen:
    HemoScreen1:
    HemoScreen2:
    EtouffWScreen:
    EtouffPScreen:
    EtouffAgeScreen:
    EtouffA1Screen:
    EtouffA2Screen:
    EtouffB1Screen:
    EtouffB2Screen:
    EtouffOE1Screen:
    EtouffOE2Screen:
    VCScreen:
    CriseScreen:
    AVCScreen:
    ConsScreen:
    RespiScreen1:
    RespiScreen2:
    PLS1:
    PLS2:
    PLS3:
    CPRAge:
    CPRA1:
    CPRA2:
    CPRE1:
    CPRE2:
    CPRB1:
    CPRB2:
    CPRC:
    AED1:
    AED2:
    Screen1:
    Screen2:
    Screen3:
    
<HomeScreen>:
    name: "home"
    
    MDLabel:
        text: "Sélectionnez la fonction désirée"
        font_style:  "H5"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.775}
        halign: "center"
        

    Image: 
        source: "try_logo.png"
        pos_hint: {"center_x":0.51, "center_y":0.45}
        size_hint_x: 0.85
        size_hint_y:0.85
    
    Button: 
        background_color: (1,1,1,0)
        pos_hint: {"center_x":0.5, "center_y":0.64}
        size_hint_x: 0.225
        size_hint_y: 0.225
        on_press: root.manager.current = "Lieu"

    Image: 
        source: "logo_p.png"
        pos_hint: {"center_x":0.5, "center_y":0.64} 
        size_hint_x: 0.225
        size_hint_y: 0.225

    Button: 
        background_color: (1,1,1,0)
        pos_hint: {"center_x":0.82, "center_y":0.45}
        size_hint_x: 0.225
        size_hint_y: 0.225
        on_press: root.manager.current = "intro"
        
    Image: 
        source: "logo_i.png"
        pos_hint: {"center_x":0.82, "center_y":0.45}
        size_hint_x: 0.225
        size_hint_y:0.225
        
    Button: 
        background_color: (1,1,1,0)
        pos_hint: {"center_x":0.18, "center_y":0.45}
        size_hint_x: 0.225
        size_hint_y: 0.225
        on_press: root.manager.current = "one"
    
    Image: 
        source: "logo_a.png"
        pos_hint: {"center_x":0.18, "center_y":0.45}
        size_hint_x: 0.255
        size_hint_y:0.255
    
    Button: 
        background_color: (1,1,1,0)
        pos_hint: {"center_x":0.5, "center_y":0.26}
        size_hint_x: 0.225
        size_hint_y: 0.225
        on_press: root.manager.current = "Search"
    
    Image: 
        source: "logo_c_edited.png"
        pos_hint: {"center_x":0.5, "center_y":0.26}
        size_hint_x: 0.255
        size_hint_y:0.255
    
    Screen: 
        MDNavigationLayout:
            ScreenManager:
                Screen: 
                    BoxLayout: 
                        orientation: "vertical" 
                        MDToolbar: 
                            title: "Menu Principal"
                            left_action_items: [["menu",lambda x: nav_drawer.set_state("open")]]
                            elevation: 10
                            specific_text_color: (1,1,1,1)

                        Widget:

                        MDToolbar:

            MDNavigationDrawer:
                id: nav_drawer

                BoxLayout:
                    orientation: "vertical"
                    spacing: "12dp"
                    padding: "8dp"

                    Image: 
                        source: "logo_pri.png"

                    MDLabel:
                        text: "  Projet de TM"
                        font_style: "Subtitle1"
                        size_hint_y:None 
                        height: self.texture_size[1]

                    MDLabel:
                        text: "  Collège Rousseau 2021-2022"
                        font_style: "Caption"
                        size_hint_y:None 
                        height: self.texture_size[1]

                    ScrollView:
                        MDList: 
                            TwoLineListItem:
                                text: "Appel Urgences"
                                secondary_text: "Numéros d'urgence dans le monde"
                                on_press: root.manager.current = "Search"
                            TwoLineListItem:
                                text: "Location AED"
                                secondary_text: "Localisation de l'AED le plus proche"
                                on_press: root.manager.current = "one"
                            TwoLineListItem:
                                text: "Premiers Secours"
                                secondary_text: "Marche à suivre des premiers secours"
                                on_press: root.manager.current = "Lieu"
                            TwoLineListItem:
                                text: "Informations"
                                secondary_text: "Pour en savoir plus sur le sujet"
                                on_press: root.manager.current = "intro"

<Container>:
    orientation: "vertical"
    size_hint_y: None
    height: "120dp"  

    MDLabel: 
        text: "1. Tapez le numéro dans votre téléphone."  
        text_color: (0,0,0,1)

    Widget: 

    MDLabel: 
        text: "2. Puis, indiquez la location, l'âge, le sexe et l'état de la victime."
        text_color: (0,0,0,1)  

    Widget: 

<Content>:
    orientation: "vertical"
    size_hint_y: None
    height: "120dp"

    Widget:

    Widget:

    MDRectangleFlatButton:
        text: "Rechercher"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        line_color: (0,0,0,1)
        pos_hint: {"center_x":0.5, "center_y":0.5}
        on_press: app.callback()

    Widget: 

<Content2>:
    orientation: "vertical"
    size_hint_y: None
    height: "120dp"

    Widget:

    Widget:

    MDRectangleFlatButton:
        id: button
        text: "Rechercher"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        line_color: (0,0,0,1)
        pos_hint: {"center_x":0.5, "center_y":0.5}
        on_press: app.callback2()

    Widget:

<SearchScreen>:
    name: "Search"

    BoxLayout: 
        orientation: "vertical"
        spacing: "10dp"

        MDToolbar: 
            title: "Appel Secours"
            right_action_items: [["magnify",lambda x: app.search_menu()]]
            elevation: 10
            specific_text_color: (1,1,1,1)

        ScrollView:
            MDList:
                id: content

        MDToolbar:
    
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<IntroScreen>:
    name: "intro"
    
    MDLabel: 
        text: "Le Projet"
        font_style: "H4"
        halign: "center"
        pos_hint: {"center_x":0.5, "center_y":0.75}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color       
    
    BoxLayout: 
        orientation: "vertical"
        padding: "15dp"

        MDLabel:
            text: "Cette application a été développée dans le cadre de mon Travail de Maturité. Le but principal du projet est de sensibiliser le public aux premiers secours. Si vous souhaitez savoir plus sur ce sujet, il existe plusieurs organisations qui sont consacrées à ce but, donc jetez un coup d'œil aux sites internet à la page suivante." 
            font_style: "Body1"
            halign: "center"
        
    MDRectangleFlatButton:
        text: "Page Suivante"
        on_press: root.manager.current = "links"
        pos_hint: {"center_x":0.5, "center_y":0.25} 

    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Informations"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
        
<LinksScreen>:
    name: "links"
    
    MDRectangleFlatButton:
        text: 'Associations'
        on_press: root.manager.current = "asso"
        pos_hint: {"center_x":0.5, "center_y":0.7}
    
    MDRectangleFlatButton:
        text:"S'engager"
        on_press: root.manager.current = "premrep"
        pos_hint: {"center_x":0.5, "center_y":0.6}
        
    MDRectangleFlatButton:
        text:"Règles/Lois"
        on_press: root.manager.current = "law"
        pos_hint: {"center_x":0.5, "center_y":0.5}
    
    MDRectangleFlatButton:
        text:"Plus sur l'AED"
        on_press: root.manager.current = "moreaed"
        pos_hint: {"center_x":0.5, "center_y":0.4} 
    
    MDRectangleFlatButton:
        text:"Plus sur les premiers secours"
        on_press: root.manager.current = "moreps"
        pos_hint: {"center_x":0.5, "center_y":0.3}
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Informations"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<AssoScreen>:
    name: "asso"

    MDLabel:
        text: "Organisations de premiers secours"
        font_style: "H4"
        halign: "center"
        pos_hint:{"center_x":0.5,"center_y":0.75}
    
    MDLabel:
        text: "Ces deux organisations sauvent un nombre considérable de vies, en formant des volontaires et en sensibilisant le public. Jetez un coup d'oeil sur leur site internet pour en savoir plus sur leur travail."
        halign: "center"
        font_style: "Body1"
        pos_hint:{"center_x":0.5,"center_y":0.525}
            
    MDRectangleFlatButton:
        text: "Alliance Suisse des Samaritains"
        on_press: app.sam_1()
        pos_hint:{"center_x":0.5,"center_y":0.35}

    MDRectangleFlatButton:
        text: "Save a life"
        on_press: app.sam_2()
        pos_hint:{"center_x":0.5,"center_y":0.25}  
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Info: Organisations"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 

<PremrepScreen>:
    name: "premrep"
    
    MDLabel:
        text: "S'engager"
        font_style: "H4"
        halign: "center"
        pos_hint:{"center_x":0.5,"center_y":0.75}
    
    MDLabel:
        text: "Si vous êtes motivés à vous engager pour sauver des vies, visitez ces deux sites qui proposent deux types d'engagement différents."
        halign: "center"
        font_style: "Body1"
        pos_hint:{"center_x":0.5,"center_y":0.6}
        
    MDRectangleFlatButton:
        text: "Réseau Save a Life"
        on_press: app.sam_3()
        pos_hint:{"center_x":0.5,"center_y":0.45}

    MDRectangleFlatButton:
        text: "AGSS"
        on_press: app.sam_4()
        size: (50,50)
        pos_hint:{"center_x":0.5,"center_y":0.35}
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Info: Enagagement"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 

<LawScreen>:
    name: "law"

    MDLabel:
        text: "Règles/Lois"
        font_style: "H4"
        halign: "center"
        pos_hint:{"center_x":0.5,"center_y":0.75}
    
    MDLabel:
        text: "Site explicant la responsabilité du secouriste non professionel d'après le droit pénal et le droit civil."
        halign: "center"
        font_style: "Body1"
        pos_hint:{"center_x":0.5,"center_y":0.6}
    
    MDRectangleFlatButton:
        text: "Responsabilité du secouriste d'après la loi"
        on_press: app.sam_5()
        pos_hint:{"center_x":0.5,"center_y":0.475}
    
    MDLabel:
        text: "Directives de la Swiss Resuscitation Council, qui sont  revisitées d'année en année" 
        halign: "center"
        font_style: "Body1"
        pos_hint:{"center_x":0.5,"center_y":0.357}

    MDRectangleFlatButton:
        text: "Guidelines SRC"
        on_press: app.sam_6()
        pos_hint:{"center_x":0.5,"center_y":0.25}
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Info: Règles/Lois"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 
        
<MoreaedScreen>:
    name: "moreaed"
    
    MDLabel:
        text: "AED"
        font_style: "H4"
        halign: "center"
        pos_hint:{"center_x":0.5,"center_y":0.75}
    
    MDLabel:
        text: "L'AED joue un rôle majeur dans la rescucitation d'une victime. Découvrez plus sur ces machines, et comment vous pouvez recensez le votre."
        halign: "center"
        font_style: "Body1"
        pos_hint:{"center_x":0.5,"center_y":0.6}
    
    MDRectangleFlatButton:
        text: "Qu'est-ce que c'est un AED?"
        on_press: app.sam_7()
        pos_hint:{"center_x":0.5,"center_y":0.45}

    MDRectangleFlatButton:
        text: "Recenser un AED"
        on_press: app.sam_8()
        pos_hint:{"center_x":0.5,"center_y":0.35} 
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Info: AED"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12  

<MorePSScreen>:
    name: "moreps"
    
    MDRectangleFlatButton:
        text: "Samaritains: Guides et conseils"
        on_press: app.sam_9()
        pos_hint:{"center_x":0.5,"center_y":0.3}
    
    MDLabel:
        text: "Premiers Secours en plus"
        font_style: "H4"
        halign: "center"
        pos_hint:{"center_x":0.5,"center_y":0.7}
    
    MDLabel:
        text: "Seulement une partie des gestes qui sauvent sont présentés dans cette application. Si vous voulez vous éduquer sur plus de gestes, visitez le site suivant."
        halign: "center"
        font_style: "Body1"
        pos_hint:{"center_x":0.5,"center_y":0.5} 
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Info: Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 

<LieuScreen>:
    name: "Lieu"
    
    MDLabel: 
        text: "Sécurisez les lieux"
        pos_hint: {"center_x":0.5, "center_y":0.7}
        halign: "center"
        font_style: "H6"
        font_size: "25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]   
    
    MDLabel: 
        text: "Faites attention à votre propre sécurité en sécurisant les lieux."
        pos_hint: {"center_x":0.5, "center_y":0.525}
        halign: "center"
        font_style: "Body1"
        font_size: "20dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
                            
    MDRectangleFlatButton:
        text: "OK"
        pos_hint: {"center_x": 0.5, "center_y":0.3}
        size_hint: (0.3, 0.075)
        on_press: root.manager.current = "Two"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<TwoScreen>:
    name: "Two"
    
    MDLabel: 
        text: "La victime ..."
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel: 
        text: "1. perd beaucoup de sang à cause d’une blessure."
        pos_hint: {"center_x":0.5, "center_y":0.65}
        halign: "center"
        font_style: "Body2"
        font_size:"20dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "2. s'étouffe."
        pos_hint: {"center_x":0.5, "center_y":0.55}
        halign: "center"
        font_style: "Body2"
        font_size:"20dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "3. est conscinente/parle."
        pos_hint: {"center_x":0.5, "center_y":0.47}
        halign: "center"
        font_style: "Body2"
        font_size:"20dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "4. semble inconsciente."
        pos_hint: {"center_x":0.5, "center_y":0.39}
        halign: "center"
        font_style: "Body2"
        font_size:"20dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDRectangleFlatButton: 
        text: "1"
        pos_hint: {"center_x":0.2, "center_y":0.28}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Hemo1"
    
    MDRectangleFlatButton: 
        text: "2"
        pos_hint: {"center_x":0.4, "center_y":0.28}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "W"
    
    MDRectangleFlatButton: 
        text: "3"
        pos_hint: {"center_x":0.6, "center_y":0.28}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "VC"
    
    MDRectangleFlatButton: 
        text: "4"
        pos_hint: {"center_x":0.8, "center_y":0.28}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Cons"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<HemoScreen1>:
    name: "Hemo1"
    
    MDLabel: 
        text: "La victime subit une hémorragie externe"
        pos_hint: {"center_x":0.5, "center_y":0.72}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]
    
    MDLabel: 
        text: "1. Protégez vos mains du sang: mettez des gants, des sacs plastiques, etc…"
        pos_hint: {"center_x":0.5, "center_y":0.6}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "2. Si vous constatez un corps étranger, n'appuyez et ne l'enlevez pas."
        pos_hint: {"center_x":0.5, "center_y":0.5}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "3. Arrêtez le saignement en appuyant directement sur la blessure."
        pos_hint: {"center_x":0.5, "center_y":0.4}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "4. Allongez la victime, et surélevez le membre qui saigne."
        pos_hint: {"center_x":0.5, "center_y":0.3}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDRectangleFlatButton: 
        text: "Suite"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Hemo2"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
    
<HemoScreen2>:
    name: "Hemo2"
        
    MDLabel: 
        text: "Pansement compressif"
        pos_hint: {"center_x":0.5, "center_y":0.78}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel:
        text: "5. Utilisez du tissu, du papier épais ou des mouchoirs pour fabriquer un tampon couvrant toute la plaie."
        pos_hint: {"center_x": 0.5, "center_y": 0.67}
        halign: "center"
        font_style: "Body2"
        font_size: "14dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "6. Tenez le en place avec un lien large (chaussette, bout de tissu) bien serré. La pression doit arrêter le saignement."
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        halign: "center"
        font_style: "Body2"
        font_size: "14dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "7. Appelez les secours et indiquez: la location, l’âge, le sexe et l’état de la victime (hémorragie externe)."
        pos_hint: {"center_x": 0.5, "center_y": 0.43}
        halign: "center"
        font_style: "Body2"
        font_size: "14dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDLabel:
        text: "8. Surveillez la victime et ne lui donnez pas à boire. Si elle perd conscience, adoptez la démarche nécessaire. "
        pos_hint: {"center_x": 0.5, "center_y": 0.31}
        halign: "center"
        font_style: "Body2"
        font_size: "14dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDRectangleFlatButton: 
        text: "Inconsciente"
        pos_hint: {"center_x":0.3, "center_y":0.2}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Cons"
    
    MDRectangleFlatButton: 
        text: "     Terminer    "
        pos_hint: {"center_x":0.7, "center_y":0.2}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<EtouffWScreen>:
    name: "W"

    MDLabel: 
        text: "La victime ..."
        pos_hint: {"center_x":0.5, "center_y":0.7}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel: 
        text: "1. tousse et parle."
        pos_hint: {"center_x":0.5, "center_y":0.6}
        halign: "center"
        font_style: "Body2"
        font_size:"20dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "2. ne peut pas tousser ou parler."
        pos_hint: {"center_x":0.5, "center_y":0.5}
        halign: "center"
        font_style: "Body2"
        font_size:"20dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
      
    MDRectangleFlatButton:
        text: "1"
        pos_hint: {"center_x":0.35, "center_y":0.35}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "EP"
    
    MDRectangleFlatButton: 
        text: "2"
        pos_hint: {"center_x":0.65, "center_y":0.35}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Etouff1"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<EtouffPScreen>:
    name: "EP"
    
    MDLabel: 
        text: "Obstruction incomplète"
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel: 
        text: "1. Ne touchez pas la victime, laissez la dans la position qu’elle préfère."
        pos_hint: {"center_x":0.5, "center_y":0.6}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "2. Encouragez la victime à tousser jusqu’à ce que le problème soit réglé.."
        pos_hint: {"center_x":0.5, "center_y":0.5}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "3. Ne lui donnez ni à manger, ni à boire."
        pos_hint: {"center_x":0.5, "center_y":0.4}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDRectangleFlatButton: 
        text: "Terminer"
        pos_hint: {"center_x":0.5, "center_y":0.25}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<EtouffAgeScreen>:
    name:"Etouff1"
    
    MDLabel: 
        text: "La victime est..."
        pos_hint: {"center_x":0.5, "center_y":0.7}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel:
        text: "1. Un adulte/enfant"
        pos_hint: {"center_x": 0.5, "center_y": 0.62}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "2. Un bébé"
        pos_hint: {"center_x": 0.5, "center_y": 0.54}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "3. Obèse ou enceinte"
        pos_hint: {"center_x": 0.5, "center_y": 0.46}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
       
    MDRectangleFlatButton: 
        text: "1"
        pos_hint: {"center_x":0.3, "center_y":0.34}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Etouff2"
    
    MDRectangleFlatButton: 
        text: "2"
        pos_hint: {"center_x":0.5, "center_y":0.34}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Etouff4"
    
    MDRectangleFlatButton: 
        text: "3"
        pos_hint: {"center_x":0.7, "center_y":0.34}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Etouff6"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
    
<EtouffA1Screen>:
    name: "Etouff2"

    MDLabel: 
        text: "Obstruction complète"
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel:
        text: "1. Appelez les secours et indiquez: la location, l’âge, le sexe et l’état de la victime (étouffement)."
        pos_hint: {"center_x": 0.5, "center_y": 0.63}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "2. Penchez la victime en avant."
        pos_hint: {"center_x": 0.5, "center_y": 0.53}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "3. Tapez 5 fois entre les omoplates vigoureusement avec la paume de la main."
        pos_hint: {"center_x": 0.5, "center_y": 0.43}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDRectangleFlatButton: 
        text: "Suite"
        pos_hint: {"center_x":0.5, "center_y":0.3}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Etouff3"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
    
<EtouffA2Screen>:
    name:"Etouff3"
   
    MDLabel: 
        text: "Prise de heimlich"
        pos_hint: {"center_x":0.5, "center_y":0.8}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]
 
    MDLabel:
        text: "4. Placez vous derrière la victime, et placez votre poing en dessous des côtes, au milieu de l'abdomen."
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "5. Placez votre deuxième main sur le poing."
        pos_hint: {"center_x": 0.5, "center_y": 0.58}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "6. Tirez vers vous 5 fois d’un coup sec, en faisant un mouvement en forme de “J”."
        pos_hint: {"center_x": 0.5, "center_y": 0.47}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "7. Alternez les 5 tapes et 5 pressions jusqu’à ce que le problème soit réglé, ou si la victime perd conscience."
        pos_hint: {"center_x": 0.5, "center_y": 0.33}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDRectangleFlatButton: 
        text: "Inconsciente"
        pos_hint: {"center_x":0.3, "center_y":0.2}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Cons"

    MDRectangleFlatButton: 
        text: "  Terminer   "
        pos_hint: {"center_x":0.7, "center_y":0.2}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<EtouffB1Screen>:
    name:"Etouff4"
 
    MDLabel: 
        text: "Obstruction complète: bébé"
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]
 
    MDLabel:
        text: "1. Appelez les secours et indiquez: la location, l’âge, le sexe et l’état de la victime (étouffement)."
        pos_hint: {"center_x": 0.5, "center_y": 0.61}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "2. Placez le bébé sur votre cuisse, la tête en bas. "
        pos_hint: {"center_x": 0.5, "center_y": 0.49}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "3. En tenant la tête du bébé, effectuez 5 tapes entre ses omoplates."
        pos_hint: {"center_x": 0.5, "center_y": 0.39}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDRectangleFlatButton: 
        text: "Suite"
        pos_hint: {"center_x":0.5, "center_y":0.28}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Etouff5"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<EtouffB2Screen>:
    name:"Etouff5"
 
    MDLabel: 
        text: "Compressions"
        pos_hint: {"center_x":0.5, "center_y":0.8}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel:
        text: "1. Retournez le bébé doucement sur votre cuisse, en maintenant sa tête et en gardant sa tête vers le bas."
        pos_hint: {"center_x": 0.5, "center_y": 0.68}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "2. Placez deux doigts de la même main sur le sternum du bébé."
        pos_hint: {"center_x": 0.5, "center_y": 0.56}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "3. Effectuez 5 compressions à deux doigts."
        pos_hint: {"center_x": 0.5, "center_y": 0.46}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDLabel:
        text: "4. Répétez le cycle 5 tapes et 5 compressions jusqu’à ce que le problème soit réglé, ou si le bébé perd conscience."
        pos_hint: {"center_x": 0.5, "center_y": 0.34}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
           
    MDRectangleFlatButton: 
        text: "Inconsciente"
        pos_hint: {"center_x":0.3, "center_y":0.225}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Cons"
    
    MDRectangleFlatButton: 
        text: "  Terminer  "
        pos_hint: {"center_x":0.7, "center_y":0.225}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<EtouffOE1Screen>:
    name: "Etouff6"

    MDLabel: 
        text: "Obstruction complète"
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel:
        text: "1. Appelez les secours et indiquez: la location, l’âge, le sexe et l’état de la victime (étouffement)."
        pos_hint: {"center_x": 0.5, "center_y": 0.63}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "2. Penchez la victime en avant."
        pos_hint: {"center_x": 0.5, "center_y": 0.53}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "3. Tapez 5 fois entre les omoplates vigoureusement avec la paume de la main."
        pos_hint: {"center_x": 0.5, "center_y": 0.43}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDRectangleFlatButton: 
        text: "Suite"
        pos_hint: {"center_x":0.5, "center_y":0.3}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Etouff7"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
    
<EtouffOE2Screen>:
    name:"Etouff7"
   
    MDLabel: 
        text: "Prise de heimlich"
        pos_hint: {"center_x":0.5, "center_y":0.8}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]
 
    MDLabel:
        text: "4. Placez vous derrière la victime, contre son dos, et placez votre poing au milieu de son sternum."
        pos_hint: {"center_x": 0.5, "center_y": 0.69}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "5. Placez votre deuxième main sur le poing,"
        pos_hint: {"center_x": 0.5, "center_y": 0.57}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "6. Tirez vers vous 5 fois d’un coup sec, en faisant un mouvement en forme de “J”."
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "7. Alternez les 5 tapes et 5 pressions jusqu’à ce que le problème soit réglé, ou si la victime perd conscience."
        pos_hint: {"center_x": 0.5, "center_y": 0.31}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDRectangleFlatButton: 
        text: "Inconsciente"
        pos_hint: {"center_x":0.3, "center_y":0.19}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Cons"

    MDRectangleFlatButton: 
        text: "  Terminer   "
        pos_hint: {"center_x":0.7, "center_y":0.19}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<VCScreen>:
    name:"VC"

    MDLabel: 
        text: "La victime..."
        pos_hint: {"center_x":0.5, "center_y":0.8}
        halign: "center"
        font_style: "H6"
        font_size: "24dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel: 
        text: "1. Ressent une forte douleur oppressive et pesante à la poitrine."
        pos_hint: {"center_x":0.5, "center_y":0.71}
        halign: "center"
        font_style: "Body2"
        font_size: "16dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "2. Présente un ou plusieurs des signes suivants:"
        pos_hint: {"center_x":0.5, "center_y":0.62}
        halign: "center"
        font_style: "Body2"
        font_size: "16dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    Image: 
        source: "AVC_2.png"
        pos_hint: {"center_x":0.5, "center_y":0.4}
        size_hint_x: 0.55
        size_hint_y: 0.55
    
    MDRectangleFlatButton: 
        text: "1"
        pos_hint: {"center_x":0.35, "center_y":0.18}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Crise"
    
    MDRectangleFlatButton: 
        text: "2"
        pos_hint: {"center_x":0.65, "center_y":0.18}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "AVC"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
    
<AVCScreen>:
    name: "AVC"
    
    MDLabel: 
        text: "La victime subit un AVC"
        pos_hint: {"center_x":0.5, "center_y":0.8}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]
 
    MDLabel:
        text: "1. Appelez les secours au plus vite et indiquez: la location, l’âge, le sexe et l’état de la victime (AVC)."
        pos_hint: {"center_x": 0.5, "center_y": 0.69}
        halign: "center"
        font_style: "Body2"
        font_size: "16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "2. Installez la victime confortablement, en évitant de la faire bouger."
        pos_hint: {"center_x": 0.5, "center_y": 0.57}
        halign: "center"
        font_style: "Body2"
        font_size: "16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "3. Ne donnez pas à manger, ni à boire."
        pos_hint: {"center_x": 0.5, "center_y": 0.49}
        halign: "center"
        font_style: "Body2"
        font_size: "16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDLabel:
        text: "4. Surveillez la victime constamment, et rassurez-la."
        pos_hint: {"center_x": 0.5, "center_y": 0.41}
        halign: "center"
        font_style: "Body2"
        font_size: "16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDLabel:
        text: "5. Si la victime perd conscience, adoptez les gestes nécessaires."
        pos_hint: {"center_x": 0.5, "center_y": 0.31}
        halign: "center"
        font_style: "Body2"
        font_size: "16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDRectangleFlatButton: 
        text: "Inconsciente"
        pos_hint: {"center_x":0.3, "center_y":0.19}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Cons"

    MDRectangleFlatButton: 
        text: "  Terminer   "
        pos_hint: {"center_x":0.7, "center_y":0.19}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
    
<CriseScreen>:
    name:"Crise"
    
    MDLabel: 
        text: "Douleurs thoraciques"
        pos_hint: {"center_x":0.5, "center_y":0.8}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel:
        text: "1. Appelez les secours et indiquez: la location, l’âge, le sexe et l’état de la victime (douleurs thoraciques)."
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "2. Installez la victime confortablement; elle ne doit faire aucun effort."
        pos_hint: {"center_x": 0.5, "center_y": 0.59}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "3. Desserez lui ses habits (exemple: enlevez la cravate ou déboutonner la chemise."
        pos_hint: {"center_x": 0.5, "center_y": 0.48}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDLabel:
        text: "4. Surveillez la constamment. Rassurez la victime et parlez-lui."
        pos_hint: {"center_x": 0.5, "center_y": 0.37}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    MDLabel:
        text: "5. Si la victime perd conscience, adoptez les gestes nécessaires."
        pos_hint: {"center_x": 0.5, "center_y": 0.28}
        halign: "center"
        font_style: "Body2"
        font_size:"16dp"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
          
    MDRectangleFlatButton: 
        text: "Inconsciente"
        pos_hint: {"center_x":0.3, "center_y":0.18}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Cons"

    MDRectangleFlatButton: 
        text: "  Terminer  "
        pos_hint: {"center_x":0.7, "center_y":0.18}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<ConsScreen>:
    name:"Cons"
    MDLabel: 
        text: "Vérifiez l’état de conscience de la victime"
        pos_hint: {"center_x":0.5, "center_y":0.7}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel: 
        text: "1. Répond-t-elle à la stimulation verbale ?"
        pos_hint: {"center_x":0.5, "center_y":0.575}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "2. Répond-t-elle à la stimulation douleureuse ?"
        pos_hint: {"center_x":0.5, "center_y":0.475}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDRectangleFlatButton: 
        text: "Oui"
        font_style: "Button"
        pos_hint: {"center_x":0.3, "center_y":0.35}
        halign: "center"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [25,0]
        on_press: root.manager.current = "VC"
        
    MDRectangleFlatButton: 
        text: "Non"
        font_style: "Button"
        pos_hint: {"center_x":0.7, "center_y":0.35}
        halign: "center"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [25,0]
        on_press: root.manager.current = "Respi1"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
                     
<RespiScreen1>:
    name: "Respi1"

    MDLabel: 
        text: "Est-ce que la victime respire ?"
        pos_hint: {"center_x":0.5, "center_y":0.8}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel: 
        text: "1. Mettez une main sur le front, et deux doigts sous le menton."
        pos_hint: {"center_x":0.5, "center_y":0.7}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "2. Basculez gentiment la tête en arrière."
        pos_hint: {"center_x":0.5, "center_y":0.6}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    Image: 
        source: "Respi_check.png"
        pos_hint: {"center_x":0.5, "center_y":0.385}
        size_hint_x: 0.5
        size_hint_y: 0.5
        
    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.18}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "Respi2"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
                       
<RespiScreen2>:
    name: "Respi2"
    
    MDLabel: 
        text: "Est-ce que la victime respire ?"
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel: 
        text: "1. Approchez vous de sa bouche et écoutez: Entendez-vous une respiration ?"
        pos_hint: {"center_x":0.5, "center_y":0.6}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "2. Mettez votre main sur l'abdomen de la victime: Sentez-vous un mouvement ?"
        pos_hint: {"center_x":0.5, "center_y":0.45}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDRectangleFlatButton: 
        text: "Oui"
        font_style: "Button"
        pos_hint: {"center_x":0.3, "center_y":0.275}
        halign: "center"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [25,0]
        on_press: root.manager.current = "PLS1"
        
    MDRectangleFlatButton: 
        text: "Non"
        font_style: "Button"
        pos_hint: {"center_x":0.7, "center_y":0.275}
        halign: "center"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [25,0]
        on_press: root.manager.current = "CPRAge"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
    
<PLS1>:
    name: "PLS1"

    MDLabel: 
        text: "PLS"
        pos_hint: {"center_x":0.5, "center_y":0.825}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel: 
        text: "1. Appelez les secours au plus vite et indiquez: la location, l’âge, le sexe et l’état de la victime (Inconsciente et respire)."
        pos_hint: {"center_x":0.5, "center_y":0.74}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "2. Mettez la victime sur son dos."
        pos_hint: {"center_x":0.5, "center_y":0.66}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "3. Prenez le bras le plus proche de vous et placez-le à angle droit par rapport à la victime."
        pos_hint: {"center_x":0.5, "center_y":0.58}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    Image: 
        source: "PLS_arm.png"
        pos_hint: {"center_x":0.5, "center_y":0.375}
        size_hint_x: 0.5
        size_hint_y:0.4

    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.175}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "PLS2"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
                       
<PLS2>:
    name: "PLS2"

    MDLabel: 
        text: "4. Pliez vers le haut le genou le plus loin de vous."
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    Image: 
        source: "PLS_knee.png"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size_hint_x: 0.6
        size_hint_y:0.6
    
    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.25}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "PLS3"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
    
<PLS3>:
    name: "PLS3"

    MDLabel: 
        text: "5. Placez une de vos mains sur le genou plié, et l’autre sur l’épaule non-étendue."
        pos_hint: {"center_x":0.5, "center_y":0.785}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "6. Ramenez le corps doucement vers vous, de manière à mettre la victime sur le côté."
        pos_hint: {"center_x":0.5, "center_y":0.7}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "7. Surveillez la victime."
        pos_hint: {"center_x":0.5, "center_y":0.63}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "8. Si la victime arrête de respirer, adoptez les gestes nécessaires."
        pos_hint: {"center_x":0.5, "center_y":0.56}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    Image: 
        source: "PLS_final.png"
        pos_hint: {"center_x":0.5, "center_y":0.38}
        size_hint_x: 0.4
        size_hint_y:0.4
    
    MDRectangleFlatButton: 
        text: "Ne respire pas"
        pos_hint: {"center_x":0.25, "center_y":0.2}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRAge"

    MDRectangleFlatButton: 
        text: "   Terminer    "
        pos_hint: {"center_x":0.75, "center_y":0.2}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
    
<CPRAge>:
    name: "CPRAge"
    
    MDLabel: 
        text: "La victime est..."
        pos_hint: {"center_x":0.5, "center_y":0.7}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel:
        text: "1. Un adulte"
        pos_hint: {"center_x": 0.5, "center_y": 0.62}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "2. Un enfant"
        pos_hint: {"center_x": 0.5, "center_y": 0.54}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "3. Un bébé"
        pos_hint: {"center_x": 0.5, "center_y": 0.46}
        halign: "center"
        font_style: "Body1"
        font_size: "35"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    
    MDRectangleFlatButton: 
        text: "1"
        pos_hint: {"center_x":0.3, "center_y":0.34}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRA1"
    
    MDRectangleFlatButton: 
        text: "2"
        pos_hint: {"center_x":0.5, "center_y":0.34}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRE1"
    
    MDRectangleFlatButton: 
        text: "3"
        pos_hint: {"center_x":0.7, "center_y":0.34}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRB1"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
        
<CPRA1>:
    name: "CPRA1"
    
    MDLabel: 
        text: "Massage cardiaque adulte"
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]
    
    MDLabel: 
        text: "1. Appelez les secours au plus vite et indiquez: la location, l’âge, le sexe et l’état de la victime (Inconsciente et ne respire pas)."
        pos_hint: {"center_x":0.5, "center_y":0.635}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "2. Envoyez quelqu’un chercher un défibrillateur, pendant que vous suivez les instructions sur l’écran."
        pos_hint: {"center_x":0.5, "center_y":0.5}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "3. Placez la victime sur le dos."
        pos_hint: {"center_x":0.5, "center_y":0.41}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "4. Déshabillez la victime: son thorax doit être nu."
        pos_hint: {"center_x":0.5, "center_y":0.33}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.225}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRA2"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12
                       
<CPRA2>:
    name: "CPRA2" 
 
    MDLabel: 
        text: "5. Mettez vous à genoux à la hauteur des épaules de la victime."
        pos_hint: {"center_x":0.5, "center_y":0.785}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "6. Placez le talon de votre main sur le sternum (entre les mamelons)."
        pos_hint: {"center_x":0.5, "center_y":0.705}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "7. Placez l’autre main au-dessus de la première."
        pos_hint: {"center_x":0.5, "center_y":0.625}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "8. Utilisez le poids de votre corps pour compresser, en gardant les bras tendus, en angle droit."
        pos_hint: {"center_x":0.5, "center_y":0.535}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    Image: 
        source: "CPR_adulte.png"
        pos_hint: {"center_x":0.5, "center_y":0.35}
        size_hint_x: 0.4
        size_hint_y:0.4
    
    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.175}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRC"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12

<CPRC>:
    name: "CPRC"

    MDLabel: 
        text: "Conseils"
        pos_hint: {"center_x":0.5, "center_y":0.8}
        halign: "center"
        font_style: "H6"
        font_size:"25dp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]
        
    MDLabel: 
        text: "1. Appuyez vite et fort au rythme de “Stayin’ alive”, en laissant le thorax revenir à sa position initiale entre les compressions."
        pos_hint: {"center_x":0.5, "center_y":0.69}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "2. Essayez de changer de masseur toutes les deux minutes."
        pos_hint: {"center_x":0.5, "center_y":0.575}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "3. N’arrêtez le massage seulement si les ambulanciers vous le demandent, si la victime recommence à respirer, si le défibrillateur le demande, ou si vous êtes trop fatigués."
        pos_hint: {"center_x":0.5, "center_y":0.44}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "4.Dès que vous êtes en possession d’un défibrillateur, cliquez 'AED'."
        pos_hint: {"center_x":0.5, "center_y":0.3}
        halign: "center"
        font_style: "Body2"
        font_size:"15dp"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
 
    MDRectangleFlatButton: 
        text: "    AED    "
        pos_hint: {"center_x":0.3, "center_y":0.2}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "AED1"

    MDRectangleFlatButton: 
        text: "Terminer"
        pos_hint: {"center_x":0.7, "center_y":0.2}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
        
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 

<CPRE1>:
    name: "CPRE1"
    
    MDLabel: 
        text: "Massage cardiaque enfant"
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]
    
    MDLabel: 
        text: "1. Appelez les secours au plus vite et indiquez: la location, l’âge, le sexe et l’état de la victime (Inconsciente et ne respire pas)."
        pos_hint: {"center_x":0.5, "center_y":0.635}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "2. Envoyez quelqu’un chercher un défibrillateur, pendant que vous suivez les instructions sur l’écran."
        pos_hint: {"center_x":0.5, "center_y":0.5}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "3. Placez la victime sur le dos."
        pos_hint: {"center_x":0.5, "center_y":0.41}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "4. Déshabillez la victime: son thorax doit être nu."
        pos_hint: {"center_x":0.5, "center_y":0.33}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.225}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRE2"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 
                       
<CPRE2>:
    name: "CPRE2" 

    MDLabel: 
        text: "5. Mettez vous à genoux à la hauteur des épaules de la victime."
        pos_hint: {"center_x":0.5, "center_y":0.785}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "6. Placez une main sur le sternum (entre les mamelons)."
        pos_hint: {"center_x":0.5, "center_y":0.7}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "7. Placez l’autre main sur votre cuisse."
        pos_hint: {"center_x":0.5, "center_y":0.63}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "8. Utilisez le poids de votre corps pour compresser, en  gardant votre bras tendu, en angle droit."
        pos_hint: {"center_x":0.5, "center_y":0.56}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    Image: 
        source: "CPR_enfant.png"
        pos_hint: {"center_x":0.5, "center_y":0.375}
        size_hint_x: 0.4
        size_hint_y:0.4
    
    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.19}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRC"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 
    
<CPRB1>:
    name: "CPRB1"
      
    MDLabel: 
        text: "Massage cardiaque bébé"
        pos_hint: {"center_x":0.5, "center_y":0.75}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]
    
    MDLabel: 
        text: "1. Appelez les secours au plus vite et indiquez: la location, l’âge, le sexe et l’état de la victime (Inconsciente et ne respire pas)."
        pos_hint: {"center_x":0.5, "center_y":0.62}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "2. Envoyez quelqu’un chercher un défibrillateur, pendant que vous suivez les instructions sur l’écran."
        pos_hint: {"center_x":0.5, "center_y":0.48}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "3. Placez le bébé sur le dos."
        pos_hint: {"center_x":0.5, "center_y":0.38}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "4. Déshabillez le bébé: son thorax doit être nu."
        pos_hint: {"center_x":0.5, "center_y":0.3}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRB2"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 
    

<CPRB2>:
    name: "CPRB2"
        
    MDLabel: 
        text: "5. Placez un linge ou autre en dessous des épaules du bébé."
        pos_hint: {"center_x":0.5, "center_y":0.725}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        
    MDLabel: 
        text: "6. Placez deux doigts de la même main (ou les deux pouces) sur le bas du sternum du bébé, et compressez."
        pos_hint: {"center_x":0.5, "center_y":0.62}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "7. Massez en continu."
        pos_hint: {"center_x":0.5, "center_y":0.53}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    Image: 
        source: "CPR_bébé.png"
        pos_hint: {"center_x":0.5, "center_y":0.375}
        size_hint_x: 0.55
        size_hint_y:0.55

    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRC"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 
                       
<AED1>:
    name: "AED1"
    MDLabel: 
        text: "Utilisation du défibrillateur"
        pos_hint: {"center_x":0.5, "center_y":0.8}
        halign: "center"
        font_style: "H6"
        font_size:"40"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        padding: [20,0]

    MDLabel:
        text: "1. Continuez le massage, sauf quand l’appareil vous demande d’arrêter. Évitez tout contact avec l’eau."
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "2. Allumez l’appareil et suivez les instructions. Mettez le en mode pédiatrique si besoin."
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]

    MDLabel:
        text: "3. Placez les électrodes comme montré sur le schéma."
        pos_hint: {"center_x": 0.5, "center_y": 0.52}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0, 0, 0, 1)
        padding: [25, 0]
    
    Image: 
        source: "AED_pos.png"
        pos_hint: {"center_x":0.5, "center_y":0.35}
        size_hint_x: 0.4
        size_hint_y:0.4
    
    MDRectangleFlatButton: 
        text: "Suite"
        font_style: "Button"
        pos_hint: {"center_x":0.5, "center_y":0.18}
        halign: "center"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "AED2"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 
    
<AED2>:
    name: "AED2"
        
    MDLabel: 
        text: "4. Pendant que la machine évalue, arrêtez le massage et ne touchez plus la victime."
        pos_hint: {"center_x":0.5, "center_y":0.72}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]

    MDLabel: 
        text: "5. Si un choc est nécessaire, éloignez vous de la victime, et criez: 'PERSONNE TOUCHE LA VICTIME'."
        pos_hint: {"center_x":0.5, "center_y":0.6}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "6. Appuyez sur le bouton pour administrer le choc."
        pos_hint: {"center_x":0.5, "center_y":0.48}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDLabel: 
        text: "7. Suivez les instructions de la machine, puis répétez les étapes 4 à 7 si nécessaire."
        pos_hint: {"center_x":0.5, "center_y":0.39}
        halign: "center"
        font_style: "Body2"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
    
    MDRectangleFlatButton: 
        text: "Conseils"
        pos_hint: {"center_x":0.3, "center_y":0.28}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "CPRC"

    MDRectangleFlatButton: 
        text: "  Terminer   "
        pos_hint: {"center_x":0.7, "center_y":0.28}
        halign: "center"
        font_style: "Button"
        theme_text_color: "Custom"
        text_color: (0,0,0,1)
        padding: [25,0]
        on_press: root.manager.current = "home"
    
    BoxLayout: 
        orientation: "vertical"
        spacing:"10dp"
        MDToolbar: 
            title: "Premiers Secours"
            elevation: 10
            specific_text_color: (1,1,1,1)
        Widget: 
        MDToolbar:
        
    MDFloatingActionButton: 
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x":0.5, "center_y":0.065}
        on_release: root.manager.current = "home"
        md_bg_color: (1,1,1,1) 
        elevation_normal: 12 
        
<Screen1>:
    name: "one"
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Location AED"
            right_action_items: [["magnify", lambda x: app.search_menu2()]]
            elevation: 10
            specific_text_color: (1, 1, 1, 1)

        MapView:
            id: content
            lat: 46.2044
            lon: 6.1432
            zoom: 12
            double_tap_zoom: True
            on_lat:
                print("lat", self.lat)
            on_lon:
                print("lon", self.lon)

        MDToolbar:

    MDFloatingActionButton:
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x": 0.5, "center_y": 0.065}
        on_release: app.root.current = "home"
        md_bg_color: (1, 1, 1, 1)
        elevation_normal: 12

<Screen2>:
    name: "two"
    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Location AED"
            elevation: 10
            specific_text_color: (1, 1, 1, 1)

        ScrollView:
            MDList:
                id: content
                on_touch_down: app.root.current = "three"

        MDToolbar:

    MDFloatingActionButton:
        icon: "home"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x": 0.5, "center_y": 0.065}
        on_release: app.root.current = "home"
        md_bg_color: (1, 1, 1, 1)
        elevation_normal: 12

<Screen3>:
    name: "three"

    MDLabel:
        text: "Copiez-collez cette adresse dans google pour aller chercher l'AED"
        font_size:"12dp"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x": 0.5, "center_y": 0.17}
        halign: "center"


    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Location AED"
            elevation: 10
            specific_text_color: (1, 1, 1, 1)

        FloatLayout:
            id: nidhi

        MDToolbar:

    MDFloatingActionButton:
        icon: "arrow-left-bold"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x": 0.5, "center_y": 0.065}
        on_press: app.root.current = "one"
        md_bg_color: (1, 1, 1, 1)
        elevation_normal: 12

"""

class HomeScreen(Screen):
    pass
class SearchScreen(Screen):
    pass
class Content(BoxLayout):
    pass
class Container(BoxLayout):
    pass
class IntroScreen(Screen):
    pass
class LinksScreen(Screen):
    pass
class AssoScreen(Screen):
    pass
class LawScreen(Screen):
    pass
class PremrepScreen(Screen):
    pass
class MoreaedScreen(Screen):
    pass
class MorePSScreen(Screen):
    pass
class LieuScreen(Screen):
    pass
class TwoScreen(Screen):
    pass
class HemoScreen1(Screen):
    pass
class HemoScreen2(Screen):
    pass
class EtouffWScreen(Screen):
    pass
class EtouffPScreen(Screen):
    pass
class EtouffAgeScreen(Screen):
    pass
class EtouffA1Screen(Screen):
    pass
class EtouffA2Screen(Screen):
    pass
class EtouffB1Screen(Screen):
    pass
class EtouffB2Screen(Screen):
    pass
class EtouffOE1Screen(Screen):
    pass
class EtouffOE2Screen(Screen):
    pass
class VCScreen(Screen):
    pass
class AVCScreen(Screen):
    pass
class CriseScreen(Screen):
    pass
class ConsScreen(Screen):
    pass
class RespiScreen1(Screen):
    pass
class RespiScreen2(Screen):
    pass
class PLS1(Screen):
    pass
class PLS2(Screen):
    pass
class PLS3(Screen):
    pass
class CPRAge(Screen):
    pass
class CPRA1(Screen):
    pass
class CPRA2(Screen):
    pass
class CPRE1(Screen):
    pass
class CPRE2(Screen):
    pass
class CPRB1(Screen):
    pass
class CPRB2(Screen):
    pass
class CPRC(Screen):
    pass
class AED1(Screen):
    pass
class AED2(Screen):
    pass
class Screen1(Screen):
    pass
class Screen2(Screen):
    pass
class Screen3(Screen):
    pass
class Content2(BoxLayout):
    pass

sm=ScreenManager()
sm.add_widget(HomeScreen(name="home"))
sm.add_widget(SearchScreen(name="Search"))
sm.add_widget(IntroScreen(name="intro"))
sm.add_widget(LinksScreen(name="links"))
sm.add_widget(AssoScreen(name="asso"))
sm.add_widget(LawScreen(name="law"))
sm.add_widget(PremrepScreen(name="premrep"))
sm.add_widget(MoreaedScreen(name="moreaed"))
sm.add_widget(MorePSScreen(name="moreps"))
sm.add_widget(LieuScreen(name="Lieu"))
sm.add_widget(TwoScreen(name="Two"))
sm.add_widget(HemoScreen1(name="Hemo1"))
sm.add_widget(HemoScreen2(name="Hemo2"))
sm.add_widget(EtouffWScreen(name="W"))
sm.add_widget(EtouffPScreen(name="EP"))
sm.add_widget(EtouffAgeScreen(name="Etouff1"))
sm.add_widget(EtouffA1Screen(name="Etouff2"))
sm.add_widget(EtouffA2Screen(name="Etouff3"))
sm.add_widget(EtouffB1Screen(name="Etouff4"))
sm.add_widget(EtouffB2Screen(name="Etouff5"))
sm.add_widget(EtouffOE1Screen(name="Etouff6"))
sm.add_widget(EtouffOE2Screen(name="Etouff7"))
sm.add_widget(VCScreen(name="VC"))
sm.add_widget(CriseScreen(name="Crise"))
sm.add_widget(AVCScreen(name="AVC"))
sm.add_widget(ConsScreen(name="Cons"))
sm.add_widget(RespiScreen1(name="Respi1"))
sm.add_widget(RespiScreen2(name="Respi2"))
sm.add_widget(PLS1(name="PLS1"))
sm.add_widget(PLS2(name="PLS2"))
sm.add_widget(PLS3(name="PLS3"))
sm.add_widget(CPRC(name="CPRC"))
sm.add_widget(CPRAge(name="CPRAge"))
sm.add_widget(CPRA1(name="CPRA1"))
sm.add_widget(CPRA2(name="CPRA2"))
sm.add_widget(CPRE1(name="CPRE1"))
sm.add_widget(CPRE2(name="CPRE2"))
sm.add_widget(CPRB1(name="CPRB1"))
sm.add_widget(CPRB2(name="CPRB2"))
sm.add_widget(AED1(name="AED1"))
sm.add_widget(AED2(name="AED2"))
sm.add_widget(Screen1(name="one"))
sm.add_widget(Screen2(name="two"))
sm.add_widget(Screen3(name="three"))

class Home(MDApp):
    connection = None
    cursor = None
    dialog1 = None
    dialog2 = None

    # creating function for search menu dialog box
    def search_menu(self):
        self.caller = TextInput(
            size_hint_y=None, height=50, size_hint_x=None, width=350, cursor_color=(0, 0, 0, 1)
        )
        if not self.dialog1:
            self.dialog1 = MDDialog(
                title="Recherche (nom du pays)",
                type="custom",
                content_cls=Content()
            )
        self.dialog1.add_widget(self.caller)
        self.dialog1.open()

    def search_menu2(self):
        self.caller2 = TextInput(
            size_hint_y=None, height=50, size_hint_x=None, width=350, cursor_color=(0, 0, 0, 1)
        )
        if not self.dialog2:
            self.dialog2 = MDDialog(
                title="Recherche (nom de commune)",
                type="custom",
                content_cls=Content2()
            )
        self.dialog2.add_widget(self.caller2)
        self.dialog2.open()

    # creating function for adding list items from csv
    def on_start(self):
        self.connection = sqlite3.connect("Trial.db")
        with open('country_base.csv', 'r') as read_obj:
            csv_dict_reader = DictReader(read_obj)

            for row in csv_dict_reader:
                icon = IconLeftWidget(icon="phone", theme_text_color="Custom", text_color=self.theme_cls.primary_color)
                items = TwoLineIconListItem(
                    text=str(row['\ufeffCountry Name:']) + "  (" + str(row['Country Code:']) + " )",
                    secondary_text="Numéro d'urgence: " + str(row['Ambulance Number:']))
                items.add_widget(icon)
                self.root.get_screen('Search').ids.content.add_widget(items)

    # creating the dialog boxes
    def callback(self, *args):
        va = self.caller.text

        self.dialog1.dismiss()

        with open('country_base.csv', 'r') as read_obj:
            csv_dict_reader = DictReader(read_obj)

            for row in csv_dict_reader:

                if va == str(row['\ufeffCountry Name:']):
                    self.dialog_2 = MDDialog(
                        title=str(row['\ufeffCountry Name:']) + ": " + str(row['Ambulance Number:']),
                        type="custom",
                        content_cls=Container()
                    )
                    self.dialog_2.open()

    def callback2(self, *args):
        self.root.current = 'two'
        self.dialog2.dismiss()
        va2 = self.caller2.text
        self.root.get_screen('two').ids.content.clear_widgets()
        app = App.get_running_app()
        app.cursor = app.connection.cursor()
        sql_statement = "SELECT * FROM Try_again_csv WHERE Adresse like '%" + va2 + "%'"
        app.cursor.execute(sql_statement)
        aeds = app.cursor.fetchall()
        for aed in aeds:

            #creating the list with search results
            icon = IconLeftWidget(icon="google-maps", theme_text_color="Custom", text_color=self.theme_cls.primary_color)
            items = OneLineIconListItem(text=str(aed[0]), on_press=lambda x, a=str(aed[0]): app.select(a))
            items.add_widget(icon)
            self.root.get_screen('two').ids.content.add_widget(items)

        app.cursor.close()

    def select(self, a):
        self.root.get_screen('three').ids.nidhi.clear_widgets()
        app = App.get_running_app()
        app.cursor = app.connection.cursor()
        sql_statement = "SELECT * FROM Try_again_csv WHERE Adresse like '%" + a + "%'"
        app.cursor.execute(sql_statement)
        aeds = app.cursor.fetchall()
        for aed in aeds:
            self.box = GridLayout(
                cols=2,
                row_force_default=True,
                row_default_height=130,
                padding="12dp",
                pos_hint={'center_y': 0.5}
            )

            self.add1 = MDLabel(
                text="Addresse: ",
                bold=True,
                theme_text_color="Custom",
                text_color=app.theme_cls.primary_color
            )
            self.add2 = MDLabel(
                text=str(aed[0])
            )

            self.type1 = MDLabel(
                text="Type de lieu: ",
                bold=True,
                theme_text_color="Custom",
                text_color=app.theme_cls.primary_color
            )
            self.type2 = MDLabel(
                text=str(aed[1])
            )

            self.horaire1 = MDLabel(
                text="Horaire d'accès: ",
                bold=True,
                theme_text_color="Custom",
                text_color=app.theme_cls.primary_color
            )
            self.horaire2 = MDLabel(
                text=str(aed[2])
            )

            self.pos1 = MDLabel(
                text="Position: ",
                bold=True,
                theme_text_color="Custom",
                text_color=app.theme_cls.primary_color
            )
            self.pos2 = MDLabel(
                text=str(aed[3])
            )

            self.ped1 = MDLabel(
                text="Mode pédiatrique: ",
                bold=True,
                theme_text_color="Custom",
                text_color=app.theme_cls.primary_color
            )
            self.ped2 = MDLabel(
                text=str(aed[4])
            )

            self.box.add_widget(self.add1)
            self.box.add_widget(self.add2)
            self.box.add_widget(self.type1)
            self.box.add_widget(self.type2)
            self.box.add_widget(self.horaire1)
            self.box.add_widget(self.horaire2)
            self.box.add_widget(self.pos1)
            self.box.add_widget(self.pos2)
            self.box.add_widget(self.ped1)
            self.box.add_widget(self.ped2)
            self.root.get_screen('three').ids.nidhi.add_widget(self.box)

        app.cursor.close()

    def on_stop(self):
        self.connection.close()

    def sam_1(self):
        webbrowser.open("https://www.samariter.ch/fr")
    def sam_2(self):
        webbrowser.open("https://www.save-a-life.ch")
    def sam_3(self):
        webbrowser.open("https://www.save-a-life.ch/s-engager/")
    def sam_4(self):
        webbrowser.open("https://www.agss.ch/fr/rejoignez-nous-0")
    def sam_5(self):
        webbrowser.open("https://www.samariter.ch/fr/la-responsabilite-du-secouriste-non-professionnel")
    def sam_6(self):
        webbrowser.open("https://www.resuscitation.ch/fr/guidelines-2021")
    def sam_7(self):
        webbrowser.open("https://www.aed.ch/?lang=FR")
    def sam_8(self):
        webbrowser.open("https://www.save-a-life.ch/recenser-un-aed/")
    def sam_9(self):
        webbrowser.open("https://www.samariter.ch/fr/premiers-secours-quelques-conseils")

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "200"
        screen = Builder.load_string(home_helper)
        return screen


Home().run()














