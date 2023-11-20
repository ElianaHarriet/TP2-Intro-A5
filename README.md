# TP2-Intro-A5
TP N°2: Software-Defined Networks - OpenFlow

## Integrantes
- [105103 - Franco Gazzola](https://github.com/franco-jyq)
- [106010 - Federico Martín Valsagna Indri](https://github.com/FedericoValsagna)
- [107205 - Eliana Harriet](https://github.com/ElianaHarriet)
- [108026 - Tomas Emanuel](https://github.com/tomasemanuel)
- [108193 - Tomás González](https://github.com/tomasgonzz)
- [101640 - Ramos Federico](https://github.com/RamosFe)


## Dependencias

Python  (https://www.python.org/downloads/)

Mininet & Openswitch (http://mininet.org/download/)

```bash
sudo apt-get install mininet
```
```bash
sudo apt-get install openvswitch-switch
```
```bash
sudo service openvswitch-switch start
```

Xterm

```bash
sudo apt install xterm
```

## Ejecución
Antes de probar la topología debemos asegurarnos de levantar el controlador con el siguiente comando

```bash
python3 pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning controller
```

Luego si podremos correr nuestra topologia:

```bash
sudo mn --custom ./topology.py --topo MyTopo,n=2 --mac --arp -x --switch ovsk --controller remote
```

## Tests

Iperf

La primer prueba consiste en validar que las peticiones hacia el puerto 80 son filtradas por el firewall

### Para establecer una conexión TCP sobre el puerto 80 desde el host1 hacia el host3

En la interfaz del host 3 indicamos que queremos inciar un servidor que escuche en el puerto 80
```bash
iperf -s -p 80
```
En la interfaz del host1 indicamos que queremos iniciar un cliente y hacer un request hacia el host 3 hacia el puerto 80
```bash
iperf -c 10.0.0.3 -p 80
```
Validamos que a la interfaz del host 3 no arribo ningun mensaje.










