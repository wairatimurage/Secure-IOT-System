class Device:
    def __init__(self, id, status):
        self.id = id
        self.status = status

inventory = []

def provision_device(id):
    new_device = Device(id, 'active')
    inventory.append(new_device)

def decommission_device(id):
    for device in inventory:
        if device.id == id:
            device.status = 'decommissioned'
            break
