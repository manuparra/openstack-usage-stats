# openstack-usage-stats

**OpenStack usage stats selected by date range**

This is a mini-tool to download the usage statistics (RAM, CPU, DISK) of all OpenStack instances at all times (created, deleted, shelved, ...) in a time range.

**Run:**

``python osus.py show -u <username> -p "<password>" -nv "<version>" -pn "<project_name>" -au "<auth_>"``

**Example:**

``python osus.py show -u mparra -p "mipassXXX" -nv "2.1" -pn "my_project_a" -au "https://auth"``

**Ad-hoc SRC:**

``python osus.py show -u "mparra" -p "mipassXXX" -nv "2.1" -pn "spsrc" -au "https://spsrc-openstack.iaa.csic.es:5000"``


