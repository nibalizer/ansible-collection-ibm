#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_vpc_cluster_info
short_description: Retrieve IBM Cloud 'ibm_container_vpc_cluster' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_container_vpc_cluster' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.4.0
    - Terraform v0.12.20

options:
    crn:
        description:
            - CRN of resource instance
        required: False
        type: str
    status:
        description:
            - The status of the cluster master
        required: False
        type: str
    worker_count:
        description:
            - Number of workers
        required: False
        type: int
    workers:
        description:
            - NA
        required: False
        type: list
        elements: str
    private_service_endpoint:
        description:
            - NA
        required: False
        type: bool
    private_service_endpoint_url:
        description:
            - NA
        required: False
        type: str
    kube_version:
        description:
            - NA
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    ingress_hostname:
        description:
            - NA
        required: False
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    albs:
        description:
            - NA
        required: False
        type: list
        elements: dict
    ingress_secret:
        description:
            - NA
        required: False
        type: str
    public_service_endpoint_url:
        description:
            - NA
        required: False
        type: str
    health:
        description:
            - NA
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    cluster_name_id:
        description:
            - Name of the cluster
        required: True
        type: str
    worker_pools:
        description:
            - NA
        required: False
        type: list
        elements: dict
    master_url:
        description:
            - NA
        required: False
        type: str
    tags:
        description:
            - NA
        required: False
        type: list
        elements: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    alb_type:
        description:
            - NA
        required: False
        type: str
        default: all
    public_service_endpoint:
        description:
            - NA
        required: False
        type: bool
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('cluster_name_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'crn',
    'status',
    'worker_count',
    'workers',
    'private_service_endpoint',
    'private_service_endpoint_url',
    'kube_version',
    'resource_crn',
    'resource_group_name',
    'ingress_hostname',
    'resource_group_id',
    'albs',
    'ingress_secret',
    'public_service_endpoint_url',
    'health',
    'resource_controller_url',
    'resource_status',
    'cluster_name_id',
    'worker_pools',
    'master_url',
    'tags',
    'resource_name',
    'alb_type',
    'public_service_endpoint',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    crn=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    worker_count=dict(
        required=False,
        type='int'),
    workers=dict(
        required=False,
        elements='',
        type='list'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    private_service_endpoint_url=dict(
        required=False,
        type='str'),
    kube_version=dict(
        required=False,
        type='str'),
    resource_crn=dict(
        required=False,
        type='str'),
    resource_group_name=dict(
        required=False,
        type='str'),
    ingress_hostname=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    albs=dict(
        required=False,
        elements='',
        type='list'),
    ingress_secret=dict(
        required=False,
        type='str'),
    public_service_endpoint_url=dict(
        required=False,
        type='str'),
    health=dict(
        required=False,
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    cluster_name_id=dict(
        required=True,
        type='str'),
    worker_pools=dict(
        required=False,
        elements='',
        type='list'),
    master_url=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    resource_name=dict(
        required=False,
        type='str'),
    alb_type=dict(
        default='all',
        type='str'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_container_vpc_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.4.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
