
ibm_container_vpc_cluster_worker_info -- Retrieve IBM Cloud 'ibm_container_vpc_cluster_worker' resource
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_vpc_cluster_worker' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  kube_version (False, str, None)
    kube version of the worker


  pool_name (False, str, None)
    worker pool name


  network_interfaces (False, list, None)
    NA


  resource_group_id (False, str, None)
    ID of the resource group.


  worker_id (True, str, None)
    ID of the worker


  cluster_name_id (True, str, None)
    Name or ID of the cluster


  pool_id (False, str, None)
    worker pool id


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  flavor (False, str, None)
    flavor of the worker


  state (False, str, None)
    State of the worker


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

