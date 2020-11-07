# -*- coding: utf-8 -*-
import struct

class socket_wrapper:

    def send_with_len(self, data):
        self.send_socket(struct.pack('>I', len(data)))
        self.send_socket(data)

    def read_with_len(self):
        length_bytes = self.read_socket(4)
        length = struct.unpack('>I', length_bytes)[0]
        return self.read_socket(length)

    def read_socket(self, should_read):
        buf = []
        total_read = 0
        while total_read < should_read:
            left_to_read = should_read - total_read
            curr_recv = self.socket_obj.recv(left_to_read)
            total_read += len(curr_recv)
            buf.extend(curr_recv)
        return "".join(buf)

    def send_socket(self, data):
        index = 0
        while index < len(data):
            index = index + self.socket_obj.send(data[index:])

    def __init__(self, socket_obj):
        self.socket_obj = socket_obj