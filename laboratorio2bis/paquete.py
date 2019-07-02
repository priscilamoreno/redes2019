import math


class Packet:
    def __init__(self, source, receiver, data):
        self.source = source
        self.receiver = receiver
        self.checksum = 0
        self.long = len(data) + 8
        self.data = data

    def set_checksum(self, new_checksum):
        self.checksum = new_checksum

    def get_source(self):
        return self.source

    def get_receiver(self):
        return self.receiver

    def get_long(self):
        return self.long

    def get_checksum(self):
        return self.checksum

    def get_data(self):
        return self.data

def complement_one(number):
    num_bits = int(math.log2(number)) + 1
    complement = ((0b1 << num_bits) - 1) ^ number
    return complement

def calculate_checksum(packet):
    sum_aux = packet.get_source() + packet.get_receiver()
    sum_aux += packet.get_long() + packet.get_checksum()
    result = complement_one(sum_aux)
    return result
