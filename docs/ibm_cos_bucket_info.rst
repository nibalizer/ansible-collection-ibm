
ibm_cos_bucket_info -- Retrieve IBM Cloud 'ibm_cos_bucket' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_cos_bucket' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  storage_class (False, str, None)
    NA


  bucket_name (True, str, None)
    NA


  bucket_type (True, str, None)
    NA


  resource_instance_id (True, str, None)
    NA


  crn (False, str, None)
    CRN of resource instance


  key_protect (False, str, None)
    CRN of the key you want to use data at rest encryption


  region_location (False, str, None)
    NA


  bucket_region (True, str, None)
    NA


  single_site_location (False, str, None)
    NA


  cross_region_location (False, str, None)
    NA


  s3_endpoint_public (False, str, None)
    Public endpoint for the COS bucket


  s3_endpoint_private (False, str, None)
    Private endpoint for the COS bucket


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

