import textwrap

FILE_NAME="test.bin"

def to_binary(var):
    print("Write var to disk in binary format")
    f = open("test.bin", "a")
    bin_var = format(var, 'b').zfill(8)
    f.write(bin_var)
    f.close()

def from_binary():
    print("Reading  binary file to mem")
    f = open("test.bin")
    var = f.read()
    f.close()

    n = 8 # how many characters in each variable
    split_list = textwrap.wrap(var, n) # make a list for every n elements (bits) per member
    print('.'.join(split_list))

if __name__ == "__main__":
    f = open("test.bin", 'w')
    f.close()

    ip_Address = "192.186.0.1"

    [to_binary(int(num)) for num in ip_Address.split(".")]
    from_binary()


class Packet:
    def __init__(self, source_ip, dest_ip, payload):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.payload = payload

    def __str__(self):
        return f"Packet from {self.source_ip} to {self.dest_ip} with payload: {self.payload}"