import platform
import hashlib

def extract_hardware_id():
    # Gather system information
    system_info = platform.uname()
    processor = system_info.processor
    system = system_info.system
    node = system_info.node
    release = system_info.release
    version = system_info.version
    machine = system_info.machine

    # Combine the information into a unique identifier
    hardware_string = f"{processor}{system}{node}{release}{version}{machine}"
    
    # Hash the identifier to make it more secure
    hardware_id = hashlib.sha256(hardware_string.encode()).hexdigest()

    return hardware_id

if __name__ == "__main__":
    hardware_id = extract_hardware_id()
    print("Hardware ID:", hardware_id)
