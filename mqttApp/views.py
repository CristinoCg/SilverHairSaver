from django.shortcuts import render
import paho.mqtt.client as mqttClient
import json
import logging
import asyncio

#logging.disable(logging.WARNING)

logging.basicConfig(level=logging.DEBUG,format='%(levelname)s - %(asctime)s - %(message)s')


conteudo = ''
# Create your views here.
def HomePageView(request):
    
    async def cliente_assincrono():
        
        cliente = mqttClient.Client('django_client')

        
        def on_connect(client, userdata, flags, rc):
            if rc==0:
                client.connected_flag=True #set flag
                logging.debug("connected OK")
            else:
                print("Bad connection Returned code=",rc)
            
        def on_message(client, userdata, message):
            global conteudo
            conteudo = str(message.payload.decode('utf-8'))
            ponto = conteudo.find(':') + 1
            if message.retain:
                ...
            else:
                ...
            logging.debug(f'Valor de conteudo, dentor do message:{conteudo[ponto:]}')
            logging.debug(str(message.payload.decode('utf-8')))
            return render(request, 'home.html',{'conteudo': conteudo[ponto:]})
            

        def on_subscribe(client, userdata, mid, granted_qos):
            logging.debug(f'Resultado:{userdata}')
            
            
        def on_disconnect(client, userdata, rc=0):
            client.loop_stop()
    
        broker = 'broker.hivemq.com'#'afdf7a62ec4f41598f7116d5ad52aa26.s1.eu.hivemq.cloud'
        porta = 1883#8883
        
        cliente.on_connect = on_connect
        cliente.on_message = on_message
        cliente.on_disconnect = on_disconnect
        cliente.on_subscribe = on_subscribe
        
        
        
        
        try:
            cliente.connect(broker,porta)
            print('Conectou')
            cliente.subscribe('teste/')
            cliente.loop_start()
        except Exception as exception:
            print('Chegou até aqui', exception)
            return render(request, 'home.html',{'conteudo': 'Não funcionou, ainda:)'})

    #print(conteudo)  
    async def main():
        tarefa = asyncio.create_task(cliente_assincrono())    
    asyncio.run(main())
    return render(request, 'home.html',{'conteudo': conteudo})



    
    

  
        
