from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
import add_servers
import json

Builder.load_file("MyGenerador.kv")

datos = {
   "Version" : "1",
   "ReleaseNotes" : "",
   "Servers" : []
}

lista_servidores = []

class MyLay(BoxLayout):
	def agregar_servidor(self, *args):
		alerta = ConfigServerAlert()
		alerta.open()
		
	def actualizar_spin(self):
		try:
			self.ids.serverSpinner.text = lista_servidores[0]
		except IndexError:
			print("No hay Servidores")
			
		except ValueError:
			print("Solo se acepta texto")
			
		self.ids.serverSpinner.values = lista_servidores
	
class ConfigServerAlert(Popup):
	def guardar_servidor(self):
		if self.ids.prtSslPay.active == True:
			nombre = self.ids.inpServerName.text
			
			servidor_sslpay = {
			   "Name" : nombre,
			   "FLAG" : "",
			   "Server IP" : "",
			   #"Server Port" : "",
			   "SSL Port" : "",
			   #"Proxy IP" : "",
			   #"Proxy Port" : "",
			   "ServerUser" : "",
			   "ServerPass" : "",
			   "Payload" : "",
			   "SNI" : "",
			   #"Slowchave" : "",
			   #"Nameserver" : "",
			   #"Slowdns" : "",
			   #"udpserver" : "",
			   #"udpauth" : "",
			   #"udpobfs" : "",
			   #"udpbuffer" : "",
			   #"udpdown" : "",
			   #"udpup" : "",
			   #"v2rayJson" : "",
			   "isSSL" : "false",
			   "isInject" : "false",
			   "isPayloadSSL" : "true",
			   "isDirect" : "false",
			   "isSlow" : "false",
			   "isUdp" : "false",
			   "isV2ray" : "false"
			   }
			datos["Servers"].append(servidor_sslpay)
			lista_servidores.append(servidor_sslpay["Name"])
			
			json_object = json.dumps(datos, indent=3)
			with open('/storage/emulated/0/prueba_server.txt', 'w') as archivo:
				archivo.write(json_object)
			
		else:
			pass
		
		self.dismiss()
		
	def check_fsslpay(self, is_active):
		if is_active:
			self.ids.prtSshSsl.active = False
			self.ids.prtSshProxy.active = False
			self.ids.prtSshDirect.active = False
			self.ids.prtSlowDns.active = False
			self.ids.prtUdp.active = False
			self.ids.prtV2ray.active = False
			
		else:
			pass
		
	def check_fssl(self, is_active):
		if is_active:
			self.ids.prtSslPay.active = False
			self.ids.prtSshProxy.active = False
			self.ids.prtSshDirect.active = False
			self.ids.prtSlowDns.active = False
			self.ids.prtUdp.active = False
			self.ids.prtV2ray.active = False
			
		else:
			pass
		
	def check_fproxy(self, is_active):
		if is_active:
			self.ids.prtSslPay.active = False
			self.ids.prtSshSsl.active = False
			self.ids.prtSshDirect.active = False
			self.ids.prtSlowDns.active = False
			self.ids.prtUdp.active = False
			self.ids.prtV2ray.active = False
			
		else:
			pass
		
	def check_fdirect(self, is_active):
		if is_active:
			self.ids.prtSslPay.active = False
			self.ids.prtSshSsl.active = False
			self.ids.prtSshProxy.active = False
			self.ids.prtSlowDns.active = False
			self.ids.prtUdp.active = False
			self.ids.prtV2ray.active = False
			
		else:
			pass
		
	def check_fslow(self, is_active):
		if is_active:
			self.ids.prtSslPay.active = False
			self.ids.prtSshSsl.active = False
			self.ids.prtSshProxy.active = False
			self.ids.prtSshDirect.active = False
			self.ids.prtUdp.active = False
			self.ids.prtV2ray.active = False
			
		else:
			pass
		
	def check_fudp(self, is_active):
		if is_active:
			self.ids.prtSslPay.active = False
			self.ids.prtSshSsl.active = False
			self.ids.prtSshProxy.active = False
			self.ids.prtSshDirect.active = False
			self.ids.prtSlowDns.active = False
			self.ids.prtV2ray.active = False
			
		else:
			pass
		
	def check_fv2ray(self, is_active):
		if is_active:
			self.ids.prtSslPay.active = False
			self.ids.prtSshSsl.active = False
			self.ids.prtSshProxy.active = False
			self.ids.prtSshDirect.active = False
			self.ids.prtSlowDns.active = False
			self.ids.prtUdp.active = False
			
		else:
			pass
	
class MyGen(App):
	def build(self):
		return MyLay()
		
if __name__ == "__main__":
	MyGen().run()