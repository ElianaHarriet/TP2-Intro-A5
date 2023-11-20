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
Antes de probar la topología debemos asegurarno de levantar el controlador con el siguiente comando

```bash
python3 pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning controller
```

Luego si podremos correr nuestra topologia:

```bash
sudo mn --custom ./topology.py --topo MyTopo,n=2 --mac --arp -x --switch ovsk --controller remote
```

## Tests

Iperf







