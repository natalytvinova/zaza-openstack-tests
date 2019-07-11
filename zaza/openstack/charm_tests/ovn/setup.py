# Copyright 2019 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Code for configuring OVN."""

import zaza.charm_lifecycle.utils
import zaza.openstack.charm_tests.vault.setup as vault_setup


def initialize_vault():
    """Initialize vault and wait for OVN charms to pick up cert and idle."""
    vault_setup.auto_initialize(validation_application=None)

    # Our expected workload status will change after we have successfully
    # joined the certificates relation
    test_config = zaza.charm_lifecycle.utils.get_charm_config()
    del test_config['target_deploy_status']['ovn']
    zaza.model.wait_for_agent_status()
    zaza.model.wait_for_application_states()
