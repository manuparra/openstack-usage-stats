# openstack-usage-stats

**OpenStack usage stats selected by date range**

This is a mini-tool to download the usage statistics (RAM, CPU, DISK) of all OpenStack instances at all times (created, deleted, shelved, ...) in a time range.

**Run:**

``python osus.py show -u <username> -p "<password>" -nv "<version>" -pn "<project_name>" -au "<auth_>"``

**Example:**

``python osus.py show -u mparra -p "mipassXXX" -nv "2.1" -pn "my_project_a" -au "https://auth"``

**Ad-hoc SRC:**

``python osus.py show -u "mparra" -p "mipassXXX" -nv "2.1" -pn "spsrc" -au "https://spsrc-openstack.iaa.csic.es:5000"``

**Output format**

``{'tenant_id': 'bd56a02429374556bbd43d325f351ea3', 
   'server_usages': 
       [{'hours': 2482.4701032541666, 
         'flavor': 'multihub.c10m24', 
         'instance_id': '0b1f6831-444f-49eb-af2b-c2dd70c155ea', 
         'name': 'multihub-kg2egzpbkmet-master-0', 
         'tenant_id': 'bd56a02429374556bbd43d325f351ea3', 
         'memory_mb': 24576, 
         'local_gb': 50, 
         'vcpus': 10, 
         'started_at': '2021-02-12T16:52:33.000000', 
         'ended_at': None, 
         'state': 'active', 
         'uptime': 13023339},
         ...],
   'total_local_gb_usage': 2163405.358809722, 
   'total_vcpus_usage': 388621.4912849582, 
   'total_memory_mb_usage': 1377455593.4289408, 
   'total_hours': 39070.38630301945, 
   'start': '2021-04-01T00:00:00.000000', 
   'stop': '2021-07-13T10:28:12.371715'
  }
``
