from utils import get_input


def detect_start_markers(datastream_buffer: str, unique_len=4) -> int:
    for i in range(unique_len,len(datastream_buffer)+1):
        packet_start = datastream_buffer[i-unique_len:i]
        if len(packet_start) == len(set(packet_start)):
            return i
    return 0



if __name__ == "__main__":
    path = 'data/06.txt'
    data = get_input(path)

    # First-part
    print(detect_start_markers(data[0]))

    # Second-part
    print(detect_start_markers(data[0], 14))
