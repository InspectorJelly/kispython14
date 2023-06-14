import struct


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


class BinaryReader:
    def __init__(self, stream, offset, order="<"):
        self.stream = stream
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = struct.calcsize(pattern)
        data = struct.unpack_from(self.order +
                                  pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_a(reader):
    a1 = read_b(reader)
    a2 = reader.read(Types.uint32)
    a3 = read_e(reader)
    a4 = reader.read(Types.int16)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4)


def read_b(reader):
    c_size = reader.read(Types.uint16)
    c_offset = reader.read(Types.uint32)
    c_reader = reader.jump(c_offset)
    b1 = [read_c(c_reader) for _ in range(c_size)]
    b2 = b''.join([reader.read(Types.char) for _ in range(6)]).decode('utf-8')
    b3 = reader.read(Types.uint8)
    b4 = read_d(reader)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4)


def read_c(reader):
    c1 = reader.read(Types.int64)
    c2 = reader.read(Types.int32)
    return dict(C1=c1, C2=c2)


def read_d(reader):
    d1 = reader.read(Types.uint8)
    d2_size = reader.read(Types.uint16)
    d2_offset = reader.read(Types.uint32)
    d2_reader = reader.jump(d2_offset)
    d2 = [d2_reader.read(Types.int8) for _ in range(d2_size)]
    d3 = [reader.read(Types.uint16) for _ in range(4)]
    d4 = [reader.read(Types.int16) for _ in range(8)]
    d5 = reader.read(Types.int16)
    d6 = reader.read(Types.uint64)
    d7 = reader.read(Types.int8)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7)


def read_e(reader):
    e1 = reader.read(Types.float)
    e2 = reader.read(Types.int32)
    return dict(E1=e1, E2=e2)


SIGNATURE_OFFSET = 5


def main(stream):
    return read_a(BinaryReader(stream, SIGNATURE_OFFSET))
