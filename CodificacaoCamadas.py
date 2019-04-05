
class Aplicacao():
    def __init__(self, mensagem):
        self.protocolo = 'dns'
        self.Mensagem =  mensagem
        self.Apresentacao = Apresentacao()

class Apresentacao():
    def __init__(self):
        self.protocolo = 'tcp'
        self.Sessao = Sessao()

class Sessao():
    def __init__(self):
        self.protocolo = 'udp'
        self.Transporte = Transporte()

class Transporte():
    def __init__(self):
      self.protocolo = 'tcp'
      self.Rede = Rede()


class Rede():
    def __init__(self):
        self.protocolo = 'ip'
        self.ip = '192.168.0.1'
        self.Enlace = Enlace()

class Enlace():
    def __init__(self):
        self.enderecoMac = '255.255.255.255'
        self.Fisica = Fisica()

class Fisica():
        def __init__(self):
            self.protocolo = 'tcp'





def main():
     a = Aplicacao  ('Palmeiras n tem mundial')
     print ('', a.Mensagem)
     print ('Aplicacao protocolo ', a.protocolo)
     print ('Apresentacao protocolo', a.Apresentacao.protocolo)
     print ('Sessao protocolo', a.Apresentacao.Sessao.protocolo)
     print ('Transporte protocolo', a.Apresentacao.Sessao.Transporte.protocolo)
     print ('Rede protocolo', a.Apresentacao.Sessao.Transporte.Rede.protocolo)
     print ('Rede protocolo', a.Apresentacao.Sessao.Transporte.Rede.ip)
     print ('Enlace protocolo', a.Apresentacao.Sessao.Transporte.Rede.Enlace.enderecoMac)
     print ('Fisica protocolo', a.Apresentacao.Sessao.Transporte.Rede.Enlace.Fisica.protocolo)




main()










