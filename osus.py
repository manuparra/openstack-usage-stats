#!/bin/env python

import argparse
from novaclient import client
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
import datetime
import json


def connect_nova_api(user=None,password=None,nova_api=None,project_name=None,auth_url=None):
  loader = loading.get_plugin_loader('password')
  auth = loader.load_from_options(auth_url=auth_url,
                                 username=user,
                                 password=password,
                                 project_name=project_name, 
                                 user_domain_id="default", 
                                 project_domain_id="default"
                                    )
  sess = session.Session(auth=auth)
  nova = client.Client(nova_api, session=sess)
  return nova

def show_usage(n=None,start_date=None,end_date=None):
  instances_summary=n.usage.list(detailed=True,start=datetime.datetime(2021,4,1),end=datetime.datetime.now())
  #print(instances_summary[0]._info['start']," to ", instances_summary[0]._info['stop'])
  #print("total_local_gb_usage:",instances_summary[0]._info['total_local_gb_usage'])
  #print("total_vcpus_usage:",instances_summary[0]._info['total_vcpus_usage'])
  #print("total_memory_mb_usage:",instances_summary[0]._info['total_memory_mb_usage'])
  #print("total_hours:",instances_summary[0]._info['total_hours'])
  #for s in instances_summary[0]._info['server_usages']:
  #    print("%s %s")
  print (instances_summary[0]._info)

def main():
    parser = argparse.ArgumentParser(description='Get OpenStack usage stats')
    parser.add_argument(
        'action', choices=['show', 'store'], help='Show and Store Openstack usage data')
    parser.add_argument(
        '-u', '--user', required=True, type=str, help='Username')
    parser.add_argument(
        '-p', '--password', required=True, type=str, help='User password')
    parser.add_argument(
        '-nv', '--nova_api', required=True, type=str, help='Nova API version')
    parser.add_argument(
        '-pn', '--project_name', required=True, type=str, help='Project name')
    parser.add_argument(
        '-au', '--auth_url', required=True, type=str, help='Authentication URL')
    parser.add_argument(
        '-sd', '--start_date', required=False, type=str, help='Start date')
    parser.add_argument(
        '-ed', '--end_date', required=False, type=str, help='End date')
    
    args = parser.parse_args()

    if args.action == "show":
      cn=connect_nova_api(user=args.user,
                          password=args.password,
                          nova_api=args.nova_api,
                          project_name=args.project_name,
                          auth_url=args.auth_url)
      show_usage(n=cn,
              start_date=args.start_date,
              end_date=args.end_date)

    elif args.action == "store":
      print(args.user)


if __name__ == "__main__":
    main()
