from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
import kivy.utils
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from tata.tatamapview import TataMapView

# Your layouts.
KV = (
    '''
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:include tata/tatamapview.kv

<MyBackdropBackLayer@ScrollView>
 
<MyBackdropFrontLayer@Screen>
 
 
<TataBackdrop>
    
    MDBackdrop:
        id: backdrop
        left_action_items: [['transfer-down', lambda x: self.open()]]
        title: "Press for nearby train and cargo services"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "services"
        
                            
        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                id: containers
                Image:
                    source: 'pic.jpg'
                    size: self.texture_size
 
        MDBackdropBackLayer:
            TataMapView:
                id:frontlayer
           
               
            
        
'''
)


class TataBackdrop(Screen): 
    pass
 
class TataBackDropLayout(FloatLayout):
    def run(self):
        Builder.load_string(KV)
        return TataBackdrop()
    