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

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import testinfra.modules.base

modules = {
    "addr": "addr:Addr",
    "ansible": "ansible:Ansible",
    "command": "command:Command",
    "docker": "docker:Docker",
    "podman": "podman:Podman",
    "environment": "environment:Environment",
    "file": "file:File",
    "group": "group:Group",
    "interface": "interface:Interface",
    "iptables": "iptables:Iptables",
    "mount_point": "mountpoint:MountPoint",
    "package": "package:Package",
    "pip": "pip:Pip",
    "pip_package": "pip:PipPackage",
    "process": "process:Process",
    "puppet_resource": "puppet:PuppetResource",
    "facter": "puppet:Facter",
    "salt": "salt:Salt",
    "service": "service:Service",
    "socket": "socket:Socket",
    "sudo": "sudo:Sudo",
    "supervisor": "supervisor:Supervisor",
    "sysctl": "sysctl:Sysctl",
    "system_info": "systeminfo:SystemInfo",
    "user": "user:User",
    "block_device": "blockdevice:BlockDevice",
}


def get_module_class(name: str) -> type["testinfra.modules.base.Module"]:
    modname, classname = modules[name].split(":")
    modname = ".".join([__name__, modname])
    module = importlib.import_module(modname)
    return getattr(module, classname)  # type: ignore[no-any-return]
