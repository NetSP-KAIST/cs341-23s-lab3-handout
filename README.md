# Lab 3: Building Your Own Network with SDN

## Content

- [bootstrap.sh](bootstrap.sh): Setup Mininet and POX controller for VM
- [controller.py](controller.py): POX controller, working as wrapper of `route.py`
- [dump.py](dump.py): Dumps network topology to `/tmp/net.json`
- **[graph.py](graph.py)**: Generate random network topology (Lab 5)
- **[route.py](route.py)**: Compute routing rules, pushing them to switches (Lab 2,3,4)
- [test.py](test.py): Test implementation of logic, opening Mininet CLI
- **[topology.py](topology.py)**: Generate Mininet topology from given network structure (Lab 1)
- [Vagrantfile](Vagrantfile): Base Vagrantfile for generating VM