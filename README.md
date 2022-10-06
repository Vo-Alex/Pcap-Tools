# Pcap Tools

Pcap tools is a set of python scripts to analyze pcap files.

## trafficMatrix.py

Create a traffic matrix from the pacp trace.

## serviceDependencies.py

Create a dependency graph between services and hosts from the pcap trace.

# Installation

## Create a venv (if you want it)

```
python -m venv env
source ./env/bin/activate
```

## Install python dependencies 

```
pip -r requirements.txt
```

## Install system dependencies 

### Debian Ubuntu

```
sudo apt install graphviz
```

### Fedora

```
sudo dnf install graphviz
```