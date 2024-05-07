# remote_management.py

import device_management

class DeviceConfig:
    def __init__(self, id, firmware_version):
        self.id = id
        self.firmware_version = firmware_version

def update_firmware(device_id, new_version):
    for device in device_management.inventory:
        if device.id == device_id:
            device.firmware_version = new_version
            break
