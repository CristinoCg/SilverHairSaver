from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import paho.mqtt.client as mqttClient
import json
import logging
import asyncio
from random import choice

#logging.disable(logging.WARNING)
logging.basicConfig(level=logging.DEBUG,format='%(levelname)s - %(asctime)s - %(message)s')
lista = list('BROWNFOX')
conteudo = ''
context = {'/batimento':'','/temperatura':'','/oxigenio':'','/localizacao':''}
flag = {'/batimento':False,'/temperatura':False,'/oxigenio':False,'/localizacao':False}
# Create your views here.
def HomePageView(request): 
    return render(request, 'home.html',{'conteudo': context}) 


def BrokerView(request):
    global lista, flag
    response_path = request.path
#    logging.debug(f'Res:{response_path}')
    async def cliente_assincrono():
        
        cliente = mqttClient.Client('django_client')      
        def on_connect(client, userdata, flags, rc):
            if rc==0:
                client.connected_flag=True #set flag
                logging.debug("connected OK")
            else:
                print("Bad connection Returned code=",rc)
            
        def on_message(client, userdata, message):
            global conteudo, context
            conteudo = str(message.payload.decode('utf-8'))
            #ponto = conteudo.find(':') + 1
            context[response_path] = conteudo
            if message.retain:
                logging.debug('This one is retained')
            else:
                logging.debug(f'Message:{context[response_path]} - URL{response_path}')

        def on_subscribe(client, userdata, mid, granted_qos):
            logging.debug(f'Dados do usuário subscribe:{userdata}')
                   
        def on_disconnect(client, userdata, rc=0):
            client.loop_stop()

        
    
        broker = 'broker.hivemq.com'
        porta = 1883
        
        cliente.on_connect = on_connect
        cliente.on_message = on_message
        cliente.on_disconnect = on_disconnect
        cliente.on_subscribe = on_subscribe
        '''if not flag[response_path]:
            flag[response_path] = True'''
        try:
            cliente.connect(broker,porta)
            logging.debug(f'Res:{response_path}')
            cliente.subscribe(response_path)
            cliente.loop_start()
        except Exception as exception:
            print('Chegou até aqui', exception)
            return HttpResponse('Nada')
            
    
    async def main():
        tarefa = asyncio.create_task(cliente_assincrono())    
    asyncio.run(main())

    return HttpResponse(context[response_path])

@csrf_protect
def BatimentoView(request):
    logging.debug(f'{context}')
    return BrokerView(request)

@csrf_protect
def TemperaturaView(request):
    logging.debug(f'{context}')
    return BrokerView(request)

@csrf_protect
def OxigenioView(request):
    logging.debug(f'{context}')
    return BrokerView(request)

@csrf_protect
def LocalizacaoView(request):
    logging.debug(f'{context}')
    return BrokerView(request)

def ClienteView(request):
    return render(request, 'paciente.html')
    


    
    

  
        
